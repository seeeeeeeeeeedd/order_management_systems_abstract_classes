from order_processor import OrderProcessor


class InStoreOrderProcessor(OrderProcessor):
    def process_order(self, order):
        return f'Заказ "{order}" будет обработан в магазине'
