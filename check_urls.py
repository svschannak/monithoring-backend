# -*- coding: utf-8 -*-

import os
from string import ascii_uppercase
from random import choice
from selenium import webdriver

from firebase_connector import DATE_FORMAT
from firebase_connector import FirebaseConnector
import datetime

import time

from operator_check import OperatorCheck


if __name__ == "__main__":
    connector = FirebaseConnector()

    for user in connector.get_all_users():
        for idx, val in user.val()['monitoring'].iteritems():
            result = dict()

            br = webdriver.PhantomJS()
            br.set_window_size(1280, 720)
            br.get(val['url'])

            element = br.find_element_by_xpath(val["selector"])
            check = OperatorCheck(val["operator"], element, val["value"]).check()
            if check:
                result['status'] = "SUCCESS"
            else:
                result['status'] = "ERROR"

            time.sleep(5)

            # create directory if not exists
            directory = "screenshots/%s" % datetime.datetime.now().strftime(DATE_FORMAT)
            if not os.path.exists(directory):
                os.makedirs(directory)

            # create and save screenshot
            file_name = ''.join(choice(ascii_uppercase) for i in range(24))
            file_path = '%s/%s.png' % (directory, file_name)

            br.save_screenshot(file_path)
            br.quit()

            result["screenshot"] = connector.upload_screenshot_and_get_url(user.key(), file_path)
            result["timestamp"] = time.time()

            connector.save_results(user.key(), idx, result)
