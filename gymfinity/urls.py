from django.conf.urls import url, include
from django.contrib import admin

from registration.views import HomeView, AddGymView, FindGymView, LandingView, GymDetailView, UserDetailView, SubscribeView

urlpatterns = [
	url(r'^subscribe/', SubscribeView.as_view()),
	url(r'^userdetail/', UserDetailView.as_view()),
	url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
	url(r'^gymdetail/(?P<pk>[-\w]+)$', GymDetailView.as_view()),
	url(r'^accounts/profile', LandingView.as_view()),
	url(r'^accounts/', include('allauth.urls')),
	url(r'^find/', FindGymView.as_view()),
	url(r'^partner/', AddGymView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
]
