from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class SwapContext:
    amount_in: float
    token_in: str                  # "token0" or "token1"
    reserve0: float
    reserve1: float
    amm_price: float
    external_price: float
    block_number: int
    timestamp: int


class Hook(ABC):
    @abstractmethod
    def before_swap(self, context: SwapContext) -> None:
        pass

    @abstractmethod
    def after_swap(self, context: SwapContext, result: dict) -> None:
        """
        `result` contains:
            {
                "amount_out": float
            }
        """
        pass
