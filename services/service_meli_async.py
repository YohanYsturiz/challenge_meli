import asyncio
from aiohttp import ClientSession


async def get_character(session, url: str) -> str:
    response = await session.get(url)
    character = await response.json
    return character['name']


async def main(self):
    async with ClientSession() as session:
        tasks = []
        for number in range(1, 4):
            url = self.endpoint + self.path
            tasks.append(asyncio.create_task(get_character(session, url=url)))

        response = await asyncio.gather(*tasks)
        print(response)

asyncio.run(main())