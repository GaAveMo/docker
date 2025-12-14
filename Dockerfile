# FROM python:3.10-slim
# WORKDIR /app
# COPY app.py .
# # for lab3 below only
# RUN pip install flask
# CMD ["python", "app.py"]

# lab4
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
# EXPOSE 5000
CMD ["python", "app.py"]



