from simulator.core.Hook import Hook, SwapContext
from simulator.core.AMM import AMM

class DynamicFeeHook(Hook):
    def __init__(self, amm: AMM):
        self.amm = amm

    def before_swap(self, context: SwapContext) -> None:
        deviation = abs(context.amm_price - context.external_price) / context.external_price

        # Raise fee if price diverges from oracle
        if deviation > 0.02:
            self.amm.set_fee(0.01)  # 1%
        else:
            self.amm.set_fee(0.003)  # 0.3%

    def after_swap(self, context: SwapContext, result: dict) -> None:
        # You can log slippage, LVR, etc. here if needed
        # print(f"Post-swap amount out: {result['amount_out']}")
        pass
