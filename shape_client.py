# Gradio frontend
import gradio as gr
import requests
import io

def classify_with_backend(image):
    url = "http://127.0.0.1:8000/classify"
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG") # Png format으로 저장 
    image_bytes = image_bytes.getvalue() # value값을 가져옴
    response = requests.post(url, files={"file": ("image.png", image_bytes, "image/png")})	# url에 접속
    if response.status_code == 200:
        return response.json().get("label", "Error")
    else:
        return "Error"

iface = gr.Interface(
    fn=classify_with_backend,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="손글씨 도형 분류하기",
    description="○, X, △ 이미지를 넣어주세요 !!"
)

if __name__ == "__main__":
    iface.launch()