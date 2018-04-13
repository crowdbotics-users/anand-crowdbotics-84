from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-shop', 'url': 'http://pypi.python.org/pypi/django-shop/0.11.3'},
    ]
    context = {
        'title': 'anand-crowdbotics-84',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
