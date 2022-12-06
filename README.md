# Test out temporalio tests for python

### Run

```
pytest -s test_concurrent.py
```

### Error

```
% pytest -s test_concurrent.py
============================================================= test session starts ==============================================================
platform darwin -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/mattgurney/projects/temporalio-tasks-tests
plugins: asyncio-0.20.2
asyncio: mode=Mode.STRICT
collected 1 item

test_concurrent.py
about to asyncio.create_task(start_workflow_worker)
about to asyncio.create_task(start_activity_worker)
sleeping for 2 seconds
start_workflow_worker starting, task_queue: f153e730-fcbb-4595-8955-ff3576f96674
start_workflow_worker worker created
start_activity_worker starting, task_queue: 7929913c-fee9-4f55-a0a6-d49fbd6dc51e
start_activity_worker worker created
sleep complete
about to trigger_workflow

trigger_workflow starting: f153e730-fcbb-4595-8955-ff3576f96674
trigger_workflow completed: f153e730-fcbb-4595-8955-ff3576f96674
Running workflow with parameter Hello World
trigger_workflow failed: f153e730-fcbb-4595-8955-ff3576f96674, e.cause: Activity task timed out
F2022-12-06T23:26:06.847+1100   ERROR   Error looking up host for shardID       {"component": "shard-controller", "address": "127.0.0.1:59850", "error": "Not enough hosts to serve the request", "operation-result": "OperationFailed", "shard-id": 1, "logging-call-at": "controller_impl.go:342"}
go.temporal.io/server/common/log.(*zapLogger).Error
        /home/runner/go/pkg/mod/go.temporal.io/server@v1.18.0/common/log/zap_logger.go:143
go.temporal.io/server/service/history/shard.(*ControllerImpl).acquireShards.func1
        /home/runner/go/pkg/mod/go.temporal.io/server@v1.18.0/service/history/shard/controller_impl.go:342
go.temporal.io/server/service/history/shard.(*ControllerImpl).acquireShards.func2
        /home/runner/go/pkg/mod/go.temporal.io/server@v1.18.0/service/history/shard/controller_impl.go:376
2022-12-06T23:26:06.862+1100    ERROR   Failed to complete timer task   {"shard-id": 1, "address": "127.0.0.1:59850", "component": "timer-queue-processor", "error": "shard closed", "logging-call-at": "timerQueueProcessor.go:302"}
go.temporal.io/server/common/log.(*zapLogger).Error
        /home/runner/go/pkg/mod/go.temporal.io/server@v1.18.0/common/log/zap_logger.go:143
go.temporal.io/server/service/history.(*timerQueueProcessorImpl).completeTimersLoop
        /home/runner/go/pkg/mod/go.temporal.io/server@v1.18.0/service/history/timerQueueProcessor.go:302
All services are stopped.


=================================================================== FAILURES ===================================================================
_________________________________________________________________ test_asyncio _________________________________________________________________
temporalio.exceptions.TimeoutError: activity ScheduleToStart timeout
...
>                   raise WorkflowFailureError(
                        cause=await self._client.data_converter.decode_failure(
                            fail_attr.failure
                        ),
E                       temporalio.client.WorkflowFailureError: Workflow execution failed

../../opt/anaconda3/envs/temporalio-tasks-tests/lib/python3.11/site-packages/temporalio/client.py:894: WorkflowFailureError
=========================================================== short test summary info ============================================================
FAILED test_concurrent.py::test_asyncio - temporalio.client.WorkflowFailureError: Workflow execution failed
============================================================== 1 failed in 12.48s ==============================================================
```
