FROM python:3.15.0b2-alpine3.22
RUN mkdir /app
WORKDIR /app
COPY . .
RUN apk update
RUN apk add --no-cache python3-dev py3-pip
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
