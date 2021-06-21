from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm


# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


# Здесь будет CRUD
@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {'users': User.objects.all(),
               'title': 'GeekShop - АДМИН | Пользователи'}
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {'title': 'GeekShop - АДМИН | Регистрация', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES,
                                    instance=selected_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'GeekShop - АДМИН | обновление пользователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    # user.delete()
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))
