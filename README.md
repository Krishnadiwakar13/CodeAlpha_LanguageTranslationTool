# 🌐 Language Translation Tool

A simple and user-friendly language translation application built with Python and Streamlit.

The application allows users to enter text, select a source language and target language, and translate the text through a clean web interface using the DeepL API.

---

## ✨ Features

- 🌍 Translate text between multiple languages
- 🔄 Swap source and target languages
- 📝 Simple text input interface
- 🔢 Real-time character counter
- 📋 Copy translated text
- 🧹 Clear input and translation
- ⚡ Fast translation using the DeepL API
- 🛡️ Secure API key handling using environment variables
- ⚠️ Error handling for failed translation requests
- 💻 Simple and responsive Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- DeepL API
- DeepL Python SDK
- python-dotenv

---

## 📁 Project Structure

```text
CodeAlpha_LanguageTranslationTool/
│
├── src/
│   ├── __init__.py
│   └── translator.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Krishnadiwakar13/CodeAlpha_LanguageTranslationTool.git
cd CodeAlpha_LanguageTranslationTool
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```powershell
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the DeepL API Key

Create a `.env` file in the project root:

```env
DEEPL_API_KEY=your_deepl_api_key
```

Replace `your_deepl_api_key` with your actual DeepL API key.

**Important:** Never commit your `.env` file or expose your API key publicly.

The `.env` file is excluded through `.gitignore`.

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧠 How It Works

The application follows a simple translation workflow:

```text
User Input
    │
    ▼
Select Source Language
    │
    ▼
Select Target Language
    │
    ▼
Translation Request
    │
    ▼
DeepL API
    │
    ▼
Translated Text
    │
    ▼
Display Result
```

The main translation logic is handled inside `src/translator.py`, while `app.py` manages the Streamlit user interface.

The application sends the selected text, source language, and target language to DeepL and displays the returned translation.

For language combinations where a direct translation is not available, the translation logic can use English as an intermediate language.

---

## 🌍 Supported Languages

The application interface includes support for multiple commonly used languages, including:

- English
- Hindi
- Spanish
- French
- German
- Italian
- Portuguese
- Russian
- Japanese
- Korean
- Chinese
- Arabic
- Bengali
- Tamil
- Telugu
- Marathi
- Gujarati
- Punjabi

Actual translation availability depends on the languages supported by the configured DeepL API account.

---

## 🧪 Testing

The translation functionality was tested with multiple language combinations, including:

- English → Hindi
- Spanish → English
- Spanish → Hindi

### Example 1

```text
Input:
Hello, how are you?

Output:
नमस्ते, आप कैसे हैं?
```

### Example 2

```text
Input:
Hola, ¿cómo estás?

Output:
Hi, how are you?
```

### Example 3

```text
Input:
Hola, ¿cómo estás?

Output:
नमस्ते, आप कैसे हैं?
```

The application successfully returned HTTP 200 responses for supported translation requests during testing.

---

## 🎯 CodeAlpha Internship Task

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship**.

### Task 1: Language Translation Tool

The project fulfills the required functionality:

- Text input
- Source language selection
- Target language selection
- Translation processing
- Displaying the translated result

Additional usability features were implemented to make the application easier to use, including:

- Language swapping
- Character counting
- Clear functionality
- Copy functionality
- Error handling
- Secure API key configuration

---

## 🔐 Security

The DeepL API key is stored in an environment variable instead of being written directly into the source code.

```env
DEEPL_API_KEY=your_deepl_api_key
```

The `.env` file is excluded from Git using `.gitignore`.

**Never upload or commit your actual API key to GitHub.**

---

## 👨‍💻 Author

**Krishna Diwakar** — AI/ML Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/krishna-diwakar-981367305)

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Krishnadiwakar13)

Built as part of the CodeAlpha AI Internship.

---

## 📄 License

This project was created for educational and internship purposes.
