class Client:
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