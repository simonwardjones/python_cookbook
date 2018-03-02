FROM python:3

# Bundle app source
COPY  . /app

run ls app

# Install app dependencies
RUN pip install -r app/requirements.txt

CMD ["python", "/app/main.py"]

# docker build -t cb .
# docker run -dp 8080:8080 --name cbr cb