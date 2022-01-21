from api.adapters.repository.account_repository import AccountRepository
from api.infra.db.mongo import Mongo

db = Mongo(db_name='pagarme', mongo_string_connection='mongodb://localhost:27017/')

repository = AccountRepository(db=db)

def test_mongo_update():
  repository.update_account(document='12345678904', update_values={'user_name': 'teste1'})