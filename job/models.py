from django.db import models

"""
Job :
- title
- location
- job type
- description
- published at
- vacancy
- salary
- category
- experience
    - apply job
    - post job
"""

JOB_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
    ("together", "Full and Part time"),
)


def image_upload(instance, file_name):
    [image_name, extension] = file_name.split('.')
    return f"jobs/{instance.id}/{instance.id}.{extension}"


class Job(models.Model):
    title = models.CharField(max_length=50)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=500, default="")
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.FloatField(default=0)
    experience = models.IntegerField(default=0)
    image = models.ImageField(upload_to=image_upload)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Job Titile: {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"name: {self.name}"
