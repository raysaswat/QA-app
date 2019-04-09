# QA-app


# create a virtualenv 
C:\Users\sray\Desktop>python -m venv myvenv
C:\Users\sray\Desktop>myvenv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Username = admin
password = admin

REST API endpoint for list of questions and json format

http://127.0.0.1:8000/api/v1/question/

http://127.0.0.1:8000/api/v1/question/?format=json

REST API endpoint for list of choices and json format
http://127.0.0.1:8000/api/v1/choice/
http://127.0.0.1:8000/api/v1/choice/?format=json


http://localhost:8000/admin/
admin dashborad

http://localhost:8000/admin/polls/question/
for list of questions

http://localhost:8000/admin/polls/choice/
for list of choices

http://localhost:8000/admin/polls/choice/2/change/
select the question,choice text, votes and to delete particular choice

http://localhost:8000/admin/polls/question/2/change/
update the question and published date to delete particular Question
