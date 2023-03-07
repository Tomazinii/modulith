from typing import Dict

class HttpRequest:

    def __init__(self,header: Dict = None, body: Dict = None, query: Dict = None):
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self) -> str:
        return f"HttpRequest(body: {self.body}, header:{self.header}, query:{self.query})"


class HttpResponse:

    def __init__(self, status_code:int, body: any ):
        self.status_code = status_code
        self.body = body

    def __repr__(self) -> str:
        return f"HttpReponse(status_code: {self.status_code}, body: {self.body})"