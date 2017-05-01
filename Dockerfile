FROM doravidan/testingmachine

COPY /IDX /Tests

WORKDIR /IDX

CMD ["python Main.py"]