"""This is the input script for the data processing pipeline. To use the pipeline, the user needs to input the
following objects:

**dir_in_str**  - The directory containing the raw FITS files from ZIMPOL to be processed

**saving_dir**  - The directory to save the processed HCI images in

**save_steps**  - Boolean. Set this to \"True\" to save FITS files for intermediate steps in the pipeline

**save_fits**   - A dictionary used to specify which FITS files for intermediate steps should be saved"""

dir_in_str = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/GG-Tau-data"
saving_dir = "C:/Users/Stephen/OneDrive - National University of Ireland, Galway/24-25 FYP/Data/manipulated-data/GG-Tau/steps_presentation"
save_steps = True

save_fits = {
    "0 phase mode": 0,                                                      # 0
    "pi phase mode": 0,                                                     # 2
    "0 overscan removed": 0,                                                # 3
    "pi overscan removed": 0,                                               # 4
    "0 ordinary ray": 0,                                                    # 5
    "0 extraordinary ray": 0,                                               # 6
    "pi ordinary ray": 0,                                                   # 7
    "pi extraordinary ray": 0,
    "0 ordinary ray, star centered": 0,
    "0 extraordinary ray, star centered": 0,
    "pi ordinary ray, star centered": 0,
    "pi extraordinary ray, star centered": 0,
    "single difference 1024x512": 0,
    "intensity 1024x512": 0,
    "single difference 512x512": 0,
    "intensity 512x512": 0,
    "Qplus": 1,
    "Qminus": 1,
    "Uplus": 1,
    "Uminus": 1,
    "Qplus intensity": 1,
    "Qminus intensity": 1,
    "Uplus intensity": 1,
    "Uminus intensity": 1,
    "Q double difference": 1,
    "U double difference": 1,
    "Q intensity": 1,
    "U intensity": 1,
    "total intensity": 1,
    "polarised intensity": 1,
    "Q double difference average": 1,
    "U double difference average": 1,
    "Q intensity average": 1,
    "U intensity average": 1,
    "total intensity average": 1,
    "polarised intensity average": 1,
    "Q double difference corrected for instrumental polarisation": 1,
    "U double difference corrected for instrumental polarisation": 1,
    "polarised intensity corrected for instrumental polarisation": 1,
    "Qphi (azimuthal Q)": 1,
    "Uphi (azimuthal U)": 1,
    "Q double difference, average of two detectors": 1,
    "U double difference, average of two detectors": 1,
    "polarised intensity, average of two detectors": 1,
    "Qphi, average of two detectors": 1,
    "Uphi, average of two detectors": 1
    }