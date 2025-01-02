# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJquerylib(RPackage):
    """Obtain 'jQuery' as an HTML Dependency Object.

    Obtain any major version of 'jQuery' (<https://code.jquery.com/>) and use
    it in any webpage generated by 'htmltools' (e.g. 'shiny', 'htmlwidgets',
    and 'rmarkdown'). Most R users don't need to use this package directly, but
    other R packages (e.g.  'shiny', 'rmarkdown', etc.) depend on this package
    to avoid bundling redundant copies of 'jQuery'."""

    cran = "jquerylib"

    license("MIT")

    version("0.1.4", sha256="f0bcc11dcde3a6ff180277e45c24642d3da3c8690900e38f44495efbc9064411")

    depends_on("r-htmltools", type=("build", "run"))
