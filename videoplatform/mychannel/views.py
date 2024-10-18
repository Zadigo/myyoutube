from secrets import token_hex

from django.contrib import messages
from django.db import transaction
from django.http import Http404
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.base import View

from mychannel.choices import ChannelCategories
from mychannel.forms import CustomizationForm, UpdateChannelForm
from mychannel.models import UserChannel


class BaseDetailView(DetailView):
    model = UserChannel
    queryset = UserChannel.objects.all()
    context_object_name = 'channel'
    pk_url_kwarg = 'reference'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        reference = self.kwargs.get(self.pk_url_kwarg)
        if reference is not None:
            queryset = queryset.filter(reference=reference)

        if reference is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "reference in the URLconf." % self.__class__.__name__
            )

        try:
            video = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _(f"No {queryset.model._meta.verbose_name} found matching the query"))
        return video


class ChannelView(BaseDetailView):
    template_name = 'pages/channel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        channel = super().get_object()

        context['is_subscribed'] = False
        subscription = channel.subscribers.filter(
            username=self.request.user.username
        )
        if subscription.exists():
            context.update({'is_subscribed': True})

        return context


class CustomizeChannelView(UpdateView):
    model = UserChannel
    form_class = CustomizationForm
    context_object_name = 'form'
    template_name = 'pages/edit/channel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channel'] = self.get_object()
        return context

    def get_object(self, queryset=None):
        queryset = super().get_queryset()
        return queryset.get(reference=self.kwargs.get('reference'))


class ChannelVideosView(ListView):
    model = UserChannel
    template_name = 'pages/list/videos.html'
    context_object_name = 'videos'

    def _get_channel(self):
        return get_object_or_404(UserChannel, reference=self.kwargs.get('reference'))
        # return self.request.user.userchannel_set.get()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['userchannel'] = self._get_channel()
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        channel = self._get_channel()
        return channel.video_set.all()


class UploadVideoView(View):
    def get(self, request, *args, **kwargs):
        user_channel = get_object_or_404(UserChannel, user=request.user)
        context = {
            'channel': user_channel,
            'categories': [choice[-1] for choice in ChannelCategories.choices]
        }
        return render(request, 'pages/edit/upload.html', context=context)

    def post(self, request, **kwargs):
        data = {'state': False}

        title = request.POST.get('title')
        # category = request.POST.get('category', ChannelCategories.BEAUTY)
        description = request.POST.get('description')

        if title is not None and description is not None:
            video = request.FILES.get('new-video')
            user_channel = get_object_or_404(UserChannel, user=request.user)
            try:
                with transaction.atomic():
                    new_video = user_channel.video_set.create(
                        user=request.user,
                        reference=token_hex(nbytes=5),
                        title=title,
                        category=ChannelCategories.BEAUTY,
                        description=description,
                        video=video
                    )
            except Exception as e:
                messages.error(request, f'Could not upload video. {e.args}', extra_tags='alert-danger')
                data.update({'message': e.args})
            else:
                data.update({'state': True, 'url': new_video.get_absolute_url()})
        return JsonResponse(data=data)


class EditVideoView(UpdateView):
    model = UserChannel
    form_class = CustomizationForm
    context_object_name = 'form'
    template_name = 'pages/edit/video.html'


class ChannelsView(ListView):
    model = UserChannel
    template_name = 'pages/channels.html'
    context_object_name = 'channels'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            queryset = self.model.objects.filter(user=self.request.user)
            if queryset.exists():
                user_channel = queryset.get()
                context['has_existing_channel'] = True
                context['existing_channel_url'] = user_channel.get_absolute_url()
            else:
                context['has_existing_channel'] = False
        return context


@require_POST
@transaction.atomic
def subscribe(request, **kargs):
    data = {'state': False}
    channel_reference = request.POST.get('channel', None)
    if channel_reference is not None:
        channel = get_object_or_404(
            UserChannel, reference=channel_reference)
        channel.subscribers.add(request.user)
        data.update({'state': True})
    else:
        messages.error(
            request,
            "An error occured - SUB-RE",
            extra_tags='alert-danger'
        )
    return JsonResponse(data=data)


@require_POST
@transaction.atomic
def unsubscribe(request, **kargs):
    data = {'state': False}
    channel_reference = request.POST.get('channel', None)
    if channel_reference is not None:
        channel = get_object_or_404(
            UserChannel, reference=channel_reference)
        channel.subscribers.remove(request.user)
        data.update({'state': True})
    else:
        messages.error(
            request,
            "An error occured - SUB-RE",
            extra_tags='alert-danger'
        )
    return JsonResponse(data=data)



@require_POST
@transaction.atomic
def delete(request, **kwargs):
    pass


@require_POST
@transaction.atomic
def create_new_channel(request, **kwargs):
    data = {'state': False}
    if not request.user.is_authenticated:
        data.update({'url': '/admin/'})
        return JsonResponse(data=data, status=201)

    current_user = request.user
    has_channels = UserChannel.objects.filter(
        user=current_user,
    )
    if not has_channels.exists():
        new_channel = UserChannel.objects.create(
            reference=token_hex(nbytes=5),
            user=request.user,
            name=current_user.username.title(),
            description=f'Welcome to your new channel - {current_user.username}'
        )
        data.update({
            'state': True,
            'url': new_channel.get_absolute_url()
        })
        return JsonResponse(data=data)
    return JsonResponse(data=data)
