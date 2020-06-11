from flask import Flask, send_file
import generate

app = Flask(__name__)

@app.route("/")

def gen_docx():
    template = 'InvoiceTpl.docx'
    document = generate.from_template(template)
    document.seek(0)

    return send_file(
        document, mimetype='application/vnd.openxmlformats-'
        'officedocument.wordprocessingml.document', as_attachment=True,
        attachment_filename='invoice.docx')
 
if __name__ == "__main__":
    app.run(debug=True)