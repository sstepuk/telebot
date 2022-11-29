FROM python:3.9.6
ENV TOKEN=''
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py
