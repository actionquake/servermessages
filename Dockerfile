FROM python3
COPY requirements.txt /opt/requirements.txt
COPY messages.py /opt/messages.py
WORKDIR /opt
RUN pip3 install -r requirements.txt