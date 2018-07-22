from django.shortcuts import render, get_object_or_404

from .models import Service, Offering

def services(request):
	'''Show all services'''
	services = Service.objects.order_by('created')
	context = {'services': services}
	return render(request, 'services/services.html', context)


def service(request, service_id):
	'''Show a single service and all of its offerings'''
	service = get_object_or_404(Service, id=service_id)
	# Store offerings linked to service in offerings variable
	offerings = service.offering_set.all()
	# Set context and render necessary template
	context = {'service': service, 'offerings': offerings}
	return render(request, 'services/service.html', context)


def offering(request, offering_id):
	'''Show a single service offering'''
	offering = get_object_or_404(Offering, id=offering_id)
	# Set context and render necessary template
	context = {'offering': offering}
	return render(request, 'services/offering.html', context)
