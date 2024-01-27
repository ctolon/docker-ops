build:
     docker compose build

build-nc:
     docker compose build --no-cache

build-progress:
     docker compose build --no-cache --progress=plain

down-with-volumes:
     docker compose down --volumes

down:
     docker compose --profile flower down

run:
     make down && docker compose --profile flower up

run-scaled:
     make down && docker compose up --scale airflow-worker=3

run-d:
     make down && docker compose --profile flower up -d

stop:
     docker compose stop

logs:
     docker compose logs -f -t --tail 20
