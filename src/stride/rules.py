from src.stride.knowledge_base import STRIDE_KNOWLEDGE_BASE
from src.stride.models import Threat


def get_threats_for_component(component: str) -> list[Threat]:
    threats_data = STRIDE_KNOWLEDGE_BASE.get(component, [])

    return [
        Threat(
            category=item["category"],
            title=item["title"],
            description=item["description"],
            mitigation=item["mitigation"],
            severity=item["severity"],
        )
        for item in threats_data
    ]