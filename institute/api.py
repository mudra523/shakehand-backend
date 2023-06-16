from institute.models import Country, Institute, Institute_Type, User, Skill, User_Skill, Job_Type, Job, User_Job, Education, Workexp, Document
from rest_framework import viewsets, permissions
from .serializers import CountrySerializer, InstituteSerializer, Institute_TypeSerializer, UserSerializer, SkillSerializer, User_SkillSerializer, Job_TypeSerializer, JobSerializer, User_JobSerializer, EducationSerializer, WorkexpSerializer, DocumentSerializer

#Country Viewsets
class CountryViewSets(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CountrySerializer

#Institute Viewsets
class InstituteViewSets(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InstituteSerializer

#Institute_Type Viewsets
class Institute_TypeViewSets(viewsets.ModelViewSet):
    queryset = Institute_Type.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Institute_TypeSerializer

#User Viewsets
class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

#Skill Viewsets
class SkillViewSets(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SkillSerializer

#User_Skill Viewsets
class User_SkillViewSets(viewsets.ModelViewSet):
    queryset = User_Skill.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = User_SkillSerializer

#Job_Type Viewsets
class Job_TypeViewSets(viewsets.ModelViewSet):
    queryset = Job_Type.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Job_TypeSerializer

#Job Viewsets
class JobViewSets(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = JobSerializer

#User_Job Viewsets
class User_JobViewSets(viewsets.ModelViewSet):
    queryset = User_Job.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = User_JobSerializer

#Education Viewsets 
class EducationViewSets(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EducationSerializer

#Workexp Viewsets
class WorkexpViewSets(viewsets.ModelViewSet):
    queryset = Workexp.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = WorkexpSerializer
    

#Document Viewsets
class DocumentViewSets(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DocumentSerializer
