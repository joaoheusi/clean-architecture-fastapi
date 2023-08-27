class Config:
    def __init__(self) -> None:
        self.VARIABLE: int = 0

    async def set_variable(self, value: int) -> None:
        self.VARIABLE = value

    async def get_variable(self) -> int:
        return self.VARIABLE


config = Config()
