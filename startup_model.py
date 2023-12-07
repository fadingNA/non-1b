import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression

df = pd.read_csv('./data/50_Startups.csv')
# independent variables (R&D, Admin, Marketing, State)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values  # dependent variable (profit)

# Encoding categorical data

ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

X_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)
print(X)
# Multiple Linear Regression does not require feature scaling
# because the coefficients of the independent variables will compensate for the different scales
# However, feature scaling is required for the dependent variable
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.score(x_test, y_test))


for i in range(0, 9):
    print(f"Predicted: {regressor.predict([x_test[i]])[0]}")
    print(f"Actual: {y_test[i]}")
    print(f"Error: {regressor.predict([x_test[i]])[0] - y_test[i]}")
    print("")

# Predicting the Test set results
y_pred = regressor.predict(x_test)
np.set_printoptions(precision=2)  # 2 decimal places
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(
    len(y_test), 1)), 1))  # concatenate the vectors vertically


# Backward Elimination
def backward_elimination(X, nums):
    X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis=1)
    X_opt = X[:, nums]
    # Ordinary Least Squares (OLS) model
    X_opt = X_opt.astype(np.float64)  # convert to float64 to avoid error
    # fit the full model with all possible predictors
    regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
    summary = regressor_OLS.summary()  # get the summary of the model
    print(summary)
    return summary


for i in range(0, 5):
    backward_elimination(X, [0, 1, 2, 3, 4, 5])

"""
Question 1: How do I use my multiple linear regression model to make a single prediction, 
for example, the profit of a startup with R&D Spend = 160000, Administratio nn Spend = 130000,
 Marketing Spend = 300000 and State = California?

Question 2: How do I get the final regression equation y = b0 + b1 x1 + b2 x2 + ... 
with the final values of the coefficients?
"""

# New data point with spends and state
new_data = np.array([[160000, 130000, 300000, 'California']])

# The array should be of type object so that it can contain both numeric and string types
new_data = new_data.astype(object)

# Transforming the new data with the column transformer to encode 'State'
# Since we've already fit the transformer, we can use it to transform new data points
new_data_transformed = ct.transform(new_data)

# Make a prediction with the transformed data
profit_prediction = regressor.predict(new_data_transformed)
print(f"Profit prediction: {profit_prediction[0]}")