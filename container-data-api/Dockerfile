FROM python:3.10-alpine

WORKDIR /src

RUN apk add --no-cache gcc curl musl-dev linux-headers librdkafka-dev

RUN pip install --upgrade pip \
    && pip install requests confluent-kafka==2.3.0 pyyaml flask

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin

COPY src /src

CMD ["python3", "-u", "main.py"]
