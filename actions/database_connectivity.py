#import mysql.connector
import logging
#import pandas as pd
#from .connections import LOGGER_FORMAT, root


class DBConnection:

    def __init__(self):
        """ Constructor """
        self.log = logging.getLogger(self.__class__.__name__)
        file_handler = logging.FileHandler(f'{self.__class__.__name__}.log')
        formatter = logging.Formatter(LOGGER_FORMAT)
        file_handler.setFormatter(formatter)
        self.log.addHandler(file_handler)
        try:
            self.db = mysql.connector.connect(host="localhost", user="root", passwd=root,
                                              database="rasa_travellers_db",auth_plugin='mysql_native_password')
            self.cursor = self.db.cursor()
        except Exception as e:
            self.log.error(f"DB connection Failed.\nError {e}")

    def execute_query(self, query):
        """
        Excecute the MYSQL query with the help of the cursor
        :param query: Input query
        :return: None
        """
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            self.log.error(f"{query} Failed.\nError {e}")

    def add_travellers_info(self,  name, phone_number):
        """
        Adds new travellers information to the database

        :param phone_number: Phone number
        :param name: Name to call the travellers

        :return: None
        """
        query = f"""INSERT INTO travel (name, phone_number) 
                    VALUES ("{name}","{phone_number}");"""
        self.execute_query(query)





