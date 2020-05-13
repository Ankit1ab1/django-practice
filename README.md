# django-practice


Part A

active jobs---http://127.0.0.1:8000/list/
create-job---http://127.0.0.1:8000/create/-----pass fields using rest framework



part B-

acending order salary-http://127.0.0.1:8000/job/?ordering=salary
descending order salary(by putting -)-http://127.0.0.1:8000/job/?ordering=-salary      


for filter -http://127.0.0.1:8000/job/?job_title=web&location=delhi       

also added filtering by is_active


for filter and ordering-http://127.0.0.1:8000/job/?job_title=Retail%20manager&ordering=-salary


I have used faker library of python for fake jobs,names etc.
population scripts is used for this.
