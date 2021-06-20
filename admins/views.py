from django.shortcuts import render

from users.models import User


# Create your views here.
def index(request):
    return render(request, 'admins/admin.html')


# Здесь будет CRUD
def admin_users(request):
    context = {'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    return render(request, 'admins/admin-users-create.html')


def admin_users_update(request, id):
    return render(request, 'admins/admin-users-update-delete.html')


def admin_users_delete(request, id):
    pass