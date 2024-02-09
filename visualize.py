#Visualize the .pck file from PA2 in ece368
import matplotlib.pyplot as plt
import numpy as np
import re


def draw_boxes(boxes):
    fig, ax = plt.subplots()
    for box in boxes:
        size_x, size_y = box[0]
        start_x, start_y = box[1]
        rect = plt.Rectangle((start_x, start_y), size_x, size_y, linewidth=2, edgecolor='r', facecolor='red', label='a')
        ax.add_patch(rect)

    ax.set_xlim(0, max(box[0][0]+box[1][0] for box in boxes))
    ax.set_ylim(0, max(box[0][1]+box[1][1] for box in boxes))
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True)
    plt.show()

if __name__ == "__main__":
    fp = open("1k.pck")
    boxes = []
    formatted_string = fp.readline()
    while(formatted_string != ''):
        size_match = re.search(r'\d+\(\((\d+),(\d+)\)\((\d+),(\d+)\)\)', formatted_string)
        if(size_match != None):
            x = (int)(size_match.group(1))
            y = (int)(size_match.group(2))
            ax = (int)(size_match.group(3))
            ay = (int)(size_match.group(4))
            output = ((x,y),(ax,ay))
            print(output)
            boxes.append(output)
        formatted_string = fp.readline()
        # print(formatted_string)

    
    fp.close()
    draw_boxes(boxes)
