import sys
import logging

from fastapi import FastAPI

from pydantic import BaseModel, Field
from starlette.middleware.cors import CORSMiddleware

from MongoObject.client import MongoDBClient
from K8SClient.client import K8SClient

from settings import MONGO_URI

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

tags_metadata = [
    {"name": "EMDC Registration", "description": "EMDC Registration APIs"},
]

app = FastAPI(openapi_tags=tags_metadata)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MetricsApiBody(BaseModel):
    host: str = Field(..., description="host name or svc name")
    port: int = Field(..., description="port name")
    path: str = Field(..., description="desired path")


class EMDCBody(BaseModel):
    name: str = Field(..., description="EMDC ID")
    location: str = Field(..., description="EMDC Location")
    node_count: int = Field(..., description="Number of nodes in EMDC")
    metrics_api: MetricsApiBody


@app.post('/register/emdc', tags=["EMDC Registration"])
def set_emdc(emdc: EMDCBody):
    mclient = MongoDBClient(mongo_uri=MONGO_URI)
    kclient = K8SClient()
    emdc_document = {
        "name": emdc.name,
        "location": emdc.location,
        "node_count": emdc.node_count,
        "metrics": {
            "host": emdc.metrics_api.host,
            "port": emdc.metrics_api.port,
            "path": emdc.metrics_api.path
        }
    }
    mclient.insert(emdc_document)
    metrics_apis = mclient.get_metric_details()
    mclient.close_connection()
    res = kclient.create_nginx_conf(
        configmap_name="nginx-conf",
        list_of_svcs=metrics_apis
    )
    return {"msg": f"EMDC: {emdc.name} inserted"}


@app.get('/emdcs', tags=["EMDC Registration"])
def get_emdcs():
    mclient = MongoDBClient(mongo_uri=MONGO_URI)
    emdc_list = mclient.get_all_emdcs()
    return emdc_list

# uvicorn api:app --reload --host 0.0.0.0
