# FIAP Threat Model AI

MVP para a 5ª fase da Pós Tech em IA da FIAP: identificação de componentes em diagramas de arquitetura de software e geração automática de relatório de Modelagem de Ameaças com STRIDE.

## Pipeline

```text
Imagem de arquitetura
        ↓
Detector YOLOv8
        ↓
Componentes identificados
        ↓
Análise STRIDE
        ↓
Relatório final
```

## Como rodar localmente

### 1. Criar ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```


### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Colocar o dataset

Extraia o dataset YOLO dentro de:

```text
data/processed/
```

O arquivo esperado é:

```text
data/processed/dataset.yaml
```

### 4. Treinar o modelo

```bash
python training/train_yolo.py
```

Ao final, copie:

```text
runs/detect/train/weights/best.pt
```

para:

```text
models/best.pt
```

### 5. Rodar a aplicação

```bash
streamlit run app/streamlit_app.py
```

## Classes

```text
user
internet
identity_provider
gateway
firewall
load_balancer
api
server
database
cache
queue
storage
```
