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
