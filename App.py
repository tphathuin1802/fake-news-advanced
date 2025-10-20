import streamlit as st

# --- Cấu hình trang ---
st.set_page_config(page_title="Fake News Detection Project", layout="wide")

# --- CSS: Font + style cho Landing Page ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

    html, body, [class*="st-"], .st-emotion-cache-10trblm, .st-emotion-cache-16txtl3 {
        font-family: 'JetBrains Mono', monospace;
    }

    /* Nền gradient nhẹ */
    .main {
        background: linear-gradient(135deg, #f0f4ff 0%, #e8f0ff 100%);
    }

    /* Căn giữa nội dung */
    .centered {
        text-align: center;
        padding-top: 10vh;
    }

    /* Tiêu đề lớn */
    .title {
        font-size: 3rem;
        font-weight: 700;
        color: #1e40af;
        margin-bottom: 0.5rem;
    }

    /* Mô tả phụ */
    .subtitle {
        font-size: 1.2rem;
        color: #475569;
        margin-bottom: 2rem;
    }

    /* Nút đẹp hơn */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        border-radius: 0.5rem;
        padding: 0.75rem 1.5rem;
        border: none;
        transition: 0.2s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #1d4ed8;
        transform: scale(1.03);
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# --- Nội dung trang Landing Page ---
st.markdown(
    """
    <div class="centered">
        <div class="title">📰 Fake News Detection Project</div>
        <div class="subtitle">
            Welcome! This interactive web app uses Machine Learning to detect whether a news article is <b>True</b> or <b>Fake</b>.<br>
            Explore how AI helps fight misinformation — and test it yourself!
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Nút điều hướng ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Explore Now"):
        st.switch_page("pages/0_Introduction.py")  # đổi đường dẫn nếu trang khác tên
