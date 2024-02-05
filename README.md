## To run use the following commands:

```
uvicorn src.shared.server.index:app --reload --host 0.0.0.0 --port 8000
```

## To run tests use:
```
python -m unittest -v
```

Look at .env.example to know how to set up .env
If you dont have a remote redis to use, you need to have it running locally on localhost:6397 or use the docker compose.


## To run using Docker Compose:
Run:
```
docker network create traefik-public
```

### Next, create the environment variables for HTTP Basic Auth:

#### Create the username, e.g.:
```
export USERNAME=admin
```
#### Create an environment variable with the password, e.g.:
```
export PASSWORD=changethis
```
#### Use openssl to generate the "hashed" version of the password and store it in an environment variable:
```
export HASHED_PASSWORD=$(openssl passwd -apr1 $PASSWORD)
```
#### And now you can start the Traefik Docker Compose stack:

```
docker-compose -f docker-compose-production.yml up
```

### Or, to run without traefik:

```
docker-compose -f docker-compose.yml up
```
