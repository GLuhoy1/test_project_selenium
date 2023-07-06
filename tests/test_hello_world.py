
def test_first(browser):
    browser.get("https://www.google.com/")
    assert "Google" in browser.title

def test_second(browser):
    browser.get("https://www.ya.ru/")
    assert "Ой!" in browser.title or "Яндекс" in browser.title

