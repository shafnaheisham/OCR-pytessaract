FROM python:3.10
WORKDIR/app
ADD ocr_app.py .
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirement.txt

CMD ["python", "./ocr_app.py"]
