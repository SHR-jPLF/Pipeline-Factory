FROM python:3

WORKDIR /app/

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD factory.py .

CMD ['python','factory.py']