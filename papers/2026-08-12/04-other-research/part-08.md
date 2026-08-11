# 📦 其他研究 | 2026年08月12日

> 本类共 **445** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-445](./part-09.md)

---

### 351. [Universal or Language-Family-Specific Script Unification for Cross-Lingual Transfer? A Case Study on Turkic Languages](https://arxiv.org/abs/2608.09356)

**<font color=#1a73e8>作者：</font>** Zijie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Closely related languages written in different scripts expose little surface overlap to multilingual models, limiting cross-lingual transfer. We compare two approaches to script unification: the general-purpose uroman romanizer and the family-specific Common Turkic Script (CTS). We train matched fastText models on transliterated Wikipedia corpora from 11 Turkic languages and evaluate them on WikiANN named entity recognition and Universal Dependencies part-of-speech tagging. CTS and uroman show no significant difference on NER, while both substantially outperform the official monolingual fastText baselines. POS results reveal no universal winner: language-specific differences are associated with the cross-lingual character n-gram coverage induced by each representation, while within-language coverage becomes more important when target-language supervision is available. Although CANINE-c achieves higher overall POS averages, the substantially simpler fastText-based systems remain competitive on several treebanks. Overall, the effectiveness of script unification depends on the language, the induced subword overlap, and the available supervision.

---


### 352. [ControlRadio: Prompt-Driven Controllable Diffusion for Cross-Modal Radio Map Generation](https://arxiv.org/abs/2608.09357)

**<font color=#1a73e8>作者：</font>** Kangjun Liu, Xiying Pan, Shuhang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radio maps describe how wireless signals propagate across space and are essential for wireless communication, sensing, and network planning. However, constructing accurate radio maps traditionally requires either dense measurements or computationally expensive physical simulations, which limits scalability and real-time deployment. Recent advances in generative artificial intelligence offer a promising alternative, but existing approaches lack fine-grained control and physical consistency when applied to real-world wireless environments. Here we present \textbf{ControlRadio}, a controllable generative framework that produces radio maps from natural-language descriptions and environmental layouts, including building structures and transmitter locations. Joint semantic and spatial conditioning enables interpretable, propagation-plausible generation, while a controlled latent prior and layout-aware conditioning improve stability and structural consistency. Extensive experiments demonstrate that ControlRadio achieves state-of-the-art accuracy and strong generalization across diverse urban scenarios, while reducing computation time by more than four orders of magnitude compared with conventional simulation-based methods. Such results suggest a new paradigm for scalable and controllable wireless environment modeling, with broad implications for next-generation communication systems and data-driven radio sensing.

---


### 353. [Deep Learning based Detection of Fishing Vessels and Fishing Monitoring using Nightlight Images](https://arxiv.org/abs/2608.09360)

**<font color=#1a73e8>作者：</font>** Shantakar Mohanty, Prasun Kumar Gupta, Raian Vargas Maretto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The demand for maritime surveillance has given rise to the need for monitoring fishing vessel activities, particularly in addressing the challenge of "dark vessels" that operate without Automatic Identification System (AIS) transmission. This study presents a novel approach for detecting small-scale fishing vessels using nighttime light (NTL) imagery from the SDGSAT-1 satellite, combined with deep learning techniques to enhance fishing monitoring awareness along the western coast of India. A dual-branch YOLO11 architecture was developed to exploit both the 10-meter panchromatic and 40-meter RGB imagery from SDGSAT-1. The custom model architecture was specifically optimized for small object detection in NTL imagery, featuring parallel convolutional backbones that process both modalities before concatenation for enhanced feature extraction. The dual-branch YOLO11 model demonstrated optimal performance with a precision of 0.99, recall of 0.93, F1-score of 0.96, and mAP@50 of 0.96, significantly outperforming single-branch implementations of YOLOv5s, YOLOv8s, and standard YOLO11s architectures. When applied to the western coast of India, the model detected 31525 vessel instances across the temporal dataset spanning 2022-23. Cross-matching analysis with AIS data revealed that only 7146 (22.7%) of detected vessels had corresponding AIS transmissions, while 24379 (77.3%) were identified as potential dark vessels. Spatio-temporal analysis showed peak fishing activity during January-April, with a primary activity corridor parallel to the coastline within 50-100 km, corresponding to productive continental shelf areas. This research contributes to maritime surveillance capabilities by highlighting the effectiveness of nighttime lights satellite imagery for fishing vessel detection and provides valuable insights into fishing patterns and potential regulatory compliance issues in Indian waters.

---


### 354. [Beyond Binary: Continuous State Optimization with Graph-Structured Objectives](https://arxiv.org/abs/2608.09366)

**<font color=#1a73e8>作者：</font>** Corinna Cortes, Yishay Mansour, Mehryar Mohri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale learning systems often face the challenge of balancing multiple,
potentially competing objectives, such as fairness, accuracy, and
latency. While recent work has formalized this as an optimization problem over
binary states, many real-world control parameters, such as fairness
thresholds, diversity mixing rates, or resource budgets, are continuous. In
this work, we extend the framework to \emph{continuous state spaces}. We model
the problem as minimizing a sum of linear objectives subject to \emph{movement
costs} that penalize system instability. We capture the local structure of
the objectives using a \emph{dependency graph} (or factor graph), where each
objective is determined by a subset of the state attributes. To address the
tension between exploration and stability, we propose \emph{Lazy
Graph-LinUCB}, an algorithm that performs lazy updates to minimize switching
costs while maintaining near-optimal regret. Beyond stability, we introduce
three advanced mechanisms to exploit the underlying graph structure: (1) an
\emph{asynchronous} update schedule that eliminates synchronization overhead
in sparse graphs; (2) an \emph{adaptive} algorithm that learns the graph
structure from data; and (3) a \emph{joint estimator} that leverages data
sharing among correlated objectives to significantly tighten regret
bounds. Empirically, we demonstrate that these structural exploitations reduce
movement costs by more than a factor of three in heterogeneous systems while
maintaining similar cumulative losses.

---


### 355. [FeedbackTrack: Visual-Cortex-Inspired Cross-Frame Feedback for Transformer Tracking](https://arxiv.org/abs/2608.09369)

**<font color=#1a73e8>作者：</font>** Yueyang Cang, Xiaoteng Zhang, Zhiyuan Ning 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual object tracking requires effective temporal integration, yet most Transformer trackers still rely on predominantly feed-forward feature extraction. Existing temporal mechanisms typically update templates, prompts, queries, or prediction states, while intermediate representations are rarely reused to modulate corresponding processing stages. We propose \textbf{FeedbackTrack}, a visual-cortex-inspired framework that introduces sparse, group-level layer-aligned cross-frame feedback into pretrained Transformer trackers. Previous-frame intermediate states are detached, cached, and returned to corresponding Transformer groups in the current frame through two lightweight pathways: Query Feedback for token-level query modulation and Gate Feedback for context-dependent feature modulation. FeedbackTrack preserves the original tracking pipeline with only a fixed-size one-frame cache. Across SPMTrack and ARTrackV2, FeedbackTrack consistently improves five backbone configurations on LaSOT and GOT-10k, achieving 83.4 AO and 79.1 AUC with SPMTrack-G while adding less than 1\% parameters. Controlled comparisons show that cross-frame feedback outperforms same-frame modulation by 1.8--3.2 AO points, demonstrating that the gains mainly come from recurrent historical information. Further analysis reveals a non-uniform depth-dependent organization of learned feedback strengths, highlighting the effectiveness of recurrent feedback for Transformer tracking.

---


### 356. [Preserve More Details: Mitigating Content Drift in Real-World Image Super-Resolution](https://arxiv.org/abs/2608.09373)

**<font color=#1a73e8>作者：</font>** Chunxiao Liu, Wei Liu, Anbin Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image super-resolution (Real-ISR) aims to reconstruct high-quality (HQ) images from low-quality (LQ) inputs subject to diverse real-world degradations. Recent advances have leveraged the LQ inputs and natural image priors learned by Stable Diffusion models to achieve impressive results. However, existing methods often overlook insufficient clarity of LQ inputs inevitably induce content drift in the generated HQ images. This manifests primarily as visual detail degradation and textual semantic shift, severely compromising both fidelity and perceptual quality. To address this challenge, we propose FSP-Diff, a novel one-step diffusion model featuring a dual-pathway architecture. This architecture comprises a Detail-Conditioned Pathway for injecting structured details to recover fine structures, and a Detail-Modulated Semantic Pathway that refines semantic guidance using structured details to mitigate semantic deviations. Extensive experiments on standard Real-ISR benchmarks demonstrate that FSP-Diff surpasses existing one-step diffusion methods in both quantitative and qualitative metrics.

---


### 357. [Efficient Human-Contact Representation for Human-Scene Interaction](https://arxiv.org/abs/2608.09388)

**<font color=#1a73e8>作者：</font>** Nghia Vu, Tuong Do, Binh X. Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-scene interaction is an active research topic with several industrial applications in virtual reality, gaming, robotics, and surveillance. Despite significant progress in network architectures to improve the results or optimize models' parameters for fast inference speed, the efficient representation of contact between humans and their environments remains an open challenge. In this paper, we propose a new efficient human-contact representation for human-scene interaction. Our primary contribution is the introduction of sparse contact masks that strategically select essential contact information, significantly reducing redundant data in high-dimensional inputs. Leveraging this efficient contact representation, we propose a suite of sparse operators to replace traditional dense operators within deep network layers for faster computation. Our approach not only enhances computational speed but also filters out non-essential contact data, thereby improving the precision of human-scene interaction models. To validate the effectiveness of our method, we conduct intensive experiments across three public benchmark datasets, focusing on two critical tasks for human-scene interaction: contact prediction and scene synthesis. The experimental results show that our approach outperforms state-of-the-art models in reconstruction accuracy and achieves a computation speed-up of at least 12 times over recent baselines.

---


### 358. [CoInS-Net: A Continuous Position-Aware Network for Joint Medical Image Interpolation and Segmentation](https://arxiv.org/abs/2608.09391)

**<font color=#1a73e8>作者：</font>** Yujia Sun, Ningfeng Que, Peiting Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate medical image interpolation and anatomical structure segmentation are fundamental for computer-aided diagnosis and treatment planning. Anisotropic medical volumes with sparse through-plane sampling often suffer from structural discontinuity and boundary blur, hindering reliable clinical image analysis. Most existing methods implement interpolation and segmentation independently, which introduces redundant computation and fails to fully exploit complementary cross-slice structural information between sequential slices. To address these issues, we propose a continuous position-aware interaction network, termed CoInS-Net, for joint frame interpolation and lesion segmentation. Unlike conventional cascaded interpolation-then-segmentation paradigms, the framework enables bidirectional interaction under a shared Swin encoder with continuous spatial coordinate queries. A spatially continuous position interpolation module generates target-position features at every scale from the relative coordinate and physical spacing, and a prototype-based task mutual interaction module lets the segmentation and interpolation branches exchange global structure through a small set of shared prototypes rather than dense feature mixing. A multi-scale task-cooperative decoder further separates each scale into shared and task-specific components, so the two tasks reinforce common anatomy while preserving their distinct requirements down to the boundary level, without extra annotations. Experiments on four public medical imaging datasets with diverse modalities and anatomical regions demonstrate that the proposed method outperforms conventional single-task schemes. The joint optimization framework effectively realizes mutual promotion between interpolation and segmentation tasks, providing a reliable and universal technical scheme for intelligent clinical medical image analysis.

---


### 359. [CableDex: Cable Length Estimation on Industrial Reels Using a Handheld Device](https://arxiv.org/abs/2608.09392)

**<font color=#1a73e8>作者：</font>** Francisco Guillén, Ricardo Almeida, Bruno Silva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CableDex is a computer vision system that addresses the time-consuming and inaccurate manual measurement of cable length on industrial reels from a single photograph captured with a mobile phone. The system combines camera calibration, instance segmentation, pose estimation, and volumetric calculation to estimate the cable length across five different reel types and various cable sizes. This system is based on an instance segmentation model trained on 1,000 manually annotated images, achieving 99.5\% mAP50 with an inference time of 5.66 ms per image. Evaluated on 75 reels across five reel types, the system achieves a MAPE of 4.90\%, within the 10\% error tolerance commonly accepted in industrial cable-reel measurement. The demonstration presents the end-to-end pipeline, from reel label scanning and image capture to segmentation and length estimation, through the mobile application.

---


### 360. [From Objectives to What Models Learn: A Landau Theory of Invariant Learning](https://arxiv.org/abs/2608.09396)

**<font color=#1a73e8>作者：</font>** Pinli Wang, Yue He, Peng Cui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Invariant learning seeks representations that remain predictive across environments, yet the behavior of its objectives along the regularization path is often opaque. We address this objective-behavior gap by viewing representation learning as multimode magnetization and deriving, from concrete invariant-learning objectives, a Landau-type effective free energy whose low-order coefficients form objective signatures and induce distinct regularization phenotypes. Effective quadratic corrections move the phase boundary and enable finite-strength mode elimination; quartic corrections regulate post-onset amplitude and typically leave residual loading at finite strength; higher-order structure governs non-monotone tails, instability, and collapse at large regularization. In a canonical bilinear model, the theory yields closed-form phase boundaries and steady-state loadings, as well as distinct critical strengths for shortcut and stable modes that define a selective-retention window. Controlled experiments confirm the predicted phase boundaries, loadings, and regularization phenotypes. In one- and two-hidden-layer ReLU networks, the same signatures remain predictive of qualitative regularization-path behavior despite depth-dependent shifts in scale. A matrix extension generalizes the framework to coupled collective modes and yields a spectral phase-boundary criterion. Together, the framework turns low-order objective signatures into predictions of regularization phenotypes and, ultimately, of what models learn as regularization varies.

---


### 361. [Sign Language Recognition Using Original and Synthetic Depth Image Based Point Cloud Data Models](https://arxiv.org/abs/2608.09400)

**<font color=#1a73e8>作者：</font>** Rustem Ozakar, Eyup Gedikli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Research regarding the sign language recognition mostly relies on RGB images, whileas sign language datasets that provide depth images are limited. Point clouds obtained from depth images can be used for sign language recognition with neural networks like PointNet. In recent years, various neural networks are used for generating realistic depth images from monocular RGB images. In this work, synthetic depth images were created from RGB images using Depth Anything V2 network. For this purpose, three sign language datasets (Real-time ASL Fingerspelling, KArSL, AUTSL) which contain both RGB and depth images were used. Classification accuracies of the point cloud data created from both original and synthetic depth images using various PointNet architectures were measured for sign language recognition. From the original and synthetic point clouds, frame based, Point Gesture Map and Long Short Term Memory data models were used for classification and their performances were compared. In the results, both original and synthetic based data achieved acceptable performance in most models. In general, original depth based point cloud models performed better than synthetic ones, however in some models synthetic depth based models performed better than the originals.

---


### 362. [One Model to Magnify Them All: Efficient Scale-Invariant Histopathology via Conditional Normalization and Continuous Magnification Training](https://arxiv.org/abs/2608.09403)

**<font color=#1a73e8>作者：</font>** Agnieszka Florkowska, Henning Müller, Marek Wodzinski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole slide images (WSIs) in digital histopathology are acquired at discrete magnification levels encoding complementary diagnostic information from global tissue architecture to fine-grained cellular morphology. Yet, deep learning models remain sensitive to scale variation. Existing magnification-invariant methods rely on multi-scale architectures at predefined discrete resolutions, while in clinical deployment the acquisition magnification varies continuously, rarely aligns with a model's fixed training resolution, and intermediate scales are common, so robust coverage otherwise demands a costly ensemble of magnification-specific models. We propose Conditional Layer Normalization (CLN), a lightweight mechanism that generates affine normalization parameters from input pixel size via a small MLP, integrated into standard CNN architectures for both WSI classification and segmentation. Trained on patches sampled continuously across a range of pixel sizes, the model decouples inference from scanner-dependent magnification and generalizes to arbitrary, previously unseen scales at test time. On the PANDA prostate cancer dataset, our approach on average matches or exceeds independently trained single-magnification models and ranks among the top three performers at every evaluated magnification, including those unseen during training. This collapses a five-model ensemble into a single network and reduces training, and inference cost roughly 4-5 times, while leaving the multiply-accumulate count unchanged. The code is available at: this https URL.

---


### 363. [MeanSR: Restoration Trajectory Learning for One-Step Perceptual Super-Resolution](https://arxiv.org/abs/2608.09405)

**<font color=#1a73e8>作者：</font>** Axi Niu, Jiawei Kou, Kang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based super-resolution (SR) achieves strong perceptual quality but requires costly iterative denoising. Existing one-step distillation methods reduce inference time but depend on expensive pretrained teachers, whereas CTMSR avoids distillation through PF-ODE consistency training yet does not explicitly model the restoration dynamics from low-resolution (LR) inputs to high-resolution (HR) images. We propose MeanSR, a one-step perceptual SR method that learns an LR-conditioned average velocity field to directly capture the finite-time transition from degraded or noisy inputs to plausible HR outputs. We further reformulate distribution trajectory matching for average-velocity generation and introduce a Stage-Aware Temporal Sampling strategy to improve trajectory learning. Experiments on synthetic and real-world benchmarks show that MeanSR outperforms CTMSR on CLIPIQA, MUSIQ, and MANIQA while substantially reducing FLOPs and inference latency. MeanSR also reconstructs sharper structures and more realistic textures with fewer perceptual artifacts.

---


### 364. [A Mechanistic Diagnostic of Rank Collapse in Post-Norm Decoder Transformers](https://arxiv.org/abs/2608.09417)

**<font color=#1a73e8>作者：</font>** Xingjian Wang, Qingyu Han, Xiaodong Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep decoder-only Transformers often replace the original Post-Norm architecture with Pre-Norm variants because Post-Norm training is highly sensitive to warmup and learning rate under conventional initialization schemes. Although prior work has identified rank collapse and gradient vanishing as related symptoms, it remains poorly understood how causal attention creates high-similarity representations and why training dynamics fail to repair them. We give a two-stage analysis of Post-Norm rank collapse using token similarity as a scalar state variable. First, at initialization, causal attention acts approximately as a prefix-averaging operator that increases token similarity across depth, while the SwiGLU branch contributes only a smaller damping effect. Second, once training enters a high-similarity regime, growth of pre-normalization residual norms makes the RMSNorm backward factor contractive; under mild conditions, gradients to earlier layers decay geometrically. As a complementary result, we characterize the properties of a collapsed network: its best predictor is frequency distribution with relatively high loss floor, and gradients in collapsed layers vanish at frequency distribution. Experiments on 48-layer decoder-only Transformers trained on C4 dataset match the predicted initialization-time similarity growth and collapse-time gradient contraction, and show that collapsed runs stay near the predicted frequency loss. Together, these results distinguish the forward similarity amplification and backward repair incapacity in Post-Norm collapse, while also characterizing the behavior of collapsed networks.

---


### 365. [Intent Speaks Louder: Controllable User Simulation Beyond Response Imitation](https://arxiv.org/abs/2608.09420)

**<font color=#1a73e8>作者：</font>** Bo Wang, Ruixing Zhang, Yunqi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User simulators are widely used as scalable environments for training and evaluating interactive assistants. Generating the next user turn is inherently one-to-many: the same profile and dialogue context may support multiple plausible continuations with different local interaction intents. A fluent response may therefore advance the dialogue through an inappropriate intent, such as acceptance rather than repair. Our key insight is that controllable user simulation should separate which local interaction intent the next user turn should realize from how that intent is expressed in language. We introduce UserIDA (User Intent-Directive Alignment), which exposes interaction intent as an explicit per-turn directive. UserIDA defines a six-way intent interface, learns directive-conditioned generation through supervised fine-tuning, and uses intent-calibrated policy optimization during group-based reinforcement learning. The reward preserves composite response quality while ensuring that intent-violating candidates rank below compliant alternatives in mixed groups. On LMSYS-USP, UserIDA achieves 86.6\% intent accuracy, outperforming the strongest dedicated user-simulator baseline by 24.3 percentage points while improving semantic and stylistic similarity. In within-context interventions, it realizes at least four of the six target intents in 91.7\% of evaluated dialogue states, compared with 22.9\% for the strongest external baseline. These results establish per-turn intent control as a complementary dimension to response fidelity in user simulation.

---


### 366. [LITEWAY: LIghtweight HAR via Temporal Efficient highWAY](https://arxiv.org/abs/2608.09421)

**<font color=#1a73e8>作者：</font>** Dominique Nshimyimana, Vitor Fortes Rey, Mengxi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable human activity recognition (HAR) remains challenging due to the computational and energy constraints of deep learning models on resource-limited devices. Existing lightweight approaches often rely on recurrent architectures (e.g., GRU and LSTM), limiting parallelism and increasing inference latency. We propose LITEWAY, a modality-agnostic, fully convolutional framework for multichannel sensor time series that replaces recurrent temporal modeling with structured convolutional decomposition. LITEWAY combines lightweight convolutional blocks, strided temporal processing, and convolution-attention pooling to efficiently capture temporal dependencies while reducing computational complexity. We evaluate LITEWAY on 16 HAR datasets against TinyHAR, TinierHAR, and MLP-HAR. LITEWAY achieves competitive macro F1 while reducing model size by 4.06x-9.52x (Light) and 3.87x-9.07x (Full) compared with TinyHAR and TinierHAR. Deployment experiments further show energy reductions of 2.29x-3.14x (Light) and 1.46x-2.01x (Full) compared with TinierHAR and MLP-HAR, highlighting efficient fully convolutional temporal modeling for wearable HAR. The source code is publicly available at this https URL.

---


### 367. [How Simple Can It Get? From Interpretable Equations to Readable Rules for Financial Decision Making](https://arxiv.org/abs/2608.09433)

**<font color=#1a73e8>作者：</font>** Adia Lumadjeng, Ilker Birbil, Erman Acar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In regulated domains such as finance, a model that cannot be explained cannot be deployed, yet many interpretable classifiers defeat their own purpose by producing formulas with dozens of features that no regulator could read. We take the reverse direction. Starting from an interpretable classifier expressed as a single equation over the input features, we progressively simplify it into more readable forms, including a pruned monomial, a directional if--then rule, and the integer scorecards and tallies that finance already deploys. Because the equation is itself the predictive model rather than a post-hoc explanation we can directly quantify what is lost under each simplification. Across four financial datasets, we find that pruning is nearly free and that fidelity can erode faster than predictive performance, allowing simpler rules to remain effective classifiers without faithfully reproducing the original model. A human assessment shows that simplification improves perceived readability, while preferences for different representations vary by professional background. Beyond measuring these losses empirically, we show that some can be anticipated from the original model: we derive a bound on the change caused by pruning and predict how faithfully a rule retaining only the direction of each feature's effect preserves the original ranking.

---


### 368. [Unveiling the Secret of AdaLN-Zero in Diffusion Transformer](https://arxiv.org/abs/2608.09438)

**<font color=#1a73e8>作者：</font>** Jie Zhu, Mingyu Ding, Boqiang Duan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformer (DiT), a rapidly emerging architecture for image generation, has gained much attention. However, despite ongoing efforts to improve its performance, the understanding of DiT remains superficial. In this work, we delve into and investigate a critical conditioning mechanism within DiT, adaLN-Zero, which achieves superior performance compared to adaLN. Our work studies three potential elements driving this performance, including an SE-like structure, zero-initialization, and a "gradual" update order, among which zero-initialization is proved to be the most influential. Building on this understanding, we propose an analysis-guided initialization strategy, termed adaLN-Gaussian, which serves both as an empirical validation of our analysis and as a practical initialization method that consistently improves optimization efficiency. On the other hand, inspired by the SE-like structure, we introduce an improved conditioning mechanism called SE-adaLN-Zero. Extensive experiments following DiT on four datasets, especially on ImageNet1K demonstrate the effectiveness and generalization of adaLN-Gaussian and SE-adaLN-Zero. Beyond class-to-image generation, we also evaluate the generalization of the two improved methods on text-to-image generation.

---


### 369. [DiffSafeMerge: Mitigating Backdoor Inheritance in Diffusion Model Merging](https://arxiv.org/abs/2608.09445)

**<font color=#1a73e8>作者：</font>** Jiayang Zhang, Ji Guo, Jiachen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Unconditional diffusion checkpoint merging assumes benign sources, yet a compromised public checkpoint can transfer a dormant backdoor while clean generation appears normal. Mitigation is difficult without knowing the compromised source, trigger, or target, and broad sanitization may degrade image quality. We introduce DiffSafeMerge (DSM), which uses a small unlabeled clean set and fixed, attack-agnostic stress probes to score source blocks, shrink suspicious contributions toward a trusted reference, and select attenuation under a clean denoising-loss budget. We evaluate four attacks, two datasets, and 21 target conditions. Intended merging already has zero worst-target ASR in 10 of 14 source cases; DSM preserves these outcomes and records no target match in the remaining four over three seeds, including three with baseline ASR of 48--100\%. Among methods with zero worst-target ASR on both datasets, DSM obtains the lowest case-averaged FID in the matched seed-0 comparison.

---


### 370. [Sekai2: From World Exploration to Interactive World Modeling](https://arxiv.org/abs/2608.09449)

**<font color=#1a73e8>作者：</font>** Kang He, Wenshuo Peng, Zihui Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models must capture how scenes evolve over time and across viewpoints. Training them for long-horizon generation and camera control therefore benefits from long videos paired with camera trajectories and temporally grounded semantics. Existing corpora rarely offer the three together: large-scale web video provides broad visual diversity but no trajectories or time-aligned text, while pose-annotated datasets are typically short-range or reconstruction-oriented. We introduce Sekai2, a multi-source real-world video dataset that carries the world-exploration footage of Sekai toward interactive world modeling. The release contains 128,892 clips totaling 2,826 hours from 10,428 source videos across 113 countries or regions, and is deliberately weighted toward sustained observation: under a common 120-second decomposition, 43,594 segments reach the full two minutes and account for 51.4% of all footage. Every clip includes a released camera trajectory and hierarchical annotations disentangling subject motion, environment dynamics, static scene content, and camera behavior, resulting in 649,597 temporally grounded segments. Crucially, we further introduce 982 panoramic sequences captured along non-linear trajectories with loops and revisits. These revisits provide repeated observations of the same locations across time and viewpoints, offering essential supervision for learning persistent scene representations, long-term spatial memory, and geometrically consistent world models. Corpus-scale analyses demonstrate complete pose-and-caption coverage, broad geographic and semantic diversity, varied camera trajectories, and highly non-redundant temporal descriptions. Together, these properties make Sekai2 a scalable resource for long-horizon video generation, camera-controllable synthesis, and interactive world-model pre-training.

---


### 371. [From Approachability Residuals to Anytime-Valid Evidence: The Online Convex Geometry of Testing by Betting](https://arxiv.org/abs/2608.09450)

**<font color=#1a73e8>作者：</font>** Jinze Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Betting-based sequential tests and Blackwell approachability are linked by a rate-explicit reduction through support-function residuals. For a compact convex target $S$ and vector observations $r_t$, an OCO learner selects a predictable normal $w_t$ and produces $q_t=\langle w_t,r_t\rangle-h_S(w_t)$. We prove the exact pathwise identity $$
\dist(\bar r_T,S)
=\frac1T\sum_{t=1}^Tq_t+\frac{\Reg_T}{T}. $$ When $|q_t|\leq B$, composing this identity with one-sided betting yields a finite-time transfer: if the OCO and log-wealth regrets are at most $a_T$ and $\ell_T$, respectively, then a target gap exceeding \[
\frac{a_T}{T}
+2B\sqrt{\frac{\log(1/\alpha)+\ell_T}{T}} \] forces rejection by time $T$, while non-rejection certifies the converse radius. We then formulate a controlled stochastic experiment in which an action selected after $w_t$ satisfies Blackwell's supporting-halfspace condition for every null mean payoff. The resulting wealth is an e-process under adaptive nulls; sublinear OCO regret gives stochastic approachability, whereas persistent mean separation under an alternative gives exponential wealth at rate at least $\delta^2/(4B^2)$. Deterministic Blackwell games and passive tests are, respectively, the noise-free and singleton-action cases of this protocol. Bounded two-sample means, kernel MMD, and active heterogeneous data sources instantiate the reduction. The resulting connection is exact algebraically, quantitative at finite time, and operational when experiments are controlled.

---


### 372. [A Content-Aware Pure Permutation with Intrinsic Avalanche Effect: Breaking the Diffusion-Permutation Dichotomy](https://arxiv.org/abs/2608.09452)

**<font color=#1a73e8>作者：</font>** Zahra Ghoraeian, Mohammad-Reza Sadeghi, Samaneh Mashhadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel permutation is a fundamental tool in image processing, image encryption, and data hiding (including watermarking and steganography) that rearranges pixels without changing their values. A common assumption in the literature is that permutation alone cannot create differential sensitivity; changing one pixel merely relocates that pixel in the output, producing no avalanche effect. This paper challenges this by introducing the Triangular Content-Aware Permutation (TCA) algorithm.
The method extracts edge points using Canny and applies Delaunay Triangulation to edges and corners, creating a unique partition. Since triangulation is highly sensitive to image geometry, changing a single pixel alters the edge map, resulting in a completely different triangulation and global permutation pattern. Unlike classical dimension-based permutations and advanced content-aware methods (2025-2026), which lack differential sensitivity, TCA increases NPCR from near-zero to 97.10% solely through pixel relocation.
Experiments on 50 images show that TCA, with an average of 14.81 iterations, achieves NPCR = 97.10% and UACI = 20.06%, proving pure permutation can create significant differential sensitivity. Conventional methods maintain near-zero NPCR. The iteration threshold varies from 6.4 to 30.7 based on content complexity. Low PSNR (11.93 dB) and near-zero correlation (~10^-3) confirm superior statistical performance. Although slower than classical methods due to triangulation, this is a deliberate trade-off for stronger security. Given the non-analytic, content-dependent nature of the pattern, TCA is ideal for reference-based encryption, fragile watermarking, and non-blind steganography.

---


### 373. [Learning to Modulate, Not to Cycle: Soft Actor---Critic Recovers Inverter-Style Heat-Pump Control](https://arxiv.org/abs/2608.09453)

**<font color=#1a73e8>作者：</font>** Faizan Ahmed, Aniket Dixit, James Brusey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On--off cycling is the main cause of compressor wear in residential heat pumps, yet reinforcement learning (RL) controllers for buildings typically optimise only energy cost and thermal comfort, ignoring how much the learned policy cycles. We add a levelised compressor-wear term to the control reward and study how the resulting behaviour depends on the RL algorithm. Training Soft Actor---Critic (SAC) and Proximal Policy Optimisation (PPO) on an identical Markov decision process for the BOPTEST bestest hydronic heat pump case, we find that SAC learns a continuous modulation policy that keeps the compressor permanently engaged---the operating principle of an inverter-driven heat pump---achieving zero start-ups per day, whereas PPO collapses to bang-bang control that cycles more than the baseline. On the BOPTEST emulator the SAC policy cuts thermal discomfort by up to 90.7% for an 11.5% cost increase, while eliminating all baseline cycling.

---


### 374. [Flow-based conditional cardiac anatomy generation for virtual cohorts](https://arxiv.org/abs/2608.09460)

**<font color=#1a73e8>作者：</font>** Konstantinos Kevopoulos, Beatrice Moscoloni, Benjamin Alheit 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cardiac digital twin research is moving from subject-specific anatomical replicas toward virtual cohorts that represent clinically relevant population subgroups. Yet access to representative imaging-derived anatomy datasets remains limited by cohort size, subgroup sparsity, and data-sharing constraints. Conditional generative models could help address this gap, but virtual cohorts are useful only if they preserve realistic, metadata-dependent anatomical variability. Existing cardiac anatomy generators largely rely on conditional variational autoencoders (cVAEs), which couple representation learning and metadata conditioning through a shared regularized latent prior. We introduce CAN-FLOW, a two-step Conditional ANatomy generation framework based on normalizing FLOWs that first learns geometry-only latent representations of diffeomorphic cardiac shape momenta and then models their sex-, age-, and body-mass-index-dependent distribution with a conditional normalizing flow. We trained CAN-FLOW on 2,208 healthy UK Biobank subjects and compared it with cVAEs across regularization strengths. CAN-FLOW generated plausible stochastic biventricular anatomies that better reproduced clinical phenotype distributions, metadata-dependent trends, subgroup variability, point-cloud coverage, and high-dimensional shape variability. Together, these results establish CAN-FLOW as a shareable framework for generating realistic, stochastically varying, metadata-conditioned biventricular anatomies for virtual cohort construction and in silico clinical trial workflows.

---


### 375. [From Prompt to Harness: Coderlet from Scratch](https://arxiv.org/abs/2608.09480)

**<font color=#1a73e8>作者：</font>** Mengfan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A model alone does not determine how a programming agent acts. What the model sees, how actions enter the environment, how feedback returns, and how one run affects the next all depend on how the harness is organized. Minimal examples usually show only the basic interaction between a model and tools, while production systems spread these relationships across complex components and dependencies. This paper studies a compact harness design by following a single request through context formation, model decision, environmental action, observation return, and state continuation. Three boundaries---model, execution, and state---connect the model service, tool environment, and persistent state, while the request lifecycle determines the order in which these transitions occur. Together, they show the harness's core role: turning model generations into environmental actions, carrying runtime feedback into later decisions, and allowing state to continue across requests. On top of this runtime structure, a harness can also be gradually refined across runs through continued bootstrapping. The design is realized in the executable artifact this https URL.

---


### 376. [Beyond Uniform Restoration: Empowering All-in-One Restoration with Pixel-Level Multimodal Guidance](https://arxiv.org/abs/2608.09482)

**<font color=#1a73e8>作者：</font>** Chunxiao Liu, Wei Liu, Anbin Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> All-in-one image restoration is a unified low-level vision task that aims to effectively recover high-quality images from inputs degraded by various types and levels of corruption using a single model. Recent works have achieved remarkable progress by learning degradation-adaptive prompts or network architectures. However, these methods typically apply a uniform restoration strategy across the entire image, neglecting the fact that different regions may suffer from distinct degradation types and varying degrees of severity. In contrast, we propose to perform restoration at the pixel level, thereby enabling more fine-grained and precise control over the restoration process. Specifically, we present MGN-AIR, a novel pixel-level restoration framework for all-in-one image restoration. Our approach first learns to estimate a pixel-level visual prompt. Then, it leverages both textual and visual prompts to provide global and local degradation cues, guiding the model on where to look and how to restore at each pixel. We conduct extensive experiments on multiple all-in-one image restoration benchmarks, covering a wide range of tasks including denoising, deraining, deblurring, dehazing, desnowing, and low-light enhancement. Experimental results demonstrate that our proposed method consistently and significantly outperforms existing approaches.

---


### 377. [Hierarchical rank-evolving representation for physics-informed neural networks](https://arxiv.org/abs/2608.09483)

**<font color=#1a73e8>作者：</font>** Ruoyang Su, Xi-Le Zhao, Kun Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, tensor-based physics-informed neural networks (T-PINNs) have received increasing attention. However, existing T-PINNs still face a fundamental challenge: they mainly rely on pre-specified low-rank tensor decompositions with manually tuned ranks, which limits their ability to capture the underlying structures of multivariate solution functions and hinders their practical deployment. To address this challenge, we propose a hierarchical rank-evolving (abbreviated as HRE) representation for multivariate functions, which endows us to faithfully capture the underlying structure of the targeted multivariate function accompanying with automatic rank determination. Concretely, in the hierarchical design of HRE representation, the target multivariate function is decomposed as a small-scale inner tensor with a set of univariate functions along each mode, where a customized tensor network decomposition can be readily deployed to capture the underlying structure of the small-scale inner tensor. In HRE representation, the crucial hyperparameters, ranks, can be adaptively revealed during the decomposition, freeing us from manual rank tuning and making HRE practically applicable to real-world problems. Besides, we build the HRE-PINNs correspondingly. Extensive numerical experiments, including high-dimensional static problems (Helmholtz equation and Poisson equation), nonlinear time-dependent problems (Klein-Gordon equation), and complex fluid-dynamics problems (flow mixing equation and Navier-Stokes equation), demonstrate that HRE-PINNs consistently outperform existing state-of-the-art approaches in terms of accuracy.

---


### 378. [SwissCrop25: A National Multi-Year Benchmark for Operational Crop Mapping](https://arxiv.org/abs/2608.09497)

**<font color=#1a73e8>作者：</font>** Thomas Lauber, Mehmet Ozgur Turkoglu, Sélène Ledain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Operational crop mapping requires models that generalise across years, resolve fine-grained crop taxonomies, and distinguish cropland from surrounding landscapes. However, existing crop mapping datasets enable evaluation of these requirements only in isolation. We therefore introduce SwissCrop25, a national-scale crop mapping benchmark dataset spanning seven growing seasons (2019-2025). SwissCrop25 combines Sentinel-2 time series, daily temperature observations, a fine-grained 73 crop taxonomy including grassland management types, and 5 explicit non-crop land cover classes. To evaluate realistic deployment conditions, we define a leave-one-year-out protocol with joint cropland delineation and crop classification for benchmarking representative crop mapping architectures. Evaluating U-TAE (convolutional temporal-attention model), TSViT (transformer-based spatio-temporal model), and Galileo (EO foundation model) reveals differences between architectures hidden by conventional benchmarks. In this setting, domain-specific models outperform Galileo, with TSViT achieving the best overall performance and a 12 pp macro-mIoU advantage over U-TAE. SwissCrop25 also exposes substantial interannual distribution shifts and shows that incorporating temperature-derived phenological information improves robustness. Finally, in-season evaluation reveals a trade-off between models, with U-TAE performing better early in the season and TSViT gaining an advantage later through improved rare-class discrimination. SwissCrop25 provides a challenging testbed for evaluating crop mapping systems under realistic operational conditions and is publicly released at this https URL .

---


### 379. [ANTMAN: An Efficient and Interpretable RTL-Level Run-Time Detection Framework for Stealthy Branch Predictor Attacks on BOOM](https://arxiv.org/abs/2608.09498)

**<font color=#1a73e8>作者：</font>** Muhammad Hassan, Maria Mushtaq, Jaan Raik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Runtime detection of microarchitectural side channel attacks remains significantly underexplored in RISCV compared with x86 and ARM ISAs, posing a serious threat to critical applications. State-of-the-art branch predictor attacks bypass traditional data and instruction caches by directly exploiting the state of internal history tables, making them inherently stealthy. Recent research has explored offline detection of microarchitectural attacks on RISC-V; however, efficient runtime detection of microarchitectural attacks on RISC-V hardware remains significantly unaddressed. State-of-the-art hardware-based runtime detection solutions leverage hardware performance counters (HPCs) but suffer from a restricted set of counter registers and tradeoffs between detection accuracy, detection speed, and sampling granularity, making them impractical for stealthy attacks. Moreover, sampling HPCs after distinct intervals leaves intermediate relationships between different microarchitectural blocks unobserved. Additionally, proprietary x86 and ARM ISAs constrain researchers from modifying processor microarchitectural designs. To address these limitations, we propose the first secure-by-design, highly interpretable, non-intrusive, RTL-level runtime detection solution for stealthy branch predictor attacks on BOOM RISC-V, evaluated under both simplified Next-Line Predictor (NLP) and complex TAGE predictor configurations. The attack detection relies on association rules extracted offline and embedded in hardware as a non-intrusive rule monitor that enables runtime detection. The proposed approach achieves excellent detection speed, terminates execution before secret disclosure, and produces zero false positives while remaining flexible for detecting previously unseen variants within the same family of branch predictor attacks.

---


### 380. [Tracking the Best Strategy in an Extensive-Form Game](https://arxiv.org/abs/2608.09501)

**<font color=#1a73e8>作者：</font>** Stephen Pasteris, Rahul Savani, Theodore Turocy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the extensive-form bandit problem where on each trial the learner plays an extensive-form game against an oblivious adversary. We focus on the notion of switching regret, which measures the expected performance of the learner against that of any switching sequence of mixed strategies in retrospect. Our algorithm takes a parameter $\rho>0$ and achieves a switching regret of $\tilde{\mathcal{O}}((1/\rho+\rho K)\sqrt{H A T})$ where $K$ is the number of switches in the comparator sequence, $H$ is the maximum number of the learner's information sets that can be traversed during a play of the game and $A$ is the number of actions that the learner can possibly take. Our algorithm is extremely efficient, taking a per trial time of only $\mathcal{O}(H B)$ where $B$ is the maximum number of actions available to the learner at any of its information sets.

---


### 381. [Renormalising Generative Models for Active Inference: Foundations, Derivations, and Verification](https://arxiv.org/abs/2608.09512)

**<font color=#1a73e8>作者：</font>** Karim Zaghw, Andrew Pashea, Marc Pritsch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Active inference offers a unified framework for perception, learning, and action, but scaling discrete active-inference models to rich spatial and temporal domains remains difficult. Renormalising generative models (RGMs) address this challenge by composing discrete generative models across spatial and temporal scales, coarse-graining lower-level states and paths into higher-level causes for objects, events, and action. However, fully reproducing and adapting the framework remains difficult: the mathematical exposition is compact, and the reference implementations are deeply integrated within specialized software environments, leaving many algorithmic details implicit. This paper addresses these challenges by providing a self-contained, derivation-oriented account of RGMs together with an open, verified implementation. We explain how the hierarchy is built, how beliefs and actions are updated within it, and how information is passed between levels. Where the published equations and implementation differ in emphasis, we make those choices explicit and explain their modelling consequences. By clarifying the theory and separating it from its original implementation context, this work lowers practical barriers to entry and makes RGMs more transparent, auditable, and reproducible, providing a foundation for future quantitative evaluation and development on machine-learning benchmarks.

---


### 382. [XFeat Revisited: Reproducibility and Evaluation of a Lightweight Image Matcher](https://arxiv.org/abs/2608.09519)

**<font color=#1a73e8>作者：</font>** Lazar Đoković, Aimee Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a reproducibility study of XFeat, a lightweight local feature extractor and matcher designed to identify corresponding points across images efficiently on resource-constrained hardware. We re-implement the architecture based on the paper and supplementary material, re-evaluate the authors' released checkpoint alongside our re-implementation, and conduct additional architectural ablations to examine design choices that were not fully justified in the original work. This distinction between re-evaluation and reproduction is important, as the paper, supplement, and public code differ in several implementation details, including the backbone layout, fusion block, and training losses. Empirically, our reproduced models closely match and, in some cases, outperform the re-evaluated original checkpoint on MegaDepth-1500 and ScanNet-1500, supporting the main claim that XFeat provides a strong accuracy-efficiency trade-off for standard image-matching benchmarks. Our ablations provide a more nuanced view of two architectural arguments from the original paper. In particular, the parallel keypoint branch is important for semi-dense matching, but its benefit is less pronounced than originally claimed, while the evidence for the specific placement of the single skip-connection remains inconclusive. Finally, we reproduce the original downstream evaluations and find close agreement for homography estimation, while Aachen visual localization remains below the reported results, even for the released checkpoint, suggesting sensitivity to underspecified evaluation details. We then extend the analysis to zero-shot out-of-distribution and cross-modal matching across retinal, thermal-visible, and multimodal remote-sensing imagery, where XFeat remains effective in some settings but degrades sharply under severe modality shifts.

---


### 383. [A Height-Constrained 2-Point Minimal Solver for Pose Estimation from Active LED Markers with Event Cameras](https://arxiv.org/abs/2608.09520)

**<font color=#1a73e8>作者：</font>** Runze Yuan, Alexander Kappler, Jun Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In many autonomous applications requiring real-time localization, active marker-based systems are preferred due to their low latency and ease of deployment compared to computationally demanding feature-based methods. Event~\mbox{cameras} offer high temporal resolution and minimal delay and are commonly used with active LED markers for robust real-time localization. Existing methods typically rely on Perspective-n-Point (PnP) solvers for pose estimation. However, structured marker layouts can be challenging to deploy in space-constrained scenarios, while partial self-motion information (e.g., gravity direction and altitude) is readily available from onboard sensors. We derive a robust and accurate minimal solver that estimates camera pose from only two LED markers by incorporating known tilt angle and camera height measured by an onboard sensor, such as an IMU or an altimeter. The proposed formulation uniquely determines the camera pose through both a closed-form and a linear least-squares solution. We further analyze degenerate configurations and characterize the conditions under which height information does not contribute to rotation estimation. For evaluation, we developed an event-based active marker system to collect real-world data with ground truth from a motion capture system. Experiments on both synthetic and real data demonstrate improved accuracy over the state-of-the-art P2P solver and competitive performance relative to P3P.

---


### 384. [TriView-YOLO: Early Multi-View Fusion for Ground Penetrating Radar Cavity Detection in Soft, High-Water-Content Soils](https://arxiv.org/abs/2608.09522)

**<font color=#1a73e8>作者：</font>** Suphawut Thawinutchokaudom, Sompote Youwai, Warat Kongkitkul 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated detection of subsurface cavities from Ground Penetrating Radar (GPR) is most difficult in soft, high-water-content ground, where conductive, water-saturated soil attenuates the signal and degrades cavity reflections, yet this is also the condition under which cavities most readily form. This paper proposes TriView-YOLO, a multi-view YOLOv12 detector for road cavity screening in such ground. Three co-registered views (longitudinal B-scan, horizontal C-scan, and cross-section B-scan) form a 9-channel input fused by a TripleInputConv layer that replaces the YOLOv12 stem; the rest of the network is unchanged, and bounding boxes are required on the longitudinal view only. Training used 1,600 expert-verified field samples, principally metropolitan road surveys of Bangkok, Thailand, acquired with a vehicle-mounted multichannel three-dimensional GPR mobile mapping system, with surveys over the firmer subgrades of Japan added to training and validation only. The test set comes exclusively from the Bangkok surveys, over soft marine clay with 80-140% water content and a water table at 1-2 m depth, a ground condition for which no dedicated deep learning cavity-detection evaluation has been reported. On this unaugmented, field-only test set, split randomly within surveys, the proposed model attains mAP50 of 0.558 +/- 0.028 over three seeds at 23.6 GFLOPs and 3.1 ms per image. Ablations show that removing the auxiliary views lowers mAP50 and recall, whereas public and synthetic training images, DINOv3 features, larger model scale, and COCO pretraining bring no gain.

---


### 385. [Generalized Convexity and Smoothness via Conjugate Duality: Optimization Theory for Deep Neural Networks](https://arxiv.org/abs/2608.09523)

**<font color=#1a73e8>作者：</font>** Binchuan Qi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural network (DNN) training with stochastic gradient descent (SGD) and its variants achieves strong empirical performance, yet classical optimization theory does not fully explain this success. This limitation arises because conventional analyses rely on assumptions such as differentiability, convexity, or smoothness, which are often violated by DNN objectives. In this paper, we establish a unified optimization framework for DNN training by generalizing classical convexity and smoothness through Legendre functions and convex conjugation. Specifically, we introduce $\mathcal{H}(\psi)$-convexity and $\mathcal{H}(\Psi)$-smoothness, which unify convex and non-convex as well as smooth and non-smooth objectives within a single formalism and reveal a natural duality between generalized smoothness and convexity. Building on these generalized properties, we introduce generalized gradient descent (GD) and generalized SGD through convex conjugation. We theoretically prove that generalized GD admits an optimal learning rate of exactly $1$, and derive rigorous gradient-energy-based convergence rates for both proposed optimizers. We further reformulate DNN training as a composite optimization problem, demonstrating that its convergence relies on jointly reducing the gradient energy and controlling the induced norm of the network Jacobian. To characterize the practical influences of network architectures and training configurations, we introduce the gradient correlation factor and model capacity risk, and quantitatively analyze how architectural designs, batch size, and model capacity shape training convergence. Extensive experiments across diverse network architectures, datasets, optimizers, and loss functions validate our theoretical bounds and demonstrate precise alignment between our theoretical predictions and empirical training dynamics.

---


### 386. [Towards Expressive and Faithful Audio-to-Image Generation: A Unified Multimodal Dataset and Synthesis Framework](https://arxiv.org/abs/2608.09529)

**<font color=#1a73e8>作者：</font>** Dongxu Ge, Shansong Liu, Cheng Gong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As an important subfield of cross-modal generation, synthesizing static visual content in the form of images from audio, namely audio-to-image (A2I) generation, has attracted increasing research attention in recent years. Nevertheless, despite the remarkable visual quality of modern text-to-image (T2I) models, the performance of A2I remains fundamentally limited by traditional datasets, which often lack both high-fidelity images and precise cross-modal alignment. As a result, existing methods still struggle to achieve high-quality audio-to-image generation through finetuning strong T2I models, thereby constraining practical applications in this area. Motivated by this gap, we introduce A2I-Set, a unified, high-quality tri-modal dataset consisting of 323K paired audio, images, and detailed text captions, specifically designed for audio-visual research, including audio-conditioned image generation. Besides, we developed a new mixed-source test set for the A2I task through human supervision. We further propose an A2I model, AudioCanvas, fine-tuned on our A2I-Set. Experiments show that AudioCanvas achieves more visually expressive as well as cross-modal alignment results that generally outperforming existing approaches. Our dataset and source code are available at this https URL.

---


### 387. [DocPure: Prompt-Free Unified Document Restoration via Degradation-Aware Structure-Guided Wavelet Modulation](https://arxiv.org/abs/2608.09536)

**<font color=#1a73e8>作者：</font>** Lingming Su, Wanglong Lu, Tao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality document images are pivotal for information archiving and downstream automatic processing. However, they are frequently compromised by diverse degradations during uncontrolled acquisition and transmission. While unified document restoration techniques have been proposed to restore images from multiple degradations, they often struggle with training multiple degradation-specific models, reliance on manual task-specific prompts, or cross-task data pairing. To address these limitations, we propose DocPure, a prompt-free unified framework that achieves degradation-aware document restoration.
We design a degradation-aware structure auto-encoder with degradation-informed routing regularization to predict clean structural priors from degraded inputs. The model is prompt-free at inference, and degradation labels are only used as auxiliary supervision for the routing regularization during training.
Furthermore, we introduce a structure-guided wavelet interaction mechanism to bridge frequency-domain features and spatial semantics. Within the structure-guided wavelet interaction mechanism, a cross-frequency adaptive modulation utilizes low-frequency sub-bands to modulate high-frequency recovery, ensuring structural consistency. Extensive experiments demonstrate that DocPure achieves strong performance compared with state-of-the-art methods across various tasks, including deblurring, denoising, compression artifact reduction, and deshadowing.

---


### 388. [verdi: retrieval is not transfer for continual world model optimization](https://arxiv.org/abs/2608.09537)

**<font color=#1a73e8>作者：</font>** Junyu Wu, Shiqin Nie, Youyi Kou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation world models have made remarkable progress in planning, simulation, and embodied intelligence. However, optimizing a pretrained world model toward a user-specified objective remains difficult: each campaign typically rediscovers optimization strategies from scratch, and the resulting knowledge rarely transfers to the next model. Existing research agents automate the optimization loop but treat successful strategies as directly reusable recipes, without principled safeguards for when transfer is appropriate. We argue instead that retrieval is not transfer: a strategy validated on one model is at best an optimization hypothesis for another, and becomes transferable knowledge only after target-side experimental valida- tion. Guided by this principle, we propose VERDI , a continual framework for evidence-licensed world model optimization. VERDI characterizes each world model through shared inference-time probes to construct an Optimization Fin- gerprint, retrieves relevant prior experience as ranked hypotheses, and validates every candidate under a frozen target-side verifier before admitting it as reusable evidence; contradictions among nearby fingerprints further trigger probe evolution, continually refining the diagnostic representation itself. Experiments on Ctrl-World, the Cosmos family, and RoboCoin show that VERDI reduces search cost by 68%, GPU cost by 69%, and negative transfer from 0.34 to 0.06, while predicting transfer outcomes with 83% sign accuracy.

---


### 389. [Towards Collaborative Joint Perception and Prediction: Framework, Baseline Evaluation, and Deployment Perspectives](https://arxiv.org/abs/2608.09541)

**<font color=#1a73e8>作者：</font>** Lei Wan, Hannan Ejaz Keen, Alexey Vinel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Connected Autonomous Vehicles (CAVs) increasingly exploit Vehicle-to-Everything (V2X) communication to exchange multi-source sensor information, enabling advanced Collaborative Perception (CP) capabilities. Extending beyond these capabilities, this work focuses on Collaborative Joint Perception and Prediction (Co-P&P), a paradigm that unifies CP with motion prediction to mitigate two persistent challenges: the accumulation of perception errors and visual occlusions. We present a conceptual framework for Collaborative Joint Perception and Prediction (Co-P&P) that improves motion prediction of surrounding road users, thereby enhancing situational awareness in complex and dynamic traffic environments. Building upon our preliminary study, this extended version compares the performance of different fusion strategies and establishes baseline performance for a modular design of perception and prediction. Experimental results show that prediction-level fusion leads to a decline in overall system performance compared to detection-level or tracking-level fusion. We further implement a minimal end-to-end Co-P&P prototype that couples collaborative point-cloud sharing via the RENO neural codec with joint detection-forecasting via FutureDet, showing that collaboration improves forecasting accuracy while neural compression preserves this benefit at roughly 34x lower communication bandwidth.

---


### 390. [Training-Free Universal Approximation by Prompting Random Transformers](https://arxiv.org/abs/2608.09558)

**<font color=#1a73e8>作者：</font>** Alexander Hsu, Rongjie Lai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How expressive is prompting a transformer? Answering this question is important for separating the roles of prompting, architecture, and pretraining in transformer models, and for determining whether task-specific behavior must be stored in model weights or can instead be induced at inference time through the prompt. We show, in an approximation-theoretic sense, that pretraining is optional: a single-layer softmax attention network with random, untrained weights can approximate any Hölder function on a compact manifold when steered by an appropriate soft prompt. Guided by the connection between softmax attention and kernel methods, we construct explicit soft prompts (a prompt per target function, independent of the query) as solutions to linear systems matching attention logits to Gaussian kernel exponents, under which the frozen transformer emulates the classical Nadaraya-Watson kernel estimator. The construction requires only a mild rank condition on the weights, which we show holds almost surely under Gaussian initialization. The prompted network inherits the theoretical guarantees of kernel regression, leading to universal approximation theorems with minimax-optimal rates that depend on the intrinsic dimension. We further quantify the cost of prompting, exposing a tradeoff between the norm of the constructed soft prompt tokens, prompt length, and hidden dimension. Numerical experiments corroborate the constructions and predicted rates.

---


### 391. [From Semantic Grounding to Decision Optimization: A Unified Framework for Long-Horizon UAV Vision-Language Navigation](https://arxiv.org/abs/2608.09564)

**<font color=#1a73e8>作者：</font>** Zeyuan Ma, Jiaxin Chen, Di Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UAV vision-language navigation (UAV-VLN) focuses on enabling an aerial agent to follow natural-language instructions in open 3D environments from egocentric visual observations. Current approaches suffer from three coupled issues: weak grounding of instruction-relevant landmarks in visual observations, insufficient exploitation of long-horizon history, and unstable decisions under local traps or repeated exploration. To address these issues, we propose a unified semantic-to-decision framework. First, we present an instruction-grounded semantic enhancement module that injects object-level semantics and relative spatial cues into the current observation state. Subsequently, we develop a relevance-aware dynamic temporal aggregation strategy that reweights the full history buffer while converting a few high-relevance frames into structured landmark prompts for the decoder. Finally, we devise a topology-aware decision method that combines local-optimum cognition with group-relative policy optimization under progress, goal, semantic, and path-compliance rewards. Experiments on the widely used AerialVLN and OpenFly benchmarks clearly demonstrate that our method achieves state-of-the-art performance.

---


### 392. [Se-DPO: Self-Evolving Token Credit for Direct Preference Optimization](https://arxiv.org/abs/2608.09568)

**<font color=#1a73e8>作者：</font>** Wenxiao Zhao, Shu Wang, Ying Nian Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) aggregates token-level log-probability ratios via uniform summation, implicitly treating all tokens as contributing equally to the preference signal. However, the contribution of individual tokens to the preference signal varies. We introduce token credit, which modulates each token's KL regularization based on its contribution to the preference outcome. We derive that effective token credit is proportional to the magnitude of each token's implicit reward, and observe that this quantity evolves substantially during training. This implies that static token credit becomes increasingly misaligned as training progresses. In this work, we propose Se-DPO (Self-Evolving Token Credit for DPO), a live mechanism that derives token credit from the model's own evolving internal signals during DPO training. Since the reward signal varies in reliability across positions, Se-DPO calibrates token credit based on both the strength and the confidence of each token's contribution. Se-DPO requires no external models, adding only a lightweight calibration network with minimal computational overhead. Experiments show that Se-DPO improves over DPO by up to 9.8 points on AlpacaEval~2 and 12.2 points on Arena-Hard.

---


### 393. [Hyperbolic Multimodal Continual Learning](https://arxiv.org/abs/2608.09572)

**<font color=#1a73e8>作者：</font>** Jiahong Liu, Ming Shen, Xiaohao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic geometry has recently emerged as a powerful representation space for multimodal learning, as it naturally captures hierarchical semantic structure across modalities. Despite this progress, how such representations behave under continual learning poses fundamentally different challenges that remain underexplored. This work provides a geometric perspective on this problem and establishes a theoretical foundation for representation preservation in hyperbolic space, showing that preventing forgetting requires cross-modal invariance under a shared hyperbolic isometry. We further show that forgetting in hyperbolic continual learning involves both semantic relation drift and hierarchy-related distortion, motivating preservation of both cross-modal relational structure and hierarchical geometry. Guided by these insights, a principled continual learning framework is derived that preserves essential geometric structure while allowing effective adaptation to new tasks. Experiments on continual multimodal benchmarks corroborate the effectiveness of the proposed approach.

---


### 394. [MSP-Net: Manifold-Guided Spectral Prompt Network for Hyperspectral Object Tracking](https://arxiv.org/abs/2608.09575)

**<font color=#1a73e8>作者：</font>** Juliu Li, Hanlin Qin, Shuowen Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral object tracking leverages abundant spectral information to provide unique advantages for target discrimination in complex scenes. However, existing methods typically treat hyperspectral images as multi-channel extensions of RGB images, performing feature fusion in fixed band order. This approach leads to models dependent on specific sensor configurations while neglecting manifold relationships between bands, making generalization to heterogeneous sensors difficult. Moreover, the discriminative contribution of bands dynamically changes with target attributes and scene variations, further limiting the representational capacity of static fusion strategies. To address this, we propose the Manifold-Guided Spectral Prompt Network (MSP-Net). This network first reconstructs band relationships and forms adaptive spectral grouping through graph-driven manifold routing, then jointly integrates grouped spectral statistics with template appearance to construct target-related dynamic conditional prompts, enhancing target features while suppressing background interference. Furthermore, as tracking progresses, spectral conditions continuously evolve based on intermediate target representations, enabling target prompts to adapt in real-time to appearance and scene changes. Meanwhile, reliable historical states are used to constrain target localization and scale fluctuations, significantly improving temporal stability in cross-sensor tracking. Experiments on HOT2020 and HOT2023 demonstrate that MSP-Net achieves AUC and Precision exceeding 0.80 and 0.96, respectively, exhibiting exceptional robustness under heterogeneous sensors, target deformation, and complex background conditions. The code will be released at this https URL.

---


### 395. [You Only Flow Once: Calibrated and Real-Time Radar Pose Estimation with Multi-Hypothesis Normalizing Flows](https://arxiv.org/abs/2608.09579)

**<font color=#1a73e8>作者：</font>** Jonas Leo Mueller, Sebastian Hoefler, Dario Zanca 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse and noisy millimeter-wave radar point cloud observations often correspond to multiple plausible human poses, making deterministic pose estimation fundamentally ill-posed. Yet existing radar methods remain deterministic, collapsing this ambiguity into a single estimate. Diffusion-based alternatives can model multi-hypothesis distributions but require costly sequential denoising for each distribution sample and lack calibrated uncertainty. We propose Multi-Hypothesis Normalizing Flow Pose Generator (MH-NFPG), which models pose distributions from radar point clouds using a conditional normalizing flow. Specifically, we combine a spatiotemporal transformer backbone with a normalizing flow that transforms a Laplace base distribution into an expressive posterior, generated in parallel through a single forward pass. Leveraging this efficiency, we outperform diffusion-based alternatives in calibration across three radar benchmarks (MM-Fi, mmRadPose, mRI), improve pose accuracy on two, and match it on the third, while achieving over 20x faster inference for applications and reducing calibration error by up to 85%. We find that calibration degrades substantially for diffusion models, whereas our flow-based approach maintains reliable coverage, also in cross-environment settings. These results demonstrate normalizing flows as a practical alternative to diffusion models for real-time, uncertainty-aware radar pose estimation. Our code will be made publicly available.

---


### 396. [CoRCi: Cross-Reconstruction of Coherent Interests Modeling in Cross-Domain Sequential Recommendation](https://arxiv.org/abs/2608.09580)

**<font color=#1a73e8>作者：</font>** Qingtian Bian, Tieying Li, Marcus de Carvalho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cross-Domain Sequential Recommendation (CDSR) aims to alleviate data sparsity by transferring dynamic user interests across related domains. A key challenge lies in effectively bridging these domains. In single-domain modeling, models cannot distinguish between domain-specific and domain-invariant interests. Recent methods merge domain-specific sequences chronologically into a mixed-domain sequence to capture domain-invariant knowledge. However, they typically deploy separate encoders for the mixed-domain sequence and train them with per-domain loss aggregation. This workflow magnifies inter-domain discrepancies and disrupts domain-invariant interest coherence, especially when query target pairs in Seq2Seq originate from different domains. In this paper, we present CoRCi (Cross-Reconstruction for Coherent Interest), a dual-target CDSR framework that tackles these drawbacks. Specifically, CoRCi proposes a Cross-Reconstruction approach that generates mixed-domain representations directly from pre-encoded specific-domain representations via cross-attention. The generated representations are then trained using a single, sequence-level, domain-agnostic loss to preserve the coherence of domain-invariant interests. To further suppress domain discrepancies in mixed-domain modeling, CoRCi introduces FocalNCE, which embeds Focal Loss into the preceding mixed-domain InfoNCE objective. The new loss assigns higher penalties to negatives drawn from the same domain as the query, thereby strengthening domain-invariant alignment. Extensive experiments on four real-world datasets demonstrate that CoRCi consistently outperforms state-of-the-art CDSR counterparts, achieving statistically significant gains across all metrics.

---


### 397. [GenTrack3: Hybrid Stochastic-Deterministic Online Multi-Object Tracking with Cluster-Aware Association](https://arxiv.org/abs/2608.09581)

**<font color=#1a73e8>作者：</font>** Toan Van Nguyen, Rasmus G. K. Christiansen, Dirk Kraft 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking (MOT) involves maintaining consistent target identities as objects dynamically enter and leave a scene. Deterministic approaches, such as tracking-by-detection with data association, produce reproducible results and are computationally efficient, but they rely heavily on motion models and are sensitive to noisy detections that can lead to association errors. In contrast, stochastic methods explicitly model uncertainty and can better handle complex non-linear dynamics, albeit at the cost of increased computational complexity and variability arising from random sampling. This paper presents an online MOT framework that integrates deterministic and stochastic principles to achieve robust tracking under uncertainty. Furthermore, a novel track-to-detection matching approach is introduced to enhance scalability with increasing target numbers while supporting group tracking. The tracking inference mechanism employs a tracklet that includes identifiers, states, velocities, track penalties and track ages of targets, supporting a systematic tracking pipeline. Each target is associated with a stochastic particle set to compute the matching cost to detections. Reference implementations of the proposed approach and baseline trackers can be found on GitHub: this https URL.

---


### 398. [TeaMatch: Teachable Cross-Modal Representation Learning for 2D-3D Matching](https://arxiv.org/abs/2608.09590)

**<font color=#1a73e8>作者：</font>** Chongjian Wang, Junjie Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning reliable correspondences between images and point clouds is fundamental for 2D-3D matching. Despite recent progress in detection-free methods, existing approaches primarily optimize matching within a single model and often struggle to maintain reliable correspondences under challenging conditions such as noisy inputs, low overlap, and ambiguous structures. In this work, we propose TeaMatch, a novel framework that introduces teachability as a criterion for cross-modal representation learning. We define teachability as the ability of a representation to be effectively recovered by weak learners under degraded inputs, reflecting its structural consistency and robustness. To this end, we construct a set of task-specific weak students that simulate common failure modes and train them to imitate the teacher on a training split while evaluating their recoverability on a disjoint meta split. The teacher is then optimized to improve the students' ability to recover reliable correspondences, guided by correspondence-level and geometry-aware constraints. Our framework can be seamlessly integrated into existing coarse-to-fine matching pipelines without additional inference cost. Extensive experiments demonstrate that TeaMatch improves matching robustness and achieves state-of-the-art performance on challenging 2D-3D matching benchmarks.

---


### 399. [Illusion or Integrity? Geometrical Consistency Metric for AIGC Video Quality Evaluation](https://arxiv.org/abs/2608.09594)

**<font color=#1a73e8>作者：</font>** Yifei Xue, Yuanchen Fei, Hao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, AI-driven video generation has attracted considerable attention. This surge increases the demand for reliable video quality assessment (VQA) metrics to evaluate AI-generated content (AIGC) videos and guide model optimization. Existing studies assess video quality through visual harmony, video-text consistency, and domain-specific alignment, yet lack quantitative metrics for measuring fidelity to physical laws. To address this limitation, we present a novel benchmark that evaluates the quality of AIGC videos based on their compliance with physical principles by quantitatively measuring geometric consistency across frames extracted from generated sequences. This serves as a proxy for estimating the extent to which generated videos conform to real-world physical rules. Specifically, GeoCon-Bench captures global motion through translation estimation, fits homography or fundamental matrix models using background correspondences, and reports complementary metrics, including inlier ratio and geometric error. We also release a dataset containing 20 scenes across six motion categories. Experiments on state-of-the-art AIGC models demonstrate the reliability of GeoCon-Bench as a video quality assessment metric.

---


### 400. [LEED: Local Embedding Evolution Distance for over-smoothing estimation and virtual node selection in GNN](https://arxiv.org/abs/2608.09596)

**<font color=#1a73e8>作者：</font>** Killian Cressant, Pedro B. Velloso  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) suffer from two fundamental limitations: over-smoothing, where node representations become indistinguishable with depth, and over-squashing, where long-range information is compressed through limited message-passing channels. Existing metrics such as Dirichlet energy provide global characterizations of over-smoothing but lack the resolution to analyze node-level behavior and guide architectural improvements. In this paper, we propose LEED (Local Embedding Evolution Distance), a novel local metric that quantifies over-smoothing by tracking the evolution of individual node embeddings across layers. By operating at the node level, LEED enables fine-grained analysis of representation dynamics during training, revealing heterogeneous over-smoothing patterns that are invisible to global energy-based measures. This locality induces informative node importance scores, interpreted as embedding-driven centrality measures. We leverage LEED to design a more efficient strategy for virtual node selection. Unlike existing approaches that depend on multiple heuristic centrality measures, our method uses LEED as a unique criterion to guide the construction of Local Virtual Nodes to mitigate over-squashing. Experiments show that LEED provides more informative diagnostics than Dirichlet energy while preserving global evaluation, and enables more effective virtual node integration, improving GNN performance across datasets.

---


> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-445](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
