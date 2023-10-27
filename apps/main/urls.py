from django.urls import path 
from .views import (
    menu_view,
    main_view,
    current_menu,
    current_item,
    current_child_item
)


urlpatterns = [
    path('',main_view,name='main_view'),
    path('menu/',menu_view,name='menu_view'),
    path('menu/<slug:menu_slug>/',current_menu,name='current_menu'),
    path('menu/<slug:menu_slug>/<slug:menu_item_slug>/',current_item,name='current_item'),
    path('menu/<slug:menu_slug>/<slug:menu_item_slug>/<slug:child_slug>/',current_child_item,name='child_url')
]
