from app.aiorequests import get, post
from app.aio_asf import AioAsf


#debug
url='https://novanoir.cn'
import asyncio
loop = asyncio.get_event_loop()

async def getr():
    text = await get(url=url)
    await asyncio.sleep(10)
    text = await text.text
    print(text)

loop.run_until_complete(getr())
print('okay')
import time
time.sleep(3)
print('another kjay')