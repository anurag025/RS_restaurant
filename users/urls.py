from django.conf.urls import url
import users.views as views
urlpatterns = [
    # master record urls
    url(r'^dashboard', views.Dashboard.as_view(), name='v2-all-cities')
]