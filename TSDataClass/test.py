# {
#     "id": 1,
#     "point": "{'time': '2024-01-01T00:00:00Z', 'value': 2}"
# }
# {
#     "id": 1,
#     "point": "{'time': '2024-01-01T01:00:00Z', 'value': 3}"
# }
# {
#     "id": 1,
#     "point": "{'time': '2024-01-01T02:00:00Z', 'value': 3}"
# }
# {
#     "id": 1,
#     "point": "{'time': '2024-01-01T03:00:00Z', 'value': 3}"
# }
# {
#     "id": 1,
#     "point": "{'time': '2024-01-01T04:00:00Z', 'value': 4}"
# }
# {
#     "id": 1,
#     "point": "{'time': '2024-01-01T05:00:00Z', 'value': 4}"
# }
import json


# problem 1
class MyDataClass(object):
    def __init__(self):
        self.this_list = []

    def insert_(self, time_id, dict_data_point):
        str_date = dict_data_point["time"]
        dict_data_point["time"] = str_date.strftime("timestamp_format")
        self.this_list.append({
            "id": time_id,
            "point": dict_data_point
        })

    def append(self, time_id, data_point):
        dict_data_point = json.loads(data_point)
        if self.this_list:
            my_sensor_tms = self.get_id_tms(time_id=time_id)
            if my_sensor_tms[time_id][-1]["value"] == dict_data_point["value"]:
                pass
            else:
                self.insert_(
                    time_id,
                    dict_data_point
                )
        else:
            self.insert_(
                time_id, dict_data_point
            )

    def get_id_tms(self, time_id):
        output = {
            f"{time_id}": [
               item["point"]for item in self.this_list if item["id"] == time_id
            ]
        }
        return output

    def get_id_tms_decompressed(self, time_id):
        decompressed_tms = []
        compressed_tms = self.get_id_tms(time_id)["time_id"]
        old_date = compressed_tms[0]["time"]
        for idx in range(1, len(compressed_tms)):
            current_date = compressed_tms[idx]["time"]
            timedelta_in_hrs = current_date - old_date
            if timedelta_in_hrs >1:
                for i in int(timedelta_in_hrs):





this_data_class = MyDataClass()


def store_next_value(time_series_id: str, point: str):
    this_data_class.append(time_series_id, point)


store_next_value("1", '{"time": "2024-01-01T00:00:00Z", "value": 2}')
store_next_value("1", '{"time": "2024-01-01T01:00:00Z", "value": 3}')
store_next_value("1", '{"time": "2024-01-01T02:00:00Z", "value": 3}')
store_next_value("1", '{"time": "2024-01-01T03:00:00Z", "value": 3}')
store_next_value("1", '{"time": "2024-01-01T04:00:00Z", "value": 4}')


# problem 2
# print(this_data_class.get_id_tms(time_id="1"))

# problem 3
print(this_data_class.this_list)
