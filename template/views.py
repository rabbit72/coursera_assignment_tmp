from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def echo(request):
    method = request.method
    if request.method == "GET":
        params = request.GET
    elif request.method == "POST":
        params = request.POST
    statement = request.META.get("HTTP_X_PRINT_STATEMENT")
    return render(request, "echo.html", status=200, context={
        "statement": statement,
        "params": params,
        "method": method.lower(),
    })


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
