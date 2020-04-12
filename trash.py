# import diffractio
# from diffractio import degrees, mm, nm, np, plt, sp, um
# from diffractio.scalar_sources_XY import Scalar_source_XY
# # from matplotlib import rcParams
# # rcParams['figure.figsize']=[10,10]
# from matplotlib import cm
#
# x0 = np.linspace(-50*um, 50*um, 20000)
# y0 = np.linspace(-50*um, 50*um, 20000)
# wavelength = 0.01 * um
#
# u = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
# u.spherical_wave(A=1, r0=(-25 * um, -25 * um), z0=-5 * mm, radius=50 * um, mask=False)
# u1 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
# u1.spherical_wave(A=1, r0=(25 * um, -25 * um), z0=-5 * mm, radius=50 * um, mask=False)
# u2 = Scalar_source_XY(x=x0, y=y0, wavelength=wavelength)
# u2.spherical_wave(A=1, r0=(0 * um, 25 * um), z0=-5 * mm, radius=50 * um, mask=False)
#
# us = u + u1 + u2
#
# us.draw(kind='amplitude')
# plt.show()



