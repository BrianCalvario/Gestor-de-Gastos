from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Gasto
from config import SQLALCHEMY_DATABASE_URI
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return "API Gestor de Gastos funcionando"

@app.route('/gastos', methods=['POST'])
def crear_gasto():
    data = request.json
    nuevo_gasto = Gasto(
        categoria=data['categoria'],
        descripcion=data.get('descripcion', ''),
        monto=data['monto'],
        fecha=datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    )
    db.session.add(nuevo_gasto)
    db.session.commit()
    return jsonify({"message": "Gasto creado correctamente"}), 201

@app.route('/gastos', methods=['GET'])
def obtener_gastos():
    gastos = Gasto.query.all()
    return jsonify([{
        "id": g.id,
        "categoria": g.categoria,
        "descripcion": g.descripcion,
        "monto": g.monto,
        "fecha": g.fecha.strftime('%Y-%m-%d')
    } for g in gastos])

@app.route('/gastos/<int:id>', methods=['PUT'])
def actualizar_gasto(id):
    gasto = Gasto.query.get_or_404(id)
    data = request.json
    gasto.categoria = data['categoria']
    gasto.descripcion = data.get('descripcion', '')
    gasto.monto = data['monto']
    gasto.fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    db.session.commit()
    return jsonify({"message": "Gasto actualizado correctamente"})

@app.route('/gastos/<int:id>', methods=['DELETE'])
def eliminar_gasto(id):
    gasto = Gasto.query.get_or_404(id)
    db.session.delete(gasto)
    db.session.commit()
    return jsonify({"message": "Gasto eliminado correctamente"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

