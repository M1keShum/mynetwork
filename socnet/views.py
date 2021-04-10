from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Users
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from .forms import CreateUser


def mainpage(request):
    allUsers = Users.objects.all()
    context = {'users': allUsers}
    return render(request, 'index.html', context)


def userpage(request, user_id):
    user = Users.objects.get(pk=user_id)
    messages = user.messages_set.all()
    context = {'user': user, 'messages': messages}
    return render(request, 'userpage.html', context)


class adduser(CreateView):
    template_name = 'createuser.html'
    form_class = CreateUser
    success_url = reverse_lazy('mainpage')


def addmessage(request, user_id):
    username = Users.objects.get(pk=user_id)
    username.messages_set.create(user=request.POST['name'], message=request.POST['message'])

    return HttpResponseRedirect(reverse('userpage', args=(username.id,)))




# class addmessage(CreateView):
#     template_name = 'createmessage.html'
#     form_class = CreateMessage
#     success_url = reverse_lazy('mainpage')
