# ASOS Product Catalog Analysis - Summary Report

**Report Date:** January 2026  
**Analysis Notebook:** asos.ipynb  
**Data Source:** products_asos.csv  
**Version:** 1.0

---

## Executive Summary

This report presents findings from a comprehensive analysis of **17,848 ASOS products** after data cleaning and transformation. The analysis reveals significant patterns in stock availability, brand performance, and pricing strategies.

| Key Metric | Finding |
|------------|---------|
| **Total Products Analyzed** | 17,848 products (after cleaning) |
| **Original Dataset Size** | 30,845 products |
| **Data Quality Dropped** | 12,467 rows with invalid prices (40.4%) |
| **Unique Brands** | 1,957 brands identified |
| **Stock Availability** | 46% In Stock / 54% Out of Stock |
| **Price Range** | £4.50 - £550.00 |
| **Brand-Stock Correlation** | Statistically significant (p < 0.05) |

---

## 1. Data Quality Overview

### 1.1 Cleaning Summary

| Cleaning Step | Action | Result |
|---------------|--------|--------|
| **Price Validation** | Removed invalid/currency values | 12,467 rows dropped (40.4%) |
| **Duplicate Removal** | Based on name, price, size | 806 duplicates removed |
| **Brand Extraction** | Standardized from product names | 1,957 unique brands identified |
| **Stock Classification** | Pattern matching on size column | Binary: In Stock / Out of Stock |
| **Missing Values** | Handled automatically | No remaining nulls in critical columns |

### 1.2 Data Completeness

| Column | Null Count Before | Action | Null Count After |
|--------|-------------------|--------|------------------|
| price | 18 (object dtype) | Converted to numeric | 0 |
| brand | Derived from name | Extraction function | 0 |
| stock | Derived from size | Pattern matching | 0 |
| name | 18 | Cleaned and filled | 0 |
| description | 18 | Cleaned and filled | 0 |

### 1.3 Dataset Statistics

| Metric | Value |
|--------|-------|
| Initial rows | 30,845 |
| Invalid price rows | 12,467 |
| Duplicates | 806 |
| **Final clean rows** | **17,848** |
| **Data retention rate** | **57.8%** |

---

## 2. Brand Analysis Findings

### 2.1 Top 10 Brands by Product Count

| Rank | Brand | Product Count | Market Share |
|------|-------|---------------|--------------|
| 1 | ASOS | 4,842 | 27.1% |
| 2 | Topshop | 1,136 | 6.4% |
| 3 | River island | 474 | 2.7% |
| 4 | New look | 469 | 2.6% |
| 5 | Miss selfridge | 427 | 2.4% |
| 6 | adidas | 395 | 2.2% |
| 7 | Collusion | 383 | 2.1% |
| 8 | Stradivarius | 345 | 1.9% |
| 9 | Bershka | 344 | 1.9% |
| 10 | Vero moda | 327 | 1.8% |

### 2.2 Brand Category Analysis

| Category | Brands | Total Products | Percentage |
|----------|--------|----------------|------------|
| **ASOS House Brands** | ASOS, Collusion | 5,225 | 29.3% |
| **Fast Fashion** | Topshop, River island, New look, Miss selfridge | 2,406 | 13.5% |
| **Sportswear** | adidas | 395 | 2.2% |
| **International Brands** | Stradivarius, Bershka, Vero moda | 1,016 | 5.7% |

### 2.3 Key Brand Insights

| Finding | Business Implication |
|---------|----------------------|
| **ASOS dominates** (27.1%) | Strong private label strategy |
| **High brand diversity** (1,957 unique) | Wide product catalog coverage |
| **Top 5 brands = 40.7%** | Concentrated brand portfolio |
| **Unknown brands** | ~3,960 products (22.2%) need brand mapping |

---

## 3. Stock Status Analysis

### 3.1 Overall Stock Distribution

| Status | Count | Percentage |
|--------|-------|------------|
| **In Stock** | 8,210 | 46.0% |
| **Out of Stock** | 9,638 | 54.0% |

### 3.2 Top 10 Brands by Out-of-Stock Products

| Rank | Brand | OOS Count | OOS Percentage |
|------|-------|-----------|----------------|
| 1 | ASOS | 2,641 | 54.5% |
| 2 | Topshop | 577 | 50.8% |
| 3 | New look | 334 | 71.2% |
| 4 | River island | 261 | 55.1% |
| 5 | Miss selfridge | 215 | 50.4% |
| 6 | adidas | 212 | 53.7% |
| 7 | Stradivarius | 212 | 61.4% |
| 8 | Vero moda | 209 | 63.9% |
| 9 | Bershka | 203 | 59.0% |
| 10 | Collusion | 176 | 46.0% |

### 3.3 Stock Insights

| Observation | Interpretation |
|-------------|----------------|
| **54% overall OOS rate** | High demand, supply constraints |
| **ASOS has most OOS products** | 2,641 items, but 54.5% OOS |
| **New look highest OOS%** | 71.2% indicates supply issues |
| **Collusion lowest OOS%** | 46.0% shows better inventory management |

---

## 4. Pricing Analysis

### 4.1 Price Statistics

| Metric | Value |
|--------|-------|
| **Price Range (Raw)** | £4.50 - £550.00 |
| **Minimum Cleaned Price** | ~£5.00 (estimated) |
| **Maximum Cleaned Price** | ~£550.00 (estimated) |
| **Average Price (In Stock)** | Calculated from data |
| **Average Price (OOS)** | Calculated from data |

### 4.2 Top 10 Most Expensive Products by Brand

| Rank | Product/Brand | Average Price |
|------|---------------|---------------|
| 1 | Napapijri skidoo | £420.00 |
| 2 | Allsaints benyon | £359.00 |
| 3 | Roxy peak | £350.00 |
| 4 | Allsaints caden | £329.00 |
| 5 | Allsaints elora | £319.00 |
| 6 | Allsaints balfern | £319.00 |
| 7 | Hugo polyester | £319.00 |
| 8 | Napapijri x | £316.67 |
| 9 | Fiorucci balconette | £275.00 |
| 10 | Napapijri a-harness | £265.00 |


---

## 5. Statistical Analysis Results

### 5.1 Chi-Square Test: Brand vs Stock Status

| Statistic | Value | Interpretation |
|-----------|-------|----------------|
| **Chi-Square** | 116.93 | Strong association |
| **P-Value** | 0.0000 | **Highly significant** |
| **Degrees of Freedom** | 9 | 10 brands × 2 stock types |
| **Statistically Significant** | **Yes** | p < 0.05 |

### 5.2 Test Interpretation

| Finding | Conclusion |
|---------|------------|
| **P-value = 0.0000** | There is a statistically significant relationship between brand and stock status |
| **Chi-square = 116.93** | Strong association between specific brands and stock availability patterns |
| **Business Impact** | Certain brands consistently have higher/lower stock availability |

---

## 6. Brand Performance Matrix

### 6.1 High Demand Brands (Top OOS Rate)

| Brand | OOS Rate | Priority |
|-------|----------|----------|
| **New look** | 71.2% | High - Investigate supply chain |
| **Vero moda** | 63.9% | Medium - Monitor stock levels |
| **Stradivarius** | 61.4% | Medium - Potential demand spike |
| **Bershka** | 59.0% | Medium - Review inventory |
| **River island** | 55.1% | Low - Within normal range |

### 6.2 Best Stock Management Brands

| Brand | In-Stock Rate | Performance |
|-------|---------------|-------------|
| **Collusion** | 54.0% | Excellent |
| **Miss selfridge** | 49.6% | Good |
| **Topshop** | 49.2% | Good |
| **Adidas** | 46.3% | Average |

---

## 7. Business Recommendations

### 7.1 Priority Actions

| Priority | Recommendation | Expected Impact |
|----------|----------------|-----------------|
| **HIGH** | Increase stock for New look, Vero moda (OOS > 63%) | Reduce customer dissatisfaction |
| **HIGH** | Investigate supply chain for top 5 OOS brands | Better availability |
| **MEDIUM** | Implement restock alerts for brands with OOS > 50% | Proactive inventory management |
| **MEDIUM** | Review pricing on out-of-stock premium items | Clear remaining inventory |
| **LOW** | Expand known brand list (22% products are "Unknown") | Better categorization |

### 7.2 Strategic Insights

| Insight | Recommendation |
|---------|----------------|
| **54% OOS rate is high** | Consider demand forecasting improvements |
| **ASOS dominates catalog** | Leverage for exclusive promotions |
| **Statistically significant brand-stock correlation** | Develop brand-specific inventory strategies |
| **Price outliers removed** | Review pricing strategy for premium products |

---

## 8. Data Files Generated

| File Name | Purpose | Record Count |
|-----------|---------|--------------|
| `products_asos_cleaned.csv` | Full cleaned dataset | 17,848 |
| `products_asos_in_stock.csv` | In-stock products only | 8,210 |
| `ASOS_Product_Dataset_Data_Dictionary.md` | Column documentation | N/A |
| `ASOS_Product_Analysis_Summary_Report.md` | This report | N/A |

---


## Contact Information

| Role | Contact |
|------|---------|
| **Data Analyst** | kingakwomakembe@gmail.com |


---

**Document Version:** 1.0  
**Document Status:** Final  
**Last Updated:** January 2026  
**Approved By:** Data Analytics Team

---

## Appendix A: Quick Python Reference

```python
# Extract key statistics from notebook output
print(f"Total products: {len(df)}")
print(f"Unique brands: {len(brand_counts)}")
print(f"In stock: {stock_counts.get('In stock', 0)}")
print(f"Out of stock: {stock_counts.get('Out of stock', 0)}")
print(f"Chi-square: {chi2:.2f}, p-value: {p:.4f}")
```

---

**END OF REPORT**