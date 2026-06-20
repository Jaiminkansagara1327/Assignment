from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from .serializers import MappingSerializer

class MappingListCreateView(APIView):
    def get(self, request):
        mappings = PatientDoctorMapping.objects.all().select_related('patient', 'doctor')
        return Response(MappingSerializer(mappings, many=True).data)

    def post(self, request):
        serializer = MappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MappingByPatientView(APIView):
    def get(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id).select_related('patient', 'doctor')
        if not mappings.exists():
            return Response({'message': 'No doctors assigned.'})
        return Response(MappingSerializer(mappings, many=True).data)

class MappingDeleteView(APIView):
    def delete(self, request, pk):
        get_object_or_404(PatientDoctorMapping, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
