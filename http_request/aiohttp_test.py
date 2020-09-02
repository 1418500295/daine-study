import aiohttp
import asyncio

async def post_03():
    async with aiohttp.ClientSession() as client:
        resp = await client.post("http://localhost:8889/postSecond",data={
            "name":"daine",
            "sex":"male"
        })
        result = await resp.json()
        print(result)

asyncio.run(post_03())


# aiohttp 的代码与 httpx 异步模式的代码重合度90%，只不过把AsyncClient换成了ClientSession
# ，另外，在使用 httpx 时，当你await client.post时就已经发送了请求。
# 但是当使用aiohttp时，只有在awiat resp.json() 时才会真正发送请求。

if __name__ == '__main__':
    a = "我是发生过都很好"
    import re
