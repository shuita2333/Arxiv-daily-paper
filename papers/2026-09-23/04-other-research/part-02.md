# 📦 其他研究 | 2026年09月23日

> 本类共 **463** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

---

### 51. [Complementary rPPG-Derived and Lip-Region Frequency Cues for Talking-Face Deepfake Detection](https://arxiv.org/abs/2609.22284)

**<font color=#1a73e8>作者：</font>** Othmane Harraq, Tamer Aldwairi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Talking-face (TF) deepfakes are detected unevenly by rPPG-based methods across generators. We study two lightweight visual-only cues, rPPG-derived waveforms extracted by RhythmFormer and lip-region discrete cosine transform (DCT) coefficients, on the seven TF methods of Celeb-DF++ under a subject-independent protocol. In-domain, lip-region DCT matches or exceeds the rPPG-derived 1D ResNet on every method except SadTalker, and Concat fusion reaches AUC 0.891 against 0.824 and 0.827 for the unimodal baselines. Under leave-one-generator-out evaluation the cues split: each transfers clearly better to three held-out methods, and IP-LAP is near chance for both. Concat averages 0.798 but falls below rPPG alone where DCT transfers poorly, so static fusion only partly exploits this complementarity. Lip-region DCT outperforms full-face DCT on six of seven methods. We treat the rPPG-derived signal as an empirical cue and do not claim it is cardiac in origin.

---


### 52. [Beyond the Survey: A Systematic Empirical Study of Detection and Association in Visual MOT](https://arxiv.org/abs/2609.22291)

**<font color=#1a73e8>作者：</font>** Linh Van Ma, Juhua Hu, Wei Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a comprehensive experimental evaluation and detailed analysis of state-of-the-art multi-object tracking algorithms, with an emphasis on quantifying the individual contributions of detection and association components to overall tracking performance. Unlike existing surveys that primarily offer theoretical categorizations or taxonomies of tracking methods, our work adopts a rigorous experimental perspective grounded in publicly available implementations, providing practical guidance for researchers and practitioners in method selection and system design. We introduce a unified pipeline diagram that consolidates the core components across the two main branches of visual multi-object tracking: tracking-by-detection and end-to-end deep learning paradigms, and systematically analyze the object detection, feature extraction, and data association modules. Through extensive empirical studies on standard benchmarks, including MOT16, MOT17, MOT20, SportsMOT, DanceTrack, and CrowdTrack datasets, we reveal critical insights: (1) detection quality dominates association strategy performance, with detector improvements yielding more than 10% gains compared to less than 5% from refined association strategies; (2) modern deep learning detectors paired with specialized re-identification models significantly outperform joint detection and embedding approaches; and (3) transformer-based end-to-end methods exhibit greater robustness to detection quality variations but at a substantial computational cost. Our findings from extensive experiments provide key insights into component-level effects in MOT, particularly the dominant influence of detection quality relative to association, while offering practical insights for designing and optimizing MOT systems under varying performance and robustness requirements. Code and experimental setups are available at this http URL.

---


### 53. [On The Robustness-Resolution Tradeoff In Temporal Quantization Of Event Streams](https://arxiv.org/abs/2609.22295)

**<font color=#1a73e8>作者：</font>** Sayeed Shafayet Chowdhury, Ruhi Sharmin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event pipelines often discretize asynchronous timestamps before learning. This step looks harmless, but its stability depends directly on temporal resolution. We study this dependence at the representation level. We first show that hard temporal binning is discontinuous: an arbitrarily small timestamp shift near a boundary can move unit event mass between bins. We then define a class of nonnegative, mass-preserving, resolution-faithful continuous encoders and prove that every encoder in this class has global L1 sensitivity at least 2/Delta, where Delta denotes bin width. Linear two-bin interpolation attains this limit. Local support and first-moment preservation also make it unique. Experiments on SHD, N-MNIST, and DVS128 Gesture support the analysis. Across uniform timestamp budgets, linear interpolation lowers mean representation drift by 47-72% while keeping clean accuracy nearly unchanged. On DVS Gesture, it produces zero prediction flips across all tested budgets and three seeds. On SHD, measured drift follows 1/Delta with R^2 = 0.992.

---


### 54. [Yarn tracking of large-scale 3D textile reinforcements using topological material features](https://arxiv.org/abs/2609.22315)

**<font color=#1a73e8>作者：</font>** Hafsa El Herichi, Arturo Mendoza, Yanneck Wielhorski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated segmentation of CT images has become increasingly important to enhance the reliability of simulations through the generation of high fidelity numerical models. This study addresses the challenging task of semi-automatically tracking textile reinforcements in fan blade dry preforms using X-ray CT images captured at coarse resolutions (i.e., above 140 $\mu$m). Our approach offers a scalable, slice-based analysis conducted on planes orthogonal to the main yarn directions, applied to a large-scale real industrial component. This enables accurate identification and tracking of yarn paths while requiring minimal training. The method models three key yarn properties statistically: their typical cross-section shape, their continuity and movement in the 3D space, and their spatial relative arrangement with respect to neighboring yarns. These statistical properties are integrated into a tracking framework via a variational formulation that optimizes all yarn center positions in successive cross-section planes. The method tracks more than 3,000 warp yarns across 1,500 slices and achieves a tracking success rate above 90%. Overall, this work demonstrates a promising approach toward large-scale, automated textile reinforcement annotation, paving the way for more efficient material characterization in complex composite structures.

---


### 55. [ALPINE: Adaptive Localization for Parameter- and Sample-Efficient Few-Shot Learning](https://arxiv.org/abs/2609.22323)

**<font color=#1a73e8>作者：</font>** Neeraj Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot learning research is predominantly evaluated on accuracy alone, with limited attention to the parameter and training-sample budgets required to reach that accuracy - a real constraint for practitioners without large-scale compute. We present an ultra-lightweight (22,249-34,917 parameter) spatial-relational architecture for few-shot image classification that combines fixed Gabor edge-energy guidance with a windowed, content-adaptive patch locator. Under a strictly matched, iso-episode-budget protocol (250 meta-training episodes, 5 canonical seeds, 600 evaluation episodes per seed), our architecture achieves 5-shot accuracy gains, consistent across all five seeds, over Prototypical Networks, Relation Networks, and MAML on both CIFAR-FS and MiniImageNet, while using 27-53% fewer parameters than any baseline. It also converges in fewer training episodes, generalizes better to an unseen fine-grained domain (CUB-200-2011 birds, zero retraining), and is more robust to 50% occlusion and 25% spatial translation than all three baselines. A series of falsification ablations - zeroing relational tokens at inference and retraining without them entirely - shows that the architecture's pairwise relational computation, while present, is not the primary driver of its performance; the content-adaptive patch locator is. We report this honestly, together with a capacity sweep showing a genuine accuracy plateau near 22-35k parameters, and release full seed-level results and checkpoint hashes for reproducibility.

---


### 56. [Dimensionality reduction for AI based hyperspectral image classification based on XAI](https://arxiv.org/abs/2609.22333)

**<font color=#1a73e8>作者：</font>** Vladimir Zeljković, Branka Stojanović, Harald Ganster 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This research addresses the challenge of limited material recycling in wood recycling processes by leveraging artificial intelligence (AI)-based dimensionality reduction. Our study explores the application of convolutional neural networks (CNNs) in multi-channel hyperspectral imaging (HSI), extending beyond RGB channels to over 200 spectral channels. Dimensionality reduction within this context involves streamlining the feature space for AI system training and inference. Focusing on explainable AI (XAI) methods, this paper contributes to a broader research initiative, presenting a solution framework that enhances the sustainability and efficiency of wood recycling processes.

---


### 57. [PAANI : On Device Visual Evidence Fusion and Explainable Guidance for River Robot Simulation](https://arxiv.org/abs/2609.22353)

**<font color=#1a73e8>作者：</font>** Savio Cardoz, Santhiya Rajan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile river monitoring robots must interpret obstacles and water boundaries that geographic waypoints alone cannot describe. On resource constrained platforms, converting imperfect visual predictions into timely and inspectable guidance is a distinct challenge. An object label or steering command does not explain which evidence supports a decision or when that evidence is unreliable. We present PAANI, an on-device perception to guidance architecture that combines a project trained YOLO11n detector and a custom MobileNetV3 Small semantic segmenter with timestamp aligned evidence fusion on Arduino UNO Q. Bounded tracking supplies object persistence, while an explicit corridor policy combines surface labels, accepted detections, urgency and mask uncertainty. Each final advisory exposes its contributing evidence and policy reasons. ROS 2 interfaces connect the local AI pipeline to a separate Gazebo vessel, localization and control testbed. Training uses 10,000 WaterScenes images for four-class detection and 1,127 MaSTr1325 images for segmentation, including 198 segmentation validation images. The selected FP32 ONNX models occupy 14.817 MB. Detector checkpoint test mAP at 0.5 IoU is 0.7388, while the separately evaluated rectangular ONNX export achieves validation mAP at 0.5 IoU of 0.7367. Segmentation ONNX validation mIoU is 0.9750. A five-minute UNO Q recording produced median and 95th percentile pipeline latencies of 467.8 ms and 580.3 ms at a configured 0.5 Hz cadence. The evaluation also identifies black input misclassification and a sampling rate mismatch that prevents the diagnostic apparent motion estimator from collecting sufficient evidence. These results support an inspectable and reusable edge robotics foundation while clearly distinguishing model accuracy and on-board execution from validated on-water collision avoidance.

---


### 58. [Contrastive Siamese Representation Learning for Predictive Maintenance of Electrical Submersible Pumps](https://arxiv.org/abs/2609.22360)

**<font color=#1a73e8>作者：</font>** Seshu K. Damarla, Xiuli Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrical submersible pumps (ESPs) are essential in offshore oil production, where unexpected failures can result in significant operational and financial losses. Accurate predictive maintenance for ESP systems remains challenging due to nonlinear operating conditions, class imbalance, and variability among pump units. To address these issues, this study presents a fault diagnosis framework that incorporates class imbalance awareness by employing Siamese contrastive representation learning and prior-corrected k-nearest neighbor (KNN) classification. The method first extracts discriminative features relevant to fault detection from vibration-domain indicators and engineered harmonic relationships. A Siamese neural network is trained with class-balanced contrastive pairs to construct an embedding space that clusters samples of the same fault type and separates different fault classes. To further mitigate class imbalance during classification, a prior-corrected distance-weighted KNN is applied. The framework is validated using a Leave-One-ESP-Out (LOEO) strategy to evaluate generalization to previously unseen ESP units. Experimental results indicate that the proposed framework delivers robust and consistent fault classification performance under realistic industrial conditions, supporting its potential for reliable predictive maintenance and intelligent ESP system monitoring.

---


### 59. [Common Cause, Not Cross-Attention: Blocking Visual Shortcuts in Audio-Video Generation](https://arxiv.org/abs/2609.22361)

**<font color=#1a73e8>作者：</font>** Jian Xu, Delu Zeng, John Paisley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint audio--video generators are trained on data in which what an event looks like and what it sounds like are strongly, often spuriously, correlated: a particular material, texture, or object appearance co-occurs with a particular sound. This paper is a controlled causal study of the resulting failure mode. Building an AV structural causal model in which the audio is, by construction, independent of the video's nuisance appearance, we show that models which let audio read video directly-through cross-attention or a shared latent-learn a visual shortcut: they predict sound from appearance rather than from the causal event, and collapse when the appearance-event correlation is broken at test time, literally synthesizing the wrong event's sound. Crucially, the popular remedy of routing both modalities through a shared common-cause latent does not fix this: a bottleneck, an unsupervised shared/private factorization, and a faithful shared-prior model all grab the appearance proxy and fail like the direct model. Blocking the shortcut instead requires an intervention on the nuisance. Under the stated SCM and intervention assumptions we prove that counterfactual invariance is necessary and sufficient to identify the causal predictor, and we verify the mechanism across a feature-vector SCM, procedural pixel video, real images with spectrogram audio and a pretrained backbone, moving real digits, and a conditional generator. On a \emph{real, pretrained} video-to-audio generator, an input-intervention test shows the model is far from invariant to sound-irrelevant edits (recolouring or graying a video substantially changes the sound it generates).

---


### 60. [MarsRecon: Self-Supervised and Multimodal Surface Representations for Mars](https://arxiv.org/abs/2609.22379)

**<font color=#1a73e8>作者：</font>** Akshay Naik, Marius F. R. Juston, Jay Mahajan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution orbital imagery offers a rich record of the Martian surface, but sparse geological labels limit supervised representation learning. We present MarsRecon, a geospatially aware pipeline for learning visual and multimodal representations from HiRISE observations of Olympus Mons. The pipeline calibrates NASA Planetary Data System products, extracts valid georeferenced patches, and trains a masked autoencoder on unlabeled imagery. Increasing input resolution and filtering invalid tokens reduced held-out reconstruction loss from 0.1751 to 0.1342 in the principal Stage A model series. We then freeze the visual encoder and align its features with observation text, coordinates, and local--global image context. The strongest current local-primary model achieves image-to-text recall@10 of 0.3787, text-to-image recall@10 of 0.9161, and local-to-global recall@10 of 0.4350 on the held-out test split. These results establish a working Mars-specific pretraining and retrieval pipeline; further crop-overlap controls and downstream geological evaluations are needed to assess the broader utility of its embeddings.

---


### 61. [Style as Cover: Deep Image Steganography via Stylized Transmission](https://arxiv.org/abs/2609.22392)

**<font color=#1a73e8>作者：</font>** Qi Li, Jidong Yang, Huaike Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image steganography hides secret message within normal images, with most existing works relying on cover-preserving transmission. However, such a paradigm becomes vulnerable once the original cover is exposed or can be reliably approximated. In this paper, we propose StyleStegaNet, a stylized image hiding framework that replaces cover matching with style-concealment transmission. Instead of transmitting a cover-like stego image, StyleStegaNet generates stylized stego images conditioned on publicly available style references, redefining steganography invisibility from cover-preserving concealment to behavior-level camouflage based on style transformation. Such a setting poses a substantial challenge to reliable secret recovery, since neural stylization can significantly alter the feature statistics exploited by deep hiding methods. To address this challenge, StyleStegaNet decouples the overall task into four coordinated stages: stego generation, stylized transmission, structure-preserving reconstruction, and secret recovery. Moreover, StyleStegaNet is optimized with a progressive three-stage training strategy, in which wavelet-domain constraints and perceptual supervision guide the recoverable information toward structural representations. We further provide an analysis showing that secret recoverability is largely restricted to the normalized structural subspace, offering a mechanistic explanation for why directly stylized baselines fail and why a reconstruction-guided recovery path is necessary. Extensive experiments on DIV2K and MS-COCO datasets demonstrate the effectiveness of StyleStegaNet. And few-shot image steganalysis with two deep detectors further shows detection accuracy near random guessing, approximately 51\%.

---


### 62. [Differentially Private and Fairness-Audited Score Diffusion for Irregular Longitudinal Health Records](https://arxiv.org/abs/2609.22401)

**<font color=#1a73e8>作者：</font>** Taimoor Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sharing irregular longitudinal health records can accelerate model development, yet synthetic releases may leak participation, distort temporal dependence, suppress rare events, or reduce utility for underrepresented groups. We present TRUST LONGSYNTH, an auditable patient level private generator that combines bounded sufficient statistics, zCDP accounted Gaussian releases, conditional analytic score diffusion, block banded temporal covariance, separate missingness and gap models, and a protected event sampling floor with population weights.
The method was evaluated on five independently generated, three cohort benchmarks containing 720 patients, fourteen irregular observation slots, six mixed variables, informative missingness, and a rare deterioration outcome. At epsilon = 12 and delta = 10 to the power of minus 5, TRUST LONGSYNTH achieved mean train synthetic test real AUPRC 0.342, Brier score 0.088, expected calibration error 0.082, correlation error 0.222, autocorrelation error 0.317, and membership attack AUROC 0.499.
Relative to the private diagonal score baseline, AUPRC increased by 7.5 percent, while Brier, calibration, correlation, and autocorrelation errors decreased by 6.1 percent, 17.0 percent, 28.0 percent, and 30.1 percent, respectively. The method did not dominate every nonprivate or discrete baseline, and corrected paired tests were inconclusive with five seeds. Canary exposure was 1.8 percent, compared with 28.8 percent for DP Score in the same stress test.
These findings support a transparent privacy utility fairness evaluation protocol, not clinical validity or unconditional release safety, and motivate governed external validation on real multi site records.

---


### 63. [Social Influence and the Allocation of Scientific Attention in AI Populations](https://arxiv.org/abs/2609.22408)

**<font color=#1a73e8>作者：</font>** Maxim Chupilkin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are becoming participants in the evaluation and use of scientific research. They encounter citation counts, download statistics and lists of popular articles developed around human readers, but the collective consequences of these signals for artificial readers remain uncertain. This paper adapts the Music Lab design to a market for academic attention. In the first experiment, 1,000 AI agents choose papers from the titles and abstracts of all 114 regular research articles published in the American Economic Review in 2025. The experiment has five independent-choice communities and five social-influence communities, each with 100 sequential agents. Only agents in the social-influence condition observe earlier selections within their community. Agents may select any number of papers. Social-information communities select 17.2 percent fewer papers per agent, concentrate their choices more heavily, and collectively cover 73 papers, compared with 90 independently. Between-community variation is greater under social information. In a second experiment with 200 agents across twenty social communities, randomly assigning papers five initial selections raises their subsequent selection rate by 45.55 percentage points (95% CI: 41.20 to 49.90). Choices have modest correspondence with external citations and little correspondence with download counts. The results show how a simple information rule shapes the volume, breadth and distribution of scientific attention in an artificial population.

---


### 64. [Learning 3D biophysical cell properties from 2D images and cell-population statistics](https://arxiv.org/abs/2609.22410)

**<font color=#1a73e8>作者：</font>** Santiago Hernández-Orozco, Hector Zenil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inferring 3D cellular properties from 2D microscopy is difficult when a reference instrument reports only population statistics rather than labels for individual cells. Here we develop a population-supervised framework that maps single 2D red-cell images to latent biophysical quantities and aggregates them to mean corpuscular volume, red-cell distribution width and mean corpuscular haemoglobin. The model combines shared local inference, a biophysically structured decoder for volume and haemoglobin, learned instance weighting and device-specific calibration. We formalise conditions under which aggregate observations identify restricted instance predictors, show why population agreement does not by itself identify single-cell properties or 3D geometry, and derive the dispersion penalty induced by subset mean matching. The development dataset comprises 390 specimens and 1,105 acquisitions across six devices, with reported Pearson correlations of 0.86--0.98 against a Sysmex analyser. The framework provides a testable route from 2D images and population supervision to 3D cellular biophysics without claiming explicit 3D reconstruction.

---


### 65. [Complex-valued Phase-Coherent Transformers](https://arxiv.org/abs/2609.22415)

**<font color=#1a73e8>作者：</font>** Leona Hioki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex-valued Transformers have inherited softmax attention over the raw complex inner product. Outside natively complex domains this standard form stays near chance, and no complex attention had been shown to correct it. We show that the match must be a scaled cosine score: L2-normalise queries and keys, so the score reads their cosine similarity and ignores their magnitudes, and hold that score at order-one scale. With this the same models train on four diagnostic tasks under two different gates; without the normalisation they stay at chance on ListOps and Needle under both gates and fall far below on the other two, and a normalised score placed at too small a scale fails as well. The resulting family of phase-coherent Transformers (\PCT) matches or exceeds the strongest real-valued baseline across long-range memory, positional retrieval, hierarchical reasoning, frequency-domain classification and physical complex signals; it shows no degradation up to depth 20; and its loss decreases log-linearly over a 61-fold range of parameters. A member of the family, complex screening combined with a phase-coherent recurrence, is the first genuinely complex-valued neural network to solve Path-X, with 91.6% of its trainable parameters complex-valued against 38.2% for S4. We record these as signs of generalisation not previously seen in complex-valued neural networks.

---


### 66. [Connected Content Retriever: Dense Graph Edge Features Powering Pre-Ranking at LinkedIn](https://arxiv.org/abs/2609.22441)

**<font color=#1a73e8>作者：</font>** Akhilesh Gupta, Sudarshan Srinivasa Ramanujam, Chirag Bhanuprasad Mehta 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In large-scale recommendation systems like the LinkedIn Feed, content generated by a member's network (connections and follows) makes up over 70% of impressions and engagement. It is therefore essential that the pre-ranking layer forwards the best possible few hundred candidates to the ranking layer. LinkedIn's professional knowledge graph carries engagement signals across both the first degree network (connections and follows) and the second-degree network: posts that a 1st-degree connection reacted to, commented on or reshared but did not author (a.k.a. stranger viral). Due to this fan out, the resulting candidate index exceeds one billion; selection of activities from the viewer's network narrows it down to roughly tens of thousands of activities that must be scored within a 120 ms p99 latency budget. We present Connected Content Retriever (CC Retriever), a pre-ranking system that scores these candidates with a full deep ranking model on GPUs at low latency. At its core is a sorted-search GPU primitive that joins dense graph affinity features (viewer to author) with document level features stored on the GPU at runtime in 5-10 ms. The shift to GPU served scoring enabled a 50x scale up of the ranking model's parameters and delivered a +2.5% lift in content time spent on the LinkedIn Feed in online experiments, significantly higher than the typical gains observed in LinkedIn Feed experiments. In this work, we describe the feature set we leverage from LinkedIn's economic graph and the model architecture used for scoring, with a particular emphasis on the online system that scales the stack.

---


### 67. [Visual Embellishments are Potential Distractions in Double-Column Reading](https://arxiv.org/abs/2609.22477)

**<font color=#1a73e8>作者：</font>** Songwen Hu, Chase Stokes, Marti Hearst 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Eye-catching graphics, such as circular figure labels and word-scale visualizations, are increasingly being placed directly within long-form text paragraphs. Some research has claimed that inline visualizations can help readers understand data-rich passages more clearly. However, research in the science of reading calls into question the introduction of images within the flow of text. In this work, we conduct an exploratory study of eye movement in both the presence and absence of visual embellishments. Using a high-resolution eye-tracker (EyeLink Portable Duo), we observed small mean increases in vertical and cross-column saccade rates among six participants, with substantial variation among readers and no detected difference in comprehension accuracy. Mean subjective ratings for the data-light circular-glyph passage indicated it is more distracting than its unembellished comparison passage. These exploratory observations differ from prior findings and motivate a larger, fully crossed study of inline graphics.

---


### 68. [Spatiotemporal Flux Probing for Single-Photon Videography](https://arxiv.org/abs/2609.22479)

**<font color=#1a73e8>作者：</font>** Jerry Yan, Matteo Forlivesi, Bowen Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the problem of recovering high-speed videos from dynamic scenes under extreme photon sparsity. Existing methods rely on aggregating photon detections in local spatiotemporal windows to improve signal-to-noise ratio; however, this local grouping discards global structure and fails in low-light regimes where photon detections are sparse in space and time. In this work, we show that the information needed to recover both motion and illumination is encoded in correlations over the full space-time pattern of photon arrivals. Building on this insight, we develop a spatiotemporal flux probing theory and an algorithm that estimates the Fourier coefficients of the underlying intensity directly from the photon stream. We demonstrate that our approach (1) recovers fast motion and temporal illumination dynamics with substantially fewer photons than prior methods, (2) enables velocity-selective videography that automatically refocuses video onto specific detected motions, and (3) generalizes across sensing modalities including single-photon, event, and spike cameras.

---


### 69. [COREM: Cosine-Relation Momentum Reshaping with Stateful Writeback](https://arxiv.org/abs/2609.22487)

**<font color=#1a73e8>作者：</font>** Yan Wang, Xiaochuan Wang, Yuxiang Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix-valued optimizer states may contain relational structure that is not captured by treating their entries independently. We study whether relations within matrix-valued optimizer states can be exploited to improve optimization. To this end, we introduce a unit-relation-transform abstraction and instantiate it as COREM, a Cosine-Relation Momentum Reshaping method with stateful writeback. COREM partitions the momentum state into update units, computes cosine relations among them, and uses these relations to reshape the momentum before writing the transformed state back to the optimizer. This stateful mechanism allows the reshaped momentum to affect not only the current update but also future optimization dynamics. We evaluate COREM on CIFAR-10 with an MLP and on enwik8 with a Transformer. Compared with Muon, COREM shows lower early-stage step efficiency but stronger improvement in the mid-to-late stages of training, achieving better final validation performance on CIFAR-10 and comparable final performance on enwik8. Spectral diagnostics on enwik8 show that COREM consistently increases entropy effective rank and reduces the concentration of singular energy in dominant modes, while preserving an anisotropic spectrum. For square matrix updates, COREM requires approximately 13.3% of the transformation FLOPs of Muon with five Newton-Schulz iterations.

---


### 70. [CultureMINE: Datasets and Methods for Improving the Cultural Capabilities of NLP Systems](https://arxiv.org/abs/2609.22494)

**<font color=#1a73e8>作者：</font>** Tania Chakraborty, Eylon Caplan, Zhaoqing Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, there has been a surge of interest in Cultural NLP, with substantial efforts to create globally inclusive NLP systems. The rapid growth of literature in this field makes it difficult to track trends in methods and data resources. To address this, we analyze over 375 papers to answer three complementary questions: (1) What Cultural Capabilities (CCs) are being targeted in NLP systems? (2) How are cultural data resources being created? and (3) What methods are being used to improve the CCs of those systems? We discuss trends observed across the three questions, and identify relevant research gaps. To facilitate further research in this field, we release our full list of analyzed papers in the form of an interactive web interface, which includes a feature to allow researchers to add their work; we hope this facilitates future research and proves to be a valuable resource for the Cultural NLP community.

---


### 71. [Event-Frame Fusion for Inter-Frame Segmentation via Event-Guided Motion](https://arxiv.org/abs/2609.22500)

**<font color=#1a73e8>作者：</font>** Dalia Hareb, Jean Martinet, Benoit Miramond 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous navigation requires precise and efficient semantic segmentation, yet existing frame-based approaches remain limited by motion blur, glare, latency, and the low temporal resolution (20-30 FPS) of conventional cameras, which leads to information loss between frames. Event cameras have emerged as an alternative sensing modality, capturing intensity changes asynchronously with high temporal resolution, high dynamic range, and sparse outputs. However, event-based algorithms still fall short of frame-based ones in accuracy, as most segmentation methods are designed for dense frame data. To overcome these limitations, we propose a hybrid vision architecture that combines conventional frame-based and event-based cameras. The system integrates two complementary components: (1) a compact Spiking Neural Network (SNN) with 42k parameters for motion estimation, and (2) a lightweight event-driven SNN with 0.84M parameters for frame-based semantic segmentation, which interpolates motion between frames to refine segmentation results. By predicting inter-frame segmentations, the framework achieves segmentation rates of up to 500 Hz with an energy consumption below 1.87 mJ per inference, while maintaining real-time GPU execution at frequencies up to 200 Hz. Additionally, our approach compensates for information loss in frames affected by blur or overexposure, enabling more robust perception in challenging conditions.

---


### 72. [Rethinking Vision Architectures with Gated Linear Attention and KAN](https://arxiv.org/abs/2609.22506)

**<font color=#1a73e8>作者：</font>** Ali Mehizel, Oussama Khaldi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers allocate most parameters to multi-layer perceptrons (MLPs) for channel mixing, while token interactions usually rely on quadratic multi-head self-attention (MHSA). Linear attention reduces sequence complexity to O(N), but remains coupled with the same fixed-activation MLP as softmax Transformers. Kolmogorov-Arnold Networks (KANs) instead place learnable univariate maps on edges, yet prior vision KANs keep MHSA or omit attention entirely. We introduce LKAT (Linear Kolmogorov-Arnold Transformer), an isotropic ViT encoder that couples chunkwise Gated Linear Attention (GLA) with a two-layer KAN feed-forward, and we provide an I/O-aware fused RBF-KAN kernel for the radial-basis grid maps. Under a shared DeiT-style recipe we compare LKAT with ViT, ViT-5, and MLP-Mixer. LKAT-B exceeds ViT-B/16, ViT-5-B, and Mixer-B/16 on ImageNet-100. Tiny/Small/Base LKAT variants scale consistently on CIFAR-10/100, and ImageNet-100 pretraining transfers to CIFAR fine-tuning. The results support gated linear attention and KAN-based radial-basis functions as complementary inductive biases for mid-scale visual representation learning.

---


### 73. [EmbeddGAN: A Novel GAN Framework Using an Embedding Network and Gini Distance Correlation](https://arxiv.org/abs/2609.22508)

**<font color=#1a73e8>作者：</font>** MaTais Caldwell, Yixin Chen, Xin Dang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative Adversarial Networks (GANs) have demonstrated strong performance in generating high-quality synthetic data. However, they are limited by no formal guarantees regarding convergence and the effectiveness of the learning process. In practice, this leads to training instability, mode collapse, and sensitivity to hyperparameters. To address this, we propose EmbeddGAN, a novel adversarial training framework based on a dependence-based objective. Instead of relying on a discriminator that classifies samples as real or fake, EmbeddGAN introduces an embedding network that learns a representation in which statistical dependence between samples and their real/fake labels is maximized, while the generator is trained to minimize this dependence. This objective is implemented using the Gini distance correlation (gCor), which equals zero if and only if the embeddings are statistically independent of the real/fake label. Minimizing this objective therefore encourages real and generated samples to become statistically indistinguishable in the learned embedding space. The embedding network projects both real and generated data into a shared low-dimensional space, where distributional discrepancies can be measured directly through pairwise distances. We adopt a minimax training strategy: the embedding network maximizes the Gini distance correlation (maximizing dependence), while the generator minimizes it (minimizing dependence). Experiments on the MNIST, CIFAR-10, and CelebA datasets demonstrate that EmbeddGAN achieves competitive performance relative to established baselines while exhibiting notably stable training dynamics on the evaluated datasets.

---


### 74. [The Choreographic Genome: Amplifying the Silent Structure of Text into Dance](https://arxiv.org/abs/2609.22519)

**<font color=#1a73e8>作者：</font>** Michael Li, Alison Ding  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative artificial intelligence have enabled the synthesis of complex human motion with unprecedented fidelity. However, current text-to-motion systems rely strictly on linguistic semantics: if an input reads "I put my hands up", the model searches for a pose with raised hands, and every non-semantic property of the text is discarded as noise. In this work, we treat that discarded structure as the signal. We present an embodied visualization instrument that amplifies not what a text means, but how it is built. Our method first quantizes dance kinematics into a motion codebook of 256 stylistic "regions" using Principal Component Analysis and K-Means clustering, and orders those regions along the dominant axis of movement. We then map the raw byte representation of any input text directly onto this codebook, producing a deterministic sequence of regions that we call the text's "choreographic genome". A precomputed plausibility graph and a set of physics smoothing routines turn this genome into fluid, full-body movement, so that the dancing body becomes a display surface for the byte-level structure that semantic systems ignore. Through a series of artistic case studies, including a Shakespeare sonnet, a machine error log, source code, an abolitionist's question, and Indigenous and Devanagari scripts, we show that each text produces a visibly distinct dance, and that scripts marginalized by ASCII-centric computing are amplified into close to three times as much movement per character. We frame this not as a motion-synthesis benchmark, but as a critical and poetic visualization that asks what we choose to count as signal, and what we allow to go unheard.

---


### 75. [Tick-Tock on the Open Fronthaul: Securing Synchronization in O-RAN](https://arxiv.org/abs/2609.22525)

**<font color=#1a73e8>作者：</font>** Yiwei Zhang, Enrico Pisanti, Imtiaz Karim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Precision Time Protocol (PTP) provides the time and phase synchronization required by disaggregated Open Radio Access Networks (O-RAN). Yet, in current open fronthaul deployments, PTP traffic lacks mandatory authentication and integrity protection, leaving synchronization vulnerable to spoofing, replay, and delay manipulation attacks that can degrade radio access performance. Existing protections are poorly suited to this setting: they either add excessive latency, do not support multicast dissemination efficiently, or fail to contain key exposure under partially trusted RUs. This paper analyzes the security risks of unprotected O-RAN PTP and develops a threat model for open fronthaul deployments. We then introduce PRTESLA-C, a lightweight synchronization protection mechanism that combines per-round delayed key disclosure with ASCON-based message authentication. PRTESLA-C uses an apply-then-verify-and-correct paradigm: timing samples are applied immediately to preserve real-time control, verified after key disclosure, and removed from persistent synchronization state if authentication fails. This design maintains sub-microsecond synchronization accuracy, provides strong protection against spoofing and replay, and bounds the impact of delay manipulation with minimal computational and latency overhead.

---


### 76. [Cross-Dialect NER for Bangla Regional Dialects Using Leave-One-Dialect-Out Cross-Validation and Explainable AI](https://arxiv.org/abs/2609.22536)

**<font color=#1a73e8>作者：</font>** Shamim Rahim Refat, Faika Fairuj Preotee, Shuvashis Sarker 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bangla, the seventh most spoken language in the world, exhibits significant regional dialectal diversity, with dialects such as Barishal, Chattogram, Sylhet, Noakhali, and Mymensingh differing in lexical, morphological, and syntactic characteristics. These variations pose substantial challenges for Named Entity Recognition (NER), limiting the generalization of models trained on Standard Bangla or a single regional dialect. This paper presents a cross-dialect Bangla NER framework using the publicly available ANCHOLIK-NER dataset, comprising 17,405 annotated sentences and 101,817 tokens across five major Bangla regional dialects. A Leave-One-Dialect-Out Cross-Validation (LODOCV) strategy is adopted, training models on four dialects and evaluating on the remaining unseen dialect. Eight pretrained transformer-based models, including BanglaBERT, MuRIL, XLM-RoBERTa, and Multilingual-E5, are evaluated under identical experimental settings. Multilingual-E5 Large achieves the highest F1-score in every fold, peaking at 97.26% on Mymensingh and reaching its lowest, 82.38%, on Chattogram, the most challenging target dialect. To improve interpretability, Local Interpretable Model-agnostic Explanations (LIME) are applied to word-level predictions, revealing that the model's decisions are driven primarily by the surface form of the target entity word itself rather than by surrounding sentence context. These findings establish a benchmark for cross-dialect Bangla NER and demonstrate the effectiveness of transformer-based transfer learning for low-resource regional dialects, while highlighting the surface-form dependence of current models as a direction for future work.

---


### 77. [AdaMerge: Tuning-Free Patch Compression for Multi-Vector Visual Document Retrieval](https://arxiv.org/abs/2609.22562)

**<font color=#1a73e8>作者：</font>** Jianxin You, Kun Ni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-vector visual document retrieval (VDR) models such as ColPali and ColNomic achieve strong accuracy by representing each document with hundreds to thousands of patch-level embeddings, at substantial storage and latency cost. Existing compression methods either prune unimportant patches or merge similar ones into clusters; the recent state-of-the-art merging method Prune-then-Merge (PtM) consistently outperforms pruning-only baselines at high compression, but requires a per-dataset cluster budget m to be tuned by grid search. We observe that the merge-cosine sequence produced by hierarchical clustering exhibits a sharp cliff separating mergeable redundancy from salient signal, and that the location of this cliff is concentrated in a narrow band across more than 11,000 documents from 14 datasets. This suggests the merge boundary can be detected per document rather than tuned per dataset. Building on this observation, we propose AdaMerge, a plug-and-play compression method that (i) detects each document's own cliff via gap analysis on the merge-cosine trajectory, and (ii) builds attention-weighted cluster centroids to preserve salient signal. On the long-document benchmark ViDoRe-V2 (4 datasets, two backbones), AdaMerge significantly outperforms tuned PtM across the operating range (p < 10^-4); on the short-document benchmark ViDoRe-V1 (10 datasets, two backbones), where all merging methods are already near-lossless, AdaMerge matches tuned PtM without any per-dataset tuning. AdaMerge adds only about 10 ms per document and exposes a single global hyperparameter shared across all datasets and backbones.

---


### 78. [Benchmarking Hybrid Deep Learning Architectures for Predictive Maintenance in Industry 4.0](https://arxiv.org/abs/2609.22583)

**<font color=#1a73e8>作者：</font>** Zhengyang, Joseph E. Hernandez, Thomas Cook 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive maintenance in Industry 4.0 refers to using data from sensors, machines, and production systems to estimate when equipment is likely to fail, so maintenance can be planned before a breakdown occurs [1]. However, a model that predicts maintenance may work perfectly in the lab but fail unexpectedly when applied to real factory data [2]. To solve this "reliability" gap, we evaluated six deep learning architectures across more than 700 experimental runs. We focused on the two dominant approaches in the field: Recurrent Neural Networks (RNNs), which process data step-by-step, like reading a sentence [3], and Transformers, a recent dominant approach, which look at the entire sequence at once to spot important connections [4]. We examined whether Transformers still outperform recurrent neural networks (RNNs) when the data includes noise [5]. We found that while Transformers excelled at tracking stable, slow-moving processes, they tend to overreact to chaotic data, mistakenly taking sensor noise for meaningful signals [6]. We also found that the hybrid method that combines a Long Short-Term Memory (LSTM) layer with a Transformer layer is more resilient to noisy data from factory shops [7]. Functioning as a noise filter, the LSTM smooths out data volatility, allowing the Transformer to focus on the bigger picture without being distracted [8]. The hybrid model did not just improve accuracy; it proved to be significantly more consistent than complex models, delivering reliable predictions regardless of how chaotic the underlying system became.

---


### 79. [Augmenting PID Control with Deep Reinforcement Learning: A Hybrid Approach to the Industrial Benchmark](https://arxiv.org/abs/2609.22584)

**<font color=#1a73e8>作者：</font>** Zhengyang, Joseph E. Hernandez, John Burtenshaw 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As industrial processes grow in complexity, traditional Proportional-Integral-Derivative (PID) controllers are often insufficient for handling their non-linear, multi-input dynamics. We propose using advanced Deep Reinforcement Learning (DRL) to prove its advantages in these complex environments. To do this, we rely on the Industrial Benchmark (IB). The IB is a realistic simulation that tests DRL algorithms against the key challenges of industrial applications: high-dimensional state spaces, delayed effects, and conflicting multi-criterial objectives. This testbed highlights DRL's core trade-off: while its final policies can often be unstable, its unique strength is the ability to autonomously discover optimal, non-obvious policies in multi-dimensional spaces where simple controllers fail. In this paper, we propose a novel hybrid PID-RL controller that leverages DRL's discovery capability while ensuring Reliability. After developing a multi-objective reward function to make DRL viable, we use a twin-delayed deep deterministic (TD3) agent as a discovery tool to find the optimal, non-obvious settings for the IB's 'Gain' and 'Shift' parameters. By feeding these discovered parameters to a simple, tuned PID controller, our hybrid model successfully combines all three characteristics: it achieves the optimal Performance and Efficiency of the best DRL agent with the Reliability of a classical controller. This work demonstrates a practical methodology for using DRL to augment, rather than replace, trusted industrial control systems.

---


### 80. [TWIG: A Time-Causal Wavelet Operator for Autoregressive Forecasting on Irregular Graphs](https://arxiv.org/abs/2609.22585)

**<font color=#1a73e8>作者：</font>** Subashree Venkatasubramanian, David A. Barajas-Solano, Chuyang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce TWIG (Time-Causal Wavelet Operator for Irregular Graphs), a graph-native neural operator for autoregressive surrogate modeling on static irregular graphs. TWIG transforms each node history into causal multiscale temporal features that separate recent variation from progressively slower memory components, then propagates these features through graph-wavelet operator blocks with gated pointwise channel mixing. The architecture is causal by construction and designed for closed-loop forecasting, where predictions are recursively reused as future inputs. We evaluate TWIG on three irregular-domain forecasting problems spanning regional diffusion, three-dimensional subsurface hydrology, and aerodynamic flow, with graphs ranging from 400 to 5,233 nodes and model capacities from approximately 70k to 10M parameters. TWIG achieves the lowest aggregate rollout errors on the subsurface-hydrology and regional-diffusion benchmarks and ranks second on the 10M-parameter aerodynamic-flow benchmark, behind the GPS Transformer. Across all three settings, TWIG consistently outperforms the corresponding non-time-causal Graph WNO baseline. These results demonstrate that TWIG provides an effective and scalable approach to stable autoregressive forecasting of dynamical fields on irregular graphs.

---


### 81. [User-Level Handover Decision Making Based on Machine Learning Approaches](https://arxiv.org/abs/2609.22593)

**<font color=#1a73e8>作者：</font>** João Lima, Alvaro Medeiros, Eduardo Aguiar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This letter covers a broad comparison of methods for classification and regression applications for a user-level handover decision making in scenarios with adverse propagation conditions involving buildings, coverage holes, and shadowing effects. The simulation campaigns are based on network simulator ns-3. The comparison encompasses classical machine learning approaches, such as KNN, SVM, and neural networks, but also state-of-the-art fuzzy logic systems and latter boosting machines. The results indicate that SVM and MLP are the most suitable for the classification of the best handover target, although fuzzy system SOFL can perform similarly with lower processing time. Additionally, for the download time estimation, LightGBM provides the smallest error with short processing time, even in hard propagation scenarios.

---


### 82. [Concurrency-Aware Process Model Forecasting with Causal Nets](https://arxiv.org/abs/2609.22614)

**<font color=#1a73e8>作者：</font>** Yongbo Yu, Jari Peeperkorn, Johannes De Smedt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process model forecasting (PMF) aims to predict the process model that will characterize a future period, thereby providing a process-level view of how behavior is expected to evolve. Existing PMF methods, however, forecast directly-follows graphs, which cannot explicitly represent concurrency. We extend PMF to causal nets by forecasting time series of relation and binding counts and using these forecasts to reconstruct future process models with AND/XOR semantics. To evaluate the resulting models, we introduce a protocol that accounts for partial traces and constructs the workflow nets required for conformance checking. Experiments on four event logs show that the forecasted models achieve conformance levels close to those of models re-mined from observations in the corresponding future windows. They also outperform static discovery baselines, which retain high precision on the structurally stable log but exhibit substantial precision losses on the other three logs. Filtering infrequent bindings improves most conformance metrics, although it also removes much of the concurrent behavior captured by the models.

---


### 83. [GaitVista: Reliability-Aware AI Measurement toward Accessible Longitudinal Gait Assessment](https://arxiv.org/abs/2609.22619)

**<font color=#1a73e8>作者：</font>** Nethmi Jayasinghe, Mihir Parashar, Amit Ranjan Trivedi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tracking recovery of walking function requires detecting meaningful gait change across rehabilitation sessions, yet objective 3D measurement remains confined to specialized motion-capture laboratories. Small camera sets and body-worn inertial sensors broaden access, but reliability varies across joints and time, allowing sensing failures to masquerade as patient change. We present \textsc{GaitVista}, a reliability-aware measurement layer whose lightweight gate assigns joint- and frame-specific visual contributions using camera coverage, local visual quality, cross-modal disagreement, and root-motion continuity, and exposes them for inspection. Across seven clean and degraded sensing conditions on TotalCapture, \textsc{GaitVista} reduces average full-body and lower-body error by \textbf{27.7\%} and \textbf{27.8\%}, attains the lowest worst-condition error among fusion methods, and reduces the gap to a joint-frame oracle from $2.76$--$5.33$~cm for condition-blind baselines to $1.11$~cm. On MoVi with image-derived keypoints, it is the only deployable fusion method to improve over both unimodal streams, reducing marker-supported error by \textbf{6.4\%} relative to the strongest learned fusion baseline. On TotalCapture, it improves bilateral knee-flexion waveform accuracy by \textbf{18.9\%}. Raw inertial measurements from five TotalCapture participants show location- and time-varying magnetic disturbance, supporting the design's reliability premise. Both benchmarks contain neurologically healthy participants in controlled settings and retain participant-specific IMU calibration; we therefore report progress toward accessible gait assessment, not validated clinical deployment.

---


### 84. [Text, Pixels, or Both? Evaluating Input Representations for Multimodal Document QA](https://arxiv.org/abs/2609.22628)

**<font color=#1a73e8>作者：</font>** Nikhil Reddy Pottanigari, Sepideh Kharaghani, Saverio Vadacchino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every document QA system begins with a choice that is rarely studied on its own: whether to feed the model page images, extracted text, or both. We isolate this choice, holding the prompt, judge, and scoring pipeline fixed, across four commercial model endpoints, two corpora, and two context regimes (gold evidence pages and the full document). On documents that fit the image budget, page images lead on accuracy at every document length on both corpora, but this advantage carries a growing latency and cost premium: text latency stays roughly flat as documents lengthen while image latency rises steadily. Text and images also fail on different questions, with exactly one representation correct on 19--25% of items across the reported cells, so neither subsumes the other. Exploiting this complementarity, a lightweight TF-IDF router that reads only the question text gains 2.6 points over always-text while cutting median latency 30% relative to always-vision, on a document-disjoint held-out split.

---


### 85. [X-Beat: An Explainable Framework for ECG Image Classification](https://arxiv.org/abs/2609.22631)

**<font color=#1a73e8>作者：</font>** Mohammad Sadman Tahsin, Haitham Y. Adarbah, Afzel Noore  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate automated interpretation of electrocardio- grams (ECGs) is essential for early detection of cardiac condi- tions such as myocardial infarction and rhythm abnormalities. However, many high-performing deep learning models remain difficult to deploy in clinical settings due to limited transparency and lack of reliability validation. In this work, we present X- Beat, an explainable and reliability-aware benchmark framework for ECG image classification designed to support trustworthy AI systems in healthcare. The proposed framework combines transfer learning with post-hoc explainability and systematic reliability evaluation across four cardiac classes: Abnormal Heartbeat, History of Myocardial Infarction, Myocardial In- farction, and Normal Heartbeat. Multiple ImageNet-pretrained CNN backbones, including EfficientNet-B0, ResNet-50, DenseNet- 121, and MobileNetV3-Large, are evaluated under a unified training protocol. Beyond standard performance metrics, we incorporate Grad-CAM-based visual explanations together with additional analyses, including explanation stability, regional sen- sitivity, and confidence-based reliability assessment, to examine whether model predictions are supported by clinically meaningful evidence. Experimental results show that ResNet-50 achieves the best performance, reaching 91.94% accuracy and a macro F1- score of 0.9098, with strong class separability (AUC up to 0.995). Explanation analyses indicate that the model primarily focuses on waveform-relevant regions, while reliability evaluation suggests that most incorrect predictions occur with lower confidence. Overall, this work provides a structured and reproducible bench- mark for evaluating both predictive performance and explanation reliability in ECG image classification, contributing toward the development of trustworthy and interpretable AI components for clinical decision support systems.

---


### 86. [Classification with Abstention Under Class-Conditional Error Constraints](https://arxiv.org/abs/2609.22632)

**<font color=#1a73e8>作者：</font>** Mohammadreza M. Kalan, Yuyang Deng, Sanaz Hamidi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study binary classification with abstention under separate class-conditional error constraints, with the objective of minimizing abstention while keeping both errors below prescribed thresholds. We characterize the distribution-free minimax rate of excess abstention risk, up to logarithmic factors, in terms of the complexity of the hypothesis class and the sample size. To make the framework amenable to computation with models such as neural networks, we introduce surrogate-loss formulations and derive finite-sample guarantees for excess surrogate ambiguity risk. We formulate the resulting learning task as a constrained optimization problem and characterize its computational complexity in the convex setting. Finally, we evaluate our approach on various datasets and compare its performance with a competing method for this problem.

---


### 87. [ConsistWorld: Evidence Routing for Consistent Multi-Agent World Models](https://arxiv.org/abs/2609.22641)

**<font color=#1a73e8>作者：</font>** Qianxun Xu, Xianfang Zeng, Xinyao Liao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video world models enable temporally coherent generation for a single observer. Extending them to multiple agents requires consistency across independently controlled views and temporal gaps under causal streaming. We present ConsistWorld, a multi-agent world model that generates camera-controlled video streams of a static scene from one shared image. We formulate consistency as routing evidence from committed multi-agent history and concurrently generated peer views to the tokens being generated. Pose Conditioned Memory Retrieval selects relevant historical observations from all agents, recovering evidence beyond the recent context window. Visibility-Gated Peer Sharing regulates current peer information according to estimated historical coverage and current-view overlap. Together, they determine which historical observations enter the context and where concurrent peer information contributes, supporting long-term recall and coordinated exploration. Both mechanisms use camera geometry and maintain a bounded active context for a fixed agent count and retrieval budget. Experiments on evidence sharing cases and video length and agent number generalizations show that ConsistWorld achieves a strong cross-time and cross-agent consistency while preserving competitive generation quality.

---


### 88. [Monotone-Constrained Diffusion Models for Long-Horizon Production Forecasting](https://arxiv.org/abs/2609.22643)

**<font color=#1a73e8>作者：</font>** Temesgen Mikael Abraha, Yves Lucet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting a long horizon from only the first observations of a sequence is ill-posed: many trajectories are consistent with the same short history. We study this problem in oil and gas production forecasting, where forecasts made after roughly the first fifth of a well's producing life drive development and abandonment decisions, and where a usable forecast must describe a monotone decline. We present Physics-SIMS-TS, a conditional diffusion forecaster that combines negative guidance against synthetic artifacts, decline-curve constraints and an isotonic projection applied during sampling, spatial training augmentation, and an ensembled stochastic sampler yielding a full predictive distribution. Across three jurisdictions and more than 35,000 wells, under a shared-space, validation-frozen protocol, Physics-SIMS-TS is the most accurate diffusion forecaster in the comparison and is competitive with, but not superior to, ensembled transformer forecasters. Its forecasts are monotone by construction at a cost of at most 0.5% in mean squared error, and its trajectory ensemble yields calibrated intervals after one dispersion factor is fitted per jurisdiction. On six standard benchmarks a reversible-instance-normalization variant of the backbone is the leading diffusion baseline. We also quantify four protocol choices on which the measured ranking depends. Code and evaluation artifacts are released.

---


### 89. [Self-Organizing Agent Teams Learn to Reason Together](https://arxiv.org/abs/2609.22682)

**<font color=#1a73e8>作者：</font>** Aneesh Pappu, Mirac Suzgun, Yongchan Kwon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collective intelligence depends not only on what team members know, but also on how they organize their work. When the structure of a solution is unknown, useful roles and divisions of labor cannot be specified in advance; teams must learn from experience how to organize reasoning as it unfolds. Human teams routinely adapt this way, while existing AI agent teams rely on fixed protocols, explicit task decomposition, or routing. We introduce Self-Organizing Agent Teams (SAT), fixed teams of AI agents that learn reusable strategies from prior collaborations to organize roles, conversational phases, participation, and information flow. These strategies enable what we call collaborative computation: agents exchange, challenge, repair, and synthesize partial reasoning into solutions no member produced independently. In two independent settings, we learn teamwork strategies that transfer unchanged to unseen benchmarks, using only 15 mathematics and 25 graduate-level knowledge problems. Across five mathematics and physics benchmarks, self-organizing teams average 66.7% accuracy, versus 48.8% for their strongest member, 58.7% for compute-matched inference by that agent, and 59.0% for a perfect router over members' independent answers; on AIME 2026, they exceed this router by 13.4 points. Because gains vary across benchmarks, we ask when self-organizing collaboration helps. Across eight benchmarks, demonstrability (the organizational-psychology construct of whether a team can distinguish correct from incorrect reasoning) strongly tracks improvement over the strongest member (Spearman $\rho=0.90$, $p=0.005$): teams benefit most when correct reasoning can be recognized once it appears. More broadly, these results suggest that organization itself can become an agent capability: agent teams can learn how to reason together and produce solutions their members could not reach independently.

---


### 90. [PanoSeg3R: Feed-Forward 3D Semantic Segmentation for Panoramic Images with an Automatic Data Curation Pipeline](https://arxiv.org/abs/2609.22687)

**<font color=#1a73e8>作者：</font>** Heechan Yoon, Dongki Jung, Phuc Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PanoSeg3R, a feed-forward framework for 3D panoramic semantic segmentation. Unlike existing methods designed for perspective inputs, PanoSeg3R jointly predicts 3D geometry and multi-view semantic segmentation in one single forward pass. Built upon a pretrained reconstruction backbone that supports panoramic images, our approach extends feed-forward 3D reconstruction with a query-based mask decoder. Furthermore, we introduce an automatic panorama data curation pipeline that leverages the complementary strengths of off-the-shelf foundation models to generate reliable pseudo semantic annotations, substantially expanding the training data and improving zero-shot generalization. PanoSeg3R achieves state-of-the-art performance on panoramic 3D semantic segmentation, improving 3D mIoU by up to 16.02 on ScanNet++, while the curated training data further improves zero-shot performance by up to 4.26 and 43.28 mIoU on Stanford2D3D and ToF-360, respectively. Website: this https URL

---


### 91. [Vision2CAD: A Visual Agent Harness for Explicit Geometry Referencing and Localization in Parametric CAD Modeling](https://arxiv.org/abs/2609.22688)

**<font color=#1a73e8>作者：</font>** Xi Cheng, Chenxi Zhai, Hang Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating parametric CAD models requires accurate geometry and stable feature dependencies. Existing methods face challenges in selecting geometric references, interpreting sketch-plane local coordinates, and establishing sketch constraints to projected external geometry. We present Vision2CAD, a visual agent harness that combines vision-language model (VLM) reasoning with deterministic CAD kernel operations. An ID-based interface supports explicit geometry selection, a local-coordinate bridge converts view coordinates into sketch coordinates, and projected-edge localization supports external sketch constraints. These mechanisms establish feature dependencies within the supported modeling operations and constraint types. We also introduce the Geometry Explicit Reference Dataset (GERD), which aligned commands, geometry states and IDs at every modeling step. On GERD-EVL and a DeepCAD test subset, Vision2CAD improves mIoU by 11.1\% and 5.6\% and reduces Chamfer distance by 17.3\% and 41.8\%, respectively. Parameter-editing experiments and ablation studies further proved the preservation of parametric dependencies.

---


### 92. [Multi-Armed Bernoulli Bandits via Minimax Single-Arm Stopping](https://arxiv.org/abs/2609.22690)

**<font color=#1a73e8>作者：</font>** Huikang Liu, Zhengchao Wang, Daniel Kuhn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop an index policy for finite-horizon Bernoulli multi-armed bandits from minimax solutions to single-arm bandit (SAB) problems. Each SAB problem involves choosing between an unknown Bernoulli arm and a known reward. We show that minimizing worst-case regret of SAB problems over all non-anticipative policies admits an exact semi-infinite linear programming formulation. The resulting stopping policies offer a natural way to compare arms: the higher the known reward against which a policy continues sampling, the more promising the unknown arm. We turn this intuition into indices based on cumulative continuation probabilities, with a monotone adjustment and a reward-shortfall cap. By relating index errors to the regret of single-arm stopping policies, we establish a distribution-free regret bound of $4.45\sqrt{KT}+10.75K$ for $K$ arms and horizon $T$. This bound matches the minimax-optimal regret order established in the literature. The guarantee extends to rewards supported on $[0,1]$ through Bernoulli randomization. We also provide a finite-grid implementation with quantified approximation loss. In numerical experiments, the SAB-based index policy achieves lower worst-case regret than every tested benchmark policy across all evaluated numbers of arms and horizons, while closely matching the grid-based MAB minimax policy in the two-arm setting.

---


### 93. [Generative Embodied Multiple Behavior Control Systems for Human-like Agents](https://arxiv.org/abs/2609.22691)

**<font color=#1a73e8>作者：</font>** Chongyu Bao, Haokai Yang, Yuhan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An enduring and richly elaborated dichotomy in cognitive neuroscience is that of human behavior control mechanisms, divided into habitual versus goal-directed. While existing human-like agent frameworks primarily focus on modeling goal- directed behavior, habitual behavior has been largely overlooked, though it plays a crucial role in human daily life. In this paper, we address this gap by studying multiple behavior control systems that jointly model goal-directed and habitual behaviors. We propose a human behavior control mechanism-inspired framework which the Habitual Controller retrieves cue-triggered behaviors from personal- ized habit memory, while the Goal-directed Controller employs a context-aware world model to predict action consequences and estimate their values. The Arbiter dynamically balances the influence of both systems according to individual differ- ences and momentary internal states. To reconstruct diverse human-level behavior instructions in 3D environments, we further develop a keyframe-guided 3D mo- tion generation module. Through extensive evaluation methods, human studies, and ablations studies, experimental results demonstrate that human-likeness per- formance is significantly improved by our approach. The efficacy of our approach indicates the benefits of leveraging habitual behavior and multiple behavior con- trol system coordination for believable embodied human-like agents.

---


### 94. [A Survey on the Linear Representation Hypothesis](https://arxiv.org/abs/2609.22695)

**<font color=#1a73e8>作者：</font>** Sewoong Lee, Marc E. Canby, Ikhyun Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The term "linear representation hypothesis" (LRH) has appeared across diverse subfields of artificial intelligence, neuroscience, and cognitive science. But previous works have not consistently treated the LRH as a falsifiable scientific hypothesis; we analyze these inconsistencies and examine their implications for how prior theoretical and methodological results should be interpreted. Based on this analysis, we argue that claims regarding linear representations become well-defined only through careful examination of the model, representation location, feature definition, and evaluation dataset. We therefore propose a more rigorous formalization of the LRH that makes these dependencies explicit and allows the hypothesis to be evaluated as a falsifiable scientific claim. Finally, we identify some non-trivial open problems that warrant further attention from the research community.

---


### 95. [Autonomous Model Lifecycle Management for Digital Twin-Based Manufacturing Control](https://arxiv.org/abs/2609.22701)

**<font color=#1a73e8>作者：</font>** Zhengyang, Thomas Cook, Fredaljohn Rohrbaugh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Manufacturing AI systems must autonomously adapt to continuous distributional shift from raw-material variability, ambient changes, and equipment aging, under strict safeguard and operator-trust requirements where model failures risk physical damage. This paper presents a closed-loop Cyber-Physical System (CPS) for autonomous model lifecycle management in automotive manufacturing, deployed since 2023. The system manages product-specialized model pairs: a sequence-to-sequence physics model (LPP) serving as a digital twin, and a deep Reinforcement Learning (RL) control policy (LCP) trained against it. Per retraining cycle, multiple model variants spanning architecture families and RL algorithms compete; only the best-scoring candidate advances. A Conductor orchestrator autonomously manages plant-wide model inventories with dependency-aware retraining and Proportional-Integral-Derivative (PID) fallback. Reflecting the principle of Human-Centric Intelligence, the LCP composite score embeds an operator-trust gate penalizing policies deviating from established practice; without it, 23% of policies are rejected by operators despite passing accuracy thresholds. Across multiple facilities, LCP-controlled processes achieve process stability improvements of 28-45% over uncontrolled baselines with zero safety incidents.

---


### 96. [Hapi: A Multivariable Land-Surface Transformer for Medium-Range Hydrological Forecasting at Continental Scale](https://arxiv.org/abs/2609.22702)

**<font color=#1a73e8>作者：</font>** Hong Zhang, John K. Hutchison, Rao Kotamarthi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate flood forecasts several days in advance are essential for flood control, water-resource management, and emergency response. Producing them at high resolution over a continental domain calls for local hydrological detail together with spatial context extending from river basins to synoptic weather systems. We developed Hapi, a U-Net Swin Transformer that uses fine three-dimensional patches and hierarchical shifted-window attention to forecast discharge, surface runoff, snow water equivalent, and soil wetness across the contiguous United States. The model produces 24--72-hour forecasts at $0.05^{\circ}$ resolution, with learned Laplacian task weights adjusting each variable's contribution to training. On 2024 test data using reconstructed weather and land-surface inputs from ERA5-Land, Hapi outperformed an operational physics-based model and a state-of-the-art AI model in flood detection. Independent validation against 3,881 U.S. Geological Survey gauges and a Hurricane Helene case study supported its advantage over the physics-based model in reproducing daily discharge. Controlled experiments showed that learned task weighting strengthens rare-flood detection, which is particularly sensitive to changes in precipitation inputs. Hapi produced a four-variable, 72-hour forecast across the contiguous United States with an average inference time of 0.11 seconds on a single A100 GPU.

---


### 97. [DOA-SORT: Directional Occlusion-Aware Multi-Object Tracking with Distributional Observations](https://arxiv.org/abs/2609.22706)

**<font color=#1a73e8>作者：</font>** Hao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity association in multi-object tracking (MOT) is vulnerable to partial occlusion, truncated detections, and fluctuating confidence scores. Existing motion-dominant trackers commonly represent occlusion as a scalar penalty. This treatment misses the directional observation bias caused by occlusion: left, right, top, and bottom occlusions distort the location and shape of a detection in different ways. We propose \ours{} (Directional Occlusion-Aware SORT), an online and training-free tracker that models these biases explicitly. First, it infers a soft front--back ordering from box overlap and relative bottom positions, and estimates directional occlusion coverage and depth. It then constructs a mixture of one clean and four directional occlusion observation components. The model uses a five-dimensional observation comprising box center, area, confidence, and aspect ratio, and adapts observation noise to predicted occlusion and detection confidence. The directional mixture likelihood is used in high-confidence association, low-confidence association, and track recovery; ambiguity penalties and local order-consistency swaps further reduce identity errors among nearby objects. On the DanceTrack validation split, \ours{} improves HOTA from 63.00 to 66.34, AssA from 45.10 to 49.57, and IDF1 from 62.19 to 65.28 over OA-SORT with the same detector and evaluation protocol. The gains are concentrated in association quality while detection accuracy remains stable. Additional local evaluations on MOT17 and MOT20 train splits characterize cross-dataset behavior under the same no-ReID tracking protocol.

---


### 98. [Explanation Navigator: Rectifying Out-of-Scope Human Interpretations of Leaky AI Explanations through Conversational Guidance](https://arxiv.org/abs/2609.22707)

**<font color=#1a73e8>作者：</font>** Yueqing Xuan, Kacper Sokol, Danula Hettiachchi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As explanations of artificial intelligence systems proliferate, their recipients must grasp not only what they convey but also recognise what they cannot. We conducted an interview study with nine participants to examine how explainees reason when their information needs exceed the scope of available explanations. Participants often unwittingly confabulated explanatory insights when relevant information was missing from the explanations, not recognising the inherent limitations thereof. We characterise such explanations as leaky explanations -- simplifications that strive to hide complexity yet whose correct interpretation hinges on understanding of the concealed details. To address out-of-scope interpretations we propose Explanation Navigator: a conversational interaction framework that detects mismatches between users' information needs and explanations' content, elucidating pertinent yet implicit details and providing complementary explanations for unmet information needs. An online study with 316 participants showed that our approach allowed explainees to recognise and rectify confabulated explanatory insights, guiding them towards developing correct understanding.

---


### 99. [UBA-ORL: Unlearning-Activated Backdoor Attacks on Offline Reinforcement Learning](https://arxiv.org/abs/2609.22711)

**<font color=#1a73e8>作者：</font>** Fengyi Wang, Cong Li, Lulu Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (offline RL) enables policy learning from pre-collected static datasets without online exploration, and is increasingly deployed not only in safety-critical domains such as autonomous driving and robotic control but also in data-mining applications such as recommendation and behavior analysis. While compliance-driven data removal enhances privacy, it also opens a previously unrecognized attack surface. We introduce UBA-ORL (Unlearning-activated Backdoor Attack on Offline Reinforcement Learning), the first unlearning-activated backdoor attack for offline RL: in the evaluated settings, the attack is substantially suppressed after normal training and becomes pronounced after a compliance-driven deletion (unlearning) request. UBA-ORL employs a dual-sample mechanism: alongside backdoor trajectories (BD) that link a trigger to malicious actions under inflated rewards, the attacker injects camouflage trajectories (CM) sharing the same trigger pattern but preserving benign actions with equally high rewards. During training, BD and CM provide competing supervisory signals; upon a legitimate deletion request on the CM subset, the residual BD signal can re-dominate, reactivating the backdoor on demand. Empirical results show that UBA-ORL achieves controllable activation under the evaluated offline-RL configurations, while no-trigger return changes vary by configuration, exposing a previously overlooked security risk in compliance-driven offline RL platforms. We urge the community to develop joint pre-/post-unlearning auditing mechanisms for compliant unlearning services.

---


### 100. [ZIL: Zero-shot Image-to-LiDAR Registration](https://arxiv.org/abs/2609.22716)

**<font color=#1a73e8>作者：</font>** Zijun Li, Xiaotian Sun, Xuelun Shen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-LiDAR registration estimates the camera pose of an image with respect to a LiDAR point cloud. It has diverse applications in autonomous driving, robot navigation etc. However, state-of-the-art (SOTA) methods still 1) mostly assume same-frame inputs, struggling with the image and point cloud from distant frames; 2) rely on domain-specific training, failing to generalize to unseen scenarios. We propose ZIL, the first foundation model for zero-shot non-synchronized image-to-LiDAR registration. ZIL encodes the input image and point cloud with the Vision and Point Transformers. In addition to regressing the relative pose, ZIL also learns to predict 3D coordinates, which substantially improves the pose accuracy without additional annotations. Interestingly, naive mix-data training cannot enable zero-shot generalization, which requires normalization on both camera intrinsics and the LiDAR vertical-axis origin. Trained on 7 public datasets with 1.4M LiDAR frames, ZIL consistently and significantly outperforms previous SOTA with a single model across 5 in-domain and zero-shot benchmarks, reducing the translation and rotation errors by up to 87% and 76% (shown in Fig. 1). Code and models are available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
