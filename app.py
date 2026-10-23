import os
from io import BytesIO

import requests
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(
    page_title="Image-Gen",
    page_icon="🐼",
    layout="centered",
)

st.title("Image-Gen 🐼")
st.caption("Turn a text prompt into an image using the OpenAI API.")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error(
        "OpenAI API key not found. Add OPENAI_API_KEY to your local .env file "
        "or configure it in your deployment's secrets."
    )
    st.stop()

client = OpenAI(api_key=api_key)

with st.sidebar:
    st.header("Generation settings")
    prompt = st.text_area(
        "Image prompt",
        placeholder="Describe the image you want to create...",
        help="Be specific about the subject, style, lighting, colours and composition.",
    )
    model = st.selectbox("Model", ("dall-e-3", "dall-e-2"))

    if model == "dall-e-3":
        size = st.selectbox(
            "Image size",
            ("1024x1024", "1024x1792", "1792x1024"),
        )
        quality = st.selectbox("Quality", ("standard", "hd"))
        number = 1
        st.caption("DALL·E 3 generates one image per request.")
    else:
        size = st.selectbox("Image size", ("256x256", "512x512", "1024x1024"))
        quality = "standard"
        number = 1
        st.caption("DALL·E 2 supports square images in these sizes.")

generate = st.button("Generate image", type="primary", use_container_width=True)

if generate:
    if not prompt.strip():
        st.warning("Please enter an image prompt first.")
        st.stop()

    try:
        with st.spinner("Generating your image..."):
            response = client.images.generate(
                model=model,
                prompt=prompt.strip(),
                size=size,
                quality=quality,
                n=number,
            )

            image_url = response.data[0].url
            if not image_url:
                st.error("The API did not return an image URL. Please try again.")
                st.stop()

            image_response = requests.get(image_url, timeout=60)
            image_response.raise_for_status()
            image_bytes = BytesIO(image_response.content).getvalue()

        st.image(image_bytes, caption="Generated image", use_container_width=True)
        st.download_button(
            label="Download image",
            data=image_bytes,
            file_name="generated_image.png",
            mime="image/png",
            use_container_width=True,
        )
        st.success("Image generated successfully.")

    except Exception as exc:
        # Avoid printing secrets or full request details in the UI.
        st.error(f"Image generation failed: {exc}")
        st.info(
            "Check your API key, API billing/credits, model access, prompt, "
            "and the selected image settings, then try again."
        )
