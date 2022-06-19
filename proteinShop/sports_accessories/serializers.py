from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import sports_accessories


class sports_accessories_serializer(serializers.ModelSerializer):
    class Meta:
        model = sports_accessories
        fields = "__all__"


#def encode():
#    model = sports_accessories_model('barbell_30')
#    model_sr = sports_accessories_serializer(model)
#    print(model_sr.data, type(model_sr.data), sep='\n')
#    json = JSONRenderer().render(model_sr.data)
#    print(json)


