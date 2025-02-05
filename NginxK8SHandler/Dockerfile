FROM python:3.9-slim
WORKDIR  /ua
COPY  ./pyproject.toml  ./poetry.lock ./
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
COPY ./src .

RUN poetry install
EXPOSE 8000
ENTRYPOINT ["poetry", "run", "uvicorn", "api:app", "--port", "8000", "--reload", "--host", "0.0.0.0"]