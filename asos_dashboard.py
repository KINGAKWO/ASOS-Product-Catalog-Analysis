import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="ASOS Product Analysis Dashboard",
    page_icon="🛍️",
    layout="wide"
)

@st.cache_data
def load_data():
    """Load and validate the cleaned data file"""
    try:
        df = pd.read_csv('products_asos_cleaned.csv')
        st.success(f"Successfully loaded {len(df):,} products")
        return df
    except FileNotFoundError:
        st.error("Data file not found! Please ensure 'products_asos_cleaned.csv' exists in the same folder as this script.")
        st.info("Check that this file is in the current directory:")
        import os
        for f in os.listdir('.'):
            if f.endswith('.csv'):
                st.code(f"- {f}")
        return None
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load the data
df = load_data()

if df is not None:
    st.title("🛍️ ASOS Product Catalog Dashboard")
    st.markdown(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    st.markdown(f"**Total Products:** {len(df):,} | **Unique Brands:** {df['brand'].nunique()}")
    st.markdown("---")

    with st.sidebar:
        st.header("🔍 Filters")
        
        # Brand Filter
        if 'brand' in df.columns:
            selected_brands = st.multiselect(
                "Select Brands",
                options=sorted(df['brand'].dropna().unique()),
                default=sorted(df['brand'].dropna().unique())[:5] if len(df['brand'].dropna().unique()) > 5 else df['brand'].dropna().unique()
            )
        else:
            st.warning("No 'brand' column found in dataset")
            selected_brands = []
        
        # Stock Filter
        if 'stock' in df.columns:
            stock_filter = st.selectbox(
                "Stock Status",
                options=["All", "In stock", "Out of stock"],
                index=0
            )
        else:
            stock_filter = "All"
        
        # Price Range Filter
        if 'price' in df.columns:
            min_price, max_price = st.slider(
                "Price Range (£)",
                min_value=float(df['price'].dropna().min()),
                max_value=float(df['price'].dropna().max()),
                value=(float(df['price'].dropna().min()), float(df['price'].dropna().max()))
            )
        else:
            st.warning("No 'price' column found in dataset")
            min_price, max_price = 0, 1000
        
        # Apply filters
        filtered_df = df.copy()
        if selected_brands:
            filtered_df = filtered_df[filtered_df['brand'].isin(selected_brands)]
        if stock_filter != "All":
            filtered_df = filtered_df[filtered_df['stock'] == stock_filter]
        filtered_df = filtered_df[(filtered_df['price'] >= min_price) & (filtered_df['price'] <= max_price)]
        
        st.info(f"**Filtered Results:** {len(filtered_df):,} products")

    # KPI CARDS
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Products", f"{len(filtered_df):,}")
    
    with col2:
        in_stock = filtered_df[filtered_df['stock'] == 'In stock'].shape[0] if 'stock' in filtered_df.columns else 0
        st.metric("In Stock", f"{in_stock:,}")
    
    with col3:
        out_stock = filtered_df[filtered_df['stock'] == 'Out of stock'].shape[0] if 'stock' in filtered_df.columns else 0
        st.metric("Out of Stock", f"{out_stock:,}")
    
    with col4:
        avg_price = filtered_df['price'].mean() if 'price' in filtered_df.columns else 0
        st.metric("Average Price", f"£{avg_price:.2f}")

    st.markdown("---")

    # STOCK STATUS DISTRIBUTION
    st.header("Stock Status Distribution")
    
    if 'stock' in filtered_df.columns:
        stock_counts = filtered_df['stock'].value_counts()
        fig_stock = px.pie(
            values=stock_counts.values,
            names=stock_counts.index,
            title="Stock Availability",
            color_discrete_sequence=['#2ecc71', '#e74c3c']
        )
        st.plotly_chart(fig_stock, use_container_width=True)

    # TOP 10 BRANDS
    st.header("Top 10 Brands")
    
    if 'brand' in filtered_df.columns:
        top_brands = filtered_df['brand'].value_counts().head(10)
        fig_brands = px.bar(
            x=top_brands.index,
            y=top_brands.values,
            title="Top 10 Brands by Product Count",
            labels={'x': 'Brand', 'y': 'Product Count'},
            color=top_brands.values,
            color_continuous_scale='Blues'
        )
        fig_brands.update_layout(xaxis_tickangle=-45, height=450)
        st.plotly_chart(fig_brands, use_container_width=True)

    # PRICING ANALYSIS
    st.header(" Pricing Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        if 'price' in filtered_df.columns:
            fig_price = px.histogram(
                filtered_df,
                x='price',
                nbins=30,
                title="Price Distribution",
                color_discrete_sequence=['#3498db']
            )
            st.plotly_chart(fig_price, use_container_width=True)
    
    with col2:
        if 'price' in filtered_df.columns and 'stock' in filtered_df.columns:
            fig_box = px.box(
                filtered_df,
                x='stock',
                y='price',
                title="Price Distribution by Stock Status",
                color='stock',
                points='all'
            )
            st.plotly_chart(fig_box, use_container_width=True)

    # OUT-OF-STOCK ANALYSIS
    st.header("Out-of-Stock Analysis")
    
    if 'stock' in filtered_df.columns:
        oos_data = filtered_df[filtered_df['stock'] == 'Out of stock'].groupby('brand').size().reset_index(name='count')
        if len(oos_data) > 0:
            oos_data = oos_data.sort_values('count', ascending=True).tail(10)
            fig_oos = px.bar(
                oos_data,
                x='count',
                y='brand',
                orientation='h',
                title="Top 10 Brands with Most Out-of-Stock Products",
                color='count',
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig_oos, use_container_width=True)

    # DATA TABLE
    st.header("📋 Product Preview")
    with st.expander("Show Sample Products"):
        st.dataframe(
            filtered_df[['name', 'brand', 'price', 'stock']].head(50),
            use_container_width=True
        )

    # FOOTER
    st.markdown("---")
    st.markdown(f"""
        <div style="text-align: center; color: #666; font-size: 0.9rem;">
        **ASOS Product Catalog Dashboard** | Data: products_asos_cleaned.csv | {datetime.now().strftime('%Y-%m-%d')}
        </div>
    """, unsafe_allow_html=True)

else:

    st.error("Dashboard cannot be displayed. Please fix the data file issue first.")
