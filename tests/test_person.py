import unittest
import sys
import os

# Ensure the parent directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from beings.person import Person

class TestPerson(unittest.TestCase):

    def test_init(self):
        person = Person("Ethan Henderson", 24, jobs=["Software"])
        self.assertEqual(person.name, "Ethan Henderson")
        self.assertEqual(person.age, 24)
        self.assertEqual(person.jobs, ["Software"])

    def test_forename(self):
        person = Person("Ethan Henderson", 24)
        self.assertEqual(person.forename, "Ethan")

    def test_surname(self):
        person = Person("Ethan Henderson", 24)
        self.assertEqual(person.surname, "Henderson")
        single_name_person = Person("Ethan", 24)
        self.assertIsNone(single_name_person.surname)

    def test_celebrate_birthday(self):
        person = Person("Ethan Henderson", 24)
        person.celebrate_birthday()
        self.assertEqual(person.age, 25)

    def test_add_job(self):
        person = Person("Ethan Henderson", 24)
        person.add_job("Engineer")
        self.assertIn("Engineer", person.jobs)
        person.add_job("Manager")
        self.assertIn("Manager", person.jobs)
        self.assertEqual(len(person.jobs), 2)

if __name__ == "__main__":
    unittest.main()
