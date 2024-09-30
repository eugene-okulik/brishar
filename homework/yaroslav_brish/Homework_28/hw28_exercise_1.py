from playwright.sync_api import Page, expect, Route
import json
import re


def test_catch_and_change_response(page: Page):
    fake_header = 'яблокофон 16 про'

    def change_header_in_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = fake_header
        new_body = json.dumps(body)
        route.fulfill(
            response=response,
            body=new_body
        )

    page.route(re.compile('library/step0_iphone/digitalmat'),
               change_header_in_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    iphone16pro = page.get_by_role(
        "button",
        name="Take a closer look - iPhone 16 Pro & iPhone 16 Pro Max"
    )
    iphone16pro.click()
    header = page.get_by_role("heading", name=fake_header)
    expect(header).to_have_text(fake_header)
