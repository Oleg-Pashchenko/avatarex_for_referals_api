from aiohttp import web
from app.handlers import *
app = web.Application()

api_v1 = '/api/v1'


async def routers():
    app.router.add_post(f'{api_v1}/register/', await register_handler)
    app.router.add_post(f'{api_v1}/login/', await login_handler)
    app.router.add_post(f'{api_v1}/account/info/', await account_info_handler)
    app.router.add_post(f'{api_v1}/referals/list/', await referals_list_handler)
    app.router.add_post(f'{api_v1}/referals/add/', await referals_add_handler)
    app.router.add_post(f'{api_v1}/account/payments/list/', await account_payments_list_handler)
    app.router.add_post(f'{api_v1}/account/payments/add/', await account_payments_add_handler)

routers()
