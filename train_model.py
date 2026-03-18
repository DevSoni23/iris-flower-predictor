# train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# 2. Create and train the model (The "Brain")
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# 3. Save the model to a file named 'model.pkl'
joblib.dump(model, 'model.pkl')

print("Success! 'model.pkl' has been created in your folder.")
