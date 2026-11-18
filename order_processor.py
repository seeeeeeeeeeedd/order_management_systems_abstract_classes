from abc import ABC, abstractmethod


class OrderProcessor(ABC):
    @abstractmethod
    def process_order(self, order):
        pass
