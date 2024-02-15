#!/usr/bin/env python3

import aws_cdk as cdk

from python_cdk_app.python_cdk_app_stack import PythonCdkAppStack


app = cdk.App()
PythonCdkAppStack(app, "PythonCdkAppStack")

app.synth()
