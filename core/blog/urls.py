from django.urls import path
from . import views
from django.views.generic import TemplateView, RedirectView

app_name = "blog"

urlpatterns = [
    path("cbv-index/", views.IndexView.as_view(), name="cbv-index"),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("go-to/", RedirectView.as_view(pattern_name="blog:fbv-index"), name="go-to"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
]
