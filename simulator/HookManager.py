from typing import List
from Hook import Hook, SwapContext

class HookManager:
    def __init__(self):
        self.hooks: List[Hook] = []

    def register(self, hook: Hook) -> None:
        self.hooks.append(hook)

    def run_before_swap(self, context: SwapContext) -> None:
        for hook in self.hooks:
            hook.before_swap(context)

    def run_after_swap(self, context: SwapContext, result: dict) -> None:
        for hook in self.hooks:
            hook.after_swap(context, result)
