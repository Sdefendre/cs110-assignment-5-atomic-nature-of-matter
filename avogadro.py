import math
import stdio

# Physical constants
R = 8.31457      # Universal gas constant, J/K/mol
TEMP = 297       # Absolute temperature, Kelvin
ETA = 9.135e-4   # Viscosity of water, Ns/m^2
RHO = 0.5e-6     # Radius of bead, m
METERS_PER_PIXEL = 0.175e-6  # Meters per pixel

# Entry point.
def main():
    # Read all displacements (in pixels) from stdin
    displacements = []
    while not stdio.isEmpty():
        val = stdio.readFloat()
        displacements.append(val)

    n = len(displacements)

    # Convert to meters and sum squared values
    sum_rsquared = 0.0
    for r_pixels in displacements:
        r_meters = r_pixels * METERS_PER_PIXEL
        sum_rsquared += r_meters * r_meters

    # Einstein-Smoluchowski: sigma^2 = 2*D*dt, so D = sigma^2 when dt=0.5
    # sigma^2 = sum(r^2) / (2n)
    sigma_squared = sum_rsquared / (2.0 * n)

    # Stokes-Einstein: D = k*T / (6*pi*eta*rho)  =>  k = 6*pi*D*eta*rho / T
    k = 6.0 * math.pi * sigma_squared * ETA * RHO / TEMP

    # Avogadro's constant: R = k * NA  =>  NA = R / k
    NA = R / k

    stdio.writeln("%.6e" % NA)

if __name__ == "__main__":
    main()
