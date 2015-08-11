from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^clients/$', views.clients, name='client-list'),
    url(r'^clients/edit/(?P<pk>\d+)/$', views.client_edit, name='client-edit'),
    url(r'^clients/(?P<pk>\d+)/$', views.client_detail, name='client-detail'),
    url(r'^entries/$', views.entries, name='entry-list'),
    url(r'^projects/$', views.projects, name='project-list'),
    url(r'^projects/edit/(?P<pk>\d+)/$', views.project_edit, name='project-edit'),
 ]
