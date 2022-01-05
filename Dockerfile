FROM python:latest
RUN mkdir /app
COPY ./src /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python bot.py $discord_token
