FROM python:alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /app ./cloud_middleware

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "--app", "cloud_middleware", "run", "--host=0.0.0.0", "--debug"]