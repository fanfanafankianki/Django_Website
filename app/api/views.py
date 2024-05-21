from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Testing
from .serializers import TestingSerializer

# Create your views here.
class TestViewSet(viewsets.ModelViewSet):
    queryset = Testing.objects.all()
    serializer_class = TestingSerializer

    @action(detail=False, methods=['put'])
    def update_all(self, request):
        # Pobranie danych z żądania
        data = request.data
        print("Received data:", data)

        if not isinstance(data, list):
            return Response({"error": "Oczekiwano listy obiektów."}, status=status.HTTP_400_BAD_REQUEST)

        # Usunięcie wszystkich obecnych obiektów Testing
        Testing.objects.all().delete()

        # Utworzenie nowych obiektów Testing na podstawie przesłanych danych
        for item in data:
            serializer = TestingSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Wszystkie obiekty zostały zastąpione."}, status=status.HTTP_200_OK)