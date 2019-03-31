# Specify a base image
FROM python:3.7-slim-stretch
# minimal Python 3.6 base image


# install some dependencies
RUN pip install -U pip
RUN pip install Flask-RESTful
RUN pip install Flask-JWT
RUN pip install Flask-SQLAlchemy

# Set Working Directory and copy required files - my Python code & files
WORKDIR /usr/app
COPY ./ ./

# Default command
CMD ["python3", "app.py"]