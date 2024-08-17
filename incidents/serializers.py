from rest_framework import serializers
from .models import User, Incident

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'pin_code', 'city', 'country']

# class IncidentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Incident
#         fields = ['id', 'incident_id', 'reporter', 'reporter_type', 'details', 'reported_date', 'priority', 'status']
#         read_only_fields = ['incident_id', 'reporter', 'reported_date']





class IncidentSerializer(serializers.ModelSerializer):
    # reporter = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    #     required=False  # Marking reporter as not required in the request payload
    # )
    # Define the reporter as a PrimaryKeyRelatedField
    reporter = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Incident
        fields = ['incident_id', 'reporter','reporter_type', 'details', 'reported_date', 'priority', 'status'] 


    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        
        # Set the reporter field to the current user
        validated_data['reporter'] = user
        
        return super().create(validated_data)    




# class IncidentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Incident
#         fields = ['id', 'incident_id', 'reporter', 'reporter_type', 'details', 'reported_date', 'priority', 'status']
#         read_only_fields = ['incident_id', 'reporter', 'reported_date']

#     def update(self, instance, validated_data):
#         if instance.status == 'Closed':
#             raise serializers.ValidationError("Closed incidents cannot be edited.")
#         return super().update(instance, validated_data)
