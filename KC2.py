""" This is the script used to run experiment KC2 in the publication 
'The role of Isostasy in the evolution and architecture of fold and
 thrust belts 
 
 By Youseph Ibrahim 
 
 This was run using UWGeodynamics V2.9"""

import UWGeodynamics as GEO
import numpy as np

u = GEO.UnitRegistry

half_rate = 10 * u.millimeter / u.year
model_length = 44.8e3 * u.meter
surfaceTemp = 273.15 * u.degK
baseModelTemp = 1603.15 * u.degK
bodyforce = 2700 * u.kilogram / u.metre**3 * 9.81 * u.meter / u.second**2
rigidbasedensity = 4000. * u.kilogram / u.metre**3
velocity = 1. * u.centimeter / u.year

KL = model_length
Kt = KL / half_rate
KM = bodyforce * KL**2 * Kt**2
KT = (baseModelTemp - surfaceTemp)

GEO.scaling_coefficients["[length]"] = KL
GEO.scaling_coefficients["[time]"] = Kt
GEO.scaling_coefficients["[mass]"]= KM
GEO.scaling_coefficients["[temperature]"] = KT

Model = GEO.Model(elementRes=(800,200),
                  minCoord=(0. * u.kilometer, -12. * u.kilometer),
                  maxCoord=(64 * u.kilometer, 4. * u.kilometer),
                  gravity=(0.0, -9.81 * u.meter / u.second**2))


Model.outputDir="1cm_4000s3_O"


Model.diffusivity = 9e-7 * u.metre**2 / u.second
Model.capacity    = 1000. * u.joule / (u.kelvin * u.kilogram)

air = Model.add_material(name="Air", shape=GEO.shapes.Layer(top=Model.top, bottom=0 * u.kilometer))
air.density = 1. * u.kilogram / u.metre**3
air.diffusivity = 1e-6 * u.metre**2 / u.second
air.capacity = 1000. * u.joule / (u.kelvin * u.kilogram)

Loose_Sediment = Model.add_material(name="Loose_Sediment", shape=GEO.shapes.Layer2D(top=0. * u.kilometer, bottom=-0.2 * u.kilometer))
Loose_Sediment.radiogenicHeatProd = 7.67e-7 * u.watt / u.meter**3
Loose_Sediment.density  = 2000. * u.kilogram / u.metre**3

Strong_1 = Model.add_material(name="Strong_1", shape=GEO.shapes.Layer2D(top=-0.2 * u.kilometer, bottom=-0.7 * u.kilometer))
Strong_1.radiogenicHeatProd = 7.67e-7 * u.watt / u.meter**3
Strong_1.density  = 2600. * u.kilogram / u.metre**3

Weak_1 = Model.add_material(name="Weak_1", shape=GEO.shapes.Layer2D(top=Strong_1.bottom, bottom=-1.2 * u.kilometer))
Weak_1.radiogenicHeatProd = 7.67e-7 * u.watt / u.meter**3
Weak_1.density  = 2200. * u.kilogram / u.metre**3

Strong_2 = Model.add_material(name="Strong_2", shape=GEO.shapes.Layer2D(top=Weak_1.bottom, bottom=-1.7 * u.kilometer))
Strong_2.radiogenicHeatProd = 7.67e-7 * u.watt / u.meter**3
Strong_2.density  = 2600. * u.kilogram / u.metre**3

Weak_2 = Model.add_material(name="Weak_2", shape=GEO.shapes.Layer2D(top=Strong_2.bottom, bottom=-2.2 * u.kilometer))
Weak_2.radiogenicHeatProd = 7.67e-7 * u.watt / u.meter**3
Weak_2.density  = 2200. * u.kilogram / u.metre**3

Strong_3 = Model.add_material(name="Strong_3", shape=GEO.shapes.Layer2D(top=Weak_2.bottom, bottom=-2.7 * u.kilometer))
Strong_3.radiogenicHeatProd = 7.67e-7 * u.watt / u.meter**3
Strong_3.density  = 2600. * u.kilogram / u.metre**3


Weak_3 = Model.add_material(name="Weak_3", shape=GEO.shapes.Layer2D(top=Strong_3.bottom, bottom=-3.2 * u.kilometer))
Weak_3.radiogenicHeatProd = 7.67e-7 * u.watt / u.meter**3
Weak_3.density  = 2300. * u.kilogram / u.metre**3

Strong_4 = Model.add_material(name="Strong_3", shape=GEO.shapes.Layer2D(top=Weak_3.bottom, bottom=-3.7 * u.kilometer))
Strong_4.radiogenicHeatProd = 7.67e-7 * u.watt / u.meter**3
Strong_4.density  = 2600. * u.kilogram / u.metre**3


Weak_4 = Model.add_material(name="Weak_3", shape=GEO.shapes.Layer2D(top=Strong_4.bottom, bottom=-4.2 * u.kilometer))
Weak_4.radiogenicHeatProd = 7.67e-7 * u.watt / u.meter**3
Weak_4.density  = 2300. * u.kilogram / u.metre**3

Basement = Model.add_material(name="Continental Crust", shape=GEO.shapes.Layer2D(top=Weak_4.bottom, bottom=-7.5 * u.kilometer))
Basement.radiogenicHeatProd = 7.67e-7 * u.watt / u.meter**3
Basement.density  = 2720. * u.kilogram / u.metre**3

Beam = Model.add_material(name="Continental Crust", shape=GEO.shapes.Layer2D(top=Basement.bottom, bottom=Model.bottom))
Beam.radiogenicHeatProd = 7.67e-7 * u.watt / u.meter**3
Beam.density  = 4000. * u.kilogram / u.metre**3


rh = GEO.ViscousCreepRegistry()


Model.minViscosity = 5e18 * u.pascal * u.second
Model.maxViscosity = 5e23 * u.pascal * u.second

air.viscosity = 5e18 * u.pascal * u.second

Loose_Sediment.viscosity = 1e20 * u.pascal * u.second

Strong_1.viscosity = 1e22 * u.pascal * u.second

Strong_2.viscosity = 1e22 * u.pascal * u.second

Strong_3.viscosity = 1e22 * u.pascal * u.second

Strong_4.viscosity = 1e22 * u.pascal * u.second


Weak_1.viscosity = 5e20 * u.pascal * u.second

Weak_2.viscosity = 5e20 * u.pascal * u.second

Weak_3.viscosity = 5e20 * u.pascal * u.second

Weak_4.viscosity = 5e20 * u.pascal * u.second

Basement.viscosity = 1e23 * u.pascal * u.second

Beam.viscosity = 1e23 * u.pascal * u.second

Loose_Sediment.plasticity = GEO.DruckerPrager(name="Strong_1",
                                                cohesion=0. * u.megapascal,
                                                cohesionAfterSoftening=0.0 * u.megapascal,
                                                frictionCoefficient=0.01,
                                                frictionAfterSoftening=0.001,
                                                epsilon1=0., epsilon2=0.25)

Strong_1.plasticity = GEO.DruckerPrager(name="Strong_1",
                                                cohesion=5. * u.megapascal,
                                                cohesionAfterSoftening=0.5 * u.megapascal,
                                                frictionCoefficient=0.1,
                                                frictionAfterSoftening=0.01,
                                                epsilon1=0., epsilon2=0.25)
Weak_1.plasticity = GEO.DruckerPrager(name="Weak_1",
                                                cohesion=5. * u.megapascal,
                                                cohesionAfterSoftening=0.5 * u.megapascal,
                                                frictionCoefficient=0.1,
                                                frictionAfterSoftening=0.01,
                                                epsilon1=0., epsilon2=0.25)
Strong_2.plasticity = GEO.DruckerPrager(name="Strong_2",
                                                cohesion=5. * u.megapascal,
                                                cohesionAfterSoftening=0.5 * u.megapascal,
                                                frictionCoefficient=0.1,
                                                frictionAfterSoftening=0.01,
                                                epsilon1=0., epsilon2=0.25)
Weak_2.plasticity = GEO.DruckerPrager(name="Weak_2",
                                                cohesion=5. * u.megapascal,
                                                cohesionAfterSoftening=0.5 * u.megapascal,
                                                frictionCoefficient=0.1,
                                                frictionAfterSoftening=0.01,
                                                epsilon1=0., epsilon2=0.25)
Strong_3.plasticity = GEO.DruckerPrager(name="Strong_3",
                                                cohesion=5. * u.megapascal,
                                                cohesionAfterSoftening=0.5 * u.megapascal,
                                                frictionCoefficient=0.1,
                                                frictionAfterSoftening=0.01,
                                                epsilon1=0., epsilon2=0.25)
Weak_3.plasticity = GEO.DruckerPrager(name="Weak_3",
                                                cohesion=5. * u.megapascal,
                                                cohesionAfterSoftening=0.5 * u.megapascal,
                                                frictionCoefficient=0.1,
                                                frictionAfterSoftening=0.01,
                                                epsilon1=0., epsilon2=0.25)
Strong_4.plasticity = GEO.DruckerPrager(name="Strong_3",
                                                cohesion=5. * u.megapascal,
                                                cohesionAfterSoftening=0.5 * u.megapascal,
                                                frictionCoefficient=0.1,
                                                frictionAfterSoftening=0.01,
                                                epsilon1=0., epsilon2=0.25)
Weak_4.plasticity = GEO.DruckerPrager(name="Weak_3",
                                                cohesion=5. * u.megapascal,
                                                cohesionAfterSoftening=0.5 * u.megapascal,
                                                frictionCoefficient=0.1,
                                                frictionAfterSoftening=0.01,
                                                epsilon1=0., epsilon2=0.25)
Basement.plasticity = GEO.DruckerPrager(name="Basement",
                                                cohesion=40. * u.megapascal,
                                                cohesionAfterSoftening=4. * u.megapascal,
                                                frictionCoefficient=0.6,
                                                frictionAfterSoftening=0.06,
                                                epsilon1=0.1, epsilon2=0.25)

# eta     = 1e23 * u.pascal * u.second # Viscosity
# mu      = 2e9 * u.pascal # Shear Modulus

# alpha = eta / mu         # Maxwell relaxation time
# dt_e    = 20e3 * u.year  # Load relaxation time
# eta_eff = ( eta * dt_e ) / (alpha + dt_e)  # effective viscosity

# yieldStrength = 12e6 * (u.kilogram * u.meter**-1 * u.second**-2)

# minVisc = 1e19 * (u.kilogram * u.meter**-1 * u.second**-2) * u.second
# maxVisc = 1e24  * (u.kilogram * u.meter**-1 * u.second**-2) * u.second

# density = 2700 * u.kilogram / u.metre**3
# gravity = 9.81 * u.metre / u.second**2

# shearVelocity = 0.5 * u.centimetre / u.year

# print('Maxwell relaxation time = ', alpha.to(u.years))
# print("Observation time        = ", dt_e.to(u.year), dt_e)
# print("effective viscosity     = ", eta_eff.to(u.pascal * u.second))

Strong_1.elasticity = GEO.Elasticity(shear_modulus=2e9 * u.pascal,
                        observation_time=20000 * u.year)
Weak_1.elasticity = GEO.Elasticity(shear_modulus=2e9 * u.pascal,
                        observation_time=20000 * u.year)
Strong_2.elasticity = GEO.Elasticity(shear_modulus=2e9 * u.pascal,
                        observation_time=20000 * u.year)
Weak_2.elasticity = GEO.Elasticity(shear_modulus=2e9 * u.pascal,
                        observation_time=20000 * u.year)
Strong_3.elasticity = GEO.Elasticity(shear_modulus=2e9 * u.pascal,
                        observation_time=20000 * u.year)
Weak_3.elasticity = GEO.Elasticity(shear_modulus=2e9 * u.pascal,
                        observation_time=20000 * u.year)
Strong_4.elasticity = GEO.Elasticity(shear_modulus=2e9 * u.pascal,
                        observation_time=20000 * u.year)
Weak_4.elasticity = GEO.Elasticity(shear_modulus=2e9 * u.pascal,
                        observation_time=20000 * u.year)

Model.init_model()

Model.set_temperatureBCs(top=293.15 * u.degK, materials=[(air, 293.15*u.degK)])



Model.set_heatFlowBCs(bottom=(-0.044 * u.watt / u.metre**2, Beam))


import underworld.function as fn




conditions = [(Model.y <= GEO.nd(Beam.top), GEO.nd(-velocity)),
              (Model.y >  GEO.nd(Beam.top),
               GEO.nd(0. * u.centimeter / u.year)),
              (True, GEO.nd(0. * u.centimeter / u.year))]

fn_condition = fn.branching.conditional(conditions)

Model.set_velocityBCs(left=[fn_condition, None],
                      right=[-velocity, 0.],
                      top=[None, None],
                      bottom=GEO.LecodeIsostasy(reference_mat=Beam, average=False))


Model.init_model()


x = np.linspace(GEO.nd(Model.minCoord[0]), GEO.nd(Model.maxCoord[0]), 1000)
y = 0.

surface_tracers = Model.add_passive_tracers(name="Surface", vertices=[x,y])
moho_tracers = Model.add_passive_tracers(name="Moho", vertices=[x,y-GEO.nd(24.*u.kilometer)])


npoints = int(Model.maxCoord[0].to(u.kilometer).magnitude) # This is the number of points used to define the surface
x_surface = np.linspace(GEO.nd(Model.minCoord[0]), GEO.nd(Model.maxCoord[0]), npoints)
y_surface = -0.01 * u.kilometer

surface_tracers_no_erosion = Model.add_passive_tracers(name="Surface-NoErosion", vertices=[x_surface,y_surface], zOnly=True)
surface_tracers_erosion = Model.add_passive_tracers(name="Surface-Erosion", vertices=[x_surface,y_surface], zOnly=True)

def Hillslope_diffusion_basic():
    from scipy.interpolate import interp1d
    from scipy.interpolate import InterpolatedUnivariateSpline

    x = GEO.dimensionalise(surface_tracers_erosion.data[:,0], u.meter).magnitude
    z = GEO.dimensionalise(surface_tracers_erosion.data[:,1], u.meter).magnitude

    dx = (Model.maxCoord[0].to(u.meter).magnitude)/npoints

    total_time = (GEO.dimensionalise(Model._dt, u.year)).magnitude

    D = ((1.0e3 * u.meter**2 / u.year).to(u.meter**2 / u.year)).magnitude

    dt = min((0.2 * dx * dx / D), total_time)

    nts = int(round(total_time/dt))

    print('total time:', total_time, 'timestep:', dt, 'No. of its:', nts)

    z_orig = z.copy()

    for i in range(nts):
        qs = -D * np.diff(z)/dx
        dzdt = -np.diff(qs)/dx
        z[1:-1] += dzdt*dt


    x_nd = GEO.nd(x*u.meter)

    z_nd = GEO.nd(z*u.meter)


    if x_nd.shape[0] > 0.:
        f1 = interp1d(x_nd, z_nd, fill_value='extrapolate', kind='nearest')

        y_eroded_surface = f1(x_nd)

        y_eroded_surface[x_nd < GEO.nd(Update_material_LHS_Length*u.kilometer )] = 0.

        surface_tracers_erosion.data[:,1] = y_eroded_surface

        Model.materialField.data[(Model.swarm.data[:,1] > f1(Model.swarm.data[:,0])) & (Model.materialField.data[:,0] != air.index)] = air.index
        Model.materialField.data[(Model.swarm.data[:,1] < f1(Model.swarm.data[:,0])) & (Model.materialField.data[:,0] == air.index)] = Sediment.index


x_c, y_c = GEO.circles_grid(radius=0.1*u.kilometer,
                     minCoord=[Model.minCoord[0], Basement.bottom],
                     maxCoord=[Model.maxCoord[0], 0.*u.kilometer])

FSE_Crust = Model.add_passive_tracers(name="FSE_Crust", vertices=[x_c, y_c])

Model.init_model()

GEO.rcParams["default.outputs"].append("projStrainTensor")
GEO.rcParams["default.outputs"].append("projStressTensor")

Model.solver.set_inner_method("mumps")
Model.solver.set_penalty(1e6)

Model.run_for( 2200000.* u.year, restartStep=-1, restartDir="1cm_4000s3_O",  checkpoint_interval=5000. * u.year)
