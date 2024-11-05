ARG PYTHON_VERSION=3
FROM python:${PYTHON_VERSION}
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT python Registration.py