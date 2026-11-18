from order_processor import OrderProcessor
from online_order_processor import OnlineOrderProcessor
from in_store_order_processor import InStoreOrderProcessor

UNKNOWN_COMMAND_MESSAGE = 'Неизвестная команда. Попробуйте снова'

commands = {
    '1': 'Обработка заказа онлайн',
    '2': 'Обработка заказа в магазине',
    '0': 'Выйти из программы'
}

ONLINE_ORDER_PROCESSOR_COMMAND, IN_STORE_ORDER_PROCESSOR_COMMAND, EXIT_COMMAND = commands.keys()


def print_commands(commands: dict[str, str]) -> None:
    for number, command in commands.items():
        print(f'{number}: {command}')


def is_valid_user_order(user_order_number: str) -> bool:
    return user_order_number.isdigit()


def process_order(order_processor: OrderProcessor) -> None:
    user_order_number = input('Укажите номер вашего заказа: ').strip()

    if not user_order_number:
        print('Номер заказа не может быть пустым!')

    else:
        if is_valid_user_order(user_order_number):
            result = order_processor.process_order(user_order_number)
            print(result)
        else:
            print('Номер заказа должен быть числом!')


is_program_running = True

print('Сервис выбора способа обработки заказа')

while is_program_running:
    print_commands(commands)
    user_command_number = input('Выберите способ обработки и укажите её номер: ').strip()

    if user_command_number in commands:
        if user_command_number == ONLINE_ORDER_PROCESSOR_COMMAND:
            order_processor = OnlineOrderProcessor()
        elif user_command_number == IN_STORE_ORDER_PROCESSOR_COMMAND:
            order_processor = InStoreOrderProcessor()
        elif user_command_number == EXIT_COMMAND:
            print('Выход из программы')
            is_program_running = False

        if is_program_running:
            process_order(order_processor)
    else:
        print(UNKNOWN_COMMAND_MESSAGE)
