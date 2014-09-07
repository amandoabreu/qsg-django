from django.shortcuts import get_object_or_404, render
from django.http import Http404
from jobs.models import Salary, Company, District

def index(request):
	return render(request, 'jobs/index.html',{'path' : request.path})

def privacy(request):
	return render(request, 'jobs/privacy.html',{'path' : request.path})

def search(request):
	return render(request, 'jobs/search.html',{'path' : request.path})

def make_search(request):
	results = Salary.objects.order_by('salary_value')[:5]
	return render(request, 'jobs/search_results.html', {'results' : results})

def company_detail(request, company_id):
	try:
		company = Company.objects.get(pk=company_id)
	except Company.DoesNotExist:
		raise Http404
	return render(request, 'jobs/company_detail.html', {'company' : company})

def district_detail(request, district_id):
	try:
		district = District.objects.get(pk=district_id)
		salaries_cnt = Salary.objects.filter(salary_district=district_id).count()
	except District.DoesNotExist:
		raise Http404
	return render(request, 'jobs/district_detail.html', {'district' : district, 'cnt' : salaries_cnt})
