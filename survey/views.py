from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import SurveyForm
from .models import Survey
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# def index(request):
#     return render(request, 'survey/survey.html')

def index(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
       
        if form.is_valid():
           
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            region_1 = form.cleaned_data['region_1']
            area_1 = form.cleaned_data['area_1']
            region_2 = form.cleaned_data['region_2']
            area_2 = form.cleaned_data['area_2']
            region_3 = form.cleaned_data['region_3']
            area_3 = form.cleaned_data['area_3']
            
            survey_instance = Survey(
                gender=gender,
                age=age,
                region_1=region_1,
                area_1=area_1,
                region_2=region_2,
                area_2=area_2,
                region_3=region_3,
                area_3=area_3,
            )
       

            survey_instance.regionsave()
            survey_instance.save() 
            
            # return redirect('http://127.0.0.1:8000/classification/')  # 저장 후 리다이렉트할 URL(로컬)
            return redirect('http://52.78.46.115/classification/')  # 저장 후 리다이렉트할 URL(서버)  
    else:
        form = SurveyForm()
    
    return render(request, 'survey/survey.html')