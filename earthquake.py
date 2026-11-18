
import streamlit as st
import pandas as pd

# --------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Global Earthquake Analytics",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# SIDEBAR INFORMATION

st.sidebar.title("🌍 Earthquake Analytics")

st.sidebar.markdown("---")

st.sidebar.subheader("About Project")

st.sidebar.write(
    """
    This dashboard analyzes global earthquake
    records from 2021 to 2025.

    **Technologies Used:**
    - Python
    - Pandas
    - Streamlit
    - Matplotlib
    - Data Visualization
    """
)

st.sidebar.markdown("---")

st.sidebar.caption("Earthquake Analytics Project | GUVI")

# --------------------------------
# 2. DASHBOARD TITLE
# --------------------------------

st.title("🌍 Global Earthquake Analytics Dashboard")

st.write("### Analysis of Global Earthquakes (2021–2025)")

st.markdown("---")

# --------------------------------
# 3. LOAD DATASET
# --------------------------------

#df = pd.read_csv("earthquake_cleaned.csv")
df = pd.read_csv("earthquake_cleaned.zip", compression="zip")

# --------------------------------
# 4. DATASET OVERVIEW
# --------------------------------

st.subheader("📊 Dataset Overview")

col1, col2 = st.columns(2)

with col1:
    st.write("**Total Records:**", f"{len(df):,}")

with col2:
    st.write("**Total Columns:**", len(df.columns))

st.markdown("---")

# --------------------------------
# 4. INTERACTIVE FILTERS
# --------------------------------

st.sidebar.header("🔎 Earthquake Filters")

# Convert time column to datetime
df["time"] = pd.to_datetime(df["time"], errors="coerce", utc=True)

# Year filter
df["year"] = df["time"].dt.year

available_years = sorted(df["year"].dropna().unique())

selected_years = st.sidebar.multiselect(
    "Select Year",
    available_years,
    default=available_years
)

# Magnitude filter
min_mag = float(df["mag"].min())
max_mag = float(df["mag"].max())

mag_range = st.sidebar.slider(
    "Select Magnitude Range",
    min_value=min_mag,
    max_value=max_mag,
    value=(min_mag, max_mag)
)

# Depth filter
min_depth = float(df["depth_km"].min())
max_depth = float(df["depth_km"].max())

depth_range = st.sidebar.slider(
    "Select Depth Range (km)",
    min_value=min_depth,
    max_value=max_depth,
    value=(min_depth, max_depth)
)

# Apply filters
filtered_df = df[
    (df["year"].isin(selected_years)) &
    (df["mag"].between(mag_range[0], mag_range[1])) &
    (df["depth_km"].between(depth_range[0], depth_range[1]))
]

st.sidebar.success(
    f"Filtered Records: {len(filtered_df):,}"
)


# --------------------------------
# 5. KEY PERFORMANCE INDICATORS
# --------------------------------


# --------------------------------
# 5. KEY PERFORMANCE INDICATORS
# --------------------------------

st.subheader("📌 Earthquake Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Earthquakes",
        value=f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        label="Average Magnitude",
        value=round(filtered_df["mag"].mean(), 2)
        if not filtered_df.empty else "N/A"
    )

with col3:
    st.metric(
        label="Maximum Magnitude",
        value=round(filtered_df["mag"].max(), 2)
        if not filtered_df.empty else "N/A"
    )

with col4:
    st.metric(
        label="Average Depth (km)",
        value=round(filtered_df["depth_km"].mean(), 2)
        if not filtered_df.empty else "N/A"
    )

st.markdown("---")

# --------------------------------
# 6. EARTHQUAKE DATA PREVIEW
# --------------------------------

# --------------------------------
# 6. EARTHQUAKE DATA PREVIEW
# --------------------------------

st.subheader("🔍 Earthquake Data Preview")

st.dataframe(
    filtered_df.head(10),
    width="stretch"
)
# --------------------------------
# 7. DATASET INFORMATION
# --------------------------------

st.subheader("📋 Dataset Information")

st.write("Column Names:")

st.write(list(df.columns))

st.success("Earthquake dataset loaded successfully!")

st.dataframe(
    df.head(10),
    use_container_width=True
)


# MAGNITUDE DISTRIBUTION

st.markdown("---")

st.subheader("📊 Earthquake Magnitude Distribution")

if not filtered_df.empty:

    magnitude_chart = (
        filtered_df["mag"]
        .dropna()
        .value_counts()
        .sort_index()
    )

    st.bar_chart(
        magnitude_chart,
        x_label="Magnitude",
        y_label="Number of Earthquakes"
    )

else:
    st.warning("No earthquake records available for the selected filters.")


# --------------------------------
# 8. EARTHQUAKE DEPTH DISTRIBUTION
# --------------------------------

st.markdown("---")

st.subheader("🌊 Earthquake Depth Distribution")

if not filtered_df.empty:

    depth_chart = (
        filtered_df["depth_km"]
        .dropna()
        .value_counts()
        .sort_index()
    )

    st.line_chart(
        depth_chart,
        x_label="Depth (km)",
        y_label="Number of Earthquakes"
    )

else:
    st.warning("No earthquake records available for the selected filters.")


# --------------------------------
# 9. YEAR-WISE EARTHQUAKE TREND
# --------------------------------

st.markdown("---")

st.subheader("📅 Year-wise Earthquake Trend")

if not filtered_df.empty:

    yearly_earthquakes = (
        filtered_df.groupby("year")["id"]
        .count()
        .reset_index()
    )

    yearly_earthquakes.columns = [
        "Year",
        "Number of Earthquakes"
    ]

    st.line_chart(
        yearly_earthquakes,
        x="Year",
        y="Number of Earthquakes",
        x_label="Year",
        y_label="Number of Earthquakes"
    )

else:
    st.warning("No earthquake records available for the selected filters.")

# --------------------------------
# 10. GLOBAL EARTHQUAKE MAP
# --------------------------------

st.markdown("---")

st.subheader("🌍 Global Earthquake Distribution Map")

if not filtered_df.empty:

    map_data = filtered_df[
        ["latitude", "longitude"]
    ].dropna()

    st.map(
        map_data,
        latitude="latitude",
        longitude="longitude",
        size=8
    )

else:
    st.warning("No earthquake locations available for the selected filters.")

# --------------------------------
# 11. TSUNAMI ANALYSIS
# --------------------------------

st.markdown("---")

st.subheader("🌊 Tsunami Analysis")

if not filtered_df.empty:

    tsunami_counts = (
        filtered_df["tsunami"]
        .map({0: "No Tsunami", 1: "Tsunami"})
        .fillna("Unknown")
        .value_counts()
    )

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Tsunami Distribution**")

        st.bar_chart(
            tsunami_counts,
            y_label="Number of Earthquakes"
        )

    with col2:
        st.write("**Tsunami Summary**")

        tsunami_total = (
            filtered_df["tsunami"] == 1
        ).sum()

        no_tsunami_total = (
            filtered_df["tsunami"] == 0
        ).sum()

        st.metric(
            "Earthquakes with Tsunami",
            f"{tsunami_total:,}"
        )

        st.metric(
            "Earthquakes without Tsunami",
            f"{no_tsunami_total:,}"
        )

else:
    st.warning("No earthquake records available for the selected filters.")

# --------------------------------
# 12. BUSINESS INSIGHTS
# --------------------------------

st.markdown("---")

st.header("💡 Key Earthquake Insights")

if not filtered_df.empty:

    # Strongest Earthquake
    strongest = filtered_df["mag"].max()

    # Deepest Earthquake
    deepest = filtered_df["depth_km"].max()

    # Year with Maximum Earthquakes
    yearly_count = filtered_df["year"].value_counts()

    busiest_year = yearly_count.idxmax()
    highest_count = yearly_count.max()

    # Tsunami Events
    tsunami_count = (filtered_df["tsunami"] == 1).sum()

    st.markdown("### 📌 Major Findings")

    st.write(
        f"1. The highest earthquake magnitude recorded "
        f"in the selected data is **{strongest:.2f}**."
    )

    st.write(
        f"2. The deepest earthquake recorded is "
        f"**{deepest:.2f} km**."
    )

    st.write(
        f"3. The year **{int(busiest_year)}** recorded "
        f"the highest number of earthquakes "
        f"({highest_count:,})."
    )

    st.write(
        f"4. A total of **{tsunami_count:,}** earthquakes "
        f"were associated with tsunami events."
    )

else:
    st.warning("No data available to generate insights.")

st.markdown("---")

st.caption(
    "Global Earthquake Analytics Dashboard | "
    "Data Analysis Project | 2021–2025"
)
