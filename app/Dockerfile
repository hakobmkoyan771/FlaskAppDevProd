FROM python

USER 0

COPY ./app.py /app/

RUN pip install flask

RUN pip install argparse

CMD ["python3", "/app/app.py", "--deb", "$DEBUG"]
