FROM doravidan/testingmachine

RUN sudo apt-get install python-pip python-dev build-essential -y

RUN sudo pip install --upgrade pip

RUN sudo pip install requests

COPY /Tests2 /Tests2

WORKDIR /Tests2

CMD ["python2.7 Main.py"]