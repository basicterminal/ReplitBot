import requests, time

import json
import lxml, os

class replbot:
            def __init__(self, connect_sid):
                self.username    = ""
                self.connect_sid = connect_sid

            def login(
                self
            ):
                r = requests.get(
                    "https://replit.com/~",
                    headers = {
                            "set-cookie": "connect.sid=%s" % (
                                          self.connect_sid
                            )
                    }
                )

                if r.status_code in [200, 201, 203, 204]:
                   print("Logged in with %s.." % (self.connect_sid[:10]))
                  
            def fetch_repl(
                self,
                author_name,
                author_repl_name
            ):
                r = requests.get(
                    "https://replit.com/data/repls/@%s/%s" % (
                           author_name,
                           author_repl_name
                    ), headers = {
                               "set-cookie": "connect.sid=%s" % (
                                           self.connect_sid
                               )
                    }
                )

                if r.status_code in [200, 201, 203, 204]:
                   return r.json()
