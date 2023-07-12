from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'survey/survey.html')


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