from src.stride.analyzer import analyze_stride

def test_analyze_stride_database():
    detections = [{"component": "database", "confidence": 0.9, "bbox": [0, 0, 10, 10]}]
    report = analyze_stride(detections)
    assert len(report) > 0
    assert any(item["component"] == "database" for item in report)
