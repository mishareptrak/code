from typing import Optional
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int


class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self.available_quantity = qty
        self._allocations = set()

    def allocate(self, line: OrderLine):
        self.available_quantity -= line.qty

    def can_allocate(self, line: OrderLine):
        if line.sku != self.sku:
            return False
        return self.available_quantity >= line.qty

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)
