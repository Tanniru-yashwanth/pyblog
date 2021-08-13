from django.urls import path
from . import views

app_name = 'pybasic'
"""
Configuring url patterns to view functions
"""
urlpatterns = [path('', views.index, name='index'),
               path('topics/', views.topics, name='topics'),
               path('topics/<int:user_id>/<int:topic_id>/', views.topic_detail, name='topic-detail'),
               path('topics/<int:tag_id>', views.tag_topics, name='tag-topics'),
]
