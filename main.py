import os
import argparse
from bbox_annotator import bbox_annotator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', type=str, default='data/images/ai.png')
    parser.add_argument('--save_dir', type=str, default='data/images/')
    parser.add_argument('--annotations_dir', type=str, default='data/annotations/')
    args = parser.parse_args()
    bbox_annotator(args.image_path, args.save_dir, args.annotations_dir)

if __name__ == '__main__':
    main()
