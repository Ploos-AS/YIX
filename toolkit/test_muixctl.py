# SPDX-License-Identifier: MIT
import unittest
from muixctl import validate

class InventoryTests(unittest.TestCase):
    def config(self, profile="nano"):
        return {"version": "0.1", "site": "example", "profile": profile,
                "switches": [{"id": "sw1"}], "route_servers": []}

    def test_nano(self):
        self.assertFalse(validate(self.config())["conformance_verified"])

    def test_micro_missing_servers(self):
        with self.assertRaises(ValueError):
            validate(self.config("micro"))

    def test_micro_shared_host(self):
        c = self.config("micro")
        c["route_servers"] = [{"id": "a", "host_failure_domain": "h1"},
                              {"id": "b", "host_failure_domain": "h1"}]
        with self.assertRaises(ValueError):
            validate(c)
        c["route_servers"][1]["host_failure_domain"] = "h2"
        self.assertEqual(validate(c)["route_servers"], 2)

    def test_regional_missing_switch(self):
        with self.assertRaises(ValueError):
            validate(self.config("regional"))

    def test_duplicate_switch(self):
        c = self.config()
        c["switches"] *= 2
        with self.assertRaises(ValueError):
            validate(c)
