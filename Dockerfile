FROM python:3.9

WORKDIR /projeto

COPY ./requirements.txt /projeto/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /projeto/requirements.txt

COPY ./app /projeto/app

CMD ["uvicorn main:app --reload"]