# Copyright 2018 Espressif Systems (Shanghai) PTE LTD
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# APIs for interpreting and creating protobuf packets for
# protocomm endpoint with security type protocomm_security0

from __future__ import print_function
from future.utils import tobytes

from .security import Security


class Security0(Security):
    def __init__(self, verbose):
        # Initialize state of the security1 FSM
        self.session_state = 0
        self.verbose = verbose
        Security.__init__(self, self.security0_session)

    def security0_session(self, response_data):
        # protocomm security0 FSM which interprets/forms
        # protobuf packets according to present state of session
        if (self.session_state == 0):
            self.session_state = 1
            return self.setup0_request()
        if (self.session_state == 1):
            self.setup0_response(response_data)
            return None

    def setup0_request(self):
        # Form protocomm security0 request packet
        setup_req = session_pb2.SessionData()
        setup_req.sec_ver = 0
        session_cmd = sec0_pb2.S0SessionCmd()
        setup_req.sec0.sc.MergeFrom(session_cmd)
        return setup_req.SerializeToString().decode('latin-1')

    def setup0_response(self, response_data):
        # Interpret protocomm security0 response packet
        setup_resp = session_pb2.SessionData()
        setup_resp.ParseFromString(tobytes(response_data))
        # Check if security scheme matches
        if setup_resp.sec_ver != session_pb2.SecScheme0:
            print("Incorrect sec scheme")

    def encrypt_data(self, data):
        # Passive. No encryption when security0 used
        return data

    def decrypt_data(self, data):
        # Passive. No encryption when security0 used
        return data
