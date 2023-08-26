uvicorn src.shared.server.routes:app --reload --host 0.0.0.0 --port 8000
python -m unittest -v
