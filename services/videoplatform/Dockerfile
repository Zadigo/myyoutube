FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Build the container with another user
# in order to prevent permission errors since
# everytime a file is created by containers,
# it creates them as 'root'
# ENV USER=ubuntu

# Create group
# RUN groupadd --gid 1000 ${USER}
# Create user (based on the current gid
# of the user on the server ex. id ubuntu)
# RUN useradd --uid 1000 --gid 1000 --base-dir /code --home-dir /code ${USER}

# Install/Update Pip
RUN pip install --upgrade pip
RUN pip3 install pipenv

WORKDIR /code

# Install dependencies
COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy

COPY . .

EXPOSE 8000

# Change the ownership to the other user
# RUN chown -R ${USER}:${USER} /code

# USER ${USER}

# Development
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

# Production
# CMD gunicorn prosite.wsgi -w 4 -b 0.0.0.0:8000 --log-level=debug --access-logfile=gunicorn_access.log --log-file=gunicorn.log
