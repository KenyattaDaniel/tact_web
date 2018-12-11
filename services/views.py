from django.shortcuts import redirect, render, get_object_or_404

from .models import Category, Service

def categories(request):
    '''Show all categories'''
    categories = Category.objects.order_by('created')
    context = {'categories': categories}
    return render(request, 'services/categories.html', context)


def category(request, category_id):
    '''Show a single category and all of its services'''
    category = get_object_or_404(Category, id=category_id)
    # Store services linked to category in services variable
    services = category.service_set.all()
    # Set context and render necessary template
    context = {'category': category, 'services': services}
    return render(request, 'services/category.html', context)


def service(request, service_id):
    '''Show a single service'''
    service = get_object_or_404(Service, id=service_id)
    # Store packages linked to service in packages variable
    packages = service.package_set.all()
    # Set context and render necessary template
    context = {'service': service, 'packages': packages}
    return render(request, 'services/service.html', context)
