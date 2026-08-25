# 📦 其他研究 | 2026年08月26日

> 本类共 **361** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-361](./part-08.md)

---

### 301. [BenthicFlow: Generating Extensible Underwater Environments via Flow Matching](https://arxiv.org/abs/2608.23173)

**<font color=#1a73e8>作者：</font>** Joaquín Figueira, Camile Lendering, Manfred Gonzalez-Hernandez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer vision applications for 3D scene understanding in underwater environments remain challenging due to the lack of high-quality 3D data and the inability of surface-trained models to generalize to underwater scenes. To address this challenge, an emerging trend is to employ generative models to close the data domain gap. However, existing methods assemble large scenes by stitching independently generated tiles post hoc with separately trained models, while demonstrating heterogeneous landscapes only within individual survey sites. We introduce BenthicFlow, a unified framework based on a single conditional flow-matching model that jointly generates aligned textures and depth maps. A MultiDiffusion-inspired sampling procedure reconciles overlapping windows throughout the generative trajectory, enabling spatially extensible RGBD mosaics without a separate stitching model. The generated mosaics are subsequently lifted into explicit 3D benthic environments using surface-aligned Gaussian surfels. Experiments across geographically distinct survey sites demonstrate that BenthicFlow preserves site-specific appearance while generating coherent, large-scale 3D scenes that closely match the target distributions. Code and trained models are available at this https URL.

---


### 302. [Neighbor-Aware View Synthesis for Restoring Missing Views in Light-Field Camera Arrays](https://arxiv.org/abs/2608.23175)

**<font color=#1a73e8>作者：</font>** Sakshi Goel, Ayush Goyal, K S Venkatesh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In light-field (LF) imaging systems, dense spatial sampling from a camera array enables powerful post-capture capabilities such as refocusing and depth estimation. However, real-world LF capture is often affected by hardware malfunctions, where one or more cameras in the array fail, leading to missing sub-aperture images and degraded reconstruction quality. This paper addresses the problem of defective or missing view restoration in light-field camera arrays. We propose a novel generative framework that synthesizes the absent views by exploiting information from a carefully selected subset of neighboring cameras. These selected images, along with a positional encoding map indicating both their locations and the desired target view, are fed into a conditional Generative Adversarial Network (cGAN) trained to generate the missing viewpoint in a geometrically consistent manner. Extensive experiments on synthetic and real-world LF datasets demonstrate that our method produces visually plausible and photometrically accurate reconstructions, outperforming baselines for view interpolation both quantitatively and qualitatively. The proposed framework thus offers a robust and efficient solution for fault-tolerant light-field image acquisition.

---


### 303. [A Comparative Study of Label-free Representation Quality Metrics in Deep Learning](https://arxiv.org/abs/2608.23182)

**<font color=#1a73e8>作者：</font>** Daniel Richards Arputharaj, Daniel Jönsson, Gabriel Eilertsen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a comparative study of label-free metrics for assessing the quality of representations in deep neural networks to understand their reliability under a wide variety of configurations. We group existing label-free metrics into three families based on their construction and analytically establish connections between metrics within the same family. We then characterise the sensitivity of spectral metrics through controlled synthetic experiments. Finally, all label-free metrics are evaluated against downstream task accuracy across a diverse set of 260 vision models on six datasets spanning generic object classification, fine-grained object classification, scene recognition and geospatial task, stratifying results by architecture class and training objective. We find that intrinsic dimensionality (ID) is the most reliable predictor among the metrics considered. However, the reliability of all metrics, including ID, is moderated by architecture class and training objective. Our results provide a clearer understanding of what label-free representation quality metrics measure, when they are reliable, and how to interpret them in practice.

---


### 304. [EchoWM: Open and Enterable Omnimodal World Models](https://arxiv.org/abs/2608.23189)

**<font color=#1a73e8>作者：</font>** Songchun Zhang, Yaowei Li, Junhao Zhuang 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present EchoWM, an omnimodal world model for enterable generative media that responds to continuous navigation while jointly generating 720p video, environmental sound, music and speech. We organize interaction around camera intent: in first-person scenes, it specifies observer motion, while in third-person scenes, camera--character dynamics are learned from data without view-specific controllers. Discrete commands and continuous poses are mapped to a shared metric-scale relative 6-DoF trajectory, with dataset-level calibration preserving motion magnitude across heterogeneous data. To jointly learn audio-visual generation and trajectory control, we construct a complementary data engine and adopt progressive training followed by autoregressive post-training for long-horizon generation. Extensive evaluations show that \model achieves strong trajectory following and high visual quality on public world-model benchmarks, supporting both first- and third-person interaction across varied subjects, and maintaining synchronized environmental sound and speech over long-horizon generation.

---


### 305. [Toward a Foundation Plug-and-Play Prior for Computed Tomography Reconstruction via a Multimodal Diffusion Model](https://arxiv.org/abs/2608.23190)

**<font color=#1a73e8>作者：</font>** Haley Duba-Sullivan, Patxi Fernandez-Zelaia, Obaidullah Rahman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) throughput is limited by scan time, which grows with both the number of projections acquired and the detector integration time for each. Reconstructing high-quality volumes from sparse-view or low-dose measurements therefore depends on an informative prior, typically a neural network trained for one specific scan setting and retrained whenever the modality, geometry, or material changes. We investigate whether a single diffusion model trained across several imaging domains can instead serve as a prior for many CT problems simultaneously. We evaluate the proposed method using the same frozen model on three datasets that differ in modality, beam geometry, material, and degradation type, spanning flaw analysis in additively manufactured metal parts imaged with cone-beam X-ray CT and concrete microstructure imaged with parallel-beam neutron CT. Our proposed method out-performs analytic reconstructions in all three cases, providing a step toward a reusable foundation prior for heterogeneous CT reconstruction problems.

---


### 306. [AI emotional support is better only when chosen, but shifts preferences even when it is not](https://arxiv.org/abs/2608.23196)

**<font color=#1a73e8>作者：</font>** Yaoxi Shi, Cathy Mengying Fang, Guy LabanPattie Maes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People increasingly face a novel decision when seeking emotional support: human or AI. In existing studies, AI's empathic messages are rated as well as or better than humans'. But these studies either assigned the support source or honored people's choice. In real life, support is often incongruent with choice, as people want one source and receive the other. Across three experiments (N = 1,951), participants chose whether to share an emotional experience with a human or an AI, then were randomly assigned to a congruent or incongruent partner. AI support was rated as superior only among those who had chosen it. Yet regardless of congruence, interacting with AI increased willingness to choose it again. In a 28-day study with OpenAI (N = 981), daily conversations shifted preferences toward AI and away from humans, but only when conversations turned personal. Emotional support choices are thus path-dependent, progressively redirecting away from human connection.

---


### 307. [PhiShark2026: A Multi-Layer Active-Web Raw-Evidence Dataset for Phishing Website Research](https://arxiv.org/abs/2608.23199)

**<font color=#1a73e8>作者：</font>** Furkan Çolhak, Ferhat Demirkıran, Hasan Dağ 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing websites are short-lived and rapidly changing, yet many phishing datasets reduce observations to URLs or precomputed features, constraining researchers to predefined representations and discarding the underlying evidence needed to derive alternative features, apply new extraction methods, examine cross-layer relationships, and reanalyze observations as phishing techniques evolve. This study addresses this limitation with a multi-layer active-web dataset comprising 67,502 scans, including 33,387 phishing observations from operational feeds and 34,115 screened benign reference observations. The corpus preserves raw evidence across HTML content and screenshots, URL and redirect behavior, HTTP and security headers, compliance files, TLS certificates, DNS and domain registration, open ports, geolocation and accessibility measurements, and network infrastructure, while explicitly recording unavailable evidence rather than treating it as negative observations. To avoid misleading infrastructure attribution on shared platforms, the study applies a hosting-aware evidence model that masks provider-owned infrastructure signals for free-hosted tenant pages while retaining meaningful page- and transport-level evidence. Characterization reveals systematic differences between phishing and benign websites across web-resource usage, domain maturity, mail and policy configuration, security headers, and infrastructure context. By preserving raw artifacts together with acquisition metadata and explicit evidence availability, the corpus provides an inspectable and reproducible foundation for future phishing measurement and dataset research.

---


### 308. [Learning Spherical Occupancy Profiles for Multi-View 3D Reconstruction and Generation](https://arxiv.org/abs/2608.23206)

**<font color=#1a73e8>作者：</font>** YiHsuan Tsai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study spherical occupancy profiles-the ray-wise occupancy probability profiles P(r) = T(r) o(r) distilled from multi-view 3D Gaussian reconstructions-as a unified intermediate representation for both discriminative and generative 3D reconstruction from images. On a 999-object subset of Google Scanned Objects with 48 turntable views each, we train (i) a discriminative per-ray decoder that injects global view-averaged and ray-specific image evidence into a FiLM-conditioned profile head, reaching median soft depth error 0.035 (normalized) on an independent 90-object test split, and (ii) a generative pipeline built on a profile VAE and a latent diffusion model, which supports unconditional sampling that matches the reconstruction manifold and image-conditioned multi-solution reconstruction whose per-object solution spread is quantifiable and tunable via classifier-free guidance. We further analyze the morphology of predicted profiles: post-hoc power sharpening and a learned sharpening target both recover ground-truth profile width without degrading depth, exposing a monotonic width-peak frontier in the L1-per-ray loss family and motivating a principled redefinition of morphology gates. Real-photo validation on two DTU scenes confirms the pipeline transfers to non-synthetic input. Our results suggest that ray-wise occupancy profiles offer a compact, learned, and uncertainty-aware interface between multi-view reconstruction and generative priors.

---


### 309. [Bee Detection and Tracking at Hive Entrance using YOLO11 and ByteTrack](https://arxiv.org/abs/2608.23213)

**<font color=#1a73e8>作者：</font>** Thi Thu Thao Nguyen, Johannes Reschke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents an automatic bee entrance monitoring system based on YOLO11 transfer learning and the ByteTrack tracking algorithm. The study investigates the influence of data augmentation, backbone freezing, and tracker parameter optimization on the detection and counting of small, fast-moving bees. The detector with progressive backbone unfreezing strategy achieved about 97.0% precision and 98.7% mAP50, while providing more stable convergence than full fine-tuning. Experiments also showed that light augmentation outperformed heavy augmentation. For tracking, ByteTrack parameters were optimized to improve trajectory continuity under low-confidence detections. On an independent 25 FPS side-view video, the optimized YOLO11-ByteTrack system correctly counted 43 of 47 incoming bees (91.5%) and 7 of 30 outgoing bees (23.3%). Error analysis showed that most counting errors were caused by missed detections due to rapid bee motion and motion blur, while tracking failures became less frequent after parameter optimization. Overall, the results indicate that moderate augmentation, progressive backbone unfreezing, and ByteTrack tuning improve the reliability of automatic bee entrance monitoring under realistic recording conditions.

---


### 310. [Aligning Biomedical Texts and Knowledge Graphs: A Systematic Comparison of Lightweight Alignment Strategies](https://arxiv.org/abs/2608.23214)

**<font color=#1a73e8>作者：</font>** Artem Bisliouk, Elizaveta Nosova, Heiko Paulheim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical knowledge exists in two complementary but distinct forms: unstructured scientific literature and structured knowledge graphs (KGs). Aligning them is essential for knowledge grounding, evidence retrieval, and KG completion, yet existing methods do not explicitly align free-text evidence with KG triples. We present a unified framework for systematically studying design choices for aligning biomedical text and KGs. With a text encoder and a KG embedding model both frozen, we learn only a lightweight projection between their spaces via a contrastive objective. This enables a fair comparison across six design dimensions: text encoder, KG embedding model, projection head, triple composition, training direction, and hard-negatives sampling. We construct CTD-Align, a corpus of over 22K one-to-one tripledocument pairs linking chemical-gene interactions from the Comparative Toxicogenomics Database to supporting PubMed passages. We evaluate alignment on it in two retrieval settings: document-to-triple and triple-to-document. We find that the triple composition and the training direction (i.e., shared retrieval space) have the greatest impact, whereas the text encoder and hard-negatives sampling matter little. Overall, simple choices win: projecting text into the KG space with a linear head over concatenated subject, predicate, and object embeddings performs best. These findings establish lightweight contrastive alignment as an effective, practical foundation for bridging biomedical text and KGs.

---


### 311. [BenthicDINO: Physics-Informed Self-Distillation for View-Invariant Side-Scan Sonar Representations](https://arxiv.org/abs/2608.23215)

**<font color=#1a73e8>作者：</font>** Taqi Hamoda, Hayat Rajani, Nuno Gracias  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated perception in side-scan sonar (SSS) imagery is severely hindered by physical acoustic artifacts, resulting in representations that inextricably mix intrinsic seabed reflectivity with transient viewing geometries. Existing self-supervised learning (SSL) frameworks rely on augmentations designed for natural images, failing to account for acoustic degradation and explicitly enforce view-invariance. To address this gap, we introduce a physics-informed self-distillation framework built upon the DINOv3 architecture utilizing a ConvNeXt-v2-Tiny backbone to maximize data efficiency. The proposed methodology enforces view-invariance through two primary mechanisms: physically motivated augmentations that simulate speckle noise, range-dependent attenuation, and radiometric miscalibration; and a Hilbert-Schmidt Independence Criterion (HSIC) penalty that explicitly decouples learned dense patch features from physical viewing parameters. Furthermore, we propose a dense, hierarchical feature fusion strategy across all four network stages to preserve fine-grained sediment details alongside deep semantic abstractions. Extensive evaluation demonstrates that the framework natively groups complex benthic topographies into stable, noise-free semantic clusters without relying on manual annotations. During supervised downstream tasks on the S3Seg dataset, the fused representations exhibited exceptional data efficiency, achieving 96% of its absolute peak performance using only 10% of the available annotated data, ultimately reaching a mean Intersection over Union (mIoU) of 71.4% and an overall accuracy of 86.5%.

---


### 312. [What is mathematics now, and what should it be?](https://arxiv.org/abs/2608.23218)

**<font color=#1a73e8>作者：</font>** Jeremy Avigad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advances in neural theorem provers have been impressive, but the successes obscure a broader vision of what AI can do for mathematics and how mathematicians can engage with AI. This essay advances a more expansive and optimistic point of view.

---


### 313. [Leveraging Remote Traffic Data for Local Air Pollutant Estimation: A Scenario-Based Machine Learning Study Across London Monitoring Sites](https://arxiv.org/abs/2608.23219)

**<font color=#1a73e8>作者：</font>** Valeria Legaria-Santiago, Amadeo Arguelles, Magdalena Saldana-Perez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vehicular traffic is a major source of air pollution; however, the contribution of remotely acquired traffic information to local machine-learning (ML) air-pollution models remains insufficiently characterised. This study evaluates four interpretable tree-based ML models (Random Forest, Extra Trees, LightGBM, and XGBoost) under six predictor scenarios combining progressively larger predictor sets, ranging from remotely acquired traffic, meteorological, and temporal variables alone to the inclusion of measurements from one and four neighbouring monitoring stations, to estimate NO$_2$, PM$_{10}$, PM$_{2.5}$, and O$_3$ concentrations across several sites in London. ML model performance was compared with a ridge linear regression model as a baseline, with spatial interpolation methods and with a cross-site validation experiment. When modelling without data from neighbouring stations, the RMSE for NO$_2$ ranged from 9.73 to 11.66 $\mu$g/m$^3$ without traffic information, compared with 8.72 to 11.52 $\mu$g/m$^3$ when traffic information was included. Additionally, for NO$_2$, SHAP analyses indicate that traffic-related variables can contribute at levels comparable to pollutant measurements from neighbouring monitoring stations in traffic-dominated~environments.

---


### 314. [Mover360: Controllable Object Manipulation in 360° Panoramic Images](https://arxiv.org/abs/2608.23238)

**<font color=#1a73e8>作者：</font>** Haoyi Zhong, Fang-Lue Zhang, Andrew Chalmers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Mover360, a controllable object manipulation framework for 360° images. Unlike perspective images, 360° images in equirectangular projection (ERP) exhibit horizontal wrap-around, latitude-dependent distortion, and global scene continuity, which makes object-level edits difficult for existing perspective editors to produce and for users to specify. To address this, Mover360 centers on object Translation (relocating a specified object within an existing panorama) while supporting reference-guided Insert and Remove as auxiliary tasks. Its interface unifies point-, bbox-, and mask-guided control by encoding each task into a fixed prompt and a compact, ERP-aligned instruction map. In the default point mode, a single click relocates an object, allowing the model to infer a plausible size, support, and illumination using panoramic context and an auxiliary depth condition. Structurally, Mover360 is a lightweight adaptation of a pretrained diffusion transformer. To generate paired supervision, we construct a UE5 data-generation pipeline with surface-aware object placement and randomized illumination, yielding large-scale paired data and a dual-domain benchmark of synthetic and real panoramas with ground truth for all three tasks. Across both test domains and two evaluation protocols, Mover360 outperforms strong baselines for perspective editing, insertion, and inpainting in reconstruction fidelity, semantic consistency, and distributional quality. Code and our benchmark dataset are available at this https URL.

---


### 315. [Semantic Reconstruction and 3-D Detection via Learned Multi-Pair Fusion in RF Imaging](https://arxiv.org/abs/2608.23249)

**<font color=#1a73e8>作者：</font>** Amir Rezaei, Wen-Xin Pan, Giuseppe Caire  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We consider a multistatic radio-frequency imaging problem with anisotropy, in which the reflection from a point depends on the positions of the transmit (Tx) and receive (Rx) arrays. The goal is to label the voxels of a field of view by a finite set of semantic classes and to group them into object instances. For the image formation of each Tx--Rx pair we apply a standard inverse-problem solver, and we feed the resulting per-pair reconstructions into a trained three-dimensional (3-D) U-Net that performs the fusion implicitly and the per-voxel classification explicitly. On a controlled, under-determined multistatic setup, we consider the following image formation methods: back-projection (BP) and the least absolute shrinkage and selection operator (LASSO) from a single deterministic snapshot, and incoherent BP and group-LASSO from multiple fading snapshots. For each imaging method we train a separate U-Net that fuses the six Tx--Rx pairs (its input channels) and assigns each voxel a probability vector over the classes. Taking the most probable class gives a labeled volume---the semantic reconstruction. Object instances and their oriented bounding boxes then follow by geometric post-processing (clustering and principal-component analysis). Across a wide range of signal-to-noise ratio, the semantic reconstruction (scored against ground truth by segmentation intersection-over-union) and the resulting 3-D detection degrade far more gracefully than the classical intensity reconstruction: the detection in particular stays reliable well into noise levels at which that reconstruction has dissolved. Because real scenes contain objects of classes the network was not trained on, we add an explicit unknown class trained by outlier exposure, which labels held-out novel objects as unknown instead of mislabeling them as a known class by reconstructed shape.

---


### 316. [From Multimodal Observation to Interpretable Suggestions: Counterfactual Time-Expanded Relational Modeling of Surgical Teams](https://arxiv.org/abs/2608.23254)

**<font color=#1a73e8>作者：</font>** Vincenzo Marco De Luca, Antonio Longa, Giovanna Varni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In surgery, patient safety is threatened not only by technical issues but also by poor teamwork. However, existing surgical AI-based solutions focus mainly on visual workflow and technical execution, neglecting the modeling of team interactions and missing opportunities to actively support clinicians in improving their teamwork skills. To address this gap, we propose a tempo-relational framework for modeling surgical team dynamics from multimodal observations. By leveraging Time-Expanded graphs, the approach captures both relational structure and temporal evolution, achieving strong expressivity while remaining robust in the low-data regime typical of surgical settings. Beyond prediction, such modeling enables the generation of efficient, interpretable, and actionable suggestions for clinicians. More specifically, we generate suggestions via a counterfactual procedure that identifies minimal yet structured changes in individual behaviors and interaction patterns associated with improvements in team performance. Experiments with simulated surgical procedures show that our approach improves predictive performance in diverse behavioral and interaction goals while offering meaningful insights into team dynamics. This work advances surgical AI beyond outcome-driven prediction towards a socially grounded, team-centric, and actionable paradigm to better understand and support the development of team skills in surgical settings.

---


### 317. [Progressively Learning Heterogeneous Skills in a Unified Latent Space](https://arxiv.org/abs/2608.23258)

**<font color=#1a73e8>作者：</font>** Yue-Yi Zhang, Ming Gong, Linpu He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose HetSkills, a novel framework designed to progressively learn heterogeneous skills within a unified latent space for physics-based character control. The core idea is to treat this latent space as a shared executable interface, enabling seamless integration of skills learned from diverse data sources, supervision forms, and tasks. HetSkills begins by learning a tracking skill that establishes a strong foundation in motion control and creates a shared motion decoder, which can be reused across tasks without the need for retraining or separate controllers. To prevent the text-to-motion skill from exploiting shortcut pathways instead of learning language semantics, we introduce motion intuition distillation to ground text-to-motion generation in language semantics and a task-guidance module that dynamically adjusts actions based on high-level language instructions. This enables HetSkills to preserve natural motion while continuously expanding its skill repertoire, making it highly adaptable for long-horizon tasks. Experimental results demonstrate the effectiveness in motion tracking, text-to-motion generation, motion completion, and downstream task adaptation, achieving impressive success rates even under challenging conditions.

---


### 318. [A Multidimensional Data-Driven Hybrid Transformer Framework for Non-invasive Continuous Blood Pressure Prediction](https://arxiv.org/abs/2608.23276)

**<font color=#1a73e8>作者：</font>** Yuexin Ma, Jingqi Hou, Yuxuan Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective. To develop and evaluate a cuffless continuous blood pressure (BP) estimator using temporal physiological and demographic features. We propose a hybrid Transformer framework to estimate diastolic and systolic BP from ECG/PPG-derived feature sequences. Approach. Rather than raw waveforms, the framework models 10-step sequences of six physiological descriptors and two demographic covariates. A Multi-Source Temporal Encoder Module combines Transformer, Kolmogorov-Arnold Network, and XGBoost branches to capture complementary temporal, nonlinear, and tabular information. A Dynamic Conditional Fusion-Decoder applies differential multi-head attention, token-weighted aggregation, and gated residual correction. A robust composite objective jointly optimizes DBP and SBP. Main results. Using the MIMIC-III Waveform and Clinical Databases, the source pool comprised 28,486 waveform segments from 203 subjects, and feature generation retained 53,621 observations from 166 subjects. On 2,431 segment-level held-out test windows, mean error +/- standard deviation was 0.41 +/- 3.74 mmHg for diastolic BP and -1.60 +/- 5.95 mmHg for systolic BP, with 95% limits of agreement of [-6.93, 7.74] and [-13.25, 10.06] mmHg, respectively. The proportions within 10 mmHg were 98.48% and 94.36%. The framework achieved the lowest standard deviations and narrowest limits of agreement among the locally retrained baselines. Significance. The feature-sequence fusion framework improved agreement with reference BP and fell within numerical AAMI and BHS Grade A thresholds on this split. This retrospective analysis is not formal device validation; subject-disjoint and external evaluation remain necessary before clinical use.

---


### 319. [Spatiotemporally Decoupled Autoregressive Diffusion Model for Human Motion Generation](https://arxiv.org/abs/2608.23279)

**<font color=#1a73e8>作者：</font>** Chengqun Yang, Liang Xu, Yanping Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven human motion synthesis has made substantial development with two core modules of motion representation and generative architecture. For representation, Vector Quantization (VQ)-based methods compress motion data into discrete tokens while latent-based models operate directly in continuous space. However, both of these representations exhibit significant limitations. VQ-based methods suffer from inherent information loss, which compromises the quality, diversity, and generalization of generated motions, while continuous representation on holistic whole-body motion hinders part-level flexibility. For architecture, diffusion and autoregressive diffusion models have demonstrated their superiority, yet the fine-grained controllability over individual body parts is also limited. Thus, we propose a unified spatiotemporally decoupled framework named DeMoDiff, which jointly redesigns representation and architecture. To enhance representation extraction capabilities and offer greater part-level controllability, we present a spatial-temporal VAE that encodes each body joint rather than compressing the whole-body motion into a single latent space. Then, we incorporate spatial-temporal masking and attention mechanisms into an autoregressive diffusion generator, achieving both generative capability and controllable editability. Extensive experiments on the HumanML3D and KIT-ML datasets demonstrate that our model achieves state-of-the-art reconstruction performance and compelling motion generation results. Moreover, our framework demonstrates strong temporal and spatial editing capabilities, further validating its effectiveness. Our project page: this https URL

---


### 320. [Dynamic Topic Modeling for Cross-Corpus Temporal Analysis](https://arxiv.org/abs/2608.23284)

**<font color=#1a73e8>作者：</font>** Ruoxuan Li, Bruce Kogut  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dynamic Embedded Topic Models (D-ETM) provide an interpretable framework for modeling temporal semantic evolution, but cross-corpus comparison remains difficult because topics are often learned independently and aligned only after training, a process that does not guarantee stable topic correspondence across corpora and time. To address this problem, we propose a D-ETM framework that first learns a common dynamic topic space over a merged multi-corpus collection, which we call the shared backbone, then introduces corpus-specific residual adaptation around the frozen backbone without creating separate latent topic spaces. This design preserves a shared topic index for cross-corpus comparison while allowing each corpus to specialize lexically. We evaluate the framework on three temporally structured corpora spanning 97 years: the Corpus of Historical American English, Harvard Business Review, and International Labour Review. Residual adaptation improves corpus-specific fit relative to the shared backbone while preserving the same-index cross-corpus topic trajectories, achieving substantially stronger alignment than full fine-tuning from the same backbone, with $97.5 \pm 0.7\%$ versus $17.9 \pm 1.1\%$ trajectory Retrieval@1, as well as stronger alignment than independent training with post-hoc Hungarian matching. These results suggest that incorporating topic alignment into the model can support more stable over-time cross-corpus comparisons while retaining corpus-specific lexical variation.

---


### 321. [How Much Regularization Survives Averaging? Update Masking in Federated Learning](https://arxiv.org/abs/2608.23286)

**<font color=#1a73e8>作者：</font>** Wenhao Yan, Fu Kuroda, Yucheng Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning on non-IID data seeks flat minima to generalize across clients, and existing methods borrow sharpness-aware minimization from centralized training. There is a second way to reach flat minima, in which the regularization comes for free from noise added to the parameter updates, and it has never been carried over to the federated setting. We show the reason. Masking charges the optimizer for moving in sharp directions. We prove that when each client draws its own mask, federated averaging weakens that charge by exactly the cohort size, and that giving every client the same mask brings it back by a factor equal to the inverse gradient diversity of the cohort. In our experiment setting on CIFAR-10, that factor is 1.19 out of a possible 10. Turning off minibatch sampling raises it to 8.96, while changing data heterogeneity a hundredfold leaves it between 1.17 and 1.50. The configurations keeping the regularization train far too poorly to use.

---


### 322. [Poisson Subspace Clustering: Focusing on the Essentials in Count Data](https://arxiv.org/abs/2608.23287)

**<font color=#1a73e8>作者：</font>** Collin Leiber, Kai Puolamäki, Heikki Mannila  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Count data represented as a matrix of non-negative integer values, such as contingency tables, are prevalent across diverse domains. When clustering such data sets, specific methods are required, as generic algorithms often fail to consider their unique distributional properties, leading to unreliable outputs. An effective strategy is to use well-established statistical models such as the Poisson and negative binomial distributions. We present 3CPO, a clustering algorithm based on statistically solid modeling of count data. In addition to the cluster labels, it identifies a subset of relevant columns, enhancing the interpretability of the results. We propose a simple iterative algorithm that maximizes the posterior probability to find good clustering solutions and discuss its properties. Extensive experiments demonstrate its ability to define high-quality clusters within associated subspaces for various data domains, ranging from gene expressions and texts to economics. Our findings suggest that 3CPO is a robust solution for clustering count data in a statistically sound and interpretable manner. Our code is available at this https URL.

---


### 323. [Spotter: Efficient Urban Visual Localization via Geo-Referenced Facade Landmarks in GPS-Degraded Environments](https://arxiv.org/abs/2608.23290)

**<font color=#1a73e8>作者：</font>** Antoni Valls, Jordi Sanchez-Riera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate visual localization on robotic and wearable platforms remains challenging in dense urban environments. Existing methodologies typically rely on GPS for absolute positioning, yet GPS signals frequently degrade in urban canyons due to multipath propagation. Consequently, standard solutions like visual odometry suffer from unmitigated drift over time, while map-matching techniques struggle to acquire the reliable GPS priors they need, on top of being too computationally heavy for real-time edge execution. To address these limitations, we propose Spotter, a robuts and real-time visual localization framework that uses building facades as a reliable source of global geo-reference, while retaining the capability to integrate GPS signals when available. In an offline stage, Spotter processes Google Street View panoramas by semantically segmenting facades and pairing multi-view stereo depth with cartographic data to build a compact metric database. At runtime, query images are matched via a cascaded retrieval and geometric verification pipeline to recover fine-grained global camera localization. We benchmark Spotter on a newly collected dataset of pedestrian sequences acquired with wearable smart glasses across several districts of Barcelona. Experimental results show that Spotter outperforms odometry-based baselines and achieves localization accuracy comparable to state-of-the-art map-based methods while operating at significantly higher frame rates.

---


### 324. [What Memory Composition Does Not Tell Us About Anomaly Detection](https://arxiv.org/abs/2608.23295)

**<font color=#1a73e8>作者：</font>** Joongwon Chae, Runming Wang, Peiwu Qin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Memory-based anomaly detectors store nominal training patches and score test patches against this memory. A patch selected for coverage therefore becomes a nor- mal reference without a separate check that geometric rarity makes it safe to trust. We probe this coupling with sparse training contamination. Under fixed representa- tions and memory budgets, we compare random, medoid, local, and global coverage selectors. We then use CLEANCON, an out-of-bag cross-image support gate that changes candidate-image eligibility while fixing the representation, absolute mem- ory size, builder, and inference rule. Global coverage strongly over-represents sparse contamination. CLEANCON reduces final-memory contamination to approx- imately zero and increases category-macro P-AP in all 12 matched comparisons. Yet along a retention sweep, the lowest-contamination memory does not attain the highest P-AP; performance continues to improve while contamination rises. Mem- ory contamination therefore does not order the resulting memories by P-AP

---


### 325. [What Remains Normal? Clean Images Miss Useful Near-Defect Normal Patches for Anomaly Detection](https://arxiv.org/abs/2608.23299)

**<font color=#1a73e8>作者：</font>** Joongwon Chae, Runming Wang, Peiwu Qin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Memory-based anomaly detectors store nominal training patches and score test patches against this memory. A patch selected for coverage therefore becomes a nor- mal reference without a separate check that geometric rarity makes it safe to trust. We probe this coupling with sparse training contamination. Under fixed representa- tions and memory budgets, we compare random, medoid, local, and global coverage selectors. We then use CLEANCON, an out-of-bag cross-image support gate that changes candidate-image eligibility while fixing the representation, absolute mem- ory size, builder, and inference rule. Global coverage strongly over-represents sparse contamination. CLEANCON reduces final-memory contamination to approx- imately zero and increases category-macro P-AP in all 12 matched comparisons. Yet along a retention sweep, the lowest-contamination memory does not attain the highest P-AP; performance continues to improve while contamination rises. Mem- ory contamination therefore does not order the resulting memories by this http URL is publicly available at this https URL.

---


### 326. [Evaluating SAT Solver Metrics as Predictors of Human-Perceived Nonogram Difficulty](https://arxiv.org/abs/2608.23300)

**<font color=#1a73e8>作者：</font>** Changdao He, Yibing Ju, Jonathan Calver 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Algorithmic solver effort is often assumed to align with perceived puzzle difficulty, but this assumption is rarely tested against human solving data. We evaluate this assumption for Nonograms, a popular logic puzzle similar to Sudoku in which numeric clues along each row and column determine a unique solution grid. We formulate Nonograms as a constraint satisfaction problem and solve them using existing SAT solvers. We then conduct a user study in which we collect data on both participant interactions and reported difficulty. We find that neither participants' reported difficulty nor their behavioural signals correlate meaningfully with SAT solver metrics; however, we find evidence that expertise moderates the relationship between solver metrics and reported difficulty. In this process, we uncover distinct, recurring solving strategies that indicate human preference for complex propagation, diverging from solver-measured complexity.

---


### 327. [Beyond Point Predictions: Uncertainty-Aware Satellite Poverty Mapping for Public Policy](https://arxiv.org/abs/2608.23322)

**<font color=#1a73e8>作者：</font>** Markus B. Pettersson, James Bailie, Mohammad Kakooei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their critical importance for policy and research, high-resolution poverty data remain limited across much of Africa. Machine learning (ML) with earth observation (EO) imagery has recently emerged as a way to supplement these data by predicting (i.e., estimating) poverty where it has not been directly measured. Yet to be used reliably, decision-makers and analysts need assurances that they will not be misled by the errors in these predictions. To meet this need, we develop an uncertainty-aware EO-ML method for poverty mapping based on simultaneous quantile regression and a novel form of conformal prediction. Using a spatiotemporal transformer trained on sequences of Landsat and nighttime-light images, we produce prediction intervals for neighborhood-level International Wealth Index estimates across Africa which are statistically guaranteed to achieve their desired coverage rates. While our method's point-prediction performance matches the state of the art, its prediction intervals are wider than might be expected given its high $R^2$ of $0.75$. However, other models of similar accuracy likely suffer from comparable uncertainty, pointing to an inherent limitation: even with its remarkably high explanatory power, EO-ML cannot naively be relied upon for policy-making, such as when designing poverty-targeting programs. To handle this challenge, we develop a procedure to efficiently allocate aid using both ground-truth surveys and model predictions while provably ensuring the risk of excluding eligible neighborhoods remains below a prespecified level. In simulations, this approach delivers substantially more aid per eligible recipient than other strategies, thereby demonstrating that EO-ML can indeed be a reliable supplement to traditional data sources---as long as methods

---


### 328. [Flesch-Kincaid Readability Depends Only on the Topic Distribution in Long Texts under Topic Models](https://arxiv.org/abs/2608.23327)

**<font color=#1a73e8>作者：</font>** Yo Ehara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Flesch Reading Ease (FRE) and the Flesch-Kincaid Grade Level (FKGL) are widely used readability scores for English computed from the same two document statistics, yet their stability on long documents need not imply invariance to lexical composition. Surprisingly, under a topic model with an explicit sentence-boundary token, both scores converge almost surely to deterministic functions of the document topic distribution through just two scalar rates: in the long-text limit, all score variation is mediated by topical composition rather than any residual readability signal. The theory covers both formulae, while the experiments evaluate FKGL. In a fixed admixture with rank[1, q, s] = 3, fibres through interior topic vectors are locally (K-3)-dimensional, whereas regular iso-score level sets are locally (K-2)-dimensional and curved. In out-of-fold evaluation on two balanced corpora, Brown and the written BNC, a topic vector inferred from one document half's content words predicts the other half's FKGL at r = 0.779 and 0.884, respectively. On Brown, adding the topic prediction to genre and mean content-word syllable count yields $\Delta R^2$ = 0.002, with a confidence interval spanning zero; on the BNC, the corresponding split-half increment is 0.024, positive in four of five K = 100 fits (median 0.021). Because inferred topics may also absorb genre, register, and style, we do not interpret these results as evidence about human readability or causal effects.

---


### 329. [Thinking Beyond Videos: Unifying Video Reasoning and Deep Research for Open-World Video Agents](https://arxiv.org/abs/2608.23329)

**<font color=#1a73e8>作者：</font>** Wenqi Liu, Shijie Ma, Yunxiao Wang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world video understanding often requires a model to locate sparse visual evidence and acquire external knowledge that is absent from the video and its parametric memory. While Thinking-with-Videos enables active temporal perception and Deep Research supports multi-step information seeking, the two capabilities are typically developed in isolation. We introduce VideoRover, a unified Video Deep Research framework that iteratively coordinates video cropping, multimodal search, and webpage browsing. Given a video-question pair, VideoRover uses each tool result to select the next action, so localized video clips guide external retrieval and retrieved evidence triggers further video inspection and verification. To develop this capability, we construct an automated data curation pipeline, producing 26K verified SFT trajectories and 3K challenging RL instances. We also introduce VideoRover-Bench, a benchmark stratified by video duration and research difficulty. Experiments on VideoDR and VideoRover-Bench show that our VideoRover-8B-RL achieves performance comparable to proprietary models in the direct-answer setting without tool use while outperforming larger open-source models equipped with the same tool suite. Ablation studies and training dynamics further validate the complementary roles of active video grounding, external retrieval, and long-horizon reinforcement learning.

---


### 330. [Controllable blind deblurring with diffusion models](https://arxiv.org/abs/2608.23343)

**<font color=#1a73e8>作者：</font>** Imane Si Salah, Emile Cribelier, Thomas Veit 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image acquisition with a camera involves several degradations due to the optical system, sensor, or low-level processing steps. We address blind deblurring in professional photography: we aim to invert unknown isotropic blur without knowledge of the degradation this http URL such inverse problems,where some high-frequency information is lost, it is challenging to use generative models to produce details that are both photo-realistic and faithful to the input. We propose SuperSharpen, a diffusion-based blind deblurring method offering explicit control over restoration strength through a blur measure. We compare two conditioning strategies: a ControlNet-style adapter on a frozen backbone, and full finetuning of the diffusion prior. Our experiments show that finetuning achieves better fidelity with fewer hallucinated details. We validate our approach on synthetic and real-world blur, demonstrating improved perceptual quality and controllable restoration strength.

---


### 331. [Towards Actionable Surgical Team Dynamics: from Teamwork to Counterfactual Annotations](https://arxiv.org/abs/2608.23344)

**<font color=#1a73e8>作者：</font>** Vincenzo Marco De Luca, Antonio Longa, Andrea Passerini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling team interactions in high-stakes environments such as operating rooms is critical for understanding how coordination, communication, and individual behaviors shape team performance and safety outcomes. Existing datasets in this domain are often fragmented across modalities, annotation schemes, and formats, limiting their ability to support integrated analyses of real-world collaborative processes. We address this limitation by introducing an extended multimodal dataset for surgical team interaction analysis, built from real operating room recordings. Starting from an existing corpus, we construct an analysis-ready version of the data by providing speaker diarization, transcripts, and multi-level annotations capturing team performance, interaction processes, and individual characteristics. Team performance is assessed using a standardized surgical teamwork evaluation protocol, while interaction quality and individual attributes are annotated through structured rating schemes covering collaboration, group dynamics, and non-technical skills. To further support the study of coordination breakdowns and performance variability, we introduce counterfactual annotations that describe plausible alternative team outcomes in the presence of observed interaction failures, enabling analysis of how specific behavioral patterns may relate to different trajectories of team performance. In addition, we provide structured temporal and relational representations designed to support computational modeling of teamwork processes and the design of AI-assisted collaborative systems. The dataset is designed to support the study of how individual actions, interaction patterns, and team-level processes jointly contribute to team outcomes in surgical settings, providing a unified resource for analyzing collaborative behavior in high-stakes domains.

---


### 332. [Beyond the Mirror: Balancing Interaction Modality and Avatar Fidelity in Public 3D Virtual Try-On Systems](https://arxiv.org/abs/2608.23345)

**<font color=#1a73e8>作者：</font>** Yueqian Guo, Tianzhao Li, Xin Lv  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual Try-On (VTON) systems deployed on large public displays face a dual barrier: the physical strain of mid-air interaction and the social inhibition caused by public self-consciousness. This paper presents a real-time 3D avatar system integrating markerless motion capture with dynamic visual fidelity control to investigate and mitigate both barriers. Through a dual-study empirical evaluation, we first decoupled physical fatigue from gesture interaction ($N=20$), demonstrating that interaction fatigue is primarily driven by visuomotor latency rather than the physical act of gesturing; our optimized low-latency gesture pipeline achieved usability comparable to touchscreens while delivering superior immersion and hygiene. Building on these insights, our second study ($N=25$) investigated the "avatar fidelity paradox" via a $2 \times 2$ factorial design manipulating interaction modality (gestures vs. touch) and visual fidelity (photorealistic MetaHuman vs. stylized mannequin). Results reveal that while high fidelity and mid-air gestures independently maximize virtual embodiment ($p < .05$), their combination elicits the highest social awkwardness. Crucially, low-fidelity avatars serve as a "psychological mask" that alleviates public embarrassment during expressive gestures, while mid-air gestures simultaneously act as a compensatory mechanism to preserve perceived try-on trust despite reduced visual realism. Finally, we propose a context-aware fidelity framework to balance privacy, immersion, and commercial trust in public spatial interactions.

---


### 333. [Test-Time Adaptation for ECG Classification via SQI-Gated Self-Training and Beat-Rhythm Consistency](https://arxiv.org/abs/2608.23347)

**<font color=#1a73e8>作者：</font>** Wenhan Jiang, Zhipeng Deng, Jiale Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models for electrocardiogram (ECG) classification often suffer from significant performance degradation when deployed in unseen domains due to shifts in acquisition devices and patient populations. Test-time adaptation (TTA) offers a practical solution by adapting models using only unlabeled data at inference time. However, existing TTA methods often underperform on ECG tasks, since naive online updates ignore the hierarchical beat-rhythm structure of cardiac cycles and are vulnerable to signal artifacts, which leads to unstable adaptation and model drift. We propose BeatRhythm-TTA, an ECG-tailored TTA framework that explicitly accounts for ECG's noisy observations and structured beat-rhythm semantics under domain shift. First, to handle pervasive ECG artifacts, we introduce a Signal Quality Index (SQI)-gated adaptation scheme that selectively filters out low-quality signals to prevent harmful updates. Second, to leverage ECG's beat-rhythm semantics, we enforce dual-level consistency so the model preserves beat morphology and rhythm dynamics while adapting to shifted acquisition conditions. Extensive experiments on multi-label ECG diagnosis across three adaptation protocols, using PTB-XL as the source domain and CPSC2018/Georgia as two target domains, demonstrate the effectiveness of our method, yielding an average +2.70% relative improvement in Macro-F1 over the best competing method.

---


### 334. [Multisensor Measurement of Train Driver Mental Fatigue: From Simulation to Reality](https://arxiv.org/abs/2608.23361)

**<font color=#1a73e8>作者：</font>** Esther Bosch, Rebecca Kruschka, David Schackmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Increasing automation in rail transport shifts the train driver's role from active control to prolonged supervisory monitoring. This creates conditions for mental fatigue (MF) and reduced vigilance. Despite the safety relevance of this issue, evidence on the feasibility and robustness of physiological indicators of MF under operational rail conditions remains limited. Most prior work relies on simulators or lab studies. The present study investigated multiple subjective, physiological, and behavioral indicators of MF in professional train drivers across two complementary settings: a high-fidelity train simulator (n=14) and a real-world rail environment (n=6). To our knowledge, this is the first study to deploy a full multisensor battery under actual train operating conditions. In both settings, a standardized protocol was used comprising a baseline drive, a one-hour auditory n-back task as an MF induction procedure, and a second drive. Heart rate variability and breathing rate showed consistent and theoretically expected changes across both environments, suggesting reduced physiological arousal following the fatigue induction task. In contrast, EEG-based frontal theta power and parietal alpha and beta power, electrodermal activity, blink duration, and behavioral indicators did not show clear mental fatigue-related patterns. Real-world data collection revealed substantial technical challenges related to vibration, sensor connectivity, and concurrent high-frequency data acquisition. These findings suggest that autonomic indicators, particularly HRV and breathing rate, represent the most promising and ecologically robust measures for operational fatigue monitoring in train drivers. However, neurophysiological measures require further validation under realistic conditions before deployment in driver monitoring systems, and larger samples are needed to confirm these preliminary patterns.

---


### 335. [SxSSD: A Secure and Extensible Software-defined Solid State Drive](https://arxiv.org/abs/2608.23365)

**<font color=#1a73e8>作者：</font>** Josh Dafoe, Bo Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Solid-state drives (SSDs) are built on NAND flash memory and expose it to the operating system through a block-based storage interface. As NAND flash has special read/write constraints due to its hardware nature, a translation between OS-level I/Os and raw flash memory I/Os is needed. This results in a flash translation layer (FTL) that creates a ``trusted computing base'' due to its physical isolation from the OS. Building on this trusted computing base, some security designs (e.g., data recovery from malware attacks) can ensure strong data security properties even if the OS is compromised. However, they mostly require modifying the FTL's firmware code, which is hard in practice because the traditional block-based FTL does not provide an interface to modify its internal functions. New flash storage interface designs, such as open-channel SSDs or zoned namespaces, have moved key FTL functions into the OS. These interfaces ease modification of FTL functions, at the cost of blurring the trusted boundary, as the FTL is no longer isolated from the OS.
In this work, we have introduced SxSSD, a secure yet extensible software-defined SSD design. By decoupling internal policy definitions from primitive FTL mechanisms, we allow trusted applications to dynamically and securely define FTL policies and the exposed storage interface (achieving increased flexibility compared to open-channel and zoned namespaces SSDs). Most significantly, SxSSD retains the isolation of traditional FTL execution (achieving security similar to traditional block-based SSDs). We have identified and addressed key security challenges introduced under a compromised OS. In addition, we have implemented a prototype of SxSSD and evaluated its overhead with different FTL policies and storage interfaces. Experimental evaluation demonstrates that the overhead incurred by SxSSD is small compared to native FTL implementations.

---


### 336. [Spectrum-Aware Bounds on Invertibility for Privacy-Enhancing Instance Encoding](https://arxiv.org/abs/2608.23382)

**<font color=#1a73e8>作者：</font>** Seokjin Hwang, Yuting, Kiwan Maeng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instance encoding is a popular empirical technique for privacy enhancement when sharing data to an untrusted server. It transforms sensitive data through an encoding process before sharing, with the hope that the encoding process retains utility but makes it hard to reconstruct the original data. However, most work offers no theoretical guarantee that the encoding process is actually irreversible. A recent work derived a mean-squared error (MSE) bound limiting any adversary's reconstruction accuracy, offering one of the first theoretical results in this domain. This bound, however, has three critical limitations: it is often too loose, only works with randomized encoders (excluding many deterministic encoders practitioners use), and only bounds MSE. We introduce a family of new bounds that (1) are tighter, (2) applicable even to fully deterministic encoders, and (3) can extend beyond MSE to other norm-based similarity metrics, by properly accounting for the encoder's spectral structure. We evaluate our bounds across a range of encoders, datasets, and attacks, showing they hold consistently and improve upon the existing bound.

---


### 337. [Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](https://arxiv.org/abs/2608.23383)

**<font color=#1a73e8>作者：</font>** Nan Duan, Haoyang Huang, Weiyang Jin 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation is progressing beyond isolated clips toward long-form narratives and interactive worlds, requiring models to preserve identities, follow user controls, and remain stable over extended rollouts. We present JoyAI-Echo-1.5, a unified audio-visual generation system with two purpose-built variants. The long-video variant introduces composable cross-shot memory that aggregates visual evidence across multiple prior shots and speaker cues derived from speech-filtered full-shot audio, enabling persistent character appearance and voice identity across flexible combinations of text, image, and memory conditioning. The world-model variant converts heterogeneous navigation inputs into calibrated metric 6-DoF camera trajectories and injects them through a geometry-aware conditioning pathway, enabling controller-agnostic interaction across flexible viewpoints. To support efficient long-horizon generation, we transform a bidirectional audio-visual backbone into a causal few-step generator using progressive teacher forcing and short- and long-horizon Self-Gradient Forcing on self-generated rollouts. Experiments demonstrate strong performance in both settings. JoyAI-Echo-1.5 achieves improvements over existing long-video baselines in cross-shot consistency, visual quality, text alignment, and speech fidelity. Its world-model variant ranks first on WBench, with an average score of 81.7, and achieves leading visual quality and long-horizon persistence on SANA-WM-Bench. Together, these results indicate that memory, geometric control, and rollout-aware training provide a practical foundation for generating coherent stories and continuously evolving interactive worlds. Project page: this https URL.

---


### 338. [Cross-lingual Biography Enrichment via Claim Extraction and Alignment](https://arxiv.org/abs/2608.23390)

**<font color=#1a73e8>作者：</font>** Yifei Song, Ziyang Chen, Emil Sayilov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> English Wikipedia is often treated as the default encyclopedic source, yet non-English Wikipedia editions can contain richer locally grounded information for long-tail figures. We study cross-lingual biography enrichment: enriching an existing English biography with facts supported by a non-English biography about the same person. Focusing on women from non-English-speaking contexts, we introduce \textsc{CLAW-4L}, a benchmark consisting of 300 Wikipedia biography pairs linking an English biography with its French, Chinese or Azerbaijani counterpart, along with claim annotations and a fine-grained claim-pair relation corpus. We propose a claim-based enrichment framework that extracts English claims from both biographies, aligns them to identify enrichment evidence from the non-English biography, and rewrites the English biography using the selected claims. Our results show that non-English Wikipedia biographies provide valuable evidence for improving English biography coverage, while lower-resource settings remain challenging.

---


### 339. [A Threshold Homomorphic Blockchain Architecture for Secure and Scalable IoT Sensor Data Aggregation](https://arxiv.org/abs/2608.23396)

**<font color=#1a73e8>作者：</font>** Narendra Kumar Dewangan, Mounira Msahli  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Homomorphic-encryption blockchain frameworks for IoT sensor aggregation generally rely on classical cryptographic hardness assumptions and seldom account for network topology in liveness and performance analysis. This work introduces Phi-PHE-BC, a topology-aware homomorphic blockchain architecture for secure and privacy-preserving IoT sensor data aggregation. The framework combines threshold Paillier decryption with graph-parameterized security and performance analysis, linking protocol behavior to the validator graph. On-chain Paillier ciphertexts support homomorphic aggregation while providing IND-CPA confidentiality under the Decisional Composite Residuosity assumption, and authentication signatures provide EUF-CMA transaction integrity. Threshold partial-decryption shares are protected by a noise-flooding wrapper that provides information-theoretic privacy under the configured statistical-hiding condition. Under partial synchrony and Byzantine fault-tolerance assumptions, liveness requires validator connectivity kappa(Gv) >= f+1. We derive topology-dependent throughput bounds for tree, star, mesh, and scale-free networks, together with a per-block communication-cost model. A game-theoretic analysis shows that honest validator participation is a dominant strategy under the stated utility model, yielding an all-honest Nash equilibrium. Experiments on Hyperledger Fabric 2.5 show lower end-to-end latency than the selected traditional PHE-blockchain baseline while maintaining controllable threshold-decryption overhead. Results across topology scaling, validator sensitivity, threshold decryption, and Byzantine-load experiments indicate that Phi-PHE-BC is a practical architecture for secure, privacy-preserving, and topology-aware IoT sensor aggregation.

---


### 340. [MomADv2: Reliable Temporal Memory for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.23405)

**<font color=#1a73e8>作者：</font>** Ziying Song, Shengkai Zhang, Lin Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon planning is critical for safe autonomous driving in complex scenarios. Existing methods improve planning continuity with temporal memory, but such memory may become invalid and mislead decisions when the driving command changes. Thus, selectively leveraging useful history while suppressing command-inconsistent memory remains a key challenge. To address this issue, we propose MomADv2, a reliable state-space memory framework for long-horizon end-to-end autonomous driving. At its core, MomADv2 introduces a Selective State-Space Planning Memory Query Module, which filters historical planning queries based on temporal continuity and command consistency, selects planning modes relevant to the current command, and models the evolution of planning intentions through a selective state-space mechanism. To further alleviate local trajectory deviations and error accumulation in long-horizon planning, we design a Flow-Matching Trajectory Residual Refiner. It learns a continuous residual correction field from the refined planning output to the expert trajectory, enabling fine-grained trajectory refinement while preserving the stability of anchor-based planning. Extensive experiments on closed-loop NAVSIM and Bench2Drive, as well as open-loop nuScenes, demonstrate that MomADv2 improves long-horizon planning consistency and reduces the average collision rate by 15.6% over MomAD under 6-second planning.

---


### 341. [Photorealistic Novel View Synthesis of Human Faces using Next-Scale Transformers](https://arxiv.org/abs/2608.23410)

**<font color=#1a73e8>作者：</font>** Federico Stella, Fei Jiang, Zhongshi Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photorealistic novel view synthesis of people remains challenging at high spatial resolutions and across multiple target cameras, where preserving identity, fine appearance details, and geometric coherence is critical. We build on the next-scale autoregressive paradigm and adapt it for human-centric view synthesis by enabling higher image resolutions, multi-view outputs and stronger cross-view consistency in a single forward pass. We train on a synthetic dataset of human faces spanning diverse identities and apparel. Contrary to diffusion models, this paradigm does not need 2D pre-training and, thanks to its next-scale architecture, it benefits from lower-resolution, general-purpose pre-trainings, with the full-sized purpose-specific images being used only in the last training stages. This enables our architecture to converge with a smaller amount of purpose-specific training data, allowing us to use a smaller but more realistic training dataset. The resulting model produces sharp and realistic views, with the option to synthesize multiple novel viewpoints simultaneously for improved agreement across views. Empirically, we observe gains in perceptual fidelity and cross-view coherence on human subjects, demonstrating that next-scale autoregression is an effective backbone for scalable, multi-output human view synthesis. We also couple our pipeline with an existing transformer-based model for pixel-aligned 3D gaussian lifting from multi-view facial inputs, resulting in accurate and photorealistic 3D models of human faces.

---


### 342. [The Axiomatic Trader: Latent Regularity, Information Budgets, and the Canonical Form of a Quantitative Investment System](https://arxiv.org/abs/2608.23416)

**<font color=#1a73e8>作者：</font>** Jiayu Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Systematic trading rests on one article of faith: that regularities found in the past persist. We state it as a time-invariant mechanism driven by an unobserved latent state, and show that it leaves a researcher five constants to declare --- the recurrence bound $Lambda$ at a block length $b$, the invariance defect $epsilon_0$ of the representation it is declared of, the coherence times $ell_i$ of the state's coordinates, the signal ceiling $rho$ and the fraction $kappa$ of it contingent on the regime --- after which the architecture of a correct quantitative investment system is nearly forced.

---


### 343. [ChebBooster: A Training-Free Approach for Efficient Diffusion Transformer Inference via Chebyshev-Inspired Extrapolation](https://arxiv.org/abs/2608.23429)

**<font color=#1a73e8>作者：</font>** Chengjie Lu, Tianchi Deng, Zhengqi He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have shown strong performance in high-fidelity image generation, but their sampling process remains computationally intensive due to full model execution at every timestep. While cache-based acceleration has been explored to mitigate inference cost, naive reuse schemes suffer from low accuracy over long intervals, and Taylor-series-based extrapolation methods often face instability caused by Runge oscillations. In this paper, we propose ChebBooster, a training-free extrapolation framework based on Chebyshev polynomial theory that achieves stable and efficient acceleration for DiTs. Specifically, we adopt the Barycentric formulation to evaluate Chebyshev approximants with high numerical stability and minimal overhead, and further decouple the extrapolation into an offline weight precomputation phase and a lightweight online application stage. Extensive experiments across three representative DiT-based models, including DiT-XL/2, PixArt-$\Sigma$, and FLUX.1-dev, demonstrate that ChebBooster achieves consistent improvements in visual quality and inference efficiency, reaching up to $3.68\times$ latency speedup and $5.12\times$ FLOPs reduction, outperforming existing training-free baselines under diverse generation tasks and resolutions.

---


### 344. [Image-Conditioned Diffusion Models for Quality Assurance of Organ-at-Risk Segmentations in Radiotherapy](https://arxiv.org/abs/2608.23432)

**<font color=#1a73e8>作者：</font>** Clea Dronne, Catharine H Clark, Xavier Loizeau 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate organ-at-risk segmentation is essential for radiotherapy planning, but reviewing segmentations is time-consuming and subjective. We investigate normative modelling for segmentation error detection in head-and-neck CT, comparing a VAE framework with an image-conditioned segmentation diffusion model. Models were evaluated on RADCURE brainstem and spinal cord segmentations using simulated boundary and width perturbations. Error detection was assessed using the Dice similarity coefficient and the Distance to Agreement (DTA) between the input and reconstructed segmentations. While both models detected some simulated errors, regional DTA showed that the diffusion model localised subtle boundary errors more consistently. These results support image-conditioned diffusion reconstruction as a promising framework for localised, anatomy-aware segmentation QA.

---


### 345. [Characterizing Necessary Losers to Explain Tournaments Losers](https://arxiv.org/abs/2608.23446)

**<font color=#1a73e8>作者：</font>** Contet Clément, Umberto Grandi, Jérôme Mengin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the problem of formally explaining why a candidate was not selected by a given tournament rule, by identifying sub-tournaments in which the candidate loses independently of how the rest of the tournament is completed. We define destructive minimal supports as any minimal sub-tournaments satisfying this property, which in formal explainable artificial intelligence correspond to abductive explanations for the question "Why does the loser lose the tournament?". For six common tournament solutions (maximin, uncovered set and its weighted variant, top-cycle, Copeland, and Borda) we provide characterizations of when a candidate is either a necessary loser or a possible winner, we determine the size of the smallest destructive minimal supports, complemented by polynomial-time algorithms for their computation except for the case of the Borda rule which is suspected to be NP-complete.

---


### 346. [Traceable Spectral Inference via Influence Functions: Efficient Data Attribution and Error Proxies for the Ariel Mission](https://arxiv.org/abs/2608.23458)

**<font color=#1a73e8>作者：</font>** Nikki Grens, Luís F. Simões, Kai Hou Yip 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretability is critical for machine learning models deployed in scientific space missions such as ESA's Ariel, where ground truth is unavailable during operations and physical plausibility must be assessed. While most explainable AI methods focus on feature attribution, this work investigates training data attribution through influence functions and introduces three key contributions for operational spectroscopy pipelines. First, influence is reformulated in terms of prediction rather than loss, enabling label-free deployment. Second, by leveraging the closed-form ridge solution of an Extreme Learning Machine, infinitesimal prediction influence is efficiently computed. Third, an influence-based conservative error proxy is derived by propagating training residuals through the influence sensitivities. Evaluated against simulated spectra, the proposed proxy correlates strongly with scale and shape-based spectral errors. Furthermore, influence functions enable the identification of the most influential samples and the approximation of the most harmful ones. Together, these results suggest that this approach can serve as an operational framework for scientific machine learning.

---


### 347. [Diversity-Based Active Learning: An Evaluation of Metric Spaces for Active Learning Selection](https://arxiv.org/abs/2608.23461)

**<font color=#1a73e8>作者：</font>** Siddharth Chilamkur, Dorit S. Hochbaum  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With rapid advancement over the last few years, many different methods are now widely used for classification. However, training these models requires substantial labeled data. Active Learning is a potential solution to this problem. Pool-based active learning minimizes costs by querying only the most informative samples from an unlabeled dataset. Diversity-based approaches, on the other hand, attempt to select a representative subset of the data. There are many different objectives for determining the selection process, including exact K-center, exact K-median, and Greedy K-center. In this paper, we will focus on evaluating the performance of Greedy K-center across a variety of metric spaces: the raw feature space, a Linear Discriminant Analysis (LDA) space, and a model-derived probability space (with and without entropy-based weighting). Using Random Forest classifiers as a baseline evaluator, our empirical results on synthetic and real-world datasets demonstrate that mapping unlabeled instances into a predictive probability space and weighting the result by entropy often dominates the other options for active learning selection with Greedy K-center.

---


### 348. [RAD: Rule-Augmented Relational Anomaly Detection](https://arxiv.org/abs/2608.23468)

**<font color=#1a73e8>作者：</font>** Noah Dahle, Anne Tumlin, Ngoc Tran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection is often applied to data stored in relational databases, yet most existing methods require flattening multiple tables into a single feature matrix. This flattening can obscure entity identity, schema structure, and multi-hop dependencies, limiting the detection of anomalies that depend on relational context rather than isolated feature values. Beyond preserving relational structure, relational anomaly detection raises an additional challenge: how to incorporate symbolic behavioral evidence into learned relational representations. To address these challenges, we study relational anomaly detection, where the goal is to identify anomalous entities or events in a multi-table database. We propose RAD, a rule-augmented relational anomaly detector that combines heterogeneous graph representation learning with refined symbolic rule signals. RAD derives candidate rules from random-forest paths over flattened summaries of the entities or events being scored, refines them into compact interpretable predicates, injects the resulting rule features into the graph model, and learns anomaly scores using reconstruction-based and pairwise-ranking supervision. To evaluate this setting, we introduce a relational anomaly detection benchmark spanning three settings: LANL cybersecurity event detection and two unexpected user-churn anomaly tasks derived from Amazon and H&M relational databases. Experiments show that RAD improves anomaly ranking over flattened tabular detectors and relational baselines under natural class imbalance, achieving the best average rank on AUROC and AUPRC across the benchmark. Ablations show that direct rule injection and ranking-based supervision are key contributors to performance, while edge reconstruction is not uniformly beneficial. Our code and data are available at: this https URL.

---


### 349. [MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters](https://arxiv.org/abs/2608.23473)

**<font color=#1a73e8>作者：</font>** ChengAo Shen, Wenchao Yu, Fangyu Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting (TSF) is evolving toward multimodal and agentic settings, yet using foundation models remains uneconomical in resource-constrained scenarios, where compact, specialized forecasters are more desirable. However, lightweight forecasters typically require substantial training data, limiting their use in domains with scarce, slowly accumulated, or privacy-sensitive time series. To address this dilemma, we investigate the challenging problem of few-shot learning for lightweight forecasters. We propose MetaCaster, a meta-harness-optimized multi-agent framework that uses agentic data generation to automatically train specialized lightweight forecasters from only a few examples and textual contexts. Our work highlights a new TSF paradigm in which agents act not as forecasters but as intermediary engineers that prepare efficient, task-specific forecasters for deployment. Experiments on 18 datasets, 23 state-of-the-art lightweight forecasters, and 14 baselines demonstrate that MetaCaster achieves both data efficiency and computational efficiency while maintaining high-quality TSF performance.

---


### 350. [On the Threat Model of Weird Generalization and Emergent Misalignment](https://arxiv.org/abs/2608.23476)

**<font color=#1a73e8>作者：</font>** Miriam Wanner, Mark Dredze, William Walden  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Narrow fine-tuning on small, domain-specific datasets can produce broad and surprising changes in model behavior-a phenomenon called weird generalization (WG). Yet, it remains unclear what features of the fine-tuning data are necessary for WG to arise. Here, we address this question by investigating a range of plausibly relevant features, including dataset size, composition, language, presentation style, and novelty relative to a model's parametric knowledge. Further, since WG evaluations rely on small question sets that assess the extent of the generalization, we also analyze how sensitive this measurement is to the set of questions used. Experiments with three open-weight models on four datasets show that the degree of WG (1) depends heavily on dataset composition and language (more than on size); (2) is greater for data familiar from pretraining than for novel data; and (3) is sensitive to the set of evaluation questions used. Collectively, these results indicate that WG is a product of quite fragile properties of both training and evaluation data. As such, we argue that WG is more plausible as an adversarial threat-requiring careful data engineering-rather than as a significant hazard inherent to routine fine-tuning.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-361](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
