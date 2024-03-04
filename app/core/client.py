from app.core import database
from app.validators import *
from app.exceptions import *


async def register(data: RegisterData):
    if database.user_registered(data.email):
        raise UserAlreadyExist()
    database.register(data.email, data.password, data.name)
    return database.create_session(data.email)


async def login(data: LoginData):
    if not database.user_registered(data.email):
        raise UserNotFound()

    if not database.check_login(data.email, data.password):
        raise UserPasswordIsIncorrect()
    return database.create_session(data.email)


async def account_info(data: AccountInfoData):
    account = database.get_account_by_session(data.session_key)
    if not account:
        raise NotAuthorized()
    return database.get_account_info(account)


async def referals_list(data: ReferalsListData):
    account = database.get_account_by_session(data.session_key)
    if not account:
        raise NotAuthorized()
    return database.get_referals_list(account)


async def referals_add(data: ReferalsAddData):
    account = database.get_account_by_referal_link(data.referal_link)
    if not account:
        raise ReferalLinkNotExists()
    database.add_referal(data.referal_link, data.avatarex_id)
    return 'Реферал привязан!'


async def account_payments_list(data: AccountPaymentsListData):
    account = database.get_account_by_session(data.session_key)
    if not account:
        raise NotAuthorized()
    return database.get_payments(account)


async def account_payments_add(data: AccountPaymentsAddData):
    account = database.get_account_by_referal(data.avatarex_user_email)
    if not account:
        raise AvatarexUserNotRegistered()
    database.add_payment(account, data.avatarex_user_email, data.amount)
    return 'Оплата добавлена!'
