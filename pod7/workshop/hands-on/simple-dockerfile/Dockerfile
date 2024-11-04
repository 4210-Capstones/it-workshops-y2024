ARG PYTHON_VERSION=3
FROM python:${PYTHON_VERSION}
RUN pip install Flask
EXPOSE 8080
WORKDIR /website
COPY . .
ENTRYPOINT python app/Registration.py