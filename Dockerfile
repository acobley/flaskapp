FROM python:3.9
RUN pip install --upgrade pip
COPY flaskapp/requirements.txt /home/flaskapp
RUN pip install -r /home/flaskapp/requirements.txt
COPY *.py /home/
COPY flaskapp/templates/*.* /home/flaskapp/templates/
ENTRYPOINT ["python"]
CMD ["/home/flaskapp/index.py" ]
EXPOSE 5000
