from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    ListFlowable,
    ListItem,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
)
from reportlab.platypus.tableofcontents import TableOfContents


ROOT = Path(__file__).resolve().parents[1]
GUIDE_DIR = ROOT / "interview-guide"
OUT_DIR = ROOT / "dist"
OUT_FILE = OUT_DIR / "senior-android-kotlin-interview-guide.pdf"

STUDY_FILES = [
    ("Study Guide", GUIDE_DIR / "STUDY-GUIDE.md"),
    ("Question Coverage", GUIDE_DIR / "QUESTION-COVERAGE.md"),
    ("Question Bank", GUIDE_DIR / "QUESTION-BANK.md"),
    ("Mock Interviews", GUIDE_DIR / "MOCK-INTERVIEWS.md"),
    ("Flashcards", GUIDE_DIR / "FLASHCARDS.md"),
    ("References", GUIDE_DIR / "references.md"),
]


class IndexedDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="normal",
        )
        self.addPageTemplates(
            [
                PageTemplate(id="main", frames=[frame], onPage=self._draw_page),
            ]
        )

    def _draw_page(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#666666"))
        page = canvas.getPageNumber()
        footer = f"Senior Android / Kotlin Interview Guide    |    Page {page}"
        canvas.drawCentredString(letter[0] / 2, 0.45 * inch, footer)
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and getattr(flowable, "_bookmark_name", None):
            text = flowable.getPlainText()
            key = flowable._bookmark_name
            level = flowable._outline_level
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, level=level, closed=level > 0)
            self.notify("TOCEntry", (level, text, self.page, key))


def make_styles():
    base = getSampleStyleSheet()
    styles = {
        "Title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=26,
            leading=32,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#111111"),
            spaceAfter=18,
        ),
        "Subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontSize=12,
            leading=18,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#555555"),
            spaceAfter=10,
        ),
        "H1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=19,
            leading=24,
            textColor=colors.HexColor("#111111"),
            spaceBefore=16,
            spaceAfter=8,
            keepWithNext=True,
        ),
        "H2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=20,
            textColor=colors.HexColor("#222222"),
            spaceBefore=12,
            spaceAfter=6,
            keepWithNext=True,
        ),
        "H3": ParagraphStyle(
            "H3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=12.5,
            leading=16,
            textColor=colors.HexColor("#333333"),
            spaceBefore=9,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "Body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=14,
            alignment=TA_LEFT,
            spaceAfter=5,
        ),
        "Label": ParagraphStyle(
            "Label",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=14,
            textColor=colors.HexColor("#222222"),
            spaceBefore=8,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "Small": ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=12,
            textColor=colors.HexColor("#555555"),
            spaceAfter=4,
        ),
        "Quote": ParagraphStyle(
            "Quote",
            parent=base["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=13,
            leftIndent=18,
            rightIndent=18,
            textColor=colors.HexColor("#333333"),
            borderColor=colors.HexColor("#dddddd"),
            borderWidth=1,
            borderPadding=6,
            spaceBefore=4,
            spaceAfter=7,
        ),
        "Code": ParagraphStyle(
            "Code",
            parent=base["Code"],
            fontName="Courier",
            fontSize=7.8,
            leading=10,
            leftIndent=8,
            rightIndent=8,
            backColor=colors.HexColor("#f4f4f4"),
            borderPadding=6,
            spaceBefore=4,
            spaceAfter=6,
        ),
        "Bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=13,
            leftIndent=14,
            firstLineIndent=0,
            spaceAfter=2,
        ),
    }
    return styles


def inline_markup(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier" backColor="#eeeeee">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)

    def repl_link(match):
        label = match.group(1)
        url = match.group(2)
        return f'<font color="#1a5fb4">{label}</font> <font color="#666666">({url})</font>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl_link, text)
    return text


def add_heading(story, text: str, level: int, styles, counter: list[int]):
    style_name = {0: "H1", 1: "H2", 2: "H3"}.get(level, "H3")
    p = Paragraph(inline_markup(text), styles[style_name])
    key = f"heading-{counter[0]}"
    counter[0] += 1
    p._bookmark_name = key
    p._outline_level = level
    story.append(p)


def flush_paragraph(story, parts: list[str], styles):
    if not parts:
        return
    text = " ".join(part.strip() for part in parts if part.strip()).strip()
    parts.clear()
    if text:
        story.append(Paragraph(inline_markup(text), styles["Body"]))


def flush_bullets(story, bullets: list[str], styles):
    if not bullets:
        return
    items = [
        ListItem(Paragraph(inline_markup(item), styles["Bullet"]), leftIndent=8)
        for item in bullets
    ]
    story.append(
        ListFlowable(
            items,
            bulletType="bullet",
            leftIndent=18,
            bulletFontName="Helvetica",
            bulletFontSize=8,
            bulletColor=colors.HexColor("#333333"),
        )
    )
    bullets.clear()


def parse_markdown(path: Path, section_title: str, styles, heading_counter: list[int]):
    story = []
    add_heading(story, section_title, 0, styles, heading_counter)

    in_code = False
    code_lines: list[str] = []
    paragraph: list[str] = []
    bullets: list[str] = []

    raw_lines = path.read_text(encoding="utf-8").splitlines()
    if path.name == "FLASHCARDS.md":
        merged = []
        i = 0
        while i < len(raw_lines):
            current = raw_lines[i]
            nxt = raw_lines[i + 1] if i + 1 < len(raw_lines) else ""
            if re.match(r"^\d+\.\s+\*\*Q:\*\*", current) and re.match(
                r"^\s+\*\*A:\*\*", nxt
            ):
                merged.append(current.rstrip().rstrip("  ") + " — " + nxt.strip())
                i += 2
            else:
                merged.append(current)
                i += 1
        raw_lines = merged

    for raw_line in raw_lines:
        line = raw_line.rstrip()

        if line.startswith("```"):
            if in_code:
                story.append(Preformatted("\n".join(code_lines), styles["Code"]))
                code_lines.clear()
                in_code = False
            else:
                flush_paragraph(story, paragraph, styles)
                flush_bullets(story, bullets, styles)
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not line.strip():
            flush_paragraph(story, paragraph, styles)
            flush_bullets(story, bullets, styles)
            continue

        heading_match = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading_match:
            flush_paragraph(story, paragraph, styles)
            flush_bullets(story, bullets, styles)
            hashes, title = heading_match.groups()
            if title.startswith("Senior Android / Kotlin"):
                continue
            level = max(0, min(len(hashes) - 1, 2))
            add_heading(story, title, level, styles, heading_counter)
            continue

        label_match = re.match(r"^\*\*([^*]+)\*\*$", line)
        if label_match:
            flush_paragraph(story, paragraph, styles)
            flush_bullets(story, bullets, styles)
            story.append(Paragraph(inline_markup(label_match.group(1)), styles["Label"]))
            continue

        if line.startswith(">"):
            flush_paragraph(story, paragraph, styles)
            flush_bullets(story, bullets, styles)
            quote = line.lstrip("> ").strip()
            if quote:
                story.append(Paragraph(inline_markup(quote), styles["Quote"]))
            continue

        bullet_match = re.match(r"^\s*(?:[-*]|\d+\.)\s+(.*)$", line)
        if bullet_match:
            flush_paragraph(story, paragraph, styles)
            bullets.append(bullet_match.group(1))
            continue

        if re.match(r"^\|.*\|$", line):
            # Keep markdown tables readable as compact monospaced text.
            flush_paragraph(story, paragraph, styles)
            flush_bullets(story, bullets, styles)
            story.append(Preformatted(line, styles["Code"]))
            continue

        paragraph.append(line)

    flush_paragraph(story, paragraph, styles)
    flush_bullets(story, bullets, styles)
    return story


def build_pdf():
    OUT_DIR.mkdir(exist_ok=True)
    styles = make_styles()

    doc = IndexedDocTemplate(
        str(OUT_FILE),
        pagesize=letter,
        rightMargin=0.68 * inch,
        leftMargin=0.68 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.7 * inch,
        title="Senior Android / Kotlin Interview Guide",
        author="Codex",
    )

    story = []
    story.append(Spacer(1, 1.3 * inch))
    story.append(Paragraph("Senior Android / Kotlin", styles["Title"]))
    story.append(Paragraph("Interview Study Guide", styles["Title"]))
    story.append(
        Paragraph(
            "Study guide, question bank, mock interviews, flashcards, and references.",
            styles["Subtitle"],
        )
    )
    story.append(Spacer(1, 0.25 * inch))
    story.append(
        Paragraph(
            "Generated from the Markdown study files in the interview-guide folder.",
            styles["Small"],
        )
    )
    story.append(PageBreak())

    story.append(Paragraph("Table of Contents", styles["H1"]))
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            name="TOCLevel1",
            fontName="Helvetica-Bold",
            fontSize=10,
            leftIndent=0,
            firstLineIndent=0,
            spaceBefore=4,
            leading=13,
        ),
        ParagraphStyle(
            name="TOCLevel2",
            fontName="Helvetica",
            fontSize=9,
            leftIndent=14,
            firstLineIndent=0,
            leading=12,
        ),
        ParagraphStyle(
            name="TOCLevel3",
            fontName="Helvetica",
            fontSize=8,
            leftIndent=28,
            firstLineIndent=0,
            leading=10,
            textColor=colors.HexColor("#555555"),
        ),
    ]
    story.append(toc)
    story.append(PageBreak())

    heading_counter = [1]
    for idx, (title, path) in enumerate(STUDY_FILES):
        if idx:
            story.append(PageBreak())
        story.extend(parse_markdown(path, title, styles, heading_counter))

    doc.multiBuild(story)
    print(OUT_FILE)


if __name__ == "__main__":
    build_pdf()
