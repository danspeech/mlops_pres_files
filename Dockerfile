# Start from the official Python base image.
FROM python:3.8

# Set the current working directory to /code.
# This is where we'll put the requirements.txt file and the app directory.
WORKDIR /code

# Copy the file with the requirements to the /code directory.
COPY ./requirements.txt /code/requirements.txt

# Install dependencies through the requirements.txt file
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the relevant files inside the /code directory.
COPY ./api.py /code/api.py
COPY ./model.py /code/model.py
COPY ./api_models.py /code/api_models.py

# Make sure that port 8080 is exposed
EXPOSE 8080

# CMD takes a list of strings, each of these strings is what you would type in the command line separated by spaces.
CMD ["uvicorn", "api:api", "--host", "0.0.0.0", "--port", "8080"]
