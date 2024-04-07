# Use the python base image with version 3.11.9
FROM python:3.11.9

WORKDIR /app

# install dependency first to speed up rebuild when app change
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# copy applications
COPY *.py /app

ENV INIT_INDEX=true
EXPOSE 7654
CMD ["python", "api.py"]