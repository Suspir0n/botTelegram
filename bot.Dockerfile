FROM python:3
ADD requirements.txt /bot/requirements.txt
WORKDIR /bot/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["./bot/bot_telegram.py"]