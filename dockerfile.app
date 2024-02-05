# Your current Docker image 
FROM --platform=linux/amd64 python:3.11

RUN apt-get update && apt-get install -y gcc unixodbc-dev gpg

# Import the Microsoft public key
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Add Microsoft's repo for the latest prod drivers for ODBC
RUN echo "deb [arch=amd64] https://packages.microsoft.com/debian/10/prod buster main" > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update

# Install the MS ODBC driver
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Proceed as before
RUN pip install poetry

WORKDIR /code
COPY ./pyproject.toml ./poetry.lock*  /code/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD ["uvicorn", "src.shared.server.index:app", "--host", "0.0.0.0", "--port", "80"]
