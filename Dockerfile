FROM python:3.15.0a6-trixie

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY app.py /app 

EXPOSE 800

CMD ["python", "app.py"]
