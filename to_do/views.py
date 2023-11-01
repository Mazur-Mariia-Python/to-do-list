from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from django.urls import reverse_lazy

from django.views import generic

from .forms import TaskForm, TagForm

from .models import Tag, Task


def index(request):
    """View function for the home page of the site."""

    tags_list = Tag.objects.all()
    tasks_list = Task.objects.all()

    context = {
        "tags_list": tags_list,
        "tasks_list": tasks_list,
    }

    return render(request, "to_do/index.html", context=context)


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    fields = "__all__"
    template_name = "to_do/tag_list.html"
    success_url = reverse_lazy("to_do:tag-list")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do:index")


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("to_do:tag-create")
