from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . import serializers
from . import models
# Create your views here.


class RuleListView(APIView):

    def get(self, request):
        try:

            data = models.Rule.objects.all()
            serializer = serializers.RuleSerializer(data)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response("Some Error Occurred " + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = serializers.RuleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignalDataView(APIView):
    def get(self, request):
        try:
            data = models.SignalData.objects.all()
            serializer = serializers.SignalListSerializer(data)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = serializers.SignalListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





