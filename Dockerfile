
#ENV PYTHONUNBUFFERED 1
#ARG CACHEBUST="This is Cachebust - change me slightly each build - 009"
#RUN echo "$CACHEBUST"

FROM python:3.8.0-buster
#FROM alpine:latest
#RUN apk-add --no-cache python3-dev && pip3 install --upgrade pip

# Make a directory for our application
WORKDIR /app
# Install dependencies
#COPY requirements.txt .


# Copy our source code
COPY . /app
RUN pip install -r requirements.txt
RUN ["chmod", "+x", "/node/execure.sh"]
# COPY /Score.txt .
# Run the application
CMD ["python", "MainScores.py"]