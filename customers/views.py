from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models.customer import Customer
from django.contrib.auth.hashers import check_password, make_password
from django.views import View


class LoginCustomer(View):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        if customer:
            if check_password(password, customer.password):
                messages.success(request, 'Successfully logged in...')
                request.session['email'] = customer.email
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid login credentials.')
                return render(request, 'customers/login.html')
        else:
            messages.error(request, 'Invalid login credentials.')
            return render(request, 'customers/login.html')

    def get(self, request):
        return render(request, 'customers/login.html')


class SignupCustomer(View):
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        password = make_password(password1)
        if check_password(password2, password):
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                password=password,
            )
            try:
                customer.save()
                messages.success(request, 'You have successfully registered.')
                return redirect('homepage')
            except IntegrityError:
                messages.error(request, 'Email id already exists!')
                return render(request, 'customers/signup.html')
        else:
            messages.error(request, 'Password is not matched.')
            return render(request, 'customers/signup.html')

    def get(self, request):
        return render(request, 'customers/signup.html')


def logout_customer(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return redirect('login')
