import httpx
import asyncio
import aiohttp

# 同步请求
def post_01():
    b = {
        "name": "daine",
        "sex": "male"
    }
    print(httpx.post("http://localhost:8889/postSecond", data=b).json())

# 异步请求
async def main():
    c = {
        "name":"daine",
        "sex":"male"
    }
    async with httpx.AsyncClient() as client:
        res = await client.post("http://localhost:8889/postSecond", data=c)
        result = res.json()
        print(result)



asyncio.run(main())
post_01()
