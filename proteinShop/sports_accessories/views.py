from rest_framework import generics
from django.forms import model_to_dict
from .models import sports_accessories, category
from .serializers import sports_accessories_serializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class sports_accessories_APIList(generics.ListCreateAPIView):
    queryset = sports_accessories.objects.all()
    serializer_class =  sports_accessories_serializer


class sports_accessories_APIView(APIView):
    def get(self, request):
        sa = sports_accessories.objects.all()
        return Response({
            'posts': sports_accessories_serializer(sa, many=True).data
        })

    def post(self, request):
        serializer = sports_accessories_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'post': serializer.data
        })


    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method path not allowed"})

        try:
            instance = sports_accessories.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serializer = sports_accessories_serializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

#class sports_accessoriesAPIView(generics.ListAPIView):
#    queryset = sports_accessories.objects.all()
#    serializer_class = sports_accessories_serializer

