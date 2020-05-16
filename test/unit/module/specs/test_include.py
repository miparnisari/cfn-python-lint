"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

import cfnlint.specs

from test.testlib.testcase import BaseTestCase
from cfnlint import Runner
from cfnlint.rules import RulesCollection
from cfnlint.rules.resources.Configuration import Configuration  # pylint: disable=E0401
import cfnlint.helpers


class TestInclude(BaseTestCase):
    """Used for Testing Rules"""

    def setUp(self):
        """Setup"""
        self.collection = RulesCollection()
        self.collection.register(Configuration())

    def tearDown(self):
        """Tear Down"""
        # Reset the Spec override to prevent other tests to fail
        cfnlint.specs.initialize_specs()

    def test_fail_run(self):
        """Failure test required"""
        filename = 'test/fixtures/templates/bad/override/include.yaml'
        template = self.load_template(filename)

        cfnlint.specs.override_specs('test/fixtures/templates/override_spec/include.json')

        bad_runner = Runner(self.collection, filename, template, ['us-east-1'], [])
        errs = bad_runner.run()
        self.assertEqual(2, len(errs))
