FROM doravidan/testingmachine

COPY IDX/E2E /Tests

CMD ["python Main.py"]