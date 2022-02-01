FROM prefecthq/prefect:latest

WORKDIR /APP

COPY . .

RUN pip install -U .

RUN pip install -r requirements.txt