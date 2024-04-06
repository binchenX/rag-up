# Use the python base image with version 3.11.9
FROM python:3.11.9

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

ENV INIT_INDEX=true
EXPOSE 7654
CMD ["python", "api.py"]