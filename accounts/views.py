from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm

from allauth.account.views import PasswordChangeView
from django.urls import reverse_lazy


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
        pass

    if is_admin(request.user):
        pass
    else:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)

            if u_form.is_valid():
                u_form.save()
                return redirect('/')
        else:
            u_form = UserUpdateForm(instance=request.user)

            context = {
                'u_form': u_form,
                'user_type': request.user.usercategory.type
            }
            return render(request, 'dashboard/profile.html', context)


class LoginAfterPasswordChangeView(PasswordChangeView):
    @property
    def success_url(self):
        return reverse_lazy('useraccount:login_redirect')


login_after_password_change = login_required(LoginAfterPasswordChangeView.as_view())

