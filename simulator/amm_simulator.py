import random
import time
from simulator.AMM import AMM
from simulator.HookManager import HookManager
from simulator.Hook import SwapContext
from simulator.hooks.DynamicFeeHook import DynamicFeeHook

class AMMSimulator:
    def __init__(self, num_blocks=50, txs_per_block=5, update_frequency=3):
        self.amm = AMM(100_000, 100_000)
        self.hooks = HookManager()
        self.hooks.register(DynamicFeeHook(self.amm))
        self.external_price = 1.0

        self.num_blocks = num_blocks
        self.txs_per_block = txs_per_block
        self.update_frequency = update_frequency

    def update_external_price(self):
        self.external_price *= 1 + (random.random() - 0.5) * 0.02

    def get_trade(self):
        amount_in = random.randint(100, 1100)
        token_in = "token0" if random.random() > 0.5 else "token1"
        return amount_in, token_in

    def run(self):
        for block_number in range(1, self.num_blocks + 1):
            if block_number % self.update_frequency == 0:
                self.update_external_price()

            print(f"\n📦 Block {block_number}")

            for tx_index in range(self.txs_per_block):
                amount_in, token_in = self.get_trade()
                reserve0, reserve1 = self.amm.get_reserves()
                amm_price = self.amm.get_price()

                context = SwapContext(
                    amount_in=amount_in,
                    token_in=token_in,
                    reserve0=reserve0,
                    reserve1=reserve1,
                    amm_price=amm_price,
                    external_price=self.external_price,
                    block_number=block_number,
                    timestamp=int(time.time())
                )

                self.hooks.run_before_swap(context)

                result = (
                    self.amm.swap_token0_for_token1(amount_in)
                    if token_in == "token0"
                    else self.amm.swap_token1_for_token0(amount_in)
                )

                self.hooks.run_after_swap(context, {"amount_out": result.amount_out})

                print(
                    f"  ▸ Tx {tx_index + 1} | {token_in} → {'token1' if token_in == 'token0' else 'token0'} | "
                    f"AMM Price: {self.amm.get_price():.4f} | Oracle: {self.external_price:.4f} | Fee: {self.amm.get_fee()}"
                )
