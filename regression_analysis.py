import sys
sys.path.insert(0, r'C:\Users\BÜŞRA\OneDrive\Masaüstü\data-orders')

from olist.order import Order
import pandas as pd
import statsmodels.api as sm

df = Order().get_training_data()
df = df[['wait_time', 'delay_vs_expected', 'review_score']].dropna()

# 1. Tek degiskenli: wait_time
X1 = sm.add_constant(df['wait_time'])
model1 = sm.OLS(df['review_score'], X1).fit()
print("=== wait_time ===")
print(model1.summary())

# 2. Tek degiskenli: delay_vs_expected
X2 = sm.add_constant(df['delay_vs_expected'])
model2 = sm.OLS(df['review_score'], X2).fit()
print("\n=== delay_vs_expected ===")
print(model2.summary())

# 3. Cok degiskenli
X3 = sm.add_constant(df[['wait_time', 'delay_vs_expected']])
model3 = sm.OLS(df['review_score'], X3).fit()
print("\n=== Cok Degiskenli ===")
print(model3.summary())