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

import asyncio
import os
import uuid

from kubernetes_asyncio import config
from kubernetes_asyncio.client import api_client
from kubernetes_asyncio.leaderelection import electionconfig, leaderelection
from kubernetes_asyncio.leaderelection.resourcelock.leaselock import LeaseLock


async def main():

    # Authenticate using config file
    await config.load_kube_config(config_file=os.environ.get("KUBECONFIG", ""))

    # Parameters required from the user

    # A unique identifier for this candidate
    candidate_id = uuid.uuid4()

    # Name of the lock object to be created
    lock_name = "examplepython"

    # Kubernetes namespace
    lock_namespace = "default"

    # The function that a user wants to run once a candidate is elected as a
    # leader. Cancellation is supported (when a held leader lock is lost).
    async def example_start_func():
        try:
            print("I am leader")
        except asyncio.CancelledError:
            print(
                "Start function cancelled - lost leader election after becoming leader"
            )

    async def example_end_func():
        print("I am no longer leader")

    # A user can choose not to provide any callbacks for what to do when a candidate fails to lead - onStoppedLeading()
    # In that case, a default callback function will be used

    async with api_client.ApiClient() as apic:
        # Create config
        leader_election_config = electionconfig.Config(
            # A legacy ConfigMapLock is also available
            LeaseLock(lock_name, lock_namespace, candidate_id, apic),
            lease_duration=17,
            renew_deadline=15,
            retry_period=5,
            onstarted_leading=example_start_func,
            onstopped_leading=example_end_func,
        )

        # Enter leader election
        await leaderelection.LeaderElection(leader_election_config).run()
        # User can choose to do another round of election or simply exit
        print("Exited leader election")


if __name__ == "__main__":
    asyncio.run(main())
