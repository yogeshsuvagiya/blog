from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_images")
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title