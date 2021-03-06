import matplotlib
matplotlib.use('Agg')
from train import Train
from test import Test
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', dest='data_path', help='path of the data',
                        default='./data', type=str)
    parser.add_argument('--model_path', dest='model_path', help='path of the model folder',
                        default='./model/', type=str)
    parser.add_argument('--output_path', dest='output_path', help='path of the output folder',
                        default='./out', type=str)
    parser.add_argument('--graph_path', dest='graph_path', help='path of the graph',
                        default='./graph', type=str)
    parser.add_argument('--batch_size', dest='batch_size', help='batch size',
                        default=64, type=int)
    parser.add_argument('--epoch', dest='epoch', help='epoch',
                        default=20, type=int)
    parser.add_argument('--restore', dest='restore', help='restore',
                        default=False, type=bool)
    parser.add_argument('--mode', dest='mode', help='train or test',
                        default='test', type=str)
    args = parser.parse_args()

    return args

args = parse_args() 

if __name__ == '__main__':
    print(args)
    epoch = args.epoch
    batch_size = args.batch_size
    data_path = args.data_path
    model_path = args.model_path
    output_path = args.output_path
    graph_path = args.graph_path
    restore = args.restore
    mode = args.mode
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    if mode == 'train':
        train = Train(epoch, batch_size, data_path, model_path, output_path, graph_path, restore)
        train.train()
    elif mode == 'test':    
        test = Test(batch_size, data_path, model_path, output_path)
        test.test()
                            
