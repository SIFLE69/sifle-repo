import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Assume you have a CSV file with historical stock data, including features and labels.
# Features could be indicators like moving averages, RSI, etc.
# Labels could be binary: 1 for stock going up, 0 for stock going down.

# Load your dataset (replace 'your_data.csv' with your actual file)
data = pd.read_csv('your_data.csv')

# Assuming 'Label' is the column indicating stock movement
labels = data['Label']
features = data.drop('Label', axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
predictions = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")













Replace 'your_data.csv' with your actual dataset file. Also, you may need to adjust the features and labels according to your dataset structure.

Keep in mind that stock market prediction is highly unpredictable, and past performance does not guarantee future results. Use machine learning models cautiously, and consider consulting financial experts before making any investment decisions.