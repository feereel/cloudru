from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
import os

routes = web.RouteTableDef()

@routes.get('/hostname')
async def hostname(request: Request) -> Response:
    with os.popen('hostname') as st:
        res = st.read().replace('\n', '')
    return web.json_response({'hostname': res})

@routes.get('/author')
async def hostname(request: Request) -> Response:
    return web.json_response({'author': os.environ.get('AUTHOR', None)})

@routes.get('/id')
async def hostname(request: Request) -> Response:
    return web.json_response({'id': os.environ.get('UUID', None)})

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8000)
