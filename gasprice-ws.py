import asyncio
import os
import time
from datetime import datetime

from websockets import connect

WS_URL = 'wss://www.gasnow.org/ws'
DURATION = 15 * 60 # 15 minutes

async def main() -> None:
  start_time = time.time()
  month = datetime.utcnow().isoformat()[:7]
  output_file = open(os.path.join('data', f'{month}.json'), "a")
  async with connect(WS_URL) as websocket:
    while time.time() <= start_time + DURATION:
      response = await websocket.recv()
      output_file.write(response + "\n")
    output_file.close()

if __name__ == "__main__":
  asyncio.run(main())
