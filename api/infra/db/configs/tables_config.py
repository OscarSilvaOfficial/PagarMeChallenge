tables = [
  {
    'name': 'Account',
    'columns': {
      'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
      'document': 'TEXT',
      'user_name': 'TEXT', 
      'balance': 'REAL'
    }
  },
  {
    'name': 'Transactions',
    'columns': {
      'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
      'description': 'TEXT',
      'from_account': 'INTEGER',
      'to_account': 'INTEGER',
      'card': 'INTEGER',
      'value': 'REAL'
    }
  }
]

collections = ['transactions', 'accounts']