# Place to override setting elsewhere, in particular things set in Makefile.linux_x86_64_ifort_icc
# look in QUIP/arch/Makefile.linux_x86_64_ifort_icc for defaults set by arch
# 
# F77=ifort
# F90=ifort
# F95=ifort
# CC=icc
# CPLUSPLUS=icpc -Kc++
# FPP=ifort -E
# LINKER=ifort
# LIBTOOL=
# OPTIM=
# COPTIM=
# DEBUG=-g -traceback -check bounds -DDUMP_CORE_ON_ABORT 
# DEBUG=-g -traceback -DDUMP_CORE_ON_ABORT 
# CDEBUG=
MATH_LINKOPTS=-mkl
EXTRA_LINKOPTS=
USE_MAKEDEP=1
MAKEDEP=makedep.py
HAVE_CP2K=1
HAVE_VASP=1
HAVE_TB=1
HAVE_PRECON=0
HAVE_LOTF=1
HAVE_ONIOM=1
HAVE_LOCAL_E_MIX=1
HAVE_QC=1
HAVE_GAP=1
HAVE_GAP_FILLER=1
HAVE_QR=1
HAVE_THIRDPARTY=1
HAVE_FX=1
HAVE_SCME=1
HAVE_MTP=1
HAVE_MBD=1
HAVE_TTM_NF=0
HAVE_CH4=1
NETCDF4_LIBS=-lnetcdf
NETCDF4_FLAGS=
HAVE_NETCDF4=1
HAVE_MDCORE=0
HAVE_ASAP=0
HAVE_CGAL=0
HAVE_METIS=0
HAVE_LMTO_TBE=0
SIZEOF_FORTRAN_T=2
