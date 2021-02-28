'''
    key takeaways:  
        define an async function\coroutine using 'async'
        'await' blocking lines in a coroutine to give ctl back to loop 

'''

import asyncio
import logging
import re
import sys
from typing import IO
import urllib.error
import urllib.parse


import aiofiles
# not using requests package because socket operations block and not awaitable
import aiohttp
from aiohttp import ClientSession

# pseudo code
# read URLs from a local file
# send GET requests to URLs and decode content
# search result href tags
# write the results to a file

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)

# create new logger instance
logger=logging.getLogger('areq')
logging.getLogger("chardet.charsetprober").disabled = True

#create a pattern for searching for href tags
HREF_RE=re.compile(r'href="(.*?)"')

# create async wrapper around get requests
async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    # call session request, return ctl to event handler while waiting
    resp=await session.request(method='GET',url=url, **kwargs)
    # will block this particular function, but not the outer event loop
    resp.raise_for_status() # error handling
    logger.info(f'Got response {resp.status} for URL: {url}')
    # get response in unicode format
    html=await resp.text()
    return html

async def parse(url: str, session: ClientSession, **kwargs) -> set:
    # find HREFs in the HTML of url
    found=set()
    try:
        html=await fetch_html(url=url, session=session, **kwargs)
    except (
        aiohttp.ClientError,
        aiohttp.http_exceptions.HttpProcessingError,
    ) as e:
        logger.error(f'aiohttp exception for {getattr(e,'status',None)}: {getattr(e,'message',None)}') 
        return found
    except Exception as e:
        logger.exception('Non-aiohttp exception occured: %s',getattr(e, "__dict__", {}))
        return found
    # another operation that can raise an exception
    else:
        for link in HREF_RE.findall(html):
            try:
                abslink=urllib.parse.urljoin(url,link)
            except (urllib.error.URLError,ValueError):
                logger.exception(f'Error parsing URL: {link}')
                pass
            else:
                found.add(abslink)
        logger.info(f'Found {len(found)} links for {url}')
        return found

async def write_one(file: IO, url: str, **kwargs) -> None:
    # write the HREFs from 'url' to 'file'
    res=await parse(url=url,**kwargs)
    if not res:
        return None
    async with aiofiles.open(file,'a') as f:
        for p in res:
            await f.write(f'{url}\t{p}\n')
        logger.info(f'Wrote resutls for source URL: {url}')

async def bulk_crawl_and_write(file: IO, urls: set, **kwargs) -> None:
    # crawl and write concurrently to 'file' for multiple 'urls'
    # use 'async with' context manager in case opening the session blocks
    # can only use 'async with' in coroutine function bodies 
    async with ClientSession() as session:
        tasks=[]
        for url in urls:
            tasks.append(
                write_one(file=file, url=url, session=session, **kwargs)
            )
        # schedules and run tasks in current event loop
        await asyncio.gather(*tasks)

if __name__=='__main__':
    import pathlib
    import sys

    # check for version 3.7
    assert sys.version_info >= (3,7),
    here=pathlib.Path(__file__).parent

    # get urls from a text file
    with open(here.joinpath('urls.txt')) as infile:
        # return a set of urls after removing whitespaces
        urls=set(map(str.strip, infile))
    
    # initialize output fle
    outpath=here.joinpath('foundurls.txt')
    with open(output,'w') as outfile:
        outfile.write('source_url \t parsed_url \n')

    # launch primary event loop using 'run'
    asyncio.run(bulk_crawl_and_write(file=output,urls=urls))
