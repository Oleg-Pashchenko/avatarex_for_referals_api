from app.core import client
from app.decorators import request_processing
from app.validators import *

@request_processing
async def register_handler(data: dict):
    data = RegisterData(**data)
    return await client.register(data)


@request_processing
async def login_handler(data: dict):
    data = LoginData(**data)
    return await client.login(data)


@request_processing
async def account_info_handler(data: dict):
    data = AccountInfoData(**data)
    return await client.account_info(data)


@request_processing
async def referals_list_handler(data: dict):
    data = ReferalsListData(**data)
    return await client.referals_list(data)


@request_processing
async def referals_add_handler(data: dict):
    data = ReferalsAddData(**data)
    return await client.referals_add(data)


@request_processing
async def account_payments_list_handler(data: dict):
    data = AccountPaymentsListData(**data)
    return await client.account_payments_list(data)


@request_processing
async def account_payments_add_handler(data: dict):
    data = AccountPaymentsAddData(**data)
    return await client.account_payments_add(data)
