class NotJustInt(Exception):
     def __init__(self, message="Not just integer in the list"):
          self.msg = message

class NotJustStr(Exception):
     def __init__(self, message="Not just string in the list"):
          self.msg = message

class other(Exception):
     def __init__(self, message="Something went wrong!"):
          self.msg = message
