FROM python:3.10.7-slim

COPY ["./LICENSE", "./requirements.txt", "/ws/"]
COPY ["./src/client/", "/ws/src/client/"]
COPY ["./src/fastapi_app/", "/ws/src/fastapi_app/"]

WORKDIR "/ws"
RUN [\
  "python", "-m", "pip", "install", \
  "--no-cache-dir", "--upgrade", "-r", "requirements.txt"\
]

EXPOSE 3000
WORKDIR "/ws/src/fastapi_app"
CMD ["python", "main.py"]
