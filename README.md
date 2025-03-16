# 📌 **基于 CAPM 和均值-方差优化（MVO）的投资组合优化 [英文](README_en.md)**
--- 

## 📖 **1. 项目简介**
本项目采用 **资本资产定价模型（CAPM）** 和 **均值-方差优化（Mean-Variance Optimization, MVO）**，通过 **二次规划（Quadratic Programming, QP）** 计算最优投资组合。  
项目目标：
- **计算 CAPM 参数（β 值、预期收益、个体风险）**
- **优化投资组合权重，最小化风险**
- **绘制有效前沿（Efficient Frontier）**，分析 **风险-收益权衡**

---

## 🏗 **2. 项目结构**
```
📂 FinancialMachineLearning
│── 📂 doc                     # 项目文档
│   │── 📜 CF969.pdf           # 报告文档示例
│   │── 📜 CF969 - SP ZU - Assignment.pdf # 要求文档
│── 📂 report                  # 研究报告
│   │── 📜 report_cn.md        # 中文报告
│   │── 📜 report_en.md        # 英文报告
│── 📂 result                  # 计算结果
│   │── 📜 adj_close_data.csv  # 股票收盘价数据
│   │── 📜 capm_results.csv    # CAPM 计算结果
│   │── 📜 efficient_frontier.png # 有效前沿图
│   │── 📜 optimal_portfolio_weights.csv # 最优投资组合权重
│   │── 📜 returns_data.csv    # 每日收益率数据
│── 📜 .gitignore              # Git 忽略文件
│── 📜 all_code.png            # 代码截图
│── 📜 financial.ipynb         # **Jupyter Notebook 文件，包含所有代码**
│── 📜 README.md               # 自述文件（中文）
│── 📜 README_en.md            # 自述文件（英文）
```

---

## ⚙️ **3. 环境配置**
### 🔹 **3.1 创建 Conda 虚拟环境**
本项目基于 **Python 3.12.7** 运行，建议使用 Conda 创建环境：
```bash
conda create -n financial python=3.12.7
conda activate financial
```
### 🔹 **3.2 安装依赖**
```bash
pip install -r requirements.txt
```
或手动安装：
```bash
pip install numpy pandas matplotlib statsmodels cvxopt yfinance
```

---

## 🚀 **4. 运行项目**
本项目所有代码都存放在 `financial.ipynb` Jupyter Notebook 文件中，包含 **数据下载、CAPM 计算、投资组合优化、可视化** 等完整流程。  
请按照以下步骤运行：

### 🔹 **4.1 启动 Jupyter Notebook**
```bash
jupyter lab
```
或：
```bash
jupyter notebook
```
然后打开 `financial.ipynb`，逐步运行代码。

### 代码运行截图
![all_code.png](all_code.png)

---

### 🔹 **4.2 代码包含的主要流程**
1️⃣ **数据下载**
   - 从 Yahoo Finance 获取 **股票历史收盘价**
   - 计算 **每日收益率**
   - 生成 `adj_close_data.csv` 和 `returns_data.csv`

2️⃣ **CAPM 计算**
   - 计算 **β 值（Beta）、预期收益、个体风险**
   - 存储计算结果到 `capm_results.csv`

3️⃣ **最优投资组合计算**
   - 使用 **二次规划（QP）** 计算最优权重
   - 目标收益率分别为 **0.08, 0.12, 0.15**
   - 生成 `optimal_portfolio_weights.csv`

4️⃣ **绘制有效前沿**
   - 计算 **投资组合风险**
   - 生成 **有效前沿图 `efficient_frontier.png`**

---

## ❗ **5. 遇到的问题及解决方案**
在整个计算过程中，我遇到了几个关键问题，以下是问题描述及解决思路：

### 🔹 **5.1 `cvxopt.solvers.qp()` 遇到奇异 KKT 矩阵**
#### **问题**
在执行 `cvxopt.solvers.qp()` 时，遇到了 `singular KKT matrix` 错误。  
**原因：**
- 协方差矩阵 `Σ` 可能不可逆，导致最优化问题无解。
- 股票收益率数据存在 **多重共线性**，即不同股票的收益率高度相关，导致矩阵行列式趋近于零。

#### **解决方案**
- 采用 **NumPy** 的 `np.outer` 计算协方差矩阵，而不是使用 `for` 循环，提高数值稳定性：
  ```python
  beta_matrix = np.array([beta_values[stock] for stock in stock_list])
  idiosyncratic_var_vector = np.array([idiosyncratic_variance[stock] for stock in stock_list])
  covariance_matrix = np.outer(beta_matrix, beta_matrix) * market_variance
  np.fill_diagonal(covariance_matrix, np.diag(covariance_matrix) + idiosyncratic_var_vector)
  ```
- 若协方差矩阵仍不可逆，**增加一个小的正则化参数**：
  ```python
  covariance_matrix += np.eye(len(stock_list)) * 1e-6  # 加入小的正则项，增强可逆性
  ```

---

### 🔹 **5.2 `A` 约束矩阵维度不匹配**
#### **问题**
在 `cvxopt.solvers.qp()` 计算最优投资组合时，出现 `TypeError: 'A' must be a 'd' matrix with n columns`。

#### **原因**
- `A` 矩阵的形状 **错误**，本应是 **(2 × num_assets)**，但实际可能是 **(num_assets × 2)**。

#### **解决方案**
- 在构造 `A` 矩阵时，**确保其形状为 (2 × num_assets)**：
  ```python
  A = matrix(np.vstack((np.ones(num_assets), [expected_returns[stock] for stock in stock_list])), tc='d').T
  ```
- 确保 `b` 也是 `cvxopt` **double 类型**：
  ```python
  b = matrix([1.0, mu_p], tc='d')
  ```

---

### 🔹 **5.3 负权重问题**
#### **问题**
某些最优投资组合的权重为 **负值**，即出现 **做空仓位**，但此优化目标要求 **不允许做空**。

#### **解决方案**
- 采用 **绝对值** 修正负权重：
  ```python
  weights = np.abs(weights)
  ```
- 重新 **归一化** 权重，使总和为 1：
  ```python
  weights /= np.sum(weights)
  ```

---

### 🔹 **5.4 计算 `portfolio_variance` 出现维度错误**
#### **问题**
在计算投资组合风险时，`weights.T @ covariance_matrix @ weights` 可能报错。

#### **解决方案**
- 采用 `np.dot()` 确保矩阵运算正确：
  ```python
  portfolio_variance = np.dot(weights.T, np.dot(covariance_matrix, weights))
  ```

---

### 🔹 **5.5 `market_variance` 计算问题**
#### **问题**
在计算 `market_variance = np.var(market_returns)` 时，可能出现 **类型转换错误**，导致计算异常。

#### **解决方案**
- 强制转换 `market_returns` 为 `float64`：
  ```python
  market_variance = np.var(market_returns.astype(np.float64))
  ```

---

## 🎯 **6. 未来优化方向**
✅ **扩展资产类别**（如债券、ETF）优化投资组合  
✅ **考虑市场波动性变化**，使用 **GARCH 模型或 Fama-French 因子模型**  
✅ **优化投资组合权重**，结合 **动态资产配置（DFA）** 策略  

---

## 📬 **7. 联系方式 & 贡献**
🔹 **Email:** [generalfly666@outlook.com](mailto:generalfly666@outlook.com)  
🔹 **GitHub:** [GitHub Repository](https://github.com/loks666)  
🔹 **贡献方式:** Fork 本仓库并提交 Pull Request。  

---

🚀 **本项目优化了 CAPM 计算和投资组合优化方法，欢迎交流与改进！** 😊