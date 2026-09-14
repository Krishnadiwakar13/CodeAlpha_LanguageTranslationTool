import streamlit as st

from src.translator import translate_text


# Supported languages
LANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Italian": "it",
    "Portuguese": "pt",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh",
    "Russian": "ru",
    "Arabic": "ar",
}

LANGUAGE_NAMES = list(LANGUAGES.keys())


# Page configuration
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐",
    layout="centered",
)


# Session state
if "source_language" not in st.session_state:
    st.session_state.source_language = "English"

if "target_language" not in st.session_state:
    st.session_state.target_language = "Hindi"

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""


# Functions
def swap_languages():
    source = st.session_state.source_language
    target = st.session_state.target_language

    st.session_state.source_language = target
    st.session_state.target_language = source


def clear_all():
    st.session_state.input_text = ""
    st.session_state.translated_text = ""


# Title
st.title("🌐 Language Translation Tool")

st.write(
    "Translate text between multiple languages using the DeepL API."
)


# Language selection
source_col, swap_col, target_col = st.columns([5, 1, 5])

with source_col:
    st.selectbox(
        "From",
        options=LANGUAGE_NAMES,
        key="source_language",
    )

with swap_col:
    st.write("")
    st.button(
        "↔",
        on_click=swap_languages,
        use_container_width=True,
    )

with target_col:
    st.selectbox(
        "To",
        options=LANGUAGE_NAMES,
        key="target_language",
    )


# Input section
st.subheader("Enter Text")

st.text_area(
    "Text to translate",
    height=180,
    placeholder="Type or paste your text here...",
    key="input_text",
    label_visibility="collapsed",
)

st.caption(
    f"Characters: {len(st.session_state.input_text)}"
)


# Action buttons
translate_col, clear_col = st.columns(2)

with translate_col:
    translate_button = st.button(
        "🌐 Translate",
        use_container_width=True,
    )

with clear_col:
    st.button(
        "🗑️ Clear",
        on_click=clear_all,
        use_container_width=True,
    )


# Translation
if translate_button:

    text = st.session_state.input_text
    source = st.session_state.source_language
    target = st.session_state.target_language

    if not text.strip():
        st.warning("Please enter some text to translate.")

    elif source == target:
        st.info("Source and target languages are the same.")

    else:
        try:
            with st.spinner("Translating..."):

                result = translate_text(
                    text,
                    LANGUAGES[source],
                    LANGUAGES[target],
                )

            st.session_state.translated_text = result

        except Exception as error:
            st.error(
                "Unable to translate the text right now. "
                "Please check your API key and internet connection."
            )


# Translation output
if st.session_state.translated_text:

    st.subheader("Translation")

    st.code(
        st.session_state.translated_text,
        language=None,
    )


# Footer
st.divider()

st.caption("Built by Krishna Diwakar")
