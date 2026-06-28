# FIAP Threat Model AI - HACKATHON

Projeto desenvolvido para a **5ª fase da Pós Tech em Inteligência Artificial da FIAP**.

O objetivo é automatizar parte do processo de **Modelagem de Ameaças (Threat Modeling)** utilizando **Visão Computacional** e **Inteligência Artificial**, identificando componentes em diagramas de arquitetura de software e gerando uma análise baseada no modelo **STRIDE**.

---

# Arquitetura da Solução

```text
                +----------------------+
                | Arquitetura (PNG)    |
                +----------+-----------+
                           |
                           v
                 +------------------+
                 | YOLOv8 Detector  |
                 +------------------+
                           |
                           v
            Componentes Detectados (JSON)
                           |
                           v
                 +------------------+
                 | STRIDE Engine    |
                 +------------------+
                           |
                           v
              Relatório de Ameaças
                           |
                           v
                     PDF / Streamlit
```

---

# Estrutura do Projeto

```text
fiap-threat-model-ai/
│
├── app/                 # Interface Streamlit
├── config/              # Configurações
├── data/
│   ├── raw/
│   ├── external/
│   └── processed/
│       └── dataset_v3/
├── docs/
├── models/
├── notebooks/
├── reports/
├── src/
│   ├── detector/
│   ├── report/
│   ├── stride/
│   └── utils/
├── tests/
├── training/
├── tools/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Tecnologias Utilizadas

* Python 3.13
* YOLOv8 (Ultralytics)
* OpenCV
* Pillow
* Streamlit
* Pandas
* NumPy
* FPDF2

---

# Como Executar

## 1. Clone o repositório

```bash
git clone https://github.com/KeityPires/hackathon.git
cd hackathon
```

---

## 2. Crie um ambiente virtual

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Windows (CMD)

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# Dataset

O projeto utiliza um dataset sintético gerado especificamente para este trabalho.

A estrutura esperada é:

```text
data/
└── processed/
    └── dataset_v3/
        ├── images/
        ├── labels/
        ├── drawio/
        ├── preview/
        ├── dataset.yaml
        └── metadata.csv
```

O dataset é gerado pelo projeto **FIAP Dataset Generator**.

---

# Treinamento

Execute:

```bash
python training/train_yolo.py
```

Após o treinamento, copie o modelo:

```text
runs/detect/train/weights/best.pt
```

para:

```text
models/best.pt
```

---

# Executando a Aplicação

```bash
python -m streamlit run app/streamlit_app.py
```

---

# Pipeline

```text
Imagem de Arquitetura

        │

        ▼

YOLOv8

        │

        ▼

Componentes Detectados

        │

        ▼

Análise STRIDE

        │

        ▼

Relatório de Ameaças

        │

        ▼

PDF + Interface Streamlit
```

---

# Classes Detectadas

| Classe             | Descrição                |
| ------------------ | ------------------------ |
| user               | Usuário                  |
| internet           | Internet                 |
| firewall           | Firewall                 |
| waf                | Web Application Firewall |
| load_balancer      | Balanceador de Carga     |
| api_gateway        | API Gateway              |
| web_server         | Servidor Web             |
| application_server | Servidor de Aplicação    |
| microservice       | Microsserviço            |
| database           | Banco de Dados           |
| cache              | Cache                    |
| queue              | Fila de Mensagens        |
| object_storage     | Armazenamento de Objetos |
| identity_provider  | Provedor de Identidade   |
| monitoring         | Monitoramento            |

---

# Próximas Etapas

* Treinar o modelo YOLOv8 utilizando o dataset sintético.
* Melhorar a precisão da detecção de componentes.
* Integrar IA Generativa para enriquecer a análise STRIDE.
* Gerar relatórios técnicos em PDF.
* Publicar a aplicação utilizando Streamlit.

---

# Autor

**Keity Pires**

Pós Tech em Inteligência Artificial — FIAP
