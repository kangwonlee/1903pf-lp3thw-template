# -*- coding: utf-8 -*-

import pylab as pl

theta_deg = pl.arange(0, 360 + 0.05, 0.1)

theta_rad = pl.deg2rad(theta_deg)

sine = pl.sin(theta_rad)

pl.plot(theta_deg, sine)

pl.grid(True)

pl.show()
#[F5] or right click & "Run Python File in Terminal"
