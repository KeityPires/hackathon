from src.stride.analyzer import analyze_stride


detections = [
    {
        "component": "api_gateway",
        "confidence": 0.998,
        "bbox": {"x1": 100, "y1": 50, "x2": 180, "y2": 120},
    },
    {
        "component": "database",
        "confidence": 0.997,
        "bbox": {"x1": 300, "y1": 200, "x2": 390, "y2": 290},
    },
    {
        "component": "identity_provider",
        "confidence": 0.992,
        "bbox": {"x1": 500, "y1": 80, "x2": 590, "y2": 160},
    },
]


report = analyze_stride(detections)

print("=" * 60)
print("RELATÓRIO STRIDE")
print("=" * 60)

for item in report:
    print(f"\nComponente: {item['component']}")
    print(f"Categoria STRIDE: {item['stride']}")
    print(f"Ameaça: {item['threat']}")
    print(f"Severidade: {item['severity']}")
    print("Mitigações:")
    for mitigation in item["mitigations"]:
        print(f"- {mitigation}")

print("\nTotal de ameaças identificadas:", len(report))