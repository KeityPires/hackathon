from datetime import datetime
from pathlib import Path

from fpdf import FPDF


def write_text(pdf: FPDF, text: str, height: int = 6):
    pdf.multi_cell(
        0,
        height,
        text,
        new_x="LMARGIN",
        new_y="NEXT",
    )


def generate_pdf(report_items, output_path="reports/threat_model_report.pdf"):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 10, "FIAP Threat Model AI", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 13)
    pdf.cell(
        0,
        8,
        "Relatorio de Modelagem de Ameacas utilizando STRIDE",
        new_x="LMARGIN",
        new_y="NEXT",
    )

    pdf.set_font("Helvetica", "", 10)
    pdf.cell(
        0,
        6,
        f"Data de geracao: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        new_x="LMARGIN",
        new_y="NEXT",
    )

    pdf.ln(8)

    for index, item in enumerate(report_items, start=1):
        pdf.set_font("Helvetica", "B", 13)
        pdf.cell(
            0,
            8,
            f"Ameaca {index}",
            new_x="LMARGIN",
            new_y="NEXT",
        )

        pdf.set_font("Helvetica", "", 11)

        write_text(pdf, f"Componente: {item['component']}")
        write_text(pdf, f"Categoria STRIDE: {item['stride']}")
        write_text(pdf, f"Descricao da ameaca: {item['threat']}")
        write_text(pdf, f"Severidade: {item['severity']}")
        write_text(pdf, "Mitigacoes recomendadas:")

        for mitigation in item["mitigations"]:
            write_text(pdf, f"- {mitigation}")

        pdf.ln(5)

    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(
        0,
        10,
        "Resumo da Analise",
        new_x="LMARGIN",
        new_y="NEXT",
    )

    pdf.set_font("Helvetica", "", 11)

    components = set(item["component"] for item in report_items)

    write_text(pdf, f"Total de ameacas identificadas: {len(report_items)}")
    write_text(pdf, f"Componentes analisados: {len(components)}")
    write_text(pdf, "Modelo de deteccao: YOLOv8")
    write_text(pdf, "Metodologia de analise: STRIDE")

    pdf.output(str(output_path))

    return output_path