FROM ubuntu

RUN apt update && apt install -y python3 python3-pip

RUN mkdir /app

COPY index.html /app/index.html

WORKDIR /app

ENTRYPOINT ["python3", "-m", "http.server"]
