import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Introduction", layout="wide")

# --- CSS TÙY CHỈNH ---
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
    </style>
    """,
    unsafe_allow_html=True,
)

# --- TITLE ---
st.markdown(
    "<div class='main-title'>Fake News Detection with Machine Learning</div>",
    unsafe_allow_html=True,
)

# --- BANNER HÌNH ẢNH (Unsplash, chủ đề “AI & News Media”) ---
st.image(
    "https://images.unsplash.com/photo-1581091215367-59ab6a3b44c6?auto=format&fit=crop&w=1600&q=80",
    use_container_width=True,
    caption="AI and Media Illustration — Understanding Truth in the Digital Age",
)

# --- INTRODUCTION ---
st.markdown("<div class='section-header'>1. Introduction</div>", unsafe_allow_html=True)
st.markdown(
    """
<div class="highlight">
In an era where misinformation spreads faster than ever, the ability to automatically detect fake news is a powerful tool for promoting media literacy and truth.  
This project demonstrates a complete workflow — from data preprocessing to model deployment — to classify news articles as **True** or **Fake** using machine learning techniques.
</div>
""",
    unsafe_allow_html=True,
)

# --- PROJECT OBJECTIVES ---
st.markdown(
    "<div class='section-header'>1.1 Project Objectives</div>", unsafe_allow_html=True
)
st.markdown(
    """
<div class="highlight">
- **Develop a Robust Classifier:** Build a system that can reliably distinguish between legitimate and fabricated news articles.  
- **Compare Model Architectures:** Evaluate models like Logistic Regression, Random Forest, and Gradient Boosting for performance and interpretability.  
- **Perform Interactive EDA:** Use visualization to uncover patterns and biases in the dataset.  
- **Deploy an Interactive Web App:** Enable real-time predictions where users can input news text and receive instant feedback.
</div>
""",
    unsafe_allow_html=True,
)

# --- DATASET INFORMATION ---
st.markdown("<div class='section-header'>1.2 The Dataset</div>", unsafe_allow_html=True)
st.markdown(
    """
<div class="highlight">
The dataset used in this project is sourced from Kaggle and consists of two parts:
- **True News:** ~21,400 articles (primarily from Reuters).  
- **Fake News:** ~23,400 articles from various sources known for misinformation.

The dataset can be accessed here:  
👉 [Kaggle - Fake News Detection Datasets](https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets)
</div>
""",
    unsafe_allow_html=True,
)

# --- FOOTER ---
st.markdown(
    "<div class='footer-note'>📘 Use the sidebar to navigate through the project sections.</div>",
    unsafe_allow_html=True,
)
