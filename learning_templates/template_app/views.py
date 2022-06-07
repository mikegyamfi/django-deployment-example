from django.shortcuts import render

# Create your views here.
def index(request):
    dict = {'text':'hello world', 'number':100}
    return render(request, 'template_app/index.html', context=dict)

def other(request):
    return render(request, 'template_app/other.html')

def relative(request):
    return render(request, 'template_app/rel_url.html')


