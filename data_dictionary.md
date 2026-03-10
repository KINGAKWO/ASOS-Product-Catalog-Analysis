# ASOS Product Dataset - Data Dictionary

**Document Version:** 2.0  
**Last Updated:** 2026-01-09  
**Dataset Source:** products_asos.csv  
**Purpose:** ASOS product catalog analysis for stock status, brand performance, and pricing insights

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Source Columns (Raw Data)](#2-source-columns-raw-data)
- [3. Cleaned/Transformed Columns](#3-cleanedtransformed-columns)
- [4. Derived Metrics](#4-derived-metrics)
- [5. Data Cleaning Rules](#5-data-cleaning-rules)
- [6. Quality Checks](#6-quality-checks)
- [7. Output Files](#7-output-files)
- [8. Usage Guidelines](#8-usage-guidelines)
- [9. Version History](#9-version-history)

---

## 1. Overview

| Attribute | Details |
|-----------|---------|
| **Dataset Name** | products_asos.csv |
| **Business Domain** | E-commerce / Fashion Retail |
| **Primary Use Cases** | Stock analysis, Brand performance, Pricing insights |
| **Data Currency** | Current product catalog snapshot |
| **Geographic Focus** | United Kingdom (GBP currency, UK sizes) |

---

## 2. Source Columns (Raw Data)

| Column Name | Data Type | Description | Common Issues |
|-------------|-----------|-------------|---------------|
| `name` | object/string | Product title/name | Brand variations, trailing spaces, inconsistent capitalization |
| `price` | object/string | Product price | Currency symbols (£), special characters, non-numeric values |
| `size` | object/string | Available sizes | Mixed format: sizes with "Out of stock" indicators |
| `description` | object/string | Product description | Empty strings, None values, potential HTML content |

---

## 3. Cleaned/Transformed Columns

### 3.1 Price Column

| Property | Value |
|----------|-------|
| **Data Type** | float64 |
| **Description** | Clean numeric price in GBP (£) |
| **Transformations** | 1. Convert to numeric (`errors='coerce'`)<br>2. Drop invalid entries (NaN)<br>3. Winsorize outliers (1st-99th percentile) |
| **Valid Range** | 1st percentile to 99th percentile |
| **Missing Values** | 0 (dropped during cleaning) |
| **Example Values** | `19.99`, `45.00`, `120.50` |

### 3.2 Brand Column

| Property | Value |
|----------|-------|
| **Data Type** | object/string |
| **Description** | Brand name extracted from product name |
| **Transformations** | 1. Case-insensitive known brand matching<br>2. Fallback to first word or first two words<br>3. Default value for unmatched brands |
| **Missing Values** | 0 (tagged as 'Unknown' if extraction fails) |
| **Example Values** | `ASOS`, `Nike`, `Stradivarius`, `Topshop`, `Unknown` |

### 3.3 Stock Column

| Property | Value |
|----------|-------|
| **Data Type** | object/string |
| **Description** | Product-level stock availability status |
| **Transformations** | 1. Pattern matching on `size` column<br>2. Binary categorization |
| **Valid Values** | `'In stock'`, `'Out of stock'` |
| **Business Rule** | Product has all sizes available = 'In stock'<br>Any size marked OOS = 'Out of stock' |
| **Example Values** | `In stock`, `Out of stock` |

### 3.4 Name Column (Cleaned)

| Property | Value |
|----------|-------|
| **Data Type** | object/string |
| **Description** | Standardized product name |
| **Transformations** | 1. Convert to string<br>2. Strip whitespace<br>3. Replace empty with 'Unknown Product' |
| **Missing Values** | 0 |
| **Example Values** | `ASOS DESIGN Skinny Jeans`, `Nike Air Max`, `Unknown Product` |

### 3.5 Description Column (Cleaned)

| Property | Value |
|----------|-------|
| **Data Type** | object/string |
| **Description** | Standardized product description |
| **Transformations** | 1. Convert to string<br>2. Strip whitespace<br>3. Replace empty with placeholder |
| **Missing Values** | 0 |
| **Example Values** | `Premium cotton denim jeans...`, `No description available` |

---

## 4. Derived Metrics

| Metric Name | Formula | Description | Use Case |
|-------------|---------|-------------|----------|
| `out_of_stock_rate` | `count('Out of stock') / total_count` (by brand) | Percentage of out-of-stock products per brand | Identify popular brands with supply issues |
| `in_stock_rate` | `count('In stock') / total_count` (by brand) | Percentage of in-stock products per brand | Assess brand inventory stability |
| `average_price_by_brand` | `mean(price)` grouped by brand | Mean product price per brand | Price competitiveness analysis |

---

## 5. Data Cleaning Rules

### 5.1 Price Handling

```python
# Step 1: Convert to numeric with coercion
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Step 2: Remove invalid entries
df = df.dropna(subset=['price'])

# Step 3: Winsorize outliers
price_lower = df['price'].quantile(0.01)
price_upper = df['price'].quantile(0.99)
df = df[(df['price'] >= price_lower) & (df['price'] <= price_upper)]
```

### 5.2 Brand Extraction Logic

```python
KNOWN_BRANDS = {
    'ASOS', 'ASOS DESIGN', 'ASOS EDITION', 
    'Topshop', 'Topman', 
    'Nike', 'adidas', 'New Balance', 'Puma', 'Reebok',
    'Stradivarius', 'Zara', 'Pull&Bear', 'Bershka',
    'JDY', 'Jaded London', 'Collusion', 'Collusion x',
    'Levi\\'s', 'Levis', 'Calvin Klein', 'CK'
}

def extract_brand(name):
    name_clean = name.strip().lower()
    for brand in KNOWN_BRANDS:
        if name_clean.startswith(brand.lower()):
            return brand
    # Fallback: first word or first two words
    words = name.split()
    return words[0].capitalize() if len(words) == 1 else ' '.join(words[:2]).capitalize()
```

### 5.3 Stock Status Detection

```python
OOS_PATTERNS = [
    r'\bOut of stock\b',
    r'\boos\b',
    r'out\s*of\s*stock',
    r'\(out of stock\)',
    r'\[out of stock\]',
]

def check_stock_status(size_value):
    for pattern in OOS_PATTERNS:
        if re.search(pattern, str(size_value), re.IGNORECASE):
            return 'Out of stock'
    return 'In stock'
```

### 5.4 Duplicate Handling

```python
# Remove duplicates based on product identity
df = df.drop_duplicates(subset=['name', 'price', 'size'], keep='first')
```

---

## 6. Quality Checks

### 6.1 Missing Values Summary

| Column | Missing Count | Action Taken |
|--------|---------------|--------------|
| `price` | Dropped rows | Removed invalid price entries |
| `brand` | Tagged as 'Unknown' | No data loss |
| `name` | Replaced placeholder | No data loss |
| `description` | Replaced placeholder | No data loss |

### 6.2 Outlier Detection

| Metric | Value |
|--------|-------|
| 1st Percentile | Lower price threshold |
| 99th Percentile | Upper price threshold |
| Outliers Removed | Prices outside thresholds |

### 6.3 Brand Distribution

| Brand Category | Count | Percentage |
|----------------|-------|------------|
| Known Brands | [Auto-generated] | [Auto-generated] |
| Unknown Brands | [Auto-generated] | [Auto-generated] |

### 6.4 Stock Distribution

| Status | Count | Percentage |
|--------|-------|------------|
| In Stock | [Auto-generated] | [Auto-generated] |
| Out of Stock | [Auto-generated] | [Auto-generated] |

---

## 7. Output Files

| File Name | Description | Records | Use Case |
|-----------|-------------|---------|----------|
| `products_asos_in_stock.csv` | Filtered dataset with in-stock products only | Varies | Availability analysis, sales-ready data |
| `products_asos_cleaned.csv` | Full cleaned dataset with all transformations | Varies | Complete analysis, reporting |

---

## 8. Usage Guidelines

### 8.1 For Data Analysts

| Task | Recommended File | Notes |
|------|------------------|-------|
| Availability Analysis | `products_asos_in_stock.csv` | Focus on active inventory |
| Stock Performance | `products_asos_cleaned.csv` | Compare in/out of stock rates |
| Pricing Analysis | `products_asos_cleaned.csv` | All price points included |
| Brand Benchmarking | `products_asos_cleaned.csv` | Full brand comparison |

### 8.2 For Data Consumers

| Consideration | Guidance |
|---------------|----------|
| **Currency** | All prices in GBP (£) |
| **Sizes** | UK sizing format (UK 4, UK 6, etc.) |
| **Stock Status** | Binary: 'In stock' or 'Out of stock' |
| **Brand Names** | Standardized (e.g., 'Nike' not 'Nike Air Max') |
| **Price Values** | Numeric only (no currency symbols) |

### 8.3 Data Limitations

| Limitation | Impact | Workaround |
|------------|--------|------------|
| No timestamp column | Cannot track historical changes | Use current snapshot only |
| No category column | Limited product classification | Infer from brand or description |
| No date range | Cannot analyze seasonality | External date metadata needed |

---

## 9. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0 | Initial | Data Team | Raw data loading and basic cleaning |
| v2.0 | 2026-01-09 | Data Team | Enhanced brand extraction, outlier handling, duplicate removal, comprehensive documentation |
| v2.1 | TBD | TBD | TBD |

---

## Appendix A: Column Dependencies

```
name ──► brand (extracted via regex matching)
size ──► stock (derived via pattern matching)
price ──► outlier handling (winsorized to 1st-99th percentile)
─────────────────────────────────────────────────────────
brand + stock ──► out_of_stock_rate (calculated)
brand ──► average_price_by_brand (calculated)
stock + brand ──► chi-square test (statistical analysis)
```

---

## Appendix B: Related Files

| File | Relationship |
|------|--------------|
| `asos.ipynb` | Notebook containing all data cleaning and analysis |
| `products_asos.csv` | Original source data |
| `products_asos_in_stock.csv` | Filtered output (in-stock only) |
| `products_asos_cleaned.csv` | Full cleaned output |
| `ASOS_Product_Dataset_Data_Dictionary.md` | This documentation file |

---

## Contact & Support

| Type | Information |
|------|-------------|
| **Questions** | Contact the Data Analytics team |
| **Updates** | Check version history for changes |
| **Issues** | Log data quality issues in tracking system |

---

**End of Document**