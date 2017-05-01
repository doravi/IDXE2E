FROM doravidan/testingmachine

COPY ./E2E /Tests

CMD ["python Main.py"]