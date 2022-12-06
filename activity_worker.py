from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

import activity_definition as ad


async def start_activity_worker(client: Client, task_queue_name):
    # Create a worker that hosts only activity implementation

    print(f"start_activity_worker starting, task_queue: {task_queue_name}")

    worker = Worker(
        client,
        task_queue=task_queue_name,
        activities=[ad.RestActivity],
    )
    print("start_activity_worker worker created")

    await worker.run()

    print("start_activity_worker complete")
