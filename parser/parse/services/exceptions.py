class ParserError(Exception):
    """ Base parsing error """

class TagNameNotExist(ParserError):
    """ Requested tag does not exist """