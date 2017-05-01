FROM doravidan/testingmachine

COPY /Tests /Tests

WORKDIR /Tests

#CMD ["python /Main.py"]