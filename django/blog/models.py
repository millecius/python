# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name="Type de jeu")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'
    def  __str__(self):
        return self.name

@python_2_unicode_compatible
class Jeux(models.Model):
    title = models.CharField(max_length=150, verbose_name="Nom du jeu")
    body = models.TextField(verbose_name="Déscription")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    picture = models.ImageField(verbose_name="Image")
    types = models.ManyToManyField(Type, verbose_name="Type de jeu")
    class Meta:
        verbose_name = 'Jeu'
        verbose_name_plural = 'Jeux'
    def  __str__(self):
        return self.title

@python_2_unicode_compatible
class Commentaire(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titre du commentaire")
    body = models.TextField(verbose_name="Commentaire")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    author = models.ForeignKey(User, verbose_name="Auteur")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    modified = models.DateTimeField(auto_now_add=True, verbose_name="Date de modification")
    def  __str__(self):
        return self.title