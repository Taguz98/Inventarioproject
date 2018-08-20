from reportlab.graphics.barcode import code128
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import FileResponse, Http404
import os.path as path

def pdf_view(request, p):
    createBarCodes(p)
    filename = './' + p + '.pdf'
    try:
        return FileResponse(open(filename, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def createBarCodes(codigo_producto):
    codeName = codigo_producto
    c = canvas.Canvas(codeName + ".pdf", pagesize=A4)
    margin_x = 7.526
    margin_y = 13.876
    padding_x = 7.526
    font_size = 15
    width, height = A4
    extra_padding = 20

    bars_width = (float(width - margin_x * 2) - 3 * padding_x) / 4
    bars_height = float(height - margin_y * 2) / 15
    bar_height = bars_height - font_size
    bar_width = (bars_width - extra_padding) / (len(codeName) * 11 + 35)

    barcode_value = codeName
    barcode128 = code128.Code128(barcode_value, barHeight=bar_height, barWidth=bar_width, humanReadable=True, )

    for i in range(0, 4):
        for j in range(0, 15):
            x = margin_x + i * (bars_width + padding_x)
            y = margin_y + j * bars_height
            barcode128.drawOn(c, x, y)

    if not path.exists("./" + str(c) + ".pdf"):
        c.save()
