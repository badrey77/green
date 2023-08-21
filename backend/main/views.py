
from django.shortcuts import render
from django.views import View

from main.forms import HomeSearchForm
from main.models import Restaurant


class Home(View):
    @staticmethod
    def get(request):
        if request.method == 'GET' and 'search_query' in request.GET:
            data = Restaurant.objects.all()
            return render(request, template_name='./main/home.html',
                          context={'title': 'Welcome ! Can I help you ?', 'results': data })

        form = HomeSearchForm()
        return render(request, template_name='./main/home.html', context={'form': form, 'title': 'Welcome ! Can I help you ?'})
