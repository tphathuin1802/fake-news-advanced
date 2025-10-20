import pandas as pd
import plotly.express as px
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Model Performance", layout="wide")

# --- CSS STYLE ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'JetBrains Mono', monospace;
    }

    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        color: #2F4F4F;
        margin-top: 0.5em;
        margin-bottom: 0.5em;
    }

    .section-header {
        font-size: 1.6rem;
        font-weight: 700;
        color: #1E90FF;
        border-left: 6px solid #1E90FF;
        padding-left: 12px;
        margin-top: 2em;
    }

    .highlight {
        background-color: #f8fbff;
        border-left: 4px solid #1E90FF;
        padding: 0.8em 1em;
        border-radius: 10px;
        margin-bottom: 1.2em;
        line-height: 1.6;
    }

    .footer-note {
        text-align: center;
        font-style: italic;
        color: gray;
        margin-top: 2em;
    }

    .insight-box {
        background-color: #fefefe;
        border-left: 4px solid #32CD32;
        padding: 1em 1.2em;
        border-radius: 10px;
        margin-top: 2em;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- PAGE TITLE ---
st.markdown(
    "<div class='main-title'>Model Performance & Evaluation</div>",
    unsafe_allow_html=True,
)

# --- BANNER ---
st.image(
    "https://images.unsplash.com/photo-1639322537228-f710d846310a?auto=format&fit=crop&w=1600&q=80",
    use_container_width=True,
    caption="AI Model Evaluation & Performance Dashboard",
)

# --- INTRODUCTION ---
st.markdown("<div class='section-header'>Overview</div>", unsafe_allow_html=True)
st.markdown(
    """
<div class="highlight">
This section details the performance of each machine learning model trained on the fake news dataset.  
Each model was evaluated using a **20% held-out test set**, focusing on **accuracy, precision, recall, and F1-score**.
</div>
""",
    unsafe_allow_html=True,
)


# --- Helper functions ---
def create_cm_df(tp, fp, fn, tn):
    return pd.DataFrame(
        [[tn, fp], [fn, tp]],
        columns=["Predicted Fake", "Predicted True"],
        index=["Actual Fake", "Actual True"],
    )


def create_report_df(p_fake, r_fake, f1_fake, p_true, r_true, f1_true):
    return pd.DataFrame(
        {
            "Metric": ["Precision", "Recall", "F1-Score"],
            "Fake (0)": [p_fake, r_fake, f1_fake],
            "True (1)": [p_true, r_true, f1_true],
        }
    ).set_index("Metric")


# --- EVALUATION METRICS (with Tabs) ---
st.markdown(
    "<div class='section-header'>Evaluation Metrics</div>", unsafe_allow_html=True
)
st.markdown(
    """
<div class="highlight">
Evaluation metrics help quantify how well a model distinguishes between fake and true news articles.  
Select each tab below to explore the formulas used to compute the model’s performance.
</div>
""",
    unsafe_allow_html=True,
)

m1, m2, m3 = st.tabs(["Confusion Matrix", "Precision & Recall", "F1 Score"])

with m1:
    st.image(
        "./assets/confusion_matrix.png",
        caption="Confusion Matrix",
        use_container_width=True,
    )
    st.markdown(
        """
The **confusion matrix** shows how many samples were correctly or incorrectly classified:

- **True Positives (TP):** Fake news correctly identified as fake.  
- **True Negatives (TN):** Real news correctly identified as true.  
- **False Positives (FP):** Real news wrongly flagged as fake.  
- **False Negatives (FN):** Fake news wrongly marked as true.
"""
    )

with m2:
    colA, colB = st.columns(2)
    with colA:
        st.image(
            "./assets/precision.png",
            caption="Precision Formula",
            use_container_width=True,
        )
    with colB:
        st.image(
            "./assets/recall.png",
            caption="Recall Formula",
            use_container_width=True,
        )

    st.markdown(
        """
**Precision:** Of all news flagged as fake, how many were truly fake?  
**Recall:** Of all actual fake news, how many did the model correctly detect?
"""
    )

with m3:
    st.image(
        "./assets/f1_score.png", caption="F1 Score Formula", use_container_width=True
    )
    st.markdown(
        """
The **F1 Score** balances precision and recall:  
when both are high, F1 is also high — a good overall indicator of model performance.
"""
    )

# --- MODEL RESULTS ---
tab1, tab2, tab3 = st.tabs(
    ["Logistic Regression", "Random Forest", "Gradient Boosting"]
)

with tab1:
    st.subheader("Logistic Regression Results")
    st.metric(label="Test Accuracy", value="98.7%")
    cm_lr = create_cm_df(tp=4150, fp=50, fn=65, tn=4600)
    report_lr = create_report_df(0.98, 0.99, 0.98, 0.99, 0.98, 0.98)
    fig_lr = px.imshow(
        cm_lr,
        text_auto=True,
        color_continuous_scale="Blues",
        title="Confusion Matrix — Logistic Regression",
    )
    st.plotly_chart(fig_lr, use_container_width=True)
    st.dataframe(report_lr, use_container_width=True)

with tab2:
    st.subheader("Random Forest Results")
    st.metric(label="Test Accuracy", value="99.1%")
    cm_rfc = create_cm_df(tp=4170, fp=30, fn=50, tn=4615)
    report_rfc = create_report_df(0.99, 0.99, 0.99, 0.99, 0.99, 0.99)
    fig_rfc = px.imshow(
        cm_rfc,
        text_auto=True,
        color_continuous_scale="Greens",
        title="Confusion Matrix — Random Forest",
    )
    st.plotly_chart(fig_rfc, use_container_width=True)
    st.dataframe(report_rfc, use_container_width=True)

with tab3:
    st.subheader("Gradient Boosting Results")
    st.metric(label="Test Accuracy", value="99.0%")
    cm_gbc = create_cm_df(tp=4165, fp=35, fn=55, tn=4610)
    report_gbc = create_report_df(0.99, 0.99, 0.99, 0.99, 0.99, 0.99)
    fig_gbc = px.imshow(
        cm_gbc,
        text_auto=True,
        color_continuous_scale="Oranges",
        title="Confusion Matrix — Gradient Boosting",
    )
    st.plotly_chart(fig_gbc, use_container_width=True)
    st.dataframe(report_gbc, use_container_width=True)

# --- INSIGHTS ---
st.markdown(
    "<div class='section-header'>Performance Insights</div>", unsafe_allow_html=True
)
st.markdown(
    """
<div class="insight-box">
- All three models achieved **exceptional accuracy (>98%)**, showing strong classification ability.  
- **Random Forest** slightly outperformed others with fewer false predictions.  
- **Logistic Regression** offered solid results with less computational cost.  
- **Gradient Boosting** provided balanced results, reducing both FP and FN.  
</div>
""",
    unsafe_allow_html=True,
)

# --- CONCLUSION ---
st.markdown("<div class='section-header'>Conclusion</div>", unsafe_allow_html=True)
st.markdown(
    """
<div class="highlight">
Traditional ML models combined with TF-IDF text features can deliver highly accurate fake news detection.  
Future work may explore transformer-based NLP models for improved contextual understanding.
</div>
""",
    unsafe_allow_html=True,
)

# --- FOOTER ---
st.markdown(
    "<div class='footer-note'>📊 Machine Learning Model Evaluation | Streamlit Dashboard © 2025</div>",
    unsafe_allow_html=True,
)
