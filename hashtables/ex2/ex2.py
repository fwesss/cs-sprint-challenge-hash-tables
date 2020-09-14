from typing import List


class Ticket:
    def __init__(self, source: str, destination: str):
        self._source = source
        self._destination = destination

    @property
    def source(self) -> str:
        return self._source

    @property
    def destination(self) -> str:
        return self._destination

    def __getitem__(self, key: str) -> str:
        return getattr(self, key)


def reconstruct_trip(tickets: List[Ticket], _: int) -> List[str]:
    routes = {}

    for ticket in tickets:
        routes[ticket["source"]] = ticket["destination"]

    route = []

    destination = routes["NONE"]
    while destination != "NONE":
        route.append(destination)
        destination = routes[destination]

    route.append("NONE")

    return route
