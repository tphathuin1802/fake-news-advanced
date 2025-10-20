import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Conclusion & Future Work", layout="wide")

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

# --- TIÊU ĐỀ ---
st.markdown(
    "<div class='main-title'>Conclusion & Future Work</div>", unsafe_allow_html=True
)

# --- BANNER MINH HỌA (từ Unsplash, 4K, còn hoạt động tốt) ---
st.image(
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1600&q=80",
    use_container_width=True,
    caption="Machine Learning & Data Insights Illustration",
)

# --- PHẦN 6: TỔNG KẾT DỰ ÁN ---
st.markdown(
    "<div class='section-header'>6. Project Summary</div>", unsafe_allow_html=True
)
st.markdown(
    """
<div class="highlight">
This project demonstrates the complete process of developing a machine learning-based fake news detector.  
Through effective NLP preprocessing and strong classification algorithms, it achieves high accuracy in distinguishing between real and fake news.

The ensemble of Logistic Regression, Random Forest, and Gradient Boosting improves stability and reliability.  
This Streamlit web app serves as an interactive proof-of-concept, allowing real-time predictions and exploration of model behavior.
</div>
""",
    unsafe_allow_html=True,
)

# --- PHẦN 7: GIỚI HẠN ---
st.markdown("<div class='section-header'>7. Limitations</div>", unsafe_allow_html=True)
st.markdown(
    """
<div class="highlight">
Although results are strong, the project faces some limitations:

- 🧠 **Dataset Bias:** The model may learn writing patterns from specific sources (e.g., Reuters vs. political blogs) rather than true credibility.  
- ⚙️ **Evolving Misinformation:** Fake news strategies evolve rapidly — current models may fail against AI-generated or more subtle misinformation.  
- 🎭 **Lack of Nuance:** The binary classification (True/Fake) cannot recognize satire, opinion articles, or mixed-content cases.
</div>
""",
    unsafe_allow_html=True,
)

# --- PHẦN 8: HƯỚNG PHÁT TRIỂN ---
st.markdown("<div class='section-header'>8. Future Work</div>", unsafe_allow_html=True)
st.markdown(
    """
<div class="highlight">
To strengthen model reliability and practical use, future improvements include:

- **Expanding Dataset:** Use a more diverse and up-to-date dataset to improve generalization.  
- **Adopting Advanced NLP Models:** Implement Transformer architectures (e.g., BERT, RoBERTa) for contextual understanding.  
- **Feature Enrichment:** Add meta-features such as headline sentiment, author/source credibility, and writing style.  
- **Integration with Fact-Checking APIs:** Connect with verified databases for enhanced transparency and explainability.
</div>
""",
    unsafe_allow_html=True,
)

# --- FOOTER ---
st.markdown(
    "<div class='footer-note'>🚀 Built with Streamlit | Empowering Transparency in Machine Learning</div>",
    unsafe_allow_html=True,
)
