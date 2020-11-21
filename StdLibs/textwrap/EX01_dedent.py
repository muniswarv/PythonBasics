#!/usr/bin/env python

import textwrap

measTempl = """
        **  Measure Capacitance
        .meas tran 
        .meas tran 
        """

measTempl = textwrap.dedent(measTempl)

print measTempl
