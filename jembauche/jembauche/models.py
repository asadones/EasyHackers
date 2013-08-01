from django.db import models

class Job(models.Model):

    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    function_code = models.CharField(max_length=100)
    industry_code = models.CharField(max_length=100)
    location_code = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    location_country = models.CharField(max_length=100)
    location_province = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    company_nb_employees = models.CharField(max_length=100)
    contract = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    contact_lastname = models.CharField(max_length=100)
    contact_givenname = models.CharField(max_length=100)

    start_date = models.DateTimeField(auto_now_add = True)
    end_date = models.DateTimeField()

    password = models.CharField(max_length=100)

    state = models.IntegerField() # 1 = en cours de creation, 2 = attente paiement, 3 = en cours

class JobOptions(models.Model):

    job_id = models.ForeignKey('Job')
    option_data = models.CharField(max_length=1000)

