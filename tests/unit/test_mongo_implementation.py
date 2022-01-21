from api.infra.db.mongo import MongoRepository

repository = MongoRepository(db_name='pagarme', db_str_connection='mongodb://localhost:27017/')

def test_mongo_update():
  repository.update_document(
    collection_name='accounts', where={'document': '12345678904'}, new_values={'user_name': 'teste'}
  )