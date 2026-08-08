import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Supply Chain AI",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* =====================================================
       GLOBAL PAGE
       ===================================================== */

    .stApp {
        background: linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef4ff 50%,
            #f8f7ff 100%
        );
    }

    .block-container {
        max-width: 1400px;

        /* FIX TOP TITLE CUTTING */
        padding-top: 4rem !important;
        padding-bottom: 3rem;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    section[data-testid="stSidebar"] h1 {
        color: #172554 !important;
    }

    section[data-testid="stSidebar"] h3 {
        color: #1e3a8a !important;
    }


    /* =====================================================
       MAIN TITLE
       ===================================================== */

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #172554;

        margin-top: 10px;
        margin-bottom: 0;

        letter-spacing: -1px;
    }

    .main-subtitle {
        font-size: 17px;
        color: #64748b;

        margin-top: 8px;
        margin-bottom: 28px;
    }


    /* =====================================================
       METRIC CARDS
       ===================================================== */

    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.95);

        border: 1px solid #e2e8f0;

        border-radius: 18px;

        padding: 20px;

        box-shadow:
            0 8px 25px rgba(15, 23, 42, 0.06);

        transition: all 0.2s ease;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-3px);

        box-shadow:
            0 12px 30px rgba(37, 99, 235, 0.12);
    }

    [data-testid="stMetricLabel"] {
        color: #64748b !important;
        font-weight: 600;
    }

    [data-testid="stMetricValue"] {
        color: #172554 !important;
        font-weight: 800;
    }


    /* =====================================================
       INPUT CONTAINERS
       ===================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {

        background: rgba(255, 255, 255, 0.95);

        border: 1px solid #dbe3ef;

        border-radius: 20px;

        box-shadow:
            0 8px 25px rgba(15, 23, 42, 0.05);

        padding: 10px;
    }


    /* =====================================================
       HEADINGS
       ===================================================== */

    h1,
    h2,
    h3 {
        color: #172554 !important;
    }


    /* =====================================================
       INPUT BOXES
       ===================================================== */

    input,
    textarea {
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] > div {
        border-radius: 10px;
    }


    /* =====================================================
       BUTTON
       ===================================================== */

    .stButton > button {

        width: 100%;

        height: 55px;

        border-radius: 14px;

        border: none;

        background: linear-gradient(
            135deg,
            #2563eb,
            #4f46e5
        );

        color: white;

        font-size: 16px;

        font-weight: 750;

        box-shadow:
            0 8px 20px rgba(37, 99, 235, 0.25);

        transition: all 0.2s ease;
    }

    .stButton > button:hover {

        transform: translateY(-2px);

        background: linear-gradient(
            135deg,
            #1d4ed8,
            #4338ca
        );

        box-shadow:
            0 12px 28px rgba(37, 99, 235, 0.35);
    }


    /* =====================================================
       SUCCESS / ERROR
       ===================================================== */

    div[data-testid="stAlert"] {

        border-radius: 16px;

        padding: 18px;

        font-size: 16px;

        font-weight: 600;
    }


    /* =====================================================
       PROGRESS BAR
       ===================================================== */

    div[data-testid="stProgressBar"] {
        margin-top: 18px;
    }


    /* =====================================================
       EXPANDER
       ===================================================== */

    details {

        background: white;

        border: 1px solid #e2e8f0;

        border-radius: 14px;
    }


    /* =====================================================
       DIVIDER
       ===================================================== */

    hr {
        border-color: #e2e8f0;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    return joblib.load("delay_model.pkl")


model = load_model()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("# 📦 Supply Chain AI")

    st.caption(
        "Intelligent Order Fulfillment System"
    )

    st.divider()

    st.markdown("### 🎯 Prediction System")

    st.write(
        "Machine learning based system for "
        "predicting order fulfillment delays."
    )

    st.divider()

    st.markdown("### 🤖 Model")

    st.info(
        "The trained classification model "
        "estimates the risk of order delay."
    )

    st.divider()

    st.markdown("### 📊 Risk Interpretation")

    st.success(
        "🟢 Low Risk — likely on time"
    )

    st.error(
        "🔴 High Risk — likely delayed"
    )

    st.divider()

    st.caption(
        "Supply Chain Intelligence"
    )

    st.caption(
        "ML Prediction Dashboard"
    )


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<p class="main-title">'
    '📦 Supply Chain Intelligence'
    '</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="main-subtitle">'
    'AI-powered Order Fulfillment Delay Risk Prediction'
    '</p>',
    unsafe_allow_html=True
)


# =========================================================
# TOP METRICS
# =========================================================

c1, c2, c3 = st.columns(3)


with c1:

    st.metric(
        "🤖 SYSTEM",
        "AI Powered",
        "Machine Learning"
    )


with c2:

    st.metric(
        "🎯 TASK",
        "Delay Risk",
        "Order Fulfillment"
    )


with c3:

    st.metric(
        "⚡ DECISION",
        "Binary",
        "On Time / Delayed"
    )


st.write("")


# =========================================================
# ORDER INFORMATION
# =========================================================

st.header("📝 Order Information")

st.caption(
    "Provide operational and logistics details "
    "to evaluate the order's delay risk."
)


# =========================================================
# INPUT SECTION
# =========================================================

col1, col2 = st.columns(2)


# =========================================================
# OPERATIONAL DETAILS
# =========================================================

with col1:

    with st.container(border=True):

        st.subheader(
            "📊 Operational Details"
        )

        st.caption(
            "Warehouse, supplier and order information"
        )


        # Supplier Reliability

        supplier_reliability_score = st.number_input(
            "Supplier Reliability Score",

            min_value=0.0,

            max_value=1.0,

            value=0.80,

            step=0.01
        )


        # Inventory

        warehouse_inventory_level = st.number_input(
            "Warehouse Inventory Level",

            min_value=0,

            value=2000
        )


        # Order Quantity

        order_quantity = st.number_input(
            "Order Quantity",

            min_value=1,

            value=250
        )


        # Processing Time

        processing_time_hours = st.number_input(
            "Processing Time (hours)",

            min_value=0.0,

            value=24.0
        )


        # Shipping Distance

        shipping_distance_km = st.number_input(
            "Shipping Distance (km)",

            min_value=0.0,

            value=500.0
        )


# =========================================================
# LOGISTICS DETAILS
# =========================================================

with col2:

    with st.container(border=True):

        st.subheader(
            "🚚 Logistics Details"
        )

        st.caption(
            "Transportation, weather and timing information"
        )


        # Shipping Method

        shipping_method = st.selectbox(
            "Shipping Method",

            [
                "Road",
                "Rail",
                "Sea",
                "Air"
            ]
        )


        # Weather

        weather_condition = st.selectbox(
            "Weather Condition",

            [
                "Clear",
                "Rain",
                "Fog",
                "Storm"
            ]
        )


        # Priority

        order_priority = st.selectbox(
            "Order Priority",

            [
                "Low",
                "Medium",
                "High"
            ]
        )


        # Order Hour

        order_hour = st.slider(
            "Order Hour",

            0,

            23,

            12
        )


        # Order Day

        order_day = st.slider(
            "Order Day",

            1,

            31,

            15
        )


        # Order Month

        order_month = st.slider(
            "Order Month",

            1,

            12,

            6
        )


        # Day of Week

        order_dayofweek = st.slider(
            "Day of Week",

            0,

            6,

            2
        )


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.write("")

st.markdown(
    "### 🚀 Ready to Analyze?"
)


if st.button(
    "🔮  ANALYZE ORDER DELAY RISK",

    use_container_width=True
):


    # =====================================================
    # INPUT DATA
    # =====================================================

    input_data = pd.DataFrame({

        "supplier_reliability_score":
        [supplier_reliability_score],

        "warehouse_inventory_level":
        [warehouse_inventory_level],

        "order_quantity":
        [order_quantity],

        "shipping_distance_km":
        [shipping_distance_km],

        "shipping_method":
        [shipping_method],

        "weather_condition":
        [weather_condition],

        "processing_time_hours":
        [processing_time_hours],

        "order_priority":
        [order_priority],

        "order_hour":
        [order_hour],

        "order_day":
        [order_day],

        "order_month":
        [order_month],

        "order_dayofweek":
        [order_dayofweek]
    })


    # =====================================================
    # PREDICTION
    # =====================================================

    prediction = model.predict(
        input_data
    )[0]


    # =====================================================
    # PROBABILITY
    # =====================================================

    probability = None


    if hasattr(
        model,
        "predict_proba"
    ):

        probability = model.predict_proba(
            input_data
        )[0][1]


    # =====================================================
    # RESULT
    # =====================================================

    st.divider()

    st.header(
        "🎯 Prediction Result"
    )


    # =====================================================
    # HIGH RISK
    # =====================================================

    if prediction == 1:

        st.error(
            "⚠️ HIGH RISK — "
            "ORDER LIKELY TO BE DELAYED"
        )

        st.write(
            "The current operational and logistics "
            "conditions indicate a higher risk of "
            "fulfillment delay."
        )


    # =====================================================
    # LOW RISK
    # =====================================================

    else:

        st.success(
            "✅ LOW RISK — "
            "ORDER LIKELY TO BE ON TIME"
        )

        st.write(
            "The current operational and logistics "
            "conditions indicate a lower risk of "
            "fulfillment delay."
        )


    # =====================================================
    # PROBABILITY
    # =====================================================

    if probability is not None:

        st.subheader(
            "📈 Delay Probability"
        )

        p1, p2 = st.columns(
            [1, 3]
        )


        with p1:

            st.metric(
                "Risk Probability",

                f"{probability * 100:.2f}%"
            )


        with p2:

            st.progress(
                float(probability)
            )


    # =====================================================
    # INPUT SUMMARY
    # =====================================================

    st.write("")

    with st.expander(
        "📋 View Prediction Input Summary"
    ):

        st.dataframe(
            input_data,

            use_container_width=True,

            hide_index=True
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "📦 Supply Chain Intelligence  •  "
    "AI-powered Order Fulfillment Risk Prediction"
)