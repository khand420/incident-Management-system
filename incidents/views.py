


# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import User, Incident
from .serializers import UserSerializer, IncidentSerializer

# class UserViewSet(viewsets.ViewSet):
#     def create(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(password=make_password(request.data['password']))
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def login(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(password=make_password(request.data['password']))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # user = serializer.save()
            # token, created = Token.objects.get_or_create(user=user)
            # return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"message": "Login successful","token": token.key}, status=status.HTTP_200_OK)
            # return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)



    def forgot_password(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # Here you would implement sending a password reset email
            return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class IncidentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        # serializer = IncidentSerializer(data=request.data)
        serializer = IncidentSerializer(data=request.data, context={'request': request})
        # print('serializer-----',serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        incidents = Incident.objects.filter(reporter=request.user.id)
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        incident = Incident.objects.filter(id=pk, reporter_name=request.user.id).first()
        if incident:
            serializer = IncidentSerializer(incident)
            return Response(serializer.data)
        return Response({"error": "Incident not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        incident = Incident.objects.filter(id=pk, reporter=request.user.id).first()
        if incident:
            if incident.status == 'Closed':
                return Response({"error": "Cannot edit closed incidents"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = IncidentSerializer(incident, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Incident not found"}, status=status.HTTP_404_NOT_FOUND)

    def search(self, request, incident_id=None):
        incident = Incident.objects.filter(incident_id=incident_id, reporter=request.user.id).first()
        if incident:
            serializer = IncidentSerializer(incident)
            return Response(serializer.data)
        return Response({"error": "Incident not found"}, status=status.HTTP_404_NOT_FOUND)






# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from .models import User, Incident
# from .serializers import UserSerializer, IncidentSerializer

# from rest_framework.decorators import action
# from rest_framework.response import Response


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class IncidentViewSet(viewsets.ModelViewSet):
#     serializer_class = IncidentSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Incident.objects.filter(reporter=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(reporter=self.request.user)


# class IncidentViewSet(viewsets.ModelViewSet):
#     serializer_class = IncidentSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Incident.objects.filter(reporter=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(reporter=self.request.user)

#     @action(detail=False, methods=['get'])
#     def search(self, request):
#         incident_id = request.query_params.get('incident_id', None)
#         if incident_id:
#             incident = self.get_queryset().filter(incident_id=incident_id).first()
#             if incident:
#                 serializer = self.get_serializer(incident)
#                 return Response(serializer.data)
#         return Response({"detail": "Incident not found."}, status=404)
