import numpy as np


def blackpad_augment(sample):
  """Performs flip augmentation on img.

  Args:
    sample: Dictionary of (np array: <ch,z,x,y>) image and mask
  """

  n_pad = int(sample["image"].shape[1]*0.4)
  
  if np.random.rand() < 0.25:

    d = np.random.choice([0,1])
    for k in sample.keys():
      sample[k] = blackpad(sample[k], d=d, n=n_pad)

  if np.random.rand() < 0.25:

    d = np.random.choice([2,3])
    for k in sample.keys():
      sample[k] = blackpad(sample[k], d=d, n=n_pad)


  return sample


def blackpad(img, d=0, n=100):

  img_pad = np.zeros(img.shape)
  if d == 0:
    img_pad[:,n:,:] = img[:,:-n,:]

  elif d == 1:
    img_pad[:,:-n,:] = img[:,n:,:]

  elif d == 2:
    img_pad[:,:,n:] = img[:,:,:-n]

  elif d == 3:
    img_pad[:,:,:-n] = img[:,:,n:]


  return img_pad
