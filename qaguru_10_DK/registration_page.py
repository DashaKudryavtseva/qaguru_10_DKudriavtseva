from pathlib import Path
from selene import browser, have, command
import tests
from qaguru_10_DK.data.users import User


class RegistrationPage:
    def __init__(self):
        self.google_adds = browser.all("[id^=google_ads][id$=container__]")
        self.submit = browser.element("#submit")

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")

        self.google_adds.with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        self.google_adds.perform(command.js.remove)

    def register(self, user: User):
        self.__fill_first_name(user.first_name)
        self.__fill_last_name(user.last_name)
        self.__fill_user_email(user.email)
        self.__choose_gender(user.gender)
        self.__fill_user_number(user.telephone_number)
        self.__fill_date_of_birth(
            user.year_of_birth, user.month_of_birth, user.day_of_birth
        )
        self.__fill_subjects(user.subjects)
        self.__choose_hobbies(user.hobbies)
        self.__upload_picture(user.picture)
        self.__fill_address(user.address)
        self.__choose_state(user.state)
        self.__choose_city(user.city)
        self.__submit_form()

    def __fill_first_name(self, value):
        browser.element("#firstName").type(value).press_enter()

    def __fill_last_name(self, value):
        browser.element("#lastName").type(value).press_enter()

    def __fill_user_email(self, value):
        browser.element("#userEmail").type(value).press_enter()

    def __choose_gender(self, value):
        browser.all("[for^=gender-radio]").element_by(have.text(value)).click()

    def __fill_user_number(self, value):
        browser.element("#userNumber").type(value)

    def __fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").send_keys(month)
        browser.element(".react-datepicker__year-select").send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def __fill_subjects(self, names: list):
        for name in names:
            browser.element("#subjectsInput").set_value(name).press_enter()

    def __choose_hobbies(self, values: list):
        for value in values:
            browser.all(".custom-checkbox").element_by(have.exact_text(value)).click()

    def __upload_picture(self, file_name):
        browser.element("#uploadPicture").set_value(
            str(
                Path(tests.__file__)
                .parent.joinpath(f'resources/{file_name}')
                .absolute()
            )
        )

    def __fill_address(self, value):
        browser.element("#currentAddress").type(value).press_enter()

    def __choose_state(self, value):
        browser.element("#state").perform(command.js.scroll_into_view)
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.text(value)
        ).click()

    def __choose_city(self, value):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.text(value)
        ).click()

    def __submit_form(self):
        self.submit.perform(command.js.scroll_into_view)
        self.submit.click()

    # def should_have_register_info(
    #     self,
    #     user_name,
    #     email,
    #     gender,
    #     telephone_number,
    #     date_of_birth,
    #     subjects,
    #     hobbies,
    #     picture,
    #     address,
    #     state_city,
    # ):
    #     browser.element(".table").all("td").even.should(
    #         have.texts(
    #             user_name,
    #             email,
    #             gender,
    #             telephone_number,
    #             date_of_birth,
    #             subjects,
    #             hobbies,
    #             picture,
    #             address,
    #             state_city,
    #         )
    #     )
    def should_have_register_info(self, user: User):
        browser.element(".table").all("td").even.should(
            have.texts(
                user.full_name,
                user.email,
                user.gender,
                user.telephone_number,
                user.date_of_birth,
                user.all_subjects,
                user.all_hobbies,
                user.picture,
                user.address,
                user.state_city,
            )
        )
