class BaseError(Exception):
    """Base pacakge error."""


class InvalidModelInputError(BaseError):
    """Model input contains an error."""
