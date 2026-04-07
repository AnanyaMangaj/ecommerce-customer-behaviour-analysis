# 🛒 Ecommerce Customer Behaviour Analysis & Recommendation System

## 📌 Project Overview

This project focuses on analyzing **customer purchasing behaviour** in an e-commerce platform using **Unsupervised Machine Learning** and **Association Rule Mining**.

The system helps in:

- Segmenting customers into meaningful groups
- Understanding customer behaviour patterns
- Discovering product associations for recommendations
- Visualizing insights through an interactive **Streamlit dashboard**

This project is useful for businesses to improve:

- Customer targeting
- Personalized recommendations
- Cross-selling strategies
- Business decision-making

---

# 🎯 Objectives

The main objectives of this project are:

1. **Analyze customer behaviour** using transaction and browsing data
2. **Segment customers** using clustering algorithms
3. **Find product recommendation patterns** using association rules
4. **Build an interactive dashboard** for easy analysis and presentation

---

# 🧠 Problem Statement

In e-commerce platforms, customers have different purchasing habits, preferences, and engagement levels.

Traditional methods fail to identify:

- High-value customers
- Low-engagement users
- Product combinations frequently bought together

This project solves that problem by using:

- **Customer segmentation**
- **Pattern discovery**
- **Recommendation rule generation**

---

# 🗂️ Project Workflow

The project follows this pipeline:

1. Data Collection
2. Data Preparation
3. Data Wrangling
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Customer Segmentation (Clustering)
7. Product Recommendation (Association Rules)
8. Streamlit Dashboard Deployment

---

# 📁 Project Structure

```bash
ecommerce-customer-behaviour-analysis/
│
├── data/
│   └── ecommerce_data.csv
│
├── notebooks/
│   └── ecommerce_analysis.ipynb
│
├── models/
│   ├── kmeans_model.pkl
│   ├── hierarchical_model.pkl
│   ├── dbscan_model.pkl
│   └── gmm_model.pkl
│
├── association_rules/
│   ├── apriori_rules.csv
│   ├── fp_growth_rules.csv
│   └── eclat_rules.csv
│
├── results/
│   ├── customer_segments.csv
│   ├── cluster_visualization.png
│   └── recommendation_examples.txt
│
├── app/
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md
```

---

# 📊 Dataset Description

The dataset contains customer transaction and behavioural information such as:

- `CustomerID`
- `TransactionID`
- `Product`
- `Category`
- `Price`
- `Quantity`
- `PaymentType`
- `City`
- `Device`
- `SessionDuration`
- `DiscountApplied`
- `ShippingType`
- `Rating`
- `ReviewText`
- `TransactionDate`

---

# ⚠️ Data Challenges Handled

During preprocessing, the following issues were addressed:

- Missing Values
- Duplicate Rows
- Wrong Data Formats
- Inconsistent Data Entries

---

# 🧹 Data Preprocessing

## 1. Handling Missing Values
Missing values were filled using:

- Mean (for numerical columns)
- Mode / default values (for categorical columns)

## 2. Removing Duplicate Rows
Duplicate customer transaction records were removed.

## 3. Correcting Data Types
Columns such as dates and numerical values were converted into proper formats.

## 4. Standardizing Text Data
Text fields like product names and categories were cleaned for consistency.

---

# 📈 Exploratory Data Analysis (EDA)

EDA was performed to understand customer and product behaviour through:

- Top-selling products
- Purchase distribution
- Customer engagement analysis
- Average spending behaviour
- Product frequency analysis

### Sample visualizations:
- Product count plots
- Spend distribution histograms
- Cluster scatter plots
- Cluster-wise comparison charts

---

# 🛠️ Feature Engineering

Customer-level features were created by aggregating transaction data.

### Important engineered features:

- **AvgSpend** → Average money spent by customer
- **TotalItems** → Total quantity purchased
- **AvgSession** → Average session duration
- **AvgRating** → Average product rating given

These features were used for clustering.

---

# 🤖 Machine Learning Models Used

## 1. Customer Segmentation (Clustering)

The following **Unsupervised Learning algorithms** were applied:

### 🔹 K-Means Clustering
Used to segment customers into fixed groups based on behavioural similarity.

### 🔹 Hierarchical Clustering
Used to create customer group hierarchies.

### 🔹 DBSCAN
Used to identify dense customer groups and noise points.

### 🔹 Gaussian Mixture Model (GMM)
Used for probabilistic clustering and flexible group assignment.

---

# 📌 Why Multiple Clustering Algorithms?

Different clustering algorithms were used to compare results and determine the best customer segmentation approach.

### Evaluation Metric Used:
- **Silhouette Score**

This helps in measuring how well-separated the customer clusters are.

---

# 🧺 Product Recommendation System

To recommend products, **Association Rule Mining** was used.

This helps discover products that are frequently bought together.

### Example rules:
- Mobile → Earphones
- Laptop → Mouse
- Dress → Heels
- Shoes → Socks

---

# 🔗 Association Rule Algorithms Used

## 1. Apriori
Finds frequent itemsets and generates product association rules.

## 2. ECLAT
Uses a vertical dataset format to discover frequent product combinations.

## 3. FP-Growth
Efficiently mines frequent patterns without generating too many candidate itemsets.

---

# 📏 Rule Evaluation Metrics

Association rules were evaluated using:

- **Support** → Frequency of occurrence
- **Confidence** → Likelihood of buying consequent product
- **Lift** → Strength of the association

---

# 📊 Output Files Generated

## `results/customer_segments.csv`
Contains customer segmentation results.

## `results/cluster_visualization.png`
Contains cluster graph visualization.

## `results/recommendation_examples.txt`
Contains sample product recommendation rules.

## `association_rules/*.csv`
Contains generated association rule outputs for each algorithm.

---

# 🌐 Streamlit Dashboard

An interactive **Streamlit dashboard** was built to visualize:

- Customer clusters
- KPI metrics
- Behaviour insights
- Cluster comparisons
- Product recommendation rules

---

# ▶️ How to Run the Project

## Step 1: Clone or Download the Project

```bash
git clone <your-repository-link>
cd ecommerce-customer-behaviour-analysis
```

If you are not using GitHub, simply open the folder in **Jupyter Lab** or **VS Code**.

---

## Step 2: Install Required Libraries

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn mlxtend streamlit
```

---

## Step 3: Run Jupyter Notebook

Open Jupyter Lab and run:

```bash
notebooks/ecommerce_analysis.ipynb
```

This notebook will:

- Clean the dataset
- Perform EDA
- Create customer features
- Train clustering models
- Generate association rules
- Save output files

---

## Step 4: Run the Streamlit App

```bash
streamlit run app/streamlit_app.py
```

After running, open the local URL shown in terminal:

```bash
http://localhost:8501
```

---

# 💻 Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-Learn**
- **Mlxtend**
- **Streamlit**
- **Jupyter Lab**

---

# 📷 Dashboard Features

The Streamlit dashboard includes:

- Sidebar filters
- Cluster selection
- KPI cards
- Customer data table
- Histograms and boxplots
- Cluster comparison charts
- Download filtered data option
- Product recommendation display

---

# 📌 Sample Business Insights

This project can help an e-commerce business answer questions like:

- Who are the highest spending customers?
- Which customers are less engaged?
- Which products are frequently bought together?
- What products should be recommended together?
- Which customer segment should be targeted with offers?

---

# 🚀 Future Enhancements

This project can be improved further by adding:

- Real-time recommendation engine
- Customer Lifetime Value (CLV) prediction
- Personalized marketing campaigns
- Deep learning recommendation system
- Streamlit Cloud deployment
- Power BI integration

---

# 📚 Learning Outcomes

By completing this project, the following concepts are demonstrated:

- Data preprocessing
- Feature engineering
- Unsupervised learning
- Clustering algorithms
- Association rule mining
- Data visualization
- Dashboard deployment

---

# 👨‍💻 Author

**Ananya Mangaj**  
AI / Data Science Project



---
