from selene import browser, have, command
from qaguru_10_DK import resource


def test_fill(browser_configuration):
    browser.open("https://demoqa.com/automation-practice-form")

    browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)
    """
    # if we are sure that there will be >= 3 ads
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).should(
        have.size_greater_than_or_equal(3)
    ).perform(command.js.remove)
    """

    # заполнение полей
    browser.element("#firstName").type("Maria").press_enter()
    browser.element("#lastName").type("Ivanova").press_enter()

    browser.element("#userEmail").type("examplemail@mail.com").press_enter()
    browser.all("[for^=gender-radio]").element_by(have.text("Female")).click()
    browser.element("#userNumber").type("8987654321")

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").send_keys("January")
    browser.element(".react-datepicker__year-select").send_keys("1996")
    browser.element(f'.react-datepicker__day--0{"01"}').click()

    browser.element("#subjectsInput").set_value("English").press_enter()

    browser.all(".custom-checkbox").element_by(have.exact_text("Sports")).click()

    browser.element("#uploadPicture").set_value(resource.path('example.png'))

    browser.element("#currentAddress").type("Sport Street, 140").press_enter()

    browser.element("#state").perform(command.js.scroll_into_view)
    browser.element("#state").click()
    browser.all("[id^=react-select][id*=option]").element_by(have.text("NCR")).click()

    browser.element("#city").click()
    browser.all("[id^=react-select][id*=option]").element_by(have.text("Delhi")).click()

    # browser.driver.execute_script("$('footer').hide()")
    browser.element("#submit").perform(command.js.scroll_into_view)
    # browser.driver.execute_script("document.body.style.zoom='60%'")
    browser.element("#submit").click()

    # сверка данных
    browser.element(".table").all("td").even.should(
        have.texts(
            "Maria Ivanova",
            "examplemail@mail.com",
            "Female",
            "8987654321",
            "01 January,1996",
            "English",
            "Sports",
            "example.png",
            "Sport Street, 140",
            "NCR Delhi",
        )
    )
