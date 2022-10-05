from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="Course")
    description = models.TextField()

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.name


class Sections(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="Course")
    description = models.TextField()

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.name


class Contact(models.Model):
    location_name = models.CharField(max_length=150)
    location_link = models.URLField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=150)

    def __str__(self):
        return self.location_name


class Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=50)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
