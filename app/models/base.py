
from abc import abstractmethod
from typing import List, Dict
from functools import cached_property
from datetime import datetime

from app.spreadsheet_service import SpreadsheetService


class BaseModel:

    SHEET_NAME = None # abstract constant (str) to be set in child class

    COLUMNS = [] # abstract constant to be set in child class

    SEEDS = [] # abstract constant to be set in child class

    ss = SpreadsheetService()

    def __init__(self, attrs:Dict):
        self.attrs = attrs

        # attributes common to all child models
        self.id = attrs.get("id")

        for col in self.COLUMNS:
            #setattr(self, col, self.attrs.get(col))
            val = self.attrs.get(col)
            #if val.startswith("20"):
            # convert datetime parsable string to datetime object, dynamically
            if self.ss.validate_timestamp(val):
                val = self.ss.parse_timestamp(val)
            setattr(self, col, val)


    @property
    def created_at(self):
        return self.ss.parse_timestamp(self.attrs.get("created_at"))

    @property
    def updated_at(self):
        return self.ss.parse_timestamp(self.attrs.get("updated_at"))


    def __iter__(self):
        """Allows you to say dict(obj) to convert the object into a dictionary."""
        yield 'id', self.id
        for col in self.COLUMNS:
            yield col, getattr(self, col)
        yield 'created_at', self.created_at
        yield 'updated_at', self.updated_at

    @property
    def row(self):
        """Returns a list of serializable values, for writing to the sheet."""
        values = []
        values.append(self.id)
        for col in self.COLUMNS:
            val = getattr(self, col)
            if isinstance(val, datetime):
                val = str(val)
            values.append(val)
        values.append(str(self.created_at))
        values.append(str(self.updated_at))
        return values






    @classmethod
    def get_sheet(cls):
       print(f"SHEET ('{cls.SHEET_NAME}')...")
       #return cls.ss.find_or_create_sheet(sheet_name=cls.SHEET_NAME)
       return cls.ss.get_sheet(sheet_name=cls.SHEET_NAME)

    @classmethod
    def find_all(cls, sheet=None):
        #sheet = cls.ss.find_or_create_sheet(sheet_name=cls.SHEET_NAME)
        #sheet = cls.ss.get_sheet(sheet_name=cls.SHEET_NAME) # assumes sheet exists, with the proper headers!
        sheet = sheet or cls.get_sheet() # assumes sheet exists, with the proper headers!
        #return sheet.get_all_records()
        records = sheet.get_all_records()
        return [cls(record) for record in records]

    @classmethod
    def create_records(cls, new_records, records=[]):
        """Appends new records (list of dictionaries) to the sheet.
            Adds auto-incrementing unique identifiers, and timestamp columns.
        """
        sheet = cls.get_sheet() # assumes sheet exists, with the proper headers!

        records = records or cls.find_all(sheet=sheet)
        #next_row_number = len(records) + 2 # plus headers plus one

        # auto-increment integer identifier
        if any(records):
            existing_ids = [r.id for r in records]
            next_id = max(existing_ids) + 1
        else:
            next_id = 1

        rows = []
        for attrs in new_records:
            attrs["id"] = next_id
            now = cls.ss.generate_timestamp()
            attrs["created_at"] = now
            attrs["updated_at"] = now

            inst = cls(attrs)
            rows.append(inst.row)
            next_id += 1

        #return sheet.insert_rows(rows, row=next_row_number)
        return sheet.append_rows(rows)




    @classmethod
    def seed(cls):
        #sheet = cls.ss.find_or_create_sheet(sheet_name=cls.SHEET_NAME)
        #sheet = cls.sheet
        #records = cls.SEEDS
        #breakpoint()
        #values = list(records[0].values()) #> ['Strawberries', 'Juicy organic strawberries.', 4.99, 'https://picsum.photos/id/1080/360/200']
        #sheet.append_rows(values=records)
        #cls.ss.write_to_sheet(sheet_name=cls.SHEET_NAME, records=cls.SEEDS)

        return cls.create_records(cls.SEEDS)





    #def save(self):
    #    print("SAVING RECORD TO SHEET: ____")


    #@property
    #@abstractmethod
    #def seeds() -> List[Dict]:
    #    """To be implemented in child class.
    #        Records to be populated in the sheet.
    #    """
    #    return []


    #@property
    #@classmethod
    #@abstractmethod
    #def sheet_name(self) -> str:
    #    """To be implemented in child class.
    #
    #        Should return the name of the corresponding sheet for this model.
    #
    #        Example:
    #
    #            @property
    #            def sheet_name(self):
    #                return "products"
    #    """
    #    return "todo"

    #@property
    #@abstractmethod
    #def to_row(self) -> List:
    #    """To be implemented in child class.
    #
    #        Should return a list of attributes in the same order as the columns in the corresponding sheet.
    #
    #        Values need to be "serializable", in other words dates and complex objects like dates need to be converted to simple scalar values such as strings.
    #
    #        Example:
    #
    #            @property
    #            def to_row(self):
    #                return [self.id, self.name, self.description, self.price, self.url, str(self.created_at)]
    #
    #    """
    #    return []
