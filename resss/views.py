from django.shortcuts import render, redirect
from .models import FormSubmission

def submit_form(request):
    if request.method == 'POST':
        data = {key: value for key, value in request.POST.items() if key.startwith('name')}
        FormSubmission.objects.crate(data=data)
        return redirect('view_data')
    return render(request, 'resss/resss.html')
    
def view_data(request):
    submissions = FormSubmission.object.all()
    return render(request, 'resss/resss.html', {'submissions': submissions})
    
