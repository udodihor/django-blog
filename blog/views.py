from django.shortcuts import render

posts = [
    {
        'author': 'IhorUd',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'August 27,2018'
    },
    {
        'author': 'JaneDoe',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'August 28,2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
