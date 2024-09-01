# riot-auth

![auth test workflow](https://github.com/floxay/python-riot-auth/actions/workflows/test-auth.yml/badge.svg?branch=main)

The goal of this project is to bypass Cloudflare's filters (403, error code: 1020).  
To do this TLS 1.3 cipher suites and signature algorithms are set via ctypes using Python's bundled libssl in `RiotAuth.create_riot_auth_ssl_ctx()`.  
Currently HTTP/2 is not being used as HTTP/1.1 does not appear to be an issue, ...and aiohttp does not support it.

## Installation
 - `$ pip install git+https://github.com/floxay/python-riot-auth.git`

## Examples
 - Example(s) can be found in the examples folder.
