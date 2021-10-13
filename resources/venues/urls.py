from django.urls import path
from . import views

app_name = 'resources.venues'

urlpatterns = [
    path('', views.detail, name='detail'),
    path('/<str:yelp_id>', views.sampleYelpOutput, name='sampleYelpOutput'),
    # path('<string:yelp_id>/', views.detail, name='detail'),

    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]