
from datetime import datetime, timezone


class DateParser:
    """Mixin for date parsing / interfacing with google sheets date formatting."""


    @staticmethod
    def generate_timestamp():
        """Generates a new timestamp of the current time in UTC timezone.
            Returns a datetime object.
        """
        return datetime.now(tz=timezone.utc)


    @staticmethod
    def parse_timestamp(ts:str):
        """Converts a timestamp string to a datetime object.

            Params:
                ts (str) : a timestamp string in format provided by google sheets

            Example: SpreadsheetService.parse_timestamp('2023-03-08 19:59:16.471152+00:00')

            Returns a datetime object.
        """
        if isinstance(ts, datetime):
            return ts
        elif isinstance(ts, str):
            date_format = "%Y-%m-%d %H:%M:%S.%f%z"
            return datetime.strptime(ts, date_format)
        #else:
        #    # something went wrong! use original value. consider raising error
        #    return ts
