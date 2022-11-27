clc
clear
close all

displacement = load('displacement.dat');
displacement = displacement';
[U,S,V] = svd(dynamic_vel,"econ");

Ur = U(:,1:10);

writematrix(Ur, 'file2write.txt')
