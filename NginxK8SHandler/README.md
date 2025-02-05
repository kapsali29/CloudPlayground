# Universal API (UA)
### Description
This is a facade API in which all metric management modules are getting registered. It leverages kubernetes Python client
to create and patch configmaps for NGINX reverse proxy to register and expose different EMDC metric APIs.
#### Core Components
+ `MongoDB`
+ `NGINX`
#### Python Libraries
+ `Python 3.9`
+ `Kubernetes Python Client`
+ `FastAPI`
+ `pymongo`
+ `uvicorn`

### Installation Steps
```shell
cd config/k8s/
kubectl apply -f cluster-role.yaml
cd nginx/
kubectl apply -f .
cd ..
cd mongodb/
kubectl apply -f .
cd ..
cd ua/
kubectl apply -f .
```
### Expose Services
```shell
kubectl port-forward svc/ua 7000:8000
kubectl port-forward svc/nginx-project 8080:80
```
### LICENSE
`This project is licensed under BSD`
