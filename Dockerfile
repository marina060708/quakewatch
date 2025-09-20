FROM python:3.12-slim
WORKDIR /app

# Install deps
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Run with Gunicorn (Flask app lives in app.py -> app)
ENV PORT=8000
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app", "--workers=2"]
