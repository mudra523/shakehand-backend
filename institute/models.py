from django.db import models

# Create your models here.
class Country(models.Model):
    country_code = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=200)

class Institute_Type(models.Model):
    name = models.CharField(max_length=50)

class Institute(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=50)
    about = models.CharField(max_length=1000)
    website = models.CharField(max_length=100)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    Institute_Type_id = models.ForeignKey(Institute_Type, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    organization_size = models.CharField(max_length=100)
    organization_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=50)
    about = models.CharField(max_length=1000)
    gender = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    institute_id = models.ForeignKey(Institute, on_delete=models.CASCADE)
    avtar = models.CharField(max_length=100)
    is_aproved = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)

class Skill(models.Model):
    skill_name = models.CharField(max_length=50)

class User_Skill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)

class Job_Type(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=1000)

class Job(models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=1000)
    institution_id = models.ForeignKey(Institute, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    opening_no = models.CharField(max_length=50)
    deadline = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    job_type_id = models.ForeignKey(Job_Type, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

class User_Job(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)

class Education(models.Model):
    univercity_name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    major_in = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Workexp(models.Model):
    job_name = models.CharField(max_length=100)
    exp_desc = models.CharField(max_length=500)
    year_of_exp = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Document(models.Model):
    document_name = models.CharField(max_length=100)
    document_file = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
