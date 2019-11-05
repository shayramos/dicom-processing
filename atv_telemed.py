# import cv2
import numpy as np
# import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files
# from google.colab.patches import cv2_imshow
# from ipywidgets import interact, interactive, fixed, interact_manual
# import ipywidgets as widgets

#diretório
MAMOGRAFIA = "Mamografias/mam1.dcm"
CT = "CT Thin Plain/CT000255.dcm"
DICOM = "DICOM/IM-0002-0083.dcm"
ds = pydicom.dcmread(DICOM)

print('A imagem tem {} x {} voxels'.format(ds.pixel_array.shape[0], ds.pixel_array.shape[1]))

#Promova a conversão dos valores armazenados nos arquivos DICOM para unidades Hounsfield. 
#Considere os valores armazenados no proprio arquivo DICOM, caso existam.
print('\nAntes da conversão:\n {}' .format(ds.pixel_array))

for n, val in enumerate(ds.pixel_array.flat):
    ds.pixel_array.flat[n]  = ds.pixel_array.flat[n] * ds.RescaleSlope + ds.RescaleIntercept
ds.PixelData = ds.pixel_array.tobytes()

print('\nDepois da conversão:\n {}' .format(ds.pixel_array))

#A partir da imagem em unidades Hounsfield, determine qual o melhor mapeamento (nível e janela)
#de conversão dos dados do exame para uma imagem de 8 bits considerando os requisitos de cada 
#um dos exames descrito acima.

#A partir das imagens de 8 bits geradas aplique as técnicas de processamento de imagem discutidas 
#em sala de aula para:
    #segmentar as estruturas ósseas dos exames de CT
    #segmentar as diferentes estruturas internas nos tecidos moles no exame de CT
    #segmentar estruturas de calcificação nas mamografias