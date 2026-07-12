from pathlib import Path
import sys
import tempfile
import pandas as pd
import streamlit as st
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.detector.detect import detect_components, save_annotated_image
from src.stride.analyzer import analyze_stride
from src.report.pdf_generator import generate_pdf

st.set_page_config(page_title="FIAP Threat Model AI", layout="wide")
st.title("FIAP Threat Model AI")
st.write("Upload de uma imagem de arquitetura para identificar componentes e gerar relatório STRIDE.")

uploaded_file = st.file_uploader("Envie uma imagem PNG/JPG", type=["png", "jpg", "jpeg"])
confidence = st.slider("Confiança mínima", 0.05, 0.95, 0.25, 0.05)

if uploaded_file:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        image_path = tmp_path / uploaded_file.name
        image_path.write_bytes(uploaded_file.getvalue())

        st.subheader("Imagem enviada")
        st.image(Image.open(image_path), use_container_width=True)

        if st.button("Detectar componentes e gerar STRIDE"):
            try:
                detections = detect_components(image_path, confidence=confidence)
                annotated_path = tmp_path / "annotated.png"
                save_annotated_image(image_path, annotated_path, confidence=confidence)

                st.subheader("Imagem anotada")
                st.image(Image.open(annotated_path), use_container_width=True)

                st.subheader("Componentes detectados")
                st.dataframe(pd.DataFrame(detections), use_container_width=True)

                report = analyze_stride(detections)
                st.subheader("Relatório STRIDE")
                st.dataframe(pd.DataFrame(report), use_container_width=True)

                pdf_path = generate_pdf(report, ROOT / "reports" / "threat_model_report.pdf")
                with open(pdf_path, "rb") as f:
                    st.download_button("Baixar relatório PDF", data=f, file_name="threat_model_report.pdf", mime="application/pdf")

            except FileNotFoundError as error:
                st.error(str(error))
                st.info("Treine o modelo primeiro e copie o arquivo best_v2.pt para models/best_v2.pt.")

            except Exception as error:
                st.error("Ocorreu um erro durante a análise.")
                st.exception(error)