#type wasm
filetype = b'\0asm'
version = b'\x01\x00\x00\x00'
#----------------
sectiontype = b'\x01'
sectionsize = b'\x07'
#-----------------
numbertypes = b'\x01'
funcs = b'\x60'
parametrs = b'\x02'
parametrsid1 = b'\x7f'
parametrsid2 = b'\x7f'
numberofresults = b'\x01'
returnvalue = b'\x7f'
#-----------------
functionid = b'\x03'
sectionsize2 = b'\x02'
numberoffunctions = b'\x01'
indexcodes = b'\x00'
#-----------------
exports = b'\x07'
sectionsize3 = b'\x07'
numberexports = b'\x01'
lenname = b'\x03'
funcname = b'sum'
exportmode = b'\x00'
exportindex = b'\x00'
#--------------------
sectioncode = b'\x0a'
setioncodesize = b'\x09'
functioncount = b'\x01'
functionbodysize = b'\x07'
localdecl = b'\x00'
#--------------------
codes = b'\x20\x00\x20\x01\x6a\x0b'

print("\033c\033[43;30m\nCreating file...............\n")
with open("main.wasm", "wb") as f1:
    f1.write(filetype)
    f1.write(version)
    #-----------------
    f1.write(sectiontype)
    f1.write(sectionsize)
    #-----------------
    f1.write(numbertypes)
    f1.write(funcs)
    f1.write(parametrs)
    f1.write(parametrsid1)
    f1.write(parametrsid2)
    f1.write(numberofresults)
    f1.write(returnvalue)
    #-----------------
    f1.write(functionid)
    f1.write(sectionsize2)
    f1.write(numberoffunctions)
    f1.write(indexcodes)
    #-----------------
    f1.write(exports)
    f1.write(sectionsize3)
    f1.write(numberexports)
    f1.write(lenname)
    f1.write(funcname)
    f1.write(exportmode)
    f1.write(exportindex)
    #-----------------
    f1.write(sectioncode)
    f1.write(setioncodesize)
    f1.write(functioncount)
    f1.write(functionbodysize)
    f1.write(localdecl)
    #-----------------
    f1.write(codes)
