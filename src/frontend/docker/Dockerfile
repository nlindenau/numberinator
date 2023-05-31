FROM python:alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /app ./frontend

EXPOSE 8080

CMD [ "python3", "-m" , "flask", "--app", "frontend", "run", "--host=0.0.0.0", "--debug"]