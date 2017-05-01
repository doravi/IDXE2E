FROM doravidan/testingmachine

COPY /IDX /Tests

CMD ["python ~/IDX/Main.py"]