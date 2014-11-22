Title: Bundle Definition

An _LV2 Bundle_ is a directory containing the file `manifest.ttl` at the top
level, which is written in [Turtle](http://www.dajobe.org/2004/01/turtle/).
See the [Simple Amplifier manifest](http://lv2plug.in/book/#_manifest_ttl_in)
for an example.

Note that host developers should use a library, such as
[Lilv](http://drobilla.net/software/lilv) which automatically discovers and
loads bundles correctly.  This page describes the format of an LV2 bundle, but
host authors typically do not need to be concerned with the details.

* All information necessary for a host to discover (but not necessarily use)
  the contents of a bundle MUST be present in `manifest.ttl`.

* The host can discover which plugins are present by scanning `manifest.ttl`
  for statements like `<plugin-uri> a lv2:Plugin`.

* The data files for each plugin are listed with the `rdfs:seeAlso` property,
  for example `<plugin-uri> rdfs:seeAlso <datafile.ttl>`.

* Descriptions may be split across several files, and several bundles.  File
  boundaries are not significant.

* If a statement like `<extension-uri> a lv2:Specification` is found, then
  `<extension-uri>` is specification which may contain information like
  additional plugin categories, properties, and human-readable labels for
  things.  The host SHOULD load the corresponding data files.

* If a statement like `<preset-uri> a pset:Preset` is found, then
  `<preset-uri>` is a preset.  The `lv2:appliesTo` property indices which
  plugin the preset applies to.  See the [presets
  extension](http://lv2plug.in/ns/ext/presets) for details.



## Installation
 
* The name of a bundle itself MUST NOT be given any long-term significance (for
  example, in saved files).

    * Hosts may include special plugin bundles as part of their installation
      and depend on the existence of those bundles in their search path, but
      otherwise the discovery process should be identical.

    * Users MUST be able to rename installed bundle directories without any
      save files breaking.


## Discovery

* If a host encounters a bundle it does not "understand" or care about, it may
  simply ignore it.

* Hosts MUST consider *all* data files associated with a plugin/spec/preset/etc
  (including `manifest.ttl`) whenever looking for information about a plugin.


## Examples

Note that `manifest.ttl` may contain information about any number of things.  A
single bundle may contain several plugins, specifications, and presets.

However, it is discouraged to group too many things into a single bundle, since
this makes it difficult for the user to manage what they have installed.
Instead, put individual plugins, presets, etc., in their own bundle.  It is a
good idea to give related bundles common name prefix (not suffix) to make their
organization clear.

### Plugin

* `manifest.ttl` contains the triple `<pluginuri> a lv2:Plugin`.

* `manifest.ttl` MAY contain triples of the form `<pluginuri> rdfs:seeAlso
  <datafile.ttl>` which indicates that more information can be found in
  `datafile.ttl`.

### Specification

* `manifest.ttl` contains the triple `<specuri> a lv2:Specification`.

* `manifest.ttl` MAY contain triples of the form `<specuri> rdfs:seeAlso
  <datafile.ttl>` which indicates that more information can be found in
  `datafile.ttl`.

* Hosts SHOULD consider this information part of their LV2 specification.
  Hosts SHOULD NOT hard-code static assumptions about the specification, such
  as plugin categories or port types (though of course, they may not support
  unknown types).

### UI

* `manifest.ttl` contains the triple `<ui> a foo:MegaWidget` where
  `foo:MegaWidget` is a "widget" type the host understands (likely one defined
  in the [UI specification](http://lv2plug.in/ns/extensions/ui)).

* `manifest.ttl` MAY contain triples of the form `<ui> rdfs:seeAlso
  <datafile.ttl>` which indicates that more information can be found in
  `datafile.ttl`.

* `manifest.ttl` contains a triple of the form `<ui> ui:binary <ui.so>` where
  `ui.so` is the module to be dynamically loaded by the host.
