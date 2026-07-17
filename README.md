# FIAP Threat Model AI - HACKATHON

Projeto desenvolvido para a **5ª fase da Pós Tech em Inteligência Artificial da FIAP**.

O objetivo é automatizar parte do processo de **Modelagem de Ameaças (Threat Modeling)** utilizando **Visão Computacional**, identificando automaticamente componentes em diagramas de arquitetura de software por meio do **YOLOv8**, realizando uma análise baseada no modelo **STRIDE** e gerando um relatório técnico em PDF.

O projeto foi desenvolvido sem a utilização de modelos de linguagem (LLMs), mantendo o foco em **Visão Computacional + regras STRIDE**, conforme o escopo proposto.

---

# Arquitetura da Solução

```text
                +----------------------+
                | Arquitetura (PNG/JPG)|
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
├── config/
├── data/
│   ├── raw/
│   ├── external/
│   └── processed/
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

- Python 3.13
- YOLOv8 (Ultralytics)
- OpenCV
- Pillow
- Streamlit
- Pandas
- NumPy
- FPDF2

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

O modelo foi treinado utilizando um **dataset sintético próprio**, desenvolvido especificamente para este projeto.

O dataset é gerado automaticamente pelo projeto **FIAP Dataset Generator**, sendo composto por diagramas contendo componentes genéricos, AWS e Microsoft Azure.

Estrutura esperada:

```text
data/
└── processed/
    └── dataset_v5/
        ├── images/
        ├── labels/
        ├── drawio/
        ├── preview/
        ├── dataset.yaml
        └── metadata.csv
```

O generator produz automaticamente:

- imagens PNG
- labels YOLO
- arquivos draw.io
- previews
- metadata.csv
- dataset.yaml

---

# Treinamento

O treinamento foi realizado utilizando **Google Colab (GPU Tesla T4 gratuita)**.

O projeto utiliza **fine-tuning**, reaproveitando um modelo previamente treinado para melhorar a detecção de componentes presentes em diagramas reais da AWS e Microsoft Azure.

Após o treinamento, copie:

```text
runs/.../weights/best.pt
```

para:

```text
models/best.pt
```

---

# Executando a Aplicação

```bash
streamlit run app/streamlit_app.py
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

| Classe | Descrição |
|----------|------------------------|
| user | Usuário |
| internet | Internet |
| firewall | Firewall |
| waf | Web Application Firewall |
| load_balancer | Balanceador de Carga |
| api_gateway | API Gateway |
| web_server | Servidor Web |
| application_server | Servidor de Aplicação |
| microservice | Microsserviço |
| database | Banco de Dados |
| cache | Cache |
| queue | Fila de Mensagens |
| object_storage | Armazenamento de Objetos |
| identity_provider | Provedor de Identidade |
| monitoring | Monitoramento |

---

# Funcionalidades

- Upload de diagramas PNG/JPG.
- Detecção automática de componentes utilizando YOLOv8.
- Ajuste do nível de confiança da detecção.
- Geração da imagem anotada.
- Análise de ameaças baseada no modelo STRIDE.
- Geração automática de relatório técnico em PDF.
- Interface Web desenvolvida com Streamlit.

---

# Resultados

Após a evolução do dataset e do processo de fine-tuning, o modelo passou a reconhecer com maior precisão diagramas reais contendo componentes da AWS e Microsoft Azure, mantendo compatibilidade com diagramas genéricos.

A estratégia adotada consistiu em:

- geração automática de datasets sintéticos;
- utilização de ícones oficiais AWS e Azure;
- fine-tuning incremental do YOLOv8;
- validação em diagramas reais.

O modelo final apresentou desempenho consistente na identificação dos componentes utilizados pela aplicação, permitindo a execução completa do pipeline de análise STRIDE.

---

## Referências

Este projeto foi desenvolvido utilizando como base as seguintes referências técnicas e recursos visuais:

- AWS Architecture Diagram Templates (Miro)
  https://miro.com/pt/modelos/diagramas-aws/

- Microsoft Azure Architecture Icons
  https://learn.microsoft.com/en-us/azure/architecture/icons/

- AWS Icons
  https://aws-icons.com/

- Azure Icons
  https://az-icons.com/

## Créditos

Os ícones utilizados para geração do dataset pertencem aos seus respectivos proprietários (Amazon Web Services e Microsoft) e foram utilizados exclusivamente para fins acadêmicos na construção do dataset do projeto.

# Autor

**Keity Pires**

Pós Tech em Inteligência Artificial — FIAP