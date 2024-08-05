from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)


@app.route("/")
def home():
    return render_template ("home.html"

# Cargar el modelo previamente guardado
with open('regmodel.pkl', 'rb') as file:
    regmodel = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict_api():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No se proporcionaron datos"}), 400

        columnas = ['LotFrontage', 'LotArea', 'OverallQual','1stFlrSF',
       '2ndFlrSF', 'GrLivArea', 
        'YrSold']
        todaslascolumnas = ['LotFrontage', 'LotArea', 'Neighborhood', 'OverallQual', 'YearBuilt',
                            'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'TotalBsmtSF', '1stFlrSF',
                            '2ndFlrSF', 'GrLivArea', 'FullBath', 'KitchenQual', 'FireplaceQu',
                            'GarageArea', 'OpenPorchSF',  'YrSold']

        print("Datos recibidos:", data)

        # Crear DataFrame con los datos recibidos y los nombres de las columnas
        df = pd.DataFrame([data], columns=todaslascolumnas)

        # Aplicar la transformación logarítmica solo a las columnas especificadas
        df[columnas] = df[columnas].applymap(lambda x: np.log(x) if x > 0 else x)

        print("Datos transformados con logaritmo:", df)

        # Convertir el DataFrame a un array para usar con el modelo
        input_data = df.values
        print("Datos logareados:", input_data)
        # Escalar los datos
        input_data = scaler.transform(input_data)
        print("Datos escalados:", input_data)

        # Realizar la predicción
        output = regmodel.predict(input_data)
        print("Predicción:", output)

        return jsonify({"prediction": float(output[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)