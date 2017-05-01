FROM doravidan/testingmachine

COPY /Tests2 /Tests

WORKDIR /Tests

#CMD ["python /__init__.py"]