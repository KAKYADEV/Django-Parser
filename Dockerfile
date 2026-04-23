# Use the official Python runtime image
FROM python:3.13  
 
# Set the working directory inside the container
WORKDIR /django-parser/parser
 
# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 
 
# Upgrade pip
RUN pip install --upgrade pip 
 
# Copy the Django project  and install dependencies
COPY requirements.txt  /django-parser/parser/
 
# run this command to install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    && mkdir -p /etc/apt/keyrings \
    && wget -qO /etc/apt/keyrings/google-linux-signing-key.gpg https://dl.google.com/linux/linux_signing_key.pub \
    && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-linux-signing-key.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable
 
RUN apt-get update && apt-get install -y \
    libnss3 \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libgtk-3-0 \
    libasound2 \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxfixes3 \
    libglib2.0-0

# Copy the Django project to the container
COPY . /django-parser/
 
# Expose the Django port
EXPOSE 8000
 
# Collect static files
RUN python manage.py collectstatic --noinput

# Run Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]