```shell
docker build -f nginx/Dockerfile -t pkapsalismartel/auto-reload-nginx .
docker tag pkapsalismartel/auto-reload-nginx:latest pkapsalismartel/auto-reload-nginx:v0.2
docker push pkapsalismartel/auto-reload-nginx:v0.2
```