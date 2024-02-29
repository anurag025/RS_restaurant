
from django.conf.urls import url
import views
urlpatterns = [
    # master record urls
    url(r'^add-item', views.AddItem.as_view(), name='v2-all-cities')]