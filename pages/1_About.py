import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="About & Methodology", layout="wide")

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
    "<div class='main-title'>About the Project & Methodology</div>",
    unsafe_allow_html=True,
)

# --- BANNER (Unsplash: AI + Research Theme) ---
st.image(
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80",
    use_container_width=True,
    caption="Machine Learning Research & Workflow Illustration",
)

# --- SECTION: METHODOLOGY ---
st.markdown("<div class='section-header'>2. Methodology</div>", unsafe_allow_html=True)
st.markdown(
    """
<div class="highlight">
The project follows a structured machine learning pipeline — from data collection and preprocessing to model training and evaluation.
</div>
""",
    unsafe_allow_html=True,
)

# --- 2.1 DATA LOADING ---
st.markdown(
    "<div class='section-header'>2.1 Data Loading and Preparation</div>",
    unsafe_allow_html=True,
)
st.markdown(
    """
<div class="highlight">
- **Loading:** The `Fake.csv` and `True.csv` datasets are loaded into memory.  
- **Labeling:** A new column `label` is added (`1` = True, `0` = Fake).  
- **Merging & Shuffling:** Both datasets are concatenated and randomly shuffled to avoid source bias or ordering effects.
</div>
""",
    unsafe_allow_html=True,
)

# --- 2.2 TEXT PREPROCESSING ---
st.markdown(
    "<div class='section-header'>2.2 Text Preprocessing</div>", unsafe_allow_html=True
)
st.markdown(
    """
<div class="highlight">
Before training, all text undergoes normalization and cleaning:  
1. Convert to lowercase  
2. Remove URLs, HTML tags, punctuation, and digits  
3. Remove English stopwords (e.g., *the, is, and*)  
4. Trim extra spaces  

These steps ensure the model focuses on meaningful content rather than formatting.
</div>
""",
    unsafe_allow_html=True,
)

# --- 2.3 FEATURE ENGINEERING ---
st.markdown(
    "<div class='section-header'>2.3 Feature Engineering (TF-IDF)</div>",
    unsafe_allow_html=True,
)
st.markdown(
    """
<div class="highlight">
- **Tokenization:** Splitting text into words (tokens).  
- **Vectorization:** Using `TfidfVectorizer` to convert text into numerical form.  
- **TF-IDF (Term Frequency–Inverse Document Frequency):** Assigns higher weights to informative words while reducing the influence of common terms.  
- The model uses both unigrams and bigrams for richer representation.
</div>
""",
    unsafe_allow_html=True,
)

# --- 2.4 MODEL TRAINING ---
st.markdown(
    "<div class='section-header'>2.4 Model Training</div>", unsafe_allow_html=True
)
st.markdown(
    """
<div class="highlight">
Three machine learning models were trained on an 80/20 train-test split:
- **Logistic Regression:** Interpretable linear model used as a baseline.  
- **Random Forest:** Ensemble of decision trees — reduces overfitting.  
- **Gradient Boosting:** Sequential tree ensemble with error correction — often achieves top performance.  

The deployed app uses an **ensemble voting system** that combines all three for final predictions.
</div>
""",
    unsafe_allow_html=True,
)

# --- TECHNOLOGY STACK ---
st.markdown(
    "<div class='section-header'>3. Technology Stack</div>", unsafe_allow_html=True
)
st.markdown(
    """
<div class="highlight">
- **Programming Language:** Python  
- **Libraries:** Scikit-learn, Pandas, NLTK  
- **Visualization:** Plotly, Matplotlib, WordCloud  
- **Deployment:** Streamlit  
- **Dataset Source:** [Fake News Detection Datasets (Kaggle)](https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets)
</div>
""",
    unsafe_allow_html=True,
)

# --- FOOTER ---
st.markdown(
    "<div class='footer-note'>🧩 This section explains the technical foundation behind the Fake News Detection Project.</div>",
    unsafe_allow_html=True,
)
