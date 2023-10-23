
FROM python:3.11.4

ADD mongo_terminal_search.py .

COPY requirements.txt .

RUN pip install -r requirements.txt 

CMD ["python", "./mongo_terminal_search.py"]


