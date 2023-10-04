FROM python:3.8-bullseye

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
