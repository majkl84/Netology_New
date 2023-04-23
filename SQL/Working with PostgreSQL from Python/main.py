import psycopg2

def create_db(conn):
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS clients (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(50) UNIQUE
        )
        """
    )
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS phones (
            id SERIAL PRIMARY KEY,
            client_id INTEGER NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
            phone_number VARCHAR(20) NOT NULL
        )
        """
    )
    conn.commit()

def add_client(conn, first_name, last_name, email=None):
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO clients (first_name, last_name, email)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (first_name, last_name, email)
    )
    client_id = cur.fetchone()[0]
    conn.commit()
    return client_id

def add_phone(conn, client_id, phone_number):
    cur = conn.cursor()
    cur.execute("INSERT INTO phones (client_id, phone_number) VALUES (%s, %s)", (client_id, phone_number))
    conn.commit()

def change_client(conn, client_id, first_name=None, last_name=None, email=None):
    cur = conn.cursor()
    if first_name:
        cur.execute(
            """
            UPDATE clients
            SET first_name = %s
            WHERE id = %s
            """,
            (first_name, client_id)
        )
    if last_name:
        cur.execute(
            """
            UPDATE clients
            SET last_name = %s
            WHERE id = %s
            """,
            (last_name, client_id)
        )
    if email:
        cur.execute(
            """
            UPDATE clients
            SET email = %s
            WHERE id = %s
            """,
            (email, client_id)
        )
    conn.commit()


def delete_client(conn, client_id):
    cur = conn.cursor()
    cur.execute(
        """
        DELETE FROM clients
        WHERE id = %s
        """,
        (client_id,)
    )
    conn.commit()

def delete_phone(conn, client_id, phone_number):
    cur = conn.cursor()
    cur.execute("DELETE FROM phones WHERE client_id = %s AND phone_number = %s", (client_id, phone_number))
    conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    cur = conn.cursor()
    query = """
            SELECT c.id, c.first_name, c.last_name, c.email, p.phone_number
            FROM clients c
            LEFT JOIN phones p ON c.id = p.client_id
            WHERE
            """
    params = ()
    if first_name:
        query += "c.first_name = %s AND "
        params += (first_name,)
    if last_name:
        query += "c.last_name = %s AND "
        params += (last_name,)
    if email:
        query += "c.email = %s AND "
        params += (email,)
    if phone:
        query += "p.phone_number = %s AND "
        params += (phone,)
    query = query[:-5] + ";"
    cur.execute(query, params)
    rows = cur.fetchall()
    clients = {}
    for row in rows:
        client_id, first_name, last_name, email, phone = row
        if client_id not in clients:
            clients[client_id] = {
                "id": client_id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phones": []
            }
        if phone:
            clients[client_id]["phones"].append(phone)
    return list(clients.values())

with psycopg2.connect(database="clients_db", user="postgres", password="majkl4321") as conn:
    create_db(conn)

    # Добавляем клиентов
    client1_id = add_client(conn, "Иван", "Иванов", "ivanov@example.com")
    client2_id = add_client(conn, "Петр", "Петров", "petrov@example.com")

    # Добавляем телефоны клиентов
    add_phone(conn, client1_id, "1234567")
    add_phone(conn, client1_id, "7654321")
    add_phone(conn, client2_id, "5555555")

    # Изменяем данные клиента
    change_client(conn, client1_id, first_name="Николай", email="nikolay@example.com")

    # Удаляем телефон клиента
    delete_phone(conn, client1_id, "1234567")

    # Удаляем клиента
    delete_client(conn, client2_id)

    # Ищем клиентов по разным параметрам
    print(find_client(conn, first_name="Николай"))  # Выведет информацию о клиенте с именем "Николай"
    print(find_client(conn, email="ivanov@example.com"))  # Выведет информацию о клиенте с email "ivanov@example.com"
    print(find_client(conn, phone="7654321"))  # Выведет информацию о клиенте, у которого есть телефон "7654321"