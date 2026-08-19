from db_config import get_db_connection

def get_order_history():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT o.order_id, c.name AS customer_name, p.name AS product_name,
               o.quantity, p.price, (o.quantity * p.price) AS total_amount,
               o.order_date
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        JOIN products p ON o.product_id = p.product_id
        ORDER BY o.order_date DESC
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_highest_value_order():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
SELECT o.order_id, c.name AS customer_name, SUM(o.quantity * p.price) AS total_amount
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        JOIN products p ON o.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY total_amount DESC
        LIMIT 1
    """
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_most_active_customer():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT c.name AS customer_name, COUNT(o.order_id) AS order_count
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        GROUP BY c.customer_id
        ORDER BY order_count DESC
        LIMIT 1
    """
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result