# Salmonjoon
# DungeonOfMandom
# 2016.05.19
# Event


class Event:
    def __init__(self, prefix, title, content):
        self.__message = '[{}] {} : {}'.format(prefix, title, content)

    def message(self):
        return self.__message
