from django.contrib import admin
from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from .views import index,rating,fiveStar,fiveStar_again
urlpatterns = [
    path('', index),
    path('r', rating),
    path('f', fiveStar_again),
]
# + debug_toolbar_urls()