from django.shortcuts import render

posts = [
    {
        "author": "CoreyMS",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "Agust 06, 2022",
    },
    {
        "author": "CoreyMS",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "Agust 07, 2022",
    },
]


# Create your views here.
def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
