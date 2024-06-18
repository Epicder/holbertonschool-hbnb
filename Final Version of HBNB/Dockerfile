FROM python:3.9-alpine

WORKDIR /Final Version of HBNB

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 wsgi:app"]