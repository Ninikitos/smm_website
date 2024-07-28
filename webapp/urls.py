from django.urls import path
from django.contrib.sitemaps.views import sitemap

from . import views
from .views import PortfolioJsonView, UGCJsonView
from .sitemaps import StaticSitemap, ProjectSitemaps


sitemaps = {
    'static': StaticSitemap,
    'project-detail': ProjectSitemaps
}

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about_us, name='about-us'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/portfolio-json/<int:num_projects>/', views.PortfolioJsonView.as_view(), name='portfolio-json'),
    path('user-generated-content/', views.ugc, name='ugc'),
    path('portfolio/ugc-json/<int:num_projects>/', views.UGCJsonView.as_view(), name='ugc-json'),
    path('coaching/', views.coaching, name='coaching'),
    path('contact/', views.contact, name='contact'),
    path('thank-you/', views.thank_you, name='thank-you'),
    path('<slug:slug>/', views.project_detail, name='project-detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]
