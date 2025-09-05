from sklearn.ensemble import RandomForestClassifier
import pickle

# Dummy simple model
X = [[70, 0, 0, 1], [30, 1, 2, 0], [90, 3, 1, 1], [40, 0, 0, 1]]
y = [0, 1, 1, 0]

model = RandomForestClassifier()
model.fit(X, y)

# Save it
with open('model/phishing_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Dummy model created!")