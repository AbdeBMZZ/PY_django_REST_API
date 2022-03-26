from rest_framework.response import Response
from .serializers import EtudiantSerializer
from rest_api.models import Etudiant
from rest_framework import status
from rest_framework.views import APIView


class EtudiantList(APIView):

    def get(self, request):
        etudiants = Etudiant.objects.all()
        serializer = EtudiantSerializer(etudiants, many=True)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def post(self, request):
        serializer = EtudiantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EtudiantDetail(APIView):

    def get(self, request, cne):
        etd = Etudiant.objects.get(cne=cne)
        serializer = EtudiantSerializer(etd, many=False)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, cne, format=None):
        etd = Etudiant.objects.get(cne=cne)
        etd.delete()
        return Response({'message': 'deleted with success'}, status=status.HTTP_200_OK)
