from django.urls import path
from django.contrib.sitemaps.views import sitemap

from . import views
from .views import PortfolioJsonView
from .sitemaps import StaticSitemap, ProjectSitemaps


sitemaps = {
    'static': StaticSitemap,
    'project-detail': ProjectSitemaps
}

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about-us'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/portfolio-json/<int:num_projects>/', PortfolioJsonView.as_view(), name='portfolio-json'),
    path('coaching/', views.coaching, name='coaching'),
    path('contact/', views.contact, name='contact'),
    path('thank_you/', views.thank_you, name='thank-you'),
    path('portfolio/<slug:slug>', views.project_detail, name='project-detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.sitemap")
]
