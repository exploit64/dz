import random
import asyncio
from asyncio import Condition, Lock, sleep

warehouse = []
max_elements = 10
warehouse_lock = Lock()
overflow_condition = Condition()
underflow_condition = Condition()


async def is_overflow():
    return len(warehouse) >= max_elements


async def is_underflow():
    return len(warehouse) == 0


async def producer(id):
    while True:
        x = random.randint(a=1, b=10000)
        print('Thread {} produced number {}'.format(id, x))
        if not await is_overflow():
            async with warehouse_lock:
                warehouse.append(x)
                async with underflow_condition:
                    underflow_condition.notify()
        else:
            async with overflow_condition:
                print("Overflow. Producer {} waiting".format(id))
                await overflow_condition.wait()
        await sleep(random.random() * 5.0)


async def consumer(id):
    while True:
        if not await is_underflow():
            async with warehouse_lock:
                print('Thread {} consumed number {}'.format(id, warehouse.pop(0)))
                async with overflow_condition:
                    overflow_condition.notify()
        else:
            async with underflow_condition:
                print("Underflow. Consumer {} waiting".format(id))
                await underflow_condition.wait()
        await sleep(random.random() * 2.0)


tasks = []
asio = asyncio.get_event_loop()
for i in range(2):
    tasks.append(asio.create_task(producer(i)))
for i in range(10):
    tasks.append(asio.create_task(consumer(i)))

asio.run_until_complete(asyncio.wait(tasks))
asio.close()
