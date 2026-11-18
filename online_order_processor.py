from order_processor import OrderProcessor


class OnlineOrderProcessor(OrderProcessor):
    def process_order(self, order):
        return f'Заказ "{order}" будет обработан онлайн'
