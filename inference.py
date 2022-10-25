import os 
import argparse
from glob import glob

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Darknet inference")
    parser.add_argument("-i", "--input_folder", type=str)
    parser.add_argument("-o", "--output_folder", type=str)
    args = parser.parse_args()

    assert '/app' in args.input_folder
    assert '/app' in args.output_folder

    os.system('rm -rf /app/tmp')
    os.system('mkdir /app/tmp')
    os.system('mkdir /app/tmp/backup')
    os.system(f'mkdir {args.output_folder}')

    all_images = glob(os.path.join(args.input_folder,'*.jpg'))

    with open('darknet_dataset/train.txt','w') as f:
        f.writelines('\n')
    with open('/app/tmp/test.txt','w') as f:
        f.writelines('\n'.join(all_images) + '\n')
    with open('/app/tmp/obj.names','w') as f:
        f.writelines(['west\n','helmet\n','worker\n'])

    os.system('echo "classes = 3 \ntrain  = /app/tmp/train.txt \nvalid  = /app/tmp/test.txt \nnames = /app/tmp/obj.names \nbackup = /app/tmp/backup/" > tmp/obj.data')

    os.system('cd /app/darknet && ./darknet detector valid /app/tmp/obj.data /app/darknet_dataset/yolov4.cfg /app/darknet_dataset/backup/yolov4_best.weights')

    os.system(f'mv /app/darknet/results/* {args.output_folder}')

    os.system('rm -rf /app/tmp')