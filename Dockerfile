
# Use an official Python runtime as a parent image
FROM python:3.7

ENV PYTHONUNBUFFERED 1

# Set the working directory to /code
RUN mkdir /code

WORKDIR /code



# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


