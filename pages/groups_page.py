#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from random import randrange

from selenium.webdriver.common.by import By

from pages.base import Base
from pages.page import Page


class GroupsPage(Base):

    _create_group_main_button = (By.CLASS_NAME, 'large')
    _alert_message_locator = (By.CSS_SELECTOR, '.alert-info')
    _result_item_locator = (By.CSS_SELECTOR,
                            'div.groups-areas > ul.group-list > li.group-item')

    def click_create_group_main_button(self):
        self.selenium.find_element(*self._create_group_main_button).click()
        from pages.create_group_page import CreateGroupPage
        return CreateGroupPage(self.testsetup)

    def wait_for_alert_message(self):
        self.wait_for_element_visible(*self._alert_message_locator)

    @property
    def results_count(self):
        return len(self.find_elements(*self._result_item_locator))

    @property
    def group_results(self):
        return [self.GroupResults(self.testsetup, web_element)
                for web_element
                in self.find_elements(*self._result_item_locator)]

    def get_random_group(self):
        random_index = randrange(self.results_count)
        return self.group_results[random_index].open_group_page()

    def open_group(self, name):
        self.selenium.find_element_by_link_text(name).click()
        from pages.group_info_page import GroupInfoPage
        return GroupInfoPage(self.testsetup)

    class GroupResults(Page):

        _group_link_locator = (By.CSS_SELECTOR, 'a')

        def __init__(self, testsetup, root_element):
            self._root_element = root_element
            Page.__init__(self, testsetup)

        def open_group_page(self):
            self.find_element(*self._group_link_locator).click()
            from pages.group_info_page import GroupInfoPage
            return GroupInfoPage(self.testsetup)
