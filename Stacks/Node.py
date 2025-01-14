from typing import Optional

class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next: Optional['Node'] = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.data == other.data
        return False
