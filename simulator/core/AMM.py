from dataclasses import dataclass

@dataclass
class SwapResult:
    amount_out: float
    new_reserve0: float
    new_reserve1: float
    effective_price: float
    fee: float


class AMM:
    def __init__(self, initial_reserve0: float, initial_reserve1: float, fee: float = 0.003):
        self.reserve0 = initial_reserve0
        self.reserve1 = initial_reserve1
        self.fee = fee  # 0.003 = 0.3%

    def add_liquidity(self, amount0: float, amount1: float) -> None:
        self.reserve0 += amount0
        self.reserve1 += amount1

    def swap_token0_for_token1(self, amount_in: float) -> SwapResult:
        amount_in_with_fee = amount_in * (1 - self.fee)
        amount_out = (amount_in_with_fee * self.reserve1) / (self.reserve0 + amount_in_with_fee)

        self.reserve0 += amount_in_with_fee
        self.reserve1 -= amount_out

        return SwapResult(
            amount_out=amount_out,
            new_reserve0=self.reserve0,
            new_reserve1=self.reserve1,
            effective_price=amount_out / amount_in,
            fee=self.fee
        )

    def swap_token1_for_token0(self, amount_in: float) -> SwapResult:
        amount_in_with_fee = amount_in * (1 - self.fee)
        amount_out = (amount_in_with_fee * self.reserve0) / (self.reserve1 + amount_in_with_fee)

        self.reserve1 += amount_in_with_fee
        self.reserve0 -= amount_out

        return SwapResult(
            amount_out=amount_out,
            new_reserve0=self.reserve0,
            new_reserve1=self.reserve1,
            effective_price=amount_out / amount_in,
            fee=self.fee
        )

    def get_price(self) -> float:
        """Returns the price of token1 in terms of token0."""
        return self.reserve1 / self.reserve0

    def get_reserves(self) -> tuple[float, float]:
        """Returns the current reserves of token0 and token1."""
        return self.reserve0, self.reserve1

    def set_fee(self, new_fee: float) -> None:
        self.fee = new_fee

    def get_fee(self) -> float:
        return self.fee
