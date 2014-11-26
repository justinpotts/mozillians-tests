#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By

from pages.base import Base


class GroupInfoPage(Base):

    _delete_group_button = (By.CSS_SELECTOR, '.button.delete.right')
    _join_group_button = (By.CSS_SELECTOR, '#join-group button')
    _leave_group_button = (By.CSS_SELECTOR, '#leave-group button')
    _group_name_locator = (By.ID, 'group_name')

    def delete_group(self):
        '''Available only if you are the group curator'''
        self.selenium.find_element(*self._delete_group_button).click()
        from pages.groups_page import GroupsPage
        return GroupsPage(self.testsetup)

    def join_group(self):
        self.selenium.find_element(*self._join_group_button).click()
        from pages.group_info_page import GroupInfoPage
        return GroupInfoPage(self.testsetup)

    def leave_group(self):
        self.selenium.find_element(*self._leave_group_button).click()
        from pages.group_info_page import GroupInfoPage
        return GroupInfoPage(self.testsetup)

    @property
    def is_a_member(self):
        return self.is_element_present(*self._leave_group_button)

    @property
    def group_name(self):
        return self.selenium.find_element(*self._group_name_locator).text
