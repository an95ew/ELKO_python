import asyncio
import aiohttp

urls = ['https://overcoder.net/q/1508487/ошибка-flask-sqlalchemy-ошибка-типа-несовместимый-тип-коллекции-модель-не',
       'https://github.com/igortereshchenko/orm/blob/master/orm_many_to_many.py',
       'https://github.com/an95ew/data_retriever_bot/blob/master/utils/db_api/postgresql.py']


async def get_info(url):
    pass

    # PLACE FOR ANY LOGIC CODE
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            print(url, 'is parsing')
            response = await aiohttp.request('get', url)
            data = await response.text()

    print(len(data), "is loaded")


containers = [get_info(url) for url in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(containers))