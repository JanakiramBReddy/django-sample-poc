from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    form_class = RegisterForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'welcome {username},your account has created successfully')
            return redirect('login')

        else:
            form = form_class()
    return render (request,'users/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request,'users/profile.html')



