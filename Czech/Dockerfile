FROM python:3.10

WORKDIR /home
RUN mkdir WP
RUN mkdir DB
ADD backuper.py .
ADD mysqldump.py .
ADD cislo.txt .
ADD datumacas.py .
ADD filer.py .
ADD pocitadlo.py .
ADD smtp.py .

RUN pip install dkimpy secure-smtplib pytz pyocclient

RUN apt-get update \
    && apt-get install -y default-mysql-client

CMD ["python","-u","backuper.py"]
