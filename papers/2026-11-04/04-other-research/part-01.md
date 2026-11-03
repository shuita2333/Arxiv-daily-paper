# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

---

### 1. [Social signals dominate clinician trust in medical AI](https://arxiv.org/abs/2611.00007)

**<font color=#1a73e8>作者：</font>** Aníbal Astobiza, Ramón Ortega Lozano, Marcos Alonso 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Accuracy and outcome data are often treated as the main determinants of trust in automation. We test this assumption against an account in which clinicians evaluate artificial intelligence (AI) using social-cognitive cues. We introduce SPOT (Synergistic Process-Outcome Trust), a Bayesian framework that models trust as inference over latent agent properties from outcome and process signals. In a within-subjects vignette study, 275 Spanish healthcare professionals evaluated 16 clinical AI scenarios varying three outcome signals (accuracy, intervention timing, prognosis) and five process signals (interface familiarity, explainability, team consensus, supervision, personalization). Ratings were analysed with linear mixed models and participant-wise cross-validation. Process signals dominated trust formation. Interface familiarity (beta = 0.71), team consensus (beta = 0.64), and explainability (beta = 0.63) produced large effects, with p values below .001, whereas stated accuracy produced a small effect (beta = 0.10). Process signals accounted for 80.3 percent of the total absolute effect magnitude and outcome signals for 19.7 percent. Trust baselines were highly idiosyncratic and poorly recovered from demographics (R-squared = 0.06 under group-wise cross-validation). Clinicians appear to treat AI systems as agents whose trustworthiness requires social validation as well as technical verification. Building trustworthy clinical AI therefore involves social, institutional, and technical factors.

---


### 2. [Beyond the Last Layer: Global Inter-Layer Aggregation for AI-Generated Image Detection](https://arxiv.org/abs/2611.00017)

**<font color=#1a73e8>作者：</font>** Wenbin Shen, Zhichao Lian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid development of generative models has made AI-generated images increasingly close to real images. It has also brought several challenges to detectors, including rapid generator updates, large changes in data distribution, and limited cross-dataset generalization. Many existing methods based on pretrained vision encoders primarily use the global representation from the last layer, potentially leaving useful information from intermediate layers underexplored. To address this issue, we propose Global Inter-Layer Aggregation (GILA). GILA extracts global representations from different depths of a frozen encoder, models interactions among layer representations through inter-layer self-attention, and adaptively aggregates the resulting contextualized representations. The method is not tied to a single pretraining objective and does not require fine-tuning the pretrained encoder. We evaluated GILA on three vision backbones with different pretraining objectives, ten seen generators, and three external datasets. The experimental results show that GILA makes better use of multi-layer information in pretrained encoders and improves detection performance and cross-dataset generalization.

---


### 3. [Intervenable Concept Dynamics for Video Activity Forecasting](https://arxiv.org/abs/2611.00020)

**<font color=#1a73e8>作者：</font>** Patrick Knab, David Steinmann, Giovanni De Felice 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept bottleneck models route predictions through human-understandable concepts, making their intermediate states inspectable and editable. Extending this model family to forecasting requires modeling how concept activations evolve over time as objects, actions, and their interactions change, yet existing CBMs ground concepts only in observed inputs and do not forecast their future evolution. We study this problem using videos of ongoing activities and forecast future activities through a named-concept state. We propose TRACE-CBM (Temporal Relational Activity Concept Evolution), which first refines observed concept activations with sparse spatio-temporal graphs. It then recursively predicts future concept states, conditioning each transition on the prior activity distribution, and decodes both observed and predicted states with a shared activity classifier. At inference time, the model supports editing concept values, activity activations, and learned edges without parameter updates, exposing the relational spatio-temporal dependencies used for forecasting. Across multiple datasets, TRACE improves observed-activity Top-1 accuracy over concept-based methods by 1.2-8.5 percentage points and attains H3 forecast Top-1 accuracy within 1.9-2.2 points of matched black-box forecasters. Intervention experiments show concept-node edits correct 25.6-34.4% of initially incorrect H3 forecasts without flipping initially correct ones, and concept steering achieves the requested target activity in up to 90.0% of cases.

---


### 4. [Diagnosing Prototype Estimation in Few-Shot Class-Incremental Learning: Training-Free Geometry Selection and Unlabeled-Query Prototype Rectification](https://arxiv.org/abs/2611.00022)

**<font color=#1a73e8>作者：</font>** Md Tanvir Hossain Saikat, Md Akib Haider, Md. Tahmid Islam Tomal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen visual encoders make prototype heads competitive in few-shot class-incremental learning (FSCIL), but it remains unclear how much of the residual head gap is sensitive to noisy novel-class means rather than to the subsequent changes introduced by classifier refitting. On identical features, we construct a retrospective matched counterfactual: first replace each five-shot novel mean with its complete-data counterpart under fixed cosine scoring, then fit a linear probe. Across sixteen strong encoder dataset pairs, mean replacement accounts for the majority of this ordered gap. Shot and classwise diagnostics support a finite-sample mechanism, whereas a weaker base-only encoder does not satisfy the same criterion. This diagnosis motivates ShrinkSel, a support-only selector over prototype radius and covariance shrinkage whose family contains shared LDA as an exact fallback. Across sixteen evaluated pairs, it improves LDA on fifteen by 0.04-1.52 points and selects the exact LDA endpoint on Aircraft. We further introduce Query Prototype Rectification (QPR), a batch-transductive extension that uses gated unlabeled queries to update novel directions while preserving the selected geometry. On CLIP ViT-B/16, QPR adds 1.21-2.03 points; exact query-wise self-exclusion retains the benefit, showing that the gains do not require self-inclusion. The update repairs scarce novel prototypes at a measurable base-class cost and weakens with plentiful supports or very small cohorts. Thus, the evidence available for prototype estimation is a central constraint in frozen-feature FSCIL.

---


### 5. [FORCE: Factorized Object Relations for Counterfactual Editing in Video World Models](https://arxiv.org/abs/2611.00023)

**<font color=#1a73e8>作者：</font>** Suraj K. Sood, Yugyung Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models predict how scenes evolve, but they are difficult to interrogate: given a model that forecasts a video, one cannot easily ask what would have happened had a particular interaction between two objects been different. We present Factorized Object Relations for Counterfactual Editing (FORCE), a world model that infers pairwise interactions from raw video without supervision and represents each as an explicit latent per object pair, so that a relation can be removed, changed, transferred or introduced directly. Objects are extracted by slot attention over frozen self-supervised features; a relation encoder infers each pair latent from a short observation window, and an interaction head turns it into a force. The latent is held fixed across the rollout, so an edit persists rather than being recomputed, and every edit acts on the model's own quantities with no mapping to simulator parameters. We evaluate in a simulated environment where the true outcome of an edit is available, scoring the change each edit induces against the change the simulator produces under the same operation. On held-out clips, FORCE's edits made from video agree with the simulator's response at 0.19 to 0.37 on our effect-based score; trained and scored on exact object positions instead, the same architecture reaches 0.57 to 0.85. The gap therefore lies not in the learned relational dynamics but in perception: what bounds an edit is how precisely objects can be located from video, and the precision editing needs lies just beyond what current object-centric perception delivers. Closing that gap is a concrete target for making counterfactual world models work from video.

---


### 6. [Edge-Optimized YOLOv11n Architecture for Offline Recognition of Nigerian Sign Language Alphanumeric Gestures](https://arxiv.org/abs/2611.00025)

**<font color=#1a73e8>作者：</font>** Adeleke Adeniyan, Abimbola H. Afolayan, Olanrewaju V. Johnson  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deaf inclusion across sub-Saharan society faces regional hurdles, with Nigeria as the core empirical focus. Existing recognition models demand heavy computational infrastructure. However, standard mobile phones used locally rarely exceed 1 GB to 4 GB of RAM. This study addresses constraints through a lightweight YOLO11n object-detection framework. The system provides real-time Nigerian Sign Language recognition for low-resource hardware. A benchmark dataset containing 11,208 raw gesture images was established. The data spans 33 static classes collected from five signers. Partitioning isolates signers S1 through S3 for training. Signer S4 provides validation data. Signer S5 is reserved for testing. Spatial augmentations are restricted strictly to the training set. This yields 23,509 training images. The validation and test sets each maintain 1,681 images across varied environments. The framework integrates a quantization-aware compression objective. Loss functions merge with squared Frobenius-norm penalties to govern weight distortion. A Spatial-Density Occlusion Index quantifies background complexity and self-occlusion. A latency-profiling equation relates floating-point operations and memory bandwidth to chipset clock speed. Performance testing on physical Android hardware utilizes unquantized FP32 weights. Mean inference latencies span 405.5 ms to 1,759.4 ms. Measured against test data, the algorithm attains a Precision of 0.9975. Recall reaches 0.9991. Mean Average Precision is 0.9942. Outcomes support offline functionality on constrained mobile devices. Practical deployment operates through a mobile utility using CameraX. The application captures gestures in real time. Recognized signs display as text instantly.

---


### 7. [SFA: A Statistical Physics-Inspired Diffusion Transformer for Efficient and High-Quality Image Generation](https://arxiv.org/abs/2611.00027)

**<font color=#1a73e8>作者：</font>** Zixuan Huang, Tianhao You, Guozhang Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers have achieved remarkable success in image generation, but accelerating attention while preserving generation quality remains a major challenge at high resolutions. Inspired by statistical physics and the widespread occurrence of scale-free laws in nature, we introduce Scale-Free Attention (SFA), which preserves fine local interactions while summarizing distant regions at progressively coarser scales. For $N$ tokens, mean pooling, token-count correction, and a shared softmax over a scale-free spatial hierarchy give SFA $O(N\log N)$ complexity in both forward and backward passes. Our Triton implementation achieves $357.3\times$ forward and $265.6\times$ backward attention speedups over FlashAttention at 262,144 tokens. After 40 epochs of PixelFlow training from scratch on ImageNet at $256\times256$ resolution, SFA achieves the best generation quality among five attention mechanisms, including full attention. Fréchet inception distance evaluated on 50,000 generated samples (FID-50k) improves from 13.25 for full attention to 12.51, and the advantage over full attention persists through 80 epochs. SFA also achieves the best generation quality among the compared efficient-attention methods on Flickr-Faces-HQ (FFHQ). Beyond training from scratch, Stable Diffusion 3.5 Medium with attention replaced by SFA retains the generation quality of its full-attention counterpart under matched fine-tuning budgets. We obtain similar results when fine-tuning pretrained PixelFlow on ImageNet. SFA establishes scale-free structure as an effective design principle for efficient, high-quality diffusion transformers.

---


### 8. [DiA: Directional Adapter](https://arxiv.org/abs/2611.00029)

**<font color=#1a73e8>作者：</font>** Ashish Kumar Singh, Prakash Chandra Chhipa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained action recognition often depends on how an action unfolds over time rather than on appearance alone. Visually similar classes may differ in preparation, execution, or completion phases, making uniformly aggregated temporal context suboptimal. We study this problem under a practical objective: i) improving recognition performance with few tunable parameters, ii) being compute efficient, and iii) using only the readily available video modality. Motivated by this missing temporal observation and the accuracy--compute efficiency--unimodality objective, we propose Directional Adapter (DiA), a parameter-efficient adapter on top of CLIP. DiA formulates temporal specialization into causal and anti-causal directions, allowing past-to-present and future-to-present cues to be modeled differently. To keep this directional modeling parameter- and compute-efficient, both directions use depth-wise temporal convolutions in a compact bottleneck space and are combined through a learnable fusion. DiA achieves state-of-the-art performance among methods using a single video input modality across seven public benchmarks, with only $\sim$3.6M tunable parameters, while also delivering higher throughput and lower inference latency than prior methods. Code is available at this https URL.

---


### 9. [Monocular Badminton Speed Estimation with Air Drag and Court Geometry](https://arxiv.org/abs/2611.00031)

**<font color=#1a73e8>作者：</font>** Diwen Huang, Sarvesh Madullapalli, Ishan Pendyala 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A single camera cannot distinguish between a slowly moving object nearby and a rapidly moving object in the distance without additional information. For a shuttlecock, air drag provides a strong deceleration cue that can be combined with known court geometry. We fit a gravity-and-drag trajectory to smartphone video and compare a free monocular fit with a fit constrained to cross the net plane. Camera calibration uses court lines, and the trajectory is fitted to observed shuttle positions and frame timestamps by robust nonlinear least squares. We evaluated 51 badminton shots from two recording sessions, spanning drop shots, drives, half-smashes and smashes. The net-plane fit reduced the median absolute speed difference from a drag-based stereo reference from 13.3% to 8.6%. A second reference, obtained by differentiating triangulated positions without a drag model, also gave a smaller median difference for the net-plane fit. The results support combining court geometry with flight dynamics for badminton speed estimation from a single camera.

---


### 10. [Gaussifier: Fast 2D Gaussian Decomposition](https://arxiv.org/abs/2611.00032)

**<font color=#1a73e8>作者：</font>** Yunlai Zhou, Yu Yin, Michael W. Jenkins 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 2D Gaussians render images at thousands of frames per second. However, fitting an image takes seconds of optimization. This confines 2D Gaussians to offline use. Feedforward methods are faster but less accurate without per-image fine-tuning. We present Gaussifier, a lightweight feedforward framework for 2D Gaussian decomposition. We learn a density map of Gaussian centers from per-image fitting data. Equal-mass Voronoi places Gaussians so that each Voronoi cell holds approximately equal density. A stateless, reusable network then refines the output in a few iterations. Gaussifier reaches 40.73/38.61\,dB PSNR on Kodak-24/DIV2K at over 60 FPS. At the same Gaussian count, it exceeds every feedforward baseline by 3.0 to 15.6\,dB in PSNR. With fewer Gaussians than any baseline, it still leads the strongest one by 2.5 to 3.5\,dB. At the same count, baselines with their own per-image fitting need 26 to 326 times longer to reach its PSNR. Gaussifier makes high-fidelity 2D Gaussian images fast and light enough for real-time applications. We release code, weights and a browser-based WebGPU demo at this https URL.

---


### 11. [Multimodal Cross-Condition Learning for Temporal Sentence Grounding in Videos](https://arxiv.org/abs/2611.00033)

**<font color=#1a73e8>作者：</font>** Allen He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal sentence grounding requires a video representation that preserves query-relevant evidence and a sentence representation that reflects the visual context in which it is interpreted. Prior end-to-end grounding addresses the first requirement through sentence-conditioned visual adaptation, but leaves the language representation independent of the video. This work proposes Multimodal Cross-Condition Learning (MCCL). Its Video Prefix Adapter (VPA) converts pooled visual context into a sequence of continuous tokens that condition a frozen DistilBERT encoder. Combined with the Sentence Conditioned Adapter (SCADA), VPA supports an ordered exchange from vision to language and back to vision. A comprehensive study examines two video backbones, LSTM and Mamba temporal modules, and four conditioning modes on two datasets. Bidirectional conditioning exceeds the stronger one-way mode by 1.6--2.3 mIoU points in all four Charades-STA settings. ActivityNet Captions exhibits a different pattern: bidirectionality helps I3D--Mamba, whereas video-to-text conditioning is stronger with C3D. The study extends one-way visual adaptation into a configurable multimodal framework and reports descriptive gains over the corresponding baselines.

---


### 12. [A Trustworthy Clinical Decision Support Framework for Brain Tumor MRI Classification: Integrating Attention-Guided Learning, Explainable AI, and Out-of-Distribution Validation](https://arxiv.org/abs/2611.00034)

**<font color=#1a73e8>作者：</font>** Arjun Kumar Gupta, Harminder Pal Monga  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for brain tumor diagnosis need to do more than achieve high classification accuracy. For practical use, they should also provide understandable predictions, recognize unsuitable inputs, and work within a usable clinical system. This paper presents a framework for classifying brain MRI into four categories: glioma, meningioma, pituitary tumor, and no tumor. The model uses InceptionResNetV2 with a Convolutional Block Attention Module (CBAM), while Grad-CAM provides visual explanations of its predictions. A two-stage out-of-distribution (OOD) mechanism screens unsuitable inputs using an initial grayscale check followed by Mahalanobis distance, softmax confidence, and predictive entropy. These components are brought together in NeuroScan AI, a real-time web application. Evaluated on a Mendeley brain tumor MRI dataset of 12,064 images, the framework achieved 98.70% validation accuracy, 96.73% test accuracy, and a macro-average AUC of 0.9965. The OOD pipeline achieved 99% detection accuracy on a preliminary 100-image benchmark. Grad-CAM visualizations showed qualitative correspondence with clinically established tumor locations across all four classes. Overall, the work brings classification, explainability, input validation, and deployment into one framework, while recognizing that broader clinical and OOD validation is still required.

---


### 13. [Selective Positional Allocation for Noise-Robust Query Retrieval in Small-Object Detection](https://arxiv.org/abs/2611.00035)

**<font color=#1a73e8>作者：</font>** Yangchen Zeng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In aerial and remote-sensing imagery, detecting tiny targets is frequently hampered less by the representational capacity of the backbone network than by the manner in which positional priors are distributed across ill-defined foreground and background regions. We introduce SPAR (Selective Positional Allocation and Retrieval), a detection framework that re-conceptualizes positional cues as an allocatable resource: they are intensified at semantically meaningful locations while responses driven by scene clutter are actively attenuated. At the heart of SPAR lies Selective Positional Embedding (SPE), an interpretable embedding mechanism paired with an activation-bar visualization that facilitates direct inspection and hyper-parameter tuning. The encoder branch, termed MOHFE, fuses heatmap-modulated positional signals with category-specific and box-level evidence to yield more compact multi-scale features; the decoder branch, termed HIDQ, employs a foreground gating operation to discard background-dominated candidates prior to query decoding. To cope with the extreme sparsity of small-object evidence, we additionally design DPSConv (Dual-Path Sampling Convolution), which augments retrieval-oriented representations through two geometrically complementary sampling routes. Notably, all heatmap supervision is derived from existing detection objectives and consumed exclusively during training, requiring no auxiliary heatmap annotations and leaving inference as an ordinary forward pass with no additional gradient overhead. Comprehensive evaluations on DOTA, DIOR, VisDrone, PASCAL VOC, NWPU VHR-10, and AITOD demonstrate the effectiveness of the proposed design: relative to the baseline, SPAR attains an improvement of up to 9.1 percentage points, shortens the decoder from eight layers to three, and reduces model parameters by 59.4% (66.3M versus 163M).

---


### 14. [Deep Learning for Detecting Building Setback Rule Violations in Urban Planning: A Case Study on Bangladesh](https://arxiv.org/abs/2611.00037)

**<font color=#1a73e8>作者：</font>** Farzana Tasnim, Faria Yasmin, Md. Tauseef-Ur-Rahman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dhaka's rapid urban growth has made building setback violations common, narrowing footpaths and blocking emergency access. RAJUK, responsible for building control in the Dhaka Metropolitan Area, enforces setback rules mainly through manual field inspection, which scales poorly. We present a systematic comparison of four machine learning approaches for classifying building setback conditions from street-level photographs: negative (compliant), moderate (borderline), and positive (violation). We built a labeled dataset of 372 geo-tagged images from sixteen Dhaka neighborhoods and expanded it with 5,968 augmented copies for training. We trained and evaluated a multi-layer perceptron (MLP), a Random Forest ensemble on frozen ResNet50 embeddings, a support vector machine on frozen ResNet18 embeddings, and a fine-tuned ResNet18 CNN. On a 1,275-image test set, the fine-tuned CNN achieved 65.4% accuracy (macro-F1 0.50), followed by Random Forest at 59.9% (macro-F1 0.44) and SVM at 58.2% (macro-F1 0.45). All models classify the compliant class reliably but struggle with the borderline moderate class due to visual ambiguity. These results establish reference performance levels for automated setback-compliance screening in a South Asian regulatory setting.

---


### 15. [Beyond Black Boxes: An Ontology Based Vision Framework for Transparent Fruit Disease Detection](https://arxiv.org/abs/2611.00039)

**<font color=#1a73e8>作者：</font>** M.J. Marapperuma, B.V.K.I. Vidanage  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficiency and reliability in the timely identification of phytopathogens would help minimize crop loss in agricultural sectors but existing deep learning based methods, although accurate, would require a large annotated dataset and are black-boxed in their operation, thus, restricting flexibility and transparency. The current paper presents a hybrid detection framework that is able to overcome these drawbacks through the unified real-time vision with a semantic knowledge base. Web Ontology Language (OWL) was used to develop a comprehensive ontology of the disease of fruits that formally codifies phytopathological knowledge, such as symptom phenotype, spectral phenotype (HSV), and morphological phenotype. Such knowledge-guided configuration guides the image processing pipeline, making it possible to diagnose using this knowledge under expert specified rules without a large training dataset. The ontology underwent a computationally verified test of its structural soundness and commonsensical practical usefulness and scored an overall of 7.4/10. On the public set of MangoFruitDDS, the diagnostic performance was an F1 Score of 85.00%, precision of 85.00%, and a recall of 85.23%. These findings are very competitive and similar to other known deep learning models like the VGG16 that prove that the knowledge-driven approach provides an accurate, transparent, and scalable solution on automated fruit disease diagnosis.

---


### 16. [Real-Time Obstacle Detection and Distance Estimation on Smartphones for Visually Impaired and Distracted Pedestrians](https://arxiv.org/abs/2611.00040)

**<font color=#1a73e8>作者：</font>** Abtin Zandi, Sarvin Nami, Roza Ganjipour 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> According to the World Health Organization, at least 2.2 billion people worldwide live with visual impairment, including tens of millions with severe vision loss. Traditional aids such as white canes or guide dogs remain costly, limited in capability, and inaccessible to many. At the same time, smartphone distraction in public spaces has been linked to elevated risks of collisions with vehicles, trips, and falls. These dual challenges motivate lightweight, smartphone-based solutions that combine accessibility with low latency. We present a Kotlin-based Android application that uses a YOLOv8 detector, retrained to recognize eighteen common urban obstacle classes, to deliver real-time obstacle alerts for both user groups. The detector was optimized with pruning, quantization, and early-exit branches, and deployed through the Android Neural Networks API (NNAPI), which can dispatch inference to GPU, NPU, or DSP accelerators when available. On a mid-range smartphone, these optimizations reduced average inference latency from about 3.2 s for the off-the-shelf YOLOv8n to 0.39-0.48 s; the recommended configuration (INT8 quantization with early exit) runs in 0.42-0.48 s while retaining a recall of 0.81. The application combines the optimized detector with ARCore-based or monocular focal-length distance estimation, so it works with a single smartphone camera and requires no LiDAR, depth camera, or other specialized sensor. Multimodal feedback, including Text-to-Speech guidance for visually impaired users and vibration alerts for distracted pedestrians, supports use across different contexts.

---


### 17. [Diagnosing Zero-Shot Forgetting in CLIP Fine-Tuning: Attention Drift Characterizes Adaptation, Representation Drift Predicts Transfer Degradation](https://arxiv.org/abs/2611.00042)

**<font color=#1a73e8>作者：</font>** Ruize Xia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning CLIP on a downstream task typically reduces its zero-shot accuracy on other tasks, and quantifying this loss ordinarily requires a labeled transfer benchmark. We study whether the loss can be anticipated from unlabeled target images that are already available during fine-tuning. Four signals are compared: the entropy of CLS token attention, linear centered kernel alignment (CKA) with the pretrained model, embedding drift, and relative weight change. ViT-B/32 is adapted by full fine-tuning (Full FT) and by LoRA on EuroSAT and Oxford-IIIT Pets over four learning rates and three seeds, with an additional ViT-B/16 grid; DTD and GTSRB are held out as confirmation targets, and forgetting is measured as zero-shot retention on CIFAR-100, Food-101, and ImageNet-R. Within a fixed configuration, the change in attention entropy is strongly associated with forgetting (mean $|\rho|=0.860$). Its sign, however, depends on the dataset, the adaptation method, and the backbone, and the pooled correlation falls to 0.361. A block decomposition shows that this sign is determined almost entirely by blocks 7 to 12. CKA ranks runs by retention at $\rho=0.960$, and the ranking is already established after the first of six epochs ($\rho=0.959$). On the held-out targets, CKA reaches $\rho=0.95$, and the block account correctly predicts the sign of the attention change for both datasets. These results support a simple decision rule: CKA is suited to comparisons across configurations, whereas attention entropy is informative only within a single configuration. The evidence is limited to one model family and short training schedules.

---


### 18. [Out-of-distribution AI-generated image detection with zero-phase deconvolution for residual whitening](https://arxiv.org/abs/2611.00043)

**<font color=#1a73e8>作者：</font>** Yusuf Yigit Pilavcı, Antoine Mallet, Vincent Itier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current AI-generated image detection methods struggle in out-of-distribution testing conditions because detectors are usually not robust when evaluated on generators not included in the training set. This work explores a way to mitigate the forensic bias between sources of images -whether real or generated -by removing generator-specific fingerprints. This new training process can be approximated by pre-processing involving a deconvolution operation designed to remove correlated noise patterns inducing loss of generalization. Indeed, we show that whitening the spatial distribution of the image noise residuals can significantly improve the performance of detectors on images coming from generators unseen during training. In particular, an end-to-end CNN model trained on whitened image residuals improves detection by 12.6% on average compared to a training involving original images.

---


### 19. [SparseWAM: Driving World-Action Models are Worth 16 Register Tokens](https://arxiv.org/abs/2611.00044)

**<font color=#1a73e8>作者：</font>** Yixiang Yang, Lizhong Zhang, Xingyu Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) transfer scene-dynamics priors to planning by jointly forecasting future scenes and ego trajectories. However, WAMs built on video generators must generate dense future videos at inference, incurring prohibitive latency, while efficient variants discard the world branch at deployment and thus forgo test-time imagination. Even when dense video latents are replaced with patch-level DINO or JEPA features, these representations still involve long token sequences and encode decision-irrelevant information. We therefore propose SparseWAM, which forecasts in a sparse register space of only 16 tokens per frame, compressed from frozen DINOv2 features and shaped by joint planning-and-scoring pretraining to concentrate decision-relevant information. Within this space, SparseWAM employs a modality-decoupled Mixture-of-Transformers with a causal attention mask that lets action tokens condition on imagined future registers, retaining explicit imagine-then-act reasoning at deployment. Its compactness further enables low-cost multimodal sampling. As a result, our SparseWAM achieves 92.6 PDMS on NAVSIM v1, 90.1 EPDMS on NAVSIM v2, and 39.6 on NavHard at only 164 ms latency, roughly 1/5 that of DriveVA, demonstrating the efficiency of the sparse register space. Code will be released upon acceptance.

---


### 20. [Faces or Models? Where the Age Gap in Facial Expression Recognition Comes From](https://arxiv.org/abs/2611.00045)

**<font color=#1a73e8>作者：</font>** Jessica Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial expression recognition (FER) systems are increasingly used in elder care, yet their accuracy on older faces is rarely measured. This study evaluated five open-source FER models on the FACES database, which holds 2,052 posed photographs of 171 adults aged 19 to 80. The models cross three architectures (ResNet-18, POSTER++ and QCS) with two training datasets (RAF-DB and AffectNet). All models lost accuracy on older faces by 11.7 to 15.2 percentage points. Older faces were harder for people too: human raters lost 8.6 points, a classifier using only facial geometry lost 8.3, and for anger, fear, and happiness older adults differed more from one another when posing. On specific expressions the models fell much further than people did. AffectNet-trained models misread older neutral faces as sad or angry 62% of the time. RAF-DB-trained models lost fear, disgust, and anger instead. The gap persisted after controlling for architecture, image quality, cropping, and expression intensity. When only the final classification layer was refitted on older faces, the gap shrank from 11 to 21 points to 4 points or less, suggesting that the models' learned features can represent older faces and that the deficit lies in how the final layer was trained.

---


### 21. [Circumpolar Wall-to-Wall Detection of Retrogressive Thaw Slumps with Scarce Labels and Extreme Class Imbalance](https://arxiv.org/abs/2611.00046)

**<font color=#1a73e8>作者：</font>** Yili Yang, Heidi Rodenhizer, Robb Young 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrogressive thaw slumps (RTS) are among the most dynamic ground deformations caused by permafrost thaw. Abrupt thaw processes such as RTS could roughly double the contribution of permafrost thaw to climate warming, and already threaten a third of Arctic infrastructure. Circumpolar RTS mapping has advanced quickly, yet released inventories together cover only part of the permafrost region. RTS occupy only 0.1-0.5% of image tiles and labels are costly, so a detector must be designed and evaluated as a rare-target problem. We therefore developed a deep learning system and mapped 20.68 M square kilometres of circumpolar permafrost using 41.6 M tiles of 4.8 m PlanetScope imagery. Training used 22,259 tiles with 2,609 RTS instances in 1,718 of them, and the model was tuned through 172 controlled experiments. A convolutional network matched every alternative tested, including multimodal fusion, foundation-model encoders and masked-autoencoder pretraining, each at far more compute for similar or worse results. Labelled data moved performance most, and a foundation model's advantage appeared only when labels were scarce. Tested once on held-out ecoregions at the real-world prevalence of 0.1-0.5%, the final model achieved an area under the precision-recall curve of 0.812-0.855, an object precision of 0.854 and F1 of 0.644. Deployed wall-to-wall, the model produced a circumpolar map of 19,068 high-confidence detections whose sampled precision ranges from 0.54 to 0.90 by size class. We present an evaluation protocol for rare targets, a controlled account of what governs accuracy under scarce labels, and the circumpolar RTS map the validated model produced.

---


### 22. [TopoMix: Continuous Spatial Mixing for Long-Tailed Data Augmentation](https://arxiv.org/abs/2611.00047)

**<font color=#1a73e8>作者：</font>** Yefan Wang, Yusen Wu, Zihui Ling 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most mixing-based augmentation methods improve generalization through a simple idea: combine two training samples with a fixed global ratio or a hard spatial replacement. While effective, this design leaves little room for local variation, which becomes a more visible limitation in long-tailed recognition, where minority classes are especially sensitive to the quality of augmented samples. We propose TopoMix, a training-free augmentation method that replaces fixed mixing with continuous spatial mixing. TopoMix constructs a smooth spatially varying mask from a low-resolution random control grid, bicubic interpolation, and stochastic non-linear shaping, and uses this mask for element-wise image mixing and label reweighting. Without introducing trainable parameters or auxiliary networks, TopoMix offers a simple way to make mixing more flexible in the input space. Experiments on standard long-tailed benchmarks show that it consistently improves over representative mixing-based baselines, indicating that smooth spatial mixing is an effective augmentation strategy for long-tailed recognition.

---


### 23. [Background Bias Assessment and Mitigation in Plant Disease Detection Using EfficientNet-B0 with Image Processing](https://arxiv.org/abs/2611.00049)

**<font color=#1a73e8>作者：</font>** Majed Molhi, Nishi Gupta, Ali Algumaei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Plant disease detection using deep learning has achieved remarkable accuracies exceeding 99% on benchmark datasets. However, these metrics may mask a critical vulnerability: models may be taking advantage of false background correlations instead of learning real pathological features. This study presents a systematic investigation of background bias in plant disease detection through a two-stage training framework with quantitative validation. We propose a three-condition evaluation protocol testing models on original, leaf-only, and background-only images to directly measure background dependency. Our approach combines standard transfer learning using EfficientNet-B0 and manipulation of background information during optimization. Experimental results on the PlantVillage dataset (20,638 images, 15 disease classes) show that while our model achieves 98.97% accuracy on the original images and maintains 96.62% accuracy on leaf-only images, the performance drops to 23.58% on background-only images. The calculated background bias (BBC) coefficient of 0.762 indicates that a large part of the model's predictive performance depends on leaf-related features rather than background distortions. This research offers clear evidence that even with the most advanced models, environmental shortcuts can be leveraged, and this highlights the importance of bias evaluation. The approach that has been used has laid a foundation for the development of agricultural AI that is ready for deployment. The implementation, models, and evaluation process are all publicly available.

---


### 24. [Auditing GeoFM Evaluation for Field-Extent Segmentation: Label Proxies, Baselines, and When Frozen Features Match Fine-tuning](https://arxiv.org/abs/2611.00054)

**<font color=#1a73e8>作者：</font>** Santosh Pant  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation-model (GeoFM) benchmarks for agricultural field-extent segmentation often rely on cropland land-cover proxies and compare against per-pixel spectral baselines. We measure how these choices affect conclusions using identical single-date Sentinel-2 pixels from six countries. Replacing polygon-derived field labels with ESA WorldCover cropland raises random-forest AUROC from 0.55-0.82 to 0.79-0.96, showing that the proxy creates a more spectrally separable task. On the actual field-extent labels, a from-scratch U-Net reaches 0.89-0.98 AUROC and has higher point AUROC than a Prithvi frozen linear probe in five of six regions. We then compare a frozen backbone and full fine-tuning using the same decoder for Prithvi and TerraMind, with ten matched seeds. At $\varepsilon=0.02$ AUROC, 9 of 12 region$\times$model cells are TOST-equivalent. Kenya is the common failure case: positives cover roughly 0.1% of pixels, and full fine-tuning performs better for both models. Cross-region results are less favorable to frozen models. On AUROC and average precision (AP), the U-Net leads the full 30-transfer matrix, while an exploratory analysis excluding Kenya finds that both frozen decoders outperform their fine-tuned counterparts; no AUROC difference is detected between frozen TerraMind and the U-Net in that subset. For Prithvi, a frozen decoder trains about $110\times$ fewer parameters than full fine-tuning. These results argue for auditing labels and baselines before interpreting GeoFM rankings, and for testing a frozen decoder before assuming that full fine-tuning will help. Our conclusions are limited to single-date, per-pixel field-extent segmentation, not parcel-boundary or instance delineation.

---


### 25. [From Clips to Streams: A Unified Framework for Streaming Sign Language Translation](https://arxiv.org/abs/2611.00055)

**<font color=#1a73e8>作者：</font>** Hoang Quan Dang, Xin Shen, Yanbin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign Language Translation (SLT) research has typically focused on pre-segmented clips, a constraint that disconnects models from the continuous reality of real-world communication. To bridge the gap from clips to streams, we formally define Streaming SLT, a realistic task demanding the joint discovery and translation of linguistic events from continuous, untrimmed video inputs. To address this challenge, we propose StreamSLST, the first end-to-end framework for Streaming Sign Language Segmentation and Translation via Deformable Transformer architecture. Unlike cascaded approaches that suffer from error propagation, StreamSLST employs a parallel decoding strategy to jointly optimize temporal segmentation and translation in a single pass. To enable scalable training on long-form videos, we incorporate a Sentence-aware Sliding Window Sampler that crops continuous streams into trainable units. We further design a Tri-modal Visual-Language Pretraining stage that aligns pose dynamics with textual semantics before joint optimization. To support comprehensive evaluation, we conduct experiments on two real-world streaming datasets, BOBSL and How2Sign, together with two newly constructed synthetic streaming benchmarks, Streaming-Phoenix-2014T and Streaming-CSL-Daily. The results demonstrate that StreamSLST consistently outperforms a matched cascaded segmentation-then-translation pipeline. Interestingly, our analysis reveals that joint optimization learns wider, translation-effective temporal support that simple expansion or rescaling of the annotated spans fails to reproduce. Our work establishes the first robust benchmark for continuous sign language understanding and paves the way for accessible real-world communication interfaces. The source code and data are available at this https URL.

---


### 26. [SemaNorm: Stain Normalization via Semantic and Morphology Alignment for Robust Cross-Hospital Computational Pathology](https://arxiv.org/abs/2611.00056)

**<font color=#1a73e8>作者：</font>** Subhankar Chattoraj, Sawon Pratiher, Arijit Ghosh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stain variability remains a major source of domain shift in computational pathology, yet existing normalization methods largely optimize color consistency without explicitly preserving morphology or diagnostic semantics. We propose SemaNorm, a self-supervised stain canonicalization stain normalizer to recover clean patches from strongly perturbed inputs, avoiding paired transfer, adversarial instability, and identity collapse. It further combines a frozen pathology foundation-model consistency loss with a differentiable nuclei-structure loss to preserve semantic and cellular organization. SemaNorm is evaluated across Camelyon17-WILDS and NCT-CRC-HE-100K using cross-hospital tumor classification, cell-graph morphology metrics, and semantic stability measured with an independent held-out foundation encoder. SemaNorm improves out-of-distribution accuracy by 5.9% over the strongest normalization baseline and by 13.5% over no normalization, while achieving the best morphology preservation. Independent foundation-model and cell-graph analyses further confirm improved semantic and structural stability. These results establish morphology- and semantics-aware optimization as a principled alternative to color-only stain normalization.

---


### 27. [Not All Minorities Are Equal: Fairness Outcomes in Private Image Generation](https://arxiv.org/abs/2611.00059)

**<font color=#1a73e8>作者：</font>** Cohen Archbold, Usman Hassan, Sen-ching Samson Cheung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Differential privacy (DP) provides formal guarantees for protecting individuals in artificial intelligence systems, but its consequences for fairness in generative models remain poorly understood. We investigate how privacy-preserving training affects the representation of demographic groups and visual attributes in generative models of human faces. Across two facial image datasets and multiple privacy levels, we find that stronger privacy can disproportionately degrade the quality and utility of some underrepresented groups, suggesting that privacy can amplify existing disparities. However, representation alone does not explain these effects: several well-represented attributes also experience substantial degradation, while some underrepresented attributes remain comparatively robust. These findings show that the impact of privacy-preserving learning cannot be explained solely by data representation and may depend on the characteristics and interactions of the information being learned. Our results highlight the need to consider both privacy and fairness when evaluating generative models.

---


### 28. [DDEL: Closed-Loop Mutual Enhancement of Dataset Distillation and Ensemble Learning](https://arxiv.org/abs/2611.00061)

**<font color=#1a73e8>作者：</font>** Weiqi Zhang, Yongquan Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation (DD) reduces a training set to a small set of examples, while ensemble learning (EL) combines predictions from several models. When applied in sequence, the distilled set remains fixed as the ensemble learns. We introduce DDEL, a framework that feeds ensemble behavior back into distillation. Each round trains the ensemble, measures loss and prediction disagreement on the source data, and uses these signals to guide the next data update. We implement this loop with distribution matching and a homogeneous three-member ensemble.
Preliminary experiments cover skin lesion classification (ISIC 2019), treatment-response prediction (I-SPY1), and binary two-year prognosis classification (NSCLC-Radiomics). With the same images-per-class budget as the open-loop comparison, DDEL reaches balanced accuracy 0.3471 on ISIC and mean ROC-AUC 0.5120 and 0.5597 on I-SPY1 and NSCLC. The I-SPY1 difference is small, and the ISIC trajectory shows that more rounds do not consistently improve performance. These results offer initial evidence for studying DD-EL feedback, with its computational cost and robustness still requiring controlled evaluation.

---


### 29. [CarDiff: Anatomically Aware Dental Caries Synthesis using Diffusion](https://arxiv.org/abs/2611.00062)

**<font color=#1a73e8>作者：</font>** Sanyam Jain, Bruna Neves de Freitas, Alexandros Iosifidis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic medical image generation can help address limited annotated data in dental imaging, particularly for under-represented caries classes. In this work, we present CarDiff, a semi-supervised framework for dental caries synthesis in panoramic radiographs. The method combines paired mask-image learning with self-supervised generation from augmented masks, while incorporating anatomy-aware conditioning between lesion regions and surrounding structures. Semantic consistency is enforced through segmentation-guided supervision and adversarial anatomical alignment. Experiments on the MLUA-DC1000 dataset show that CarDiff achieves improved synthesis quality compared with existing semantic synthesis baselines, obtaining the best Fréchet Inception Distance (FID) (90.76) and Learned Perceptual Image Patch Similarity (LPIPS) (0.48) scores among evaluated methods. We further assess the generated radiographs for downstream segmentation augmentation across seven architectures. Using a 5x augmented training set improves average Dice score by up to 6.5%, with larger gains observed for medium and combined lesion classes. These results suggest that anatomically consistent diffusion synthesis may be useful for dental radiograph augmentation under limited supervision. The code is available at this https URL.

---


### 30. [Where Generated Floor Plans Stop: Encoding Practice Acceptance Rules to Evaluate Machine Learning Floor Plan Generators](https://arxiv.org/abs/2611.00063)

**<font color=#1a73e8>作者：</font>** Yiliang Shao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine learning floor plan generators are proposed as aids to design decisions, yet they are judged mainly by how closely a generated plan's room adjacencies match the request, a measure without architectural knowledge. We encode an architecture practice's floor plan acceptance rules, taken from its production layout software, as six checks applied in a fixed order, report each plan at the first check it fails, and calibrate the two room-shape limits, which no building code states, so that each alone rejects 5 per cent of built apartments. A transfer specification records which checks public data can carry. Applied to four published generators and two built corpora, RPLAN and Modified Swiss Dwellings (MSD), the checks stop the generators at different points. A room proportion check alone refuses 33.7 per cent of the House-GAN++ plans the checker can read and build, against 5.0 per cent of RPLAN, a gap that survives three measurement controls. At the 5 per cent rate, MSD apartments pass all six checks 5.5 to 23.5 points more often than House-GAN++, depending on the plans counted. The two generators that score best on the adjacency measure, Compatibility, pass least, because of how they represent plans, and within the two that pass most it barely predicts which plans pass. The checks thus expose what the standard measure misses; the checker is released. Passing is not shown to mean acceptance in practice.

---


### 31. [Comparing Monocular and Multi-View 3D Pedestrian Reconstruction Strategies for Urban Intersection Sensing](https://arxiv.org/abs/2611.00066)

**<font color=#1a73e8>作者：</font>** Kauan Mariani, Matheus Carvalho, Joel Perca 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding how pedestrians move and interact at urban intersections is central to traffic-safety assessment, mobility planning, and smart-city sensing. Such analyses rely on physically grounded descriptions of motion: 3D body pose, metric trajectories, and pose-derived descriptors such as stature and walking speed. Recovering these from fixed roadside cameras is difficult: viewpoints are oblique and long-range, occlusions are frequent, and neither ground-truth 3D pose nor cross-camera identity labels are typically available. We compare two strategies for deriving pedestrian motion descriptors from a multi-camera intersection dataset: a monocular learned pipeline that combines text-prompted segmentation, tracking, and learned 3D body estimation, and a calibrated multi-view geometric pipeline that combines 2D pose estimation, tracking, cross-camera association, and triangulation. Because 3D ground truth is unavailable, we evaluate both with reference-free criteria relevant to intersection analysis: pedestrian coverage, anthropometric plausibility, walking-speed distributions, computational cost, and failure modes. The two strategies exhibit complementary trade-offs. The learned pipeline is simpler to deploy and covers more pedestrians, but suffers from scale ambiguity and systematic height compression; the geometric pipeline yields metric reconstructions more efficiently, but requires calibration, discards pedestrians seen by only one camera, and can produce severe outliers in dense crowds. We distill these findings into practical guidance for selecting a reconstruction strategy and configuring camera infrastructure according to the target analysis task.

---


### 32. [SAMP: Self-Adaptive Margin Prioritization For Robust Diffusion Watermarking](https://arxiv.org/abs/2611.00069)

**<font color=#1a73e8>作者：</font>** Yuhao Xue, Jiuan Zhou, Yu Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have made high-fidelity visual generation widely accessible, while also lowering the barrier to producing convincing visual forgeries and complicating content provenance. Existing watermarking methods typically use a fixed embedding strength throughout denoising or treat all watermark dimensions equally. As a result, they may introduce unnecessary distortion when some watermark dimensions are already reliable, while failing to sufficiently reinforce those that are more vulnerable to subsequent perturbations. Therefore, robust watermarking requires adapting both the embedding strength during denoising and the optimization priority across watermark dimensions. To address this problem, we present SAMP, a self-adaptive framework consisting of global margin regulation and vulnerability-sensitive allocation. Global margin regulation adjusts the embedding strength according to the separation between the target codeword and competing codewords, together with the estimated effects of common attacks. Vulnerability-sensitive allocation identifies watermark dimensions that are more easily weakened by local perturbations and gives them higher optimization priority. Experimental results demonstrate that SAMP achieves an average information recovery accuracy of 0.993. Compared with state-of-the-art methods, SAMP improves PSNR by 16.8% and reduces LPIPS by 47.1%. These results validate the effectiveness of SAMP for reliable and high-quality diffusion watermarking.

---


### 33. [How Reliable Are Object Detection Models Beyond Clear Weather? A Deployment-Oriented Robustness Study for Autonomous Driving](https://arxiv.org/abs/2611.00071)

**<font color=#1a73e8>作者：</font>** Munshaibur Rahman Mahin, Isha Das, Most. Sonia Islam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving perception systems must maintain reliable object detection under diverse environmental conditions, not only in clear daytime scenes. However, the cross-weather robustness of modern detectors remains insufficiently characterised under source-only evaluation. This study evaluates representative object detection architectures trained exclusively on clear daytime driving scenes and tested without adaptation under unseen fog, rain, snow, and night conditions. The evaluation covers lightweight and medium-scale one-stage, two-stage, and transformer-based detectors within a unified protocol. Robustness is assessed using performance Drop (%), a Weather Robustness Index (WRI), and class-level sensitivity analysis for critical road participants, including cars, buses, trucks, and persons. Prediction confidence reliability under environmental domain shift is measured using Expected Calibration Error (ECE). Results reveal consistent performance degradation in adverse conditions, reaching 62.90% at night. Buses show the highest sensitivity to environmental variability, while cars remain comparatively stable across weather transitions. Comparisons indicate that YOLO-based detectors exhibit the lowest calibration mismatch, reflecting stronger agreement between predicted confidence and empirical detection correctness. In contrast, DETR achieves the lowest robustness score, with a WRI of 0.6859, indicating greater vulnerability to cross-weather domain shift. These findings offer deployment-oriented insights into detector robustness and confidence reliability for safety-critical intelligent vehicle perception systems.

---


### 34. [CRaFT-XDet: Causal and Robust Fusion Transformer for Dual-Energy X-ray Prohibited Item Detection](https://arxiv.org/abs/2611.00072)

**<font color=#1a73e8>作者：</font>** Moinul Hossain, Munshaibur Rahman Mahin, Taskin Khaleque 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated prohibited item detection in X-ray security imagery is fundamentally constrained by severe object overlap, scanner-dependent domain shifts, and spurious correlations induced by cluttered baggage composition. Existing detectors largely rely on appearance-driven supervision, limiting their robustness and cross-scanner generalisation. We introduce CRaFT-XDet, a causality-grounded and physics- motivated detection framework that reformulates X-ray threat detection as invariant representation learning under attenuation-driven modality variation. Our approach is grounded in a Scanner-Invariant Causal Detection formalisation (Theorem 1), which establishes that minimising the proposed Causal Invariance Regularisation (CIR) objective across partitioned scanner environments approximates the interventional distribution P (Y | do(Xobj)) under standard identifiability assumptions, providing a principled causal formulation for dual-energy X-ray detection. CRaFT-XDet integrates: (i) causal feature disentanglement to suppress context-induced shortcuts; (ii) physics-motivated regularisation to enforce material-consistent embeddings; and (iii) transformer-based cross-energy interaction modelling for structured reasoning in cluttered scenes. With 29.2 M parameters, 89.5 GFLOPs, and 345 FPS (1.7 ms inference), CRaFT-XDet is real-time deployable. Trained on SIXray with five-fold cross-validation, the framework achieves 0.9389 mAP@0.5 and 0.8021 mAP@0.5:0.95. Without domain adaptation, CRaFT-XDet maintains strong cross- dataset performance on OPIXray and HiXray, indicating robust generalization across heterogeneous scanner distributions. In category-agnostic binary threat detection, the model attains 93.92% recall and 0.9031 mean IoU, highlighting reliability in safety-critical screening where missed detections are costly.

---


### 35. [When frequency domain classification is superior to spatial](https://arxiv.org/abs/2611.00073)

**<font color=#1a73e8>作者：</font>** Yanir Harel, Shalom Rosner, Ronit D. Gross 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image classification models largely rely on local characteristics and feature extraction for their predictions. This focused approach works well in the spatial domain, but reportedly falls short in the frequency domain, even though both representations contain the same information. This study demonstrates that the significant reduction in accuracy in the frequency domain stems from the lack of local features. Locally swapping data in the frequency domain significantly decreases its inverse spatial domain accuracy, even below that of the frequency domain; however, the frequency domain accuracy remains relatively constant. Moreover, the use of datasets containing global features in the spatial domain yields higher accuracy in the frequency domain. Using these results, a hybrid model is constructed, combining one model trained only in the frequency domain and another trained only in the spatial domain to achieve higher classification accuracy. The proposed visual geometry group (VGG) and vision transformer (ViT) architectures are trained on the ImageNet-100, WikiArt, DTD, FMD, PSVRT, and KTH-TIPS2-b datasets and evaluated.

---


### 36. [When Morphs Look Better: Face Image Quality as a Training-Free Signal for Morphing Attack Detection](https://arxiv.org/abs/2611.00074)

**<font color=#1a73e8>作者：</font>** Hao Peng, Fu Bo, Mahmoud Elshirbeny 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face image quality assessment (FIQA) estimates the utility of a face image for automated face recognition and has been proposed as a morphing attack detection (MAD) signal that requires no morph-specific training. We evaluate 17 FIQA methods from all current FIQA categories on 20 morphing attack sets from two datasets, FRLL and FEI, including five diffusion-based attack sets. Each quality score is used directly as a MAD decision score. Unlike prior work, which inverted a quality measure when this lowered its error, we fix the score direction of each method in advance from its definition, so that cases in which morphs receive higher quality than bona fide samples remain visible. On FRLL, DifFIQA(R) achieves a mean D-EER of 11.42%, and together with CLIB-FIQA and eDifFIQA(L) clearly outperforms all other FIQA methods. A strong separation of bona fide and morph scores does not imply good detection performance: on the diffusion-based attacks, up to 11 of 17 methods assign higher quality to morphs than to bona fide samples, and the largest reversed separation in the study coincides with the worst detection result of the study. Performance also depends strongly on the attack: GraFIQs(L), the best detector of DCMorph and Arc2Morph on FRLL, performs poorly on the landmark-based and GAN-based attacks. On FEI, the lowest mean D-EER is 39.75%, and a threshold set on the bona fide data of one dataset does not transfer to the other.

---


### 37. [CRAFT: Corrective and Robust Multi-Agent Framework for Text-to-Parametric CAD](https://arxiv.org/abs/2611.00076)

**<font color=#1a73e8>作者：</font>** Mohammed Musthafa Rafi, Anushrut Jignasu, Mahdi Saraeian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-CAD generation has the potential to make mechanical CAD more accessible, but existing approaches face a trade-off between data dependence and output fidelity. Supervised methods rely on large paired text-model datasets, while zero-shot prompting strategies are often brittle and tend to lose the parametric structure needed for downstream editing and customization. We present CRAFT, a corrective and robust multi-agent framework that produces parametric OpenSCAD programs from natural language without task-specific training. At its core is a JSON intermediate representation that carries symbolic parametric expressions throughout the generation process, so the resulting models remain editable and retain their parametric structure. CRAFT combines semantic understanding, parametric planning, compilation, rendering, self-correction, and component-level verification within a layered recovery process, using multi-view visual feedback to detect and repair geometric errors. Across NopSCADlib, ABC, and Slice-100K, CRAFT is competitive with direct zero-shot baselines in perceptual and geometric quality while exposing substantially more editable parametric structure.

---


### 38. [AegisBench: Auditing Aerial Search-and-Rescue Person Detection Under the Conditions It Is Deployed In](https://arxiv.org/abs/2611.00077)

**<font color=#1a73e8>作者：</font>** Amogh Vinaykumar, Prem Kamasani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Drone-based person detection is being adopted by emergency-management agencies to find missing people faster than ground teams can. The benchmarks behind that adoption were collected in calm, clear daylight, while the missions that trigger deployment happen in floods, wildfires, storms, and at night. AegisBench measures that gap. It applies nine physically motivated corruptions from four disaster families, each at three severities monotone in a declared image statistic or physical quantity, to two aerial search-and-rescue datasets, HERIDAL and SARD. Three architecturally distinct detectors (Faster R-CNN, YOLOv11, RT-DETR) are scored across 168 conditions by one shared evaluator, at confidence thresholds frozen on clean validation data as a fielded system would run. Robustness is highly uneven. Low light is the extreme case: a 4.5-stop exposure loss drives recall to exactly zero for all three detectors on both datasets, a result that holds under threshold-free mAP and across three training seeds, and is mirrored on 300 real night drone images, where 2 of 759 people are found. Surviving detections largely stay on target, so the failure is silent: an empty frame looks the same as one whose occupants the system cannot see. Fine-tuning on milder low-light levels recovers 0.06 to 0.19 recall at the held-out severity, at an architecture-dependent cost on other conditions, and does not transfer to real night imagery. Spatial corruptions rank differently on the two datasets, which we cannot attribute to altitude alone because their parameters scale with frame size rather than person size. We release the corruption engine, evaluation pipeline, and all per-condition results as an audit instrument for anyone evaluating these systems.

---


### 39. [From Zero to OCR: A Data-Centric Framework for Unsupported Low-Resource Scripts](https://arxiv.org/abs/2611.00078)

**<font color=#1a73e8>作者：</font>** Faizan Iqbal, Haq Nawaz Malik, Hafsah Pervaiz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical character recognition (OCR) remains inaccessible to many low-resource scripts because annotated document images are unavailable and synthetic training data can fail to preserve script-specific visual structure. We present a data-centric framework that builds end-to-end OCR for such scripts from only an unannotated text corpus and digital fonts, without manually annotating a single training image. A synthetic data engine renders word, line and page images with correct complex-script shaping and automatically derived labels; a YOLOv8 word detector and a convolutional recurrent recognizer trained with connectionist temporal classification learn from these images; and a stage-gate evaluation protocol isolates recognition error before detection is introduced. We demonstrate the framework on Kashmiri, a Perso-Arabic Nastaliq script with approximately 6.8 million speakers that none of six widely used OCR engines supports. Three line-level recognizers, including one transferred from Arabic, stalled between 41% and 79% character error rate (CER), motivating a word-level formulation; subsequent improvements came primarily from rendering fidelity, diacritic-preserving crop margins and tuned non-maximum suppression. The resulting system achieves 0.39% CER on held-out words, 10.0% on synthetic pages and 13.5% on browser-rendered digital pages, and establishes reference results of 18.45% on typeset book pages and 49.8% on degraded historical documents. We publicly release the trained models, the inference code and a synthetic dataset of 285,864 Kashmiri text-line images, and we describe a step-by-step procedure for building OCR for other unsupported scripts.

---


### 40. [Faithful Where You Look: Anchor-Based Evaluation Hides Text Fabrication in Image-Conditioned Video Generation](https://arxiv.org/abs/2611.00079)

**<font color=#1a73e8>作者：</font>** Yujia Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-conditioned video models are used to show real places, so whether their output stays faithful to the place they were shown is a practical question. The text benchmarks we found that check fidelity against a reference do so at an anchor - an annotated region, typically the sign the task is about. We show that this choice hides most of the failure. We conditioned four models from three vendors on 48 street-level references of Tokyo storefronts and measured text fidelity at the annotated sign and in the periphery, the other text the reference covers. At the anchor, all four models are close to a no-model control (anchor text fidelity 0.90-0.94 against 0.996) and are not reliably separated from one another. In the periphery, 36-54% of generated text regions have no counterpart in the reference, against 1.6% for the control, although every prompt forbade new readable text. Two blinded raters agree on which regions are fabricated (kappa = 0.83-0.96), the result held in preregistered rounds on two vendors whose videos the measure had never seen (42% and 56%), and VBench-I2V's reference-based consistency scores show no evidence of tracking it in our sample. Most fabricated text is legible-looking text where the reference shows none or cannot be read - a form that string-matching metrics discard, which is why our own first measure missed it. A preregistered Latin-script replication in London missed its bar in a first round and met it in an independent second round. We release code, annotations, per-video scores, ratings and every preregistration. Code and data: this https URL

---


### 41. [Sequential Transfer Learning for Plant Disease Recognition Across Perennial Crop Domains Using MobileNetV2-CBAM](https://arxiv.org/abs/2611.00080)

**<font color=#1a73e8>作者：</font>** Ropkathaa Choudhury  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: This study investigates whether a learned disease-recognition representation can be progressively reused across distinct perennial crop domains and how its predictive behaviour changes as target-domain heterogeneity increases.
Design/methodology/approach: A lightweight MobileNetV2 framework enhanced with the Convolutional Block Attention Module (CBAM) was evaluated through sequential transfer from Walnut to Cashew, Coffee and Mango, followed by validation on the heterogeneous ABCGMP six-crop benchmark. Each stage used the preceding model representation and was evaluated on an independent test set using complementary classification measures.
Findings: Test accuracy increased from 75.76% for the Walnut baseline to 84.85% after CBAM integration, followed by 90.67% on Cashew, 100.00% on Coffee and 99.50% on Mango. The final ABCGMP evaluation achieved 88.44% accuracy, 81.49% Balanced Accuracy and 0.9949 ROC-AUC. The results show that substantial predictive capability was retained through successive crop transfers, while broader multi-crop heterogeneity introduced a measurable performance constraint.
Originality: The study provides an empirical characterisation of sequential knowledge reuse across multiple perennial crop domains using a common lightweight attention-enhanced representation, extending evaluation beyond isolated source-to-target transfer.

---


### 42. [HistGramBench: Measuring Structural Recovery When Multimodal Models Redraw Historical Mathematical Diagrams as TikZ](https://arxiv.org/abs/2611.00081)

**<font color=#1a73e8>作者：</font>** Minh Quang Tran, Carter He, Cameron Bloch 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital libraries preserve mathematical books printed from the sixteenth to the twentieth century, but the lettered diagrams in them, the figures on which Euclidean proofs depend, remain scanned images whose content cannot be searched. Redrawing such a diagram as a short drawing program would record which points lie on which lines and circles. But a printed plate offers no source code against which the redrawing could be checked. We introduce HistGramBench, a benchmark of 2,507 diagrams from 95 works printed between 1551 and 1933 in eight languages. For each diagram, two AI models from different providers agree on the facts a reader takes from the figure, such as which lines are parallel or where two lines meet, and every redrawing is checked against those facts on the model's own drawing. We evaluate six affordable AI models. The best recovers about three fifths of these facts, and most of what the models miss comes from programs that never produce a drawing. Parallels and tangencies are the hardest relations to reproduce. HistGramBench gives historians and librarians a way to measure when such tools can make old mathematical diagrams searchable.

---


### 43. [Rethinking Feature Perturbation for Single-Source Domain Generalization: A Representation-Space Analysis and Spectral Case Study](https://arxiv.org/abs/2611.00091)

**<font color=#1a73e8>作者：</font>** Badr-Eddine Benelmostafa, Sohaib Baroud  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature perturbation is widely used in single-source domain generalization (SSDG), yet it is typically evaluated by task performance rather than by the representation changes it induces. We investigate whether perturbations can be compared through measurable descriptors of these changes. We introduce a four-dimensional representation-space description comprising feature displacement $D_F$, relational displacement $D_R$, a task-region ratio $\Theta_{\mathrm{Task}}$, and subspace deviation $\Theta_{\mathrm{Subspace}}$. We use these descriptors as an empirical analysis framework, not as a universal geometry, to characterize existing perturbation mechanisms. Across two object-detection settings involving style and weather shifts, we observe distinct geometric profiles and a concentration of relatively strong out-of-domain (OOD) configurations within a bounded region of the descriptor space. These findings do not establish a universal optimum but motivate investigating whether regions associated with stronger SSDG performance can be identified without target-domain access. As a case study, we introduce Dual-Invariant Spectral Perturbation (DISP), a non-learned Fourier-phase perturbation with explicit controls over phase magnitude $\rho$, channel coupling $\kappa$, and frequency support $\mathcal{M}$. We empirically examine how these controls affect the proposed descriptors. DISP achieves strong OOD performance in our experiments, illustrating how explicit perturbation controls can be analyzed through a representation-space description. We hope this viewpoint can contribute to more interpretable, controllable, and ultimately testable approaches to feature perturbation in SSDG.

---


### 44. [A Novel Lightweight Multi-Scale Branching Encoder for Few-Shot Image Classification](https://arxiv.org/abs/2611.00099)

**<font color=#1a73e8>作者：</font>** Oriod Malo, Alexandre Xavier Falcão, Laurent Najman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-Shot Learning (FSL) addresses classification scenarios in which only a small number of labeled examples are available for each class. This paper presents the Sum12 Multi-Scale branching encoder, a lightweight convolutional architecture designed to improve the embedding stage of Prototypical Networks without substantially increasing computational cost. The encoder uses seven parallel convolutional branches whose kernel-size combinations sum to 12, allowing local and broader spatial structures to be represented within a unified Multi-Scale feature space. The proposed architecture was evaluated on Omniglot, CIFAR- FS, FC100, and miniImageNet under controlled few-shot learning protocols and compared with the original Prototypical Network encoder and Inception-inspired branch variants. Additional ablation studies have investigated fusion strategies, dilated convolutions, branch compositions, and receptive field budget. Beyond few-shot learning, the encoder was also tested on the MedMNIST 2D benchmark to assess its behavior in conventional supervised medical image classification. Across these experiments, Sum12 generally improved the low-shot classification performance with respect to the basic ProtoNet encoder while preserving a compact model size. These properties suggest that the proposed encoder may be suitable for low-data visual recognition and resource-constrained intelligent imaging applications. However, complete end-to- end validation on the target embedded platform, including resolution of the observed implementation discrepancies, remains future work.

---


### 45. [Demystifying Prompt Stealing Attacks against Synthetic Video](https://arxiv.org/abs/2611.00102)

**<font color=#1a73e8>作者：</font>** Junyan Huang, Sanskar Agmain, Chen Gong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creators publicly showcase generated content to advertise and sell their work, but these examples may also enable unauthorized reproduction and customization. We study whether an adversary can derive reusable inputs from a single public video for faithful reconstruction and controlled editing, without access to the original prompt or generator. We adapt captioning and prompt optimization approaches to video prompt stealing attacks (PSAs) and find that prompt recovery alone provides limited reconstruction fidelity. Even the original prompt produces different spatial and temporal realizations when the initial noise changes. Using an independent generator enlarges the reconstruction gap, as reusing the original prompt and seed can still produce substantially different videos. We propose V-PSA, which uses a recovered caption and DDIM inversion to construct a reference trajectory under an independent generator. Null-Text Inversion then optimizes per-step unconditional embeddings to reduce deviations from this trajectory during reconstruction. The resulting inputs also guide generation when the caption is modified, supporting edits that change selected content while preserving the target's layout and motion. We construct a benchmark containing 12,000 video-prompt pairs from three victim generators and four prompt sources. V-PSA achieves video-to-video similarity around 0.9 between target and reconstructed videos, substantially improving over prompt-only baselines with similarity score of 0.6, and supports multiple controlled variations that preserve the target's structure. Additional experiments show that augmenting prior image PSAs with inversion-derived inputs also improves reconstruction. Our results show that evaluations restricted to prompt recovery can underestimate an attacker's ability to reconstruct public generative outputs.

---


### 46. [Detector-Integrated Multi-Cue Association for Occlusion-Aware UAV Multi-Object Tracking](https://arxiv.org/abs/2611.00105)

**<font color=#1a73e8>作者：</font>** Shu-Hung Chou, Trong-An Bui, Wei-Ming Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking (MOT) in unmanned aerial vehicle (UAV) imagery is challenging because vehicles are small, visually similar, and frequently occluded, which leads to identity switches (IDSW). Appearance-based trackers such as DeepSORT rely on a standalone re-identification (ReID) network, whose per-target inference limits runtime speed, while the appearance of small or occluded vehicles remains unreliable. This paper proposes a detector-integrated multi-cue tracking framework. Lightweight projection heads are attached to the neck of the YOLOv8n detector to extract target embeddings through ROIAlign, producing detections and embeddings in a single forward pass. A multi-cue association cost then combines motion, IoU, and appearance distances with weights determined through ablation, complemented by low-score rescue and appearance-memory protection. On the UAVDT benchmark, the proposed method achieves a MOTA of 28.33, a HOTA of 31.16, and an IDF1 of 38.18 at 82.59 FPS, the best among the compared trackers in all three metrics, and reduces IDSW by 58.4\% compared with DeepSORT.

---


### 47. [Dynamic Merging Mutually-Distilled Multi-View Networks for RGB-Event-based Representation Learning](https://arxiv.org/abs/2611.00107)

**<font color=#1a73e8>作者：</font>** Futian Wang, Fan Zhang, Xiao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal fusion algorithms combining conventional frame-based cameras and event cameras have recently attracted substantial research attention. Typically, existing approaches convert event streams into frames, voxels, or tensors, and then learn the required spatiotemporal information from these transformed event representations for fusion with conventional frame-camera data. Obviously, such paradigms only exploit the limited representational capacity of event data. Moreover, standard training pipelines fail to fully leverage diverse model parameters obtained throughout the learning process. In this paper, we propose a novel mutual distillation method leveraging multi-view teacher network weights to better integrate multiple event representations and achieve model-parameter level fusion. Specifically, we employ multiple encoders to extract different types of event representations and perform mutual knowledge distillation at both the feature-level and logit-level in this process. Afterwards, we perform a dynamic hierarchical model merge strategy on the model parameters from the first stage to yield a unified multi-modal RGB-Event representation model. Experimental results across multiple event-based datasets demonstrate that our proposed framework achieves significant performance improvements.

---


### 48. [A New Formulation of the Elastica Model with Application to Image Inpainting](https://arxiv.org/abs/2611.00110)

**<font color=#1a73e8>作者：</font>** Zuoqiang Shi, Xue-Cheng Tai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Curves and interfaces play a central role in computer vision and image processing, and Euler's elastica energy is one of the most successful tools to model and manipulate them. The elastica energy is usually computed through a level-set or a phase field representation of the curve, in which the curvature term makes the energy nonlinear, non-convex and, in the level-set case, non-differentiable, so that its minimization is notoriously difficult. In this paper, we propose a new formulation of the elastica model based on a binary representation of curves. The key ingredient is a very simple formula for the curvature: if $\phi$ is the $\pm1$ binary function associated with a curve $\Gamma$, then along $\Gamma$ the curvature is given by $-\frac{1}{C_0\epsilon}\left(R_\epsilon *\phi\right)+O(\epsilon)$, where $R_\epsilon$ is a radial kernel supported in a ball of radius $\epsilon$ and $C_0$ is an explicit constant. No derivative of $\phi$ is involved and the convolution is evaluated by FFT. The resulting energy is a weighted total variation, so that formally the new formulation is a generalization of the well-known ROF model; a phase field type model is obtained from the same curvature formula. Combining FFT with the split Bregman iteration, which for the present problem coincides with an augmented Lagrangian method (ALM), we obtain efficient algorithms whose subproblems are either linear systems solved by conjugate gradient or explicit pointwise formulas. Numerical experiments on the inpainting of binary images are presented to demonstrate the effectiveness of the proposed algorithms.

---


### 49. [SpatialVec: A Unified Representation Learning Framework for Geospatial Objects with Boundary-Aware Sampling](https://arxiv.org/abs/2611.00111)

**<font color=#1a73e8>作者：</font>** Samya Acharja, Kanchan Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial representation learning is essential for Geospatial Artificial Intelligence (GeoAI) applications, enabling machine learning models to capture the geometry, location, and spatial relationships of geographic entities such as points, polylines, and polygons. Existing spatial encoding methods often struggle to preserve fine-grained topological information, particularly for interactions involving complex geometries such as polylines and polygons. These approaches inadequately capture boundary structure and local spatial context, causing topology-sensitive relationships near geometry boundaries to be underrepresented in the learned embedding space. Consequently, accurately modeling complex spatial interactions remains a significant challenge for downstream spatial reasoning tasks. To fill the gap, we introduce SpatialVec, a boundary-aware spatial representation learning framework that adaptively samples geometry boundaries and their surrounding regions, capturing fine-grained geometric structures critical for topology-aware spatial reasoning. A transformer-based encoder-decoder trained through geometry reconstruction produces compact, geometry-aware, and unified representations for points, polylines, and polygons. Empirical evaluation on two real-world datasets shows that SpatialVec substantially improves the preservation of challenging topological relationships involving polygonal interactions and outperforms state-of-the-art baselines significantly on downstream prediction and classification tasks.

---


### 50. [Predicting Cognitive Profiles from Structural MRI using Spatial Graph Representation Learning](https://arxiv.org/abs/2611.00113)

**<font color=#1a73e8>作者：</font>** Taslima Ferdaus Shuva, Md. Tanvir Rahman, Risala Tasin Khan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting cognitive abilities from structural neuroimaging remains challenging due to the high dimensionality and geometric complexity of brain morphology. Conventional models typically flatten regional morphometry into tabular features, failing to explicitly represent spatial relationships. We propose a Spatial-Topological Graph Neural Network (ST-GNN) to predict four distinct cognitive phenotypes across large pediatric cohorts (N = 2,378 to 2,424). By projecting regional morphometry onto a population-level standardized spatial graph, ST-GNN restricts message passing to defined neighboring regions. Evaluations demonstrate that ST-GNN effectively fuses spatial morphology with systemic covariates, outperforming linear baselines and topology-free deep models. Ablations reveal that imposing a sparse geometric topology (K-nearest neighbors) and utilizing global feature scaling - which preserves absolute morphometric scale - outperform fully connected networks and region-normalized approaches. These choices provide transferable architectural inductive biases, revealing differences between computational routing and morphometric feature attribution. Integrated Gradients analysis identified distinct morphological features consistent with neuroanatomical evidence, such as cerebellar volume for working memory and superior frontal surface area for executive function. These findings suggest standardized structural MRI provides useful information for task-specific cognitive prediction, establishing a foundation for MRI-based neurodevelopmental assessment.

---


> [!TIP]
> 当前位于：**1-50**（第 1/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
