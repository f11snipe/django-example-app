FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV BASE_DIR /app
RUN mkdir -p $BASE_DIR
WORKDIR $BASE_DIR
COPY requirements.txt $BASE_DIR/
RUN pip install -r requirements.txt
COPY . $BASE_DIR/
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
