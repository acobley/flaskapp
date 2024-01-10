FROM python:3.9
RUN pip install --upgrade pip
COPY requirements.txt /home/
RUN pip install -r /home/requirements.txt

# Python modules
COPY *.py /home/
COPY modules/data/*.py /home/modules/data/
COPY modules/utils/*.py /home/modules/utils/

# Webpage
COPY templates/*.* /home/templates/
COPY ./css/*.css /home/css/

ENTRYPOINT ["python"]
CMD ["/home/index.py" ]
EXPOSE 80
