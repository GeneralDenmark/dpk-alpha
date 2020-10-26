import pathlib
from PIL import Image



ROOT_DIR = pathlib.Path(__file__).parent
input_dir = ROOT_DIR.joinpath('input')
output_dir = ROOT_DIR.joinpath('output')

if not input_dir.is_dir():
    input_dir.mkdir()

files = [x for x in input_dir.glob('**/**') if x.is_file()]

if len(files) == 0:
    raise Exception('Empty input folder')

if not output_dir.is_dir():
    output_dir.mkdir()


rotation = 360
interval = 5


for i in range(0, rotation, interval):



