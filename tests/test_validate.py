import unittest

from oif_fabric.validate import validate_resource


class ValidateResourceTests(unittest.TestCase):
    def test_accepts_minimal_resource(self):
        resource = {
            "id": "example.echo",
            "name": "Example Echo",
            "resource_type": "tool",
            "publisher": {"name": "Example"},
            "version": "1.0.0",
            "capabilities": [{"id": "text.echo"}],
        }
        self.assertEqual(validate_resource(resource), [])

    def test_rejects_non_object(self):
        self.assertEqual(validate_resource([]), ["resource must be a JSON object"])

    def test_reports_missing_fields(self):
        errors = validate_resource({})
        self.assertIn("missing required field: id", errors)
        self.assertIn("missing required field: capabilities", errors)

    def test_rejects_empty_capabilities(self):
        resource = {
            "id": "x", "name": "X", "resource_type": "tool",
            "publisher": {"name": "Example"}, "version": "1",
            "capabilities": [],
        }
        self.assertIn("capabilities must be a non-empty array", validate_resource(resource))


if __name__ == "__main__":
    unittest.main()
