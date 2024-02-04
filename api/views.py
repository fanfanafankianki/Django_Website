from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Testing
from .serializers import TestingSerializer
from services.services import save
from services.services import dropDatabase
from services.services import get_all_records
import sys
sys.stdout = sys.stderr
import json

# Create your views here.
class TestViewSet(viewsets.ModelViewSet):
    
    queryset = Testing.objects.all()
    serializer_class = TestingSerializer

    @action(detail=False, methods=['put'])
    def update_all(self, request):
        data = request.data
        dropDatabase()   # Before putting values we have to truncate database firstly
        for record in data:
          name = record['name']
          description = record['description']
          imagePath = record['imagePath']
          product = []
          food_products = []
          print(f' name={name} description={description} imagePath={imagePath}')
          save(name,description,imagePath)

        # TUTAJ MAM NA TO WYJEBANE NA TA DJANGO
        if not isinstance(data, list):
            return Response({"error": "Oczekiwano listy obiektów."}, status=status.HTTP_400_BAD_REQUEST)
        for item in data:
            serializer = TestingSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Wszystkie obiekty zostały zastąpione."}, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def fetch_all(self, request):
        all_testings = Testing.objects.all()
        #PROPER DATA FORMAT LIST OF >> {"id": 2, "name": "Training 2", "description": "Description 2", "imagePath": "https://www.runningdad.com/wp-content/uploads/2017/04/workoutwednesday-400x250.png", "products": []},
        id = 1
        update_list_for_angular = []
        postgress_return = get_all_records()
        for record in postgress_return:
            name = record[0]
            description = record[1]
            imagePath = record[2]
            formatted_record = {"id":id,"name":name,"description":description,"imagePath":imagePath,"products":[]}
            update_list_for_angular.append(formatted_record)
            print(formatted_record)
            id+=1
        return Response(update_list_for_angular)

    