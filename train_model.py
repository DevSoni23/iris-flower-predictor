
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)
joblib.dump(model, 'model.pkl')
print("Success! 'model.pkl' has been created in your folder.")
