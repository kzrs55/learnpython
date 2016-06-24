# -*- coding: utf-8 -*-

url_dict_test={
    "star_url": "http://doc.scrapy.org/en/1.1/topics/spiders.html",
    "requestPageType": {
        "requestType": "Request",
        "contentType": "HTML",
        "method": "GET",
        "renderJs": "true",
        "formData": {},
        "headers": {
            "Cookie": {},
            "Referer": ""
        }
    },
    "actions": [
        {
            "InputAction": {
                "css_path": "input.head_search_key",
                "value": "浙江"
            }
        },
        {
            "ClickAction": {
                "css_path": "button.head_search_btn"
            }
        },
        {
            "WaitAction": {
                "condition": "presence_of_element_located((By.CSS_SELECTOR, \"div.dataItem\"))",
                "timeout": 60
            }
        }
    ],
}

