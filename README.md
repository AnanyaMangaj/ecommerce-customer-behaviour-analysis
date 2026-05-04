<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=200&section=header&text=🛒%20Customer%20Behaviour%20Analysis&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=E-Commerce%20Intelligence%20Platform&descAlignY=58&descAlign=50" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Models-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

<br/>

> **Segment customers. Discover patterns. Drive revenue.** 
> An end-to-end unsupervised ML pipeline with clustering, association rule mining, and an interactive Streamlit dashboard.

<br/>

[🚀 Quick Start](#-quick-start) • [📊 Features](#-features) • [🤖 Models](#-machine-learning-models) • [📷 Dashboard](#-streamlit-dashboard) • [📁 Structure](#-project-structure) • [🔮 Future Work](#-future-enhancements)

</div>

---

## 🧭 Project Overview

E-commerce platforms generate massive amounts of behavioural data — but raw data alone doesn't drive decisions. This project transforms customer transaction records into **actionable intelligence** using:

- 🔍 **4 Clustering Algorithms** to identify distinct customer personas
- 🛒 **3 Association Rule Algorithms** to power product recommendations  
- 📊 **Interactive Streamlit Dashboard** for real-time business insights

Whether you're a data scientist, analyst, or business strategist — this project gives you the tools to understand *who* your customers are and *what* they buy together.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧹 **Smart Preprocessing** | Handles missing values, duplicates, format errors & text inconsistencies |
| 🔬 **EDA** | Product trends, spend distributions, engagement patterns |
| ⚙️ **Feature Engineering** | Customer-level aggregations: AvgSpend, TotalItems, AvgSession, AvgRating |
| 🤖 **Multi-Model Clustering** | K-Means, Hierarchical, DBSCAN, GMM with Silhouette Score evaluation |
| 🧺 **Recommendation Engine** | Apriori, ECLAT, FP-Growth association rules with Support/Confidence/Lift |
| 📊 **Live Dashboard** | Streamlit app with filters, KPI cards, charts, and downloadable results |

---

## 🗂️ Dataset

The dataset (`data/ecommerce_data.csv`) contains customer transaction and behavioural records:

```
CustomerID · TransactionID · Product · Category · Price · Quantity
PaymentType · City · Device · SessionDuration · DiscountApplied
ShippingType · Rating · ReviewText · TransactionDate
```

> 📌 All preprocessing steps are documented in `notebooks/ecommerce_analysis.ipynb`

---

## 🤖 Machine Learning Models

### 🔷 Customer Segmentation — Clustering

<table>
<tr>
<td width="50%">

**K-Means Clustering**  
Groups customers into *k* fixed segments based on behavioural similarity. Fast and interpretable.

**Hierarchical Clustering**  
Builds a tree of customer groups. Useful for exploring nested relationships.

</td>
<td width="50%">

**DBSCAN**  
Identifies dense customer clusters and flags outliers/noise automatically.

**Gaussian Mixture Model (GMM)**  
Probabilistic soft-clustering for flexible, overlapping group assignment.

</td>
</tr>
</table>

> 📏 **Evaluation:** All models are compared using the **Silhouette Score**

---

### 🛒 Product Recommendations — Association Rules

| Algorithm | Approach | Key Strength |
|---|---|---|
| **Apriori** | Breadth-first frequent itemset mining | Simple, interpretable rules |
| **ECLAT** | Vertical data format (tidset intersections) | Fast for dense datasets |
| **FP-Growth** | Compressed FP-tree structure | No candidate generation overhead |

**Sample Rules Discovered:**

```
📱 Mobile     →  🎧 Earphones     (Lift: high)
💻 Laptop     →  🖱️  Mouse         (Confidence: strong)
👗 Dress      →  👠 Heels          (Support: frequent)
👟 Shoes      →  🧦 Socks          (Lift: strong)
```

> 📏 **Metrics:** Support · Confidence · Lift

---

## 📊 Streamlit Dashboard

The interactive dashboard (`app/streamlit_app.py`) gives you:

- 🔍 **Sidebar Filters** — Select customer cluster dynamically
- 📌 **KPI Cards** — Total Customers, Avg Spend, Total Items, Avg Rating
- 📄 **Data Table** — Filterable customer-level segment view
- 📈 **Histograms & Boxplots** — Spend distributions and item quantities
- 📊 **Cluster Comparison Chart** — Avg spend across all clusters
- ⬇️ **CSV Download** — Export filtered data instantly
- 🛍️ **Recommendation Panel** — Display product association rules

---

## 🗺️ Project Workflow

```
Raw Data  ──►  Preprocessing  ──►  EDA  ──►  Feature Engineering
                                                      │
                    ┌─────────────────────────────────┘
                    ▼
            Customer Segmentation         Product Recommendations
          ┌─────────────────────┐       ┌──────────────────────────┐
          │  K-Means            │       │  Apriori                 │
          │  Hierarchical       │       │  ECLAT                   │
          │  DBSCAN             │       │  FP-Growth               │
          │  GMM                │       └──────────────────────────┘
          └─────────────────────┘                  │
                    │                              │
                    └──────────────┬───────────────┘
                                   ▼
                        Streamlit Dashboard
```

---

## 📁 Project Structure

```bash
ecommerce-customer-behaviour-analysis/
│
├── 📂 data/
│   └── ecommerce_data.csv              # Raw dataset
│
├── 📂 notebooks/
│   └── ecommerce_analysis.ipynb        # Full analysis pipeline
│
├── 📂 models/
│   ├── kmeans_model.pkl
│   ├── hierarchical_model.pkl
│   ├── dbscan_model.pkl
│   └── gmm_model.pkl
│
├── 📂 association_rules/
│   ├── apriori_rules.csv
│   ├── fp_growth_rules.csv
│   └── eclat_rules.csv
│
├── 📂 results/
│   ├── customer_segments.csv           # Segmentation output
│   └── cluster_visualization.png       # Cluster scatter plot
│
├── 📂 app/
│   └── streamlit_app.py                # Interactive dashboard
│
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ecommerce-customer-behaviour-analysis.git
cd ecommerce-customer-behaviour-analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

<details>
<summary>Or install manually</summary>

```bash
pip install pandas numpy matplotlib seaborn scikit-learn mlxtend streamlit
```

</details>

### 3. Run the Notebook

Open Jupyter Lab and execute:

```
notebooks/ecommerce_analysis.ipynb
```

This will clean data → perform EDA → engineer features → train models → generate association rules → save outputs.

### 4. Launch the Dashboard

```bash
streamlit run app/streamlit_app.py
```

Then open → **http://localhost:8501**

---

## 💡 Business Questions This Solves

| Question | Solution |
|---|---|
| Who are our highest-value customers? | K-Means / GMM cluster profiles |
| Which customers are disengaged? | DBSCAN outlier detection |
| What products are bought together? | Apriori / FP-Growth rules |
| What should we cross-sell? | Confidence-based recommendations |
| Which segment to target with offers? | Silhouette-optimised clusters |

---

## 🔮 Future Enhancements

- [ ] 🔄 Real-time recommendation engine
- [ ] 📈 Customer Lifetime Value (CLV) prediction
- [ ] 🎯 Personalised marketing campaign integration
- [ ] 🧠 Deep learning recommendation system (NCF / Transformers)
- [ ] ☁️ Streamlit Cloud deployment
- [ ] 📊 Power BI / Tableau integration

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat-square)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Mlxtend](https://img.shields.io/badge/Mlxtend-Association%20Rules-blue?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

</div>

---

## 👩‍💻 Author

<div align="center">

**Ananya Mangaj**  
*AI / Data Science*

[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/AnanyaMangaj)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/ananya-mangaj)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=100&section=footer" width="100%"/>

*⭐ Star this repo if you found it useful!*

</div>
