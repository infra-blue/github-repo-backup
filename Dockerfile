FROM python:3-slim
WORKDIR /github-repo-backup/

RUN apt-get -y update
RUN apt-get -y install git

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3","-u" ,"main.py"]