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
from datetime import datetime

from kubernetes_asyncio import client
from kubernetes_asyncio.client.rest import ApiException

from ..leaderelectionrecord import LeaderElectionRecord


class LeaseLock:
    def __init__(self, name, namespace, identity, api_client):
        """
        :param name: name of the lock
        :param namespace: namespace
        :param identity: A unique identifier that the candidate is using
        """
        self.api_instance = client.CoordinationV1Api(api_client=api_client)

        # lease resource identity and reference
        self.name = name
        self.namespace = namespace
        self.lease_reference = None

        # identity of this candidate
        self.identity = str(identity)

    # get returns the election record from a Lease Annotation
    async def get(self, name, namespace):
        """
        :param name: Name of the lease object information to get
        :param namespace: Namespace in which the lease object is to be searched
        :return: 'True, election record' if object found else 'False, exception response'
        """
        try:
            lease = await self.api_instance.read_namespaced_lease(name, namespace)
        except ApiException as e:
            return False, e
        else:
            self.lease_reference = lease
            return True, self.election_record(lease)

    async def create(self, name, namespace, election_record):
        """
        :param electionRecord: Annotation string
        :param name: Name of the lease object to be created
        :param namespace: Namespace in which the lease object is to be created
        :return: 'True' if object is created else 'False' if failed
        """
        body = client.V1Lease(
            metadata={"name": name}, spec=self.update_lease(election_record)
        )

        try:
            await self.api_instance.create_namespaced_lease(
                namespace, body, pretty=True
            )
            return True
        except ApiException:
            logging.exception("Failed to create lock")
            return False

    async def update(self, name, namespace, updated_record):
        """
        :param name: name of the lock to be updated
        :param namespace: namespace the lock is in
        :param updated_record: the updated election record
        :return: True if update is successful False if it fails
        """
        try:
            # update the Lease from the updated record
            self.lease_reference.spec = self.update_lease(
                updated_record, self.lease_reference.spec
            )

            await self.api_instance.replace_namespaced_lease(
                name=name, namespace=namespace, body=self.lease_reference
            )
            return True
        except ApiException:
            logging.exception("Failed to update lock")
            return False

    def update_lease(self, leader_election_record, current_spec=None):
        # existing or new lease?
        spec = current_spec if current_spec else client.V1LeaseSpec()

        # lease configuration
        spec.holder_identity = leader_election_record.holder_identity
        spec.lease_duration_seconds = int(leader_election_record.lease_duration)
        spec.acquire_time = self.time_str_to_iso(leader_election_record.acquire_time)
        spec.renew_time = self.time_str_to_iso(leader_election_record.renew_time)

        return spec

    def election_record(self, lease):
        """
        Get leader election record from Lease spec.
        """
        leader_election_record = LeaderElectionRecord(None, None, None, None)

        if not lease.spec:
            return leader_election_record

        if lease.spec.holder_identity:
            leader_election_record.holder_identity = lease.spec.holder_identity
        if lease.spec.lease_duration_seconds:
            leader_election_record.lease_duration = str(
                lease.spec.lease_duration_seconds
            )
        if lease.spec.acquire_time:
            leader_election_record.acquire_time = str(
                datetime.replace(lease.spec.acquire_time, tzinfo=None)
            )
        if lease.spec.renew_time:
            leader_election_record.renew_time = str(
                datetime.replace(lease.spec.renew_time, tzinfo=None)
            )

        return leader_election_record

    # conversion between kubernetes ISO formatted time and elector record time
    def time_str_to_iso(self, str_time):
        formats = ["%Y-%m-%d %H:%M:%S.%f%z", "%Y-%m-%d %H:%M:%S.%f"]
        for fmt in formats:
            try:
                return datetime.strptime(str_time, fmt).isoformat() + "Z"
            except ValueError:
                pass
        logging.error("Failed to parse time string: %s", str_time)
