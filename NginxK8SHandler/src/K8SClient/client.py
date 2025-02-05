from kubernetes import config, dynamic
from kubernetes.client import api_client

from .utils import nginx


class K8SClient(object):
    def __init__(self):
        self.client = dynamic.DynamicClient(
            api_client.ApiClient(configuration=config.load_incluster_config())
        )
        self.config_map_api = self.client.resources.get(api_version="v1", kind="ConfigMap")

    @staticmethod
    def manifest_base(configmap_name):
        configmap_manifest = {
            "kind": "ConfigMap",
            "apiVersion": "v1",
            "metadata": {"name": configmap_name},
            "data": {}
        }
        return configmap_manifest

    @staticmethod
    def set_location(
            path,
            svc,
            port
    ):
        this_location = nginx.Location(
            '/' + f'{path}' + '/',
            nginx.Key('rewrite', '/' + f'{path}' + '/(.*)  /$1 break'),
            nginx.Key('proxy_pass', f'http://{svc}:{port}')
        )
        return this_location

    def get_configmap(
            self,
            config_map_name,
            namespace="default"
    ):
        result = self.config_map_api.get(
            name=config_map_name,
            namespace=namespace
        )
        return result

    def patch_configmap(
            self,
            config_map_name,
            configmap_manifest,
            namespace="default"
    ):
        update_configmap = self.config_map_api.patch(
            name=config_map_name,
            namespace=namespace,
            body=configmap_manifest
        )

    def create_nginx_conf(
            self,
            configmap_name,
            list_of_svcs
    ):
        configmap_manifest = self.manifest_base(configmap_name)
        nginx_conf = nginx.Conf()
        nginx_server = nginx.Server()
        nginx_server.add(nginx.Key('listen', '80'))
        for svc_details in list_of_svcs:
            nginx_server.add(self.set_location(
                svc_details['path'],
                svc_details['host'],
                svc_details['port']
            ))
        nginx_conf.add(nginx_server)
        configmap_manifest["data"]["nginx.conf"] = " ".join(nginx_conf.as_strings)
        self.patch_configmap(
            config_map_name=configmap_name,
            configmap_manifest=configmap_manifest
        )
        return nginx_conf
