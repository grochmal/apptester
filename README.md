README for `apptester`

[![Build Status][trbuild]][trlink]

[trbuild]: https://api.travis-ci.org/grochmal/apptester.svg?branch=master
[trlink]: https://travis-ci.org/grochmal/apptester "Travis CI"

## Introduction

Just a simple app that echoes headers, and controls caching by GET arguments.
It is meant for testing of web and application servers configuration.

For example, one could check whether the load balancer and application server
is passing enough environment parameters to determine whether HTTPS is in use.
By connecting to the app through HTTP and then through HTTPS and checking the
`scheme` and the `REQUEST_SCHEME` CGI/WSGI variable.

## Copying

Copyright (C) 2018 Michal Grochmal

This file is part of `apptester`.

`apptester` is free software; you can redistribute and/or modify all or parts
of it under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 3 of the License, or (at your option)
any later version.

`apptester` is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

The COPYING file contains a copy of the GNU General Public License.  If you
cannot find this file, see <http://www.gnu.org/licenses/>.

