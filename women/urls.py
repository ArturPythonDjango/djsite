from django.urls import path, include, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000
    path('about/', about, name='about'),  # http://127.0.0.1:8000/about/
    # path('cats/<int:catid>/', categories),  # http://127.0.0.1:8000/cats/1/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
