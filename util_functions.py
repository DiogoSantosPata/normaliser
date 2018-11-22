"""
This script contains useful functions to analyse the data
"""


def bandPassFilter(s,fL,fH,b,fs):
    '''
    s = data
    fL =  #low Cutoff frequency (in (0, 0.5)).
    fH =  #high Cutoff frequency (in (0, 0.5)).
    b = 0.08  # Transition band      (in (0, 0.5)).
    N = int(np.ceil((4 / b)))
    '''

    fL = fL/float(fs)
    fH = fH/float(fs)
    b  = b/float(fs)
    N = int(np.ceil((4 / b)))

    if not N % 2: N += 1  # Make sure that N is odd.
    n = np.arange(N)

    # Compute a low-pass filter with cutoff frequency fH.
    hlpf = np.sinc(2 * fH * (n - (N - 1) / 2.))
    hlpf *= np.blackman(N)
    hlpf = hlpf / np.sum(hlpf)

    # Compute a high-pass filter with cutoff frequency fL.
    hhpf = np.sinc(2 * fL * (n - (N - 1) / 2.))
    hhpf *= np.blackman(N)
    hhpf = hhpf / np.sum(hhpf)
    hhpf = -hhpf
    hhpf[(N - 1) / 2] += 1

    # Convolve both filters.
    h = np.convolve(hlpf, hhpf)
    mar = (len(h)-1)/2
    return np.convolve(s,h)


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def smooth_psd(p, sz=40, sigma=10):
    '''
        sz :  length of gaussFilter vector
        sigma = 10     
    '''    
    x = np.linspace(-sz / 2, sz / 2, sz);
    gaussFilter = np.exp(-x** 2 / (2 * sigma**2));
    gaussFilter = gaussFilter / sum (gaussFilter); # normalize
    pp = np.convolve(p, gaussFilter, 'same');    
    return pp