from django.utils import timezone

from django.db import models
from PIL import Image
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.text import slugify


class AboutPageModel(models.Model):
    about_title = models.CharField(max_length=100)
    about_description = models.TextField()
    about_image_one = models.ImageField(upload_to='about_page_images/', null=True)
    about_slug_one = models.SlugField(default="", blank=True)
    about_image_two = models.ImageField(upload_to='about_page_images/', null=True)
    about_slug_two = models.SlugField(default="", blank=True)

    def __str__(self):
        return self.about_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resize_image(self.about_image_one, 315, 368)
        resize_image(self.about_image_two, 252, 294)

    class Meta:
        verbose_name_plural = "About page"

class ServicePageModel(models.Model):
    service_image_one = models.ImageField(upload_to='service_page_images/', null=True)
    service_slug_one = models.SlugField(default="", blank=True)
    service_title_one = models.CharField(max_length=255)
    service_list_one = models.TextField()

    service_image_two = models.ImageField(upload_to='service_page_images/', null=True)
    service_slug_two = models.SlugField(default="", blank=True)
    service_title_two = models.CharField(max_length=255)
    service_list_two = models.TextField()

    service_image_three = models.ImageField(upload_to='service_page_images/', null=True)
    service_slug_three = models.SlugField(default="", blank=True)
    service_title_three = models.CharField(max_length=255)
    service_list_three = models.TextField()

    service_image_four = models.ImageField(upload_to='service_page_images/', null=True)
    service_slug_four = models.SlugField(default="", blank=True)
    service_title_four = models.CharField(max_length=255)
    service_list_four = models.TextField()

    def __str__(self):
        return "Service page"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resize_image(self.service_image_one, 660, 790)
        resize_image(self.service_image_two, 660, 790)
        resize_image(self.service_image_three, 660, 790)
        resize_image(self.service_image_four, 660, 790)

    class Meta:
        verbose_name_plural = "Service page"

class CoachingPageModel(models.Model):
    coaching_title = models.CharField(max_length=100)
    coaching_description = models.TextField()
    coaching_image_one = models.ImageField(upload_to='coaching_page_images/', null=True)
    coaching_slug_one = models.SlugField(default="", blank=True)
    coaching_image_two = models.ImageField(upload_to='coaching_page_images/', null=True)
    coaching_slug_two = models.SlugField(default="", blank=True)

    def __str__(self):
        return self.coaching_title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resize_image(self.coaching_image_one, 315, 368)
        resize_image(self.coaching_image_two, 252, 294)

    class Meta:
        verbose_name_plural = "Coaching page"

class ClientInformation(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=50, blank=True)
    scope = models.CharField(max_length=100, blank=True)
    work = models.URLField(blank=True)
    social = models.CharField(max_length=50, blank=True)
    services = models.CharField(max_length=400, blank=True)
    is_social_agency = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
    budget = models.IntegerField(default=0, blank=True, null=True)
    start_date = models.DateField(default=None, null=True, blank=True)
    message = models.TextField(default=timezone.now, max_length=1200, blank=True)

    def __str__(self):
        return f"{self.name}, {self.lastname}"

    class Meta:
        verbose_name_plural = "Client information"

class ProjectModel(models.Model):
    name = models.CharField(max_length=100, default="Project", blank=False)
    slug = models.SlugField(unique=True, blank=True)
    cover = models.ImageField(upload_to="project_covers/", null=True)
    review = models.CharField(max_length=200, blank=False, null=True)
    description = models.TextField(max_length=400, blank=False)
    strategy = models.TextField(max_length=1000, blank=False)
    stat_one = models.CharField(max_length=10, blank=False)
    text_one = models.CharField(max_length=25, blank=False)
    stat_two = models.CharField(max_length=10, blank=False)
    text_two = models.CharField(max_length=25, blank=False)
    stat_three = models.CharField(max_length=10, blank=False)
    text_three = models.CharField(max_length=25, blank=False)
    photo_content_description = models.TextField(default="")
    video_content_description = models.TextField(default="")
    media_stat_content_description = models.TextField(default="")
    is_home_page = models.BooleanField(default=False, null=True)
    is_ugc = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Projects"

class ProjectImagesModel(models.Model):
    name = models.CharField(max_length=200, default="Project photo", blank=False)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    image_slug = models.SlugField(default="", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Project images"

class ProjectVideosModel(models.Model):
    name = models.CharField(max_length=200, default="Project video", blank=False)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    video = models.FileField(upload_to='projects_videos/')

    def __str__(self):
        return  self.name
    class Meta:
        verbose_name_plural = "Project videos"

class ProjectMediaStatModel(models.Model):
    name = models.CharField(max_length=200, default="Project media statistics", blank=False)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects_media_stat/')
    image_slug = models.SlugField(default="", blank=True)

    class Meta:
        verbose_name_plural = "Project media stat"

def resize_image(image_field, new_width, new_height):
    if image_field:
        img = Image.open(image_field.path)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(image_field.path)

@receiver(pre_delete, sender=AboutPageModel)
def delete_images(sender, instance, **kwargs):
    instance.about_image_one.delete(False)
    instance.about_image_two.delete(False)

@receiver(pre_delete, sender=CoachingPageModel)
def delete_images(sender, instance, **kwargs):
    instance.coaching_image_one.delete(False)
    instance.coaching_image_two.delete(False)

@receiver(pre_delete, sender=ServicePageModel)
def delete_images(sender, instance, **kwargs):
    instance.service_image_one.delete(False)
    instance.service_image_two.delete(False)
    instance.service_image_three.delete(False)
    instance.service_image_four.delete(False)

@receiver(pre_delete, sender=ProjectImagesModel)
def delete_images(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(pre_delete, sender=ProjectVideosModel)
def delete_images(sender, instance, **kwargs):
    instance.video.delete(False)

@receiver(pre_delete, sender=ProjectMediaStatModel)
def delete_images(sender, instance, **kwargs):
    instance.image.delete(False)