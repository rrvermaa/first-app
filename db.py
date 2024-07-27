import pyodbc

class ListDatabase:
  
  def __init__(self):
      self.conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=LAPTOP-TQ5A6E2S\SQLEXPRESS; DATABASE=cafe;')
      self.cursor = self.conn.cursor()
      
  def get_lists(self):
    query = 'SELECT * FROM lists'
    result = self.cursor.execute(query)
    result_dict = []
    for row in result.fetchall():
      list_dict = {}
      list_dict['id'] = row[0]
      list_dict['name'] = row[1]
      list_dict['age'] = row[2]
      result_dict.append(list_dict)
  
    return result_dict    
  
  def get_list(self,id = "325eda30c79249be95fe6c3dfdc4ee64"):
    query = f"SELECT * FROM lists WHERE id = '{id}'"
    result = self.cursor.execute(query)
    for row in result.fetchall():
      list_dict = { }
      list_dict['id'], list_dict['name'], list_dict['age'] = row
      return [list_dict]
    
  def add_item(self, id, request_data):
    query = f"INSERT INTO lists(id, name, age) VALUES('{id}', '{request_data['name']}', '{request_data['age']}')"
    self.conn.execute(query)
    self.conn.commit()
  
  def update_item(self, id, body):
    query = f"UPDATE lists SET name = '{body['name']}', age = '{body['age']}' WHERE id = '{id}'"
    self.cursor.execute(query)
    if self.cursor.rowcount == 0:
      return False
    else:
      self.conn.commit()
      
  def delete_item(self,id):
    query = f"DELETE FROM lists where id = '{id}'"
    self.cursor.execute(query)
    if self.cursor.rowcount == 0:
        return False
    else:
        self.conn.commit()
        return True
    
      