from pathlib import Path
from collections import Counter

DATASET = Path("data/processed/dataset_v4")

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}

NUM_CLASSES = 15


def validate_split(split: str, counter: Counter):
    images_dir = DATASET / "images" / split
    labels_dir = DATASET / "labels" / split

    images = {
        f.stem
        for f in images_dir.iterdir()
        if f.suffix.lower() in IMAGE_EXTENSIONS
    }

    labels = {
        f.stem
        for f in labels_dir.glob("*.txt")
    }

    print(f"\n=== {split.upper()} ===")
    print(f"Imagens: {len(images)}")
    print(f"Labels : {len(labels)}")

    missing_labels = images - labels
    missing_images = labels - images

    if missing_labels:
        print(f"❌ {len(missing_labels)} imagens sem label")

    if missing_images:
        print(f"❌ {len(missing_images)} labels sem imagem")

    for label_file in labels_dir.glob("*.txt"):
        with open(label_file, encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):

                values = line.strip().split()

                if len(values) != 5:
                    print(f"Formato inválido: {label_file.name}:{line_number}")
                    continue

                cls = int(values[0])

                if cls < 0 or cls >= NUM_CLASSES:
                    print(f"Classe inválida: {label_file.name}:{line_number}")
                    continue

                counter[cls] += 1

                for value in values[1:]:
                    v = float(value)

                    if not 0 <= v <= 1:
                        print(
                            f"Valor fora do intervalo [0,1]: "
                            f"{label_file.name}:{line_number}"
                        )


def main():

    counter = Counter()

    validate_split("train", counter)
    validate_split("val", counter)

    print("\n==============================")
    print("Distribuição das classes")
    print("==============================")

    classes = [
        "user",
        "internet",
        "firewall",
        "waf",
        "load_balancer",
        "api_gateway",
        "web_server",
        "application_server",
        "microservice",
        "database",
        "cache",
        "queue",
        "object_storage",
        "identity_provider",
        "monitoring",
    ]

    total = 0

    for i, name in enumerate(classes):
        qtd = counter[i]
        total += qtd
        print(f"{name:<22} {qtd}")

    print("\n------------------------------")
    print(f"Total de objetos: {total}")
    print("------------------------------")


if __name__ == "__main__":
    main()