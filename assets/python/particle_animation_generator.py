

import numbers


number_of_particles = 100
animation_time = 6 / 100

print(animation_time)

for i in range(number_of_particles):
    print(".particle:nth-child({number_of_particles}n + {}) {".format(number_of_particles, i + 1))
    print("    -webkit-animation-delay: 0.{}s".format(i))
    print("}\n")