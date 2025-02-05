from K8SClient.client import K8SClient

k = K8SClient()

res = k.create_nginx_conf(
    configmap_name="nginx-conf",
    list_of_svcs=[
        {"host": "httpbin.default.svc.cluster.local", "port": 5000, "path": "httpbin"},
        {"host": "nodeserver.default.svc.cluster.local", "port": 5000, "path": "nodeserver"}
    ]
)
