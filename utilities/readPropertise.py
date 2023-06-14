import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class Readconfig():
    @staticmethod
    def getApplicationURL( ):
        url=config.set('common info','baseurl')
        return url
    @staticmethod
    def getUsermail( ):
        useremail=config.get('common info','username')
        return useremail

    @staticmethod
    def getPassword( ):
        password=(config.get('common info','Password'))
        return password
