from django.shortcuts import render,redirect
from .models import Place
import random
import json
import pandas as pd
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Area  # 가정: 앱의 이름이 'myapp'
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# 클러스터링 및 유사도 기반 지역 추천 함수
def recommend_areas(cluster_df, survey_data):
    cluster_df['average_vector'] = cluster_df['average_vector'].apply(lambda vector_str: np.array([float(num) for num in vector_str[1:-1].split()]))
    similar_areas = pd.DataFrame()
    input_areas = []

    for myarea in ['myarea_1', 'myarea_2', 'myarea_3']:
        if myarea in survey_data and survey_data[myarea] and survey_data[myarea] in cluster_df['area'].values:
            cluster = cluster_df[cluster_df['area'] == survey_data[myarea]]['cluster'].values[0]
            area_vector = cluster_df[cluster_df['area'] == survey_data[myarea]]['average_vector'].values[0]
            same_cluster = cluster_df[cluster_df['cluster'] == cluster].copy()  
            same_cluster['similarity'] = same_cluster['average_vector'].apply(lambda x: cosine_similarity(area_vector.reshape(1, -1), x.reshape(1, -1))[0][0])
            same_cluster = same_cluster[same_cluster['area'] != survey_data[myarea]]
            similar_areas = pd.concat([similar_areas, same_cluster])
            input_areas.append(survey_data[myarea])
        else:
            print(f"{myarea} does not exist in the dataframe or is empty in the request.")
            
    for area in input_areas:
        similar_areas = similar_areas[similar_areas['area'] != area]
    
    if not similar_areas.empty:
        top_5_areas = similar_areas.sort_values('similarity', ascending=False)['area'].values[:5]
        return top_5_areas
    else:
        return []

    
class Survey_simila_View(View):
    def get(self, request):
        file_path = 'survey_data.json'
        survey_data = read_json_file(file_path)
        # print('survey_data : ',survey_data)
        # 데이터를 JsonResponse 형태로 반환합니다.
        gender = survey_data.get('gender', '')
        age = survey_data.get('age', '')
        family = survey_data.get('family', '')

        filtered_data = Place.objects.filter(gender=gender, age=age, family=family)
        top_places = filtered_data.order_by('-rating')[:15]
        # print(f"Filtered data: {filtered_data}")

        recommended_places = random.sample(list(top_places), min(len(top_places), 5))
        # print(f"Recommended places: {recommended_places}")


        # JSON 파일로 반환할 데이터를 생성합니다.
        similadest = {
            'place_gender': gender,
            'place_age': age,
            'place_family': family,
            'place_location': [place.location for place in recommended_places],
            # 추가 필드들도 필요에 따라 포함시킬 수 있습니다.
        }

        survey_data_02 = read_json_file(file_path)             
        print('survey_data_02 : ',survey_data_02)
        myarea_1 = survey_data_02 .get('myarea_1', '')
        myarea_2 = survey_data_02 .get('myarea_2', '')
        myarea_3 = survey_data_02 .get('myarea_3', '')     
        
        data = {
            'myarea_1': myarea_1,
            'myarea_2': myarea_2,
            'myarea_3': myarea_3,
        }

        print('data : ',data)

        df = pd.DataFrame(list(Area.objects.values()))  # 데이터베이스에서 모든 지역을 불러옴
        top_5 = recommend_areas(df, data)
        destination = json.dumps(list(top_5))

        result_file_path = 'similadest.json'
        with open(result_file_path, 'w') as file:
            json.dump(similadest , file)
        
        result_file_path_02 = 'destination.json'
        with open(result_file_path_02 , 'w', encoding='cp949') as file:
            json.dump(destination, file)
        
        print(f"similadest : {similadest }")
        print(f"destination : {destination }")
        return render(request, 'waiting/waiting.html', {'similadest': similadest} )    


    # def post(self,request):

    #     file_path = 'survey_data.json'
        # survey_data_02 = read_json_file(file_path)             
        # print('survey_data_02 : ',survey_data_02)
        # myarea_1 = survey_data_02 .get('myarea_1', '')
        # myarea_2 = survey_data_02 .get('myarea_2', '')
        # myarea_3 = survey_data_02 .get('myarea_3', '')     
        
        # data = {
        #     'myarea_1': myarea_1,
        #     'myarea_2': myarea_2,
        #     'myarea_3': myarea_3,
        # }

        # print('data',data)
        # data = json.loads(request.body)  # 요청으로부터 데이터를 로드
        # df = pd.DataFrame(list(Area.objects.values()))  # 데이터베이스에서 모든 지역을 불러옴
        # top_5_areas = recommend_areas(df, data)  # 추천 지역 계산
        # print(f"top_5_areas : {top_5_areas }")
   
        # return render(request, 'waitting/waitting.html', {'top_5_areas': top_5_areas} )
        # # return JsonResponse({'recommendations': list(top_5_areas)})

# def index(request):
#     return render(request, 'waitting/index.html')

# def recommend(request):
#     if request.method == 'POST':
#         gender = request.POST.get('gender')
#         age = request.POST.get('age')
#         companion = request.POST.get('companion')

#         # Filter data based on the input
#         filtered_data = Place.objects.filter(gender=gender, age=age, companion=companion)
#         print(f"Filtered data: {filtered_data}")
    
#         # Sort by rating and select top 15
#         top_places = filtered_data.order_by('-rating')[:15]
#         print(f"Top places: {top_places}")
    
#         # Randomly select 5 places
#         recommended_places = random.sample(list(top_places), min(len(top_places), 5))
#         print(f"Recommended places: {recommended_places}")
    
#         return render(request, 'waitting/results.html', {'recommended_places': recommended_places})
#     else:
#         return render(request, 'index.html')