import aiohttp

async def get_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data:
                    return data[0]['url']
                else:
                    return None
            else:
                return None
