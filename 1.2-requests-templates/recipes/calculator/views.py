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

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipes(request, dish):
    servings = request.GET.get('servings', 1)
    dish_list = ['omlet', 'pasta', 'buter']
    if dish in dish_list:
        if dish == 'omlet':
            context = {
                'recipe': {
                    'яйца, шт': 2 * int(servings),
                    'молоко, л': 0.1 * int(servings),
                    'соль, ч.л.': 0.5 * int(servings),
                }
            }

        if dish == 'pasta':
            context = {
                'recipe': {
                    'макароны, г': 0.3 * int(servings),
                    'сыр, г': 0.05 * int(servings),
                }
            }

        if dish == 'buter':
            context = {
                'recipe': {
                    'хлеб, ломтик': 1 * int(servings),
                    'колбаса, ломтик': 1 * int(servings),
                    'сыр, ломтик': 1 * int(servings),
                    'помидор, ломтик': 1 * int(servings),
                }
            }
    else:
        context = {}
    return render(request, 'calculator/index.html', context)
