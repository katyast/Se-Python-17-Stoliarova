class Film(object):

    def __init__(self, name="", year=""):
        self.name = name
        self.year = year

    @classmethod
    def unic_name(cls):
        from random import randint
        import datetime
        now_time = datetime.datetime.now()
        now_time = str(now_time)
        film_name = "unic_title_" + now_time
        return cls(name=film_name,
                   year="19" + str(randint(0, 10)))