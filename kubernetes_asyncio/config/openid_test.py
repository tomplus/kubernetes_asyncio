import json

import pytest
from aiohttp import web
from aiohttp.test_utils import TestClient
from aiohttp.test_utils import TestServer
from asynctest import patch

from .config_exception import ConfigException
from .openid import OpenIDRequestor


def make_responder(response):

    async def responder(request):
        return response

    return responder


def respond_json(data):
    return make_responder(
        web.Response(
            text=json.dumps(data),
            content_type='application/json',
        )
    )


@pytest.fixture
def requestor():
    return OpenIDRequestor(
        'client-id',
        'client-secret',
        '',
    )


@pytest.yield_fixture
def working_client(loop, aiohttp_client):
    app = web.Application()

    app.router.add_get('/.well-known/openid-configuration', respond_json({'token_endpoint': '/token'}))
    app.router.add_post('/token', respond_json({'id-token': 'id-token-data', 'refresh-token': 'refresh-token-data'}))

    with patch('kubernetes_asyncio.config.openid.OpenIDRequestor._client_session') as _client_session:
        client = TestClient(TestServer(app, loop=loop), loop=loop)
        _client_session.return_value = client
        loop.run_until_complete(client.start_server())

        yield client

        loop.run_until_complete(client.close())


@pytest.yield_fixture
def fail_well_known_client(loop, aiohttp_client):
    app = web.Application()

    app.router.add_get('/.well-known/openid-configuration', make_responder(web.Response(status=500)))

    with patch('kubernetes_asyncio.config.openid.OpenIDRequestor._client_session') as _client_session:
        client = TestClient(TestServer(app, loop=loop), loop=loop)
        _client_session.return_value = client
        loop.run_until_complete(client.start_server())

        yield client

        loop.run_until_complete(client.close())


@pytest.yield_fixture
def fail_token_request_client(loop, aiohttp_client):
    app = web.Application()

    app.router.add_get('/.well-known/openid-configuration', respond_json({'token_endpoint': '/token'}))
    app.router.add_post('/token', make_responder(web.Response(status=500)))

    with patch('kubernetes_asyncio.config.openid.aiohttp.ClientSession') as _client_session:
        client = TestClient(TestServer(app, loop=loop), loop=loop)
        _client_session.return_value = client
        loop.run_until_complete(client.start_server())

        yield client

        loop.run_until_complete(client.close())


async def test_refresh_token_success(requestor, working_client):
    resp = await requestor.refresh_token('my-refresh-token')

    assert resp['id-token'] == 'id-token-data'
    assert resp['refresh-token'] == 'refresh-token-data'


async def test_failed_well_known(requestor, fail_well_known_client):
    with pytest.raises(ConfigException):
        await requestor.refresh_token('my-refresh-token')


async def test_failed_refresh_token(requestor, fail_token_request_client):
    with pytest.raises(ConfigException):
        await requestor.refresh_token('my-refresh-token')
