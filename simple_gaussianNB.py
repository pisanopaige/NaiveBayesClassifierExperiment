from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

# Load breast cancer data
breast_cancer_data = load_breast_cancer()
x = breast_cancer_data.data
y = breast_cancer_data.target

# Split into train and test datasets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# Train GaussianNB model using train datasets
classifier = GaussianNB()
classifier.fit(x_train, y_train)

# Make predictions using test datasets and evaluate how well the model does
y_pred = classifier.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
confusionMatrix = confusion_matrix(y_test, y_pred)

print(accuracy)
print(confusionMatrix)