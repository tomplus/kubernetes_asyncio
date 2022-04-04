# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from six.moves.urllib.parse import urlencode, urlparse, urlunparse

from kubernetes_asyncio.client import ApiClient
from kubernetes_asyncio.client.rest import RESTResponse

STDIN_CHANNEL = 0
STDOUT_CHANNEL = 1
STDERR_CHANNEL = 2
ERROR_CHANNEL = 3
RESIZE_CHANNEL = 4


def get_websocket_url(url):
    parsed_url = urlparse(url)
    parts = list(parsed_url)
    if parsed_url.scheme == 'http':
        parts[0] = 'ws'
    elif parsed_url.scheme == 'https':
        parts[0] = 'wss'
    return urlunparse(parts)


class WsResponse(RESTResponse):

    def __init__(self, status, data):
        self.status = status
        self.data = data
        self.headers = {}
        self.reason = None

    def getheaders(self):
        return self.headers

    def getheader(self, name, default=None):
        return self.headers.get(name, default)


class WsApiClient(ApiClient):

    def __init__(self, configuration=None, header_name=None, header_value=None,
                 cookie=None, pool_threads=1, heartbeat=None):
        super().__init__(configuration, header_name, header_value, cookie, pool_threads)
        self.heartbeat = heartbeat

    async def request(self, method, url, query_params=None, headers=None,
                      post_params=None, body=None, _preload_content=True,
                      _request_timeout=None):

        # Expand command parameter list to indivitual command params
        if query_params:
            new_query_params = []
            for key, value in query_params:
                if key == 'command' and isinstance(value, list):
                    for command in value:
                        new_query_params.append((key, command))
                else:
                    new_query_params.append((key, value))
            query_params = new_query_params

        if headers is None:
            headers = {}
        if 'sec-websocket-protocol' not in headers:
            headers['sec-websocket-protocol'] = 'v4.channel.k8s.io'

        if query_params:
            url += '?' + urlencode(query_params)

        url = get_websocket_url(url)

        if _preload_content:

            resp_all = ''
            async with self.rest_client.pool_manager.ws_connect(url, headers=headers, heartbeat=self.heartbeat) as ws:
                async for msg in ws:
                    msg = msg.data.decode('utf-8')
                    if len(msg) > 1:
                        channel = ord(msg[0])
                        data = msg[1:]
                        if data:
                            if channel in [STDOUT_CHANNEL, STDERR_CHANNEL]:
                                resp_all += data

            return WsResponse(200, resp_all.encode('utf-8'))

        else:

            return await self.rest_client.pool_manager.ws_connect(url, headers=headers, heartbeat=self.heartbeat)
