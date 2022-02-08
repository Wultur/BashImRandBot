FROM python:3.8.5

WORKDIR /BashImRandBot

COPY . /BashImRandBot

RUN pip install pipenv && pipenv install --system --deploy

CMD ["python", "/BashImRandBot/bot.py"]
