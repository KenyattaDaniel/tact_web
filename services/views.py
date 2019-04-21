from django.shortcuts import redirect, render, get_object_or_404

from .models import Category, Service, Package

def categories(request):
    '''Show all categories'''
    categories = Category.objects.order_by('created')
    context = {'categories': categories}
    return render(request, 'services/categories.html', context)


def category(request, category_title_slug):
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_title_slug)
        context_dict['category_title'] = category.title

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        services = Service.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['services'] = services
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'services/category.html', context_dict)


def service(request, service_title_slug, category_title_slug):
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        service = Service.objects.get(slug=service_title_slug)
        context_dict['service_title'] = service.title
        category = Category.objects.get(slug=category_title_slug)
        context_dict['category_title'] = category.title

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        packages = Package.objects.filter(service=service)
        # Adds our results list to the template context under name pages.
        context_dict['packages'] = packages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['service'] = service

    except Service.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'services/service.html', context_dict)
