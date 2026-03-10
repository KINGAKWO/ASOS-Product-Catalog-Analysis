# 📦 ASOS Product Catalog Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20%2B-orange)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-green)

> 📊 E-commerce data analysis project featuring 17,848 ASOS products with inventory management insights, brand performance metrics, and pricing strategies using Python and interactive dashboarding.

---

## 🎯 Overview

This project performs comprehensive data analysis on the ASOS fashion retail product catalog. It includes data cleaning, exploratory data analysis (EDA), statistical testing, and an interactive dashboard for visualizing key business insights.

### Key Highlights

| Metric | Value |
|--------|-------|
| **Total Products Analyzed** | 17,848 products |
| **Original Dataset Size** | 30,845 products |
| **Unique Brands** | 1,957 brands |
| **Stock Availability** | 46% In Stock / 54% Out of Stock |
| **Price Range** | £4.50 - £550.00 |
| **Statistical Significance** | Brand-Stock Correlation (p < 0.05) |

---

## 📁 Project Structure

```
ASOS Product Catalog Analysis/
├── README.md                 # This documentation file
├── asos.ipynb               # Data cleaning & analysis notebook
├── asos_dashboard.py        # Streamlit interactive dashboard
├── requirements.txt         # Python dependencies
├── summary report.md        # Analysis summary report
├── data_dictionary.md       # Column documentation
├── products_asos.csv        # Original dataset (56 MB)
├── products_asos_cleaned.csv # Cleaned dataset (33 MB)
├── products_asos_in_stock.csv # In-stock only (15 MB)
```

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|-------|
| **Programming** | Python 3.8+ |
| **Data Analysis** | pandas, NumPy, SciPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Dashboard** | Streamlit |
| **Statistics** | Chi-Square Test (scipy.stats) |

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step 1: Clone or Download

```powershell
# Clone the repository or download the files
cd "ASOS Product Catalog Analysis"
```

### Step 2: Install Dependencies

```powershell
# Install all required packages
pip install -r requirements.txt

# Or install individually
python -m pip install pandas numpy streamlit plotly matplotlib seaborn scipy scikit-learn
```

### Step 3: Verify Installation

```powershell
# Check packages are installed
pip list

# Verify key packages
python -c "import pandas; import streamlit; import plotly; print('All packages OK!')"
```

---

## 📊 How to Run

### Option 1: Interactive Dashboard (Recommended)

```powershell
# Navigate to project folder
cd "ASOS Product Catalog Analysis"

# Run Streamlit dashboard
streamlit run asos_dashboard.py

# Or using Python module
python -m streamlit run asos_dashboard.py

# Open in browser: http://localhost:8501
```

### Option 2: Jupyter Notebook

```powershell
# Start Jupyter
jupyter notebook

# Open: asos.ipynb
# Run all cells to reproduce analysis
```

### Option 3: Command Line Data Analysis

```powershell
# Direct Python execution
python asos_analysis.py

# Or load in Jupyter/Kernels
```

---

## 🔍 What This Dashboard Shows

### Key Features

| Feature | Description |
|---------|-------------|
| **KPI Cards** | Total products, stock status, average price |
| **Stock Distribution** | Pie chart of In Stock vs Out of Stock |
| **Brand Analysis** | Top 10 brands by product count |
| **Price Analysis** | Distribution and comparison by stock status |
| **Out-of-Stock Analysis** | Brands with highest OOS rates |
| **Interactive Filters** | Filter by brand, stock status, price range |

### Interactive Controls

- **Brand Selector**: Choose specific brands to analyze
- **Stock Filter**: View only In Stock or Out of Stock items
- **Price Range Slider**: Adjust min/max price boundaries
- **Data Table**: Preview individual product details

---

## 📈 Key Findings

### Data Quality Summary

| Cleaning Step | Action | Result |
|---------------|--------|--------|
| **Price Validation** | Removed invalid values | 12,467 rows dropped (40.4%) |
| **Duplicate Removal** | Based on name, price, size | 806 duplicates removed |
| **Brand Extraction** | Standardized from names | 1,957 unique brands identified |
| **Missing Values** | Filled or dropped | Cleaned dataset ready |

### Business Insights

| Finding | Implication |
|---------|-------------|
| **54% Out-of-Stock Rate** | High demand, supply constraints |
| **ASOS Dominates Catalog** | 27% of products are house brand |
| **Price-Correlation with Stock** | Premium items tend to sell faster |
| **Statistically Significant** | Brand-stock relationship (p < 0.05) |

### Top 10 Brands by Product Count

| Rank | Brand | Count |
|------|-------|-------|
| 1 | ASOS | 4,842 |
| 2 | Topshop | 1,136 |
| 3 | River island | 474 |
| 4 | New look | 469 |
| 5 | Miss selfridge | 427 |

---

## 📋 Data Dictionary

For detailed column information, see **[data_dictionary.md](data_dictionary.md)**.

| Column | Type | Description |
|--------|------|-------------|
| `name` | string | Product name/title |
| `price` | float | Price in GBP (£) |
| `size` | string | Available sizes (UK format) |
| `brand` | string | Extracted brand name |
| `stock` | string | 'In stock' or 'Out of stock' |
| `description` | string | Product description |

---

## 📂 Output Files

| File | Purpose | Record Count |
|------|---------|--------------|
| `products_asos_cleaned.csv` | Full cleaned dataset | 17,848 |
| `products_asos_in_stock.csv` | In-stock products only | 8,210 |
| `summary report.md` | Analysis findings | N/A |
| `data_dictionary.md` | Column documentation | N/A |

---

## 🧪 Testing

```powershell
# Test data loading
python -c "import pandas as pd; df = pd.read_csv('products_asos_cleaned.csv'); print(f'Loaded {len(df)} rows')"

# Test dashboard
streamlit run asos_dashboard.py --server.headless true

# Verify all files exist
dir *.csv
dir *.md
dir *.py
```

---

## 📝 Usage Examples

### Load Cleaned Data

```python
import pandas as pd
df = pd.read_csv('products_asos_cleaned.csv')
print(df.head())
print(df.describe())
```

### Analyze Stock Status

```python
stock_counts = df['stock'].value_counts()
print(stock_counts)
```

### Filter by Brand

```python
nike_products = df[df['brand'] == 'Nike']
print(f"Nike products: {len(nike_products)}")
```

---

## 📊 Screenshots

<img width="1919" height="907" alt="image" src="https://github.com/user-attachments/assets/d6e61073-494d-44a1-b249-95bf71ae76fa" />


<img width="1919" height="904" alt="image" src="https://github.com/user-attachments/assets/ea23eb6d-950e-41bf-94b0-12c461fdbb67" />


**Dashboard Home View:**
- KPI cards showing key metrics
- Stock distribution pie chart
- Top brands bar chart

**Analysis Views:**
- Price distribution histogram
- Price vs Stock box plots
- Out-of-Stock brand rankings

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is for educational/portfolio purposes based on https://www.youtube.com/watch?v=ux9uxKM171E by "Lore So What"

---

## 📬 Contact

| Resource | Link |
|----------|------|
| **Project** | [ASOS Product Catalog Analysis](./) |
| **Data Source** | https://drive.google.com/drive/folders/1W569j3au1iYVtWm5WeWer2gBGU2Xwzui |
| **Documentation** | [summary report.md](summary report.md) |
| **Data Dictionary** | [data_dictionary.md](data_dictionary.md) |

---

## 🎓 Learning Resources

| Topic | Resource |
|-------|----------|
| **Python for Data Science** | [IBM Python for Data Science Course](https://www.coursera.org) |
| **Streamlit Dashboards** | [Streamlit Official Docs](https://docs.streamlit.io) |
| **Pandas Analysis** | [Pandas Documentation](https://pandas.pydata.org/docs) |
| **Data Visualization** | [Matplotlib & Seaborn Tutorials](https://matplotlib.org) |

---

## 🏆 Achievements

- ✅ **IBM Data Analytics Foundations**
- ✅ **IBM Excel for Data Analysis**
- ✅ **IBM Data Visualization**
- ✅ **IBM Python for Data Science**
- ✅ **IBM Data Analysis with Python**
- ✅ **IBM Python Project for Data Science**
- ✅ **IBM Databases & SQL for Data Science**

---

## 📅 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | February 2026 | Initial release with cleaning, analysis, and dashboard |

---

<div align="center">

**Built with ❤️ for the IBM Data Analytics Learning Journey (https://github.com/KINGAKWO/ibm-data-analytics-journey)**

📊 [Explore the Dashboard](./asos_dashboard.py) | 📈 [View Summary Report](./summary report.md) | 📚 [Data Dictionary](./data_dictionary.md)

</div>
