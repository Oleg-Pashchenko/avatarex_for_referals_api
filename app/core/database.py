from app.core.models import Account


def user_registered(email: str) -> bool:
    pass


def check_login(email: str, password: str) -> bool:
    pass


def register(email: str, password: str, name: str):
    pass


def create_session(email: str) -> str:
    pass


def get_account_by_session(session_key: str) -> Account:
    pass


def get_account_info(account: Account) -> dict:
    pass


def get_referals_list(account: Account) -> dict:
    pass


def get_account_by_referal_link(referal_link: str) -> Account:
    pass


def add_referal(referal_key: str, avatarex_id: int):
    pass


def get_payments(account: Account) -> dict:
    pass


def get_account_by_referal(avatarex_user_email: str) -> Account:
    pass


def add_payment(account: Account, avatarex_user_email: str, amount: int):
    pass
