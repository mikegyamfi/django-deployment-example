from django.conf.urls import url
from template_app import views

app_name = 'template_app'

urlpatterns = [
    url('other/', views.other, name='other'),
    url('relative/', views.relative, name='relative')
]