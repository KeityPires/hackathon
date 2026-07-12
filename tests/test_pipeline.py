from pathlib import Path

from src.detector.detect import detect_components
from src.stride.analyzer import analyze_stride
from src.report.pdf_generator import generate_pdf


image_path = Path("tests/assets/arch_0044_test.png")

detections = detect_components(image_path)
report_items = analyze_stride(detections)

pdf_path = generate_pdf(
    report_items=report_items,
    output_path="reports/threat_model_report.pdf"
)

print("=" * 60)
print("PIPELINE EXECUTADO COM SUCESSO")
print("=" * 60)
print(f"Componentes detectados: {len(detections)}")
print(f"Ameaças identificadas: {len(report_items)}")
print(f"Relatório gerado em: {pdf_path}")