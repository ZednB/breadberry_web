from django.shortcuts import render

from breadberry.models import Category, Position


def home(request):
    position = Position.objects.filter(is_popular=True)
    context = {'position': position}
    return render(request, 'breadberry/popular.html', context)


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


def salad_list(request):
    salad = Category.objects.filter(title='Салаты').first()
    if salad:
        salad = salad.position.all()
    else:
        salad = []
    context = {'salad_list': salad}
    return render(request, 'breadberry/salad_list.html', context)


def hot_list(request):
    hot = Category.objects.filter(title='Горячее').first()
    if hot:
        hot = hot.position.all()
    else:
        hot = []
    context = {'hot_list': hot}
    return render(request, 'breadberry/hot_list.html', context)


def saj_list(request):
    saj = Category.objects.filter(title='Садж').first()
    if saj:
        saj = saj.position.all()
    else:
        saj = []
    context = {'saj_list': saj}
    return render(request, 'breadberry/saj_list.html', context)


def steak_list(request):
    steak = Category.objects.filter(title='Стейки').first()
    if steak:
        steak = steak.position.all()
    else:
        steak = []
    context = {'steak_list': steak}
    return render(request, 'breadberry/steak_list.html', context)


def paste_list(request):
    paste = Category.objects.filter(title='Пасты').first()
    if paste:
        paste = paste.position.all()
    else:
        paste = []
    context = {'paste_list': paste}
    return render(request, 'breadberry/paste_list.html', context)


def fastfood_list(request):
    fastfood = Category.objects.filter(title='Фастфуд').first()
    if fastfood:
        fastfood = fastfood.position.all()
    else:
        fastfood = []
    context = {'fastfood_list': fastfood}
    return render(request, 'breadberry/fastfood_list.html', context)
