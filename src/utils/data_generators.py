from faker import Faker

faker = Faker()


class DataGenerator:
    @staticmethod
    def generate_email():
        return f"{faker.user_name()}@gmail.com"

    @staticmethod
    def generate_password():
        return faker.password()
