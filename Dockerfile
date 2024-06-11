# Gunakan image resmi Python sebagai base image
FROM python:3.11-slim

# Set working directory di dalam container
WORKDIR /app

# Copy requirements.txt terlebih dahulu agar dependencies dapat di-cache
COPY requirements.txt .

# Install dependencies menggunakan pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh kode proyek ke dalam container
COPY . .

# Command yang akan dijalankan saat container dijalankan
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
