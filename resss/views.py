from django.shortcuts import render, redirect
from .models import FormSubmission

def submit_form(request):
    if request.method == 'POST':
        data = {key: value for key, value in request.POST.items() if key.startswith('name')}
        FormSubmission.objects.create(data=data)
        return redirect('view_data')
    return render(request, 'resss/resss.html')
    
def view_data(request):
    submissions = FormSubmission.objects.all()
    return render(request, 'resss/data.html', {'submissions': submissions})
    
