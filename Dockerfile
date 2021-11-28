FROM python:latest
RUN mkdir /app
ADD ./src /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python bot.py $discord_token