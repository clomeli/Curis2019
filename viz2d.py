import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import json
import numpy as np
import random
dic = {}
with open('data/sets/nuscenes/image_annotations.json', 'r') as f:
        dic = json.load(f)
img_to_bbox = {}
for i,obj in enumerate(dic):
    if obj['filename'] in img_to_bbox:
        img_to_bbox[obj['filename']].append([obj['category_name'], obj['bbox_corners']])
    else:
        img_to_bbox[obj['filename']]= [[obj['category_name'], obj['bbox_corners']]]


# bboxs = img_to_bbox['samples/CAM_FRONT/n008-2018-08-01-15-16-36-0400__CAM_FRONT__1533151605012404.jpg']
# img=mpimg.imread('data/sets/nuscenes/samples/CAM_FRONT/n008-2018-08-01-15-16-36-0400__CAM_FRONT__1533151605012404.jpg')
dpi = 300
cmap = {'v':'b', 'a':'g', 'h':'r', 'm':'c', 's':'m', 'c':'y', 'p':'k'}

for i in range(100):
    file = random.choice(list(img_to_bbox.keys()))
    print(i)
    bboxs = img_to_bbox[file]
    img=mpimg.imread('data/sets/nuscenes/' + file)
    fig = plt.figure(frameon=False)
    fig.set_size_inches(img.shape[1] / dpi, img.shape[0] / dpi)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.axis('off')
    fig.add_axes(ax)
    ax.imshow(img)
    for bbox in bboxs:
        name = bbox[0]
        color = cmap[name[0]]
        bbox = bbox[1]
        ax.add_patch(
            plt.Rectangle((bbox[0], bbox[1]),
                          bbox[2] - bbox[0],
                          bbox[3] - bbox[1],
                          fill=False, edgecolor= color,
                          linewidth=0.5, alpha=.5))
        ax.text(
                    bbox[0], bbox[1] - 2,
                    name,
                    fontsize=3,
                    family='serif',
                    bbox=dict(
                        facecolor='k', alpha=0.2, pad=0, edgecolor='none'),
                    color='white')

    fig.savefig('sample_2d/' + str(i) + '.jpg', dpi = dpi)
