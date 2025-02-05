import pymongo


class MongoDBClient(object):
    def __init__(
            self,
            mongo_uri,
            database_name="aces",
            collection_name="emdcs"
    ):
        self.__conn = pymongo.MongoClient(mongo_uri)
        self.db = self.__conn[database_name]
        self.collection = self.db[collection_name]

    def get_collections_(self):
        collection_names_ = self.db.list_collection_names()
        return collection_names_

    def insert(self, obj_dict):
        self.collection.insert_one(obj_dict)

    def insert_many_(self, df):
        df = df.to_dict('records')
        self.collection.insert_many(df)

    def close_connection(self):
        self.__conn.close()

    def get_metric_details(self):
        metrics_apis = [
            record["metrics"]
            for record in self.collection.find({}, {"metrics": 1})
        ]
        return metrics_apis

    def get_all_emdcs(self):
        emdcs = [
            record
            for record in self.collection.find({}, {"_id": 0})
        ]
        return emdcs