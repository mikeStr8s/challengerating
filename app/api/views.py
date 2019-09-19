from rest_framework import generics

import api.models as mdl
import api.serializers as srl


class MonsterList(generics.ListAPIView):
    queryset = mdl.Monster.objects.all()
    serializer_class = srl.MonsterListSerializer


class MonsterDetail(generics.RetrieveAPIView):
    queryset = mdl.Monster.objects.all()
    serializer_class = srl.MonsterSerializer