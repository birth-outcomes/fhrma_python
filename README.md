# FHRMA Python
Replicating components of the MATLAB FHRMA package within Python

## FHRMA (Fetal Heart Rate Morphological Analysis)

**Description:**

Source: https://github.com/utsb-fmm/FHRMA/tree/master

License: GPL-3.0

The dataset contains 155 FHR recordings in which a reference baseline, accelerations and decelerations have been annotated by expert consensus. 66 FHR recordings with a shared expert analysis have been included in a training dataset, and 90 other FHR recordings with a non-shared expert analysis have been included in an evaluation dataset. *Note: think this is referring to the training and test - with the evaluation not provided as below*. The dataset also contains the results produced by 12 re-coded automatic analysis methods from the literature.

Researchers wishing to evaluate their automatic analysis method should submit their results for comparison with the expert consensus. The baseline, accelerations, decelerations, and over-shoots are not publicly shared for the recordings in the evaluation dataset to avoid any training on those data.

Main information are published in : [1] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Delgranche, A., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - Fetal heart rate signal dataset for training morphological analysis methods and evaluating them against an expert consensus. Preprints pp. Submitted to data in brief,2019, DOI:10.20944/preprints201907.0039.v1

**Citation:**

The toolbox is related to several papers. Please cite those papers if you use any of the data or source code of this repository. [4] must be cited if you use the toolbox. [1] must be cited if you use the morphological analysis (baseline, Acceleration, deceleration) [3] must be cited if you use the morphological analysis dataset. [5] must be cited if you use the WMFB method (current best) for morphological analysis. [6] must be cited if you use the false signal detection, method, interface and/or dataset.
* [1] Houzé de l’Aulnoit, A., Boudet, S., Demailly, R., Delgranche, A., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - Automated fetal heart rate analysis for baseline determination and acceleration/deceleration detection: A comparison of 11 methods versus expert consensus. Biomedical Signal Processing and Control 49:113 -123,2019, DOI:10.1016/j.bspc.2018.10.002
* [2] Houzé de l'Aulnoit, Agathe, Boudet, Samuel, Demailly, Romain, Peyrodie, Laurent, Beuscart, Regis, Houzé de l'Aulnoit, Denis - Baseline fetal heart rate analysis: eleven automatic methods versus expert consensus. Engineering in Medicine and Biology Society (EMBC), 2016 IEEE 38th Annual International Conference of the pp. 3576--3581,2016, DOI:10.1109/EMBC.2016.7591501 Download on researchgate
* [3] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Delgranche, A., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - Fetal heart rate signal dataset for training morphological analysis methods and evaluating them against an expert consensus. Preprints pp. Submitted to data in brief,2019, DOI:10.20944/preprints201907.0039.v1
* [4] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Delgranche, A., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - A fetal heart rate morphological analysis toolbox for MATLAB. SoftwareX. 2020 Jan 1;11:100428. DOI:10.1016/j.softx.2020.100428
* [5] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - Fetal heart rate baseline computation with a weighted median filter. Computers in biology and medicine. 2019 Nov 1;114:103468. DOI:10.1016/j.compbiomed.2019.103468
* [6] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Peyrodie, L., Houzé de l’Aulnoit,D. - Use of deep learning to detect the maternal heart rate and false signals on fetal heart rate recordings. Biosensors 2022; 12(9):691. DOI:10.3390/bios12090691