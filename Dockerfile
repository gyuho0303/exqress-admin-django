FROM python:3.8
COPY . /usr/src/myadminpage/
WORKDIR /usr/src/myadminpage
RUN pip3 install -r requirements.txt
CMD ["python3", "myadminpage/manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000/tcp
