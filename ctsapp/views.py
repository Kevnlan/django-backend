from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProspectsSerializer
from .models import Prospects
# Create your views here.


class ProspectsViews(APIView):
    def get(self, request, id=None):
        if id: 
            prospect = Prospects.objects.get(id=id)
            serializer = ProspectsSerializer(prospect)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        prospects = Prospects.objects.all()
        serializer = ProspectsSerializer(prospects, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProspectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        prospect = Prospects.objects.get(id=id)
        serializer = ProspectsSerializer(prospect, data=request.data, partial=True)
        if serializer.is_valid:
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        prospect = get_object_or_404(Prospects, id=id)
        prospect.delete()
        return Response({"status": "success", "data": "Record Deleted"})
