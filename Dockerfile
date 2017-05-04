FROM doravidan/testingmachine

RUN sudo apt-get install python-pip python-dev build-essential -y

RUN sudo pip install --upgrade pip

RUN sudo pip install requests

RUN sudo pip install paramiko

COPY /Tests2 /Tests2

RUN sudo chmod 777 /Tests2

WORKDIR /Tests2

RUN sudo -s

CMD sudo python2.7  '/Tests2/Main.py'
