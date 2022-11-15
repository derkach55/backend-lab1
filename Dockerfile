FROM python:3.10

WORKDIR = .

COPY requirements.txt .

ENV FLASK_APP=lab1.py

ENV PORT=5000

RUN pip install -r requirements.txt

COPY . .

EXPOSE $PORT

CMD flask run --host 0.0.0.0 -p $PORT