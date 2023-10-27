from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import Menu , MenuItem , ChildrenElement



def main_view(request:HttpRequest)->HttpResponse:
    template_name = 'main/index.html'
    menus = Menu.objects.all()
    return render(
        request=request,
        template_name=template_name,
        context={'menus':menus}
    )


def menu_view(request:HttpResponse)->render:
    template_name = 'menu/menu.html'
    return render(
        template_name=template_name,
        request=request,
        context={}
    )

def current_menu(request:HttpRequest,menu_slug:str)->HttpResponse:
    template_name = 'menu/current_menu.html'
    menu_item :Menu = Menu.objects.get(slug = menu_slug)
    return render(
        request=request,
        template_name=template_name,
        context={'menu':menu_item}
    )

def current_item(request:HttpRequest,menu_slug:str,menu_item_slug:str)->HttpResponse:
    template_name = 'menu/current_menu_item.html'
    menu_item :MenuItem = MenuItem.objects.get(slug = menu_item_slug)
    menu : Menu = Menu.objects.get(slug= menu_slug)
    return render(
        request=request,
        template_name=template_name,
        context={
            'item':menu_item,
            'menu':menu
        }
    )

def current_child_item(request:HttpRequest,menu_slug,menu_item_slug,child_slug:str):
    template_name = 'menu/current_child.html'
    child_element: ChildrenElement = ChildrenElement.objects.get(
        slug = child_slug
    )
    return render(
        request=request,
        template_name= template_name,
        context={
            'child':child_element
        }
    )