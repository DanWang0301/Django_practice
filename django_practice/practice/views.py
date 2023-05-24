from django.shortcuts import render

# Create your views here.
def hello_view(request):
    return render(request, 'home_page.html', {
        'data': "Lesson 1, make home page.",
    })