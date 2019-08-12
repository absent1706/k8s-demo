FROM python:3.7

# flower dependencies
RUN pip install flower

EXPOSE 5555
COPY . .
# note that we run fixed version of flower
# see fix in flower/command.py:64
CMD ["python", "-m" , "flower"]
