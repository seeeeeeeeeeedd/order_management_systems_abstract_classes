from order_processor import OrderProcessor


class OnlineOrderProcessor(OrderProcessor):
    def process_order(self, order: str) -> str:
        return f'Заказ "{order}" будет обработан онлайн'
