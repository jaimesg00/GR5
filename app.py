from flask import Flask, render_template, request, redirect, url_for, session
from config import get_db_connection
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "taskapp"  

#Inicio
@app.route('/')
def home():
    return render_template('index.html')

#Inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

    connection.close()

    if user is not None:
        stored_password_hash = user[4]  
        if check_password_hash(stored_password_hash, password):
            session['email'] = email
            session['name'] = user[1]
            session['surnames'] = user[2]
            return redirect(url_for('tasks'))
        else:
            return render_template('index.html', message="Las credenciales no son correctas")
    else:
        return render_template('index.html', message="Las credenciales no son correctas")

#Registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        surnames = request.form['surnames']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        if name and surnames and email and password:
            connection = get_db_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
                existing_user = cursor.fetchone()

            if existing_user:
                return render_template('register.html', message="Este correo ya está registrado.")
            
            with connection.cursor() as cursor:
                sql = "INSERT INTO users (name, surnames, email, password_hash) VALUES (%s, %s, %s, %s)"
                data = (name, surnames, email, hashed_password)
                cursor.execute(sql, data)
            connection.commit()
            connection.close()

            return render_template('register.html', register_message="Usuario registrado con éxito. ¡Ahora puedes iniciar sesión!")

    return render_template('register.html')


#Tareas
@app.route('/tasks', methods=['GET'])
def tasks():
    email = session['email']
    
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM tasks WHERE email = %s", [email])
        tasks = cursor.fetchall()

    columnNames = [column[0] for column in cursor.description]
    insertObject = [dict(zip(columnNames, record)) for record in tasks]

    connection.close()

    return render_template('tasks.html', tasks=insertObject)

#Cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

#Nueva tarea
@app.route('/new-task', methods=['POST'])
def new_task():
    if 'email' not in session:
        return redirect(url_for('login'))  

    title = request.form['title']
    description = request.form['description']
    start_datetime = request.form.get('start_datetime', None)
    end_datetime = request.form.get('end_datetime', None)
    email = session['email']  

   
    date_task = datetime.now()  

    if start_datetime:
        start_datetime = datetime.strptime(start_datetime, "%Y-%m-%dT%H:%M")
    else:
        start_datetime = datetime.now()

    if end_datetime:
        end_datetime = datetime.strptime(end_datetime, "%Y-%m-%dT%H:%M")
    else:
        end_datetime = None

    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = """
            INSERT INTO tasks (title, description, start_datetime, end_datetime, email, date_task) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        data = (title, description, start_datetime, end_datetime, email, date_task)
        cursor.execute(sql, data)
    connection.commit()
    connection.close()

    return redirect(url_for('tasks'))

#Borrar tarea
@app.route("/delete-task", methods=["POST"])
def deleteTask():
    task_id = request.form['id']

    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    connection.commit()
    connection.close()

    return redirect(url_for('tasks'))

#Añadir usuario 
@app.route('/new-user', methods=['POST'])
def new_user():
    name = request.form['name']
    surnames = request.form['surnames']
    email = request.form['email']
    password = request.form['password']

    hashed_password = generate_password_hash(password)

    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

    if existing_user:
        return redirect(url_for('tasks', message="Este correo ya está registrado."))

    with connection.cursor() as cursor:
        sql = "INSERT INTO users (name, surnames, email, password_hash) VALUES (%s, %s, %s, %s)"
        data = (name, surnames, email, hashed_password)
        cursor.execute(sql, data)

    connection.commit()
    connection.close()

    return redirect(url_for('tasks'))




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

