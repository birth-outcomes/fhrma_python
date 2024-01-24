% Investigate differences between MATLAB and Python

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Investigating Taylor et al. 2012 acceleration/deceleration function

clear;

% Set the record and the number of the expert analysis
record = 'train28';
i = 118;

% Change to the directory of the FHRMA add-on
cd '/home/amy/MATLAB Add-Ons/Collections/Fetal Heart Rate Morphological Analysis Toolbox (FHRMA)'

% Load expert analyses
load FHRMAdataset/analyses/expertAnalyses.mat

% Load the relevant FHR data
file = ['FHRMAdataset/traindata/', record, '.fhr'];

% Clean the FHR
[FHR1,FHR2,~,TOCO,timestamp] = fhropen(file);
[FHRi,FHRraw,TOCOi] = preprocess(FHR1,FHR2,TOCO,data(i).unreliableSignal);

% Make copy
FHRbl=FHRi;

bl1=butterfilt(FHRi,4,0,0.008,3,1);
FHRbl(FHRi-bl1>5)=0;
FHRbl(FHRi-bl1<-5)=0;

bl2=butterfilt(interpolFHR(FHRbl),4,0,0.006,3,1);
FHRbl(FHRi-bl2>5)=0;
FHRbl(FHRi-bl2<-5)=0;

bl3=butterfilt(interpolFHR(FHRbl),4,0,0.006,3,1);
FHRbl(FHRi-bl3>10)=0;
FHRbl(FHRi-bl3<-5)=0;

baseline=butterfilt(interpolFHR(FHRbl),4,0,0.006,3,1);

% Apply Butterworth filter
FuzzyLine=butterfilt(FHRi,4,0,0.02,4,1);

plot(FuzzyLine);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Investigating Wrobel et al. 2013 baseline function

clear;

% Set the record and the number of the expert analysis
record = 'train28';
i = 118;

% Change to the directory of the FHRMA add-on
cd '/home/amy/MATLAB Add-Ons/Collections/Fetal Heart Rate Morphological Analysis Toolbox (FHRMA)'

% Load expert analyses
load FHRMAdataset/analyses/expertAnalyses.mat

% Load the relevant FHR data
file = ['FHRMAdataset/traindata/', record, '.fhr'];

% Clean the FHR
[FHR1,FHR2,~,TOCO,timestamp] = fhropen(file);
[FHRi,FHRraw,TOCOi] = preprocess(FHR1,FHR2,TOCO,data(i).unreliableSignal);

% Subsample by average - i.e. find the mean of every 10 records
sFHR=avgsubsamp(FHRi,10);
baseline=zeros(1,length(sFHR));

for i=1:length(sFHR)
    wins=max(1,i-160);
    wine=min(length(sFHR),i+160);
    baseline(i)=myriad(sFHR(wins:wine),0.25);
end
newbaseline=resamp(baseline,10,length(FHRi),1);

function m=myriad(x,k2)
    ma=round(max(x));
    mi=round(min(x));
    myrs=zeros(1,ma-mi+1);
    for i=0:ma-mi
        myrs(i+1)=sum(log(k2+(x-i-mi).^2));
    end
    [~,m]=min(myrs);
    m=m+mi;
end