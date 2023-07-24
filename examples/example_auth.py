import asyncio
import sys

import riot_auth

# region asyncio.run() bug workaround for Windows, remove below 3.8 and above 3.10.6
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# endregion

CREDS = "USERNAME", "PASSWORD"

auth = riot_auth.RiotAuth()
asyncio.run(auth.authorize(*CREDS))

# Note: if you have 2FA enabled, these will be None (see "example_auth_with_2fa_enabled.py"):
print(f"Access Token Type: {auth.token_type}\n")
print(f"Access Token: {auth.access_token}\n")
print(f"Entitlements Token: {auth.entitlements_token}\n")
print(f"User ID: {auth.user_id}")

# Reauth using cookies. Returns a bool indicating whether the reauth attempt was successful.
asyncio.run(auth.reauthorize())
