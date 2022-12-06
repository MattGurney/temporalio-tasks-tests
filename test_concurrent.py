import uuid
import asyncio
import time
import pytest
import activity_worker as aw
import workflow_worker as ww
from temporalio.client import WorkflowFailureError


@pytest.mark.asyncio
async def test_asyncio(client):
    workflow_task_queue_name = str(uuid.uuid4())
    activity_task_queue_name = str(uuid.uuid4())

    async def start_workflow_worker(client, workflow_task_queue_name):
        await ww.start_workflow_worker(client, workflow_task_queue_name)

    async def start_activity_worker(client, activity_task_queue_name):
        await aw.start_activity_worker(client, activity_task_queue_name)

    async def trigger_workflow(client, workflow_task_queue_name):
        print("")
        print(f"trigger_workflow starting: {workflow_task_queue_name}")

        handle = await client.start_workflow(
            ww.TestWorkflow.run,
            "Hello World",
            id=str(uuid.uuid4()),
            task_queue=workflow_task_queue_name,
        )

        print(f"trigger_workflow completed: {workflow_task_queue_name}")

        try:
            return await handle.result()
        except WorkflowFailureError as e:
            print(f"trigger_workflow failed: {workflow_task_queue_name}, e.cause: {e.cause}")
            raise e
        except Exception as e:
            print(f"trigger_workflow exception: {e}, e.cause: {e.cause}")
            raise e

    async def main():
        print("")

        print("about to asyncio.create_task(start_workflow_worker)")
        workflow_worker_task = asyncio.create_task(
            start_workflow_worker(client, workflow_task_queue_name)
        )

        print("about to asyncio.create_task(start_activity_worker)")
        activity_worker_task = asyncio.create_task(
            start_activity_worker(client, activity_task_queue_name)
        )

        sleep_time = 2
        print(f"sleeping for {sleep_time} seconds")
        await asyncio.sleep(sleep_time)
        print("sleep complete")

        print("about to trigger_workflow")
        await trigger_workflow(client, workflow_task_queue_name)

    await main()
