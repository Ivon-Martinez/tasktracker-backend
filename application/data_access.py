from flask import current_app


def get_all_tasks():
	from application import mysql

	if not mysql:
		raise RuntimeError("MySQL extension not initialized")
	
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM tasks")
	tasks = cur.fetchall()
	cur.close()
	return tasks


def add_task_to_db(title, description):
    from application import mysql
    
    if not mysql:
        raise RuntimeError("MySQL extension not initialized")

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO tasks (title, description) VALUES (%s, %s)",
        (title, description)
    )
    mysql.connection.commit()
    task_id = cur.lastrowid
    cur.close()
    return task_id


def update_task_in_db(task_id, title, description):
    from application import mysql

    if not mysql:
        raise RuntimeError("MySQL extension not initialized")

    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE tasks SET title = %s, description = %s WHERE id = %s",
        (title, description, task_id)
    )
    mysql.connection.commit()
    updated_rows = cur.rowcount
    cur.close()
    return updated_rows


def delete_task_from_db(task_id):
    from application import mysql

    if not mysql:
        raise RuntimeError("MySQL extension not initialized")

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    mysql.connection.commit()
    deleted_rows = cur.rowcount
    cur.close()
    return deleted_rows
