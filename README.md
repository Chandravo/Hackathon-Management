# Hackathon Management

A hackathon management portal where users can create hackathons, register for hackathons and also add submissions for hackathons 

## Tech Stack


**Server:** Python, Django

**Database:** PostgreSQL

## Run Locally

Clone the project

```bash
  git clone https://github.com/Chandravo/Hackathon-Management
```


We recommend you to use virtual environment

```bash
  python -m venv venv
```

Activate virtual environment

&emsp;&emsp;For Windows PowerShell

```bash
    env/Scripts/activate.ps1
```

&emsp;&emsp;For Linux and MacOS

```bash
    source env/bin/activate
```

Install dependencies

Note: For Windows users, replace psycopg2-binary with psycopg2 in requirements.txt

```bash
  pip install -r requirements.txt
```

Make sure you have installed PostgreSQL

Run the following commands in psql shell:  
```
psql postgres
```
Create a new database for your Django project:
```
CREATE DATABASE hackathon_management;
```
Create a new user with a password:
```
CREATE USER username WITH PASSWORD 'your_pass';
```
Grant all privileges on the database to the user:

```
GRANT ALL PRIVILEGES ON DATABASE hackathon_management TO username;
```
Exit the Postgres shell:
```
\q
```

Create `.env` file in base directory and place Secret-Key, and Database credentials

Run Migrations

```
 python manage.py makemigrations
```

```
 python manage.py migrate
```

Create Super User
```
  python manage.py createsuperuser
```

Start the server

```bash
  python manage.py runserver
```



## Postman Collection for Endpoints

[Postman Collection](https://api.postman.com/collections/20527262-1b8436d6-db3d-490c-85dc-a7732ef40ecd?access_key=PMAT-01H08D151NQ4QAR3JA3DEBGNWX)

