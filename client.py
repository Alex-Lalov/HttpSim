class Client:
    """
    A class to create clients

    Attributes
    ----------
    id : str
        a string containing the id/name of a client
    password : str
        the pass or secret that is used

    Methods
    -------
    __eq__(self, other)
        Overloads the equivelance of the class
    getClientData(self)
        Returns client json data
    """
    def __init__(self, id : str, password : str):
        # Client's authentication data
        self.__client_data = {
            "client_id": id,
            "client_pass": password
        }
    
    def __eq__(self, other):
        if self.__client_data["client_id"] == other.__client_data["client_id"]:
            if self.__client_data["client_pass"] == other.__client_data["client_pass"]:
                return True
        return False
    
    def getClientData(self):
        return self.__client_data