import os
import random
import asyncio
import aiohttp


async def download_image(session, url, folder):
    async with session.get(url) as response:
        if response.status == 200:
            filename = os.path.basename(url).split('=')[-1]
            filepath = os.path.join(folder, filename)
            with open(filepath, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
            print(f"Downloaded {filename}")
        else:
            print(f"Failed to download {url}: status {response.status}")

async def download_images(amount, folder):
    urls = [f"https://picsum.photos/200/300?random={random.randint(1, 1000)}.jpg" for _ in range(amount)]
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url, folder) for url in urls]
        await asyncio.gather(*tasks)

async def main():
    amount = int(input("Enter the number of images to download: "))
    folder = input("Enter the folder to save the images: ")

    if not os.path.exists(folder):
        os.makedirs(folder)

    await download_images(amount, folder)
    await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
