FROM python:3.9
RUN pip install --upgrade pip
COPY requirements.txt /home/
RUN pip install -r /home/requirements.txt
COPY *.py /home/
COPY templates/*.* /home/templates/

COPY modules/data/*.py /home/modules/data/*.py
COPY modules/utils/*.py /home/modules/utils/*.py

ENTRYPOINT ["python"]
CMD ["/home/index.py" ]
EXPOSE 80
