import subprocess
import julia

julia.install()
print("Julia installation done")
subprocess.call(['julia', '-e', 'import Pkg; Pkg.add("PastaQ")'])
print("PastaQ installation done")
