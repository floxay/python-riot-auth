# riot-auth Copyright (c) 2022 Huba Tuba (floxay)
# Licensed under the MIT license. Refer to the LICENSE file in the project root for more information.

__all__ = (
    "RiotAuthenticationError",
    "RiotAuthError",
    "RiotMultifactorError",
    "RiotRatelimitError",
    "RiotUnknownErrorTypeError",
    "RiotUnknownResponseTypeError",
)


class RiotAuthError(Exception):
    """Base class for RiotAuth errors."""


class RiotAuthenticationError(RiotAuthError):
    """Failed to authenticate."""


class RiotRatelimitError(RiotAuthError):
    """Ratelimit error."""


class RiotMultifactorAttemptError(RiotAuthError):
    """Multi-factor attempt failed."""


class RiotUnknownResponseTypeError(RiotAuthError):
    """Unknown response type."""


class RiotUnknownErrorTypeError(RiotAuthError):
    """Unknown response error type."""
