try:
    from config import load_config
except Exception as e:
    print("Config failed:", e)

import asyncio

async def dummy_life():
    while True:
        print("Bot holding process...")
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(dummy_life())
