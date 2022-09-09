from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializers


# Create your views here.

# class based APIViews

class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        try:
            id = pk
            if id is not None:
                try:
                    stu = Student.objects.get(id=id)
                    serializer = StudentSerializers(stu)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    stu = Student.objects.all()
                    serializer = StudentSerializers(stu, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        try:
            serializer = StudentSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            msg = str(e)
            return Response({'msg': msg}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, formet=None):
        try:
            id = pk
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Complete Data Updated'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            msg = str(e)
            return Response({'error': msg}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        try:
            id = pk
            print(id)
            stu = Student.objects.get(id=id)
            print(stu)
            serializer = StudentSerializers(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'Partial Data Updated'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            msg = str(e)
            return Response({'error': msg}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        id = pk
        try:
            if id is not None:
                try:
                    stu = Student.objects.get(id=id)
                    stu.delete()
                    return Response({'msg': 'Data Deleted'}, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'id is NONE'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


