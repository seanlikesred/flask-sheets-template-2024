
from abc import abstractmethod
from typing import List, Dict

#from app.services.sheets_service import SpreadsheetService

class BaseModel:

    def __init__(self, attrs:Dict):
        self.attrs = attrs

    @abstractmethod
    @property
    def sheet_name(self) -> str:
        """To be implemented in child class.

            Should return the name of the corresponding sheet for this model.


            Example:

                @property
                def sheet_name(self):
                    return "products"
        """
        return "todo"

    @abstractmethod
    @property
    def to_row(self) -> List:
        """To be implemented in child class.

            Should return a list of attributes in the same order as the columns in the corresponding sheet.

            Values need to be "serializable", in other words dates and complex objects like dates need to be converted to simple scalar values such as strings.

            Example:

                @property
                def to_row(self):
                    return [self.id, self.name, self.description, self.price, self.url, str(self.created_at)]

        """
        return []


    #def save(self):
    #    print("SAVING RECORD TO SHEET: ____")
