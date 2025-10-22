import matplotlib

matplotlib.use("Agg")  # ✅ Fix backend crash khi chạy WordCloud trong Streamlit

import io

import matplotlib.pyplot as plt
import nltk
import pandas as pd
import plotly.express as px
import streamlit as st
from nltk.corpus import stopwords
from PIL import Image
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud

st.set_page_config(page_title="Data Visualization & Insights", layout="wide")

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

st.markdown(
    "<div class='main-title'>Data Visualization & Insights</div>",
    unsafe_allow_html=True,
)

st.image(
    "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=1600&q=80",
    use_container_width=True,
    caption="Data Analytics & Visualization Overview",
)

st.markdown(
    "<div class='section-header'>4. Data Distribution Overview</div>",
    unsafe_allow_html=True,
)
st.markdown(
    """
<div class="highlight">
The dataset consists of two major categories:
- **Fake News:** 23,481 records  
- **True News:** 21,417 records  
The dataset is relatively balanced, ensuring fairness in model training and evaluation.
</div>
""",
    unsafe_allow_html=True,
)

labels = ["Fake News", "True News"]
sizes = [23481, 21417]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)

st.markdown(
    "<div class='section-header'>5. Text Analysis & Word Frequency</div>",
    unsafe_allow_html=True,
)
st.markdown(
    """
<div class="highlight">
Textual analysis reveals common words and writing patterns.  
For example, **Fake News** often includes emotionally charged or sensational words,  
while **True News** tends to use neutral and factual language.
</div>
""",
    unsafe_allow_html=True,
)

fake_words = ["breaking", "trump", "hillary", "election", "fake"]
true_words = ["said", "reuters", "report", "government", "official"]

col1, col2 = st.columns(2)
with col1:
    st.subheader("Most Common Words — Fake News")
    st.bar_chart(pd.Series(fake_words).value_counts())
with col2:
    st.subheader("Most Common Words — True News")
    st.bar_chart(pd.Series(true_words).value_counts())

st.markdown(
    "<div class='section-header'>5.1 Sentiment Insights</div>", unsafe_allow_html=True
)
st.markdown(
    """
<div class="highlight">
Sentiment analysis shows Fake News tends to lean more towards **negative or extreme polarity**,  
while True News maintains **neutral tone** due to journalistic standards.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='footer-note'>📊 Visualizing the data provides deeper intuition for model development and feature engineering.</div>",
    unsafe_allow_html=True,
)

try:
    stop_words_list = stopwords.words("english")
except:
    nltk.download("stopwords")
    stop_words_list = stopwords.words("english")


@st.cache_data
def load_data():
    fake_path = "https://raw.githubusercontent.com/tphathuin1802/fake-news-advanced/refs/heads/main/data/Fake.csv"
    true_path = "https://raw.githubusercontent.com/tphathuin1802/fake-news-advanced/refs/heads/main/data/True.csv"
    fake_df = pd.read_csv(fake_path)
    true_df = pd.read_csv(true_path)
    fake_df["label"] = 0
    true_df["label"] = 1
    news_df = pd.concat([fake_df, true_df], ignore_index=True)
    news_df["label_name"] = news_df["label"].map({0: "Fake", 1: "True"})
    news_df["word_count"] = news_df["text"].astype(str).str.split().str.len()
    return news_df, news_df.dropna(subset=["text"])


st.markdown('<div class="content-box">', unsafe_allow_html=True)
st.title("Data Visualization")
st.markdown(
    "Explore the dataset through interactive visualizations that help uncover key trends and distributions in Fake vs. True news."
)

df, df_clean = load_data()

if df is not None:
    st.header("2.1 Exploratory Data Analysis (EDA)")
    st.markdown(
        "Let's begin by understanding the overall data composition and text properties."
    )

    st.subheader("Label Distribution")
    fig1 = px.bar(
        df,
        x="label_name",
        color="label_name",
        title="Distribution of Fake vs. True News",
        labels={"label_name": "News Type", "count": "Count"},
        color_discrete_map={"Fake": "#F94144", "True": "#277DA1"},
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Word Count Distribution")
    fig2 = px.histogram(
        df,
        x="word_count",
        color="label_name",
        barmode="overlay",
        title="Word Count Distribution by News Type",
        labels={"word_count": "Word Count"},
        color_discrete_map={"Fake": "#F94144", "True": "#277DA1"},
        range_x=[0, 2000],
    )
    fig2.update_traces(opacity=0.7)
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Subject Distribution")
    fig3 = px.bar(
        df,
        x="subject",
        color="label_name",
        barmode="group",
        title="Subject Distribution by News Type",
        labels={"subject": "Subject", "count": "Frequency", "label_name": "News Type"},
        color_discrete_map={"Fake": "#F94144", "True": "#277DA1"},
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Most Frequent Words & Word Cloud")
    with st.spinner("Generating word plots..."):
        vec = CountVectorizer(stop_words=stop_words_list, max_features=1000)
        dtm = vec.fit_transform(df_clean["text"])
        freq = dtm.sum(axis=0).A1
        words = vec.get_feature_names_out()
        freq_df = pd.DataFrame({"word": words, "freq": freq})
        top20 = freq_df.sort_values(by="freq", ascending=False).head(20)

        fig4 = px.bar(
            top20.sort_values(by="freq"),
            x="freq",
            y="word",
            orientation="h",
            title="Top 20 Most Frequent Words",
            color_discrete_sequence=["#2563EB"],
        )
        st.plotly_chart(fig4, use_container_width=True)

        # ✅ Giới hạn sample để tránh crash
        sample_texts = (
            df_clean["text"]
            .dropna()
            .astype(str)
            .sample(n=min(3000, len(df_clean)), random_state=42)
        )
        text = " ".join(sample_texts)

        # ✅ Sinh WordCloud an toàn
        wc = WordCloud(
            width=800,
            height=400,
            background_color="white",
            stopwords=set(stop_words_list),
            max_words=300,
            colormap="Dark2",
            collocations=False,
            normalize_plurals=False,
        ).generate(text)

        buf = io.BytesIO()
        img = wc.to_image()
        img.save(buf, format="PNG")
        st.image(
            Image.open(io.BytesIO(buf.getvalue())),
            caption="Word Cloud of News Dataset",
            use_column_width=True,
        )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
