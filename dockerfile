FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

COPY . /code/
ENTRYPOINT ["/code/entrypoint.sh"]