from django.shortcuts import render, get_object_or_404
from django.http import Http404

from butter_cms import ButterCMS


client = ButterCMS('bb642c7222ed11498c5aa3d59ab90870ede2e615')

def tactics(request, page=1):
    response = client.posts.all({'page_size': 10, 'page': page})

    try:
        recent_posts = response['data']
    except:
        # In the event we request an invalid page number, no data key will exist in response.
        raise Http404('Page not found')

    next_page = response['meta']['next_page']
    previous_page = response['meta']['previous_page']

    return render(request, 'tactics/tactics.html', {
        'recent_posts': recent_posts,
        'next_page': next_page,
        'previous_page': previous_page
    })


def tactic(request, slug):
    try:
        response = client.posts.get(slug)
    except:
        raise Http404('Post not found')

    post = response['data']
    return render(request, 'tactics/tactic.html', {
        'post': post
    })