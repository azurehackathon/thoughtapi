FROM ubuntu:16.04
RUN set -xe \
    && apt-get update \
    && apt-get install -y python-pip
WORKDIR /app
ADD ./code /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 9000
ENV NAME World
CMD ["python", "api.py"]
