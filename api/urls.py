from django.urls import path
from .views import KeyValueList, KeyValueDetail

urlpatterns = [
    path('store/', KeyValueList.as_view()),
    path('store/<int:pk>', KeyValueDetail.as_view()),
]