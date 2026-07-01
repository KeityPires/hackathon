import json
from pathlib import Path
from typing import List, Dict, Any

KB_PATH = Path(__file__).resolve().parent / "knowledge_base.json"


def load_knowledge_base(path: str | Path = KB_PATH) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def infer_severity(component: str, stride_category: str) -> str:
    high_risk_components = {"database", "api_gateway", "gateway", "identity_provider"}
    high_risk_categories = {
        "Information Disclosure",
        "Elevation of Privilege",
        "Spoofing",
    }

    if component in high_risk_components and stride_category in high_risk_categories:
        return "Alta"

    if component in high_risk_components:
        return "Média"

    return "Baixa"


def analyze_stride(detections: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    kb = load_knowledge_base()

    components = sorted(
        set(item.get("component") for item in detections if item.get("component"))
    )

    report = []

    for component in components:
        item = kb.get(component)

        if not item:
            continue

        mitigations = item.get("mitigations", [])

        for stride_category, threats in item.items():
            if stride_category == "mitigations":
                continue

            for threat in threats:
                report.append({
                    "component": component,
                    "stride": stride_category,
                    "threat": threat,
                    "severity": infer_severity(component, stride_category),
                    "mitigations": mitigations,
                })

    return report