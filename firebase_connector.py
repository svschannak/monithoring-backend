import pyrebase
import datetime
import os

config = {
  "apiKey": os.environ["MONITHORING_FB_API_KEY"],
  "authDomain": os.environ["MONITHORING_FB_AUTH_DOMAIN"],
  "databaseURL": os.environ["MONITHORING_FB_DB_URL"],
  "storageBucket": os.environ["MONITHORING_FB_STORAGE_BUCKET"],
  "serviceAccount": "service_file/service_account.json"
}


DATE_FORMAT = "%Y-%m-%d-%H-%M"


class FirebaseConnector:

    def __init__(self):

        self.firebase = pyrebase.initialize_app(config)
        self.db = self.firebase.database()
        self.storage = self.firebase.storage()
        self.current_time = datetime.datetime.now().strftime(DATE_FORMAT)

    def get_all_users(self):
        return self.db.child("user").get().each()

    def save_results(self, user_id, monitoring_id, result):
        self.db.child("user").child(user_id).child('monitoring').child(monitoring_id).child('results').child(self.current_time).set(result)

    def upload_screenshot_and_get_url(self, user_id, filename):
        result = self.storage.child("user").child(user_id).child("%s" % filename).put(filename)
        return self.storage.child("user").child(user_id).child("%s" % filename).get_url()

