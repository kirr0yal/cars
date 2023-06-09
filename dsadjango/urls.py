from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path
from views_name import name
from market.views import show_cars, audi_purchase


def hello_world(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('audi', show_cars),
    path('buy_car/<int:id_>', audi_purchase),
    path('name', name)
]
