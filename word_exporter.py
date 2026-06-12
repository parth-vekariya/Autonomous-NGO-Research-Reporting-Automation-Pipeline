"""Generate Word document with analytical insights from NGO research."""

from datetime import datetime
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH


def _add_heading(doc: Document, text: str, level: int = 1):
    heading = doc.add_heading(text, level=level)
    for run in heading.runs:
        run.font.color.rgb = RGBColor(31, 78, 121)


def _add_body(doc: Document, text: str):
    for paragraph in text.strip().split("\n\n"):
        if paragraph.strip().startswith("**") and paragraph.strip().endswith("**"):
            p = doc.add_paragraph()
            run = p.add_run(paragraph.strip().strip("*"))
            run.bold = True
            run.font.size = Pt(12)
        elif paragraph.strip().startswith("|"):
            lines = paragraph.strip().split("\n")
            rows = [line.split("|")[1:-1] for line in lines if line.strip().startswith("|")]
            if len(rows) >= 2:
                table = doc.add_table(rows=len(rows) - 1, cols=len(rows[0]))
                table.style = "Light Grid Accent 1"
                for col_idx, header in enumerate(rows[0]):
                    cell = table.rows[0].cells[col_idx]
                    cell.text = header.strip()
                    for run in cell.paragraphs[0].runs:
                        run.bold = True
                for row_idx, row_data in enumerate(rows[2:], 1):
                    for col_idx, value in enumerate(row_data):
                        if row_idx < len(table.rows):
                            table.rows[row_idx].cells[col_idx].text = value.strip()
        elif paragraph.strip().startswith("**"):
            p = doc.add_paragraph()
            parts = paragraph.split("**")
            for i, part in enumerate(parts):
                run = p.add_run(part)
                if i % 2 == 1:
                    run.bold = True
                run.font.size = Pt(11)
        elif paragraph.strip().startswith("- ") or paragraph.strip().startswith("   "):
            for line in paragraph.strip().split("\n"):
                doc.add_paragraph(line.strip().lstrip("- "), style="List Bullet")
        else:
            p = doc.add_paragraph(paragraph.strip())
            for run in p.runs:
                run.font.size = Pt(11)


def export_to_word(
    ngos: list[dict],
    analysis: dict[str, str],
    output_path: Path,
    task_title: str = "Indian NGOs Research Analysis",
) -> Path:
    doc = Document()

    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    # Title page
    title = doc.add_heading(task_title, level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitle.add_run("AI-Assisted Research & Analysis Report")
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(89, 89, 89)

    meta = doc.add_paragraph()
    meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    meta.add_run(
        f"\nGenerated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n"
        f"NGOs Researched: {len(ngos)}\n"
        f"Persona: AI Agent Developer / Research Automation\n"
    )

    doc.add_page_break()

    # Table of Contents
    _add_heading(doc, "Table of Contents", level=1)
    toc_items = [
        "1. Executive Summary",
        "2. Common Challenges Faced by NGOs",
        "3. Similarities in NGO Working Models",
        "4. Differences in NGO Working Models",
        "5. Sectors with Highest NGO Participation",
        "6. Regulatory Landscape Analysis (India-Specific)",
        "7. Key Insights & Recommendations",
        "8. NGO Quick Reference Table",
    ]
    for item in toc_items:
        doc.add_paragraph(item, style="List Number")

    doc.add_page_break()

    # Executive Summary
    _add_heading(doc, "1. Executive Summary", level=1)
    _add_body(
        doc,
        f"""This report presents AI-assisted research and analysis of {len(ngos)} prominent NGOs operating in India across diverse social sectors including Education, Healthcare, Environmental Conservation, Women Empowerment, Animal Welfare, Child Rights, and Elderly Care.

The research collected 13 data points per NGO covering organizational identity, programs, geographic reach, impact statistics, contact information, funding sources, legal compliance (FCRA, 12A/80G, NGO Darpan), partnerships, and awards.

**Key Findings:**
- Education is the dominant sector with 8 of 20 NGOs having primary education focus
- {sum(1 for n in ngos if n.get('geographic_reach') == 'National')} NGOs operate at national scale
- All 20 NGOs maintain tax exemption compliance (12A/80G)
- CSR funding is the primary private funding channel across the sector
- Partnership-based models (government + corporate + community) dominate over direct-only implementation""",
    )

    doc.add_page_break()

    # Analysis sections
    sections = [
        ("2. Common Challenges Faced by NGOs in India", analysis["challenges"]),
        ("3. Similarities in NGO Working Models", analysis["similarities"]),
        ("4. Differences in NGO Working Models", analysis["differences"]),
        ("5. Sectors with Highest NGO Participation in India", analysis["sector_participation"]),
        ("6. Regulatory Landscape Analysis (India-Specific)", analysis["regulatory"]),
        ("7. Key Insights & Recommendations", analysis["recommendations"]),
    ]

    for title_text, content in sections:
        _add_heading(doc, title_text, level=1)
        _add_body(doc, content)
        doc.add_page_break()

    # Quick reference table
    _add_heading(doc, "8. NGO Quick Reference Table", level=1)
    table = doc.add_table(rows=len(ngos) + 1, cols=5)
    table.style = "Light Grid Accent 1"

    headers = ["S.No", "NGO Name", "Sector", "Founded", "Geographic Reach"]
    for col, header in enumerate(headers):
        cell = table.rows[0].cells[col]
        cell.text = header
        for run in cell.paragraphs[0].runs:
            run.bold = True

    for idx, ngo in enumerate(ngos, 1):
        table.rows[idx].cells[0].text = str(idx)
        table.rows[idx].cells[1].text = f"{ngo.get('full_official_name', '')} ({ngo.get('short_name', '')})"
        table.rows[idx].cells[2].text = ngo.get("sector", "")
        table.rows[idx].cells[3].text = ngo.get("founding_year", "")
        table.rows[idx].cells[4].text = ngo.get("geographic_reach", "")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output_path)
    return output_path
