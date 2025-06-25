from flask import Blueprint, jsonify, request
from application.data_access import get_all_tasks, add_task_to_db, update_task_in_db, delete_task_from_db 


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
	try:
		tasks = get_all_tasks()
		return jsonify({"tasks": tasks})
	except Exception as e:
		return jsonify({"error": str(e)}), 500


@main_bp.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = get_all_tasks()
        return jsonify({"tasks": tasks})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main_bp.route('/tasks', methods=['POST'])
def add_task():
	print("POST /tasks received")
	try:
		data = request.get_json()
		print("Request JSON:", data)

		title = data.get('title')
		description = data.get('description')

		if not title:
			return jsonify({"error": "Title is required"}), 400
		
		
		task_id = add_task_to_db(title, description)
		
		
		return jsonify({"message": "Task added", "task_id": task_id}), 201
	except Exception as e:
		
		return jsonify({"error": str(e)}), 500


@main_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
	try:
        	data = request.get_json()
        	if not data:
            		return jsonify({"error": "We didn’t receive the task information. Please check and try again."}), 400

        	title = data.get('title')
        	description = data.get('description')


	        if not title or not isinstance(title, str) or title.strip() == "":
        		return jsonify({"error": "Title is required and must be a non-empty string"}), 400

	        if description is not None and not isinstance(description, str):
        		return jsonify({"error": "Description must be a string"}), 400

	        updated = update_task_in_db(task_id, title.strip(), description)
	

        	if updated:
            		return jsonify({"message": "Task updated"}), 200
        	else:
            		return jsonify({"error": "Task not found"}), 404

	except Exception as e:
        	return jsonify({"error": str(e)}), 500


@main_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
	try:
        	deleted = delete_task_from_db(task_id)

        	if deleted:
            		return jsonify({"message": "Task deleted"}), 200
        	else:
            		return jsonify({"error": "Task not found"}), 404

	except Exception as e:
        	return jsonify({"error": str(e)}), 500
