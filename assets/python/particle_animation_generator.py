

import numbers


number_of_particles = 99
animation_time = 6 / 100

print(animation_time)

for i in range(number_of_particles):
    print(".particle:nth-child(99n + {}) ".format(i+1) + "{")
    print("    -webkit-animation-delay: 0.{}s".format(i + 1))
    print("}\n")