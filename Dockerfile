FROM python:3.11-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8051

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]