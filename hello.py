"""
This module description would be similar to the class description
"""

class MyClass:
    """
    Class Description
    """
    data_member_1: str
    data_member_2: str

    def __init__(self, data_member_1: str = None, data_member_2: str = None) -> None:
        """
        Class Initialization Function. Gets called when the object is created

        Parameters
        ----------
        data_member_1 (str) : Parameter Description
        data_member_2 (str) : Parameter Description

        Raises
        ------
        ValueError
            If the value of data_member_1 is None

        """
        if self.data_member_1 is None and self.data_member_2 is None:
            raise ValueError("data_member_1 and data_member_2 cannot be None")

        self.data_member_1 = data_member_1
        self.data_member_2 = data_member_2

    def __dict__(self) -> dict:
        """
        Dictionary format of the class

        Returns
        -------
        dict : The object in its JSON format

        """
        return {
            "data_member_1": self.data_member_1,
            "data_member_2": self.data_member_2
        }

    def __eq__(self, another_object: MyClass) -> bool:
        """
        Checking equality between two objects of MyClass

        Parameters
        ----------
        another_object (MyClass) : Parameter Description

        Returns
        -------
        bool : Whether the compared objects are same

        """
        are_objects_equal = True
        my_dict = dict(self)
        another_object_dict = dict(another_object)

        for key in my_dict:
            if my_dict[key] != another_object_dict[key]:
                are_objects_equal = False
                break

        return are_objects_equal
