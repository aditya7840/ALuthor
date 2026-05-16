from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
import time
from utils.loggers import get_logger

logger = get_logger("formatter")


def create_pdf(book):
    filename = f"book_{int(time.time())}.pdf"

    doc = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    story = []

    front = book["front"]
    back = book["back"]
    tp = front["title_page"]

    # Title Page
    story.append(Spacer(1, 100))
    story.append(Paragraph(tp["title"], styles["Title"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"Author: {tp['author']}", styles["Normal"]))
    story.append(Paragraph(tp["edition"], styles["Normal"]))
    story.append(Spacer(1, 10))

    # Copyright
    story.append(Paragraph("Copyright", styles["Heading2"]))
    story.append(Paragraph(tp["copyright"], styles["Normal"]))
    story.append(Spacer(1, 10))

    # Dedication
    story.append(Paragraph("Dedication", styles["Heading2"]))
    story.append(Paragraph(tp["dedication"], styles["Normal"]))
    story.append(PageBreak())

    # TOC
    story.append(Paragraph("Contents", styles["Heading2"]))
    for i, t in enumerate(tp["toc"], 1):
        story.append(Paragraph(f"{i}. {t}", styles["Normal"]))
    story.append(PageBreak())

    # Chapters
    for i, ch in enumerate(book["chapters"], 1):
        story.append(Paragraph(f"Chapter {i}: {ch['title']}", styles["Heading2"]))
        story.append(Spacer(1, 8))
        story.append(Paragraph(ch["content"], styles["BodyText"]))
        story.append(PageBreak())

    # Afterword
    story.append(Paragraph("Afterword", styles["Heading2"]))
    story.append(Paragraph(back["afterword"], styles["Normal"]))
    story.append(Spacer(1, 10))

    # References
    story.append(Paragraph("References", styles["Heading2"]))
    for r in back["references"]:
        story.append(Paragraph(f"- {r}", styles["Normal"]))
    story.append(Spacer(1, 10))

    # About Author
    story.append(Paragraph("About the Author", styles["Heading2"]))
    story.append(Paragraph(back["about_author"], styles["Normal"]))

    doc.build(story)

    logger.info(f"PDF generated: {filename}")
    print(f"✅ Book created: {filename}")