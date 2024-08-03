# eureka_api 💡
Repository for the Eureka backend microservice, programmed in Python using the Django Framework.

# Requirements 📋
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Django 4.2](https://docs.djangoproject.com/en/4.2/topics/install/#installing-official-release)
- [Docker](https://www.docker.com/products/docker-desktop/)

# Installation 👩‍💻

### Create virtual environment in Python (only first time) 🐍

###### Windows

```bash
python -m venv venv
```

###### Linux

```bash
virtualenv -p python3.11 venv
```

### Activate the virtual environment 🗺

###### Windows:

```bash
venv\Scripts\activate
```

###### Linux:

```bash
source venv/bin/activate
```

### Install the requirements 😋

```bash
pip install -r requirements.txt
```

### Compose the Docker containers (only first time) 🐋

```bash
docker-compose up
```

### Access the application in your browser 

Open your browser and go to:

```bash
localhost:8000
```

### Run the tests for mock 🧪

**Note:** Ensure that Docker is running before executing the tests.

```bash
python manage.py test
```

### Configure the `.env` file 🤗

Copy the `.env.example` file to create a `.env` file and modify it as needed:

```bash
cp .env.example .env
```

In the `.env` file, you can customize the variables to your needs:

- `STAGE`: 
  - Use **`TEST`** to run tests with the mock setup.
  - Use **`TEST_DB`** to run tests with the database configured via Docker.

- **Database Configuration**:
  - `DB_NAME`: Your database name.
  - `DB_USER`: Your database user.
  - `DB_PASSWORD`: Your database password.
  - `DB_PORT`: Database port (default is 5432).

- **MinIO Configuration**:
  - `LOCALSTACK_ACCESS_KEY`: Your access key for MinIO.
  - `LOCALSTACK_SECRET_KEY`: Your secret key for MinIO.

### Access the MinIO UI 🚀

You can access the MinIO UI (an S3 compatible storage for local testing) at:

```bash
localhost:9001
```

Log in using the `LOCALSTACK_ACCESS_KEY` and `LOCALSTACK_SECRET_KEY` provided in your `.env` file.

### Populate the Database

1. **Install DBeaver (recommended):**
   - [DBeaver Download](https://dbeaver.io/download/)

2. **Create a connection and select PostgreSQL as your DB:**
   - Host: `localhost`
   - Port: `5432`
   - User and Password: As specified in your `.env` file.

3. **Run the queries located in the `populate_db` directory** to populate your database with initial data.

## Contributors 💰🤝💰

- Bruno Vilardi - [Brvilardi](https://github.com/Brvilardi) 👷‍♂️
- Hector Guerrini - [hectorguerrini](https://github.com/hectorguerrini) 🧙‍♂️
- João Branco - [JoaoVitorBranco](https://github.com/JoaoVitorBranco) 😎
- Vitor Soller - [VgsStudio](https://github.com/VgsStudio) ☀
- Luigi Trevisan - [LuigiTrevisan](https://github.com/LuigiTrevisan) 🍄
- Felipe Carillo - [FelipeCarillo](https://github.com/FelipeCarillo) 🚀