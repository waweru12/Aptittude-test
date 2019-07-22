from django.conf.urls.static import static
from tester import views
from django.conf.urls import url,include
from django.conf import settings

from rest_framework import routers

from tester.views import ExamQuestionViewset
from .views import QuestionViewset, ExamViewset

router = routers.DefaultRouter()
router.register(r'question',QuestionViewset)
router.register(r'exam',ExamViewset)





urlpatterns = [
    url(r'^api/',include(router.urls)),

    url(r'^$',views.welcome,name="welcome"),
    url(r'^create/',views.create_user,name="create_user"),
    url(r'^validate_login/',views.log_in,name="log_user"),
    url(r'^add_exam/',views.add_exam,name="add_exam"),
    url(r'^add_question/',views.add_question,name="add_question"),
    url(r'^test',views.get_data,name="getdata"),
    url(r'^logout',views.log_out,name="log_out"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)