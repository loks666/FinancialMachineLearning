### 📌 **Portfolio Optimization Using CAPM and Mean-Variance Optimization (MVO) [Chinese](README.md)**

## 📖 **1. Project Overview**
This project applies the **Capital Asset Pricing Model (CAPM)** and **Mean-Variance Optimization (MVO)** using **Quadratic Programming (QP)** to compute the optimal portfolio allocation.  
Project objectives:
- **Calculate CAPM parameters (β values, expected returns, and idiosyncratic risk)**
- **Optimize portfolio weights to minimize risk**
- **Plot the Efficient Frontier to analyze the risk-return tradeoff**

---

## 🏗 **2. Project Structure**
```
📂 FinancialMachineLearning
│── 📂 doc                     # Project documentation
│   │── 📜 CF969.pdf           # Reference materials
│── 📂 report                  # Research reports
│   │── 📜 report_cn.md        # Chinese report
│   │── 📜 report_en.md        # English report
│── 📂 result                  # Computed results
│   │── 📜 adj_close_data.csv  # Adjusted close price data
│   │── 📜 capm_results.csv    # CAPM calculation results
│   │── 📜 efficient_frontier.png # Efficient frontier plot
│   │── 📜 optimal_portfolio_weights.csv # Optimized portfolio weights
│   │── 📜 returns_data.csv    # Daily returns data
│── 📜 .gitignore              # Git ignore file
│── 📜 all_code.png            # Screenshot of all code
│── 📜 financial.ipynb         # **Jupyter Notebook containing all code**
│── 📜 README.md               # Readme (Chinese)
│── 📜 README_en.md            # Readme (English)
```

---

## ⚙️ **3. Environment Setup**
### 🔹 **3.1 Creating a Conda Virtual Environment**
This project runs on **Python 3.12.7**, and it is recommended to use Conda for environment management:
```bash
conda create -n financial python=3.12.7
conda activate financial
```
### 🔹 **3.2 Installing Dependencies**
```bash
pip install -r requirements.txt
```
or manually install:
```bash
pip install numpy pandas matplotlib statsmodels cvxopt yfinance
```

---

## 🚀 **4. Running the Project**
All code is contained in `financial.ipynb`, which includes **data downloading, CAPM calculations, portfolio optimization, and visualization**.  
Follow the steps below:

### 🔹 **4.1 Start Jupyter Notebook**
```bash
jupyter lab
```
or:
```bash
jupyter notebook
```
Then open `financial.ipynb` and run the code step by step.

### Code Execution Screenshot
![all_code.png](all_code.png)

---

### 🔹 **4.2 Main Workflow**
1️⃣ **Data Downloading**
   - Fetch **historical stock closing prices** from Yahoo Finance
   - Compute **daily returns**
   - Generate `adj_close_data.csv` and `returns_data.csv`

2️⃣ **CAPM Calculation**
   - Compute **β values (Beta), expected returns, and idiosyncratic variance**
   - Store results in `capm_results.csv`

3️⃣ **Portfolio Optimization**
   - Use **Quadratic Programming (QP)** to determine optimal weights
   - Target returns: **0.08, 0.12, 0.15**
   - Generate `optimal_portfolio_weights.csv`

4️⃣ **Plotting the Efficient Frontier**
   - Compute **portfolio risk**
   - Generate **efficient frontier plot `efficient_frontier.png`**

---

## ❗ **5. Issues Encountered and Solutions**
During the computations, several key issues were encountered. Below is a summary of the problems and the corresponding solutions:

### 🔹 **5.1 `cvxopt.solvers.qp()` Encountered Singular KKT Matrix**
#### **Issue**
While executing `cvxopt.solvers.qp()`, an error `singular KKT matrix` occurred.  
**Causes:**
- The covariance matrix `Σ` was **non-invertible**, making the optimization problem unsolvable.
- The stock return data had **high multicollinearity**, meaning returns were highly correlated, causing the matrix determinant to approach zero.

#### **Solution**
- Compute the covariance matrix using **NumPy's `np.outer`**, instead of using `for` loops, to improve numerical stability:
  ```python
  beta_matrix = np.array([beta_values[stock] for stock in stock_list])
  idiosyncratic_var_vector = np.array([idiosyncratic_variance[stock] for stock in stock_list])
  covariance_matrix = np.outer(beta_matrix, beta_matrix) * market_variance
  np.fill_diagonal(covariance_matrix, np.diag(covariance_matrix) + idiosyncratic_var_vector)
  ```
- If the covariance matrix remains non-invertible, **add a small regularization term**:
  ```python
  covariance_matrix += np.eye(len(stock_list)) * 1e-6  # Add small regularization term
  ```

---

### 🔹 **5.2 `A` Constraint Matrix Dimension Mismatch**
#### **Issue**
An error `TypeError: 'A' must be a 'd' matrix with n columns` occurred while solving the quadratic programming problem.

#### **Cause**
- The `A` matrix shape was **incorrect**, it should be **(2 × num_assets)**, but it was mistakenly **(num_assets × 2)**.

#### **Solution**
- Ensure the shape of `A` is **(2 × num_assets)**:
  ```python
  A = matrix(np.vstack((np.ones(num_assets), [expected_returns[stock] for stock in stock_list])), tc='d').T
  ```
- Ensure `b` is also of type `double`:
  ```python
  b = matrix([1.0, mu_p], tc='d')
  ```

---

### 🔹 **5.3 Negative Portfolio Weights Issue**
#### **Issue**
Some optimal portfolio weights were **negative**, implying **short-selling**, which was **not allowed** in this optimization.

#### **Solution**
- Use **absolute values** to fix negative weights:
  ```python
  weights = np.abs(weights)
  ```
- **Normalize** weights so they sum up to 1:
  ```python
  weights /= np.sum(weights)
  ```

---

### 🔹 **5.4 Dimension Error in `portfolio_variance` Calculation**
#### **Issue**
The operation `weights.T @ covariance_matrix @ weights` caused a **shape mismatch error**.

#### **Solution**
- Use `np.dot()` to ensure correct matrix multiplication:
  ```python
  portfolio_variance = np.dot(weights.T, np.dot(covariance_matrix, weights))
  ```

---

### 🔹 **5.5 `market_variance` Computation Issue**
#### **Issue**
When calculating `market_variance = np.var(market_returns)`, **data type conversion errors** occurred, causing incorrect computations.

#### **Solution**
- Explicitly convert `market_returns` to `float64`:
  ```python
  market_variance = np.var(market_returns.astype(np.float64))
  ```

---

## 🎯 **6. Future Improvements**
✅ **Expand asset classes**, including bonds and ETFs for better diversification  
✅ **Incorporate market volatility changes**, such as using **GARCH models or Fama-French factor models**  
✅ **Enhance portfolio weight optimization** with **Dynamic Factor Allocation (DFA) strategies**  

---

## 📬 **7. Contact & Contributions**
🔹 **Email:** [generalfly666@outlook.com](mailto:generalfly666@outlook.com)  
🔹 **GitHub:** [GitHub Repository](https://github.com/loks666)  
🔹 **Contributing:** Fork this repository and submit a Pull Request.  

---

🚀 **This project enhances CAPM calculations and portfolio optimization—collaborations and improvements are welcome!** 😊