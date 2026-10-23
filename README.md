# Image-Gen 🐼

A simple Streamlit web app that turns text prompts into images using the OpenAI Images API. Choose an image model and supported size, generate an image, and download the result.

## Features

- Simple Streamlit interface
- Text-to-image generation through OpenAI
- Model-specific image-size and quality options
- Image preview and PNG download
- Environment-variable configuration for API credentials
- Basic input validation and error handling

## Requirements

- Python 3.10 or newer
- An OpenAI API key with access to the selected image model
- API billing/credits configured for your OpenAI account, where required

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/geeranlone/image-gen.git
cd image-gen
```


### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure your API key

Copy `.env.example` to `.env` and replace the placeholder with your own key.

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

macOS / Linux:

```bash
cp .env.example .env
```

Edit `.env`:

```env
OPENAI_API_KEY=your_real_api_key_here
```

**Never commit `.env` or share your API key.** The repository's `.gitignore` excludes `.env`.

### 5. Start the app

```bash
streamlit run app.py
```

Streamlit will print a local URL, usually `http://localhost:8501`.

## GitHub upload

Create a new, empty repository on GitHub named `image-gen`. Do not add a README or license on GitHub if you already have these files locally. Then run these commands from the project folder:

```bash
git init
git add .
git status
git commit -m "Build Streamlit OpenAI image generator"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/image-gen.git
git push -u origin main
```

Replace the remote URL with your actual repository URL. Before committing, inspect `git status` and confirm `.env` is not listed.

If Git says the remote `origin` already exists, update it with:

```bash
git remote set-url origin https://github.com/geeranlone/image-gen.git
```

## Deploy with Streamlit Community Cloud

1. Push the project to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/) and connect your GitHub account.
3. Create an app and select your repository, branch (`main`) and main file (`app.py`).
4. In the app's **Settings → Secrets**, add:

```toml
OPENAI_API_KEY = "use urs"
```

5. Deploy the app. Do not put your API key in source code or in a committed `.env` file.

Availability, model access, and API pricing are controlled by OpenAI and may change. Check the current OpenAI documentation if a model or setting is rejected.

## Project structure

```text
image-gen/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## Troubleshooting

- **API key missing:** check that `.env` exists locally and contains `OPENAI_API_KEY=...`, or configure Streamlit secrets when deployed.
- **Authentication or quota error:** verify the key, account access, billing and usage limits.
- **Model or image-size error:** confirm the chosen model supports the selected size and quality in the current API documentation.
- **Dependency/import error:** activate your virtual environment and run `pip install -r requirements.txt`.

## Disclaimer

This is a learning/demo project. Generated images and API usage may incur charges. Review OpenAI's current terms, image policies and pricing before use.
