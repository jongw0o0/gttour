from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SurveyForm
from .models import Survey

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
            myarea = region_1 + ' ' + area_1
            # region_2 = form.cleaned_data['region_2']
            # area_2 = form.cleaned_data['area_2']
            # region_3 = form.cleaned_data['region_3']
            # area_3 = form.cleaned_data['area_3']
            
            survey_instance = Survey(
                gender=gender,
                age=age,
                region_1=region_1,
                area_1=area_1,
                myarea = myarea
                # region_2=region_2,
                # area_2=area_2
                # region_3=region_3,
                # area_3=area_3
            )
            # survey_instance.save()
            survey_instance.regionsave()
 
            return redirect('success_url')  # 저장 후 리다이렉트할 URL
    else:
        form = SurveyForm()
    
    return render(request, 'survey/survey.html', {'form': form})







# def api(request):
#     members = []
#     for member in Member.objects.all().order_by('id'):
#         member_dict = OrderedDict([
#                 ('id',member.id),
#                 ('name',member.name),
#                 ('email',member.email),
#                 ('age',member.age),
#             ])
#         members.append(member_dict)

#     data = OrderedDict([
#             ('status','ok'),
#             ('members',members),
#         ])

#     json_str = json.dumps(data, ensure_ascii=False, indent=2)
#     return HttpResponse(json_str, content_type='application/json; charset=utf-8')