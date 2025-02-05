# Istio Installation Steps
```shell
cd config/
```
### Install Istio CLI
```shell
curl -L https://istio.io/downloadIstio | sh -
cd istio-<version>  # Go to the Istio package directory
export PATH=$PWD/bin:$PATH  # Add istioctl to your PATH
```

### Install Istio in the Cluster
```shell
istioctl install --set profile=default -y
```

### Enable Automatic Sidecar Injection
```shell
kubectl label namespace default istio-injection=enabled
```

### Install Prometheus
```shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/prometheus --version 25.0.0 -n istio-system --set prometheus-node-exporter.hostRootFsMount.enabled=false
```

### Install Kiali
```shell
kubectl apply -f kiali/kiali.yaml
```
visualize the mesh  using the following command

```shell
istioctl dashboard kiali
```