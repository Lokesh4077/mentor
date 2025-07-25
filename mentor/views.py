from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def details(request):
    return render(request, 'course-details.html')

def events(request):
    return render(request, 'events.html')

def footer(request):
    return render(request, 'footer.html')

def header(request):
    return render(request, 'header.html')

def pricing(request):
    return render(request, 'pricing.html')

def trainers(request):
    return render(request, 'trainers.html')

def starter(request):
    return render(request, 'starter-page.html')

def courses(request):
    return render(request, 'courses.html')