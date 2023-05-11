from selene import browser

from qaguru_10_DK.data.users import User
from qaguru_10_DK.registration_page import RegistrationPage


def test_fill():
    user = User(
        'Maria',
        'Ivanova',
        'examplemail@mail.com',
        'Female',
        '8987654321',
        '1996',
        'January',
        '01',
        ['English', 'Chemistry'],
        ['Sports', 'Reading'],
        'example.png',
        'Sport Street, 140',
        'NCR',
        'Delhi',
    )
    registration_page = RegistrationPage()
    browser.open("/automation-practice-form")
    registration_page.take_out_ads()

    # WHEN
    registration_page.register(user)

    # THEN
    registration_page.should_have_register_info(user)
