FROM python:3.9.6
ENV TOKEN='5833600323:AAEnpFPbuxWjKLqEqvfeeYXBEZeUiWMrdiE'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py