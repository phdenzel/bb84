from pathlib import Path
import numpy as np
import svgutils.compose as sc
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from layout import BB84Setup

sq2pi = np.sqrt(2*np.pi)

def transmission1(img_base, seconds, fps):
    base = Path("tmp/transmission1")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, seconds, seconds*fps)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        ti = ti % 1
        alpha = min(1, 100 * np.exp(-0.5*(ti-0.5)**2/0.1**2) / (sq2pi*0.1))
        print(filename)
        layout.default_index(layout.alice_index, 'alice')
        layout.set_index('alice', detector=0, signal_alpha=alpha, signal_distance=ti)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transmission2(img_base, seconds, fps):
    base = Path("tmp/transmission2")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, seconds, seconds*fps)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        ti = ti % 1
        alpha = min(1, 100 * np.exp(-0.5*(ti-0.5)**2/0.1**2) / (sq2pi*0.1))
        print(filename)
        layout.default_index(layout.alice_index, 'alice')
        layout.set_index('alice', detector=0, signal=1, signal_alpha=alpha, signal_distance=ti)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transmission3(img_base, seconds, fps):
    base = Path("tmp/transmission3")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, seconds, seconds*fps)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        ti = ti % 1
        alpha = min(1, 100 * np.exp(-0.5*(ti-0.5)**2/0.1**2) / (sq2pi*0.1))
        print(filename)
        layout.default_index(layout.alice_index, 'alice')
        layout.set_index('alice', detector=1, signal=2, signal_alpha=alpha, signal_distance=ti)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transmission4(img_base, seconds, fps):
    base = Path("tmp/transmission4")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, seconds, seconds*fps)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        ti = ti % 1
        alpha = min(1, 100 * np.exp(-0.5*(ti-0.5)**2/0.1**2) / (sq2pi*0.1))
        print(filename)
        layout.default_index(layout.alice_index, 'alice')
        layout.set_index('alice', detector=1, signal=3, signal_alpha=alpha, signal_distance=ti)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transmission5(img_base, seconds, fps):
    base = Path("tmp/transmission5")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, seconds, seconds*fps)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        ti = ti % 1
        alpha = min(1, 100 * np.exp(-0.5*(ti-0.5)**2/0.1**2) / (sq2pi*0.1))
        print(filename)
        layout.default_index(layout.alice_index, 'alice')
        layout.set_index('alice', detector=0, signal_alpha=alpha, signal_distance=ti)
        layout.set_index('bob', detector=1)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transmission6(img_base, seconds, fps):
    base = Path("tmp/transmission6")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, seconds, seconds*fps)
    head_icons = [sc.SVG(img_base/"alice_text.svg"),
                  sc.SVG(img_base/"bob_text.svg")]
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        ti = ti % 1
        alpha = min(1, 100 * np.exp(-0.5*(ti-0.5)**2/0.1**2) / (sq2pi*0.1))
        print(filename)
        layout.default_index(layout.alice_index, 'alice')
        layout.set_index('alice', detector=0, signal=1, signal_alpha=alpha, signal_distance=ti)
        layout.set_index('bob', detector=1)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transmission7(img_base, seconds, fps):
    base = Path("tmp/transmission7")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, seconds, seconds*fps)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        ti = ti % 1
        alpha = min(1, 100 * np.exp(-0.5*(ti-0.5)**2/0.1**2) / (sq2pi*0.1))
        print(filename)
        layout.default_index(layout.alice_index, 'alice')
        layout.set_index('alice', detector=1, signal=2, signal_alpha=alpha, signal_distance=ti)
        layout.set_index('bob', detector=1)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transmission8(img_base, seconds, fps):
    base = Path("tmp/transmission8")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, seconds, seconds*fps)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        ti = ti % 1
        alpha = min(1, 100 * np.exp(-0.5*(ti-0.5)**2/0.1**2) / (sq2pi*0.1))
        print(filename)
        layout.default_index(layout.alice_index, 'alice')
        layout.set_index('alice', detector=1, signal=3, signal_alpha=alpha, signal_distance=ti)
        layout.set_index('bob', detector=1)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transition1(img_base, seconds, fps):
    base = Path("tmp/transition1")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, 29, int(seconds*fps)).astype(int)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        print(filename)
        layout.set_index('alice', detector=2+ti)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transition2(img_base, seconds, fps):
    base = Path("tmp/transition2")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, 29, int(seconds*fps)).astype(int)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        print(filename)
        layout.set_index('alice', detector=31-ti)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transition3(img_base, seconds, fps):
    base = Path("tmp/transition3")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, 29, int(seconds*fps)).astype(int)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        print(filename)
        layout.set_index('alice', detector=2+ti)
        layout.set_index('bob', detector=1)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transition4(img_base, seconds, fps):
    base = Path("tmp/transition4")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, 29, int(seconds*fps)).astype(int)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        print(filename)
        layout.set_index('alice', detector=31-ti)
        layout.set_index('bob', detector=1)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transition5(img_base, seconds, fps):
    base = Path("tmp/transition5")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, 29, int(seconds*fps)).astype(int)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        print(filename)
        layout.set_index('alice', detector=0)
        layout.set_index('bob', detector=2+ti)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transition6(img_base, seconds, fps):
    base = Path("tmp/transition6")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, 29, int(seconds*fps)).astype(int)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        print(filename)
        layout.set_index('alice', detector=0)
        layout.set_index('bob', detector=31-ti)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transition7(img_base, seconds, fps):
    base = Path("tmp/transition7")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, 29, int(seconds*fps)).astype(int)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        print(filename)
        layout.set_index('alice', detector=1)
        layout.set_index('bob', detector=2+ti)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()

def transition8(img_base, seconds, fps):
    base = Path("tmp/transition8")
    base.mkdir(parents=True, exist_ok=True)
    t = np.linspace(0, 29, int(seconds*fps)).astype(int)
    for i, ti in enumerate(t):
        filename = base / f"frame_{i:05d}.png"
        plt.axis('off')
        plt.style.use('dark_background')
        layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                       sc.SVG(img_base/"bob_text.svg")])
        print(filename)
        layout.set_index('alice', detector=1)
        layout.set_index('bob', detector=31-ti)
        layout.plot()
        plt.savefig(filename, transparent=True)
        plt.gcf().clear()


if __name__ == "__main__":
    fps = 180
    seconds = 1
    img_base = Path("assets/images")
    fig = plt.figure()
    #transmission1(img_base, seconds, fps)
    #transmission2(img_base, seconds, fps)
    #transmission3(img_base, seconds, fps)
    #transmission4(img_base, seconds, fps)
    #transmission5(img_base, seconds, fps)
    #transmission6(img_base, seconds, fps)
    #transmission7(img_base, seconds, fps)
    #transmission8(img_base, seconds, fps)
    #transition1(img_base, seconds, fps/3)
    transition2(img_base, seconds, fps/3)
    transition3(img_base, seconds, fps/3)
    transition4(img_base, seconds, fps/3)
    transition5(img_base, seconds, fps/3)
    transition6(img_base, seconds, fps/3)
    transition7(img_base, seconds, fps/3)
    transition8(img_base, seconds, fps/3)

    
