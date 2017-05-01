FROM doravidan/testingmachine

COPY /IDX /Tests

CMD ["python Main.py"]