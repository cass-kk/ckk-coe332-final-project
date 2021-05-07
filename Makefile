NSPACE="casskk"
APP="app"
VER="0.2.0"
RPORT="6395"
FPORT="5015"
UID="869425"
GID="816966"

build-db:
	docker build -t ${NSPACE}/${APP}-rd:${VER} \
                     -f docker/Dockerfile.db \
                     ./

build-api:
	docker build -t ${NSPACE}/${APP}-api:${VER} \
                     -f docker/Dockerfile.api \
                     ./

build-worker:
	docker build -t ${NSPACE}/${APP}-worker:${VER} \
                     -f docker/Dockerfile.wrk \
                     ./

clean-db:
	docker ps -a | grep ${NSPACE}-rd | awk '{print $$1}' | xargs docker rm -f

clean-api:
	docker ps -a | grep ${NSPACE}-api | awk '{print $$1}' | xargs docker rm -f

clean-worker:
	docker ps -a | grep ${NSPACE}-worker | awk '{print $$1}' | xargs docker rm -f


build-all: build-db build-api build-worker

clean-all: clean-db clean-api clean-worker


compose-up:
	VER=${VER} docker-compose -f docker/docker-compose.yml pull
	VER=${VER} docker-compose -f docker/docker-compose.yml -p ${NSPACE} up -d --build ${NSPACE}-rd
	VER=${VER} docker-compose -f docker/docker-compose.yml -p ${NSPACE} up -d --build ${NSPACE}-api
	sleep 5
	VER=${VER} docker-compose -f docker/docker-compose.yml -p ${NSPACE} up -d --build ${NSPACE}-wrk

compose-down:
	VER=${VER} docker-compose -f docker/docker-compose.yml -p ${NSPACE} down

k:
	cat deploy/* | TAG=${VER} envsubst '$${TAG}' | yq | kubectl apply -f -

k-del:
	cat deploy/*deployment.yml | TAG=${VER} envsubst '$${TAG}' | yq | kubectl delete -f -
