tables = [
  {
    'name': 'Account',
    'columns': {
      'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
      'user_name': 'TEXT', 
      'balance': 'REAL'
    }
  },
  {
    'name': 'DebitCard',
    'columns': {
      'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
      'number': 'INTEGER',
      'client_name': 'TEXT',
      'expire_date': 'TEXT',
      'cvv': 'INTEGER',
      'type': 'TEXT'
    }
  },
  {
    'name': 'Transactions',
    'columns': {
      'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
      'description': 'TEXT',
      'from_account': 'INTEGER',
      'to_account': 'INTEGER',
      'card': 'INTEGER'
    }
  }
]