#!/usr/bin/env python
#
# bankchange.py
# Stephane Gagnon
# www.StephaneGagnon.net
# Send a bank select cc0, cc32, pc
# Optionally send a note, velocity and duration
#

import argparse
import logging
import sys
import time

from rtmidi.midiutil import open_midiport
from rtmidi.midiconstants import *


log = logging.getLogger('bankchange')


# Message Container
class MidiMessage(object):
    def __init__(self, midiout, channel=None):
        self.midiout = midiout
        self.channel = channel - 1

    def all_notes_off(self):
        self.midiout.send_message([CONTROLLER_CHANGE + self.channel, 120, 0])

    def bank_select(self, msb=None, lsb=None, program=None):
        BankSelect(self.midiout, self.channel, msb, lsb, program).send()

    def send_note(self, note=None, velocity=100, duration=1):
        Note(self.midiout, self.channel, note, velocity, duration).play()


# Note object
class Note(object):
    def __init__(self, midiout, channel=None, note=None, velocity=100,
                 duration=1):
        self.midiout = midiout
        self.note_on = [NOTE_ON + channel, note, velocity]
        self.note_off = [NOTE_OFF + channel, note, 0]

        if duration is None:
            self.duration = 1
        else:
            self.duration = duration

        if velocity is None:
            velocity = 100

    def play(self):
        """Play the note."""
        self.midiout.send_message(self.note_on)
        time.sleep(self.duration) # note length
        self.midiout.send_message(self.note_off)


# Bank Select object
class BankSelect(object):
    def __init__(self, midiout, channel=None, msb=None, lsb=None,
                 program=None):
        self.midiout = midiout
        self.channel = channel
        self.program = program - 1
        self.msb = msb
        self.lsb = lsb

        self.bank_select_msb = [CONTROLLER_CHANGE + self.channel, BANK_SELECT,
                                self.msb]
        self.bank_select_lsb = [CONTROLLER_CHANGE + self.channel,
                                BANK_SELECT_LSB, self.lsb]
        self.program_change = [PROGRAM_CHANGE + self.channel, self.program]

    def send(self):
        """Send a bank change."""

        self.midiout.send_message(self.bank_select_msb)
        self.midiout.send_message(self.bank_select_msb)
        self.midiout.send_message(self.program_change)
        # give time for the MIDI device to process the bank change
        # before sending note if specified
        time.sleep(0.1)


def main(args=None):
#
#    Main program function.
#
    parser = argparse.ArgumentParser(description='BankChange Script')
    parser.add_argument('-p', '--port', dest='port',
        help='MIDI output port name or number (default: open virtual input)')
    parser.add_argument('-v', '--verbose', action="store_true",
        help='verbose output')
    parser.add_argument('-c', '--channel', dest='channel', type=int,
        help='Channel number 1-16')
    parser.add_argument('-m', '--msb', dest='msb', type=int,
        help='MSB Value')
    parser.add_argument('-l', '--lsb', dest='lsb', type=int,
        help='LSB Value')
    parser.add_argument('-pc', '--program', dest='program', type=int,
        help='Program Change')
    parser.add_argument('-n', '--note', dest='note', type=int,
        help='Note Value')
    parser.add_argument('-vel', '--velocity', dest='velocity', type=int,
        help='Note velocity, default=100')
    parser.add_argument('-d', '--duration', dest='duration', type=int,
        help='Note duration, default=1')

    args = parser.parse_args(args if args is not None else sys.argv[1:])

    logging.basicConfig(format="%(name)s: %(levelname)s - %(message)s",
        level=logging.DEBUG if args.verbose else logging.WARNING)

    try:
        midiout, port_name = open_midiport(args.port, "output")
    except (EOFError, KeyboardInterrupt):
        return

    #log.info("Sending message out...")

    try:
        message = MidiMessage(midiout, args.channel)
        # Helper if you have hanging notes:
        # message.all_notes_off()
        message.bank_select(args.msb, args.lsb, args.program)

        if args.note is not None:
            message.send_note(args.note, args.velocity, args.duration)
    except:
        print("Unexpected error: %s" % sys.exc_info()[0])
    finally:
        print('Done')
        midiout.close_port()
        del midiout


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
