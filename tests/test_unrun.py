import yaml, unittest


class TestUnrun(unittest.TestCase):
    def setUp(self):
        self.file = "unrun.yaml"
        with open(self.file, 'w') as f:
            self.scripts = yaml.safe_load(f)

    def tearDown(self):
        with open(self.file, 'w') as f:
            yaml.dump(self.scripts, f)


if __name__ == '__main__':
    unittest.main()
