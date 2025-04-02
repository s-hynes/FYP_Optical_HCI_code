"""This is me learning how to use dictionaries to specify which images I want to save from the pipeline."""

d = {
    "0 phase mode": 1, 
    "pi phase mode": 0, 
    "0 overscan removed": 0, 
    "pi overscan removed": 0, 
    "0 ordinary ray": 0,
    "0 extraordinary ray": 0,
    "pi ordinary ray": 0,
    "pi extraoridnary ray": 0,
    "0 ordinary ray, star centered": 0,
    "0 extraordinary ray, star centered": 0,
    "pi ordinary ray, star centered": 0,
    "pi extraordinary ray, star centered": 0,
    "single difference 1024x512": 0,
    "intensity 1024x512": 0,
    "single difference 512x512": 1,
    "intensity 512x512": 0,
    "Qplus": 0,
    "Qminus": 0,
    "Uplus": 0,
    "Uminus": 0,
    "Qplus intensity": 0,
    "Qminus intensity": 0,
    "Uplus intensty": 0,
    "Uminus intensity": 0,
    "Q double difference": 0,
    "U double difference": 0,
    "Q intensity": 0,
    "U intensity": 0,
    "total intensity": 0,
    "polarised intensity": 0,
    "Q double difference average": 0,
    "U double difference average": 0,
    "Q intensity average": 1,
    "U intensity average": 0,
    "total intensity average": 0,
    "polarised intensity average": 0,
    "Q double difference corrected for instrumental polarisation": 0,
    "U double difference corrected for instrumental polarisation": 0,
    "polarised intensity corrected for instrumental polarisation": 0,
    "Qphi (azimuthal Q)": 0,
    "Uphi (azimuthal U)": 0,
    "U double difference, average of two detectors": 0,
    "Q double difference, average of two detectors": 0,
    "polarised intensity, average of two detectors": 0,
    "Qphi, average of two detectors": 0,
    "Uphi, average of two detectors": 0
    }

print("")
for key in d:
    if d[key]==True:
        print("Saving {0}".format(key))
print("")
for key, value in d.items():
    if value==True:
        print("Saving {0}".format(key))
print("")


if d["0 phase mode"]==True:
    print("Saving 0 phase mode")

"""
if d["pi phase mode"]==True:
    print("Saving pi phase mode")
"""