from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=False)
    deadline = models.DateTimeField(auto_now_add=False, blank=True)
    completed = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:

        ordering = ["-created_at"] and ["completed"]

    def __str__(self):
        return self.content
