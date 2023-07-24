from django.db import models

# Create your models here.

class Survey(models.Model):
    GENDER_CHOICES = (
        ('M', '남'),
        ('F', '여'),
    )

    AGE_CHOICES = (
        ('1', '10대'),
        ('2', '20대'),
        ('3', '30대'),
        ('4', '40대'),
        ('5', '50대'),
        ('6', '60대 이상'),
    )

    REGION_CHOICES = (
        ('서울특별시', '서울특별시'),
        ('경기도', '경기도'),
        ('인천광역시', '인천광역시'),
        ('강원특별자치도', '강원특별자치도'),
        ('충청북도', '충청북도'),
        ('충청남도', '충청남도'),
        ('대전광역시', '대전광역시'),
        ('세종특별자치시', '세종특별자치시'),
        ('전라북도', '전라북도'),
        ('전라남도', '전라남도'),
        ('광주광역시', '광주광역시'),
        ('경상북도', '경상북도'),
        ('경상남도', '경상남도'),
        ('대구광역시', '대구광역시'),
        ('울산광역시', '울산광역시'),
        ('부산광역시', '부산광역시'),
        ('제주특별자치도', '제주특별자치도'),
    )

    AREA_CHOICES = (
       ("종로구", "종로구"),
       ("중구", "중구"),
       ("용산구", "용산구"),
       ("성동구", "성동구"),
       ("광진구", "광진구"),
       ("동대문구", "동대문구"),
       ("중랑구", "중랑구"),
       ("성북구", "성북구"),
       ("강북구", "강북구"),
       ("도봉구", "도봉구"),
       ("노원구", "노원구"),
       ("은평구", "은평구"),
       ("서대문구", "서대문구"),
       ("마포구", "마포구"),
       ("양천구", "양천구"),
       ("강서구", "강서구"),
       ("구로구", "구로구"),
       ("금천구", "금천구"),
       ("영등포구", "영등포구"),
       ("동작구", "동작구"),
       ("관악구", "관악구"),
       ("서초구", "서초구"),
       ("강남구", "강남구"),
       ("송파구", "송파구"),
       ("강동구", "강동구"),
       ("수원시 장안구", "수원시 장안구"),
       ("수원시 권선구", "수원시 권선구"),
       ("수원시 팔달구", "수원시 팔달구"),
       ("수원시 영통구", "수원시 영통구"),
       ("성남시 수정구", "성남시 수정구"),
       ("성남시 중원구", "성남시 중원구"),
       ("성남시 분당구", "성남시 분당구"),
       ("의정부시", "의정부시"),
       ("안양시 만안구", "안양시 만안구"),
       ("안양시 동안구", "안양시 동안구"),
       ("부천시", "부천시"),
       ("광명시", "광명시"),
       ("평택시", "평택시"),
       ("동두천시", "동두천시"),
       ("안산시 상록구", "안산시 상록구"),
       ("안산시 단원구", "안산시 단원구"),
       ("고양시 덕양구", "고양시 덕양구"),
       ("고양시 일산동구", "고양시 일산동구"),
       ("고양시 일산서구", "고양시 일산서구"),
       ("과천시", "과천시"),
       ("구리시", "구리시"),
       ("남양주시", "남양주시"),
       ("오산시", "오산시"),
       ("시흥시", "시흥시"),
       ("군포시", "군포시"),
       ("의왕시", "의왕시"),
       ("하남시", "하남시"),
       ("용인시 처인구", "용인시 처인구"),
       ("용인시 기흥구", "용인시 기흥구"),
       ("용인시 수지구", "용인시 수지구"),
       ("파주시", "파주시"),
       ("이천시", "이천시"),
       ("안성시", "안성시"),
       ("김포시", "김포시"),
       ("화성시", "화성시"),
       ("광주시", "광주시"),
       ("양주시", "양주시"),
       ("포천시", "포천시"),
       ("여주시", "여주시"),
       ("연천군", "연천군"),
       ("가평군", "가평군"),
       ("양평군", "양평군"),
    #    ("중구", "중구"),
       ("동구", "동구"),
       ("미추홀구", "미추홀구"),
       ("연수구", "연수구"),
       ("남동구", "남동구"),
       ("부평구", "부평구"),
       ("계양구", "계양구"),
       ("서구", "서구"),
       ("강화군", "강화군"),
       ("옹진군", "옹진군"),
       ("춘천시", "춘천시"),
       ("원주시", "원주시"),
       ("강릉시", "강릉시"),
       ("동해시", "동해시"),
       ("태백시", "태백시"),
       ("속초시", "속초시"),
       ("삼척시", "삼척시"),
       ("홍천군", "홍천군"),
       ("횡성군", "횡성군"),
       ("영월군", "영월군"),
       ("평창군", "평창군"),
       ("정선군", "정성군"),
       ("철원군", "철원군"),
       ("화천군", "화천군"),
       ("양구군", "양구군"),
       ("인제군", "인제군"),
       ("고성군", "고성군"),
       ("양양군", "양양군"),
       ("청주시 상당구", "청주시 상당구"),
       ("청주시 서원구", "청주시 서원구"),
       ("청주시 흥덕구", "청주시 흥덕구"),
       ("청주시 청원구", "청주시 청원구"),
       ("충주시", "충주시"),
       ("제천시", "제천시"),
       ("보은군", "보은군"),
       ("옥천군", "옥천군"),
       ("영동군", "영동군"),
       ("증평군", "증평군"),
       ("진천군", "진천군"),
       ("괴산군", "괴산군"),
       ("음성군", "음성군"),
       ("단양군", "단양군"),
       ("천안시 동남구", "천안시 동남구"),
       ("천안시 서북구", "천안시 서북구"),
       ("공주시", "공주시"),
       ("보령시", "보령시"),
       ("아산시", "아산시"),
       ("서산시", "서산시"),
       ("논산시", "논산시"),
       ("계룡시", "계룡시"),
       ("당진시", "당진시"),
       ("금산군", "금산군"),
       ("부여군", "부여군"),
       ("서천군", "서천군"),
       ("청양군", "청양군"),
       ("홍성군", "홍성군"),
       ("예산군", "예산군"),
       ("태안군", "태안군"),
    #    ("동구", "동구"),
    #    ("중구", "중구"),
    #    ("서구", "서구"),
       ("유성구", "유성구"),
       ("대덕구", "대덕구"),
       ("세종특별자치시", "세종특별자치시"),
       ("전주시 완산구", "전주시 완산구"),
       ("전주시 덕진구", "전주시 덕진구"),
       ("군산시", "군산시"),
       ("익산시", "익산시"),
       ("정읍시", "정읍시"),
       ("남원시", "남원시"),
       ("김제시", "김제시"),
       ("완주군", "완주군"),
       ("진안군", "진안군"),
       ("무주군", "무주군"),
       ("장수군", "장수군"),
       ("임실군", "임실군"),
       ("순창군", "순창군"),
       ("고창군", "고창군"),
       ("부안군", "부안군"),
       ("목포시", "목포시"),
       ("여수시", "여수시"),
       ("순천시", "순천시"),
       ("나주시", "나주시"),
       ("광양시", "광양시"),
       ("담양군", "담양군"),
       ("곡성군", "곡성군"),
       ("구례군", "구례군"),
       ("고흥군", "고흥군"),
       ("보성군", "보성군"),
       ("화순군", "화순군"),
       ("장흥군", "장흥군"),
       ("강진군", "강진군"),
       ("해남군", "해남군"),
       ("영암군", "영암군"),
       ("무안군", "무안군"),
       ("함평군", "함평군"),
       ("영광군", "영광군"),
       ("장성군", "장성군"),
       ("완도군", "완도군"),
       ("진도군", "진도군"),
       ("신안군", "신안군"),
    #    ("동구", "동구"),
    #    ("서구", "서구"),
       ("남구", "남구"),
       ("북구", "북구"),
       ("광산구", "광산구"),
       ("포항시 남구", "포항시 남구"),
       ("포항시 북구", "포항시 북구"),
       ("경주시", "경주시"),
       ("김천시", "김천시"),
       ("안동시", "안동시"),
       ("구미시", "구미시"),
       ("영주시", "영주시"),
       ("영천시", "영천시"),
       ("상주시", "상주시"),
       ("문경시", "문경시"),
       ("경산시", "경산시"),
       ("의성군", "의성군"),
       ("청송군", "청송군"),
       ("영양군", "영양군"),
       ("영덕군", "영덕군"),
       ("청도군", "청도군"),
       ("고령군", "고령군"),
       ("성주군", "성주군"),
       ("칠곡군", "칠곡군"),
       ("예천군", "예천군"),
       ("봉화군", "봉화군"),
       ("을진군", "울진군"),
       ("울릉군", "울릉군"),
       ("창원시 의창구", "창원시 의창구"),
       ("창원시 성산구", "창원시 성산구"),
       ("창원시 마산합포구", "창원시 마산합포구"),
       ("창원시 마산회원구", "창원시 마산회원구"),
       ("창원시 진해구", "창원시 진해구"),
       ("진주시", "진주시"),
       ("통영시", "통영시"),
       ("사천시", "사천시"),
       ("김해시", "김해시"),
       ("밀양시", "밀양시"),
       ("거제시", "거제시"),
       ("양산시", "양산시"),
       ("의령군", "의령군"),
       ("함안군", "함안군"),
       ("창녕군", "창녕군"),
       ("고성군", "고성군"),
       ("남해군", "남해군"),
       ("하동군", "하동군"),
       ("산청군", "신창군"),
       ("함양군", "함양군"),
       ("거창군", "거창군"),
       ("합천군", "합천군"),
    #    ("중구", "중구"),
    #    ("동구", "동구"),
    #    ("서구", "서구"),
    #    ("남구", "남구"),
    #    ("북구", "북구"),
       ("수성구", "수성구"),
       ("달서구", "달서구"),
       ("달성군", "달성군"),
       ("군위군", "군위군"),
    #    ("중구", "중구"),
    #    ("남구", "남구"),
    #    ("동구", "동구"),
    #    ("북구", "북구"),
       ("울주군", "울주군"),
    #    ("중구", "중구"),
    #    ("서구", "서구"),
    #    ("동구", "동구"),
       ("영도구", "영도구"),
       ("부산진구", "부산진구"),
       ("동래구", "동래구"),
       ("남구", "남구"),
       ("북구", "북구"),
       ("해운대구", "해운대구"),
       ("사하구", "사하구"),
       ("금정구", "금정구"),
       ("강서구", "강서구"),
       ("연제구", "연제구"),
       ("수영구", "수영구"),
       ("사상구", "사상구"),
       ("기장군", "기장군"),
       ("제주시", "제주시"),
       ("서귀포시", "서귀포시"),

)


    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.CharField(max_length=1,choices=AGE_CHOICES)
    family= models.BooleanField(default=False)
    region_1 = models.CharField(max_length=30, choices=REGION_CHOICES)
    area_1 = models.CharField(max_length=30, choices=AREA_CHOICES)
    region_2 = models.CharField(max_length=30, choices=REGION_CHOICES, blank=True)
    area_2 = models.CharField(max_length=30, choices=AREA_CHOICES, blank=True)
    region_3 = models.CharField(max_length=30, choices=REGION_CHOICES, blank=True)
    area_3 = models.CharField(max_length=30, choices=AREA_CHOICES, blank=True)    

   
    myarea_1 = models.CharField(max_length=60)
    myarea_2 = models.CharField(max_length=60, blank=True)
    myarea_3 = models.CharField(max_length=60, blank=True)

    
    def regionsave(self, *args, **kwargs):
        self.myarea_1 = self.region_1 + ' ' + self.area_1
        self.myarea_2 = self.region_2 + ' ' + self.area_2
        self.myarea_3 = self.region_3 + ' ' + self.area_3
