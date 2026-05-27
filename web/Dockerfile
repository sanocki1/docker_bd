FROM python:3.11

WORKDIR /app

COPY dependencies.txt .

RUN pip install -r dependencies.txt

COPY . .

CMD ["python", "app.py"]