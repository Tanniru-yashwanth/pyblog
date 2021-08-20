from django.urls import path
from . import views

app_name = 'pybasic'
"""
Configuring url patterns to view functions
"""
urlpatterns = [path('', views.index, name='index'),
               path('topics/', views.topics, name='topics'),
               path('topics/<int:topic_id>/', views.topic_detail, name='topic-detail'),
               path('topics/<int:topic_id>/comment', views.comment, name='comment'),
               path('topics/<int:topic_id>/ask', views.question, name='question'),
               path('topics/<int:topic_id>/add_tag_topic', views.add_tag_topic, name='add-tag-topic'),
               path('topics/add_tag', views.tag, name='add-tag'),
               path('tags/<int:tag_id>/', views.tag_topics, name='tag-topics'),
]
