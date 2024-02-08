import telegraph as tg
from .. import BOT_USERNAME,LOGGER

telegraph = None
if telegraph == None:
    client = tg.Telegraph(domain="graph.org")
    telegraph = client.create_account(short_name=BOT_USERNAME, author_name=BOT_USERNAME)
    access_token = telegraph["access_token"]
    LOGGER.info("Telegraph account created")

async def upload(file_path):
    if access_token is None or file_path is None:
        return
    
    client = tg.Telegraph(access_token=access_token, domain="graph.org")
    with open(file_path, "rb") as file:
        response = client.upload_file(file)

    return await modify(response[0]["src"])


async def modify(resp):
    domains = ['telegra.ph', "graph.org"]
    return ["https://" + domain + resp for domain in domains]