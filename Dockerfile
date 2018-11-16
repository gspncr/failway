FROM python:alpine3.7
ADD https://raw.githubusercontent.com/gspncr/failway/master/nr.py /app/
ADD https://raw.githubusercontent.com/gspncr/failway/master/layout.html /app/templates/
ADD https://raw.githubusercontent.com/gspncr/failway/master/layout.html /app/templates/
ADD https://raw.githubusercontent.com/gspncr/failway/master/500.html /app/templates/
ADD https://raw.githubusercontent.com/gspncr/failway/master/404.html /app/templates/
RUN pip install flask beautifulsoup4
EXPOSE 80
CMD python3 ./app/nr.py
