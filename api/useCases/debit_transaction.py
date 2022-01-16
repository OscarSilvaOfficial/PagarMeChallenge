from api.adapters.repository.interfaces.account_repository_interface import AccountRepositoryInterface
from api.adapters.repository.interfaces.card_repository_interface import CardRepositoryInterface
from api.adapters.repository.interfaces.transaction_repository_interface import TransactionsRepositoryInterface
from api.entities.transaction.transaction import Transactions
from api.useCases.interfaces.debit_transaction_use_case import DebitTransactionsUseCaseInterface
from api.entities.card.debit_card import DebitCard
from api.entities.account.account import Account


class DebitTransactionsUseCase(DebitTransactionsUseCaseInterface):
  
  def __init__(
    self, 
    transaction_repository: TransactionsRepositoryInterface, 
    account_repository: AccountRepositoryInterface,
    debit_card_repository: CardRepositoryInterface
  ):
    self._transaction_repository = transaction_repository
    self._account_repository = account_repository
    self._debit_card_repository = debit_card_repository
  
  def get_transactions(self):
    return self._transaction_repository.get_transactions()
  
  def get_transaction(self, transaction_id: int):
    return self._transaction_repository.get_transaction(transaction_id=transaction_id)

  def create_transaction(self, value: float, from_document: str, to_document: str, card_number: int, cvv: int):
    from_account_data = self._account_repository.get_account(document=from_document)
    to_account_data = self._account_repository.get_account(document=to_document)
    card_data = self._debit_card_repository.get_card(number=card_number)
        
    from_account = Account(**from_account_data).id
    to_account = Account(**to_account_data).id
    card = DebitCard(**card_data).id

    transaction = Transactions(
      description='Debit transaction',
      card=card,
      from_account=from_account,
      to_account=to_account,
      value=value
    )
        
    return self._transaction_repository.create_transaction(transaction=transaction)
      