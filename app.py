import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Employee Attrition Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("EA.csv")

df = load_data()

st.title("Employee Attrition Dashboard")
st.markdown("An interactive insight platform for HR Directors to explore attrition patterns and workforce dynamics.")

# Sidebar filters
st.sidebar.header("Filters")
departments = st.sidebar.multiselect("Select Department", options=df['Department'].unique(), default=df['Department'].unique())
genders = st.sidebar.multiselect("Select Gender", options=df['Gender'].unique(), default=df['Gender'].unique())
education_fields = st.sidebar.multiselect("Select Education Field", options=df['EducationField'].unique(), default=df['EducationField'].unique())

df_filtered = df[
    (df['Department'].isin(departments)) &
    (df['Gender'].isin(genders)) &
    (df['EducationField'].isin(education_fields))
]

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Attrition Drivers", "Salary & Satisfaction", "Experience & Tenure", "Custom Exploration"])

with tab1:
    st.subheader("1. Attrition Rate by Department")
    fig1 = px.histogram(df_filtered, x='Department', color='Attrition', barmode='group')
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("2. Age Distribution")
    fig2 = px.histogram(df_filtered, x='Age', color='Attrition', barmode='overlay')
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("3. Gender Distribution")
    fig3 = px.histogram(df_filtered, x='Gender', color='Attrition', barmode='group')
    st.plotly_chart(fig3, use_container_width=True)

with tab2:
    st.subheader("4. Attrition by Job Role")
    fig4 = px.histogram(df_filtered, x='JobRole', color='Attrition', barmode='group')
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("5. Attrition by Overtime")
    fig5 = px.histogram(df_filtered, x='OverTime', color='Attrition', barmode='group')
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("6. Attrition by Distance From Home")
    fig6 = px.box(df_filtered, x='Attrition', y='DistanceFromHome')
    st.plotly_chart(fig6, use_container_width=True)

    st.subheader("7. Attrition by Business Travel")
    fig7 = px.histogram(df_filtered, x='BusinessTravel', color='Attrition', barmode='group')
    st.plotly_chart(fig7, use_container_width=True)

with tab3:
    st.subheader("8. Monthly Income Distribution")
    fig8 = px.box(df_filtered, x='Attrition', y='MonthlyIncome')
    st.plotly_chart(fig8, use_container_width=True)

    st.subheader("9. Satisfaction vs Monthly Income")
    fig9 = px.scatter(df_filtered, x='MonthlyIncome', y='JobSatisfaction', color='Attrition')
    st.plotly_chart(fig9, use_container_width=True)

    st.subheader("10. Job Satisfaction Distribution")
    fig10 = px.histogram(df_filtered, x='JobSatisfaction', color='Attrition')
    st.plotly_chart(fig10, use_container_width=True)

    st.subheader("11. Work-Life Balance Distribution")
    fig11 = px.histogram(df_filtered, x='WorkLifeBalance', color='Attrition')
    st.plotly_chart(fig11, use_container_width=True)

with tab4:
    st.subheader("12. Total Working Years vs Attrition")
    fig12 = px.box(df_filtered, x='Attrition', y='TotalWorkingYears')
    st.plotly_chart(fig12, use_container_width=True)

    st.subheader("13. Years at Company")
    fig13 = px.histogram(df_filtered, x='YearsAtCompany', color='Attrition', nbins=20)
    st.plotly_chart(fig13, use_container_width=True)

    st.subheader("14. Years in Current Role")
    fig14 = px.histogram(df_filtered, x='YearsInCurrentRole', color='Attrition', nbins=15)
    st.plotly_chart(fig14, use_container_width=True)

    st.subheader("15. Years with Current Manager")
    fig15 = px.histogram(df_filtered, x='YearsWithCurrManager', color='Attrition')
    st.plotly_chart(fig15, use_container_width=True)

with tab5:
    st.subheader("16. Explore Any Two Variables")
    x_axis = st.selectbox("Select X-Axis", df.columns)
    y_axis = st.selectbox("Select Y-Axis", df.columns, index=1)
    color_by = st.selectbox("Color By", df.columns, index=df.columns.get_loc("Attrition"))
    fig_custom = px.scatter(df_filtered, x=x_axis, y=y_axis, color=color_by)
    st.plotly_chart(fig_custom, use_container_width=True)

    st.subheader("17. Data Table View")
    st.dataframe(df_filtered)

    st.subheader("18. Attrition Counts")
    st.bar_chart(df_filtered['Attrition'].value_counts())

    st.subheader("19. Department-wise Attrition %")
    attrition_rate = df_filtered[df_filtered['Attrition'] == 'Yes'].groupby('Department').size() / df_filtered.groupby('Department').size()
    st.bar_chart(attrition_rate)

    st.subheader("20. Correlation Heatmap")
    numeric_df = df_filtered.select_dtypes(include='number')
    st.dataframe(numeric_df.corr())
