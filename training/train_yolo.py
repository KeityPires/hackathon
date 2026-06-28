from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
DATASET_YAML = ROOT / "data" / "processed" / "dataset.yaml"

def main():
    if not DATASET_YAML.exists():
        raise FileNotFoundError(f"Dataset não encontrado em {DATASET_YAML}")

    model = YOLO("yolov8n.pt")
    model.train(
        data=str(DATASET_YAML),
        epochs=50,
        imgsz=640,
        batch=16,
        project=str(ROOT / "runs" / "detect"),
        name="train",
        exist_ok=True,
    )

if __name__ == "__main__":
    main()
