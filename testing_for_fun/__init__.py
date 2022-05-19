import aiohttp
from argparse import ArgumentParser
import asyncio
from lxml import html
from typing import Iterable


class EmojiPicker:
    SLACKMOJIS = "https://slackmojis.com/emojis/search"

    def __init__(self) -> None:
        pass

    async def pick(self, query: str) -> Iterable[str]:
        results = []
        async with aiohttp.ClientSession() as session:
            async with session.get(self.SLACKMOJIS, params={"query": query}) as resp:
                if resp.status == 200:
                    page = html.document_fromstring(await resp.read())
                    for _, _, link, *_ in page.iterlinks():
                        if link.startswith("https://"):
                            results.append(link)
        return results


async def amain():
    parser = ArgumentParser()
    parser.add_argument("search", type=str)
    args = parser.parse_args()
    results = await EmojiPicker().pick(args.search)
    for result in results:
        print(f"URL: {result}")


def main():
    asyncio.run(amain())
