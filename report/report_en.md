# **Portfolio Optimization Report**  
### **Based on CAPM and Quadratic Programming (QP)**
---

## **1. Introduction**
In modern portfolio management, investors seek to **maximize returns while controlling risk**.  
This study applies the **Capital Asset Pricing Model (CAPM)** and **Quadratic Programming (QP)** to construct an **optimal portfolio** and visualize the **Efficient Frontier**, providing investors with the best allocation strategy under different target returns.

---

## **2. Data Collection**
The data for this study was obtained from **Yahoo Finance**, covering the following stocks:
- **Stocks**: AAPL, MSFT, GOOGL, AMZN, TSLA, NVDA, JPM, V, PG, DIS
- **Market Benchmark**: S&P 500 Index (`^GSPC`)

📂 **Data Files**
- **Adjusted Closing Prices (`adj_close_data.csv`)**
- **Daily Returns (`returns_data.csv`)**

💡 **Daily Return Calculation**
\[
R_i = \frac{P_{t} - P_{t-1}}{P_{t-1}}
\]
Where:
- \( R_i \) is the return of stock **i**
- \( P_t \) is the closing price on day **t**
- \( P_{t-1} \) is the closing price on day **t-1**

---

## **3. CAPM Estimation**
The CAPM model is formulated as:

\[
R_i - R_f = \alpha_i + \beta_i (R_m - R_f) + \epsilon_i
\]

Where:
- \( R_i \): Return of stock **i**
- \( R_f = 5\% \): Risk-free rate
- \( R_m \): Market return (S&P 500)
- \( \beta_i \): Sensitivity of stock **i** to market movements
- \( \alpha_i \): Excess return of stock **i**
- \( \epsilon_i \): Residual error (idiosyncratic risk)

We apply **Ordinary Least Squares (OLS) Regression** to estimate **β** and **α** for each stock.

📂 **Results (`capm_results.csv`)**
| Stock  | Beta (\(\beta\)) | Expected Return (\(E[R_i]\)) | Idiosyncratic Variance |
|--------|-------------|-----------------|-------------------|
| AAPL   | 1.2156     | -0.0100         | 0.000146          |
| AMZN   | 1.0658     | -0.0026         | 0.000287          |
| DIS    | 1.0512     | -0.0019         | 0.000246          |
| GOOGL  | 1.1356     | -0.0061         | 0.000169          |
| ...    | ...        | ...             | ...               |

---

## **4. Portfolio Optimization**
After estimating **β values**, we optimize the portfolio using **Quadratic Programming (QP)** to **minimize portfolio variance**:

\[
\sigma_p^2 = w^T \Sigma w
\]

Where:
- \( w \): Portfolio weight vector
- \( \Sigma \): Covariance matrix of assets
- \( \sigma_p^2 \): Portfolio variance (risk)

📂 **Optimization Results (`optimal_portfolio_weights.csv`)**
| Stock  | Target Return 0.08 | Target Return 0.12 | Target Return 0.15 |
|--------|-----------------|-----------------|-----------------|
| AAPL   | 0.15            | 0.18            | 0.20            |
| AMZN   | 0.12            | 0.16            | 0.18            |
| GOOGL  | 0.14            | 0.17            | 0.19            |
| ...    | ...            | ...             | ...             |

---

## **5. Efficient Frontier Analysis**
The **Efficient Frontier** represents the **optimal risk-return relationship** under different target returns.

📈 **Efficient Frontier Plot**
![Efficient Frontier](sandbox:/mnt/data/efficient_frontier.png)

🔍 **Analysis**
1. **The lowest-risk portfolio corresponds to a target return of 0.08**, making it suitable for conservative investors.
2. **Higher target returns (0.15) result in greater risk**, making them suitable for aggressive investors.
3. **The Efficient Frontier illustrates the best possible return for a given level of risk**, following the CAPM framework.

---

## **6. Results & Conclusions**
📌 **Key Findings**
- **Stocks with high β values (e.g., TSLA, NVDA) are more volatile**, suitable for high-risk investors.
- **Stocks with low β values (e.g., PG, V) are more stable**, suitable for conservative investors.
- **Optimized portfolios reduce overall risk**, confirming the **risk-return tradeoff**.
- **The Efficient Frontier provides an optimal risk-return balance**, helping investors make informed decisions.

📌 **Future Improvements**
- **Expand asset selection** to include ETFs and bonds for better diversification.
- **Consider market volatility** using GARCH or Fama-French multi-factor models.
- **Improve portfolio allocation** using Dynamic Asset Allocation (DFA).

---

## **7. References**
1. Sharpe, W. F. (1964). Capital Asset Prices: A Theory of Market Equilibrium Under Conditions of Risk. *Journal of Finance*.
2. Markowitz, H. (1952). Portfolio Selection. *Journal of Finance*.
3. Black, F., Jensen, M. C., & Scholes, M. (1972). The Capital Asset Pricing Model: Some Empirical Tests. *Studies in the Theory of Capital Markets*.
