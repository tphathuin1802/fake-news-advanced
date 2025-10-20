import pickle
import re
import string

import nltk
import streamlit as st
from nltk.corpus import stopwords
from PIL import Image

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Fake News Detector Chatbox", layout="centered")

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
        font-size: 2.5rem;
        font-weight: 700;
        color: #2F4F4F;
        margin-top: 0.5em;
        margin-bottom: 0.5em;
    }

    .chatbox {
        background-color: #f8fafc;
        border: 1px solid #d0d7de;
        border-radius: 12px;
        padding: 1em 1.5em;
        margin-top: 1.2em;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.05);
    }

    .result-box {
        background-color: #f1f5f9;
        border-left: 5px solid #2563eb;
        padding: 1em;
        border-radius: 8px;
        font-size: 1.05rem;
        margin-top: 1.2em;
    }

    .fake {
        background-color: #ffe4e1;
        border-left: 5px solid #dc2626;
    }

    .true {
        background-color: #ecfdf5;
        border-left: 5px solid #16a34a;
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


# --- TẢI STOPWORDS ---
try:
    stop_words_list = stopwords.words("english")
except:
    nltk.download("stopwords")
    stop_words_list = stopwords.words("english")


# --- CACHE MODELS ---
@st.cache_data
def load_components():
    """Load trained models and vectorizer."""
    try:
        with open("./models/vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)
        with open("./models/lr.pkl", "rb") as f:
            lr = pickle.load(f)
        with open("./models/gbc.pkl", "rb") as f:
            gbc = pickle.load(f)
        with open("./models/rfc.pkl", "rb") as f:
            rfc = pickle.load(f)
        return vectorizer, lr, gbc, rfc
    except FileNotFoundError:
        st.error("⚠️ Model files (.pkl) not found.")
        return None, None, None, None


# --- TIỀN XỬ LÝ VĂN BẢN ---
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r"https?://\S+www\.\S+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[%s]" % re.escape(string.punctuation), " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\d", " ", text)
    text = re.sub(r"\n", " ", text)
    text_tokens = text.split()
    text_tokens = [word for word in text_tokens if word not in stop_words_list]
    text = " ".join(text_tokens)
    return re.sub(r"\s+", " ", text).strip()


def output_label(n):
    return "Fake News" if n == 0 else "True News"


# --- DỰ ĐOÁN ---
def manual_predict(news_text, vectorizer, lr, gbc, rfc):
    processed_text = preprocess_text(news_text)
    vectorized_text = vectorizer.transform([processed_text])
    pred_lr = lr.predict(vectorized_text)[0]
    pred_gbc = gbc.predict(vectorized_text)[0]
    pred_rfc = rfc.predict(vectorized_text)[0]
    preds = [pred_lr, pred_gbc, pred_rfc]
    fake_count = preds.count(0)

    details = f"""
    - **Logistic Regression:** {output_label(pred_lr)}  
    - **Gradient Boosting:** {output_label(pred_gbc)}  
    - **Random Forest:** {output_label(pred_rfc)}  
    """

    conclusion = (
        '<div class="result-box fake"><b>📰 Conclusion:</b> This article is likely <b>FAKE NEWS</b> 🚨</div>'
        if fake_count >= 2
        else '<div class="result-box true"><b>📰 Conclusion:</b> This article is likely <b>TRUE NEWS</b> ✅</div>'
    )
    return details + conclusion


# --- UI HIỂN THỊ ---
st.markdown(
    "<div class='main-title'>🧠 Fake News Detector Chatbox</div>",
    unsafe_allow_html=True,
)

# Banner minh họa
try:
    image = Image.open("./assets/image.png")
    st.image(
        image,
        width=400,
        caption="Enter a news article below and let AI analyze its credibility.",
    )
except FileNotFoundError:
    st.warning("⚠️ Could not find './assets/image.png'.")

# Load model components
vectorizer, lr, gbc, rfc = load_components()

# Ô nhập liệu
with st.container():
    st.markdown("<div class='chatbox'>", unsafe_allow_html=True)
    user_input = st.text_area(
        "📝 Paste or type the article text here:",
        height=200,
        placeholder="Type or paste your news content...",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Nút Predict
if st.button("🔍 Analyze"):
    if user_input.strip() == "":
        st.warning("⚠️ Please input an article to analyze.")
    elif vectorizer is not None:
        with st.spinner("Analyzing with AI models..."):
            result_html = manual_predict(user_input, vectorizer, lr, gbc, rfc)
            st.markdown(result_html, unsafe_allow_html=True)

st.markdown(
    "<div class='footer-note'>🤖 Powered by Machine Learning | Built with Streamlit</div>",
    unsafe_allow_html=True,
)
