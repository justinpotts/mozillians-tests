#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from selenium.webdriver.common.by import By
from pages.base import Base

class VerifyEmail(Base):


    _verify_email_locator = (By.LINK_TEXT, 'Verify Email')

    def verify_email(self, user):
        self.selenium.find_element(*self._verify_email_locator).click()

        credentials = self.testsetup.credentials[user]

        from browserid import BrowserID
        pop_up = BrowserID(self.selenium, self.timeout)
        pop_up.sign_in(user['email'], user['password'])
        WebDriverWait(self.selenium, 20).until(lambda s: self.is_user_loggedin)
