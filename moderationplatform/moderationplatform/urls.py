from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path(
        'v1/moderation/', 
        csrf_exempt(GraphQLView.as_view(graphiql=True))
    ),
    path('admin/', admin.site.urls),
]
