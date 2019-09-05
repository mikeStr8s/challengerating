FROM python:3
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY . /usr/src/app
# RUN pip install --upgrade pip
RUN apt update
RUN apt install netcat -y
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]