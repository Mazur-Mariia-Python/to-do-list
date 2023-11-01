from django.db import models


class Tag(models.Model):
    """The theme of the task"""

    name = models.CharField(max_length=255)

    class Meta:
        """
        Tags should be ordered by name
        """

        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    """Describes what you should do"""

    content = models.CharField(max_length=255)
    """Datetime, when a task was created"""
    created_at = models.DateTimeField(auto_now_add=False)
    """
    Optional deadline datetime if a task should be done 
    until some datetime
    """
    deadline = models.DateTimeField(auto_now_add=False, null=True)
    """The boolean field that marks if the task is done or not"""
    completed = models.BooleanField()
    """Tags that are relevant for this task"""
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        """
        Tasks should be ordered from not done to done and from newest
        to oldest
        """

        ordering = ["-created_at"] and ["completed"]

    def __str__(self):
        return self.content
