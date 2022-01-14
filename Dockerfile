FROM python:3.9

WORKDIR /dsproj

ADD . /dsproj

COPY ./requirements.txt /dsproj/requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /dsproj

EXPOSE 8000
CMD ["python", "manage.py", "collectstatic", "--noinput"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--insecure"]
