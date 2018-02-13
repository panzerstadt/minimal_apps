from django.shortcuts import render

# Create your views here.
def show_app(request):
    return render(request, 'minimal_app/minimal_app_page.html')