class Config:
    def __init__(self):
        self.VARIABLE = 0

    async def set_variable(self, value):
        self.VARIABLE = value

    async def get_variable(self):
        return self.VARIABLE


config = Config()
