from MLXpress.wine import classification,vis
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
classification(model)

vis(model)
