Changelog
=========

For details and minor changes, please see the `version control log messages
<https://github.com/SpotlightKid/python-rtmidi/commits/master>`_.


Development
-----------

Enhancements / Changes:
  * Renamed example script ``midiwrapper.py`` to ``midioutwrapper.py`` to
    better indicate its function.

Fixes:
  * ``midiout`` example: removed surplus second argument to ``open_midioutput``
    left over from previous version of script.
  * Fixed example script file names in header comments.

2019-04-15 version 1.3.0
------------------------

Enhancements / Changes:
  * Added ``get_api_display_name`` module-level function.
  * Added ``get_api_name`` module-level function.
  * Added ``get_compiled_api_by_name`` module-level function.
  * Updated ``rtmidi`` sub-module to include all changes from upstream up to
    commit 791dfea.

Documentation:
  * Improved installation instructions and listed options recognized by
    ``setup.py``.


2019-01-18 version 1.2.1
------------------------

Fixes:
  * Fixed build when compiling with JACK support, but JACK version is too old
    to have ``jack_port_rename`` function (#40).

Project infrastructure:
  * Added Linux builds for Python 2.7 and 3.4 - 3.7 to Travis CI setup.


2019-01-13 version 1.2.0
------------------------

Project infrastructure:
  * RtMidi Sources and header are now included as a git sub-module from
    the 'python-rtmidi' branch of a fork_ of the upstream RtMidi repository.
    This fork incorporates changes and fixes by pull requests to the
    upstream repository, which are (yet) unmerged, and some changes
    specific to python-rtmidi.

Enhancements / Changes:
  * Added ``get_rtmidi_version`` module-level function.
  * Added ``set_client_name`` and ``set_port_name`` methods to ``MidiIn``'s and
    ``MidiOut``'s base class.
  * Added a bunch of new custom exceptions, all derived from ``RtMidiError``.
  * A default error handler callback is now set for ``MidiIn`` and ``MidiOut``
    instances, which maps C++ level errors into custom Python exceptions.

Examples:
  * Enhanced example script ``midiwrapper.py`` with methods for more MIDI
    messages, including sending all kinds of controller change and of (N)RPN
    messages.

Fixes:
  * Fixed SysEx message reception in JACK backend in RtMidi: messages broken up
    over several events are now collected into a single event before being
    passed to the input callback or returned by ``MidiIn.get_message``.
  * Fixed missing MIDI message input filtering in JACK backend in RtMidi:
    ``MidiIn.ignoreTypes`` now works as intended.

Testing:
  * Restructured tests in ``test_rtmidi`` and added tests for new methods.


.. _fork:
    https://github.com/SpotlightKid/rtmidi


2018-10-10 version 1.1.2
------------------------

Project infrastructure:
  * Added bagdes and link to documentation to README visible on GitHub page.
  * Tweaked project description wording.
  * Updated copyright year in various documentation files.

Building:
  * Binary wheels for Windows and OS X for Python 2.7, 3.5 (only Windows), 3.6,
    and 3.7 are automatically built on AppVeyor resp. Travis CI and uploaded to
    PyPI when a new release tag is pushed to GitHub.

    Thanks to Benoit Pierre for the PR (#36).
  * Upload Gzip'ed instead Bzip'ed tarballs for source distributions to PyPI.
  * ``python setup.py test`` now runs ``tox``, so ``tests_require`` in
    ``setup.py`` is empty now. We want dependencies to be only handled by
    ``pip``, never by ``setuptools``.

Documentation:
  * Minor additions, updates, fixes and wording tweaks.


2018-08-06 version 1.1.1
------------------------

Building:
  * Rebuild ``src/_rtmidi.cpp`` with current Cython for Python 3.7
    compatibility.
  * Remove testing with Python 3.3 environment from ``tox.ini`` and add Python
    3.6 and 3.7.
  * Update dev requirements for Python 3.7 compatibility.
  * Upload releases with twine.

Documentation:
  * Python 3.3 is not officially tested or supported anymore.


2017-04-21 version 1.1.0
------------------------

Project infrastructure:
  * Updated project homepage URL; copyright year and link to docs in readme.

Building:
  * Added script to automate updating github pages docs.

Enhancements / Changes:
  * Synced with upstream RtMidi_ (2.1.1-907a94c).
  * Applied patch from https://github.com/thestk/rtmidi/pull/89.
    This means that when using the ALSA API port names are reported in the form
    ``<client name>:<port name> <port id>`` (this change was actually already
    in version 1.0.0).
  * Added new ``MidiIn`` / ``MidiOut`` method ``is_port_open``.
  * ``MidiIn`` / ``MidiOut`` constructors and ``open_port`` /
    ``open_virtual_port`` methods now raise ``TypeError`` when an
    invalid type is passed as the client resp. port name.

Documentation:
  * Various small documentation improvements.

Examples:
  * Basic examples: some clean-up, more comments, updated API usage.
  * Added new advanced example script ``midiwrapper.py``.
  * Added new advanced example script ``recvrpn.py``.
  * ``wavetablemodstep.py``: added command line param to set controller number.
  * ``midi2command``: Fixed wrong mock lru_cache substitution for Python < 3.2.


2016-11-07 version 1.0.0
------------------------

Project infrastructure:
  * Added automatic documentation publishing on readthedocs.org.

Documentation:
  * Added auto docs for MidiIn/MidiOut classes to sphinx docs.
  * Removed pre-release related information from installation docs.

Building:
  * Added generated INSTALL.rst to repo to make ReadTheDocs integration work.

Examples:
  * Added new example script ``panic.py``.


2016-10-09 version 1.0.0rc1
---------------------------

Project infrastructure:
  * Moved repository to Github.

Fixes:
  * ``midiutil.open_midiport``:

    * Correctly report and log I/O direction and instance type.
    * Fix naming of virtual port.

Enhancements / Changes:
  * Synced with upstream RtMidi_ (2.1.1-399a8ee).
  * ``midiutil``:

    * The function ``midiutil.open_port`` has been renamed to ``open_midiport``.

    * Added convenience functions ``open_midiinput`` and ``open_midioutput``,
      which wrap ``open_midiport``.

    * RtMidi API to use can be specified via the ``RTMIDI_API`` environment
      variable. Only used when ``API_UNSPECIFIED`` is passed for the ``api``
      argument. Value should be one of the ``API_*`` constant names with out
      the ``API_`` prefix, e.g. ``UNIX_JACK`` for the Jack API.

  * Cython wrapper class hierarchy restructured to better match the underlying
    C++ classes and remove code duplication.
  * Some source code re-ordering was done.

Documentation:
  * Added basic structure and initial content of Sphinx documentation.
  * Documented exceptions raised by ``MidiIn/Out.open_[virtual_]port()``.
  * Some docstring corrections and formatting fixes.

Building:
  * Simplified ``setup.py`` by throwing out old compatibility stuff.
  * Explicitly call ``PyEval_InitThreads`` from Cython code instead of using
    undocumented compiler macro.

Examples:
  * Moved `osc2midi` example into its own repository at
    https://github.com/SpotlightKid/osc2rtmidi.git

  * Add new ``sequencer`` example.

  * Add new ``noteon2osc`` example.

  * ``midifilter``:

    * Moved ``main.py`` to ``__main__.py``, removed old code and fixed command
      line args access.
    * Streamlined event matching.
    * Added ``CCToBankChange`` filter.
    * ``Queue`` module renamed to ``queue`` in Python 3.
    * Fixed opening of output port erroneously used ``"input"``.
    * Fixed positional command line args handling.
    * Set command name for argparse.

  * ``midi2command``:

    * Added README.
    * Added command line option to select backend API.
    * Catch errors when opening port.
    * Set client and port name.
    * Cache command lookup (Python 3.2+ only).

  * ``sysexsaver``:

    * Moved ``main.py`` to ``__main__.py``, some refactoring.
    * ``models.py``: Fixed wrong entry for manufacturer ``(0, 32, 81)``.
    * Moved module level code into ``main`` function.
    * Include model name in output file, if possible.

  * ``drumseq``:

    * Fixed global access in ``Sequencer`` class.
    * Use ``args.FileType`` for pattern command line args.


2014-06-11 version 0.5b1
------------------------

Fixes:
  * Synced RtMidi_ code with git repo @ 2c7a6664d6, which fixed several issues
    (see https://github.com/thestk/rtmidi/issues?state=closed).
  * ``MidiIn/Out.open_virtual_port`` returns ``self`` for context manager
    support, consistent with ``MidiIn/Out.open_port``.
  * Fix Python <= 2.6 incompatible encode method call (python-rtmidi
    officially only supports Python >= 2.7). Thanks to Michiel Overtoom for
    reporting this.
  * Respect passed MIDI api when requesting MidiOut instance from
    ``midiutil.open_midiport``.

.. _rtmidi: https://github.com/thestk/rtmidi

Enhancements / Changes:
  * Support for Windows Kernel Streaming API was removed in RtMidi (it was
    broken anyway) and consequently in ``python-rtmidi`` as well.
  * Raise ``RtMidiError`` exception when trying to open a (virtual) port on a
    ``MidiIn/Out`` instance that already has an open (virtual) port.
  * Add some common synonyms for MIDI events and controllers and some source
    comments about controller usage to ``midiconstants`` module.

Documentation:
  * Fix and clarify ``queue_size_limit`` default value in docstrings
  * Various docstring consistency improvements and minor fixes.

Examples:
  * New example script ``midi2command.py``, which executes external commands
    on reception of configurable MIDI events, with example configuration.
  * New example directory ``drumseq`` with a simple drum pattern sequencer
    and example drum patterns. Thanks to Michiel Overtoom for the original
    script!


2013-11-10 version 0.4.3b1
--------------------------

Building:
  * Add numeric suffix to version number to comply with PEP 440.
  * Add missing ``fill_template.py`` to source distribution.
  * Set default setuptools version in ``ez_setup.py`` to 1.3.2, which
    contains fix for bug #99 mentioned below.

Documentation:
  * Add note to installation guide about required ``--pre`` option with pip.


2013-11-07 version 0.4.2b
-------------------------

Fixes:
  * Add missing ``API_*`` constant to list of exported names of ``_rtmidi``
    module.

Enhancements / Changes:
  * Change default value of ``encoding`` argument of ``get_ports`` and
    ``get_port_name`` methods to `"auto"`, which selects appropriate encoding
    based on system and backend API used.

  * Add ``api`` parameter to ``midiutil.open_midiport`` function to select
    backend API.

  * Make client name for ``MidiOut`` and `` MidiIn`` different again,
    because some backend APIs might require unique client names.

Building:
  * Include workaround for setuptools bug (see bitbucket issue #99) in
    setup file.

  * Add custom distutils command to fill placeholders in ``INSTALL.rst.in``
    template with release meta data.

  * Setuptools is now required, pure distutils won't work anymore, so removing
    the fallback import of ``setup`` from distutils.


2013-11-05 version 0.4.1b
-------------------------

Building:
  * Include missing ``_rtmidi.cpp`` file in source distribution.

Documentation:
  * Fill in release data placeholders in ``INSTALL.rst``.


2013-11-05 version 0.4b
-----------------------

Fixes:
  * Fix string conversion in constructors and ``open_*`` methods.

  * Change default value ``queue_size_limit`` argument to ``MidiIn``
    constructor to 1024.

  * Update version number in ``RtMidi.cpp/h`` to reflect actual code state.

Enhancements / Changes:
  * Elevated development status to beta.

  * Allow ``MidiIn/Out.open_port`` methods to be used with the ``with``
    statement and the port will be closed at the end of the block.

  * ``MidiIn``/``MidiOut`` and ``open*()`` methods: allow to specify ``None``
    as client or port name to get the default names.

  * Move ``midiconstants`` module from examples into ``rtmidi`` package
    and added ``midiutil`` module.

  * ``midiutils.open_midiport``:

    * Allow to pass (substring of) port name as alternative to port number.
    * Re-raise ``EOFError`` and ``KeyboardInterrupt`` instead of using
      ``sys.exit()``.
    * Add ``client_name`` and ``port_name`` arguments.
    * Add ``use_virtual`` argument (default ``False``) to request opening
      of a virtual MIDI port.
    * Add ``interactive`` keyword argument (default ``True``) to disable
      interactive prompt for port.

  * Raise ``NotImplemented`` error when trying to open a virtual port with
    Windows MultiMedia API.

  * Change default name of virtual ports.

Documentation:
  * Re-organize package description and installation instructions into several
    files and add separate text files with changelog and license information.

  * Add detailed instructions for compiling from source on Windows

  * Add docstrings to all methods and functions in ``_rtmidi`` module.

  * Add docstring for ``midiutils.open_midiport`` function.


Examples:
  * Add new example package ``osc2midi``, a simple, uni-directional OSC to MIDI
    mapper.

  * New example script ``sendsysex.py`` to demonstrate sending of MIDI system
    exclusive messages.

  * New example script ``wavetablemodstep.py`` to demonstrate sending of
    MIDI control change messages.

  * New ``sysexsaver`` example.

  * Convert ``midifilter`` example script into a package.

  * Upgrade  from ``optparse`` to ``argparse`` in example scripts.

  * Enable logging in test scripts.


Building:
  * Switch from ``distribute`` back to ``setuptools``.

  * Include ``ez_setup.py`` in source distribution.

  * Include examples in source distribution.

  * Install ``osc2midi`` example as package and command line script.

  * Enable C++ exceptions on Windows build.


2013-01-23 version 0.3.1a
-------------------------

Enhancements:
    * Increase sysex input buffer size for WinMM API again to 8192 (8k) bytes.
      Requested by Martin Tarenskeen.


2013-01-14 version 0.3a
-----------------------

Bug fixes:
    * Add ``encoding`` parameter to ``get_port_name`` methods of ``MidiIn``
      and ``MidiOut`` to be able to handle non-UTF-8 port names, e.g. on
      Windows (reported by Pierre Castellotti).
    * Add ``encoding`` parameter to ``get_ports`` method as well and pass it
      through to ``get_port_name``. Use it in the test scripts.

Enhancements:
    * Increase sysex input buffer size for WinMM API to 4096 bytes.

Examples:
    * Add new ``midifilter.py`` example script.

Building:
    * Add ``setuptools``/``distribute`` support.


2012-07-22 version 0.2a
-----------------------

Bug fixes:
    * Fix uninitialized pointer bug in ``RtMidi.cpp`` in 'MidiOutJack' class,
      which caused a warning in the jack process callback when creating a
      ``MidiOut`` instance with the JACK API.
    * ``testmidiin_*.py``: fix superfluous decoding of port name (caused error
      with Python 3).

Enhancements:
    * Simplify some code, some things gleaned from rtmidi_python.
    * Documentation typo fixes and more information on Windows compilation.
    * Enhancements in test scripts:

      * ``test_probe_ports.py``: Catch exceptions when creating port.
      * ``test_midiin_*.py``:

        * Better error message for missing/invalid port number.
        * Show how to convert event delta time into absolute time when
          receiving input.

Building:
    * Building on OS X 10.6.9 with CoreMIDI and JACK for OS X successfully
      tested and test run without errors.
    * WinMM support now compiles with Visual Studio 2008 Express and tests
      work under Windows XP SP3 32-bit.
    * Add command line option to exclude WinMM or WinKS API from compilation.
    * Add missing ``extra_compile_args`` to Extension kwargs in setup file.
    * Add ``library_dirs`` to Extension kwargs in setup file.
    * Use ``-frtti`` compiler option on OS X (neccessary on 10.7?).
    * Fix file name conflict on case-insensitive file systems by prefixing
      ``rtmidi.{pyx,cpp}`` with an underscore
    * Provide correct compiler flags for compiling with Windows MultiMedia API.
    * Adapt windows library and include path for Visual Studio 2008 Express.
    * add support for compiling with Windows Kernel Streaming API (does not
      not compile due to syntax errors in RtMidi.cpp yet).


2012-07-13 version 0.1a
-----------------------

First public release.
