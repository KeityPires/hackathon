from pathlib import Path

from src.detector.detect import (
    detect_components,
    save_annotated_image,
)

image = Path("tests/assets/arch_0044_test.png")

detections = detect_components(image)

print("=" * 50)
print("COMPONENTES DETECTADOS")
print("=" * 50)

for detection in detections:
    print(detection)

save_annotated_image(
    image_path=image,
    output_path="reports/deteccao_teste_2.png"
)

print("\nImagem anotada salva em reports/deteccao_teste_2.png")