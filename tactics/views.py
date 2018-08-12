from django.shortcuts import render, get_object_or_404

from .models import Tactic


def tactics(request):
    '''Show all tactics'''
    tactics = Tactic.objects.order_by('created')
    context = {'tactics': tactics}
    return render(request, 'tactics/tactics.html', context)


def tactic(request, tactic_id):
    '''Show a single tactic'''
    tactic = get_object_or_404(Tactic, id=tactic_id)
    # Set context and render necessary template
    context = {'tactic': tactic}
    return render(request, 'tactics/tactic.html', context)
