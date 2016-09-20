Title: Developing

The best way to learn LV2 is by example.  The documentation and example
projects mentioned below are good starting points.  If you're writing a plugin
in C, copying one of the
[example plugins](http://lv2plug.in/git/cgit.cgi/lv2.git/tree/plugins) in LV2
as a template is recommended.

**What *not* to do:** If you are new to LV2, do *not* look at the
specifications and API references first!  These references provide detail, but
not necessarily a clear high-level view.  Start with the suggestions below, and
check the references later when you need specifics.


## Implementing Plugins

LV2 includes several well-documented example plugins which are simple
demonstrations of various plugin types.  If you prefer to read source code,
they are in the
[`plugins`](http://lv2plug.in/git/cgit.cgi/lv2.git/tree/plugins) directory of
the LV2 distribution.

There is also a "book" generated from the literate source code of these plugins
(work in progress):

* [Programming LV2 Plugins](http://lv2plug.in/book)

After writing a plugin, be sure to [validate](validating-lv2-data.html) the
data to check for typos and invalid constructs.


## Implementing Hosts

LV2 hosts use a library to handle all the details of plugin discovery,
investigation, and instantiation.  [Lilv](http://drobilla.net/software/lilv) is
the standard library for hosts:

* [Lilv API Reference](http://drobilla.net/docs/lilv/)

Plans are currently underway to incorporate simple and thoroughly documented hosts into LV2, along the lines of the plugin
examples.  Until then, several external projects serve as useful examples:

* [lv2apply](http://git.drobilla.net/cgit.cgi/lilv.git/tree/utils/lv2apply.c)
  is a very simple program included with Lilv which applies an LV2 plugin to an
  audio file.  Start here to learn the basics of loading an LV2 plugin.
* [Jalv](http://drobilla.net/software/jalv) is
  real-time [Jack](http://jackaudio.org) host which supports MIDI, embedded GUIs,
  presets, state saving, and other features.


## Reference

Most LV2 specifications have two parts: code and data.  The "specification"
documentation comes from the data, and defines/documents the various concepts
involved.  Start there to better understand an extension's purpose.

The API reference is generated from Doxygen, and serves the usual purpose.  Go
there for documentation about a specific function, struct, or define.

* [Specifications](http://lv2plug.in/ns)
* [API Reference](http://lv2plug.in/doc/html)


## Distribution and Packaging

* [Filesystem Hierarchy Standard](filesystem-hierarchy-standard.html)
* [Bundle Definition](bundle-definition.html)


## Contributing to LV2

Both LV2 itself and this site are stored in [git](http://lv2plug.in/git):

    :::sh
    git clone http://lv2plug.in/git/lv2
    git clone http://lv2plug.in/git/lv2site

There is also an official mirror on [Github](https://github.com/drobilla/lv2).

Contributions are most welcome.  If you plan to implement something
significant, it is a good idea to discuss it with the community on the mailing
list to be sure you're headed in the right direction.  Feel free to get
creative, but note that all released LV2 APIs are permanently stable, so
changes that break them can not be accepted.

A good entry point for beginners is writing new example plugins (using an
existing example as a template) to demonstrate some functionality in the
simplest possible way.

Happy hacking!


## Help

If you have any trouble or questions in general, ask on the
[mailing list](http://lists.lv2plug.in/listinfo.cgi/devel-lv2plug.in), or visit
us in [#lv2](http://webchat.freenode.net/?channels=lv2) on irc.freenode.net


## Other Resources

* [Logo](http://lv2plug.in/logo)
* [LV2 Achievement of GMPI Requirements](http://lv2plug.in/gmpi.html)
