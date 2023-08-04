FROM python:3.9

RUN mkdir -p /std_app

COPY  . /std_app

RUN python -m pip install -r /std_app/requirement.txt

EXPOSE 5000


CMD ['python' '/std_app/app.py']

