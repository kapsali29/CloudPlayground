import os

MONGODB_HOSTNAME = os.environ.get('MONGODB_HOST', 'mongodb.default.svc.cluster.local')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_URI = f"mongodb://{MONGODB_HOSTNAME}:{MONGO_PORT}"
