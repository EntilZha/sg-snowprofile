%% Hardness Profile
% Chago Rodriguez
% chagorodriguez@u.boisestate.edu
% BSU Geoscience Department
% Last update 12.23.2013

%% Start of Code
% Clear variables
clear all;
close all;

%% Load Data
fileID = fopen('hardness.txt');
D=textscan(fileID,'%f %s' ); % load data
layer=D(:,1);           % layer [cm]
hard=D(:,2);            % hardness 

%% Layer Data Formatting
n=length(layer{1,1});
xu=layer{1,1};% xu is the vector for the upper depth of each layer
xl=layer{1,1};% xl is the vector for the lower depth of each layer
xu(n)=[];
xl(1)=[];

%% Hardness Data Formatting
% F-   1
% F    2
% 4F-  3
% 4F   4
% 1F-  5
% 1F   6
% P-   7
% P    8
% K-   9
% K    10
% H is variable for hardness using the above scale
% create vector with hardness for every layer
n=length(hard{1,1})-1;
h=hard{1,1};
H=ones(n,1);
for z=1:n
    switch h{z};
        case {'F-'}
            H(z)=1;
        case {'F'}
            H(z)=2;
        case {'4F-'}
            H(z)=3;
        case {'4F'}
            H(z)=4;
        case {'1F-'}
            H(z)=5;
        case {'1F'}
            H(z)=6;
        case {'P-'}
            H(z)=7;
        case {'P'}
            H(z)=8;
        case {'K-'}
            H(z)=9;
        case {'K'}
            H(z)=10;
    end
end

%% Generate hardness profile for Chapelco Day 1 & Day 2
figure(1);clf
hold on;

for z=1:n
    switch H(z);
        case {1,2}; % F hard layers
            c=[0.9 0.1 0.1];
        case {3,4}; % 4F hard layers
            c=[1 0.6 0];
        case {5,6}; % 1F hard layers
            c=[0.1 0.4 1];
        case {7,8}; % P hard layers
            c=[0.4 0.2 0.9];
        case {9,10} % K hard layers
            c=[0.5 0.9 0.1];
    end
    patch([0 H(z) H(z) 0], ...
          [xu(z) xu(z) xl(z) xl(z)],c);
end

%% Make chart pretty
grid on;
box on;
set(gca,'ydir','reverse');
set(gca,'XTick',[0:2:10]);xlim([-0.1 10]);
set(gca,'XTickLabel',{'','Fist', '4F', '1F', 'P','K'});
set(gca,'YTick',[0:10:200]);ylim([-2 max(xl)+2]);
title('Snow Hardness Profile by SNOWGEEK');
ylabel('Depth [cms]');
xlabel('Hardness');


