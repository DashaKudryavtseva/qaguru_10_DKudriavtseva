from qaguru_10_DK.pages.registration_page import RegistrationPage


def test_fill(browser_configuration):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Maria')
    registration_page.fill_last_name('Ivanova')
    registration_page.fill_user_email('examplemail@mail.com')

    registration_page.choose_gender('Female')
    registration_page.fill_user_number('8987654321')

    registration_page.fill_date_of_birth('1996', 'January', '01')

    registration_page.fill_subjects('English', 'Chemistry')
    registration_page.choose_hobbies('Sports', 'Reading')

    registration_page.upload_picture('example.png')

    registration_page.fill_address('Sport Street, 140')

    registration_page.choose_state('NCR')
    registration_page.choose_city('Delhi')

    registration_page.submit_form()

    # THEN
    registration_page.should_have_register_info(
        "Maria Ivanova",
        "examplemail@mail.com",
        "Female",
        "8987654321",
        "01 January,1996",
        "English, Chemistry",
        "Sports, Reading",
        "example.png",
        "Sport Street, 140",
        "NCR Delhi",
    )
