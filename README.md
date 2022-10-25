# Railway-Workers-Detection
Object detection of railway workers, their helmets and vests, using YOLOv4 and Darknet Framework.

## Instalation
```
git clone https://github.com/AlexeyAB/darknet.git
make up 
make in
cd darknet
mkdir build_release
cd build_release
cmake ..
cmake --build . --target install --parallel 8

```
Download and unzip [dataset.zip](https://drive.google.com/file/d/1BKMXnyPFT6uFWCSbyrZ7r5st9bCQwb2T/view) in /app/dataset.

Download [weights](https://drive.google.com/file/d/1mUE7lEqelFs6YBWyT1fbPo_Eb1W6OTZ5/view?usp=sharing) unzip and put it in /app/darknet_dataset/backup/ folder.

(Optionaly) Donwload [weights](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137) of YOLOv4 pretrained on MSCOCO if you want to reproduce training. 

## Results
### mAP@0.5: 98.73%

<image src="darknet_dataset/chart.png" alt="Графики обучения" height=700px>
  
## Inference on your own data
```
python inference.py -i /full/path/to/input/folder -o /full/path/to/output/folder
```

