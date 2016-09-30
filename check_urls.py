import os
from string import ascii_uppercase
from random import choice
from selenium import webdriver

from firebase_connector import DATE_FORMAT
from firebase_connector import FirebaseConnector
import datetime

import time

if __name__ == "__main__":
    connector = FirebaseConnector()

    for user in connector.get_all_users():
        for idx, val in user.val()['monitoring'].iteritems():
            br = webdriver.PhantomJS()
            br.set_window_size(1280, 720)
            br.get(val['url'])

            try:
                result = {
                    'content': br.find_element_by_xpath(val["selector"]).text,
                    'status': "SUCCESS",
                    'reason': ""
                }
                # TODO: Implement different operators

            except:
                result = {
                    'content': "",
                    'status': "ERROR",
                    'reason': "element not found"
                }

            #time.sleep(5)

            directory = "screenshots/%s" % datetime.datetime.now().strftime(DATE_FORMAT)
            if not os.path.exists(directory):
                os.makedirs(directory)

            file_name = ''.join(choice(ascii_uppercase) for i in range(24))
            file_path = '%s/%s.png' % (directory, file_name)

            br.save_screenshot(file_path)
            br.quit()

            result["screenshot"] = connector.upload_screenshot_and_get_url(user.key(), file_path)
            result["timestamp"] = time.time()
            connector.save_results(user.key(), idx, result)
