from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from truss import create

iris = load_iris()
data_x = iris['data']
data_y = iris['target']
model = RandomForestClassifier()
model.fit(data_x, data_y)

tr = create(model, target_directory="sklearn_truss")


# truss predict --target_directory sklearn_truss --request '[[0, 0, 0, 0]]'