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

There is an [FHRMA github](https://github.com/utsb-fmm/FHRMA) and [FHRMA wiki](https://github.com/utsb-fmm/FHRMA/wiki).

The raw FHR records are available for the [training](https://github.com/utsb-fmm/FHRMA/tree/master/FHRMAdataset/traindata) and [test](https://github.com/utsb-fmm/FHRMA/tree/master/FHRMAdataset/testdata) data. These are .fhr files which can be opened with the fhropen.m function in MATLAB. They were sampled at 4Hz. For each sample, a uint32 serves as the UNIX timestamp for the beginning of the recording. Next, a uint16 corresponds to the FHR from the first sensor (multiplied by 4), a uint16 for the FHR signal from the second sensor (multiplied by 4) (unused here), a uint8 for the TOCO signal (multiplied by 2), and a uint8 reserved to store signal quality (unused here). 

The main folder in the GitHub repository contains functions from the software, including functions for analysis with the 12 methods, which follow a file structure of 'aa'm then method - e.g. [aamwmfb.m](https://github.com/utsb-fmm/FHRMA/blob/master/aamwmfb.m).

[The analyses folder in the github](https://github.com/utsb-fmm/FHRMA/tree/master/FHRMAdataset/analyses) contains MAT files which have record of when accelerations and decelerations occur for each record, according to the different methods. The methods are [listed here](https://github.com/utsb-fmm/FHRMA/wiki/FHRMA-dataset). As described on the [dataset page](https://github.com/utsb-fmm/FHRMA/wiki/FHRMA-dataset), these files contain:
* Filename (name of the record)
* Baseline (baseline signal sampled at 4Hz)
* Accelerations (2xn table with beginning and end of each acceleration in minutes)
* Decelerations (2xn table with beginning and end of each deceleration in minutes)
* Overshoots (2xn table with beginning and end of overshoots in minutes) (excluded from evaluation)
* Unreliable signal (periods of maternal heart rate or too much missing signal preventing good analysis) (excluded from evaluation)
* Not to analyse (period not to be analysed due to insufficient signal before or after for baseline positioning)
* Training data (boolean set to 1 if recording is part of the training dataset and 0 of part of evaluation)

The baseline, accelerations, decelerations, and over-shoots are not publicly shared for the recordings in the evaluation dataset to avoid any training on those data.

It states that the files are also available in WFDB format on the PhysioNet page, but I've not yet been able to identify the Physionet page.

These files are either from **expert evaluation, or automated analysis** from 12 different methods available in the literature. Methods in table below as from [[source]](https://doi.org/10.1016/j.softx.2020.100428), ordered by their performance in their evaluation of them. Not included in FHRMA but included in the leaderboard are two methods from Zhong et al. 2022, which perform in 1st and 3rd place.

| Function name | Filename | Publication | Baseline computation method | Acceleration/deceleration thresholding described? |
| --- | --- | --- | --- | --- |
| aamwmfb | WMFB_orig.mat | Boudet et al. (2020) | Based on a weighted median filter baseline (WMFB). The weights are set to the prior probabilities that the FHR is in the baseline state. The unstable FHR periods have low probabilities. Successive baselines are computed with a progressive trimming process. Periods far from previous baselines have also low probabilities. | Yes |
| aamlu | L_std.mat | Lu et Wei (2012) | A method using empirical mode decomposition; periods exhibiting significant differences between two successive local FHR minima are excluded from the baseline computation. | No (probably standard thresholding) |
| aamhouze | H_std.mat | Houzé et al. (1990) | Based on a series of logic rules applied to various signal derivatives, followed by a smoothing step. | No (not described clearly enough to be reprogrammed) |
| aamtaylor | T_orig.mat / T_std.mat | Taylor et al. (2000) | A linear low-pass filtering method with progressive trimming. | Yes |
| aamwrobel | W_std.mat | Wróbel et al. (2013) | Based on myriad filters: an intermediate approach, between a linear average filter and use of the mode. | No (probably standard thresholding) |
| aammongelli | MG_std.mat | Mongelli et al. (1997) | This method computes a primary mode and a secondary mode; the two modes can be switched, depending on continuity and frequency criteria. | No |
| aamayres | A_std.mat | Ayres de Campos et al. (2000) | Based on “frequent” FHR values in a 10-min moving window. | Yes (= standard thresholding) |
| aammantel | MT_orig.mat / MT_std.mat | Mantel et al. (1990) | The method uses the mode or another local maximum of the FHR histogram to obtain an initial baseline. The final baseline is obtained by progressively trimming the first baseline (based on Dawes et al.’s method). This method was developed for antepartum recording. | Yes |
| aampardey | P_std.mat | Pardey et al. (2002) | The method first uses the histogram’s mode or another local maximum. The second baseline is obtained by linear filtering of the FHR and trimming as a function of the first baseline (based on Dawes et al.’s method). | Yes (=standard thresholding) |
| aamjimenez | J_orig.mat / J_std.mat | Jimenez et al. (2002) | Unstable periods (with a derivative above a cut-off) are removed, and the baseline is calculated after smoothing the remaining signal. | Yes |
| aammaeda | MD_std.mat | Maeda et al. (2012) | The baseline is set to the FHR level that occurs most often within a 10 bpm-wide bin. | No (not described clearly enough to be reprogrammed) |
| aamcazares | C_orig.mat/ C_std.mat | Cazares et al. (2002) | Based on morphological filters; an opening filter removes accelerations and a closing filter removes decelerations. | Only described for acceleration (presumably the same for deceleration) |

It also contains work around identification of false signals which is described in [this pre-print](https://www.preprints.org/manuscript/202207.0131/v1) and in [these python files](https://github.com/utsb-fmm/FHRMA/tree/master/FS%20training%20python%20sources).

In their [presentation on YouTube](https://youtu.be/gjpBs4utlbM?si=Y4HOXwd0FEzbbZiD&t=1146), can see that the training and test data are from two different sources:
* Training dataset is 66 recordings, duration 90 min (30 min - 7 hours), digitial acquisition or scan, medium or hard to assess, consensus of 3 experts
* Test dataset is 90 recordings, duration 105 min (90 min - 120 min), digitial acquisition, easy or medium or hard to assess, 3 independent experts and a consensus

**Citation:**

The toolbox is related to several papers. Please cite those papers if you use any of the data or source code of this repository. [4] must be cited if you use the toolbox. [1] must be cited if you use the morphological analysis (baseline, Acceleration, deceleration) [3] must be cited if you use the morphological analysis dataset. [5] must be cited if you use the WMFB method (current best) for morphological analysis. [6] must be cited if you use the false signal detection, method, interface and/or dataset.
* [1] Houzé de l’Aulnoit, A., Boudet, S., Demailly, R., Delgranche, A., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - Automated fetal heart rate analysis for baseline determination and acceleration/deceleration detection: A comparison of 11 methods versus expert consensus. Biomedical Signal Processing and Control 49:113 -123,2019, DOI:10.1016/j.bspc.2018.10.002
* [2] Houzé de l'Aulnoit, Agathe, Boudet, Samuel, Demailly, Romain, Peyrodie, Laurent, Beuscart, Regis, Houzé de l'Aulnoit, Denis - Baseline fetal heart rate analysis: eleven automatic methods versus expert consensus. Engineering in Medicine and Biology Society (EMBC), 2016 IEEE 38th Annual International Conference of the pp. 3576--3581,2016, DOI:10.1109/EMBC.2016.7591501 Download on researchgate
* [3] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Delgranche, A., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - Fetal heart rate signal dataset for training morphological analysis methods and evaluating them against an expert consensus. Preprints pp. Submitted to data in brief,2019, DOI:10.20944/preprints201907.0039.v1
* [4] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Delgranche, A., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - A fetal heart rate morphological analysis toolbox for MATLAB. SoftwareX. 2020 Jan 1;11:100428. DOI:10.1016/j.softx.2020.100428
* [5] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Peyrodie, L., Beuscart, R., Houzé de l’Aulnoit,D. - Fetal heart rate baseline computation with a weighted median filter. Computers in biology and medicine. 2019 Nov 1;114:103468. DOI:10.1016/j.compbiomed.2019.103468
* [6] Boudet, S., Houzé de l’Aulnoit, A., Demailly, R., Peyrodie, L., Houzé de l’Aulnoit,D. - Use of deep learning to detect the maternal heart rate and false signals on fetal heart rate recordings. Biosensors 2022; 12(9):691. DOI:10.3390/bios12090691