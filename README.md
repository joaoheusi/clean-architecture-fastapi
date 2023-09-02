To run use the following commands:

uvicorn src.shared.server.index:app --reload --host 0.0.0.0 --port 8000
python -m unittest -v

Look at .env.example to know how to set up .env

If you dont have a remote redis to use, you need to have it running locally on localhost:6397
