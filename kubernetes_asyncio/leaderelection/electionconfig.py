# Copyright 2021 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from collections.abc import Coroutine  # noqa:F401

logging.basicConfig(level=logging.INFO)


class Config:
    # Validate config, exit if an error is detected

    # onstarted_leading and onstopped_leading are defined as coroutines rather
    # than callables in order to faciliate passing context. For example, this
    # allows the ApiClient used by the leader election to be shared and reused.
    def __init__(
        self,
        lock,
        lease_duration,
        renew_deadline,
        retry_period,
        onstarted_leading,  # type: Coroutine
        onstopped_leading=None,  # type: Coroutine | None
    ):
        self.jitter_factor = 1.2

        if lock is None:
            raise ValueError("lock cannot be None")
        self.lock = lock

        if lease_duration <= renew_deadline:
            raise ValueError("lease_duration must be greater than renew_deadline")

        if renew_deadline <= self.jitter_factor * retry_period:
            raise ValueError(
                "renewDeadline must be greater than retry_period*jitter_factor"
            )

        if lease_duration < 1:
            raise ValueError("lease_duration must be greater than one")

        if renew_deadline < 1:
            raise ValueError("renew_deadline must be greater than one")

        if retry_period < 1:
            raise ValueError("retry_period must be greater than one")

        self.lease_duration = lease_duration
        self.renew_deadline = renew_deadline
        self.retry_period = retry_period

        if onstarted_leading is None:
            raise ValueError("callback onstarted_leading cannot be None")
        self.onstarted_leading = onstarted_leading

        self.onstopped_leading = onstopped_leading
