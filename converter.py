import imageio
import os

clip = os.path.abspath('videoplayback.mp4')

def gifMaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat # videoplayback + .gif

    print(f'converting {inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps'] # gif has same fps as video

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frame {frames}')
    print('Done!')
    writer.close()

gifMaker(clip, '.gif')

