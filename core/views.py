from django.shortcuts import render

def index(request):
	'''Display TacT homepage.'''
	return render(request, 'core/index.html')

def about(request):
	'''Display TacT about page.'''
	return render(request, 'core/about.html')

def contact(request):
	'''Display TacT contact page.'''
	return render(request, 'core/contact.html')
