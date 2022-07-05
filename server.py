from flask import render_template
import config

app = config.connex_app

# Nacitanie konfiguracneho suboru pre swagger
app.add_api('swagger.yml')

# Spustenie flask aplikacie s debug modom
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
