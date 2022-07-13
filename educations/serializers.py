from rest_framework import serializers

from educations.models import Education


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = ['id','institution_name','course','start_date','end_date','certificate_link','account_id']
        read_only_fields = ["id"]

class ListEducationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Education
        fields = ['id','institution_name','course','start_date','end_date','certificate_link']
