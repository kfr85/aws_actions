FROM python:3.7.0
RUN pip install botocore
RUN mkdir /opt/app
WORKDIR /opt/app
COPY ./actions.py /opt/app
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
CMD ["python", "/opt/app/actions.py"]
