# Source Distribution

Another reason for this package to exist is as a template for packaging.
We have samples of `MAIFEST.in`, `setup.cfg`, `tox.ini` and similar files.
This is slightly different from the [sample python packaging][pypa] to suit
the `/src/` directory before the application directory.  With the `/src/`
directory we can make sure at test phase that the installation will install the
package correctly, i.e. that the tests are not getting the sources through
imports from the current path.

