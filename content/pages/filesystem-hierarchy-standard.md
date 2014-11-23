Title: Filesystem Hierarchy Standard

This page defines the standard locations where LV2 data should be installed.
All LV2 data is installed in [bundles](bundle-definition.html) which are discovered by hosts and other tools.

LV2 bundles are self-contained and may contain any kind of data (binary, text, executable, system-specific, portable, etc.).  These different kinds of data are not installed to separate paths as in the traditional Unix FHS.  There is one important distinction, however: user-specific and system-wide bundles.  User-specific bundles are likely writable by the user, while system-wide bundles appear to all users and are read-only.

## Standard Paths

LV2 bundles (directories typically named like "foo.lv2") SHOULD be in these standard locations:

Platform | User Specific                      | System Wide
---------|------------------------------------|------------------------------
Unix     | `$HOME/.lv2`                       | `$PREFIX/lib/lv2`
Mac OS X | `$HOME/Library/Audio/Plug-Ins/LV2` | `/Library/Audio/Plug-Ins/LV2`
Windows  | `%APPDATA%/LV2`                    | `%COMMONPROGRAMFILES%/LV2`

`$PREFIX` should be /usr/local by default in all source distributions.

## Bundle Discovery

The environment variable `LV2_PATH` is the search path for LV2 bundles.  Like the `PATH` variable for programs, it is colon-delimited on Unix and OSX, semicolon-delimited on Windows, and searched from left to right.  Based on the above locations, the default `LV2_PATH` is:

Platform | Default Path
---------|-------------
Unix     | `$HOME/.lv2:/usr/local/lib/lv2:/usr/lib/lv2`
Mac OS X | `$HOME/Library/Audio/Plug-Ins/LV2:/Library/Audio/Plug-Ins/LV2:/usr/local/lib/lv2:/usr/lib/lv2`
Windows  | `%APPDATA%/LV2;%COMMONPROGRAMFILES%/LV2`

## User Saved Data (e.g. Presets)

Hosts may wish to write data to bundles at run time (e.g. to save a preset, metadata, or even new plugins).  The user specific portion of LV2_PATH should be used for this so hosts will automatically discover this data.  It is best to write separate bundles for such things so the user can easy manage them with the shell or file manager.  Whenever writing to a bundle, a file lock should be held on the `manifest.ttl` file.

## Bundle Names

Bundle directory names are NOT strong identifiers, and may be different from system to system (or at different times on the same system).  Users may change them freely for any reason without fear of breakage.  Accordingly, hosts *MUST NOT_' attach significance to bundle names between invocations (e.g. in save files).  LV2 plugins and other resources '_MUST* be referred to by URI in save files, NOT by file system path.
