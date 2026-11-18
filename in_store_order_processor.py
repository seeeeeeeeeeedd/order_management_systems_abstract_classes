from order_processor import OrderProcessor


class InStoreOrderProcessor(OrderProcessor):
    def process_order(self, order: str) -> str:
        return f'Заказ "{order}" будет обработан в магазине'
