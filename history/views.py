from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from history.models import History


class MyHistory(ListView):
    model = History
    template_name = 'pages/history.html'
    context_object_name = 'user_history'

    def get_queryset(self):
        search = self.request.GET.get('search', None)
        if search is None:
            queryset = self.model.objects.filter(
                user=self.request.user
            )
        else:
            queryset = self.model.objects.filter(
                video__title__icontains=search
            )
        return queryset


@require_POST
def pause_history(request):
    data = {'state': False}
    if request.user.is_authenticated:
        data.update({'state': True})
    return JsonResponse(data=data)


@require_POST
def delete_history(request):
    data = {'state': False}
    if request.user.is_authenticated:
        items = History.objects.filter(user=request.user)
        if items.exists():
            items.delete()
            data.update({'state': True})
    return JsonResponse(data=data)


@require_POST
def delete_from_history(request):
    data = {'state': False}
    if request.user.is_authenticated:
        item_id = request.POST.get('history_id', None)
        if item_id is not None: 
            item = get_object_or_404(History, id=item_id)
            item.delete()
            data.update({'state': True})
    return JsonResponse(data=data)
        
