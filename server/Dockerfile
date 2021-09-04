# Use an official Python runtime as a parent image
FROM python:3.9.0-slim

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# Copy the current directory contents into the container at /code/
COPY . /app/

RUN apt-get update \
&& apt-get install gcc libc-dev python3-dev -y \
&& apt-get clean

#RUN mkdir /app

# Set the working directory to /code/
WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN pip install gunicorn


EXPOSE 8000

CMD ["sh", "entrypoint.sh"]
