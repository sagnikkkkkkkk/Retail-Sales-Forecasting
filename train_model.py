"""Train models for Retail Sales Forecasting and save artifacts.

Usage: python train_model.py
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib


def load_and_prepare(path='data/retail_sales_dummy.csv'):
    df = pd.read_csv(path, parse_dates=['date'])
    df = df.sort_values('date').reset_index(drop=True)
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['weekday'] = df['date'].dt.weekday
    df['is_weekend'] = (df['weekday'] >= 5).astype(int)
    df['dayofyear'] = df['date'].dt.dayofyear
    df['lag_1'] = df['sales'].shift(1).fillna(method='bfill')
    df['rolling_7'] = df['sales'].rolling(7, min_periods=1).mean()
    df['promotion'] = df['promotion'].fillna(0).astype(int)
    return df


def train_and_evaluate(df):
    features = ['dayofyear', 'month', 'weekday', 'is_weekend', 'promotion', 'lag_1', 'rolling_7']
    X = df[features]
    y = df['sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)

    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)

    def metrics(y_true, y_pred):
        return {
            'mae': mean_absolute_error(y_true, y_pred),
            'rmse': mean_squared_error(y_true, y_pred, squared=False),
            'r2': r2_score(y_true, y_pred)
        }

    results = {
        'lr': metrics(y_test, lr_pred),
        'rf': metrics(y_test, rf_pred)
    }

    # Save best model (choose by RMSE)
    best = 'lr' if results['lr']['rmse'] <= results['rf']['rmse'] else 'rf'
    model_to_save = lr if best == 'lr' else rf
    joblib.dump(model_to_save, 'sales_model.joblib')

    # Save test predictions for inspection
    test_out = df.iloc[-len(y_test):].copy()
    test_out['lr_pred'] = lr_pred
    test_out['rf_pred'] = rf_pred
    test_out.to_csv('test_predictions.csv', index=False)

    return results


def main():
    df = load_and_prepare()
    results = train_and_evaluate(df)
    print('Evaluation results:')
    print(results)


if __name__ == '__main__':
    main()
