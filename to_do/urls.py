from django.urls import path

from .views import index, TagListView, TaskCreateView, TagCreateView

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "to_do"
