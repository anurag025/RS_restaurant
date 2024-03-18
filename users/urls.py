from django.conf.urls import url
import users.views as views
urlpatterns = [
    # master record urls
    url(r'^user', views.User.as_view(), name='v2-all-cities')
]