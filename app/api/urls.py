from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

import api.views as vws


urlpatterns = [
    path('monsters/', vws.MonsterList.as_view(), name='monster-list'),
    path('monsters/<int:pk>', vws.MonsterDetail.as_view(), name='monster-detail'),
]
