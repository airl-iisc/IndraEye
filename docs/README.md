<div>

# SAGA: Semantic-Aware Gray color Augmentation for Visible-to-Thermal Domain Adaptation across Multi-View Drone and Ground-Based Vision Systems


[Manjunath D](https://scholar.google.com/citations?user=379B-doAAAAJ&hl=en), [Aniruddh Sikdar](https://scholar.google.com/citations?user=FdgpBuoAAAAJ&hl=en&authuser=1), [Prajwal Gurunath](https://scholar.google.com/citations?user=1D-q8wwAAAAJ&hl=en&oi=ao), [Sumanth Udupa](https://scholar.google.com/citations?user=d3cLdNoAAAAJ&hl=en&oi=ao), [Suresh Sundaram](https://scholar.google.com/citations?user=5iAMbhMAAAAJ&hl=en&authuser=1)

Domain-adaptive thermal object detection plays a key role in facilitating visible (RGB)-to-thermal (IR)  adaptation by reducing the need for co-registered image pairs and minimizing reliance on large annotated IR datasets. However, inherent limitations of IR images, such as the lack of color and texture cues, pose challenges for RGB-trained models, leading to increased false positives and poor-quality pseudo-labels. To address this, we propose Semantic-Aware Gray color Augmentation (SAGA), a novel strategy for mitigating color bias and bridging the domain gap by extracting object-level features relevant to IR images. Additionally, to validate the proposed SAGA for drone imagery, we introduce the IndraEye, a multi-sensor (RGB-IR) dataset designed for diverse applications. The dataset contains 5,612 images with 145,666 instances, captured from diverse angles, altitudes, backgrounds, and times of day, offering valuable opportunities for multimodal learning, domain adaptation for object detection and segmentation, and exploration of sensor-specific strengths and weaknesses. IndraEye aims to enhance the development of more robust and accurate aerial perception systems, especially in challenging environments. Experimental results show that SAGA significantly improves RGB-to-IR adaptation for autonomous driving and IndraEye dataset, achieving consistent performance gains of +0.4 to +7.6 when integrated with state-of-the-art domain adaptation techniques. The dataset and codes are available at \href{https://bit.ly/indraeye}{https://bit.ly/indraeye}

</div>

<div>

## IndraEye: Infrared Electro-Optical Drone-based Aerial Object Detection Dataset


[Manjunath D](https://scholar.google.com/citations?user=379B-doAAAAJ&hl=en), [Aniruddh Sikdar](https://scholar.google.com/citations?user=FdgpBuoAAAAJ&hl=en&authuser=1), [Prajwal Gurunath](https://scholar.google.com/citations?user=1D-q8wwAAAAJ&hl=en&oi=ao), [Sumanth Udupa](https://scholar.google.com/citations?user=d3cLdNoAAAAJ&hl=en&oi=ao), [Suresh Sundaram](https://scholar.google.com/citations?user=5iAMbhMAAAAJ&hl=en&authuser=1)

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
For inquiries, please contact: manjunathd1@iisc.ac.in, aniruddhss@iisc.ac.in, prajwalg@iisc.ac.in, sumanthudupa@iisc.ac.in, vssuresh@iisc.ac.in
