from django.urls import path
from . import views
from django.views.generic import TemplateView, RedirectView

app_name = "blog"

urlpatterns = [
    path("fbv-index/", views.indexView, name="fbv-index"),
    # path("cbv-index/",TemplateView.as_view(template_name="index.html", extra_context={"title": "cbv-index"}), name="cbv-about"),
    path("cbv-index/", views.IndexView.as_view(), name="cbv-index"),
    path("go-to/", RedirectView.as_view(pattern_name="blog:fbv-index"), name="go-to"),
]
