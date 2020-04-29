from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from django.shortcuts import render, reverse, get_object_or_404, HttpResponseRedirect, HttpResponse, redirect

class IndexView(View):
	pass