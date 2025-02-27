from flask_restx import Namespace, Resource, fields

api = Namespace('example', description='Пример API')

# Модель для Swagger
data_model = api.model('Data', {
    'id': fields.Integer(readonly=True),
    'message': fields.String(required=True)
})

@api.route('/data')
class ExampleResource(Resource):
    @api.doc('get_data')
    def get(self):
        """Получить тестовые данные"""
        return {"message": "Hello from Flask-RESTX!"}

    @api.doc('create_data')
    @api.expect(data_model)
    def post(self):
        """Создать новые данные"""
        payload = api.payload
        print("Received data:", payload)
        return {"status": "success", "data": payload}, 201