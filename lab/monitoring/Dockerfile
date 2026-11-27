FROM debian:13-slim
RUN apt-get update && apt-get install -y --no-install-recommends bird2 python3 && rm -rf /var/lib/apt/lists/*
COPY exporter.py /exporter.py
USER 65534:65534
CMD ["python3", "/exporter.py"]
