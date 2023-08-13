from pathlib import Path
import numpy as np
import svgutils.compose as sc
import cairosvg
import cairocffi
from PIL import Image
from io import BytesIO
from matplotlib import pyplot as plt


def pixelate_svg(svgobj, color={'stroke': '#ffffff'}):
    svgstr = svgobj.tostr()
    for ckey in color:
        svgstr = svgstr.replace(
            bytes(f'{ckey}: #ffffff', encoding='utf-8'),
            bytes(f'{ckey}: {color[ckey]}', encoding='utf-8'))
    png = cairosvg.svg2png(svgstr)
    return Image.open(BytesIO(png))


class BB84Setup:
    """
    A layout of the BB84 setup of two parties, Alice and Bob, and an
    adversary Eve.  Each party is represented by an optional head
    icon, a detector icon, and a tally region (of bits/measurement and
    bases).  The parties, more specifically their detectors, are
    linked via a quantum channel in which signals, i.e. photons, can
    be transmitted.
    """
    icon_base = Path("assets/images")
    default_color = "#FFFFFF"
    alice_color = "#00AF87"
    bob_color = "#5F8AF7"
    eve_color = "#E83A82"
    signal_color = "#FFD787"
    public_color = "#F6F9FE"
    

    def __init__(self,
                 resolution=(4096, 2160),
                 positions=None,
                 alice_index=None,
                 bob_index=None,
                 head_icons=None,
                 detector_icons=None,
                 activation_icons=None,
                 signal_icons=None):
        """
        Args:
          resolution (int, int)
          positions (list(float), list(float))
          alice_index (dict)
          bob_index (dict)
          head_icons (list(svgutils.compose.SVG))
          detector_icons (list(svgutils.compose.SVG))
          activation_icons (list(svgutils.compose.SVG))
          signal_icons (list(svgutils.compose.SVG))
        """
        self.resolution = resolution
        if positions is None:
            positions = [[0, 0], [1, 1]]
        self.positions = positions
        self.alice_index = self.default_index(alice_index, 'alice')
        self.bob_index = self.default_index(bob_index, 'bob')
        self.head_icons = head_icons
        # if isinstance(head_icons, (list, tuple)):
        #     self.head_icons = {'alice': head_icons[0],
        #                        'bob': head_icons[1]}
        if detector_icons is None:
            self.detector_icons = {
                'alice': self.load_detector_svgs(self.icon_base),
                'bob': self.load_detector_svgs(self.icon_base)}
        if activation_icons is None:
            self.activation_icons = {
                'alice': self.load_activation_svgs(self.icon_base),
                'bob': self.load_activation_svgs(self.icon_base)}
        if signal_icons is None:
            self.signal_icons = {
                'alice': self.load_signal_svgs(self.icon_base),
                'bob': self.load_signal_svgs(self.icon_base)}

    @property
    def has_head(self):
        return self.head_icons is not None or len(self.head_icons) > 0

    def default_index(self, index, party):
        if index is None:
            index = {}
        sign = 1 if party.lower() == 'alice' else -1
        u_vec = lambda x, y: [sign*x, sign*y]
        det_x, det_y = 0.09, 0.09
        index.setdefault('name', party)
        index.setdefault('head', 0 if party.lower() == 'alice' else 1)
        index.setdefault('sign', 1 if party.lower() == 'alice' else -1)
        index.setdefault('head_scale', 3.0)
        index.setdefault('head_offset', u_vec(0.08, 0.05))
        index.setdefault('detector', 0)
        index.setdefault('detector_scale', 1.0)
        index.setdefault('detector_rotation', 0)
        index.setdefault('detector_offset', u_vec(det_x, det_y))
        index.setdefault('signal', 0)
        index.setdefault('signal_scale', 2.0)
        index.setdefault('signal_offset', u_vec(2*det_x, 2*det_y))
        index.setdefault('signal_y_adjust', 0.15)
        index.setdefault('signal_distance', None)
        index.setdefault('signal_alpha', 1)
        index.setdefault('is_sender', party.lower() == 'alice')
        return index

    def set_index(self, party, **kwargs):
        if party.lower() == 'alice':
            index = self.alice_index
        elif party.lower() == 'bob':
            index = self.bob_index
        for k in kwargs.keys():
            if k not in index:
                del kwargs[k]
        index.update(kwargs)

    def position(self, index, offsetkey=None, use_center=True, use_offset=True):
        """
        A parties' position is composed of
          - main position (pos): 'head' index entry from <positions>
          - center: the center of the offset component
          - offset: the offset of a component relative to 'head'

        Returns:
          (float, float): pos - center + offset
        """
        r = np.array(self.resolution)
        pos = np.array(self.positions[index['head']]) \
            + np.array(index['head_offset'])
        prefix = offsetkey.replace('_offset', '')
        offsetkey = f'{prefix}_offset'
        icons = getattr(self, f'{prefix}_icons')
        if isinstance(icons, dict):
            icons = icons[index['name']]
        center = np.array([0, 0])
        if icons and use_center:
            center[0] = icons[index[prefix]].width/2
            center[1] = icons[index[prefix]].height/2
        offset = np.array([0, 0])
        if offsetkey in index and use_offset and offsetkey != 'head_offset':
            offset = np.array(index[offsetkey])
        return r*pos - center + r*offset

    def alice_position(self, offsetkey=None, use_center=True, use_offset=True):
        return self.position(self.alice_index,
                             offsetkey=offsetkey, use_center=use_center)

    def bob_position(self, offsetkey=None, use_center=True, use_offset=True):
        return self.position(self.bob_index,
                             offsetkey=offsetkey, use_center=use_center)

    def signal_lerp(self, A, B, fraction, y_adjust=0, scale=1):
        position = []
        rotation = []
        AB = B - A
        if fraction is not None:
            position = A + scale*fraction * AB - np.array([0, y_adjust])
            rotation = [180/np.pi * np.arctan2(AB[1], AB[0])]
        return position, rotation

    def setup(self, party):
        # fetch settings
        index = getattr(self, f'{party}_index')
        color = getattr(self, f'{party}_color')
        components = []
        # head
        if self.head_icons:
            head = self.set_svg_color(self.head_icons[index['head']],
                                      color={'fill': color})
            head.moveto(*self.position(index, 'head'), index['head_scale'])
            components.append(head)
        # detector
        detector = self.set_svg_color(self.detector_icons[party][index['detector']],
                                      color={'stroke': color})
        detector.moveto(*self.position(index, 'detector'), index['detector_scale'])
        detector.rotate(index['detector_rotation'])
        components.append(detector)
        return sc.Panel(*components)

    def setup_alice(self):
        return self.setup('alice')

    def setup_bob(self):
        return self.setup('bob')

    def setup_eve(self):
        return None

    def setup_signal(self):
        # signal
        party = 'alice' if self.alice_index['is_sender'] else 'bob'
        index = getattr(self, f'{party}_index')
        other = getattr(self, f'{"bob" if party == "alice" else "alice"}_index')
        components = []
        signal = self.set_svg_color(self.signal_icons[party][index['signal']],
                                    color={'stroke': self.signal_color})
        if index['is_sender']:
            p_signal, rot_signal = \
                self.signal_lerp(
                    self.position(index, 'signal', use_center=True),
                    self.position(other, 'signal', use_center=True),
                    index['signal_distance'],
                    self.resolution[1]*index['signal_y_adjust'])
            if list(p_signal):
                signal.moveto(*p_signal, index['signal_scale'])
                signal.rotate(*rot_signal)
                components.append(signal)
        # lay quantum connection
        # quantum_bridge = sc.Line(
        #     [self.alice_position('signal', use_center=False, use_offset=True),
        #      self.bob_position('signal', use_center=False, use_offset=True)],
        #     width=8,
        #     color=self.public_color)
        # content.append(quantum_bridge)
        return sc.Panel(*components)

    def images(self):
        content = []
        # build a layout for each party
        alice_layout = self.setup_alice()
        bob_layout = self.setup_bob()
        if alice_layout:
            alice_svg = sc.Figure(*[str(r) for r in self.resolution], alice_layout)
            content.append(alice_svg)
        if bob_layout:
            bob_svg = sc.Figure(*[str(r) for r in self.resolution], bob_layout)
            content.append(bob_svg)
        # add the adversary
        eve_layout = self.setup_eve()
        if eve_layout:
            eve_svg = sc.Figure(*[str(r) for r in self.resolution], eve_layout)
            content.append(eve_svg)
        # signal between the parties
        signal_layout = self.setup_signal()
        if signal_layout:
            signal_svg = sc.Figure(*[str(r) for r in self.resolution], signal_layout)
            content.append(signal_svg)
        # stack layers for a scenario 
        figures = [sc.Figure(*[str(r) for r in self.resolution], c)
                   for c in content]
        try:
            return [self.pixelate_svg(svg, color=None) for svg in figures]
        except cairocffi.CairoError:
            return []

    def plot(self):
        svgs = self.images()
        if not svgs:
            return svgs
        images = []
        for svg in svgs[:-1]:
            img = plt.imshow(svg)
            images.append(img)
        party = 'alice' if self.alice_index['is_sender'] else 'bob'
        index = getattr(self, f'{party}_index')
        img = plt.imshow(svgs[-1], alpha=index['signal_alpha'])
        images.append(img)
        return images

    @staticmethod
    def set_svg_color(svgobj, color=None, default_color=default_color):
        if color is None:
            color = {}
        for key in color:
            for e in svgobj.root.iter():
                style = e.get('style')
                if style and key in style:
                    e.set('style', style.replace(f'{key}: {default_color.lower()}',
                                                 f'{key}: {color[key].lower()}'))
        return svgobj

    @staticmethod
    def pixelate_svg(svgobj, color=None, default_color=default_color):
        png = cairosvg.svg2png(svgobj.tostr())
        return Image.open(BytesIO(png))

    @staticmethod
    def load_detector_svgs(base_dir=None):
        if base_dir is None:
            base_dir = Path(".")
        detectors = [sc.SVG(base_dir / f"detector{i}.svg") for i in range(32)]
        return detectors

    @staticmethod
    def load_activation_svgs(base_dir=None):
        if base_dir is None:
            base_dir = Path(".")
        activations = [[sc.SVG(base_dir / f"activation{i}_{j}.svg")
                        for j in range(1, 5)] for i in range(2)]
        return activations

    @staticmethod
    def load_signal_svgs(base_dir=None):
        if base_dir is None:
            base_dir = Path(".")
        signals = [sc.SVG(base_dir / f"wave{i}.svg") for i in range(4)]
        return signals


if __name__ == "__main__":
    img_base = Path("assets/images")
    layout = BB84Setup(head_icons=[sc.SVG(img_base/"alice_text.svg"),
                                   sc.SVG(img_base/"bob_text.svg")])
    layout.set_index('alice', detector=0, signal_distance=0.2, signal_alpha=0.4)
    plt.style.use('dark_background')
    layout.plot()
    plt.axis('off')
    plt.show()
