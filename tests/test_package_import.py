"""Integration smoke tests for the installed SIC/XE + SVL packages."""

import unittest


class PackageImportTests(unittest.TestCase):
    def test_svl_frontend_and_checksum_import(self):
        from svl.lexer import tokenize
        from svl.parser_rd import Parser
        from svl.gate231 import compute_checksums
        self.assertTrue(callable(tokenize))
        self.assertTrue(callable(Parser))
        self.assertTrue(callable(compute_checksums))

    def test_sicxe_compiler_and_simulator_import(self):
        from svl_to_sic import SICXECodeGen
        from sic_xe_assembler_sim import Assembler, Simulator, parse_source
        self.assertTrue(callable(SICXECodeGen))
        self.assertTrue(callable(Assembler))
        self.assertTrue(callable(Simulator))
        self.assertTrue(callable(parse_source))


if __name__ == "__main__":
    unittest.main()
