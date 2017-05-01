FROM doravidan/testingmachine

RUN sudo apt-get install python-pip python-dev build-essential -y

RUN sudo pip install --upgrade pip

COPY /Tests2 /Tests2

#CMD ["python /Main.py"]