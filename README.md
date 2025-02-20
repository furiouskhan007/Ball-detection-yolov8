# The Yolov8 custom model is trained on 3 classes but the code is modified to detect only one class Soccer (class ID 2) only
# Classes names:
- football
- otherball
- soccer
nc: 3
# roboflow:
  license: CC BY 4.0
  project: ca_proj_group4
* url: https://universe.roboflow.com/mbs4542-caproject/ca_proj_group4/dataset/2
  version: 2
  workspace: mbs4542-caproject
test: test/images
train: train/images
val: valid/images

Output:
