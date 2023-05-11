import dataclasses
import datetime


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    telephone_number: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subjects: list[str]
    hobbies: list[str]
    picture: str
    address: str
    state: str
    city: str

    @property
    def full_name(self):
        return ' '.join([self.first_name, self.last_name])

    @property
    def date_of_birth(self):
        return f'{self.day_of_birth} {self.month_of_birth},{self.year_of_birth}'

    @property
    def all_subjects(self):
        return ', '.join(self.subjects)

    @property
    def all_hobbies(self):
        return ', '.join(self.hobbies)

    @property
    def state_city(self):
        return ' '.join([self.state, self.city])
