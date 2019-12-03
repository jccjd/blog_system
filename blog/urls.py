from django.urls import path

from blog import views

urlpatterns = [
    path(r'', views.get_blogs),
    path(r'<int:blog_id>', views.get_details, name='detail')
]