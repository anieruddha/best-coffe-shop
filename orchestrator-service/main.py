import asyncio
from temporalio.worker import Worker
from temporalio.client import Client
from workflow import CoffeeOrderWorkflow
from temporal_config import TEMPORAL_ADDRESS, TASK_QUEUE


async def main():
    print(TEMPORAL_ADDRESS)
    client = await Client.connect(TEMPORAL_ADDRESS)
    worker = Worker(
        client,
        task_queue=TASK_QUEUE,
        workflows=[
            CoffeeOrderWorkflow
        ],
    )
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())