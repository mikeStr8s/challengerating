from django.urls import path

import encounter.views as vws


urlpatterns = [
    path('', vws.Encounter.as_view(), name='encounter'),
]
