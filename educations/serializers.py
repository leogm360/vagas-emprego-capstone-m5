from rest_framework import serializers

from educations.models import Education

class EducationSerializer(serializers.ModelSerializer):
    # account_id = UserSerializer(read_only=True)

    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = ['id']
        