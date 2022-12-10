import os
from datetime import date
from supabase import create_client, Client


class supabaseClient:
    """
    Wrapper around the supabase Client class to abstract away the database commands
    Does some light error checking as well
    """

    empty_item = {
        "item_id": None,
        "expiry": None,
        "comment": "",
    }

    def __init__(self, URL : str, KEY: str):
        self._client = Client = create_client(URL, KEY)
        self._userID = None

    def __del__(self):
        """
        Cleans up after client
        """
        self._client.auth.sign_out()

    def signIn(self, email : str, passwd : str):
        """
        Log into existing User
        """
        session = self._client.auth.sign_in(email=email, password=passwd)
        if session: 
            print(self._client.supabase_key)
            self._userID = session.user.id
            self._client.postgrest.auth(session.access_token)
            print(self._client.supabase_key)

    def signUp(self, email : str, passwd : str):
        """
        Create new User
        """
        self._user = self._client.auth.sign_up(email=email, password=passwd)

    def getItemID(self, barcode : int) -> str:
        """
        Get the Item ID from DB by barcode
        """
        itemID = None
        command = self._client.table("items").select("*").eq('barcode', barcode)
        data = command.execute()
        if len(data.data) > 0:
            response = data.data[0]
            itemID = response['item_id']

        return itemID

    def getItems(self):
        """
        Gets all of the user's items
        """
        command = self._client.table("inventory").select("*")
        data = command.execute()

        print(data.data)

        #print(self._client.auth.user())

        return True
    
    def sendItem(self, itemID: str, expiry : date = None, comment : str = "")  -> bool:
        """
        Sends item to the DB
        """
        item = {
            "item_id": itemID,
            "expiry": expiry,
            "comment": comment,
        }

        command = self._client.table("inventory").insert(item)
        data = command.execute()

        print(data.data)

        return True

    def removeItem(self, itemID: str, expiry : date = None) -> bool:
        """
        Removes an item from the DB
        """
        True

    def getBarcode(self, item: str) -> str:
        """
        Get the Barcode based on the item's ID
        """
        barcode_id = None
SUPABASE_KEY
        return barcode_id

    def getUserID(self) -> str:
        return "ID"


if __name__ == "__main__":
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    sbClient = supabaseClient(url, key)

    email = "test@smartfridge.co.uk"
    passwd = "SmartFridge"
    sbClient.signIn(email,passwd)


    print("hello")
    barcode = 5018306330719
    item = sbClient.getItemID(barcode)

    print(item)

    sbClient.getItems()
    response = sbClient.sendItem(itemID=item)

    del sbClient
