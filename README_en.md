# 📌 **Portfolio Optimization Based on CAPM and Mean-Variance Optimization (MVO) [Chinese](README_cn.md)**
--- 

## 📖 **1. Project Overview**
This project applies the **Capital Asset Pricing Model (CAPM)** and **Mean-Variance Optimization (MVO)** to compute the optimal investment portfolio using **Quadratic Programming (QP)**.

### Project Goals:
- **Calculate CAPM parameters (β value, expected return, idiosyncratic risk)**
- **Optimize portfolio weights to minimize risk**
- **Plot the Efficient Frontier to analyze risk-return trade-offs**

---

## 🏗 **2. Project Structure**
```
📂 FinancialMachineLearning
│── 📂 doc                     # Project Documentation
│   │── 📜 CF969.pdf           # Report Example
│   │── 📜 CF969 - SP ZU - Assignment.pdf # Assignment Requirements
│── 📂 report                  # Research Reports
│   │── 📜 report_cn.md        # Chinese Report
│   │── 📜 report_en.md        # English Report
│   │── 📜 capm_regression_*.png # CAPM Regression Analysis Charts
│   │── 📜 efficient_frontier.png # Efficient Frontier Chart
│   │── 📜 idiosyncratic_risk.png # Idiosyncratic Risk Bar Chart
│   │── 📜 optimal_portfolio_weights.png # Optimal Portfolio Weights Chart
│── 📂 result                  # Computation Results
│   │── 📜 adj_close_data.csv  # Adjusted Closing Price Data
│   │── 📜 capm_results.csv    # CAPM Calculation Results
│   │── 📜 efficient_frontier.png # Efficient Frontier Chart
│   │── 📜 optimal_portfolio_weights.csv # Optimal Portfolio Weights
│   │── 📜 returns_data.csv    # Daily Returns Data
│── 📜 .gitignore              # Git Ignore File
│── 📜 all_code.png            # Code Screenshot
│── 📜 financial.ipynb         # **Jupyter Notebook Containing All Code**
│── 📜 README.md               # README (English)
│── 📜 README_cn.md            # README (Chinese)
```

---

## ⚙️ **3. Environment Setup**
### 🔹 **3.1 Create Conda Virtual Environment**
This project runs on **Python 3.12.7**, and it is recommended to use Conda for environment setup:
```bash
conda create -n financial python=3.12.7
conda activate financial
```
### 🔹 **3.2 Install Dependencies**
```bash
pip install -r requirements.txt
```
Or manually install:
```bash
pip install numpy pandas matplotlib statsmodels cvxopt yfinance
```

---

## 🚀 **4. Running the Project**
All code is stored in `financial.ipynb`, which includes **data retrieval, CAPM calculation, portfolio optimization, and visualization**.
Follow the steps below to run the project:

### 🔹 **4.1 Start Jupyter Notebook**
```bash
jupyter lab
```
Or:
```bash
jupyter notebook
```
Then open `financial.ipynb` and execute the cells sequentially.

### Code Execution Screenshot
![all_code.png](all_code.png)

---

### 🔹 **4.2 Main Code Workflow**
1️⃣ **Data Retrieval**
   - Fetch **historical adjusted closing prices** from Yahoo Finance
   - Compute **daily returns**
   - Save results to `adj_close_data.csv` and `returns_data.csv`

2️⃣ **CAPM Computation**
   - Compute **β values (Beta), expected returns, and idiosyncratic risk**
   - Store results in `capm_results.csv`

3️⃣ **Optimal Portfolio Computation**
   - Use **Quadratic Programming (QP)** to compute optimal weights
   - Target returns: **0.08, 0.12, 0.15**
   - Save results in `optimal_portfolio_weights.csv`

4️⃣ **Plot Efficient Frontier**
   - Compute **portfolio risk**
   - Generate **Efficient Frontier chart (`efficient_frontier.png`)**

---

## ❗ **5. Issues and Solutions**
During the computation process, several key issues were encountered. Below are their descriptions and solutions:

### 🔹 **5.1 Singular KKT Matrix in `cvxopt.solvers.qp()`**
(Complete issue description and solution remain unchanged)

---

## 🎯 **6. Future Optimization Directions**
✅ **Expand asset classes (e.g., bonds, ETFs) for better portfolio optimization**  
✅ **Incorporate market volatility modeling using GARCH or Fama-French factor models**  
✅ **Optimize portfolio weights using dynamic asset allocation (DFA) strategies**  

---

## 📬 **7. Contact & Contribution**
🔹 **Email:** [generalfly666@outlook.com](mailto:generalfly666@outlook.com)  
🔹 **GitHub:** [GitHub Repository](https://github.com/loks666)  
🔹 **Contribution:** Fork this repository and submit a Pull Request.  

---

🚀 **This project optimizes CAPM calculations and portfolio optimization methods. Contributions and discussions are welcome!** 😊

