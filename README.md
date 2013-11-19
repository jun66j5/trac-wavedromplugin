WaveDromPlugin
===================

Provides WaveDrom processor to render wavedrom drawings within Trac wiki page

Installation
------------

### 1. install the plugin ###

    $ easy_install https://github.com/jun66j5/trac-wavedromplugin/archive/trunk.zip

### 2. Enable the plugin ###

    ; conf/trac.ini
    [components]
    tracwavedrom.* = enabled

Example
-------
Paste the following in your Trac wiki

    {{{
    #!WaveDrom
    { "signal" : [{ "name": "Alfa", "wave": "01.zx=ud.23.45" }] }
    }}}

It would be render wavedrom drawings within Trac wiki page.
