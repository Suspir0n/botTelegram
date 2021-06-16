FROM python:3
ADD requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
ENV FLASK_APP=app
CMD ["-m" , "flask", "run", "--host=0.0.0.0"]