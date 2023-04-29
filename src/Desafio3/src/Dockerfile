FROM python:3.11.2
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python3","-m","flask","run","--host=0.0.0.0"]