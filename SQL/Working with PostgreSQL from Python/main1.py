import psycopg2


def create_db(conn):
    with conn.cursor() as curs:
        curs.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL
            );
        """)
        curs.execute("""
            CREATE TABLE IF NOT EXISTS phones (
                id SERIAL PRIMARY KEY,
                client_id INTEGER REFERENCES clients(id),
                phone VARCHAR(255) UNIQUE NOT NULL
            );
        """)
class Client:
    def __init__(self, first_name, last_name, email, phones=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phones = phones or []


def add_client(conn, first_name, last_name, email, phone=None):
    with conn.cursor() as curs:
        # Check if a client with the given email already exists
        curs.execute(
            """
            SELECT id FROM clients WHERE email = %s;
            """,
            (email,)
        )
        existing_client = curs.fetchone()
        if existing_client:
            return existing_client[0]

        # Insert the new client into the database
        curs.execute(
            """
            INSERT INTO clients (first_name, last_name, email) 
            VALUES (%s, %s, %s) RETURNING id;
            """,
            (first_name, last_name, email)
        )
        client_id = curs.fetchone()[0]

        # If a phone number is provided, add it to the database
        if phone:
            try:
                add_phone(conn, client_id, phone)
            except ValueError as e:
                conn.rollback()
                return str(e)

        # Commit the changes and return the client_id
        conn.commit()
        return client_id

def add_phone(conn, client_id, phone):
    with conn.cursor() as curs:
        if find_client(conn, phone=phone):
            return "Такой номер телефона уже используется"
        curs.execute(
            """
            SELECT * from clients 
            WHERE id = %s;
            """,
            (str(client_id),)
        )
        if not curs.fetchone():
            return "Такого клиента не существует"
        curs.execute(
            """
            INSERT INTO phones (client_id, phone) 
            VALUES (%s, %s)
            ON CONFLICT (phone) DO NOTHING;
            """,
            (client_id, phone)
        )
        if curs.rowcount == 0:
            return "Такой номер телефона уже используется"
        conn.commit()
        return "Телефон успешно добавлен"
def change_client(conn, client_id, first_name=None, last_name=None, email=None):
    with conn.cursor() as curs:
        # Check if the new email already exists in the table
        curs.execute(
            """
            SELECT id FROM clients WHERE email = %s;
            """,
            (email,)
        )
        conflicting_client = curs.fetchone()

        # If there is a conflicting client, delete it
        if conflicting_client:
            delete_client(conn, conflicting_client[0])

        # Construct the SQL statement and data
        sql = """
            UPDATE clients SET
            first_name = COALESCE(%s, first_name),
            last_name = COALESCE(%s, last_name),
            email = COALESCE(%s, email)
            WHERE id = %s;
        """
        data = (first_name, last_name, email, client_id)

        # Execute the SQL statement
        curs.execute(sql, data)

        # Commit the changes
        conn.commit()

def delete_phone(conn, client_id, phone):
    with conn.cursor() as curs:
        curs.execute(
            """
            DELETE FROM phones 
            WHERE client_id=%s AND phone=%s
            """,
            (client_id, phone)
        )
        if not curs.rowcount:
            return "Такого номера телефона не существует"
        conn.commit()
        return "Номер телефона успешно удален"


def delete_client(conn, client_id):
    with conn.cursor() as curs:
        # Delete all phones associated with the client
        curs.execute(
            """
            DELETE FROM phones WHERE client_id = %s;
            """,
            (client_id,)
        )

        # Delete the client
        curs.execute(
            """
            DELETE FROM clients WHERE id = %s;
            """,
            (client_id,)
        )

        # Commit the changes
        conn.commit()


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as curs:
        params = []
        data = []
        if first_name:
            params.append("first_name=%s")
            data.append(first_name)
        if last_name:
            params.append("last_name=%s")
            data.append(last_name)
        if email:
            params.append("email=%s")
            data.append(email)
        if phone:
            params.append("id IN (SELECT client_id FROM phones WHERE phone=%s)")
            data.append(phone)
        if not params:
            return []
        sql = "SELECT * FROM clients WHERE " + " AND ".join(params)
        curs.execute(sql, data)
        rows = curs.fetchall()
        return [Client(row[1], row[2], row[3]) for row in rows]

with psycopg2.connect(
            host="localhost",
            port="5432",
            dbname="create_db",
            user="postgres",
            password="majkl4321"
        ) as conn:
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