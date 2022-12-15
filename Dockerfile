FROM python:3.10
EXPOSE 5000

WORKDIR /app
RUN pip install -U pip
RUN curl -sSL https://install.python-poetry.org | python
ENV PATH="$PATH:/root/.local/bin"
RUN poetry config virtualenvs.create false
COPY . .
RUN poetry install
CMD [ "flask", "run"]