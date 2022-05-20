import aiohttp
from argparse import ArgumentParser
import asyncio
import logging
from lxml import html
from typing import Iterable

FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class EmojiPicker:
    SLACKMOJIS = "https://slackmojis.com/emojis/search"

    def __init__(self) -> None:
        pass

    async def pick(self, query: str) -> Iterable[str]:
        results = []
        async with aiohttp.ClientSession() as session:
            resp = await session.get(self.SLACKMOJIS, params={"query": query})
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
        log.info(f"URL: {result}")


def main():
    asyncio.run(amain())
