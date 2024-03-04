class NotAuthorized(Exception):
    def __init__(self):
        super().__init__("Сессия устарела. Пожалуйста, пройдите авторизацию!")


class UserAlreadyExist(Exception):
    def __init__(self):
        super().__init__("Пользователь уже существует!\nПопробуйте войти.")


class UserNotFound(Exception):
    def __init__(self):
        super().__init__("Пользователя с данным Email не существует!\nПопробуйте с другой почтой или зарегистрируйтесь!")


class UserPasswordIsIncorrect(Exception):
    def __init__(self):
        super().__init__("Введенный пароль не подходит. Повторите попытку еще раз!")


class ReferalLinkNotExists(Exception):
    def __init__(self):
        super().__init__("Реферальная ссылка не существует!")


class AvatarexUserNotRegistered(Exception):
    def __init__(self):
        super().__init__("Данный пользователь Avatarex не привязан к реферальной системе!")
