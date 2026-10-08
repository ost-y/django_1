from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def index(request):
    return render(request, 'index.html')

def omlet(request):
    number_dish = int(request.GET.get('servings', 1))
    x = DATA['omlet']
    y = dict()
    for k, v in x.items():
        if number_dish:
            y[k] = v * number_dish


    result = "\n".join([f"{ingredient}: {amount}" for ingredient, amount in y.items()])
    return HttpResponse(result)

def pasta(request):
    number_dish = int(request.GET.get('servings', 1))
    x = DATA['pasta']
    y = dict()
    for k, v in x.items():
        if number_dish:
            y[k] = v * number_dish


    result = "\n".join([f"{ingredient}: {amount}\n" for ingredient, amount in y.items()])
    return HttpResponse(result)

def buter(request):
    number_dish = int(request.GET.get('servings', 1))
    x = DATA['buter']
    y = dict()
    for k, v in x.items():
        if number_dish:
            y[k] = v * number_dish


    result = "\n".join([f"{ingredient}: {amount}" for ingredient, amount in y.items()])
    return HttpResponse(result)