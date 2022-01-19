FROM python:3.10-alpine

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "api.infra.entrypoint:app", "--host", "0.0.0.0", "--port", "80"]
