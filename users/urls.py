from django.conf.urls import url
import users.views as views
urlpatterns = [
    # master record urls
    url(r'^add', views.AddUser.as_view(), name='v2-all-cities')
]