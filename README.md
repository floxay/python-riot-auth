# riot-auth

The goal of this project is to bypass Cloudflare's filters (403, error code: 1020).  
To do this TLS 1.3 cipher suites and signature algorithms are set via ctypes using Python's bundled libssl in `RiotAuth.create_riot_auth_ssl_ctx()`.  
Currently HTTP/2 is not being used as HTTP/1.1 does not appear to be an issue, ...and aiohttp does not support it.

# I will NOT be updating the User Agent anymore.
The class variable can be modified at runtime like this:
```py
from riot_auth import RiotAuth

RiotAuth.RIOT_CLIENT_USER_AGENT = "UPDATED USER AGENT STRING GOES HERE"
```
The format of the string can be found here;
https://github.com/floxay/python-riot-auth/blob/ec615cdb75eb639016d16770ea8eb8fd61ddb0a1/riot_auth/auth.py#L35
**The value set should match this format otherwise you will get TypeError exceptions.**

If you have no idea how to update it;  
Currently [Officer's Valorant-API](https://dash.valorant-api.com/) can be used to get the Riot Client version, use the [/version](https://valorant-api.com/v1/version) endpoint and look for the `riotClientBuild` key in the response.
With this you can create a task/simple function that updates the `RIOT_CLIENT_USER_AGENT` class variable.

***I will not help with coding such system/script and any issues asking for help regarding this will be closed.  
Issues due to outdated/blacklisted user agent values will also be closed.***

## Installation
 - `$ pip install git+https://github.com/floxay/python-riot-auth.git`

## Examples
 - Example(s) can be found in the examples folder.
