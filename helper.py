from requests_html import AsyncHTMLSession


def multi_request(urls, headers=None):
    if len(urls) == 0:
        return []
    if headers is None:
        headers = {}
    session = AsyncHTMLSession()

    scrape_fns= []
    for url in urls:
        async def get_site_content(url=url):
            return await session.get(url, headers=headers)

        scrape_fns.append(get_site_content)

    results = session.run(*scrape_fns)
    session.close()

    return results
