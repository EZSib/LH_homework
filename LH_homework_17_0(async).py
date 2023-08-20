import  asyncio
import time

async def hello():
    print('hello')
    await asyncio.sleep(3)
    print('bye')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(hello(), hello()))