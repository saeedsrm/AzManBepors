from django.urls import path
from .views import *

urlpatterns = [

    path('new-category/', CategoryCreateView.as_view(), name='new-category'),
    path('new-tag/', TagCreateView.as_view(), name='new-tag'),
    path('all-question/', QuestionListView.as_view(), name='all-question'),
    path('create-new-question/', QuestionCreateView.as_view(), name='create-new-question'),
    path('update-question/<int:pk>/', QuestionUpdateView.as_view(), name='update-question'),
    path('delete-question/<int:pk>/', QuestionDeleteView.as_view(), name='delete-question'),
]
