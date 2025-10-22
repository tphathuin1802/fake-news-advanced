import requests
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Introduction", layout="wide")

# --- CSS TUỲ CHỈNH ---
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


# --- BANNER (TỰ ĐỘNG KIỂM TRA NGUỒN HÌNH KHẢ DỤNG) ---
def get_working_image(urls, timeout=5):
    for url in urls:
        try:
            r = requests.head(url, timeout=timeout)
            if r.status_code == 200:
                return url
        except Exception:
            continue
    return None


banner_urls = [
    "https://images.unsplash.com/photo-1590608897129-79da98d159f1?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&w=1600&q=80",
    "https://images.unsplash.com/photo-1581093588401-22b3031a798f?auto=format&fit=crop&w=1600&q=80",
]

banner = get_working_image(banner_urls)

if banner:
    st.image(
        banner,
        use_container_width=True,
        caption="Fake vs True News — Understanding Truth in the Digital Era",
    )
else:
    st.markdown(
        """
        <div style="display:flex;align-items:center;justify-content:center;width:100%;height:320px;border-radius:8px;
                    background:linear-gradient(90deg,#f0f8ff,#eef6ff);box-shadow:0 2px 6px rgba(0,0,0,0.06);margin-bottom:16px;">
          <p style="font-family: 'JetBrains Mono', monospace; color:#1E90FF; font-size:20px;">
          [ Banner image unavailable — using placeholder ]
          </p>
        </div>
        """,
        unsafe_allow_html=True,
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
