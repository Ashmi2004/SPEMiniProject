FROM ubuntu:latest
COPY calculator.html /app/calculator.html
COPY style.css /app/style.css
COPY testing/test.py /app/test.py

CMD ["python", "test.py"]
