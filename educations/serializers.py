from rest_framework import serializers
# from accounts.serializers import AccountSerializer

from educations.models import Education


class EducationSerializer(serializers.ModelSerializer):
    # account = AccountSerializer(read_only=True)

    class Meta:
        model = Education
        fields = "__all__"
        read_only_fields = ["id"]

class ListEducationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Education
        fields = ['institution_name','course','start_date','end_date','certificate_link']
