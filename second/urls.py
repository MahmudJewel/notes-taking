from django.urls import path
from . import views
from second.views import delete_note

urlpatterns= [
	path('', views.htmlfile, name='html'),
	
]
