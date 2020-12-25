% img = imread('0918_154158_hdr_ev-3.0_source_NNguide_6119.png');

% result= AGCWD(img, 0.5);
%%%histgram equalization
RGB= imread('E:\\2020_codes\\data\\0415_225926_hdr_ev-3.0_result.jpg');
%%%%use the dehaze
% dehaze_out = imreducehaze(RGB);
% montage({RGB,dehaze_out})
% title('Hazy Image (Left) vs. Reduced Haze Image (Right)');
 
LAB = rgb2lab(RGB);
L = LAB(:,:,1)/100;
wSat=1;
bSat=10;
dyn=1.0;
[v, vmin, vmax] = robustNormalization(L, wSat, bSat, dyn);
LAB(:,:,1)= v*100;

% L = LAB(:,:,1)/100;
% LAB(:,:,1) = adapthisteq(L,'NumTiles',...
%                          [8 8],'ClipLimit',0.001)*100;
J = lab2rgb(LAB); 
figure, imshow(RGB);
figure, imshow(J);
imwrite(J, 'E:\\2020_codes\\data\\0415_225926_hdr_ev-3.0_result_nornalize.jpg');