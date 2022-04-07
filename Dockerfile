FROM python:3.10.4-alpine3.15

WORKDIR /usr/hoge/hoge

COPY . .

RUN pip install py-cord --pre
RUN pip install mcrcon
RUN pip install python-dotenv

CMD ["python3","main.py"]