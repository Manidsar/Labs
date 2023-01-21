# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Lamp:
    def __init__(self, power: float, light_color: str):
        """
        Объект - настольная лампа
        power: мощность лампочки
        light_color: Цвет, которым светит лампа
        >>> lamp = Lamp(500, 'red')  # инициализация экземпляра класса
        """

        if not isinstance(power, (int, float)):
            raise TypeError("Мощность лампы должна быть типа int или float")
        if power < 0:
            raise ValueError("Мощность лампы не может быть отрицательной")
        self.power = power

        if type(light_color) is not str:
            raise ValueError("Цвет лампы должен быть строкой")
        self.light_color = light_color

    def change_color(self, new_color):
        """
        Функция, которая меняет цвет, которым светит лампа
        :return: Изменяет значение light_color
        >>> lamp = Lamp(500, 'red')
        >>> lamp.change_color('green')
        """
        pass

    def is_turn_on(self):
        """
        Фунция, которая проверяет включена ли лампа
        :return: True/False
        >>> lamp = Lamp(500, 'red')
        >>> lamp.is_turn_on()
        """
        pass


class Phone:
    def __init__(self, battery, model):
        """
        Объект - телефон
        battery - заряд телефона
        model - модель телефона
        >>> phone = Phone(100, 'samsung')  # инициализация экземпляра класса
        """
        if not isinstance(battery, (int, float)):
            raise TypeError("Заряд телефона должен быть типа int или float")
        if not 0 <= battery <= 100:
            raise ValueError("Заряд батареи находится в пределах от 0 до 100")
        self.battery = battery

        if type(model) is not str:
            raise ValueError("Модель телефона - строковый тип данных")
        self.model = model

    def charge_phone(self, power):
        '''
        :param power: процент добавляемого заряда на телефон
        :raise: ValueError: Если количество добавляемого заряда превышает ограничения на battery
        >>> phone = Phone(100, 'samsung')
        >>> phone.charge_phone(10)
        '''
        if not isinstance(power, (int, float)):
            raise TypeError("Заряд должен быть типа int или float")
        if power < 0:
            raise ValueError("Добавляемый заряд должен быть положительной величиной")
        pass

    def check_battery(self):
        '''
        :return: процент зарядки на телефоне
        >>> phone = Phone(100, 'samsung')
        >>> phone.check_battery()
        '''
        pass


class Student:
    def __init__(self, status, course):
        '''

        :param status: Показывает учебный статус студента (учится, академ.отпуск)
        :param course: Показывает номер курса студента
        >>> st = Student('учится', 2)
        '''
        if type(course) is not int:
            raise TypeError("Номер курса - целое число")
        if not 1 <= course <= 6:
            raise ValueError("Номер курса может быть от 1 до 6")
        self.course = course

        if type(status) is not str:
            raise ValueError("Статус студента - строковый тип данных")
        self.model = status

    def change_status(self, new_status):
        '''
        Изменяет стадус студента
        >>> st = Student('учится', 2)
        >>> st.change_status('Отчислен')
        '''
        pass

    def change_course(self, new_course):
        '''
        :param new_course: новый курс студента
        >>> st = Student('учится', 2)
        >>> st.change_course(3)
        '''
        if type(new_course) is not int:
            raise TypeError("Номер курса - целое число")
        if not 1 <= new_course <= 6:
            raise ValueError("Номер курса может быть от 1 до 6")
        self.course = new_course


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest




