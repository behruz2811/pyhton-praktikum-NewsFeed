from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# Create your views here.
def UserLoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Muvaffaqiyatli login amalga oshirildi!')
                else:
                    return HttpResponse("Sizning profilingiz faol holatda emas!")

            else:
                return HttpResponse('Bunday foydalanuvchi topilmadi!')
        else:
            return HttpResponse('Foydalanuvchi nomi yaroqsiz!')
    # GET method
    else:
        form = LoginForm

    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)


def DashboardView(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'pages/user_profile.html', context)
