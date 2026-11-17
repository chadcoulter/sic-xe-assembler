# SIC/XE assembler and SVL compiler

The Python distribution `redsigma-sicxe` installs the SIC/XE assembler/simulator and the SVL-to-SIC/XE compiler.

## Package dependency

This project installs **SVL as a Python package** (`redsigma-svl`) rather than copying SVL sources into this repository. The dependency is pinned to commit `a208b527d158a4f377ec59b4dbcb9de93cc8f80b` from `chadcoulter/svl` for repeatable dependency resolution.

The installed `redsigma-svl` package exposes the existing import namespace `svl`, including `svl.lexer`, `svl.parser_rd`, and `svl.gate231`.

## Install (Windows cmd or another terminal)

Git and Python 3.10+ are required for the source dependency. From the SIC/XE repository root:

```cmd
python -m pip install -e .
```

To verify the package imports:

```cmd
python -c "from svl.lexer import tokenize; from svl.parser_rd import Parser; from svl.gate231 import compute_checksums; from svl_to_sic import SICXECodeGen; from sic_xe_assembler_sim import Assembler, Simulator; print('SVL + SIC/XE imports OK')"
```

To compile one of the SVL repository's example programs (when available locally):

```cmd
python svl_to_sic.py path\to\svl\examples\test_add.svl --emit-asm
```

The package also installs the commands `sicxe-assemble` and `svl-to-sicxe`.

## Scope

This change only packages the existing code and resolves the missing SVL import dependency. It does not modify machine instruction semantics, the SVL compiler, or its 231-gate checks.
