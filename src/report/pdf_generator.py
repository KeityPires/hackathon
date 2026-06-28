from pathlib import Path
from fpdf import FPDF

def generate_pdf(report_items, output_path="reports/threat_model_report.pdf"):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Relatorio de Modelagem de Ameacas - STRIDE", ln=True)
    pdf.ln(5)

    for item in report_items:
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, f"Componente: {item['component']}", ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 6, f"Categoria STRIDE: {item['stride']}")
        pdf.multi_cell(0, 6, f"Ameaca: {item['threat']}")
        pdf.multi_cell(0, 6, f"Severidade: {item['severity']}")
        pdf.multi_cell(0, 6, "Contramedidas: " + ", ".join(item["mitigations"]))
        pdf.ln(4)

    pdf.output(str(output_path))
    return output_path
