from django.urls import path, include
from . import views
from django.views.generic import TemplateView, RedirectView

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # path("go-to/", RedirectView.as_view(pattern_name="blog:fbv-index"), name="go-to"),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path(
        "post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"
    ),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path(
        "post/<int:pk>/edit", views.PostEditView.as_view(), name="post-edit"
    ),
    path(
        "post/<int:pk>/delete",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
