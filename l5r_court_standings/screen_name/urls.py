from django.conf.urls import url

from .views import registered_names
from .views import register_new_name

urlpatterns = [
    url(r'^$', registered_names.show_registered_names, name='registered_names'),
    url(r'^new/', register_new_name.post, name='new_username'),
    url(r'^register/', register_new_name.register, name='register_username')
]
