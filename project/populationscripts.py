import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
# Import settings
django.setup()

import random
from job.models import JobModel
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):
        JobModel.objects.get_or_create(company_name=fakegen.company(),job_title=fakegen.job(),company_mail="ankit@gmail.com",location='India',salary=1000000,is_active=True,job_desc="later")


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')