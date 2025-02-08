from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post

# Create your views here.


def indexView(request):
    context = {
        "title": "fbv-index",
    }
    return render(request, "index.html", context=context)


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "cbv-index"
        context["posts"] = Post.objects.all()
        return context


class PostList(ListView):
    # queryset = Post.objects.all()

    def get_queryset(self):
        posts = Post.objects.filter(status=False)
        return posts

    context_object_name = "posts"
    paginate_by = 2
