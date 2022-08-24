up:
	@ docker-compose up -d

down:
	@ docker-compose down

build:
	@  docker-compose build --no-cache

build-and-run:
	@ docker-compose up -d --no-deps --build --force-recreate  --remove-orphans