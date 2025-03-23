from django.shortcuts import render

from breadberry.models import Category, Position


def home(request):
    position = Position.objects.filter(is_popular=True)
    context = {'position': position}
    return render(request, 'breadberry/base.html', context)


def breakfast_list(request):
    breakfast = Category.objects.filter(title='Завтраки').first()
    if breakfast:
        breakfast = breakfast.position.all()
    else:
        breakfast = []
    context = {'breakfast': breakfast}
    return render(request, 'breadberry/breakfast_list.html', context)


def drink_list(request):
    drink = Category.objects.filter(title='Напитки').first()
    if drink:
        drink = drink.position.all()
    else:
        drink = []
    context = {'drink': drink}
    return render(request, 'breadberry/drink_list.html', context)
