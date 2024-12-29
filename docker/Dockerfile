FROM continuumio/miniconda3:latest

RUN conda update -n base -c defaults conda

WORKDIR /data/

COPY ./requirements.yml /data/requirements.yml

RUN conda env update -n base -f /data/requirements.yml

# COPY ./app /code/app

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# CMD ["fastapi", "run", "app/main.py", "--port", "80"]