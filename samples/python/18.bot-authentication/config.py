#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("89867f1b-6b09-4bd1-8f7c-6adbea6748f3", "")
    APP_PASSWORD = os.environ.get("ec-Ue6x39tCHhd6A_R-hlBLrTZ5IRNnEH_", "")
    CONNECTION_NAME = os.environ.get("Phoenix951205", "")
