from django.shortcuts import render, redirect, HttpResponse
from .models import Contact
from django.core.mail import send_mail, EmailMessage

def save(request):
	d = request.POST
	Contact.objects.create(
		name = d['name'],
		email = d['email'],
		date = d['date'],
		department = d['department'],
		telnumber = d['phone'],
		extra = d['message'],
		)

	# send_mail("Registration", ("""
	# 	Name:{}
	# 	Date:{}
	# 	Department:{}
	# 	Phone:{}
	# 	Message:{}
	# 	""").format(d['name'], d['date'], d['department'], d['phone'], d['message']), "admin@mail.ru", ['admin@mail.ru'])

	return redirect("home")