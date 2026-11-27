FROM debian:13-slim
RUN apt-get update && apt-get install -y --no-install-recommends bird2 iproute2 && rm -rf /var/lib/apt/lists/*
CMD ["bird", "-f", "-c", "/etc/bird/bird.conf"]
