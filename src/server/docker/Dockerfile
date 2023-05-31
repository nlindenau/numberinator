FROM python:alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /app ./server

EXPOSE 8080

CMD [ "python3", "-m" , "flask", "--app", "server", "run", "--host=0.0.0.0", "--debug"]