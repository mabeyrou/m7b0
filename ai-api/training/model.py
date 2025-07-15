import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Chargement et préparation
df = pd.read_csv("adult.csv")
df = df.dropna()
df["income"] = df["income"].map({"<=50K": 0, ">50K": 1})

X = df.drop("income", axis=1)
y = df["income"]

# 2. Encodage des variables catégorielles
X = pd.get_dummies(X)

# 3. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Entraînement
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# 5. Évaluation
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
