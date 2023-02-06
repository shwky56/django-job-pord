from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job, Category


# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 2)
    page_namber = request.GET.get('page')
    page_obj = paginator.get_page(page_namber)
    
    print(job_list) 
    context = {'jobs' : page_obj}
    return render(request, 'job/job_list.html', context)

def job_detail(request, id):
    job_detail = Job.objects.get(id=id)
    print(job_detail.title)
    return render(request, 'job/job_detail.html', {'job' : job_detail})