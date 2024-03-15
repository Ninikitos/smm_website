from datetime import datetime
from django.shortcuts import render
from django.urls import reverse

from .models import (AboutPageModel,
                     ServicePageModel,
                     CoachingPageModel,
                     ClientInformation,
                     ProjectModel,
                     ProjectImagesModel,
                     ProjectVideosModel,
                     ProjectMediaStatModel)
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View

from django.core.mail import EmailMessage
from django.conf import settings


def index(request):
    projects_model = ProjectModel.objects.all()
    projects = []

    for project in projects_model:
        if project.is_home_page:
            projects.append(project)

    return render(request, "webapp/index.html", {
        'projects': projects
    })


def about_us(request):
    about_content = AboutPageModel.objects.first()
    return render(request, "webapp/about_us.html", {
        'about_content': about_content
    })


def services(request):
    service_content = ServicePageModel.objects.first()
    return render(request, "webapp/services.html", {
        'service_content': service_content
    })


def portfolio(request):
    return render(request, 'webapp/portfolio.html', {})


class PortfolioJsonView(View):
    def get(self,request, *args, **kwargs):
        upper = kwargs.get('num_projects')
        lower = upper - 4
        projects = list(ProjectModel.objects.values()[lower:upper])
        projects_size = len(ProjectModel.objects.all())
        max_size = True if upper >= projects_size else False
        return JsonResponse({'data': projects, 'max': max_size, 'min': projects_size}, safe=False)


def project_detail(request, slug):
    project = ProjectModel.objects.get(slug=slug)
    images = ProjectImagesModel.objects.filter(project=project)
    videos = ProjectVideosModel.objects.filter(project=project)
    media_stats = ProjectMediaStatModel.objects.filter(project=project)
    return render(request, 'webapp/project.html', {
        'project': project,
        'images': images,
        'videos': videos,
        'media_stats': media_stats
    })


def coaching(request):
    coaching_content = CoachingPageModel.objects.first()
    return render(request, "webapp/coaching.html", {
        'coaching_content': coaching_content
    })


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company', '')
        scope = request.POST.get('scope', '')
        work = request.POST.get('work', '')
        social = request.POST.get('social', '')
        services = ', '.join(request.POST.getlist('service', []))
        is_social_agency = request.POST.get('is_social_agency', '')
        is_social_agency = 'Yes' if is_social_agency == 'yes' else 'No'
        budget = request.POST.get('budget', None)
        start_date = request.POST.get('start-date', None)
        if start_date == "":
            start_date = datetime.now().strftime("%Y-%m-%d")
        message = request.POST.get('message', '')

        # Create an instance of the model and save the data
        ClientInformation.objects.create(
            name=name,
            lastname=lastname,
            email=email,
            phone=phone,
            company=company,
            scope=scope,
            work=work,
            social=social,
            services=services,
            is_social_agency=is_social_agency,
            budget=budget,
            start_date=start_date,
            message=message
        )
        # Email to predefined address with all data information
        message = (f"{name} {lastname} just completed a contact form. Client's email address is {email} "
                   f"and a phone number {phone}. Rest information could be found in admin page of your website. \n\n")
        email = EmailMessage(
            'New client request from a website',
                message,
            settings.EMAIL_HOST_USER,
            ['ninikitos90@gmail.com']
        )
        email.send()
        return HttpResponseRedirect(reverse('thank-you'))
    else:
        return render(request, "webapp/contact.html")


def thank_you(request):
    return render(request, 'webapp/thank_you.html')