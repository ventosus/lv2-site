Title: Developing

The way to learn about implementing LV2 is by example.  The documentation and
example projects listed below have been created specifically for this purpose,
look at these first.  Copying an example as a template is recommended.


**What *not* to do:** If you are interested in implementing LV2, do *not* look
at the specifications and API references first!  These are *references* that do
not always provide a clear high-level view.  Once you've gotten started based
on the information below, if you need more specific detail, then the references
are useful.


## Implementing Plugins

LV2 includes several example plugins which are simple demonstrations of various
types of plugins and the features they require with thorough documentation.  If
you prefer to read source code, they are in the `plugins` directory of the LV2
distribution.

If you would prefer to read a document, there is also a "book" generated from
the literate source code of these plugins:

* [Programming LV2 Plugins](http://lv2plug.in/book)


## Implementing Hosts

LV2 hosts use a library to handle all the details of plugin discovery,
investigation, and instantiation.  [Lilv](http://drobilla.net/software/lilv) is
the standard library for this.

* [Lilv API Reference](http://drobilla.net/docs/lilv/)

Plans are currently underway to incorporate simple and thoroughly documented hosts into LV2, along the lines of the plugin
examples.  Until then, several external projects serve as useful examples:

* [lv2file](https://github.com/jeremysalwen/lv2file) is a very simple
  single-file program that applies an LV2 plugin to an audio file.

* [Jalv](http://drobilla.net/software/jalv) is a relatively simple yet
  fully-featured [Jack](http://jackaudio.org) host for LV2 plugins.  Start at
  the core, [jalv.c](http://dev.drobilla.net/browser/trunk/jalv/src/jalv.c),
  which weighs in at just under 1000 SLOC.  Jalv also supports MIDI, embedded
  GUIs, presets, state saving, and other features.


## Reference

Most LV2 specifications have two parts: code and data.  The "specification"
documentation comes from the data, and documents the various concepts in the
specification, with links to the API reference of the associated APIs.  After
examples, this is the best place to better understand an extension.

The API reference is generated from Doxygen, and serves the usual purpose.  Go
there for documentation about a specific function, struct, or define.

* [Specifications](http://lv2plug.in/ns)

* [API Reference](http://lv2plug.in/doc/html)


## Other Documentation

* [Filesystem Hierarchy Standard](filesystem-hierarchy-standard.html)

* [Validating LV2 Data](validating-lv2-data.html)

* [Bundle Defnition](bundle-definition.html)


## Contributing to LV2

Both LV2 itself and this site are stored in [git](http://lv2plug.in/git):

    :::sh
    git clone http://lv2plug.in/git/lv2
    git clone http://lv2plug.in/git/lv2site

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
