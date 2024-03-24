from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import ProjectModel


class ProjectSitemaps(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return ProjectModel.objects.all()

    def location(self, obj):
        return '/project-detail/%s' % (obj.slug)


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.80
    protocol = 'https'

    def items(self):
        return ['index', 'about-us', 'services', 'portfolio', 'coaching']  # returning static pages; home and contact us

    def location(self, item):
        return reverse(item)