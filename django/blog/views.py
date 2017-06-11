# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from models import Jeux
from models import Commentaire

from django.views.generic import TemplateView

from django.views.generic import *
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.

def BlogIndex(request):
    return render(request, 'index.html')

def BlogHome(request):
    return render(request, 'home.html')

def BlogGame(request, pk):
    jeux = Jeux.objects.all()
    return render(request, 'game.html', {'jeux': jeux, 'page': pk})

def Game(request, slug, pk):
    jeu = get_object_or_404(Jeux, slug=slug)
    return render(request, 'gamedetails.html', {'jeu': jeu, 'page': pk})

def BlogAbout(request):
    return render(request, 'about.html')

def BlogLogin(request):
    return render(request, 'login.html')
    
class LoginView(TemplateView):
  template_name = 'login.html'
  def post(self, request, **kwargs):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )
    return render(request, self.template_name)

class LogoutView(TemplateView):
  template_name = 'login.html'
  def get(self, request, **kwargs):
    logout(request)
    return render(request, self.template_name)

def liste(request, page=1):
    minis_list = MiniURL.objects.order_by('-nb_acces')
    paginator = Paginator(minis_list, 5)  # 5 liens par page
    try:
        minis = paginator.page(page)
    except EmptyPage:
        minis = paginator.page(paginator.num_pages)
    return render(request, 'mini_url/liste.html', locals())


def BlogComment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['stephane.gibory@gmail.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm(request.POST)

    comments = Commentaire.objects.all()
    return render(request, 'comment.html', {'comments': comments, 'form': form})

def Comment(request, slug):
    comment = get_object_or_404(Commentaire, slug=slug)
    return render(request, 'gamedetails.html', {'comment': comment})