<div>

# Exiting News!
📣 📣 Excited to announce the 1st  Challenge on Multi-modal object detection at International conference on Emerging Technology in Autonomous Aerial Vehicles (ETAAV) in August 2025 at IISc, Bangalore


This challenge focuses on enhancing the performance on thermal domain without forgetting the visible domain for object detection task that involve:
👉  Training YOLO model efficiently to utilize both domains effectively.
👉  Proposing novel methods (such as Domain Adaptation, Domain Generalization) to achieve superior performance.

Looking forward to exciting talks, challenges, and discussions bringing together the vision and robotics communities!
🗓️ Join us on August 18 at ETAAV 2025 at IISc, Bengaluru.
🌐 More details: https://sites.google.com/view/etaav2025

Thanks to the amazing organizing team: Manjunath D, Aniruddh Sikdar, Aditya Gandhamal and Samahith !🙌

<div>

<div>

# SAGA: Semantic-Aware Gray color Augmentation for Visible-to-Thermal Domain Adaptation across Multi-View Drone and Ground-Based Vision Systems

<div>

<!-- <a href="https://sites.google.com/view/indraeye">
<img src="https://github.com/Manjuphoenix/IndraEye/blob/master/images/airl_logo-1.jpg" alt="Paper Link" width="70px">
</a>&nbsp;&nbsp;&nbsp;&nbsp; -->

<a href="https://arxiv.org/pdf/2504.15728">
<img src="https://img.shields.io/badge/Paper-arxiv.2403.20126-red" alt="Paper Link" width="190px">
</a>
<!-- <img src="https://github.com/Manjuphoenix/IndraEye/blob/master/images/airl_logo-1.jpg" alt="Paper Link" width="60px">
</div>


<!--
</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://arxiv.org/pdf/2410.20953">
<img src="https://img.shields.io/badge/Paper-arxiv.2403.20126-red" alt="Paper Link" width="190px">
</a> -->




[Manjunath D](https://scholar.google.com/citations?user=379B-doAAAAJ&hl=en), [Aniruddh Sikdar](https://scholar.google.com/citations?user=FdgpBuoAAAAJ&hl=en&authuser=1), [Prajwal Gurunath](https://scholar.google.com/citations?user=1D-q8wwAAAAJ&hl=en&oi=ao), [Sumanth Udupa](https://scholar.google.com/citations?user=d3cLdNoAAAAJ&hl=en&oi=ao), [Suresh Sundaram](https://scholar.google.com/citations?user=5iAMbhMAAAAJ&hl=en&authuser=1)

Domain-adaptive thermal object detection plays a key role in facilitating visible (RGB)-to-thermal (IR)  adaptation by reducing the need for co-registered image pairs and minimizing reliance on large annotated IR datasets. However, inherent limitations of IR images, such as the lack of color and texture cues, pose challenges for RGB-trained models, leading to increased false positives and poor-quality pseudo-labels. To address this, we propose Semantic-Aware Gray color Augmentation (SAGA), a novel strategy for mitigating color bias and bridging the domain gap by extracting object-level features relevant to IR images. Additionally, to validate the proposed SAGA for drone imagery, we introduce the IndraEye, a multi-sensor (RGB-IR) dataset designed for diverse applications. The dataset contains 5,612 images with 145,666 instances, captured from diverse angles, altitudes, backgrounds, and times of day, offering valuable opportunities for multimodal learning, domain adaptation for object detection and segmentation, and exploration of sensor-specific strengths and weaknesses. IndraEye aims to enhance the development of more robust and accurate aerial perception systems, especially in challenging environments. Experimental results show that SAGA significantly improves RGB-to-IR adaptation for autonomous driving and IndraEye dataset, achieving consistent performance gains of +0.4 to +7.6 when integrated with state-of-the-art domain adaptation techniques. The dataset and codes are available at https://bit.ly/indraeye



#### Download dataset from [here](https://bit.ly/indraeye).
#### Project page Link: [link](https://sites.google.com/view/indraeye).


### IndraEye Dataset structure:
```sh
[data]
    ├── IndraEye_eo-ir_split_version3
       ├── eo
              ├── train
                        ├── Annotations (Pascal VOC format)
                        ├── annotations (COCO json format)
                        ├── images (.jpg format with individual .json files)
                        ├── labels (.txt for YOLO format)
                        ├── labelTxt (.txt for DOTA format)
              ├── val
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
```

Classes list (in same order as class id): 0: "backhoe_loader", 1: "bicycle", 2: "bus", 3: "car", 4: "cargo_trike", 5: "ignore", 6: "motorcycle", 7: "person", 8: "rickshaw", 9: "small_truck", 10: "tractor", 11: "truck", 12: "van"



<!--
### SAGA
<img src="/images/SAGA.png" class=center>


### SAGA
![Images](/images/SAGA.png)





### Qualitative Comparision
![Images](/images/cmt_pred.png)


<div style="display: flex; justify-content: center; gap: 20px;">

  <div>
    <img src="/images/SAGA.png" alt="SAGA" style="width: 50%;">
  </div>

  <div>
    <img src="/images/cmt_pred.png" alt="Qualitative Comparison" style="width: 50%;">
  </div>

</div>
-->

<h2>SAGA</h2>
<div align="center">
  <img src="/images/SAGA.png" alt="SAGA" style="width:60%;">
  <p style="font-size:2px">
    Illustration of SAGA augmentation. The process involves extracting objects from the image, converting them to grayscale, and reintegrating them into the original image while preserving background color information.
  </p>
</div>

<!-- 
<h2>Qualitative Comparison</h2>
<div align="center">
  <img src="/images/cmt_pred.png" alt="Qualitative Comparison" style="width:50%;">
  <div>
    Output predictions to highlight the importance of the SAGA augmentation on CMT algorithm. (a) and (c) shows the increase in false positives while using vanilla CMT. Meanwhile (b) and (d) shows the reduction in false positives when using SAGA with CMT, showcasing its effectiveness.
  </div>
</div>
-->


<!--
<table>
  <tr>
    <td align="center">
      <img src="/images/SAGA.png" alt="SAGA" style="width: 100%;">
    </td>
    <td align="center">
      <img src="/images/cmt_pred.png" alt="Qualitative Comparison" style="width: 50%; height: 100%">
    </td>
  </tr>
</table>
-->

</div>

# SAGA Usage
To convert RGB image to instance gray image use the following command:
```bash
python inst_gry.py --coco_json_file /path/to/coco/json --image_directory /path/to/images  --inst_gry_directory /path/to/store/images

```


<table>
  <tr>
    <th><h2>IndraEye Dataset</h2></th>
    <th><h2>Qualitative Comparison</h2></th>
  <tr>
    <td align="center">
      <img src="/images/eo_ir.jpg" alt="Qualitative Comparison" style="width: 100%;">
      <p style="font-size:2px">
        IndraEye RGB-IR samples. (a,b): High scale-variation medium altitude with minimal slant-angle during day time.
        (c,d): High scale-variation medium altitude with minimal slant-angle during night time.
        (e,f): High altitude with lesser slant-angle covering a large area.
        (g-h): Mid altitude with high scale variations.
      </p>
    </td>
    <td align="center">
      <img src="/images/cmt_pred.png" alt="SAGA" style="height: 80%; width: 80%;">
      <p style="font-size:2px">
    Output predictions to highlight the importance of the SAGA augmentation on CMT algorithm. (a) and (c) shows the increase in false positives while using vanilla CMT. Meanwhile (b) and (d) shows the reduction in false positives when using SAGA with CMT, showcasing its effectiveness.
  </p>
    </td>
  </tr>
</table>

<!-- 
<div>

## IndraEye: Infrared Electro-Optical Drone-based Aerial Object Detection Dataset
> **Abstract:** *Deep neural networks (DNNs) have demonstrated superior performance when trained on well-illuminated environments, given that the images are captured through an Electro-Optical (EO) camera, which offers rich texture content. In critical applications such as aerial surveillance, maintaining consistent reliability of DNNs throughout all times of the day is paramount, including during low-light conditions where EO cameras often struggle to capture relevant details. Furthermore, UAV-based aerial object detection encounters significant scale variability stemming from varying altitudes and slant angles, introducing an additional layer of complexity. Existing approaches consider only illumination change/style variations as the domain shift, while in aerial surveillance, correlation shifts also acts as a hindrance to the performance of DNNs. In this paper we propose a multi-sensor (EO-IR) labelled object detection dataset consisting of 5276 images with 142991 instances covering multiple viewing angles and altitudes, 7 backgrounds and at different times of the day. This dataset serves as an effective resource for UAV-based object detection, facilitating the development of robust DNNs capable of operating round-the-clock.*

</div>


<div align="center">

![Images](/images/eo_ir.jpg)
**Visualization of our EO-IR images**
</div>


<div align="center">
  <img src="/images/eo_ir.jpg" alt="Qualitative Comparison" style="width:50%;">
</div>
-->

### License
This repo is released under the CC BY 4.0 license. Please see the LICENSE file for more information.

### Contact
For inquiries, please contact: manjunathd1@iisc.ac.in


## Citation

If you use our dataset, code, or results in your research, please consider citing our paper:

```BibTeX
@misc{d2025sagasemanticawaregraycolor,
      title={SAGA: Semantic-Aware Gray color Augmentation for Visible-to-Thermal Domain Adaptation across Multi-View Drone and Ground-Based Vision Systems}, 
      author={Manjunath D and Aniruddh Sikdar and Prajwal Gurunath and Sumanth Udupa and Suresh Sundaram},
      year={2025},
      eprint={2504.15728},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2504.15728}, 
}

```

