from pathlib import Path
from typing import List, Dict, Any
from ultralytics import YOLO

DEFAULT_MODEL_PATH = Path("models/best.pt")

def load_model(model_path: str | Path = DEFAULT_MODEL_PATH) -> YOLO:
    model_path = Path(model_path)
    if not model_path.exists():
        raise FileNotFoundError(
            f"Modelo não encontrado em {model_path}. Treine o YOLO e copie best.pt para models/."
        )
    return YOLO(str(model_path))

def detect_components(image_path: str | Path, model_path: str | Path = DEFAULT_MODEL_PATH, confidence: float = 0.25) -> List[Dict[str, Any]]:
    model = load_model(model_path)
    results = model(str(image_path), conf=confidence)
    detections = []
    result = results[0]
    names = result.names

    for box in result.boxes:
        cls_id = int(box.cls[0].item())
        conf = float(box.conf[0].item())
        x1, y1, x2, y2 = [float(v) for v in box.xyxy[0].tolist()]
        detections.append({
            "component": names[cls_id],
            "confidence": round(conf, 4),
            "bbox": [round(x1, 2), round(y1, 2), round(x2, 2), round(y2, 2)]
        })
    return detections

def save_annotated_image(image_path: str | Path, output_path: str | Path, model_path: str | Path = DEFAULT_MODEL_PATH, confidence: float = 0.25) -> Path:
    import cv2
    model = load_model(model_path)
    results = model(str(image_path), conf=confidence)
    annotated = results[0].plot()
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(output_path), annotated)
    return output_path
