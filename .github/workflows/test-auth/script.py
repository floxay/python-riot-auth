import asyncio
import os

import riot_auth


USERNAME = os.getenv("RIOT_USERNAME")
assert USERNAME
PASSWORD = os.getenv("RIOT_PASSWORD")
assert PASSWORD

auth = riot_auth.RiotAuth()
asyncio.run(auth.authorize(username=USERNAME, password=PASSWORD))
assert auth.user_id
