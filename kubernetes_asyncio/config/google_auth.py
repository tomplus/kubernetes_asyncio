import asyncio.subprocess
import json
import shlex
from types import SimpleNamespace


async def google_auth_credentials(provider):

    if 'cmd-path' not in provider or 'cmd-args' not in provider:
        raise ValueError('GoogleAuth via gcloud is supported! Values for cmd-path, cmd-args are required.')

    cmd = shlex.split(' '.join((provider['cmd-path'], provider['cmd-args'])))
    cmd_exec = asyncio.create_subprocess_exec(*cmd,
                                              stdin=None,
                                              stdout=asyncio.subprocess.PIPE,
                                              stderr=asyncio.subprocess.PIPE)
    proc = await cmd_exec

    data = await proc.stdout.read()
    data = data.decode('ascii').rstrip()
    data = json.loads(data)

    await proc.wait()
    return SimpleNamespace(
        token=data['credential']['access_token'],
        expiry=data['credential']['token_expiry']
    )
