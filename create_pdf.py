import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages after 1)
        if self._pageNumber > 1:
            self.drawString(54, 755, "Student Performance Analytics System — Project Documentation")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(54, 747, letter[0] - 54, 747)
            
        # Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 54, 30, page_str)
        self.drawString(54, 30, "EWB Courses | Assessment Activity — Python Internship")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(54, 40, letter[0] - 54, 40)
        self.restoreState()

def build_pdf(filename="Project_Documentation.pdf"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, filename)

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=50,
        rightMargin=50,
        topMargin=46,
        bottomMargin=46
    )

    styles = getSampleStyleSheet()

    primary_color = colors.HexColor("#1E3A8A")   # Navy
    secondary_color = colors.HexColor("#2563EB") # Blue
    text_dark = colors.HexColor("#1F2937")       # Dark Charcoal
    gray_bg = colors.HexColor("#F8FAFC")         # Slate tint
    border_color = colors.HexColor("#CBD5E1")    # Slate border

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=primary_color,
        spaceAfter=2
    )

    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=14,
        textColor=secondary_color,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        "Heading1_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11.5,
        leading=14.5,
        textColor=primary_color,
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        "Body_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11.5,
        textColor=text_dark,
        spaceAfter=3
    )

    bullet_style = ParagraphStyle(
        "Bullet_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11.5,
        textColor=text_dark,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2.5
    )

    code_style = ParagraphStyle(
        "Code_Custom",
        parent=styles["Normal"],
        fontName="Courier",
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#0F172A")
    )

    th_style = ParagraphStyle(
        "TH_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=10.5,
        textColor=colors.white
    )

    td_style = ParagraphStyle(
        "TD_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=10.5,
        textColor=text_dark
    )

    story = []

    # Title & Header
    story.append(Paragraph("Student Performance Analytics System", title_style))
    story.append(Paragraph("Project Documentation — Assessment Activity", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.2, color=primary_color, spaceAfter=8))

    # Meta Info Table
    meta_data = [
        [
            Paragraph("<b>Student Name:</b> Anshika Pal", body_style),
            Paragraph("<b>Email:</b> anshikapal2512@gmail.com", body_style)
        ],
        [
            Paragraph("<b>Course:</b> Python Internship (EWB Courses)", body_style),
            Paragraph("<b>GitHub:</b> github.com/anshikapal2512-dora", body_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[256, 256])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), gray_bg),
        ('BOX', (0, 0), (-1, -1), 0.5, border_color),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(meta_table)

    # 1. Project Title
    story.append(Paragraph("1. Project Title", h1_style))
    story.append(Paragraph(
        "<b>Project Name:</b> Student Performance Analytics System &nbsp;|&nbsp; "
        "<b>Author:</b> Anshika Pal (anshikapal2512@gmail.com) &nbsp;|&nbsp; "
        "<b>Context:</b> EWB Courses Python Internship Submission",
        body_style
    ))

    # 2. Objective
    story.append(Paragraph("2. Objective", h1_style))
    story.append(Paragraph(
        "The project delivers an automated analytics application to track, evaluate, and extract meaningful academic insights "
        "from student records. It eliminates manual, error-prone calculation of totals, averages, percentages, and grades, while "
        "providing personalized student report cards and batch-level insights for educators.",
        body_style
    ))

    # 3. Technologies Used
    story.append(Paragraph("3. Technologies Used", h1_style))
    tech_data = [
        [Paragraph("Technology / Tool", th_style), Paragraph("Role & Usage in Project", th_style)],
        [Paragraph("<b>Python 3</b>", td_style), Paragraph("Core language for application logic, calculations, and interactive loop.", td_style)],
        [Paragraph("<b>Pandas</b>", td_style), Paragraph("Dataframe manipulation, CSV reading, vectorized statistics (.mean, .idxmax, .sort_values).", td_style)],
        [Paragraph("<b>NumPy</b>", td_style), Paragraph("Numerical operations, vectorized mean evaluations, and statistical calculations.", td_style)],
        [Paragraph("<b>OS Module</b>", td_style), Paragraph("Dynamic relative path resolution ensuring portability across operating systems.", td_style)],
        [Paragraph("<b>Git & GitHub</b>", td_style), Paragraph("Version control, source code hosting, and project submission tracking.", td_style)],
    ]
    tech_table = Table(tech_data, colWidths=[110, 402])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, border_color),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, gray_bg]),
        ('PADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(tech_table)

    # 4. Dataset Description
    story.append(Paragraph("4. Dataset Description", h1_style))
    story.append(Paragraph(
        "The dataset <b>students1.csv</b> contains 20 student entries indexed by <code>Student_ID</code>.",
        body_style
    ))
    ds_data = [
        [Paragraph("Column", th_style), Paragraph("Type", th_style), Paragraph("Description", th_style), Paragraph("Example", th_style)],
        [Paragraph("Student_ID", td_style), Paragraph("Integer", td_style), Paragraph("Unique student identifier (DataFrame index)", td_style), Paragraph("1", td_style)],
        [Paragraph("Name", td_style), Paragraph("String", td_style), Paragraph("Full name of the student", td_style), Paragraph("Aman", td_style)],
        [Paragraph("Department", td_style), Paragraph("String", td_style), Paragraph("Academic engineering department", td_style), Paragraph("Computer Engineering", td_style)],
        [Paragraph("English", td_style), Paragraph("Integer", td_style), Paragraph("Marks scored in English (out of 100)", td_style), Paragraph("78", td_style)],
        [Paragraph("Hindi", td_style), Paragraph("Integer", td_style), Paragraph("Marks scored in Hindi (out of 100)", td_style), Paragraph("67", td_style)],
        [Paragraph("Maths", td_style), Paragraph("Integer", td_style), Paragraph("Marks scored in Mathematics (out of 100)", td_style), Paragraph("56", td_style)],
        [Paragraph("Attendance", td_style), Paragraph("Float", td_style), Paragraph("Overall student attendance percentage", td_style), Paragraph("75.0", td_style)],
    ]
    ds_table = Table(ds_data, colWidths=[75, 55, 302, 80])
    ds_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('BOX', (0, 0), (-1, -1), 0.5, border_color),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, gray_bg]),
        ('PADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(ds_table)

    # 5. Implementation
    story.append(Paragraph("5. Implementation", h1_style))
    story.append(Paragraph("<b>1. File Path Resolution:</b> Uses <code>os.path.dirname(os.path.abspath(__file__))</code> to dynamically locate <code>students1.csv</code>, guaranteeing portability.", bullet_style))
    story.append(Paragraph("<b>2. Data Ingestion:</b> Loads the CSV using <code>pd.read_csv(csv_path, index_col='Student_ID')</code> and reports total enrolled records.", bullet_style))
    story.append(Paragraph("<b>3. Student Lookup & Evaluation:</b> Performs case-insensitive, whitespace-trimmed lookup. Calculates total marks, average, percentage, grade (A: &ge;90, B: &ge;75, C: &ge;60, D: &ge;35, F: &lt;35), and pass/fail standing (&ge;35).", bullet_style))
    story.append(Paragraph("<b>4. Interactive Menu Loop:</b> Implements a continuous <code>while True</code> loop presenting 5 analytical choices, preventing accidental script exits.", bullet_style))

    # 6. Key Features
    story.append(Paragraph("6. Key Features", h1_style))
    features = [
        "<b>Case-Insensitive Search:</b> Handles name inputs in any casing with extra spaces stripped.",
        "<b>Automated Report Card Generation:</b> Computes totals, averages, grades, percentage, and pass/fail status.",
        "<b>Batch Statistical Analytics:</b> Instant identification of highest scorer, best subject, and class averages.",
        "<b>Persistent User Loop:</b> Users can execute multiple queries in one session before choosing to exit.",
        "<b>Portable Architecture:</b> Safe column access by name and portable relative path resolution."
    ]
    for feat in features:
        story.append(Paragraph(f"• {feat}", bullet_style))

    # 7. Output & Execution Results
    story.append(Paragraph("7. Output / Execution Results", h1_style))
    sample_output = (
        "_____Student Performance Analytics System_____\n"
        "Total number of students in the dataset: 20\n\n"
        "Enter the name of the student to get the report: Aman\n"
        "_____Student_Report_____\n"
        "Student_ID: 1 | Name: Aman | Department: Computer Engineering\n"
        "Marks -> English: 78 | Hindi: 67 | Maths: 56\n"
        "Total: 201 | Average: 67.0 | Grade: C | Status: Pass | Percentage: 67.0% | Attendance: 75.0%\n\n"
        "_____Questions/Answers Menu_____\n"
        "[1] Highest Scorer: Kajal (Average: 87.00)\n"
        "[2] Best Subject: Hindi (Average: 84.35)\n"
        "[3] Passed Students: 20 out of 20 passed\n"
        "[4] Overall Class Average: 79.70"
    )
    output_table = Table([[Paragraph(sample_output.replace('\n', '<br/>'), code_style)]], colWidths=[512])
    output_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F1F5F9")),
        ('BOX', (0, 0), (-1, -1), 0.5, border_color),
        ('PADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(output_table)

    # 8. Final Outcome
    story.append(Paragraph("8. Final Outcome", h1_style))
    story.append(Paragraph(
        "The project successfully achieved all specified goals. The Python CLI analytics application reliably reads and "
        "evaluates student records, generates complete individualized report cards, and provides instant batch-level metrics. "
        "The project is fully tested, documented, version-controlled with Git, and hosted on GitHub.",
        body_style
    ))

    # 9. Challenges & Learning
    story.append(Paragraph("9. Challenges & Learning", h1_style))
    challenges = [
        "<b>Hardcoded Paths:</b> Windows absolute paths broke portability; solved via dynamic relative paths using <code>os.path</code>.",
        "<b>Case Sensitivity:</b> Searches for lowercase names previously failed; resolved with <code>.str.strip().str.lower()</code>.",
        "<b>Repeated Computations:</b> Multiple mean calculations were optimized by caching values in local variables.",
        "<b>Single-Run Menu:</b> Replaced immediate script termination with an interactive <code>while True</code> loop."
    ]
    for ch in challenges:
        story.append(Paragraph(f"• {ch}", bullet_style))

    # 10. GitHub Repository
    story.append(Paragraph("10. GitHub Repository", h1_style))
    story.append(Paragraph(
        "<b>Repository Link:</b> <font color='#2563EB'><u>https://github.com/anshikapal2512-dora/student-performance-analytics</u></font><br/>"
        "Contains <code>main.py</code>, <code>students1.csv</code>, <code>README.md</code>, <code>PROJECT_DOCUMENTATION.md</code>, and <code>Project_Documentation.pdf</code>.",
        body_style
    ))

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully built: {output_path}")

if __name__ == "__main__":
    build_pdf()
