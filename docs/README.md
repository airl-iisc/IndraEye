<div align="center">

# IndraEye: Infrared Electro-Optical Drone-based Aerial Object Detection Dataset


[Manjunath D](https://github.com/manjuphoenix), [Aniruddh Sikdar](https://scholar.google.com/citations?user=FdgpBuoAAAAJ&hl=en&authuser=1), [Prajwal Gurunath](https://scholar.google.com/citations?user=RrKoTX4AAAAJ&hl=en), [Sumanth Udupa](https://github.com/NaJaeMin92), [Suresh Sundaram](https://scholar.google.com/citations?user=5iAMbhMAAAAJ&hl=en&authuser=1)

> **Abstract:** *Deep neural networks (DNNs) have demonstrated superior performance when trained on well-illuminated environments, given that the images are captured through an Electro-Optical (EO) camera, which offers rich texture content. In critical applications such as aerial surveillance, maintaining consistent reliability of DNNs throughout all times of the day is paramount, including during low-light conditions where EO cameras often struggle to capture relevant details. Furthermore, UAV-based aerial object detection encounters significant scale variability stemming from varying altitudes and slant angles, introducing an additional layer of complexity. Existing approaches consider only illumination change/style variations as the domain shift, while in aerial surveillance, correlation shifts also acts as a hindrance to the performance of DNNs. In this paper we propose a multi-sensor (EO-IR) labelled object detection dataset consisting of 5276 images with 142991 instances covering multiple viewing angles and altitudes, 7 backgrounds and at different times of the day. This dataset serves as an effective resource for UAV-based object detection, facilitating the development of robust DNNs capable of operating round-the-clock.*

</div>


<div align="center">
  
![Images](/images/eo_ir.jpg)
**Visualization of our EO-IR images**
</div>


## Dataset structure:
```sh
[data]
    ├── IndraEye_eo-ir_split_version2
       ├── eo
              ├── train
                        ├── Annotations (Pascal VOC format)
                        ├── annotations (COCO json format)
                        ├── images (.jpg format with individual .json files)
                        ├── labels (.txt for YOLO format)
                        ├── labelTxt (.txt for DOTA format)
              ├── val
                        (Same as train)
              ├── test
                        (Same as train)
       ├── ir
              ├── train
                        ├── Annotations (Pascal VOC format)
                        ├── annotations (COCO json format)
                        ├── images (.jpg format with individual .json files)
                        ├── labels (.txt for YOLO format)
                        ├── labelTxt (.txt for DOTA format)
              ├── val
                        (Same as train)
              ├── test
                        (Same as train)
```

Classes list (in same order as class id): 0: "backhoe_loader", 1: "bicycle", 2: "bus", 3: "car", 4: "cargo_trike", 5: "ignore", 6: "motorcycle", 7: "person", 8: "rickshaw", 9: "small_truck", 10: "tractor", 11: "truck", 12: "van"

* Download dataset from the [link](https://bit.ly/indraeye).
* Website Link: [link](https://sites.google.com/view/indraeye).


## License
This repo is released under the CC BY 4.0 license. Please see the LICENSE file for more information.

## Contact
For inquiries, please contact: manjunathd1@iisc.ac.in, prajwalg@iisc.ac.in, sumanthudupa@iisc.ac.in, vssuresh@iisc.ac.in
