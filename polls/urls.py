from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # /polls/<id>/
    path('<int:question_id>', views.detail, name='detail'),
    # /polls/<id>/result
    # path('<int:question_id>/result', views.result, name='result'),
    # /polls/<id>/vote
    # path('<int:question_id>/vote', views.detail, name='vote')
]