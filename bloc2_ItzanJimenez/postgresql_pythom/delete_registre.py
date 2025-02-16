import connect
def delete_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_delete ='''
    DELETE FROM clientes
    WHERE id_cliente = 1
    '''
    cursor.execute(sql_delete)
    conn.commit()

    cursor.close()
    conn.close()

    return {"Delete succesfully"}