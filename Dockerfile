# -------- Build Stage --------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# -------- Runtime Stage --------
FROM python:3.11-slim

WORKDIR /app

# Copy only installed packages from builder
COPY --from=builder /usr/local /usr/local

COPY app/ .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
