from datetime import timedelta

from temporalio import workflow
from temporalio.client import Client
from temporalio.worker import Worker
from temporalio.common import RetryPolicy


# Basic workflow that logs and invokes an activity
@workflow.defn
class TestWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        print("Running workflow with parameter %s" % name)
        return await workflow.execute_activity(
            "RestActivity",
            name,
            start_to_close_timeout=timedelta(seconds=10),
            schedule_to_start_timeout=timedelta(seconds=10),
            schedule_to_close_timeout=timedelta(seconds=10),
            retry_policy=RetryPolicy(maximum_attempts=1),  # Don't retry tests
            task_queue="my-activity-task-queue",
        )


async def start_workflow_worker(client: Client, task_queue_name: str):
    # Create a worker that hosts only workflow implementation
    print(f"start_workflow_worker starting, task_queue: {task_queue_name}")

    worker = Worker(
        client,
        task_queue=task_queue_name,
        workflows=[TestWorkflow],
    )
    print("start_workflow_worker worker created")

    await worker.run()

    print("start_workflow_worker complete")
