

class Test:
    
    def __init__(self) -> None:
        self.session = None

    
    def __enter__(self):
        self.session = "session_maker()"
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("SAIu")


with Test() as z:
    print(z.session)

