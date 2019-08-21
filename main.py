from typing import Any
import unittest
import exercises


class AlgorithmTest(unittest.TestCase):
    algorithm_name: str
    input_args: dict
    expected_output: Any

    def __init__(self, *args, algorithm_name=None, input_args=None, expected_output=None):
        super().__init__(*args)
        self.algorithm_name = algorithm_name
        self.input_args = input_args
        self.expected_output = expected_output

    def test_algorithm_input_output(self):
        algorithm = getattr(exercises, self.algorithm_name, None)

        output = algorithm(**self.input_args)
        self.assertEqual(
            output,
            self.expected_output,
            "\nComputed output: {0}\nExpected output: {1}".format(output, self.expected_output)
        )


if __name__ == "__main__":
    suite = unittest.TestSuite()

    for inp, out in (({"s1": "pouet", "s2": "prout"}, False), ({"s1": "abc", "s2": "bca"}, True),
                     ({"s1": "abbc", "s2": "bcba"}, True), ({"s1": "abbc", "s2": "cba"}, False),
                     ({"s1": "abbc", "s2": ""}, False), ({"s1": "", "s2": ""}, True)):
        suite.addTest(AlgorithmTest(
            "test_algorithm_input_output",
            algorithm_name="is_anagram",
            input_args=inp,
            expected_output=out
        ))

    for inp, out in (("()", True), ("({})", True), ("({}[])", True), ("(){}[]", True), ("(({[{}]}))", True),
                     ("({)}", False), ("(()", False), ("())", False), ("(((()", False), ("())))", False),
                     ("int main() { for (int i = 0; i < 42; i++) { if (i == 26) { printf(\"coucou\"); } } }", True)):
        suite.addTest(AlgorithmTest(
            "test_algorithm_input_output",
            algorithm_name="check_bracket_consistency",
            input_args={
                "string": inp
            },
            expected_output=out
        ))

    runner = unittest.TextTestRunner()
    runner.run(suite)


