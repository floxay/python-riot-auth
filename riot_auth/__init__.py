__version__ = "1.0.6"

from .auth import (
    RiotAuth,
    RiotAuthenticationError,
    RiotAuthError,
    RiotMultifactorError,
    RiotRatelimitError,
    RiotUnknownErrorTypeError,
    RiotUnknownResponseTypeError,
)

__all__ = (
    "RiotAuth",
    "RiotAuthenticationError",
    "RiotAuthError",
    "RiotMultifactorError",
    "RiotRatelimitError",
    "RiotUnknownErrorTypeError",
    "RiotUnknownResponseTypeError",
)
