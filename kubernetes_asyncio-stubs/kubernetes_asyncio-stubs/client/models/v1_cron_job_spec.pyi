import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CronJobSpec:
    concurrency_policy: typing.Optional[str]
    failed_jobs_history_limit: typing.Optional[int]
    job_template: kubernetes_asyncio.client.V1JobTemplateSpec
    schedule: str
    starting_deadline_seconds: typing.Optional[int]
    successful_jobs_history_limit: typing.Optional[int]
    suspend: typing.Optional[bool]
    time_zone: typing.Optional[str]
    
    def __init__(self, *, concurrency_policy: typing.Optional[str] = ..., failed_jobs_history_limit: typing.Optional[int] = ..., job_template: kubernetes_asyncio.client.V1JobTemplateSpec, schedule: str, starting_deadline_seconds: typing.Optional[int] = ..., successful_jobs_history_limit: typing.Optional[int] = ..., suspend: typing.Optional[bool] = ..., time_zone: typing.Optional[str] = ...) -> None:
        ...
    def to_dict(self) -> V1CronJobSpecDict:
        ...
class V1CronJobSpecDict(typing.TypedDict, total=False):
    concurrencyPolicy: typing.Optional[str]
    failedJobsHistoryLimit: typing.Optional[int]
    jobTemplate: kubernetes_asyncio.client.V1JobTemplateSpecDict
    schedule: str
    startingDeadlineSeconds: typing.Optional[int]
    successfulJobsHistoryLimit: typing.Optional[int]
    suspend: typing.Optional[bool]
    timeZone: typing.Optional[str]
