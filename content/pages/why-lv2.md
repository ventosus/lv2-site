Title: Why LV2?

Unlike many popular audio plugin APIs, LV2 is a platform-agnostic
[Free Software](http://www.gnu.org/philosophy/free-sw.html) specification with
a liberal license permitting virtually any implementation (both free and
proprietary).

LV2 has been designed with extensibility in mind right from the start, so if
LV2 currently can't do what you need, functionality can be added without
breaking any pre-existing hosts or plugins.

## Features

* Audio, control, "control voltage" (audio-rate control), and event (e.g. MIDI) input and output.

* Expressive metadata, including:

    * "Meaningful" controls (e.g. gain or envelope attack) allowing intelligent host control or UI generation.

    * Control units (e.g. Hz, octaves, dB).

    * Multi-channel port groups (e.g. stereo, 5.1 surround, ambisonics).

* Decentralized extensibility: any developer can implement (almost) any feature within LV2.

* Graceful compatibility: features can be optional.

* Embeddable GUIs in any toolkit, with network transparent control.

* Plugin "bundles" may include any files, such as samples.

* Presets (bundled and/or user saved).

* Plugin state saving and restoring.

* Host-managed logging.

* Non-realtime plugin worker methods ("idiot-proof" non-realtime operations, like sample loading without dropouts).

* Message-based plugin communication, for advanced plugin control from UIs or other code.

* Transport awareness, both real time and tempo time (bars, beats, etc.).


## Bundles

Everything an LV2 plugin needs is bundled inside a "bundle" directory. Users
can easily manage their installations by moving, renaming, or deleting bundles
with any file manager.


## Plugin Metadata

LV2 separates static metadata from code, so information about installed plugins
can be discovered without loading any modules or executing any third-party
code.

Any data can be added to a plugin description without breaking compatibility.


## Simple Core API

The "core" API of LV2, [lv2.h](http://lv2plug.in/ns/lv2core/lv2.h), is
essentially `ladspa.h` with extensibility hooks added.  It is a simple C header
with the basic methods typical to audio plugins.


## Extensibility

While the core API of LV2 is very simple, extensions can add arbitrary
functionality.  The community works together to define standard extensions for
commonly needed functionality, but developers are free to implement any
extensions they need for their own applications.  This is particularly useful
for developing new functionality and testing it in a real application before
proposing a new standard extension.
