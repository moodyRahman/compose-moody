
FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8081

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8081", "run:app"]
