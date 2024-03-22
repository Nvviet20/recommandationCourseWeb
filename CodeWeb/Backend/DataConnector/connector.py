from neo4j import GraphDatabase


DEFAULT_URI= "neo4j+s://73f9a4e9.databases.neo4j.io:7687"  #bolt://localhost:7687
DEFAULT_USERNAME= "neo4j" 
DEFAULT_PASSWORD= "XtvZQ_Fof-5SAkwa2eCEYQVNsTJ3xSqOaMM_X4D4fx8" #12345678


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnector(metaclass=SingletonMeta):


    def __init__(self, uri=DEFAULT_URI, username= DEFAULT_USERNAME, password= DEFAULT_PASSWORD):
        self.uri = uri
        self.username = username
        self.password = password

    
    def getConnection(self):
        return GraphDatabase.driver(self.uri, auth=(self.username, self.password))
    

