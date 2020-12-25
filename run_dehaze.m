img = imread('./20201217_dehaze/0112_231953_hdr_EV0_result.jpg');

dehaze = false ;
contrast = true;

LAB = rgb2lab(img);
L = LAB(:,:,1)/100;

if dehaze
    [L_dehaze, T, L] = imreducehaze(L, 0.1);
    imshow(T);
%     D = -log(1-T+eps);
%     imshow(D,[])
%     title('depth estimate')
%     colormap hot

else
    wSat = 1;
    bSat = 10;
    dyn  = 1.0;
    [v,vmin,vmax] = robustNormalization(L, hiswSat, bSat, dyn);
end
% dehaze_out = imreducehaze(img, 0.5);

LAB(:, :, 1) = L_dehaze*100;
J = lab2rgb(LAB);
figure, imshowpair(img, J, 'montage')
imwrite(J, './20201217_dehaze/0112_231953_hdr_EV0_result_normalize.jpg');


