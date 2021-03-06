

import numpy as np
import matplotlib.pyplot as plt
import mcml_scattering_pulsOx as mcml

medium = mcml.medium
model = mcml.model

air = medium("air", # name
             1.0, # n
             1.0, # g
             None, # z
             0, # mua
             0) # mus

####### TESTS #######
### from paper ###

N = 50000 # number of photons to send

    # input for data in table 1
test1 = medium("test 1", # name
                1.0, # n
                0.75, # g
                0.01, # z [cm]
                10.0, # mua
                90.0) # mus
testStructure1 = [air,test1,test1,air]
testNum1 = len(testStructure1)-2 # number of layers for test 1
                                # subtract first layer (air) and last layer
                                # for computation purposes. therefore, 
                                # add a duplicate of the final layer at
                                # the end of the medium structure
mcmlTest1 = model(testStructure1,testNum1)
mcmlTest1.run(N)
print(mcmlTest1.Tt_a[0])
mcmlDataTest1 = mcmlTest1.computeAndScaleArraySums()
print(mcmlTest1.Tt_a[0])

    # input for data in table 2
test2 = medium("test 2", # name
                1.5, # n
                0.0, # g
                0.01, # z [cm]
                10.0, # mua
                90.0) #mus
testStructure2 = [air,test2,test2,air]
testNum2 = len(testStructure2)-2 # number of layers for test 2
mcmlTest2 = model(testStructure2,testNum2)
mcmlTest2.run(N)
mcmlDataTest2 = mcmlTest2.computeAndScaleArraySums()



print("--- Test 1 Results ---")
print("A: ", mcmlTest1.A)
print("Rd: ", mcmlTest1.Rd)
print("Tt: ", mcmlTest1.Tt)
print("(van de Hurst) Error Rd: ",abs(0.09739-mcmlTest1.Rd)) # 0.09739 comes
                                                              # from paper
print("(van de Hurst) Error Tt", abs(0.66096-mcmlTest1.Tt)) # 0.66096 comes 
                                                            # from paper
print("(Prahl) Error Rd: ",abs(0.09711-mcmlTest1.Rd)) # 0.09711 comes from 
                                                        # paper
print("(Prahl) Error Tt", abs(0.66159-mcmlTest1.Tt)) # 0.66159 comes from 
                                                        # paper
                                                        
    # plot of radial distribution of reflectance (fig 3a in paper)
fig1 = plt.figure(101)
plt.plot(np.arange(0, 0.5*np.pi, mcmlTest1.da), mcmlTest1.Rd_a,"r-")
plt.xlabel("Exit Angle Alpha [rad]")
plt.ylabel("Rd_a [1/sr]")
plt.ylim((0,0.03))

    # plot of radial distribution of transmittance (fig 3b in paper)
fig2 = plt.figure(102)
plt.plot(np.arange(0, 0.5*np.pi, mcmlTest1.da), mcmlTest1.Tt_a, "b-")
plt.xlabel("Exit Angle Alpha [rad]") # Tt_ra records total transmittance,
plt.ylabel("Tt_a [1/sr]") # not diffuse transmittance,so unscattered light 
                            # (alpha = 0) will be recorded which is why 
                            # alpha = 0 gives a large result (Tt_a ~ 16)
 
   # plot of absorption for test 1 (not in paper)
# nr = mcmlTest1.nr
# nz = mcmlTest1.nz
# R, Z = np.meshgrid(np.arange(round(-0.5*nr),round(0.5*nr)), np.arange(0,nz))
# plt.contourf(mcmlTest1.A_rz[R,Z])
# cbar = plt.colorbar()
# cbar.ax.set_ylabel("photon 'weight' abosorbed per volume [1/cm**3]")
# plt.xlabel("r")
# plt.ylabel("z [cm]")
# plt.gca().invert_yaxis() # z-axis is directed down in simulation
# plt.show()

print("____________________________")
print("--- Test 2 Results ---")
print("A: ", mcmlTest2.A)
print("Rd: ", mcmlTest2.Rd)
print("Tt: ", mcmlTest2.Tt)
print("(Giovanelli) Error Rd2: ", abs(0.2600-mcmlTest2.Rd)) # 0.2600 comes 
                                                                # from paper
print("(Prahl) Error Rd2: ", abs(0.26079-mcmlTest2.Rd)) # 0.26079 comes 
                                                            # from paper

    # input for fig 4 in paper
# fluenceTest1 = medium("fluence", 1, 0.09, 1.0, 0.1, 100)
# fluenceTest2 = medium("fluence", 1.37, 0.09, 1.0, 0.1, 100)
# ftStruct1 = [air, fluenceTest1, fluenceTest1, air]
# ftStruct2 = [air, fluenceTest2, fluenceTest2, air]
# fTest1 = model(ftStruct1, len(ftStruct1)-2)
# fTest2 = model(ftStruct2, len(ftStruct2)-2)
# fTest1.run(N)
# fTest2.run(N)
# fTest1.computeAndScaleArraySums()
# fTest2.computeAndScaleArraySums()

# phi1 = fTest1.Phi_z
# phi2 = fTest2.Phi_z
# plt.plot(np.arange(0, 1, fTest1.dz), phi1, "r-")
# plt.plot(np.arange(0, 1, fTest2.dz), phi2, "b-")
# plt.xlim((0,1))
# plt.xlabel("z [cm]")
# plt.ylim((0,10))
# plt.ylabel("fluence")
