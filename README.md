# Railway-Workers-Detection
Object detection of railway workers, their helmets and vests, using Darknet Framework.

Instalation:
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

Download [weights](https://drive.google.com/drive/folders/1Os5-WUCTDswMcVKQn6L25fKbTNLPie48) unzip and put it in /app/darknet_dataset/backup/ folder.

(Optionaly) Donwload [weights](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137) of YOLOv4 pretrained on MSCOCO if you want to reproduce training. 

