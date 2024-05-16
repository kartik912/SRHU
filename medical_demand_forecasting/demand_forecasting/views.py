from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from demand_forecasting import predict
def index(request):
    list1, list2, list3, list4 = predict.predict_class.pred()
    return render(request, 'front.html')
def summer(request):
    return render(request, 'summer.html')

def winter(request):
    return render(request, 'winter.html')

def autumn(request):
    return render(request, 'autumn.html')

def rainy(request):
    return render(request, 'rainy.html')
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passw = request.POST.get('password')
        
        if username=='kartik' and passw=='1234':
            return redirect('index')
        else:
            return HttpResponse("Your username or password is incorrect")
    return render(request, 'login.html')

def admin_page(request):
    return render(request, 'admin.html')

# def register_page(request):
#     if request.method == 'POST':
#         print(request.POST)
#         uname = request.POST.get('username')
#         password = request.POST.get('password')
#         conpassword = request.POST.get('confirmPassword')
#         print(uname, password)
#         if password != conpassword :
#             return HttpResponse("Password not same")
#         else:
#             my_user = User.objects.create_user(uname,password)
#             my_user.save()
#             return redirect('login')
        

    # return render(request, 'register.html')