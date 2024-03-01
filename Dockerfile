
FROM python:3.11.4

ADD mongo_terminal_search.py .

COPY requirements.txt .
COPY format_mongo.py .

RUN pip install -r requirements.txt 

CMD ["python", "./mongo_terminal_search.py"]


