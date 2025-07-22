from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', canonical_url='https://amplitudavoln.ru/')

@app.route('/volnovodnye-truby-med-latun/')
def med_latun():
    return render_template('med_latun.html', canonical_url='https://amplitudavoln.ru/volnovodnye-truby-med-latun/')

@app.route('/Volnovodnye-truby-iz-alyuminievyh-splavov/')
def alyuminii():
    return render_template('alyuminii.html', canonical_url='https://amplitudavoln.ru/Volnovodnye-truby-iz-alyuminievyh-splavov/')

@app.route('/zayavka/')
def zayavka():
    return render_template('zayavka.html', canonical_url='https://amplitudavoln.ru/zayavka/')

@app.route('/robots.txt')
def robots():
    return send_from_directory(os.getcwd(), 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.getcwd(), 'sitemap.xml')

@app.route('/google90a2af5fc16f449f.html')
def google_verification():
    return 'google-site-verification: google90a2af5fc16f449f.html'

@app.route('/yandex_8d8d6515a40fab06.html')
def yandex_verification():
    return '''
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        </head>
        <body>Verification: 8d8d6515a40fab06</body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
