from django.db import models
from django.db.models import fields
from rest_framework import serializers
from institute.models import Country, Institute, Institute_Type, User, Skill, User_Skill, Job_Type, Job, User_Job, Education, Workexp, Document

# Country Serializer
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_code', 'name']

# Institute_Type Serializer
class Institute_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute_Type
        fields = '__all__'

# Institute Serializer
class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        # fields = ['name', 'email', 'password', 'about', 'website', 'country_id', 'logo', 'organization_size', 'organization_type', 'status']
        fields = '__all__'

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# Skill Serializer
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

# User_Skill Serializer
class User_SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Skill
        fields = '__all__'

# Job_Type Serializer
class Job_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Type
        fields = '__all__'

# Job Serializer
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

# User_Job Serializer
class User_JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Job
        fields = '__all__'

# Education Serializer
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


# Workexp Workexp
class WorkexpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workexp
        fields = '__all__'

# Document Serializer
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

