from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers
from . import views, spider_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'plays', views.PlayViewSet)
router.register(r'platforms', views.PlatformViewSet)
router.register(r'studios', views.StudioViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'roles', views.CharacterViewSet)
router.register(r'tags', views.TagViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('createeditor', views.createeditor, name='createeditor'),

    path('spider_bbs', spider_views.spider_bbs, name='spider_bbs'),
    path('spider_baibian', spider_views.spider_baibian, name='spider_baibian'),
    path('spider_tiantian', spider_views.spider_tiantian, name='spider_tiantian'),
    path('spider_qu', spider_views.spider_qu, name='spider_qu'),


    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
