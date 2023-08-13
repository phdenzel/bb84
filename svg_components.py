import numpy as np
import matplotlib.pyplot as plt

P2 = np.pi/2


def wave_packet(*pars, N=500, from_=-1, to_=1):
    pars = list(pars)
    t = np.linspace(from_, to_, N)
    ga, gb, gc = pars.pop(0)
    sa, sb, sc = pars.pop(0)
    ca, cb, cc = pars.pop(0)
    if ga == gb == gc == 0:
        gauss = np.ones_like(t)
    else:
        gauss = ga * np.exp(-0.5*(t-gc)**2/gb**2)
    if sa == sb == sc == 0:
        sin = np.ones_like(t)
    else:
        sin = sa * np.sin(sc + sb*t)
    if ca == cb == cc == 0:
        cos = np.ones_like(t)
    else:
        cos = ca * np.cos(cc + cb*t)
    return t, gauss * sin * cos


def plt_detector(cx=0, cy=0, r=1.0, theta=0,
                 mask=[1, 1, 1, 1, 1], pltkw={}):
    p11, p12 = r+0j, -r+0j
    p21, p22 = r*1j, -r*1j
    if theta:
        rot = 1j**(theta/P2)
        p11 *= rot
        p12 *= rot
        p21 *= rot
        p22 *= rot
    #print(p11, p12, p21, p22)
    if int(mask[1]): plt.plot([p11.real, 0], [p11.imag, 0], **pltkw)
    if int(mask[2]): plt.plot([0, p12.real], [0, p12.imag], **pltkw)
    if int(mask[3]): plt.plot([p21.real, 0], [p21.imag, 0], **pltkw)
    if int(mask[4]): plt.plot([0, p22.real], [0, p22.imag], **pltkw)
    if int(mask[0]):
        circ = plt.Circle((cx, cy), r,
                          lw=pltkw['lw'], color=pltkw['c'], fill=False)
        plt.gca().add_patch(circ)


def svg_wave_variants(N=500, from_=-1, to_=1,
                      figsize=(5, 5), color='#fff', lw=4):
    kw = {'c': color, 'lw': lw, 'solid_capstyle': 'round'}
    for i, (pars1, pars2, pars3) in enumerate(zip(
            [ (1, 0.3,  0),  (1, 0.4,  0),  (1, 0.5, 0),  (1, 0.4,  0) ],
            [ (1,  50, P2),  (1,  18, P2),  (1,   3, 0),  (1, 4.8, P2) ],
            [ (0,   0,  0),  (1,  80,  0),  (1,  60, 0),  (1,  65,  0) ])):
        t, wave = wave_packet(pars1, pars2, pars3,
                              N=N, from_=from_, to_=to_)
        plt.figure(figsize=figsize)
        plt.plot(t, wave, **kw)
        plt.axis('off')
        plt.savefig(f'assets/images/wave{i}.svg', format='svg', transparent=True)
        plt.show()


def svg_detector_variants(figsize=(5, 5), color='#fff', lw=4):
    kw = {'c': color, 'lw': lw, 'solid_capstyle': 'round'}
    for i, (r_i, theta_i) in enumerate(zip(
            [0.7]*32, [0, P2/2]+list(np.linspace(0, P2/2, 30)))):
        # plot entire detector sign
        plt.figure(figsize=figsize)
        plt_detector(0, 0, r_i, theta_i, pltkw=kw)
        plt.xlim(-1.1*r_i, 1.1*r_i)
        plt.ylim(-1.1*r_i, 1.1*r_i)
        plt.axis('off')
        plt.savefig(f'assets/images/detector{i}.svg', format='svg', transparent=True)
        plt.show()
        mask = 16
        # plot individual internal components
        if i >= 2:
            continue
        for j in range(1, 5):
            plt.figure(figsize=figsize)
            mask = mask >> 1
            plt_detector(0, 0, r_i, theta_i,
                         mask=f'{int(bin(mask)[2:]):05d}',
                         pltkw=kw)
            plt.xlim(-1.1*r_i, 1.1*r_i)
            plt.ylim(-1.1*r_i, 1.1*r_i)
            plt.axis('off')
            plt.savefig(f'assets/images/activation{i}_{j}.svg',
                        format='svg', transparent=True)
            plt.show()


if __name__ == "__main__":
    svg_wave_variants(500, -1, 1)
    svg_detector_variants(lw=12)
