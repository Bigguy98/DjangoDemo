from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # /polls/<id>/
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    # /polls/<id>/result
    path('<int:pk>/result', views.ResultView.as_view(), name='result'),
    # /polls/<id>/vote
    path('<int:pk>/vote', views.vote, name='vote')
]