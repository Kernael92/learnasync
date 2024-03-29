import asyncio 
from quart import Quart 

app = Quart(__name__)

async def count():
    print("one")
    await asyncio.sleep(1) 
    # asyncio.sleep() is used to stand in for a non-blocking call(but one that also takes some time to complete)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time 
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s 
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")