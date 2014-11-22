Title: Validating LV2 Data
Date: 2014-11-20 21:33
Category: Documentation

Because LV2 data written in Turtle does not need to be compiled like C, the
author must take care to ensure it is valid.  For example, if there is a typo
in a predicate, a plugin may silently fail to work correctly.

To prevent this kind of error, use `sord_validator` from
[Sord](http://drobilla.net/software/sord).  This program will check that all
the properties in a set of Turtle data are actually defined, that the domain
and range is valid, and that typed literals are valid (for example, that they
have the correct type, or that `lv2:symbol` properties are actually valid LV2
symbols).

To do this, the validator needs to be passed all relevant data, including the
vocabularies which define the properties and classes used.  The LV2
distribution contains all the external vocabularies used in the `schemas`
directory.  If `sord_validate` is installed, and an LV2 source tree is present,
then LV2 data can be checked like so:

    :::sh
    sord_validate $(find /path/to/lv2-x.y.z -name '*.ttl') /path/to/data.ttl

To check all data in your bundle:

    :::sh
    sord_validate $(find /path/to/lv2-x.y.z -name '*.ttl') $(find /path/to/bundle.lv2 -name '*.ttl')

For those unfamiliar with UNIX basics, the `find` command finds all files
matching a pattern, and putting a command in `$()` on a command line
substitutes the output of that command in place.  So, these commands simply
expand to `sord_validate` being called with a list of files as arguments.

Developers SHOULD include targets in their build scripts for running the
validator to ensure plugin data is correct before distribution.
