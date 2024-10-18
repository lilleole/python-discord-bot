FROM pypy:3-slim


WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

CMD [ "python", "./bot.py" ]