# FHRMA Python

Replicating components of the MATLAB FHRMA package within Python

## Context - features based on FIGO guidelines

In the context of the FIGO guidelines, the routinely judged FHR components, often called **FIGO-based or morphological features**, are the baseline heart rate, variability, accelerations, and decelerations. These components are the most robust indicators to ascertain fetal well-being. For this reason, in almost all studies that address automated CTG analysis, these basic morphological features are confirmed as an indispensable part of the analyses. The initial studies on automated CTG analysis focused on the detection of morphological features that clinicians examine with the naked eye, but this is challenging due to a lack of standards on how computers estimate the diagnostic indices.[[source]](https://doi.org/10.1016/j.bspc.2018.05.016)

Studies have since explored the use of other features from **linear, non-linear, discrete wavelet transform (DWT), empirical mode decomposition (EMD), time-frequency and image-based time-frequency (IBTF) domains**.[[source]](https://doi.org/10.1016/j.bspc.2018.05.016)

Refer to `03_literature_review` in the `ctg_exploratory` repository for some of the publications describing this, as well as examples of commercial software for this, that have been evaluated in clinical practice.

## Context - FHR baseline

The FHR baseline is defined as the **mean of the signal after accelerations and decelerations have been excluded**. It is challenging to define a method for determining the FHR baseline because:
* It has a circular definition, as accelerations and decelerations are defined as periods when the signal is consistently above or below the baseline.
* There is high variability in some recordings, making it hard to distinguish between change in the baseline, and an acceleration or deceleration.[[source]](https://doi.org/10.3389/fped.2023.1190441)

M'Barek et al. 2023 state that you can overcome this issue by calibrating your method on baselines, accelerations and decelerations annotated by a consensus of obstetricians (they use those on the FHRMA dataset).[[source]](https://doi.org/10.3389/fped.2023.1190441)

The FHRMA toolbox contains a range of published methods for FHR baseline calculation implemented within MATLAB.

## FHRMA (Fetal Heart Rate Morphological Analysis)

**Description:**

Source: https://github.com/utsb-fmm/FHRMA/tree/master

License: GPL-3.0

The dataset contains 155 FHR recordings in which a reference baseline, accelerations and decelerations have been annotated by expert consensus. 66 FHR recordings with a shared expert analysis have been included in a training dataset, and 90 other FHR recordings with a non-shared expert analysis have been included in an evaluation dataset. The dataset also contains the results produced by 12 re-coded automatic analysis methods from the literature.

Main information are published in : [1] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Delgranche, A., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - Fetal heart rate signal dataset for training morphological analysis methods and evaluating them against an expert consensus. Preprints pp. Submitted to data in brief,2019, DOI:10.20944/preprints201907.0039.v1

**Citation:**

The toolbox is related to several papers. Please cite those papers if you use any of the data or source code of this repository. [4] must be cited if you use the toolbox. [1] must be cited if you use the morphological analysis (baseline, Acceleration, deceleration) [3] must be cited if you use the morphological analysis dataset. [5] must be cited if you use the WMFB method (current best) for morphological analysis. [6] must be cited if you use the false signal detection, method, interface and/or dataset.
* [1] Houzé de l’Aulnoit, A., Boudet, S., Demailly, R., Delgranche, A., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - Automated fetal heart rate analysis for baseline determination and acceleration/deceleration detection: A comparison of 11 methods versus expert consensus. Biomedical Signal Processing and Control 49:113 -123,2019, DOI:10.1016/j.bspc.2018.10.002
* [2] Houzé de l'Aulnoit, Agathe, Boudet, Samuel, Demailly, Romain, Peyrodie, Laurent, Beuscart, Regis, Houzé de l'Aulnoit, Denis - Baseline fetal heart rate analysis: eleven automatic methods versus expert consensus. Engineering in Medicine and Biology Society (EMBC), 2016 IEEE 38th Annual International Conference of the pp. 3576--3581,2016, DOI:10.1109/EMBC.2016.7591501 Download on researchgate
* [3] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Delgranche, A., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - Fetal heart rate signal dataset for training morphological analysis methods and evaluating them against an expert consensus. Preprints pp. Submitted to data in brief,2019, DOI:10.20944/preprints201907.0039.v1
* [4] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Delgranche, A., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - A fetal heart rate morphological analysis toolbox for MATLAB. SoftwareX. 2020 Jan 1;11:100428. DOI:10.1016/j.softx.2020.100428
* [5] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - Fetal heart rate baseline computation with a weighted median filter. Computers in biology and medicine. 2019 Nov 1;114:103468. DOI:10.1016/j.compbiomed.2019.103468
* [6] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Peyrodie, L., Houzé de l’Aulnoit,D. - Use of deep learning to detect the maternal heart rate and false signals on fetal heart rate recordings. Biosensors 2022; 12(9):691. DOI:10.3390/bios12090691