Title: Why LV2?

Unlike many popular audio plugin APIs, LV2 is a platform-agnostic
[Free Software](http://www.gnu.org/philosophy/free-sw.html) specification with
a liberal license.

## Features

* Audio, control, "control voltage" (audio-rate control), and event (e.g. MIDI) input and output.
* Expressive metadata, including:
    * "Meaningful" controls (e.g. gain or envelope attack) allowing intelligent host control or UI generation.
    * Control units (e.g. Hz, octaves, dB).
    * Multi-channel port groups (e.g. stereo, 5.1 surround, ambisonics).
* Extensibility: almost any feature is possible within LV2.
* Graceful compatibility: features can be optional.
* Embeddable GUIs in any toolkit, with network transparent control.
* Plugin "bundles" may include any files, such as samples.
* Presets, both bundled and user saved, in the same format.
* Plugin state saving and restoring.
* Host-managed logging.
* Non-realtime plugin worker methods ("idiot-proof" non-realtime operations, like sample loading without dropouts).
* Message-based plugin communication, for advanced plugin control from UIs or other code.
* Transport awareness, both real time and musical time.


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

The more powerful features of LV2 are built as "extensions" on the core API.
The community works together to define standard extensions for commonly needed
functionality, but developers are free to implement any extensions they need
for their own applications.  This is particularly useful for developing new
functionality and testing it in a real application before proposing a new
standard extension.

This makes improving the LV2 standard a frictionless process for developers,
but standard extensions are not second-class citizens.  If you have no need for
new features, or interest in developing LV2 itself, you can simply treat the
core and standard extensions as a unified API.
