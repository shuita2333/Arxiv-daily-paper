# 📦 其他研究 | 2026年07月16日

> 本类共 **203** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-203](./part-05.md)

---

### 101. [Filtering-out poor-quality images for data preparation](https://arxiv.org/abs/2607.12352)

**<font color=#1a73e8>作者：</font>** Roopdeep Kaur, Gour Karmakar, Muhammad Imran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Filtering noise is a fundamental part of data preparation that enhances image quality for applications such as object segmentation, detection, and recognition. Various noise reduction techniques are proposed in the literature, including the use of median, Gaussian, and bilateral filters. Convolutional neural networks (CNNs) have gained popularity in image denoising owing to their ability to extract complex patterns and features from data. CNNs are highly adaptable, making them effective tools for various image-denoising tasks. One drawback of CNN-based techniques is that they require an appropriate training dataset and all images to be resized. Another notable drawback of all these filtering techniques is that they work for certain types of environmental and camera noises. To bridge this research gap, in this paper, for the first time, instead of denoising, we propose an approach that filters out poor-quality images for various environmental and camera impacts. In our approach, quality is assessed using an image quality assessment metric and an optimum threshold is used to filter out poor-quality images. We also ensure that a sufficient number of images remain to develop the deep learning (DL) model. The results produced using real and simulated traffic and object recognition data demonstrate the performance supremacy of the proposed approach compared with the state-of-the-art approaches. The average recognition accuracy for our proposed approach is 93.8% for the traffic sign recognition dataset and 84.9% for the object recognition dataset. This indicates our model's potential for real-life applications such as autonomous vehicles.

---


### 102. [Reducing information dependency does not cause training data privacy. Adversarially non-robust features do](https://arxiv.org/abs/2607.12354)

**<font color=#1a73e8>作者：</font>** Rasmus Torp, Shailen K. Smith, Adam Breuer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we challenge the prevailing view that information dependency (including rote memorization) drives training data exposure to image reconstruction attacks. We show that extensive exposure can persist without rote memorization and is instead caused by a tunable connection to adversarial robustness. We begin by presenting three surprising results: (1) recent defenses that inhibit reconstruction by Model Inversion Attacks (MIAs), which evaluate leakage under an idealized attacker, do not reduce standard measures of information dependency (HSIC); (2) models that maximally memorize their training datasets remain robust to MIA reconstruction; and (3) models trained without seeing 97% of the training pixels, where recent information-theoretic bounds give arbitrarily strong privacy guarantees under standard assumptions, can still be devastatingly reconstructed by MIA.
To explain these findings, we provide causal evidence that privacy under MIA arises from what the adversarial examples literature calls ``non-robust'' features (generalizable but imperceptible and unstable features). We further show that recent MIA defenses obtain their privacy improvements by unintentionally shifting models toward such features. To establish this causal relationship, we introduce Anti Adversarial Training (AT-AT), a training regime that intentionally learns non-robust features to obtain both superior reconstruction defense and higher accuracy than state-of-the-art defenses. Our results revise the prevailing understanding of training data exposure and reveal a new privacy-robustness tradeoff.

---


### 103. [ACID: Adaptive Caching for vIDeo generation](https://arxiv.org/abs/2607.12358)

**<font color=#1a73e8>作者：</font>** Om Agrawal, Saurabh Agarwal, Aditya Akella  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models produce high-quality generations but remain slow at inference due to their sequential denoising procedure. Caching-based acceleration methods address this by reusing intermediate model outputs: leading dynamic approaches such as TeaCache, EasyCache, and DiCache accumulate a drift signal and skip expensive model evaluations when accumulated drift stays below a fixed threshold {\tau}. This threshold controls an apparent tradeoff - raising it yields faster generation at the cost of visual quality, while lowering it preserves quality but sacrifices speed. We show this tradeoff is not fundamental; it is an artifact of holding {\tau} constant throughout denoising. We identify the existence of critical steps - timesteps where the drift signal changes rapidly - and show that applying a low threshold selectively at these steps while caching aggressively elsewhere recovers most of the quality of conservative caching at substantially higher inference speeds. Building on this insight, we propose ACID, a lightweight, training-free wrapper that monitors the rate of change of each method's existing drift signal to dynamically switch between a low and a high threshold. ACID is signal-agnostic and modular: it requires no retraining and plugs directly into existing dynamic caching methods without modifying their core mechanisms. Evaluated across three caching methods (TeaCache, EasyCache, DiCache) and three open-source video diffusion models (HunyuanVideo, Wan 2.1, CogVideoX), ACID consistently expands the Pareto frontier of visual quality versus inference speed beyond what any fixed threshold achieves. In particular, on TeaCache and HunyuanVideo, ACID achieves up to 2.16x speedup over the no-caching baseline, and up to 38% additional speedup over the conservative fixed-threshold baseline with negligible (<0.3 dB PSNR, <0.01 SSIM, <0.01 LPIPS) quality degradation.

---


### 104. [Same Loss, Same Noise, Opposite Schedules: Noise Structure and Optimizer Normalization Jointly Determine Whether Learning-Rate Cooldown Helps](https://arxiv.org/abs/2607.12360)

**<font color=#1a73e8>作者：</font>** Subham Singh, Ashutosh Mishra, Subha Raut  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The cooldown phase of a warmup-stable-decay (WSD) learning-rate schedule, now a default in large-model pretraining, lowers the final training loss in some settings and does nothing in others. We give a provable account of which case obtains, and it turns on two properties together: the structure of the gradient noise and whether the optimizer normalizes its update. On a strongly convex objective with multiplicative (gradient-proportional) noise, stochastic gradient descent contracts geometrically at a constant learning rate, so cooldown has nothing to improve. Under the same objective and noise, sign-based and normalized methods, the standard surrogates for adaptive optimizers, settle on a noise floor of order $\eta^2$ and reach the minimizer only as the learning rate is driven to zero; any additive noise then reinstates a floor for every method. The mechanism is elementary: an SGD step shrinks in proportion to the gradient and so anneals itself, whereas a normalized step keeps unit scale and cannot. We solve the signSGD stationary law on the quadratic exactly and obtain the floor constant in closed form, prove a local form of the dissociation under $(L_0,L_1)$-smoothness, extend the floor to normalized SGD in dimension d>1 by a scale-invariance argument, and establish robustness to momentum and heavy-tailed noise. Simulation confirms every prediction, and we demonstrate the resulting noise-regime diagnostic on a real classification task with directly measured gradient noise. The mechanism explains whether cooldown helps; the interior cooldown fraction used at scale lies outside stationary landscape-and-noise geometry.

---


### 105. [Implicit 4D Gaussian Splatting for Fast Motion with Large Inter-Frame Displacements](https://arxiv.org/abs/2607.12362)

**<font color=#1a73e8>作者：</font>** Seung-gyeom Kim, Areum Kim, Yongjae Yoo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 4D Gaussian Splatting (4DGS) methods often fail under fast motion with large inter-frame displacements, where Gaussian attributes are poorly learned during training, and fast-moving objects are often lost from the reconstruction. In this work, we introduce Spatiotemporal Position Implicit Network for 4DGS, coined SPIN-4DGS, which learns Gaussian attributes from explicitly collected spatiotemporal positions rather than modeling temporal displacements, thereby enabling more faithful splatting under fast motions with large inter-frame displacements. To avoid the heavy memory overhead of explicitly optimizing attributes across all spatiotemporal positions, we instead predict them with a lightweight feed-forward network trained under a rasterization-based reconstruction loss. Consequently, SPIN-4DGS learns shared representations across Gaussians, effectively capturing spatiotemporal consistency and enabling stable high-quality Gaussian splatting even under challenging motions. Across extensive experiments, SPIN-4DGS consistently achieves higher fidelity under large displacements, with clear improvements in PSNR and SSIM on challenging sports scenes from the CMU Panoptic dataset. For example, SPIN-4DGS notably outperforms the strongest baseline, D3DGS, by achieving +1.83 higher PSNR on the Basketball scene.

---


### 106. [Lost in Visual Translation: A VLM-Assisted Perceptual-Semantic Coherence Framework for EEG-to-Image Reconstruction](https://arxiv.org/abs/2607.12364)

**<font color=#1a73e8>作者：</font>** Sukriti Tiwari, BHVSP Subrahmanyam, Nidhi Goyal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> EEG-to-image evaluation should distinguish visual fidelity from recoverable meaning. Yet EEG-derived reconstructions are blurry, distorted, and low-detail, causing SSIM, LPIPS, and CLIP to penalize semantically recoverable outputs or reward plausible but incorrect ones. We analyze 6,855 ground-truth/reconstruction pairs from ATM, ENIGMA, BrainVis, and DreamDiffusion using semantic probes, caption harshness and blind-spot rates, and controlled degradations. Pixel metrics show near-zero correlation with semantic consistency, while representation metrics conflate perceptual and semantic errors. We therefore introduce a BCI-aware framework in which four VLMs assess image pairs through structured questions, producing Tolerant Perceptual Alignment Scores (T-PAS) and Tolerant Semantic Alignment Scores (T-SAS). Their consensus is distilled into the BCI-Coherence Score (BCS), a compact evaluator achieving a T-PAS MAE of 0.079 (r = 0.700) and a T-SAS MAE of 0.082 (r = 0.850) on our data. Human validation shows highly reliable joint coherence judgments, with Cohen's kappa = 0.882 +/- 0.174 and Krippendorff's alpha = 0.882, supporting perceptual-semantic recoverability over generic visual similarity. Code and resources are available at this https URL.

---


### 107. [UMSS: Towards Unsupervised Multi-modal Semantic Segmentation](https://arxiv.org/abs/2607.12372)

**<font color=#1a73e8>作者：</font>** Haitian Zhang, Thai Duy Nguyen, Xiangyuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal semantic segmentation (MSS) is essential for robust perception in complex environments, yet its potential remains largely untapped because of the prohibitive cost of human annotations. While unsupervised semantic segmentation (USS) has achieved strong results on a single RGB modality, its naive extension to multimodal data is often hindered by fusion degradation. This occurs because, without explicit supervision, existing frameworks struggle to reconcile the heterogeneous structural patterns captured by different sensors and therefore fail to effectively exploit their complementary information. In this paper, we make the first attempt to address the novel problem of Unsupervised Multimodal Semantic Segmentation (UMSS), aiming to effectively exploit complementary sensor information in a fully label free setting. To this end, we propose UniM2 (Unified Multimodal), a novel framework built on DINOv3 that transforms conventional fusion methods into consistent performance gains. Our key idea is to learn a unified latent space driven by Cross Modal Correspondence Synergy (CMCS) to extract intrinsic shared semantic cues, bypassing the need for label guided adaptive fusion. To mitigate inherent intermodal conflicts, we introduce a Cross Modal Harmonizer (CMH) that designates RGB as a stable reference, effectively suppressing inconsistent relational supervision while guiding the model to exploit complementary structural features. Extensive experimental results on NYU Depth v2 and MFNet show that UniM2 improves mIoU by 6.4% and 9.8%, respectively, demonstrating clear advantages over existing frameworks for UMSS.

---


### 108. [Demonstration of the common dual-channel feature decoupling characteristic of front-door mediation causal inference methods in whole-slice image classification](https://arxiv.org/abs/2607.12376)

**<font color=#1a73e8>作者：</font>** Zhirui Zhang, Tianhang Nan, Yong Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Causal inference using front door intervention and multi-instance learning (MIL) has advanced the analysis of Whole Slide Images (WSI) in digital pathology. These methods adjust feature distributions of subtle evidence sub-images to correctly associate them with WSI-level diagnoses. We propose and prove 2 hypotheses for evaluating such methods: 1) Causal inference MIL introduces an independent classification channel that effectively completes WSI classification; 2) Greater difference between features extracted by the new and baseline channels increases effectiveness in eliminating false correlations. This hypothesis describes the core of causal inference MILs: overlaying parallel, independent channels to eliminate false associations between WSI-level diagnostic and non-diagnostic evidence sub-images by increasing deep feature diversity. Based on these hypotheses, we evaluated several causal inference MILs on breast cancer and non-small cell lung cancer datasets. This hypothesis provides a new theoretical perspective for applying causal inference to WSI analysis.

---


### 109. [SeamGen: Artist-Aligned UV Seam Generation via Graph Flow Matching](https://arxiv.org/abs/2607.12379)

**<font color=#1a73e8>作者：</font>** Hao Xu, Yuqing Zhang, Yiqian Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UV seam placement is a critical yet labor-intensive step in 3D content creation, requiring artists to balance chart shape, seam concealment, and alignment with semantic and geometric features. Existing automatic methods are primarily based on per-object optimization, relying on handcrafted objectives to avoid distortion or on proxies from pretrained models to inject semantic information. However, these strategies are not always well aligned with seams used in industrial production pipelines, often resulting in layouts that deviate from artist-preferred seam patterns and practical production requirements. To address these limitations, we propose SeamGen, a generative model for UV seam generation that aligns with artist preferences and production requirements. Instead of depending on manually designed objectives and constraints, SeamGen learns the distribution of per-edge seam labels from a large corpus of existing seam layouts using a flow-matching generative model. A key challenge is that typical Transformer architectures used in flow matching models are designed for sequential representations, such as point clouds, and cannot naturally account for mesh topology. To enable mesh-native learning, we design a Mesh Transformer backbone that interleaves local graph attention over mesh edges with global self-attention across vertices, capturing both fine-grained geometric cues and long-range topological coherence. To further improve inference-time controllability and quality, we exploit the training-free inpainting capability of flow models for both localized seam refinement and constraint-guided seam generation. Extensive experiments show that by learning priors from professional seam layout data, SeamGen produces UV layouts that better align with artist-authored preferences and achieve superior perceptual quality compared with distortion-based and semantic-proxy baselines.

---


### 110. [SinAE: A Single-Architecture Flow-Matching Autoencoder for Cross-Domain Atomic Systems](https://arxiv.org/abs/2607.12380)

**<font color=#1a73e8>作者：</font>** Yuxuan Ren, Fan Yang, Jianhua Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small molecules, crystals, and proteins all reduce to atoms in 3D space, yet their generative pipelines remain fragmented across domains, each with its Small molecules, crystals, and proteins all reduce to atoms in 3D space, yet their generative pipelines remain fragmented across domains, each with its own graph, equivariant, or frame-based architecture. Cross-domain training would mitigate per-domain data scarcity, but direct generation in 3D coordinate space cannot easily handle the heterogeneous structural priors of all three domains, and no prior latent autoencoder is simultaneously lossless and architecturally general across all three. We introduce SinAE, a single-architecture flow-matching autoencoder for molecules, crystals, and proteins, with vanilla Transformer encoder and decoder and no equivariant, graph, or domain-specific operators. Rather than requiring the encoder to capture fine-grained geometry, SinAE shifts the reconstruction burden into an iterative flow-matching decoder, achieving near-lossless reconstruction across domains and reducing reconstruction errors by orders of magnitude relative to prior latent baselines. The same per-token latent supports a standard Diffusion Transformer prior that reaches strong performance on molecular, crystal, and protein generation benchmarks. Joint molecule--crystal training strictly improves both domains, providing direct evidence of cross-domain transfer through a shared atomic latent. Code is available at this https URL .

---


### 111. [Differentiable Clone-Structured Causal Graphs for End-to-End Cognitive Map Learning from Image Sequences](https://arxiv.org/abs/2607.12382)

**<font color=#1a73e8>作者：</font>** Arash Nikzad, Sasan Sarbishegi, Ali Dasmeh 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How can an agent build a structured map of its world from nothing but an ongoing sequence of raw sensory input and its own movements, especially when natural variation means exact sensory patterns rarely repeat? The Clone-Structured Causal Graph algorithm (CSCG), a normative hippocampus model, shows how an interpretable map can be learned from aliased observations. However, CSCG requires a predefined discrete alphabet, and its expectation-maximization formulation is not easily combined with existing neural network modules, preventing the end-to-end processing of raw image sequences. We remove this barrier by reformulating CSCG as a single, fully differentiable module, gradCSCG, and coupling it to a learned vector-quantized variational autoencoder (VQ-VAE) perceptual front-end. A soft emission forward pass allows the map-learning objective to flow back into perception, while a set of loss-balancing mechanisms mitigates module collapse during joint training. We demonstrate, first, that gradient training reproduces CSCG's results on original symbolic grid worlds by recovering room topology from heavily aliased observations. Second, we show that map recovery remains robust on MNIST image sequences, where each visit to a location yields a newly sampled image of its assigned digit. Across four heavily aliased environments, the end-to-end pipeline successfully uncovers the underlying adjacency graph with high edge precision and recall, directly from visual input. This work provides a proof of principle that CSCG can serve as a composable building block in a deep learning architecture.

---


### 112. [Beyond Binary Detection: A Multi-Dimensional Taxonomy of Cancer Misinformation on Reddit](https://arxiv.org/abs/2607.12383)

**<font color=#1a73e8>作者：</font>** Aria Pessianzadeh, Pooriya Jamie, Naima Sultana 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cancer-related discussions on social media provide an important space for information exchange and peer support, but also facilitate the spread of misinformation that may influence prevention, screening, and treatment decisions. Existing research on cancer misinformation often relies on narrow definitions, small-scale datasets, or binary labeling frameworks. We introduce a multi-dimensional taxonomy for characterizing cancer misinformation in Reddit discussions of breast, lung, colon, and prostate cancer. The taxonomy captures seven dimensions, including misinformation presence, information type, risk level, stance, and topical focus. Using expert-annotated data, we evaluate multiple large language models (LLMs) for scalable misinformation annotation and analyze cancer misinformation across Reddit communities. Our results show that cancer-related misinformation constitutes approximately 6\% of Reddit cancer discussions, with substantial variation across communities and misinformation topics. Few-shot prompting substantially improves classification performance, particularly for nuanced taxonomy dimensions. We additionally identify recurring misinformation narratives centered on unsupported treatments, distrust of conventional medicine, and misleading claims about diagnosis and screening. Our taxonomy, dataset, and findings provide a foundation for multi-dimensional modeling of online cancer misinformation.

---


### 113. [ReDiTT: Retrieval Augmented Conditional Diffusion Transformers for Asynchronous Time Series](https://arxiv.org/abs/2607.12391)

**<font color=#1a73e8>作者：</font>** Saiyue Lyu, Zhitian Zhang, Ruizhi Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a diffusion based model for asynchronous time series prediction, where the goal is to predict the next inter event time and event type. To address the inherent uncertainty of future events, we introduce ReDiTT, a retrieval augmented conditional diffusion transformer that operates in latent space. ReDiTT retrieves structurally similar latent sequences from a memory bank during both training and inference and incorporates them as reference conditions through cross attention. This retrieval based conditioning allows the model to attend to relevant temporal dynamics and provides global structural guidance for generation. As a result, ReDiTT stabilizes long horizon forecasting and improves sample diversity. Experiments on seven real world datasets demonstrate state of the art performance on next event prediction and long horizon forecasting. Our code is available at this https URL.

---


### 114. [Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning](https://arxiv.org/abs/2607.12395)

**<font color=#1a73e8>作者：</font>** Xinyu Tang, Gangqiang Cao, Yurou Liu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards without human-annotated data, often referred to as zero RL, has emerged as a powerful paradigm for eliciting chain-of-thought reasoning. However, due to computational constraints, existing studies are largely restricted to small models, leaving the training dynamics and emergent capabilities at a large scale unexplored. To meaningfully explore this frontier, we aim to elicit high-quality reasoning behaviors from the model. However, we find that naive scaling often suffers from poor readability, token redundancy, and a lack of adaptive reasoning depth. To address these challenges, we present a stable and efficient training pipeline, incorporating algorithmic and system optimizations such as clipped importance sampling, training-inference ratio correction, and mixed-precision control. Our experiments offer three key findings that validate the "bitter lesson" of scaling: (1) scaling to 1T parameters significantly enhances sample efficiency and performance ceilings; (2) the training process progresses sequentially through an initial discovery phase followed by a sharpening phase; and (3) the model spontaneously develops advanced cognitive behaviors, including anthropomorphism, structured formatting, self-verification, parallel reasoning, and context anxiety, rendering hand-crafted heuristics redundant. Evaluated on seven mathematical benchmarks, Ring-2.5-1T-Zero achieves competitive performance. Additionally, to assess CoT quality beyond final-answer correctness, we propose a structured evaluation framework across three dimensions: comprehensibility, reproducibility, and efficiency, where our model demonstrates clear advantages in producing structured and concise reasoning traces. By sharing our observed emergent phenomena, we hope to provide the community with deeper insights into scaling behaviors, particularly at the 1-trillion scale.

---


### 115. [Seeing Globally, Refining Locally: Global Visual Guidance and Local Ultrasound Cues for Robust Freehand 3-D Ultrasound Reconstruction](https://arxiv.org/abs/2607.12398)

**<font color=#1a73e8>作者：</font>** Yameng Zhang, Zhongyu Chen, Dianye Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Freehand 3-D ultrasound (US) imaging has attracted increasing attention owing to its intuitive volumetric visualization, ease of use, and low cost. However, accurate 3-D reconstruction critically depends on stable probe pose estimation, yet existing trackerless methods remain susceptible to accumulated pose errors, particularly over long scanning trajectories. To address this limitation, we propose a global-to-local pose estimation framework that exploits external camera observations for globally stable localization and B-mode US images for anatomy-aware local refinement. Specifically, the framework comprises a dual-camera branch that performs contextual feature aggregation across camera views and temporal observations to estimate a globally consistent probe trajectory, and a B-mode branch that performs anatomical feature aggregation from sequential US images to capture tissue-dependent local motion cues. A cross-modal fusion module subsequently integrates the contextual camera features and anatomical US features to predict pose residuals and refine the camera-derived estimates in the transformation space. Furthermore, a multi-scale pose loss constrains relative motion over multiple temporal horizons to suppress accumulated drift during extended scans. The proposed framework is validated on phantom and in vivo datasets. On two in-house datasets (FUSION-J and FUSION-L) collected using different machines, the proposed US + Dual-Cam model reduces average trajectory drift to 1.67 mm and 1.29 mm, representing improvement of 16.50% and 27.12%, respectively, over a strong dual-camera baseline, while substantially outperforming US-only pose estimation (>13 mm drift). In in vivo forearm arteries reconstruction, it achieves Hausdorff distances of 1.58 mm, demonstrating the effectiveness of the proposed method on real clinical scenarios.

---


### 116. [Physically Aware Radiomics Without Interpolation: Disentangling Voxel Geometry and Signal Modification in CT and MRI](https://arxiv.org/abs/2607.12399)

**<font color=#1a73e8>作者：</font>** David Corral Fontecha, Juan Miranda Bautista, Pablo Menendez Fernández-Miranda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective: Radiomic texture features are usually computed in voxel-index neighborhoods, implicitly assuming isotropic spatial relationships. In anisotropic images, this can confound voxel geometry with interpolation-induced signal changes. We developed a voxel-spacing-aware radiomic framework that incorporates physical geometry into texture computation without resampling.
Approach: We modified PyRadiomics to account for voxel spacing while preserving the native image signal. Four configurations were compared: native non-resampled extraction (NR), isotropic resampling (RS), voxel-spacing-aware extraction (VS), and fake-isotropic preprocessing (FK), in which spacing metadata were overwritten without altering the image array. Experiments included 685 LIDC-IDRI pulmonary nodules and 209 I-SPY2 breast MRI cases, with 196 radiomic descriptors. Robustness was assessed using ICC, within-subject variability, Friedman testing, feature selection, machine learning, a multilayer perceptron, and external validation.
Main results: VS showed near-native agreement with NR: median ICC(A,1) was 0.9976 in CT and 0.9984 in MRI. RS produced lower agreement and larger deviations, while FK showed intermediate behavior, confirming that spacing metadata alone can affect radiomic features. Gradient-derived and neighborhood-sensitive descriptors were most affected by preprocessing. VS preserved predictive performance comparable to NR in external CT validation, whereas MRI showed greater variability across preprocessing strategies and classifiers.
Significance: Voxel-spacing-aware extraction separates geometric modeling from interpolation-induced signal modification while preserving the native image signal, offering a coherent alternative to isotropic resampling for radiomic analysis of anisotropic CT and MRI.

---


### 117. [Contrastive-Augmented Flow Matching for Style-Content Disentanglement](https://arxiv.org/abs/2607.12404)

**<font color=#1a73e8>作者：</font>** Yusong Li, Pingchuan Ma, Ming Gui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning representations that separate content and style is crucial for controllable generation and compositional generalization. However, diffusion and flow-based models trained primarily with generative objectives often produce entangled or misaligned factors. To address this gap, we introduce Contrastive Augmented Flow Matching (CAtFM), a framework that integrates contrastive regularization into an invertible flow matching formulation to promote structured content-style representations. Rather than constraining intermediate latents or velocity fields, we apply contrastive supervision to predicted endpoints during training, enforcing semantic consistency across transported distributions while allowing disentanglement to emerge implicitly, without assuming strictly pure or fully factorized content and style representations. Our main experiments operate in the CLIP embedding space, with additional validation using frozen DINO and ALIGN encoders. Across synthetic data, in-domain styles, and real-world benchmarks (ImageNet, WikiArt, DomainNet, and DTD), CAtFM improves content and style retrieval, enhances embedding cluster separation, and achieves stronger open-set robustness compared to generative and discriminative baselines. Overall, CAtFM provides a simple way to couple discriminative constraints with deterministic transport, improving disentanglement and robustness under distribution shift.

---


### 118. [Mechanical Analysis of Parachute Suspension Line Deployment with Binding Tapes Using PINN](https://arxiv.org/abs/2607.12409)

**<font color=#1a73e8>作者：</font>** Xiang Zhao, Ronghui Quan, Yaqi Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parachutes are widely utilized in aviation, aerospace and lifesaving missions. As the initial stage of parachute deployment, suspension line extraction and straightening directly determines the smooth implementation of subsequent inflation procedures. This ultra-short process involves intricate dynamic load variations. Most existing studies adopt numerical integration of ordinary differential equations to calculate line tension, yet this method fails to rapidly acquire tension values at arbitrary positions along suspension lines. This paper develops a physics-informed neural network (PINN) algorithm for tension prediction during line extraction and straightening, which outperforms traditional integration methods in both computational efficiency and numerical accuracy. Furthermore, the regulatory law of binding tape parameters on line dynamic tension is investigated. Comparative validations against flight test data and conventional numerical results verify the reliability and effectiveness of the proposed PINN framework.

---


### 119. [PolarBM: Complex-valued Boltzmann Machine for Modeling Audio Signals in Polar and Log-polar Coordinates](https://arxiv.org/abs/2607.12417)

**<font color=#1a73e8>作者：</font>** Toru Nakashika, Kohei Yatabe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although vast amounts of data, such as audio signal spectra, are naturally represented using complex numbers, conventional machine learning methods often simplify complex-domain problems by employing frameworks designed for real-valued variables. While this simplification offers computational benefits, it discards structural information regarding the inherent relationship between amplitude and phase. In this paper, we propose a novel Boltzmann machine (BM), named PolarBM, capable of naturally handling complex-valued variables in the polar coordinate (i.e., an amplitude-phase representation). PolarBM defines a probability density function for complex variables in which the phase explicitly depends on the amplitude, thereby capturing the physically important relationships of complex-valued signals. Furthermore, to process audio signals in accordance with human auditory perception, we propose LogPolarBM, which models amplitude on a logarithmic scale. This extension yields a flexible conditional probability density function, a power-weighted noncentral complex Gaussian (PW-NCCG) distribution, whose marginal amplitude distribution encompasses the Rice, Nakagami, and noncentral chi distributions as special cases. For practical applications, we also introduce the restricted variants of these proposed models: PolarRBM and LogPolarRBM. Experimental results demonstrate that by explicitly modeling the dependency between amplitude and phase, the proposed RBMs achieve superior modeling accuracy compared to conventional models, including deep neural networks. Although our experiments focus on audio signals, the utility of the proposed BMs is not limited to audio applications; their potential extends widely across various fields of science and engineering that involve complex-valued data, such as wireless communications and quantum mechanics.

---


### 120. [DeGuNet: Depth-Guided Ultra-Compact Backbones for Efficient LiDAR-Camera 3D Detection](https://arxiv.org/abs/2607.12419)

**<font color=#1a73e8>作者：</font>** Haifa Zhang, Yijing Wang, Peixi Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In autonomous driving perception, the fusion of LiDAR and camera modalities has become the dominant paradigm for 3D object detection. However, current multi-modal frameworks heavily rely on massive visual backbones pretrained on 2D semantic tasks. This reliance introduces substantial parameter redundancy and a structural misalignment, as 2D priors are ill-equipped to handle the extreme sparsity of LiDAR projections required for Bird's-Eye-View geometry. To address this, we present DeGuNet, an ultra-compact and plug-and-play image backbone explicitly designed for depth-guided representation learning. By incorporating sparsity-aware feature extraction mechanisms, DeGuNet effectively aligns multi-view images with unstructured LiDAR depth while strictly preventing invalid-region contamination. Extensive experiments on the nuScenes dataset demonstrate DeGuNet's broad plug-and-play applicability and superior efficiency. When integrated into established baselines, it fundamentally eliminates architectural redundancy, reducing GPU memory consumption by up to 66.5% and achieving a 1.16x inference speedup. Concurrently, DeGuNet delivers up to a 6.20 absolute mAP gain, establishing a new paradigm for parameter-efficient multi-modal 3D perception.

---


### 121. [Accepted Prefixes Are Not All You Need: A Negative Result on PEFT-Based Block-Diffusion Drafting](https://arxiv.org/abs/2607.12422)

**<font color=#1a73e8>作者：</font>** Abdurrahman Javat, Allan Kazakov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive language model inference by using a cheap drafter to propose multiple future tokens and a target model to verify them. A common design goal is therefore to improve draft quality while reducing auxiliary parameters and systems overhead. We study a negative result for this direction through PEFT-BD, a same-backbone speculative decoding method in which a LoRA-like adapter acts as a block-diffusion drafter for an autoregressive verifier. PEFT-BD is motivated by several attractive properties: it avoids tokenizer mismatch, avoids loading a separate draft model, adds only a small number of trainable parameters, and uses a BD3LM-style denoising objective to propose a block of tokens in parallel. Despite these advantages, PEFT-BD does not yield a practical speedup in our Qwen3-0.6B experiments. Although the method obtains nontrivial accepted prefixes, profiling shows that each speculative step requires an adapter-enabled full-backbone draft pass followed by an adapter-disabled full-backbone verification pass. Thus, the drafter is parameter-efficient but not compute-efficient. Our results isolate a simple but important condition for successful speculative decoding: the drafter must be substantially cheaper to execute than the verifier. Longer accepted prefixes alone cannot compensate when draft computation remains verifier-scale.

---


### 122. [Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents](https://arxiv.org/abs/2607.12428)

**<font color=#1a73e8>作者：</font>** A H M Nazmus Sakib, Dipayan Banik, Murtuza Jadliwala  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing adoption of autonomous coding agents accelerates software development but also introduces scoped security risks within high-impact file paths that can outpace traditional human review capacity. While prior research has primarily evaluated these systems in terms of functional correctness and productivity, this paper presents a large-scale empirical study using the AIDev dataset to systematically characterize security code smells in agent-generated pull requests (PRs). Through a combination of a validated LLM-as-a-judge framework and manual qualitative analysis, we identify and classify security misconfigurations across 16,112 file changes spanning 4,022 pull requests. Our results reveal that 38.9% of agent-generated PRs contain at least one security smell, with supply chain integrity issues accounting for 82.3% of all detected security smells. Furthermore, hard-coded credentials constitute 99.6% of all critical-severity security smells. Crucially, we find that human collaborators are responsible for introducing 67.6% of genuine leaked secrets within these agent-assisted workflows, while existing automated and human review processes fail to detect 81.1% of these credentials prior to integration. These findings highlight substantial security risks in agent-assisted software development workflows and suggest a potential reduction in developer vigilance. They also underscore the urgent need for context-aware security guardrails implemented directly at the point of human-AI collaboration.

---


### 123. [More Than Where You Are: Learning Semantics, Structure, and Geometry from Cross-View Localization](https://arxiv.org/abs/2607.12429)

**<font color=#1a73e8>作者：</font>** Mao Chen, Xiangkai Zhang, Zhiyong Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Consistent cross-view understanding under extreme viewpoint changes is essential for spatial intelligence, as it enables models to recognize the same scene across extreme viewpoint gaps. Cross-view localization naturally provides a promising pathway toward this ability, as it requires a model to align ground-view imagery with geo-referenced satellite-view imagery despite drastic appearance changes to estimate camera poses. Recent visual foundation models have made this long-standing localization problem increasingly feasible by providing rich 2D representations for cross-view matching. However, we argue that cross-view localization should not be viewed merely as 2D matching or pose estimation. In this work, we revisit cross-view localization as more than pose estimation and investigate how it can help the model develop consistent cross-view understanding under extreme viewpoint changes, including stable semantics, reliable structure, and transferable geometry. We identify three key limitations of existing methods that prevent them from achieving this. They usually lack explicit 3D grounding, rely on strict point-wise matching that can weaken semantic consistency, and learn from an absolute objective that provides limited guidance for geometric reasoning. To address these limitations, we propose CROSS, a unified cross-view localization framework built upon 3D-grounded alignment, structure-aware matching, and hypothesis ranking. This formulation makes structure learning an intrinsic requirement, encourages semantic representations to remain stable, and enables the model to acquire transferable geometry. Extensive experiments on the KITTI and VIGOR datasets show that CROSS achieves state-of-the-art performance in cross-view localization. More importantly, CROSS effectively learns stable semantics, reliable structure, and transferable geometry across extremely different viewpoints.

---


### 124. [ARDepth: Auto-regressive Monocular Depth Estimation with Progressive Visual Conditioning](https://arxiv.org/abs/2607.12433)

**<font color=#1a73e8>作者：</font>** Zijie Wang, Wei Zhang, Weiming Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently become the dominant paradigm for monocular depth estimation (MDE). However, they implicitly assume that depth can be recovered as a globally smooth field through iterative denoising, which does not explicitly reflect the piecewise and scale-dependent organization of scene geometry. In practice, geometric structure emerges progressively across spatial scales, where coarse layout, surfaces, and boundaries are constructed in a hierarchical manner. Motivated by this observation, we introduce ARDepth, which formulates depth estimation as structured auto-regressive generation. Instead of recovering depth through global refinement, ARDepth progressively constructs depth representations as spatial resolution increases. To support this generative process, we introduce Scale-Progressive Conditioning (SPC) to inject multi-scale visual features at each generation stage, and Semantic-Aware Guidance (SAG) to provide scene-level semantic priors that enhance global structural consistency. Together, these designs enable the model to capture fine-grained local details while maintaining coherent global geometry. Empirical results demonstrate that our approach achieves strong performance and produces structurally consistent depth predictions across scales, validating auto-regressive generation as a promising alternative paradigm for geometric modeling.

---


### 125. [Fisher Rank Inflation: A Spectral Signature of Memorization under Label Noise](https://arxiv.org/abs/2607.12438)

**<font color=#1a73e8>作者：</font>** Satwik Bathula, Anand A. Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep networks trained with label noise often learn clean structure before memorizing corrupted labels. We show that this transition leaves a spectral signature in the centered scatter of per-example last-layer gradients. Its effective rank transiently expands during memorization and contracts after corrupted labels are fit. We call this phenomenon Fisher Rank Inflation. Corrupted labels increase effective rank by injecting spectral mass into low-energy or previously unused eigendirections, increasing the entropy of the gradient spectrum. We derive a first-order leave-one-out attribution formula, identify conditions under which corrupted examples contribute more strongly than clean examples, and explain why attribution signals weaken once the normalized Fisher-gradient spectrum stabilizes. We test these predictions on CIFAR-10, CIFAR-100, and CIFAR-10N using SmallCNN, ResNet18, and Vision Transformers. Across settings, Fisher effective rank exhibits a consistent inflation--collapse trajectory aligned with memorization. At peak-rank checkpoints, corrupted examples are enriched among the highest rank-contributing samples, with top-100 noisy fractions from \(69.2\%\) to \(96.2\%\) across five-seed synthetic-corruption experiments and \(94.4\%\pm1.9\%\) on CIFAR-10N. First-order spectral attribution closely matches exact leave-one-out contributions in convolutional models and remains enriched in the Vision Transformer. Peak effective rank increases monotonically with corruption severity, from \(28.88\pm1.95\) under clean training to \(97.09\pm1.78\) at \(60\%\) corruption. In several settings, the retrospectively identified onset of rank inflation precedes observable test degradation. These results establish Fisher Rank Inflation as a spectral signature connecting corrupted-example enrichment, corruption severity, and the transition from structure learning to memorization.

---


### 126. [WikiSTAR: A System for Shedding Light on the Hidden History of Scientific Wikipedia Articles](https://arxiv.org/abs/2607.12441)

**<font color=#1a73e8>作者：</font>** Omer Ehrlich, Nitzan Barzilay, Rona Aviram 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Wikipedia plays a key role in shaping public understanding of science, and its openly accessible revision history is a unique record of how scientific knowledge evolves over time. Yet scientifically meaningful revisions are obscured by the sheer volume of routine edits, leaving each article's scientific history hidden. We present WikiSTAR (Scientific Tracking of Article Revisions), an interactive system for exploring scientifically meaningful changes across an article's revision history. Using an LLM classifier with an expert-designed multi-label taxonomy, WikiSTAR first tags edit types such as the addition of technical terms, new research findings, and changes in scientific narrative. Then, through interactive views, an article's full revision history can be traced at any granularity - from aggregate trends that reveal when and in which sections scientific content was added or refined, down to individual edits - showing how scientific knowledge develops at a scale previously impossible. In a user study, experts from three domains found that WikiSTAR surfaced new patterns and research questions and enabled previously impractical analyses. We release our system, code and a human-annotated benchmark.

---


### 127. [Language Identification with Succinct Machine-Independent Traces](https://arxiv.org/abs/2607.12443)

**<font color=#1a73e8>作者：</font>** Moses Charikar, Jon Kleinberg, Chirag Pabbaraju  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Motivated by the power of large language models, there has been renewed interest in the Gold-Angluin model of language identification in the limit, with an eye toward variants of the model that might overcome the negative results for its original formulation. Recent papers on this question have proposed looking at computational traces and annotations of training strings as a source of additional power for a learner, reflecting empirical regularities such as the way that commented source code is easier to learn from than arbitrary source code, and text annotated with algorithmically generated chain-of-thought tokens can be easier to learn from than the raw text itself. This recent work has shown positive results for language identification in the presence of such computational traces, but the traces in these positive results come from explicit automata-theoretic machine models that generate the language, where the underlying vocabulary of tokens for the traces is very large. In this paper, we address two fundamental issues left open by this line of work: can we achieve positive results with traces that use only a small alphabet, and can we define traces directly from the language itself, without requiring an underlying machine model that generates it? We establish positive results for both of these questions: for an arbitrary collection of languages, we show how to define computational traces that enable identification in the limit, using an alphabet of tokens that is linear in the size of the alphabet that the languages are defined over, and independent of any other properties of the languages.

---


### 128. [Let RGB Be the Language of Vision](https://arxiv.org/abs/2607.12450)

**<font color=#1a73e8>作者：</font>** Timing Yang, Jinrui Yang, Xinlong Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work introduces a unified formulation for vision models, where diverse forms of visual information beyond natural images, such as masks, depth maps, and other structured visual signals, are all represented as RGB images, while general visual tasks can be converted into a common RGB-to-RGB image editing problem. In this paradigm, different types of visual information internally share the same encoding and decoding architecture and parameters as natural images, enabling a single model to transfer across tasks through a unified visual interface, in a way analogous to how language models operate over text. We refer to this formulation as RGB In and RGB Out (RINO). Built upon a generic image editing backbone without task-specific fine-tuning, RINO demonstrates robust and competitive zero-shot performance on both dense understanding tasks such as segmentation and depth estimation (where we unify outputs as RGB), and dense-conditioned generation tasks such as pose-to-image generation (where we unify inputs as RGB). We hope this study provides useful insights toward general unified vision-language systems, where diverse visual tasks can be expressed, interpreted, and solved through a shared visual language. Code is available at this https URL.

---


### 129. [Do We Really Need Transformers for Global Spatial Information Extraction in Traffic Forecasting?](https://arxiv.org/abs/2607.12462)

**<font color=#1a73e8>作者：</font>** Qihang Zhang, Siyao Zhang, Letao Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing traffic forecasting models commonly focus on extracting spatial dependencies, particularly global spatial information, which characterizes the representations obtained through interactions between each individual node and all nodes across the traffic network. However, the underlying mechanism by which such global information is modeled and extracted remains insufficiently investigated. Whether global information must be extracted by high-degree-of-freedom adaptive attention or can be captured by a simple global aggregation operator remains unclear. For this purpose, we design a controlled ablation framework that replaces only the spatial mixing module to test attention-based global interaction. Across six traffic benchmarks, uniform full-range mixing and standard spatial attention each achieve lower MAE on three datasets, with only a 0.14% difference in mean MAE, while the former reduces node-scale spatial mixing complexity from O(N2) to O(N). Mechanism analysis further decomposes spatial attention into a row-uniform global background and a non-uniform residual. The residual shows dataset-dependent marginal value, suggesting that spatial attention should be justified by stable gains beyond a row-uniform global background. The corresponding source code is publicly available at: this https URL

---


### 130. [Steering Diffusion Models via Class-Contrastive Influence for Few-Shot Medical Classification](https://arxiv.org/abs/2607.12464)

**<font color=#1a73e8>作者：</font>** Jeeyung Kim, Erfan Esmaeili, Qiang Qiu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When labeled data are scarce, off-the-shelf diffusion models can augment training sets for few-shot medical image classification, but not all generated samples are equally useful for the downstream task. Existing approaches largely improve synthetic data by increasing realism, diversity, or domain adaptation, while overlooking a more fundamental question: how should sample usefulness for classification be measured and optimized? We address this with Class-Contrastive Influence (C2I), a criterion that quantifies a sample's usefulness through its gradient-based influence on the classifier. We find that effective samples exhibit a strong C2I gap: their loss gradients align with validation gradients from the same class and oppose those from other classes. Our analysis further suggests that such high-C2I samples are hard, boundary-proximal examples that help refine the decision boundary and improve robustness. Building on this insight, we fine-tune diffusion models with reinforcement learning using a C2I-based reward to steer generation toward class-informative samples. Across several few-shot medical imaging benchmarks, C2I-guided generation improves downstream accuracy and robustness over diffusion-based augmentation baselines, showing that synthetic augmentation is most effective when guided by task usefulness rather than image quality alone.

---


### 131. [Sample Efficient Generative Optimization for Molecular Design](https://arxiv.org/abs/2607.12488)

**<font color=#1a73e8>作者：</font>** Sarina Kopf, Cristina Nevado, Philippe Schwaller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular optimization in drug discovery, materials design, and catalysis requires searching vast chemical spaces under tight evaluation budgets, since high-fidelity oracles and experimental measurements are costly. The practical impact of an optimization method therefore hinges on its sample efficiency: how few evaluations it needs to find strong candidates. We introduce Sample Efficient Generative Optimization (SEGO), a framework for Bayesian optimization on adaptively generated molecules. In SEGO, a probabilistic surrogate model forms a hypothesis about where hits lie in chemical space, a generative model is steered to propose candidates in that region, the most promising candidate is selected via an acquisition function, and the resulting oracle call is used both to sharpen the surrogate and to anchor the generator in real reward. SEGO attains state-of-the-art performance on the practical molecular optimization (PMO) benchmark using only one tenth of the oracle calls consumed by other methods, and on a multiparameter docking task it reaches ten hits in roughly half the oracle calls of existing approaches. These gains move molecular optimization closer to campaigns driven by direct experimental feedback.

---


### 132. [RealSkin: Spatio-Spectral Partial Neural Adjoint Maps for Image-to-3D Attribute Transfer](https://arxiv.org/abs/2607.12495)

**<font color=#1a73e8>作者：</font>** Jing Li, Yawei Luo, Xiangze Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creating photorealistic 3D assets requires bridging the appearance gap between real-world observations and synthetic models. A promising approach is to transfer visual attributes from real images onto synthetic 3D surfaces. Traditional methods struggle with resolution mismatch and the inherent discreteness of point correspondences. In contrast, resolution-robust functional maps enable smooth attribute propagation but rely on near-isometry assumptions and topological consistency. To address these limitations, we propose RealSkin, a self-supervised framework that performs correspondence optimization in a learned spectral domain, guided by spatial correspondences. We first introduce a spatial-guided registration algorithm to establish coarse correspondences under severe topological discrepancies. To relax strict isometric assumptions and handle partial correspondences, we further design a spectral-aware neural adjoint network that incorporates partial correspondences into a neural function space and models non-isometric residuals for correspondence refinement. Experimental results demonstrate that our method achieves state-of-the-art performance on challenging real-to-synthetic scenarios. The code will be publicly released.

---


### 133. [Adversarial Attacks on Online Handwriting using Salience-based Temporal Editing](https://arxiv.org/abs/2607.12500)

**<font color=#1a73e8>作者：</font>** Yataro Tamura, Brian Kenji Iwana, Jiseok Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models for online handwriting recognition have been shown effective and are increasingly deployed in practical applications. However, their vulnerability to adversarial attacks is still a challenge. Existing adversarial methods are predominantly designed for image-based inputs and typically rely on additive spatial perturbations. When applied to online handwriting, which is inherently represented as a time series of pen trajectories, such perturbations often introduce high-frequency jitter and visibly unnatural stroke artifacts. In this work, we propose a novel adversarial attack framework for online handwriting recognition based on salience-guided temporal editing. Instead of adding noise, the proposed method generates adversarial examples by inserting and deleting points at time steps selected according to temporal salience, preserving the shape and smoothness of the original handwriting. Temporal salience is estimated using gradient-based activation mapping, which guides edits toward time steps that strongly support the original class prediction. We evaluate the proposed approach on the Unipen and CASIA-OLHWDB datasets under both white-box and one-shot black-box attack settings. Experimental results demonstrate that while conventional image-based attacks achieve strong white-box performance, they exhibit poor transferability across models. In contrast, the proposed temporal editing attack achieves stronger one-shot black-box transferability while preserving the visual structure of the handwriting. These results indicate that temporal editing is a relevant threat model for online handwriting recognition, particularly in one-shot black-box transfer settings.

---


### 134. [What Does Goodness Measure? A Likelihood-Ratio Account of Forward-Forward Learning](https://arxiv.org/abs/2607.12501)

**<font color=#1a73e8>作者：</font>** Paolo Giannitrapani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Forward-Forward (FF) algorithm trains each layer locally, so that a scalar goodness - the sum of squared activations - is high on real inputs and low on contrastive ones, with activations normalized between layers. Both choices are usually treated as heuristics. Under an explicit generative model they are not: the squared goodness is the sufficient statistic of a likelihood-ratio test between two zero-mean populations differing in scale, and the FF threshold is its boundary. It generalizes: anisotropic populations yield a Mahalanobis goodness, the plain square being its isotropic case; heavy-tailed populations yield a saturating statistic whose slope is a posterior precision - divisive normalization - with bounded evidence and an advantage only under aggregation. The same lens characterizes the inter-layer normalization: it must remove the length while preserving per-coordinate energy, explaining a depth collapse we observe under unit-norm normalization; and the pairwise objective admits a scale-inflation shortcut that a whitened goodness removes.

---


### 135. [On the Security Implications of PQC in TLS: Handshake Exhaustion and IDS Degradation](https://arxiv.org/abs/2607.12504)

**<font color=#1a73e8>作者：</font>** Lin-Fa Lee, Yi-Yu Chang, Chia-Mu Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-Quantum Cryptography (PQC) is increasingly being integrated into TLS 1.3 to enhance resilience against quantum-enabled attacks. However, the additional computational and communication overhead introduced by PQC primitives during the handshake phase may also amplify the impact of TLS handshake exhaustion attacks, leading to more severe Distributed Denial-of-Service (DDoS) threats.
In this study, we establish an empirical testbed consisting of one PQC-enabled TLS server and ten attacking nodes, generating over 16.5 GB of mixed traffic data that includes both legitimate browsing behavior and high-intensity handshake exhaustion attacks.
Experimental results show that PQC-TLS can prolong periods of sustained high CPU utilization on the server by up to 88 times, significantly amplifying the effectiveness of such attacks. Furthermore, we evaluate state-of-the-art deep learning-based Intrusion Detection Systems (IDS) and observe a substantial decline in attack detection performance under PQC traffic conditions.
In particular, exosphere achieves only around 50% recall, while HyperVision's AU-ROC degrades to near-random levels (0.49), revealing critical detection blind spots in existing IDS when operating in PQC environments.
The main contributions of this work are threefold: (1) we systematically quantify and analyze the root causes of IDS detection blind spots in PQC settings; (2) we publicly release a comprehensive PQC-DDoS hybrid traffic dataset, including precise attack timestamps and server-side resource monitoring data; and (3) we open-source all experimental code and AWS deployment scripts, enabling a fully reproducible cloud-based testing environment.
These resources aim to support both academia and industry in developing next-generation PQC-aware intrusion detection systems.

---


### 136. [Open-Source Intelligence and Music Information Retrieval for Geographic Attribution of Musical Affect and the Ecological Limits of Population Inference](https://arxiv.org/abs/2607.12517)

**<font color=#1a73e8>作者：</font>** Mohammadreza Rashidi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A common intuition holds that a region's music mirrors the temperament of its people, so that melancholic melodies mark melancholic populations. We test the measurable half of that intuition and reject the inferential half. Using the Essen Folksong Collection, a corpus of thousands of notated folk melodies, we extract real melodic and affect-related features from 2393 deduplicated melodies spanning 16 countries and 7 geographic regions, with the analysis performed on symbolic scores rather than audio. The mode of each melody is computed with a key-finding algorithm rather than read from the file, because the collection's own documentation warns its major and minor labels are unreliable. Cross-country differences in melodic structure are large and highly significant. All 8 tested features differ across countries at p<0.001, with the leap-related features reaching p<10^-90, and China carries a distinctive wide-leap, high-activity signature (arousal composite +1.24 standard deviations, mean absolute interval 2.77 semitones against Germany's 2.17). We then test the inferential half. We correlate the regional musical-affect measures with two published, validated national indices, the World Happiness Report ladder score and the Hofstede individualism index. None of the 6 correlations is significant (0 of 6). The geography of musical affect is real and measurable, but it does not predict how happy or how individualist a population is, and any claim that it does is an ecological fallacy. We release the full extraction and analysis pipeline, and a fail-closed checker re-derives every number in this paper from the data.

---


### 137. [OOD-RL-Bench: A Benchmark Framework for Out-of-Distribution Detection in Reinforcement Learning](https://arxiv.org/abs/2607.12523)

**<font color=#1a73e8>作者：</font>** Emil Mittag, Richard Dazeley, Peter Vamplew  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable reinforcement learning (RL) agents must maintain operational integrity amidst sensor malfunctions, dynamic disturbances, and slow environmental shifts. The detection of out-of-distribution conditions is pivotal to determining when an agent's observations, transitions, or trajectory dynamics deviate from the assumptions underpinning its policy training. Current out-of-distribution (OOD) detection benchmarks typically evaluate image classifiers or static low-dimensional datasets, failing to account for the complex, action-dependent temporal structure inherent in RL trajectories. To address this gap, we present OOD-RL-Bench, a comprehensive and extensible framework designed to evaluate OOD detectors against categories of anomalies injected into RL trajectories. Detectors and anomaly injectors are integrated through shared interfaces and configuration, which allows new scoring methods and perturbation families to be evaluated without modification of the core benchmark loop. We evaluate the utility of the framework using a Deep Q-Network policy within the LunarLander-v3 environment. We assess the performance of each detector across a suite of anomaly types using matched-time AUROC, matched-time AUPRC, matched-time false-positive rate, detection delay, and segmented-onset metrics. Our analysis reveals significant performance variance across anomaly types: observation perturbations and regime switches are identified with high accuracy by several methods, while observation delay and action-conditioned dynamics remain difficult even when post-onset anomaly scores are compared against clean scores from the same timesteps. We make the framework, trained policy checkpoint, and complete results publicly available as a reproducible artefact.

---


### 138. [Open-Source Intelligence for Code Provenance and the Security Patterns that Separate Human and Large-Language-Model Implementations of Common Programming Tasks](https://arxiv.org/abs/2607.12524)

**<font color=#1a73e8>作者：</font>** Mohammadreza Rashidi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Developers now draw code from two very different sources, the accumulated human answers on sites such as Stack Overflow and the output of large language models. We ask two questions about that split. First, can the provenance of a code snippet be recovered from the code itself, and second, do the two sources differ in the security patterns they adopt for the same task. Using only open sources, a public gateway of open-weight language models and the public Stack Overflow API, we build a fully reproducible pipeline that collects real implementations of 31 security-sensitive programming tasks, among them OAuth with PKCE, JWT verification, password hashing, and SQL access, from 9 language models and from human answers, and scores every sample with deterministic security and style detectors. On 528 real samples we train a cross-validated classifier that recovers human versus model provenance with 93 percent accuracy against a 78 percent baseline, and a 7-way classifier that attributes a sample to the specific model that wrote it at 48 percent. We then report where the sources diverge on security, which patterns models adopt more often than the human corpus and which they inherit from it. Running the same tasks in Python, JavaScript, Go, and Java, we find the security divergence holds in every language while the provenance boundary is partly language-specific and does not transfer symmetrically between them. A vulnerability repair case study, in which models are handed insecure code and asked to fix it, finds a 77 percent repair rate across 21 seeds and 12 weakness classes, but a recurring partial-fix failure in which the model removes the insecure pattern without adding the correct defense. The pipeline is data driven, so any new task or language is added as a single specification entry, and a fail-closed checker re-derives every number in this paper from the stored data.

---


### 139. [From Preimage Search To Source-Grounded Feature Inversion](https://arxiv.org/abs/2607.12526)

**<font color=#1a73e8>作者：</font>** Kaixiang Shu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpreting a neural network requires understanding what its internal features extract from a particular input. Feature inversion seeks to express a selected feature in the input domain, but canonical iterative methods search for an input whose re-encoded representation matches the target. Because many inputs can satisfy this constraint, target matching alone does not specify the inverse associated with the sample that generated the feature. We formulate source-grounded feature inversion by conditioning the inverse on the source-local network geometry at the target-generating input. At each boundary of the computational DAG, backpropagation provides the correct reverse dependencies but transports an adjoint signal rather than an upstream-state estimate. We locally repair this signal with a closed-form matrix Wiener map from a mean-seed VJP to the upstream state, followed by a second Wiener map for the JVP forward-consistency residual, and compose the repaired states through the same DAG in one finite reverse pass. One calibrated zero-intercept map family supports new inputs, depths, channels, and channel groups across diverse CNN and Transformer architectures, tensor components, and visual distributions without query-specific optimisation. Matched target and source controls verify that each inverse depends on the selected feature and the local operators of the sample being explained, rather than a target-independent image template. Prediction-conditioned feature atlases align these visualisations with independent interventions on the corresponding internal features. Together, source-grounded feature inversion opens the model's hidden feature hierarchy to inspection at the level of individual layers and channels, linking what the network extracts from an input to the internal evidence that shapes its decision.

---


### 140. [Evidence-Grounded AI for Musculoskeletal Care](https://arxiv.org/abs/2607.12527)

**<font color=#1a73e8>作者：</font>** Wenjie Li, Yujie Zhang, Fanrui Zhang 等 37 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Musculoskeletal diseases are among the leading causes of disability worldwide and create the greatest global need for rehabilitation. Because recovery, remodelling and degeneration often unfold over months to years, musculoskeletal care requires longitudinal management that repeatedly integrates evolving patient evidence, external medical knowledge and stage-specific functional goals. In routine practice, this evidence is fragmented across visits, departments and hospital systems, limiting individualized, evidence-based care. Here we report OrthoPilot, a clinical artificial intelligence system powered by a large language model that integrates hospital data streams with authoritative external knowledge for continuous musculoskeletal management. OrthoPilot autonomously retrieves real-time imaging, laboratory, pathology and order data and converts evolving patient states into evidence-based decisions from admission diagnosis to rehabilitation planning. We established a specialist-validated benchmark from real-world electronic health records spanning 1,000 disease codes. In a reader study across the complete care pathway, OrthoPilot was compared with 81 orthopaedic physicians and surpassed experts with 25 years of experience in diagnostic reasoning, clinical decision-making and management planning. It also outperformed all evaluated intelligent systems across 60 external clinical centres. In a prospective study of 1,870 complex cases, OrthoPilot increased full-chain management success by 10.6%. During an 8-month randomised deployment involving 8,240 inpatients, it increased cumulative cases per bed by 9.7% and improved patient-reported access to health information. These results move clinical AI from predicting isolated events toward executing longitudinal management across complete musculoskeletal care pathways.

---


### 141. [DiTailed: Ensuring Visual Object Consistency in Text-Image-to-Image Flow Matching Models](https://arxiv.org/abs/2607.12539)

**<font color=#1a73e8>作者：</font>** Francesco Taioli, Daniel Coelho, Iaroslav Melekhov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite remarkable progress in text-guided image editing, generative models frequently fail to preserve visual object consistency, defined as the preservation of a subject's key attributes throughout the editing process. We address this limitation through three contributions. First, we introduce ABO-Edit, a dataset specifically designed to study object consistency, comprising over 12,000 triplets of source images, editing prompts, and high-quality target images rendered from artist-designed 3D assets, with multi-view coverage and human-verified quality control. Second, we uncover an overlooked property of image-editing rectified flow models: the conditioning embedding space, not directly supervised during training, encodes a prediction of the final generated image even at high noise levels. Third, exploiting this finding, we propose FlowMirror, a parameter-free auxiliary loss that supervises this conditioning embedding space. Without architectural changes, our method improves generation quality across several metrics over baselines.

---


### 142. [Edge-Aware Thermal Infrared UAV Swarm Tracking](https://arxiv.org/abs/2607.12544)

**<font color=#1a73e8>作者：</font>** Yu-Hsi Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal infrared (TIR) imaging is essential for UAV swarm operations in visually degraded environments. However, tracking tiny UAVs remains challenging due to limited appearance cues, frequent occlusions, and rapid maneuvers. Despite significant progress driven by benchmarks such as the Anti-UAV challenge, existing methods primarily prioritize accuracy while overlooking the computational constraints of real-time edge deployment. The standard Kalman Filter (KF) offers the efficiency required for edge devices, yet its constant-velocity assumption often breaks down under highly dynamic UAV motion and thermal sensor jitter. More sophisticated nonlinear estimators can improve robustness but often introduce additional computational costs. To address this gap, we propose an edge-aware online tracking pipeline centered on the Adaptive Kinematic Kalman Filter (AKKF), which augments the linear KF with state-dependent kinematic modeling while preserving real-time efficiency. Combined with transient false-positive suppression and kinematics-driven predictive coasting, the presented pipeline improves trajectory continuity under challenging TIR conditions. Experiments on the Beyond Strong Baseline (BSB) benchmark provide a starting point for edge-aware UAV tracking by jointly evaluating tracking performance and computational efficiency, offering insights toward future real-time deployment.

---


### 143. [VanillaBench: The Hidden Accuracy Cost of Adversarial Robustness](https://arxiv.org/abs/2607.12545)

**<font color=#1a73e8>作者：</font>** Niklas Bunzel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversarial robustness research has produced hundreds of defended models over the past decade, yet the literature almost universally reports robustness results in isolation: standard (clean) accuracy and adversarial accuracy of the robust model are shown, but the gap to the corresponding vanilla model is rarely quantified. We introduce VanillaBench, a systematic benchmark that makes this gap explicit. For every adversarially-trained model catalogued by RobustBench across four threat models, we compute the accuracy difference against multiple vanilla references from Papers with Code, computed over both all entries and no-extra-data entries, the best vanilla model as of the robust model's publication year, and an architecture-matched baseline. Across all 186 robust models, the mean delta clean relative to the best vanilla model ranges from -7.7 to -29.5 percentage points, and even the single most robust model per track still trails its temporal vanilla counterpart by 4.0-21.0 points. The architecture-matched comparison, which isolates the effect of adversarial training from architectural differences, reveals a mean gap of -3.5 to -17.5 points. Restricting this architecture-matched comparison to models whose vanilla accuracy is known for the exact same architecture, rather than approximated from a related one, narrows the gap to -4.0 to -14.0 points. These results demonstrate that the robustness-accuracy trade-off is substantially larger than what is typically conveyed by individual papers. This information is critical for practitioners and decision-makers. When deploying models in real-world settings, the accuracy cost of robustness directly affects business outcomes, yet current publications do not provide the vanilla baseline needed to assess it. We argue that future robustness evaluations should report vanilla-referenced accuracy gaps as a standard component.

---


### 144. [CGRL: Concept-Guided Pruning and Representation Learning for Whole-Slide Image Classification](https://arxiv.org/abs/2607.12556)

**<font color=#1a73e8>作者：</font>** Thuc Huynh, Tuan Le, Doanh C. Bui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised whole-slide image (WSI) classification is widely used in computational pathology because slide-level labels are easier to obtain than dense region annotations. Existing multiple instance learning (MIL) methods often aggregate large bags of patch embeddings using mainly visual cues, which can retain many non-informative patches and provide weak alignment between instance features and class-level disease semantics. We propose Concept-Guided Pruning and Representation Learning (CGRL), a simple framework that introduces class-level concept prototypes derived from disease prompts into the MIL pipeline. First, concept-relevance pruning ranks patch instances by their similarity to class concepts and retains the top-K concept-relevant patches for downstream MIL aggregation. Second, concept-guided contrastive representation learning constructs class-wise positive and negative patch sets from the same similarity matrix and optimizes target-class, symmetric auxiliary, and cross-class separation objectives, thereby regularizing the projected concept space. We evaluate CGRL on TCGA-BRCA and TCGA-NSCLC using multiple representative MIL methods. Experimental results show that CGRL improves several model-dataset combinations, with gains depending on the downstream MIL model and dataset. It achieves particularly clear improvements in accuracy and macro-F1 while reducing computational cost through concept-relevance pruning. These findings demonstrate that class-level semantic concepts provide an effective and practical prior for patch selection and representation learning in weakly supervised computational pathology.

---


### 145. [Traceback Translators Against Forgetting in Continual Fake Speech Detection](https://arxiv.org/abs/2607.12569)

**<font color=#1a73e8>作者：</font>** Enrico Gottardis, Mattia Tamiazzo, Simone Milani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fake speech detectors are increasingly challenged by the development of new and more accurate generative models. To cope with this problem, continual learning techniques are nowadays widely considered feasible strategies for updating models to new datasets, but they also lead to decreased performance on previously seen samples (catastrophic forgetting). In this work, we propose a forgetting-resilient solution based on the adoption of domain translators within a frozen detector, which remaps the new feature spaces into the original ones by means of a traceback translator network. Experimental results show that this strategy enables the achievement of high detection rates with respect to traditional retraining, while minimizing the computational effort and preserving the detection accuracy on previous data.

---


### 146. [Vertical Standardisation for High-Risk AI Systems under the EU AI Act: A Domain-Specific Framework for Algorithmic Hiring](https://arxiv.org/abs/2607.12588)

**<font color=#1a73e8>作者：</font>** Anna Gatzioura, Vrettos Moulos, Nina Baranowska  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> According to the recent European legislation, high-risk AI systems will have to adapt in order to comply with requirements related to specific areas, like risk management, data quality and governance, logging and traceability, technical documentation, transparency, human oversight, and accuracy, as outlined in the European Artificial Intelligence (AI) Act. As the standardisation process for AI is expected to remain iterative and, so far, there are no European standards on AI fully covering the challenges of algorithmic hiring, we propose specific standardisation-oriented recommendations related to the relevant AI areas specified by the European Commission. For each of these areas, we set the context by describing the requirements that AI systems in high-risk domains, and especially in recruitment, should fulfil, as well as the activities that should be carried out to ensure their appropriate use and desired performance, in line with the requirements deriving from the AI Act. Unlike existing horizontal approaches to AI governance and standardisation, this paper contributes a vertical, domain-specific framework for algorithmic hiring, and especially ranking-based recruitment systems, by mapping the requirements of the AI Act to concrete standardisation recommendations, focusing on lifecycle discrimination risks, fairness-aware data governance, explainability, human oversight, and post-deployment monitoring in recruitment systems. Even though our recommendations were informed by the outcomes of the European project FINDHR, they are not tied to the project's technical artefacts and could be implemented using alternative methods, tools, or governance mechanisms.

---


### 147. [WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction](https://arxiv.org/abs/2607.12592)

**<font color=#1a73e8>作者：</font>** Li Hu, Guangyuan Wang, Peng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present WanToFight, a generative game engine that simulates real-time, two-player The King of Fighters '97 (KOF~'97) gameplay from keyboard input. Prior generative game engines target either single-player first-person settings or non-real-time cooperative scenarios; multi-player control, real-time inference, complex physical interaction, and adversarial gameplay have not been jointly addressed. WanToFight closes this gap with three components built on the Wan-1.3B video diffusion transformer: a streaming autoregressive generator with block-causal attention and a rolling KV cache; a visually grounded Player Association module that binds each player's keyboard signal to a character identity; and a gated, locally causal keyboard injection module trained with a single-player-to-full-gameplay curriculum. A four-step DMD-distilled student paired with a pruned VAE decoder sustains 30FPS at 512x384 on a single NVIDIA RTX 5090 over the duration of a complete match. To our knowledge, WanToFight is the first generative game engine to combine multi-player control, real-time inference, complex physical interaction, and adversarial gameplay in one system.

---


### 148. [Lightweight Multi-Scale Anomaly Detection for Resource-Constrained Edge Devices](https://arxiv.org/abs/2607.12599)

**<font color=#1a73e8>作者：</font>** Raheen Junaid Wani, Smruti R. Sarangi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series anomaly detection is increasingly important in IoT systems, sensor networks, and edge monitoring applications, where models must operate under strict constraints on memory, latency, and power consumption. While recent deep-learning approaches have improved detection accuracy, many remain computationally expensive and often fail to capture subtle anomalies due to limited multi-scale sensitivity. Autoencoders are widely used for anomaly detection because they reconstruct normal patterns well, leading to elevated reconstruction errors for anomalous inputs. Their simplicity and efficiency also make them suitable lightweight backbones for handling multi-scale inputs. To address these challenges, we propose a Lightweight MultiScale AutoEncoder (LMSAE) network for univariate time-series anomaly detection, designed to be compact and computationally efficient. LMSAE leverages the Discrete Wavelet Transform (DWT) to extract multi-scale features and employs a multi-scale loss function to improve sensitivity to subtle or hidden anomalies. Experiments on benchmark datasets demonstrate competitive or superior detection performance despite using significantly fewer parameters and a model size of less than 500 KB. LMSAE also achieves low-latency, low-power inference on the NVIDIA Jetson Nano, with 9x reduction in inference latency and 2x reduction in power consumption, making it ideal for edge deployment.

---


### 149. [Decouple and Reason: Anatomically Guided Two-Stage Voxel-Level Grounding of Free-Text Findings in 3D Chest CT](https://arxiv.org/abs/2607.12602)

**<font color=#1a73e8>作者：</font>** Kwang-Hyun Uhm, Inhwa Son, Sung-Jea Ko  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic voxel-level grounding of free-text findings in 3D chest Computed Tomography (CT) is critical for clinical interpretability. However, this task remains highly challenging due to the intricate spatial complexity of large 3D volumes and the heterogeneity of free-text findings. Existing end-to-end approaches often struggle to simultaneously learn the localized feature representations required for accurate 3D segmentation and the complex semantic understanding needed for text alignment, leading to suboptimal grounding performance. To overcome this fundamental limitation, we propose a novel decoupled framework that disentangles the problem into two specialized stages: (1) class-agnostic lesion segmentation and (2) text-volume reasoning. This structural separation allows the model to first extract candidate sub-volumes by localizing potential abnormalities. Subsequently, intensive cross-modal reasoning is performed to align these localized sub-volumes with free-text medical findings. To resolve the spatial ambiguities inherent in local regions, the reasoning module is augmented with explicit anatomical guidance, utilizing relative spatial coordinates and lung lobe priors. Evaluated on the ReXGroundingCT benchmark, our method achieves state-of-the-art performance in overall grounding quality on the official leaderboard. These results demonstrate that decoupling detection from reasoning is a highly effective paradigm for handling the complexity of 3D medical visual grounding. Our code is publicly available at this https URL.

---


### 150. [Translation as a Computationally Efficient Bridge: Feasibility of English BERT for Low-Resource Languages](https://arxiv.org/abs/2607.12612)

**<font color=#1a73e8>作者：</font>** Hielke Muizelaar, Giulia Rivetti, Marco Spruit 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> BERT models have revolutionised Natural Language Processing (NLP) through their ability to process unstructured text across diverse domains. However, developing high-quality BERT models for non-English languages remains challenging due to limited annotated data and high computational demands. Translating non-English data into English and fine-tuning existing English BERT models offers a resource-efficient alternative, yet few studies have structurally compared translation-based fine-tuning with native-language BERT performance across tasks and languages. This study provides such a comparison, evaluating the feasibility of translation-based fine-tuning across six NLP tasks: Sentiment Analysis, Hate Speech Detection, Question Answering, Named Entity Recognition, Part-of-Speech Tagging, and Natural Language Inference, using datasets translated from Bulgarian, Chinese, Dutch, Italian, and Russian. Across all settings, the translation-based approach was comparable or superior in 53.3 percent of cases. Gains were most frequent in Question Answering, Part-of-Speech Tagging, and Natural Language Inference, while performance declines were common in Named Entity Recognition and Hate Speech Detection. The results show that translation-based fine-tuning is most effective for tasks relying on syntactic or structural patterns and for languages typologically close to English, such as Dutch, but less effective for token-level or culturally nuanced tasks, particularly in Chinese. Overall, this study demonstrates that translation-based fine-tuning offers a scalable, resource-efficient, and empirically validated path for extending NLP to low-resource languages while advancing linguistic inclusivity and sustainability in artificial intelligence.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-203](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
