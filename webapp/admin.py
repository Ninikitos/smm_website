import os

from django.contrib import admin
from django.utils.text import slugify

from .models import (AboutPageModel,
                     ServicePageModel,
                     CoachingPageModel,
                     ClientInformation,
                     ProjectModel,
                     ProjectImagesModel,
                     ProjectVideosModel,
                     ProjectMediaStatModel)

def update_slug_from_image(obj, image_fields, slug_fields):
    for i, image_field in enumerate(image_fields):
        image = getattr(obj, image_field)
        slug = getattr(obj, slug_fields[i])

        if image and hasattr(image, 'file') and hasattr(image.file, 'name'):
            image_filename = os.path.basename(image.file.name)
            image_filename = image_filename.replace("cfakepath", "").rsplit('.', 1)[0]

            # Only set slug if it's different from the slug derived from the image name
            if not slug:
                setattr(obj, slug_fields[i], slugify(image_filename))
            elif slug != slugify(image_filename):
                setattr(obj, slug_fields[i], slug)

    obj.save()

class AboutPageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        image_fields = ['about_image_one', 'about_image_two']
        slug_fields = ['about_slug_one', 'about_slug_two']

        update_slug_from_image(obj, image_fields, slug_fields)

class ServicePageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        image_fields = [
            'service_image_one',
            'service_image_two',
            'service_image_three',
            'service_image_four',
        ]

        slug_fields = [
            'service_slug_one',
            'service_slug_two',
            'service_slug_three',
            'service_slug_four',
        ]

        update_slug_from_image(obj, image_fields, slug_fields)

class CoachingPageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        image_fields = ['coaching_image_one', 'coaching_image_two']
        slug_fields = ['coaching_slug_one', 'coaching_slug_two']

        update_slug_from_image(obj, image_fields, slug_fields)

class ProjectImagesAdmin(admin.ModelAdmin):

    list_display = ('name', 'project_name')
    list_filter = ('project__name',)
    def project_name(self, obj):
        return obj.project.name if obj.project else ''
    project_name.short_description = 'Project Name'

    def save_model(self, request, obj, form, change):
        image_field = ['image']
        slug_field = ['image_slug']

        update_slug_from_image(obj, image_field, slug_field)

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_home_page', 'is_ugc')
    list_filter = ('is_ugc', )

class ProjectVideosAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_name')
    list_filter = ('project__name',)
    def project_name(self, obj):
        return obj.project.name if obj.project else ''
    project_name.short_description = 'Project Name'
class ClientInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'phone')

class ProjectMediaStatAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_name')
    list_filter = ('project__name',)

    def project_name(self, obj):
        return obj.project.name if obj.project else ''

    project_name.short_description = 'Project Name'

admin.site.register(AboutPageModel, AboutPageAdmin)
admin.site.register(ServicePageModel, ServicePageAdmin)
admin.site.register(CoachingPageModel, CoachingPageAdmin)
admin.site.register(ClientInformation, ClientInformationAdmin)
admin.site.register(ProjectModel, ProjectModelAdmin)
admin.site.register(ProjectImagesModel, ProjectImagesAdmin)
admin.site.register(ProjectVideosModel, ProjectVideosAdmin)
admin.site.register(ProjectMediaStatModel, ProjectMediaStatAdmin)

