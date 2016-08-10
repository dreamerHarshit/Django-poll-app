from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_question/$',views.get_name,name='add_question'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/(?P<message>[a-z]+)/$', views.vote, name='vote'),
    url(r'^user_detail/$',views.view_name,name = 'user_detail'),
    url(r'^login_id/$',views.login_view,name ='login_id'),
    url(r'^sign_up/$',views.signup_view,name ='sign_up'),
    url(r'^log_out/$',views.logout_view,name = 'log_out'),

] 