FROM doravidan/testingmachine

COPY /Tests2 /Tests2

WORKDIR /Tests

#CMD ["python /__init__.py"]