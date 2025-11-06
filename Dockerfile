FROM python:3.12-slim

#Evita bytecode y forza logs en stdout
ENV PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1

# Set the working directory

WORKDIR /app

#Dependencias de sistema necesarias para mysqlclient y utilidades complementarias
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        pkg-config \
        openssh-client \
    && rm -rf /var/lib/apt/lists/*


# install dependencias de python antes de copiar el codigo
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt


#copy the application to the working directory

COPY . .

EXPOSE 8000

# Start the ssh tunnel
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
