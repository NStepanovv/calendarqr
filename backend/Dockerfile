FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgresql-client \
    && apt-get clean

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "calendarqr.wsgi:application", "--bind", "0.0.0.0:8000"]