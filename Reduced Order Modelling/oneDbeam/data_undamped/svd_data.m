clc
clear
close all

% Load displacement data file
displacement = load('displacement.dat');
% Transpose the data file 
displacement = displacement';

% get the number of nodes and number of time steps
% m is the number of nodes
% n is the number of time steps
[m,n] = size(displacement);

% separate x and y displamcements
x_disp = displacement(1:2:m,:);
y_disp = displacement(2:2:m,:);

% Perform SVD on the data
[Ux,Sx,Vx] = svd(x_disp,"econ");
[Uy,Sy,Vy] = svd(y_disp,"econ");

% Get the first r modes
Uxr = Ux(:,1:10);
Uyr = Uy(:,1:10);

% % disp_arranged = [x_disp; y_disp];
% % 
% % [U,S,V] = svd(disp_arranged,'econ');
% % Ux = U(1:m/2,:);
% % Uy = U(m/2+1:m,:);

writematrix(Uxr,'Uxr.csv')
writematrix(Uyr,'Uyr.csv')
