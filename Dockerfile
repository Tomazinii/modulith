FROM python:3

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP=run.py

EXPOSE 5000

RUN alembic upgrade head

CMD ["flask", "run", "--host=0.0.0.0"]