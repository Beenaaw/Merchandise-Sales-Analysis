import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Merch Sales Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("merch_sales.csv")

df = load_data()

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Select Section", [
    "Overview Project",
    "Dashboard",
    "Insight & Recommendation"
])

# 1. Overview
if menu == "Overview Project":
    st.title("MERCH SALES ANALYSIS: PRICE, SHIPPING AND CUSTOMER")
    st.markdown("""
    **Background:** The merchandise sales data from a US-based influencer’s global retail website shows fluctuating trends across 2023-2024. This analysis explores the impact of price, shipping, product preferences, reviews, and demographics on sales.

    **Goal:** Help optimize marketing and distribution strategy to ensure sustainable growth in digital retail.
    """)

# 2. Dashboard
elif menu == "Dashboard":
    st.title("📊 Interactive Sales Dashboard")

    # KPI Metrics
    total_sales = df["Sales Price"].sum()
    total_orders = df.shape[0]
    avg_rating = df["Rating"].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${total_sales:,.0f}")
    col2.metric("Total Orders", f"{total_orders:,}")
    col3.metric("Average Rating", f"{avg_rating:.2f}")

    st.markdown("---")
    st.subheader("Sales by Product Category and Shipping Type")
    col4, col5 = st.columns(2)

    with col4:
        cat_sales = df.groupby("Product Category")["Sales Price"].sum().sort_values()
        fig1, ax1 = plt.subplots()
        cat_sales.plot(kind="barh", color="mediumseagreen", ax=ax1)
        ax1.set_xlabel("Total Sales")
        st.pyplot(fig1)

    with col5:
        shipping_count = df["International Shipping"].value_counts()
        fig2, ax2 = plt.subplots()
        shipping_count.plot.pie(autopct="%1.1f%%", colors=["gold", "lightblue"], ax=ax2)
        ax2.set_ylabel("")
        st.pyplot(fig2)

    st.markdown("---")
    st.subheader("Shipping Charges vs Sales")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df, x="Shipping Charges", y="Sales Price", hue="International Shipping", ax=ax3)
    st.pyplot(fig3)

    st.markdown("---")
    st.subheader("Customer Demographics")
    col6, col7 = st.columns(2)

    with col6:
        gender = df["Buyer Gender"].value_counts()
        st.bar_chart(gender)

    with col7:
        fig4, ax4 = plt.subplots()
        sns.histplot(df["Buyer Age"], kde=True, ax=ax4)
        st.pyplot(fig4)

    st.markdown("---")
    st.subheader("Product Ratings")
    col8, col9 = st.columns(2)

    with col8:
        rating = df["Rating"].value_counts().sort_index()
        st.bar_chart(rating)

    with col9:
        fig5, ax5 = plt.subplots()
        sns.boxplot(x="Rating", y="Sales Price", data=df, ax=ax5)
        st.pyplot(fig5)

    st.markdown("---")
    st.subheader("Top 10 Locations by Sales")
    loc_sales = df.groupby("Order Location")["Sales Price"].sum().sort_values(ascending=False).head(10)
    fig6, ax6 = plt.subplots()
    loc_sales.plot(kind="bar", color="coral", ax=ax6)
    ax6.set_ylabel("Total Sales")
    st.pyplot(fig6)

# 3. Insight & Recommendation
elif menu == "Insight & Recommendation":
    st.title("🧠 Insights & 🎯 Recommendations")

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("🔍 Insights")
        st.markdown("""
        - **Clothing** tetap menghasilkan penjualan tinggi di berbagai harga.
        - Pengiriman **lokal** lebih dominan, tapi **internasional** tetap berdampak besar.
        - **Shipping charges kecil** cenderung menghasilkan penjualan lebih tinggi.
        - Mayoritas pembeli adalah **laki-laki usia 25-35 tahun**.
        - Produk dengan **rating 4 dan 5** menyumbang lebih dari 60% total penjualan.
        - **Sydney** jadi kota dengan total penjualan terbesar.
        """)

    with col_right:
        st.subheader("📌 Recommendations")
        st.markdown("""
        - Lakukan **promosi/diskon** untuk produk kategori Ornaments dan Other.
        - Tawarkan **gratis ongkir internasional** untuk mendorong pembeli luar negeri.
        - Perluas campaign ke **perempuan dan remaja** lewat TikTok dan Instagram.
        - Kombinasikan produk **rating rendah dengan tinggi** dalam bentuk bundling.
        - Gunakan rating tinggi sebagai materi promosi dalam konten pemasaran.
        """)