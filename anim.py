from pathlib import Path
from copy import deepcopy
import numpy as np
import svgutils.compose as sc
from matplotlib import pyplot as plt
from layout import BB84Setup, brighten

sq2pi = np.sqrt(2*np.pi)


def transmission(img_base, seconds, fps,
                 alice_detector=0, bob_detector=0,
                 signal=0, polarisation=0):
    base = Path(f"frames/transmission_{alice_detector}-{bob_detector}.{signal}.{polarisation}")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, seconds, seconds*fps)
    head_icons = [sc.SVG(img_base/"alice_text.svg"), sc.SVG(img_base/"bob_text.svg")]
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[deepcopy(h) for h in head_icons])
        ti = ti % 1
        alpha = min(1, 100 * np.exp(-0.5*(ti-0.5)**2/0.1**2) / (sq2pi*0.1))
        print(filename)
        layout.default_index(layout.alice_index, 'alice')
        layout.set_index('alice', detector=alice_detector,
                         signal=signal, signal_polarisation=polarisation,
                         signal_alpha=alpha, signal_distance=ti)
        layout.set_index('bob', detector=bob_detector)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def detector_transition(img_base, seconds, fps,
                        alice_detector=0, bob_detector=0,
                        transition='alice'):
    if transition == 'alice':
        transition_str = f"{alice_detector}.{int(not alice_detector)}"
        base = Path(f"frames/transition_{transition_str}-{bob_detector}")
    else:
        transition_str = f"{bob_detector}.{int(not bob_detector)}"
        base = Path(f"frames/transition_{alice_detector}-{transition_str}")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, 29, int(seconds*fps)).astype(int)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        print(filename)
        if transition == 'alice':
            dt = 2+ti if alice_detector == 0 else 31-ti
            layout.set_index(transition, detector=dt)
            layout.set_index('bob', detector=bob_detector)
        else:
            dt = 2+ti if bob_detector == 0 else 31-ti
            layout.set_index(transition, detector=dt)
            layout.set_index('alice', detector=alice_detector)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def detection(img_base, seconds, fps,
              alice_detector=0, bob_detector=0,
              activation='bob'):
    base = Path(f"frames/activation_{alice_detector}-{bob_detector}.{activation}")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, seconds, int(seconds*fps))
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        color = getattr(layout, f'{activation}_color')
        factor = min(1, 0.1 * np.exp(-0.5*(ti-0.5)**2/0.1**2) / (sq2pi*0.1))
        print(filename, factor, brighten(color, factor))
        layout.set_index(activation, detector_color=brighten(color, factor))
        if activation == 'alice':
            layout.set_index(activation, detector=alice_detector,
                             detector_color=brighten(color, factor))
            layout.set_index('bob', detector=bob_detector)
        else:
            layout.set_index(activation, detector=bob_detector,
                             detector_color=brighten(color, factor))
            layout.set_index('alice', detector=alice_detector)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def tally_scenario(img_base, seconds, fps,
                   alice_tally, alice_bases,
                   bob_tally, bob_bases):
    pass


if __name__ == "__main__":
    fps = 180
    seconds = 1
    img_base = Path("assets/images")

    fig = plt.figure()

    # transmissions
    if 0:
        for a in range(2): # alice detector
            for b in range(2): # bob detector
                for i in range(2): # signal icons
                    #transmission(img_base, seconds, fps, a, b, i, 0)
                    for p in range(1, 3): # polarisation
                        transmission(img_base, seconds, fps, a, b, i, p)

    # transitions
    if 0:
        for a in range(2):
            for b in range(2):
                for t in ['alice', 'bob']:
                    detector_transition(img_base, seconds, fps/3, a, b, t)

    # activation
    if 0:
        for a in range(2):
            for b in range(2):
                for t in ['bob', 'alice']:
                    detection(img_base, seconds, fps/3, a, b, t)

    # tally scenario

