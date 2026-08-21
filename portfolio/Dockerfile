FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=portfolio.settings
ENV DJANGO_DEBUG False

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Compile SCSS to CSS before collecting static files
RUN python manage.py compilescss

# Collect static files into STATIC_ROOT
RUN python manage.py collectstatic --noinput --clear
# Expose Django port
EXPOSE 8000 

# Run the app with Gunicorn
CMD ["sh", "-c", "gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000"]
