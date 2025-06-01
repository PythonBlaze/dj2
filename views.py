from django.shortcuts import render

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

def index(request):
    # получаем название рецепта из GET-параметра
    recipe_name = request.GET.get('recipe')
    # по умолчанию — пустой словарь
    recipe = {}
    
    # если рецепт есть в DATA — берем его
    if recipe_name in DATA:
        recipe = DATA[recipe_name]
    
    # передаем в контекст
    context = {
        'recipe': recipe
    }
    
    # рендерим шаблон с контекстом
    return render(request, 'calculator/index.html', context)
