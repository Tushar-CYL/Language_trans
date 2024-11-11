# import streamlit as st
# from googletrans import Translator, LANGUAGES
# from gtts import gTTS
# import base64

# # Initialize translator
# translator = Translator()

# # Function to get binary file download link
# def get_binary_file_downloader_html(bin_file, file_label='File'):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     bin_str = base64.b64encode(data).decode()
#     href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_label}">Download {file_label}</a>'
#     return href

# # Streamlit UI
# st.set_page_config(page_title="Language Translator", layout="wide")

# st.title("🌍 Language Translator")

# # Sidebar for language selection
# st.sidebar.title("Language Settings")
# target_language = st.sidebar.selectbox(
#     "Select Target Language",
#     options=list(LANGUAGES.values()),
#     index=list(LANGUAGES.values()).index('english')
# )

# # Get language code
# target_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]

# # Main content area
# col1, col2 = st.columns([1, 1])

# with col1:
#     input_text = st.text_area(
#         "Enter text to translate",
#         height=200,
#         placeholder="Type or paste your text here..."
#     )

# with col2:
#     if input_text:
#         try:
#             # Translate text
#             translation = translator.translate(
#                 input_text, 
#                 dest=target_lang_code
#             )
#             translated_text = translation.text
            
#             st.text_area(
#                 "Translated Text",
#                 value=translated_text,
#                 height=200
#             )
            
#             # Text-to-speech
#             try:
#                 tts = gTTS(text=translated_text, lang=target_lang_code, slow=False)
#                 tts.save("translation.mp3")
                
#                 audio_file = open('translation.mp3', 'rb')
#                 audio_bytes = audio_file.read()
                
#                 st.audio(audio_bytes, format='audio/mp3')
#                 st.markdown(
#                     get_binary_file_downloader_html("translation.mp3", "Download Audio"),
#                     unsafe_allow_html=True
#                 )
#             except Exception as e:
#                 st.warning(f"Text-to-speech not available for {target_language}")
                
#         except Exception as e:
#             st.error(f"Translation error: {str(e)}")

# # Feature list in sidebar
# st.sidebar.markdown("---")
# st.sidebar.markdown("### Features")
# st.sidebar.markdown("- Supports 100+ languages")
# st.sidebar.markdown("- Text-to-speech capability")
# st.sidebar.markdown("- Download translated audio")


import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS

# Initialize translator
translator = Translator()

# Streamlit UI
st.set_page_config(page_title="Language Translator", layout="wide")

st.title("Language Translator")

# Sidebar for language selection
st.sidebar.title("Language Settings")
target_language = st.sidebar.selectbox(
    "Select Target Language",
    options=list(LANGUAGES.values()),
    index=list(LANGUAGES.values()).index('english')
)

# Get language code
target_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    input_text = st.text_area(
        "Enter text to translate",
        height=100,  # Reduced height
        placeholder="Type or paste your text here..."
    )

with col2:
    if input_text:
        try:
            # Translate text
            translation = translator.translate(
                input_text, 
                dest=target_lang_code
            )
            translated_text = translation.text
            
            st.text_area(
                "Translated Text",
                value=translated_text,
                height=100  # Reduced height
            )
            
            # Text-to-speech with button trigger
            try:
                tts = gTTS(text=translated_text, lang=target_lang_code, slow=False)
                tts.save("translation.mp3")
                
                # Display the Play Audio button with 📀 icon
                if st.button("📀 Play Audio"):
                    audio_file = open('translation.mp3', 'rb')
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/mp3')
                    st.toast("Playing audio 🎧")
                
            except Exception:
                st.toast(f"Audio not available for {target_language}")
                
        except Exception as e:
            st.error(f"Translation error: {str(e)}")

# Feature list in sidebar
