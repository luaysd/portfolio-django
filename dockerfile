FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . /app/

# Expose port 8000 for Django
EXPOSE 8000

# Command to run Gunicorn
CMD ["gunicorn", "your_project_name.wsgi:application", "--bind", "0.0.0.0:8000"]
