from flask import Flask, send_file
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

@app.route("/")
def inicio():
    return '<a href="/pdf">Descargar mi primer PDF</a>'

@app.route("/pdf")
def crear_pdf():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)

    pdf.drawString(100, 750, "Hola, este es tu primer PDF creado desde una web.")
    pdf.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="archivo.pdf")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

