


from pystrich.datamatrix import DataMatrixEncoder


import os


def generate(DMMessage,DMimagename):

    DM = DataMatrixEncoder(str(DMMessage)) #Create datamatrix
    dirname = os.path.dirname(__file__)
    DMimagepath = os.path.join(dirname, "matrix_image_temp\\" + DMimagename + '.png')

    DM.save(DMimagepath)
   
    return DMimagepath