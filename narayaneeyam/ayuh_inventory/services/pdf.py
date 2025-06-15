import os

from fpdf import FPDF, HTMLMixin

from django.conf import settings


class PDF(FPDF, HTMLMixin):
    def header(self):
        # mandatory line of code
        self.set_font(family="Helvetica", style="B", size=13)
        self.set_text_color(37, 153, 92)

        # logo
        self.image(
            name=settings.APP_SETTINGS.get("LETTERHEAD_LOGO_IMAGE"), x=10, y=5, w=20
        )

        # title
        title_width = (
            self.get_string_width(settings.APP_SETTINGS.get("LETTERHEAD_NAME")) + 6
        )
        self.set_x((210 - title_width) / 2)
        self.cell(w=title_width, h=2, txt="", border=0, new_y="NEXT", align="C")
        self.set_x((210 - title_width) / 2)
        self.cell(
            w=title_width,
            h=4,
            txt=settings.APP_SETTINGS.get("LETTERHEAD_NAME"),
            border=0,
            new_y="NEXT",
            align="C",
        )

        # motto
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(92, 82, 77)
        self.set_x((210 - title_width) / 2)
        self.cell(
            w=title_width,
            h=4,
            txt=settings.APP_SETTINGS.get("LETTERHEAD_MOTTO"),
            border=0,
            align="C",
        )

        # contact
        self.add_font(
            "DejaVu", "", str(os.path.join(os.getcwd(), "DejaVuSansCondensed.ttf"))
        )
        self.set_font("DejaVu", "", 9)
        self.set_text_color(0, 0, 0)
        self.set_y(7)
        self.set_x(170)
        self.cell(
            w=40,
            h=4,
            txt=settings.APP_SETTINGS.get("LETTERHEAD_ADDR_LINE1"),
            border=0,
            new_y="NEXT",
            align="R",
        )
        self.set_x(170)
        self.cell(
            w=40,
            h=4,
            txt=settings.APP_SETTINGS.get("LETTERHEAD_ADDR_LINE2"),
            border=0,
            new_y="NEXT",
            align="R",
        )
        self.set_x(170)
        self.cell(
            w=40,
            h=4,
            txt=settings.APP_SETTINGS.get("LETTERHEAD_CONTACT1"),
            border=0,
            new_y="NEXT",
            align="R",
        )
        self.set_x(170)
        self.cell(
            w=40,
            h=4,
            txt=settings.APP_SETTINGS.get("LETTERHEAD_CONTACT2"),
            border=0,
            new_y="NEXT",
            align="R",
        )

        # line
        self.set_line_width(0.2)
        self.set_draw_color(r=255, g=128, b=0)
        self.line(x1=0, y1=25, x2=210, y2=25)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 6)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
