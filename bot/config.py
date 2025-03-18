import os
from dotenv import load_dotenv

load_dotenv()

infura_url = os.getenv("INFURA_URL")
etherscan_api_key = os.getenv("ETHERSCAN_API_KEY")
graph_API_KEY = os.getenv("graph_API_KEY")
botbundler_token = os.getenv("baxbot")
GRAPHQL_URL = os.getenv("GRAPHQL_URL")
MORALIS_API_KEY=os.getenv("MORALIS_API_KEY")