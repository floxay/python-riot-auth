import asyncio
import sys

import aioconsole
import riot_auth


async def main() -> None:
    CREDS = "USERNAME", "PASSWORD"

    auth = riot_auth.RiotAuth()

    multifactor_status = await auth.authorize(*CREDS)

    while multifactor_status is True:
        # fetching the code must be asynchronous or blocking
        code = await aioconsole.ainput("Input 2fa code: ")
        try:
            await auth.authorize_mfa(code)
            break
        except riot_auth.RiotMultifactorError:
            print("Invalid 2fa code, please try again")

    print(f"Access Token Type: {auth.token_type}\n")
    print(f"Access Token: {auth.access_token}\n")
    print(f"Entitlements Token: {auth.entitlements_token}\n")
    print(f"User ID: {auth.user_id}")

# region asyncio.run() bug workaround for Windows, remove below 3.8 and above 3.10.6
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# endregion

asyncio.run(main())
