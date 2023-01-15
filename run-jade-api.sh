source venv/bin/activate
uvicorn main:app --error-logfile '-' --access-logfile '-'