import connect
def update_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_update ='''
    UPDATE clientes
    SET teléfono_cliente=666111222
    WHERE id_cliente = 1
    '''
    cursor.execute(sql_update)
    conn.commit()

    cursor.close()
    conn.close()

    return {"Update succesfully"}