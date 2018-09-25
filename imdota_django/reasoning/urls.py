from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'plays', views.PlayViewSet)
router.register(r'platforms', views.PlatformViewSet)


urlpatterns = [
    # path('', views.index, name='index'),
    # path('signin', views.signin, name='signin'),
    # path('signup', views.signup, name='signup'),
    # path('createeditor', views.createeditor, name='createeditor'),
    # path('bbsspider', views.bbsspider, name='bbsspider'),
    # path('playlist', views.playlist, name='playlist'),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
