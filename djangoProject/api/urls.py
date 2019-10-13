from django.conf.urls import url
import api.views as views

urlpatterns = [
    url(r'^testmodel2/$', views.TestFieldViewList.as_view(),
        name=views.TestFieldViewList.name),
    url(r'^testmodel2/(?P<pk>[0-9]+)/$', views.TestFieldViewDetails.as_view(),
        name=views.TestFieldViewDetails.name),

    url(r'^current-local/$', views.CurrentLocalDevicesViewList.as_view(),
        name=views.CurrentLocalDevicesViewList.name),
    url(r'^current-local/(?P<pk>[0-9]+)/$', views.CurrentLocalDevicesViewDetails.as_view(),
        name=views.CurrentLocalDevicesViewDetails.name),
]
