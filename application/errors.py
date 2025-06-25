def register_error_handlers(app):
	@app.errorhandler(404)
	def not_found(error):
		return {'error': 'Not found'}, 404

	@app.errorhandler(500)
	def server_error(error):
		return {'error': 'Server error'}, 500
