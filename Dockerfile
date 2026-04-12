FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY score_batch_v3.py /app/score_batch_v3.py
COPY models_v3/final/model.cbm /app/models_v3/final/model.cbm
COPY examples/sample_input_v3.csv /app/examples/sample_input_v3.csv

CMD ["python", "score_batch_v3.py", "--help"]
