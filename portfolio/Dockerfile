FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=portfolio.settings

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose Django port
EXPOSE 8000 

# Run the app with Gunicorn
CMD ["sh", "-c", "python manage.py collectstatic --noinput ", "&& gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]
