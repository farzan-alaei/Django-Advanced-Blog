from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post
from .forms import PostForm


# Create your views here.

"""
def indexView(request):
    context = {
        "title": "fbv-index",
    }
    return render(request, "index.html", context=context)
"""


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "cbv-index"
        context["posts"] = Post.objects.all()
        return context


class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "blog.view_post"
    queryset = Post.objects.all()
    # model = Post
    ordering = "id"

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

    context_object_name = "posts"
    # paginate_by = 2


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


"""
class PostCreateView(FormView):
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ["author", "title", "content", "status", "category", "published_date"]
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        profile = self.request.user.profile_set.first()
        if not profile:
            return self.form_invalid(form)

        form.instance.author = profile
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"
