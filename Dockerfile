# Official Python image
FROM python:3.10-slim

# Working directory inside container
WORKDIR /app

# Copy requirements file first (for caching layers)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Run your Python bot (change main.py if your filename is different)
CMD ["python", "main.py"]