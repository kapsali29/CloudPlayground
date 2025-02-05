helm repo add dask https://helm.dask.org/
helm repo update
helm install dask-kubernetes-operator dask/dask-kubernetes-operator --version 2024.3.1
