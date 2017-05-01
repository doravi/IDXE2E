FROM doravidan/testingmachine

COPY E2E E2E

CMD ["python Main.py"]