from rest_framework import routers
from .api import CountryViewSets, InstituteViewSets, Institute_TypeViewSets, UserViewSets, SkillViewSets, User_SkillViewSets, Job_TypeViewSets, JobViewSets, User_JobViewSets, EducationViewSets, WorkexpViewSets, DocumentViewSets


router = routers.DefaultRouter()
router.register('api/country', CountryViewSets, 'country')
router.register('api/institute', InstituteViewSets, 'institute')
router.register('api/institute_type', Institute_TypeViewSets, 'institute_type')
router.register('api/user', UserViewSets, 'user')
router.register('api/skill', SkillViewSets, 'skill')
router.register('api/user_skil', User_SkillViewSets, 'user_skil')
router.register('api/job_type', Job_TypeViewSets, 'job_type')
router.register('api/job', JobViewSets, 'job')
router.register('api/user_job', User_JobViewSets, 'user_job')
router.register('api/education', EducationViewSets, 'education')
router.register('api/workexp', WorkexpViewSets, 'workexp')
router.register('api/document', DocumentViewSets, 'document')

urlpatterns = router.urls
