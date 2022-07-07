# riot-auth

The goal of this project is to bypass Cloudflare's filters (403, error code: 1020).\
To do this TLS 1.3 cipher suites and signature algorithms are set via ctypes using Python's bundled libssl.\
Currently HTTP/2 is not used as it does not appear to be an issue, ...and aiohttp does not support it.


## Installation
 - `$ pip install git+https://github.com/floxay/python-riot-auth.git`

## Examples
 - Example(s) can be found in the examples folder.
