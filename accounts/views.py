from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from allauth.account.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View

def is_seller(user):
    return user.account.business_type == 'Seller'


def is_buyer(user):
    return user.account.business_type == 'Buyer'

def is_admin(user):
    pass

def login_redirect_view(request):
    if is_seller(request.user):
        return redirect('/dashboard/seller-dashboard/')

    elif is_buyer(request.user):
        return redirect('/dashboard/buyer-dashboard/')



class LoginAfterPasswordChangeView(PasswordChangeView):
    @property
    def success_url(self):
        return reverse_lazy('useraccount:login_redirect')


login_after_password_change = login_required(LoginAfterPasswordChangeView.as_view())


