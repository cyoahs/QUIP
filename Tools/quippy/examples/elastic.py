from quippy import *

p = Potential("IP SW", """
   <SW_params n_types="2" label="PRB_31_plus_H">
   <comment> Stillinger and Weber, Phys. Rev. B  31 p 5262 (1984), extended for other elements </comment>
   <per_type_data type="1" atomic_num="1" />
   <per_type_data type="2" atomic_num="14" />
   <per_pair_data atnum_i="1" atnum_j="1" AA="0.0" BB="0.0"
         p="0" q="0" a="1.0" sigma="1.0" eps="0.0" />
   <per_pair_data atnum_i="1" atnum_j="14" AA="8.581214" BB="0.0327827"
         p="4" q="0" a="1.25" sigma="2.537884" eps="2.1672" />
   <per_pair_data atnum_i="14" atnum_j="14" AA="7.049556277" BB="0.6022245584"
         p="4" q="0" a="1.80" sigma="2.0951" eps="2.1675" />
   
   <!-- triplet terms: atnum_c is the center atom, neighbours j and k -->
   <per_triplet_data atnum_c="1"  atnum_j="1"  atnum_k="1"
         lambda="21.0" gamma="1.20" eps="2.1675" />
   <per_triplet_data atnum_c="1"  atnum_j="1"  atnum_k="14"
         lambda="21.0" gamma="1.20" eps="2.1675" />
   <per_triplet_data atnum_c="1"  atnum_j="14" atnum_k="14"
         lambda="21.0" gamma="1.20" eps="2.1675" />
   
   <per_triplet_data atnum_c="14" atnum_j="1"  atnum_k="1"
         lambda="21.0" gamma="1.20" eps="2.1675" />
   <per_triplet_data atnum_c="14" atnum_j="1"  atnum_k="14"
         lambda="21.0" gamma="1.20" eps="2.1675" />
   <per_triplet_data atnum_c="14" atnum_j="14" atnum_k="14"
         lambda="21.0" gamma="1.20" eps="2.1675" />
   </SW_params>
   """)

mp = MetaPotential("Simple", p)


a = diamond(5.44, 14)

c = fzeros((6,6))
c0 = fzeros((6,6))

metapot_calc_elastic_constants(mp, a, c=c, c0=c0, relax_initial=True, return_relaxed=True)

print 'Relaxed lattice constant'
print a.lattice[1,1]
print

print 'Unrelaxed elastic constants'
print (c0*GPA).round(decimals=3)
print

print 'Relaxed elastic constants'
print (c*GPA).round(decimals=3)
print

if len(sys.argv[1:]) == 1:
   a = Atoms(sys.argv[1])
   elastic_fields(a, a.lattice[1,1], c[1,1], c[1,2], c[4,4])
   a.show('Sig_xx')
else:
   print 'Usage: elastic.py <input file>'


