sublime-generate-uuid
=====================

Sublime Text plugin to generate a UUID at every cursor and copy it to the clipboard.

# Installation
## Manual

Sublime Text 2:

    git clone https://github.com/craighurley/sublime-generate-uuid.git \
    ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/sublime-generate-uuid

Sublime Text 3:

    git clone https://github.com/craighurley/sublime-generate-uuid.git \
    ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/sublime-generate-uuid

## Package Control

First, install the Package Control plugin, instructions here: http://wbond.net/sublime_packages/package_control.

Once you install Package Control, restart Sublime Text and bring up the Command Palette (<kbd>command+shift+p</kbd> on OS X, <kbd>super+shift+p</kbd> on Linux/Windows).

Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select "HL7" when the list appears.

# Usage
To generate a UUID (version 4), simply press the following keys:

- Linux: <kbd>ctrl+u</kbd>
- Windows: <kbd>ctrl+u</kbd>
- OS X: <kbd>ctrl+u</kbd>

Every time you generate a UUID, the UUID is also copied to the paste buffer.

# Info

- http://www.sublimetext.com
- http://en.wikipedia.org/wiki/Universally_unique_identifier
