FROM python:3.10-slim
WORKDIR /app
COPY app.py .
# for lab3 below only
RUN pip install flask
CMD ["python", "app.py"]


