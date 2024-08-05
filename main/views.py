from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import EditRequestSerializer


# Create your views here.
class EditRequestView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        obj = EditRequestSerializer(data=request.data, context={"request": request})
        if obj.is_valid():
            print(obj.validated_data)
            obj.save()
            return Response(obj.data, status=status.HTTP_201_CREATED)
        return Response(obj.error_messages, status=status.HTTP_400_BAD_REQUEST)
