import os
import argparse
import datetime
import time
import tqdm
import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def train(args):



def main():
    parser = argparse.ArgumentParser(description='Train a Linear AE')
    parser.add_argument('--data-dir', required=True, help='Directory containing the training data', dest='data_dir')
    parser.add_argument('--train-file', required=True, help='Model configuration (.models.json format).', dest='train_file_name')
    parser.add_argument('--output-dir', required=True, help='HLA information of the reference data (.hla.json format).', dest='out_dir')
    parser.add_argument('--num-epoch', default=100, type=int, required=False, help='Number of epochs to train (Default 100).', dest='num_epoch')
    parser.add_argument('--patience', default=8, type=int, required=False, help='Patience for early-stopping (Default 8).', dest='patience')
    parser.add_argument('--rs', default=2023, type=int, required=False, help='Random seed used for splitting train and validation sets (Default 2023).', dest='rs')
    parser.add_argument('--val-split', default=0.2, type=float, required=False, help='Ratio of splitting data for validation (Default 0.2).', dest='val_split')

    args = parser.parse_args()

    train(args)


if __name__ == '__main__':
    main()
