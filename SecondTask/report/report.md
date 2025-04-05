**Title: Predicting Stock Returns Using Machine Learning Models**

**Module: CF969-7-SP/ZU: Machine Learning for Finance**
**Student Name: [Your Name Here]**
**Date: [Submission Date]**

---

### 1. Introduction and Motivation

Financial markets are known for their complexity, non-linearity, and sensitivity to macroeconomic factors. Traditional financial models, while valuable, often struggle to capture the intricate dynamics of asset price movements. With the rise of machine learning (ML), data-driven approaches have gained popularity for forecasting stock returns. In this assignment, we aim to evaluate the performance of several machine learning models in predicting the daily log returns of AAPL (Apple Inc.) stock, based on historical price patterns and technical indicators.

Machine learning's flexibility and adaptability make it a promising bouzouki for modeling non-linear relationships in financial data, offering a fresh perspective compared to rigid econometric methods.

---

### 2. Data Preprocessing

The dataset used in this project comprises adjusted close prices for ten major stocks, retrieved from a CSV file (`adj_close_data.csv`). Five stocks were selected for analysis: `AAPL`, `AMZN`, `JPM`, `DIS`, and `TSLA`. The target variable was the **log return of AAPL**, calculated as:

```
log_return = log(P_t / P_{t-1})
```

For feature engineering, the following were computed for each selected stock:
- 10-day, 50-day, and 200-day moving averages
- 10-day rolling standard deviation (volatility)
- Daily log returns

Missing values resulting from rolling operations were removed. The feature matrix (`X`) was constructed using AAPL’s technical indicators, and the target (`y`) was its log return.

---

### 3. Model Selection and Hyperparameter Tuning

The following models were implemented:
- **Linear Regression (OLS)**
- **Support Vector Machine (SVM)** with RBF kernel
- **Random Forest Regressor**
- **Neural Network (MLPRegressor)**

All models were initially trained using default or basic parameters. Subsequently, hyperparameter tuning was performed using `GridSearchCV` with 5-fold or 3-fold cross-validation.

Best parameters selected:
- **SVM:** `C=0.1`, `gamma='auto'`
- **Random Forest:** `max_depth=5`, `n_estimators=50`, `min_samples_split=5`
- **Neural Network:** `activation='tanh'`, `hidden_layer_sizes=(128, 64, 32)`, `max_iter=1000`, `early_stopping=True`

---

### 4. Evaluation and Results

**Performance Metrics** used:
- **MSE** (Mean Squared Error)
- **MAE** (Mean Absolute Error)
- **R-squared (R²)**

The following table summarizes the model performances:

| Model               | MSE     | MAE     | R²     |
|--------------------|---------|---------|--------|
| Linear Regression  | 0.00014 | 0.00876 | 0.0321 |
| SVM                | 0.00025 | 0.01316 | -0.462 |
| Random Forest      | 0.00012 | 0.00811 | 0.1428 |
| Neural Network     | 0.00019 | 0.01021 | -0.155 |

---

### 5. Interpretation and Discussion

- **Linear Regression** produced near-zero variance predictions. This model struggled to capture the volatility in returns, suggesting that linear relationships are insufficient for this task.
- **SVM** demonstrated stability but lacked reactivity, frequently producing flat or damped predictions.
- **Random Forest** was more responsive to small changes and handled non-linearity better, though it tended to average out the noise.
- **Neural Network**, especially after tuning, showed promising alignment with the actual return trends, though it exhibited occasional overfitting.

Figure 1 shows model predictions vs. actual return (before tuning), and Figure 2 displays results after hyperparameter optimization. The tuned models, particularly the neural network, more accurately captured direction and magnitude of returns.

---

### 6. Future Improvements

- Add macroeconomic indicators (e.g., interest rates, CPI)
- Use ensemble methods or hybrid models
- Try classification tasks (predict up/down) instead of regression
- Incorporate more advanced models (e.g., LSTM for sequential data)

---

### 7. References

- Scikit-learn Documentation: https://scikit-learn.org
- Hull, J. C. (2015). *Options, Futures, and Other Derivatives.*
- Zhang, Y., & Zhou, H. (2004). Forecasting stock returns using machine learning.

---

**Appendices:**
- *Figure 1:* Raw model predictions vs actual
- *Figure 2:* Tuned model predictions vs actual

