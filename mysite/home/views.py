from django.shortcuts import render,redirect
from django.views import View
from django.conf import settings
from .forms import UserRegistrationForm
# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations

class HomeView(View):
    def get(self, request) :
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed' : settings.INSTALLED_APPS,
            'islocal' : islocal
        }
        return render(request, 'home/main.html', context)
 
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            print("inside if register")
            form.save()
            print("after saving data")
            return redirect('login')

    else:
        form=UserRegistrationForm()
    return render(request,'registration/registeration.html',{'form':form})
