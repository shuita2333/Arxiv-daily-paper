# 📦 其他研究 | 2026年07月28日

> 本类共 **169** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-169](./part-04.md)

---

### 101. [A Leakage-Free Stacked Ensemble Method for Multiclass Classification](https://arxiv.org/abs/2607.22081)

**<font color=#1a73e8>作者：</font>** S. P. Sharmila, Aruna Tiwari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multiclass classification is a fundamental problem across a wide range of domains. It is still challenging due to possession of high inter-class similarity, class imbalance datasets, and variability in data distributions. Rule-based classifiers such as XGBoost often achieve stronger performance on structured features, but they are limited in capturing smooth functional relationships among variables. Similarly, neural network models can represent complex nonlinear interactions but frequently suffer from overfitting and generalization issues. To address these limitations, we propose LFS-FRAME, a Leakage-Free Stacked ensemble framework that integrates functional learning using Kolmogorov-Arnold Networks (KAN) and rule-based learning via XGBoost for robust multiclass classification.
The proposed framework constructs unbiased meta-features by employing a strict out-of-fold stacking strategy to ensure complete isolation between training and validation data hence preventing performance leakage. By learning over probabilistic outputs from heterogeneous base learners, the meta-classifier effectively exploits both global functional patterns and sharp decision boundaries present in the complex data. Experimental evaluations on multi-class datasets demonstrate that LFS-FRAME improves performance metrics, and overall accuracy is 89.85% in identifying major families and 81.74% in identifying sub-families relative to strong single-model baselines. These results highlight the effectiveness of leakage-free functional and rule-based stacking for reliable and generalizable multiclass classification.

---


### 102. [FAIR: Feature-Augmented Implicit Regularization for AI-generated Fake Image Detection](https://arxiv.org/abs/2607.22087)

**<font color=#1a73e8>作者：</font>** Md Redwanul Haque, Manzur Murshed, Manoranjan Paul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalization remains a critical bottleneck in AI-generated image detection. Because many modern generators are proprietary or adversarially modified, existing detectors overfit to the low-level textural patterns of accessible training data, resulting in severe failures on unseen domains. Conventional regularization techniques (e.g., $L_1$/$L_2$ norms, Dropout) apply indiscriminate parametric constraints and fail to provide the domain-invariant structure necessary for cross-generator robustness. To address this, we propose Feature-Augmented Implicit Regularization (FAIR). FAIR introduces an orthogonal, macro-structural prior, specifically, Scene Composition Structure (SCS), during training to geometrically constrain the model's optimization trajectory. By augmenting the primary feature space with domain-invariant SCS features, FAIR explicitly penalizes texture-biased shortcut learning. Crucially, this structural prior is entirely discarded at inference, yielding a smoothed, generalized decision boundary with zero architectural or computational overhead. Extensive evaluations across five massive benchmarks demonstrate that integrating FAIR into state-of-the-art detectors significantly improves cross-generator generalization, boosting accuracy by up to 8.04% and establishing new state-of-the-art robustness in zero-shot transfer scenarios.

---


### 103. [Spectral Prior for Reducing Exposure Bias in Diffusion Models](https://arxiv.org/abs/2607.22091)

**<font color=#1a73e8>作者：</font>** Yuya Kobayashi, Masato Ishii, Yuhta Takida 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models typically suffer from error accumulation during iterative sampling, commonly referred to as exposure bias. We reveal systematic frequency-dependent discrepancies between training and inference, which can be interpreted as frequency-dependent SNR error. Crucially, the direction of this mismatch varies across models and timesteps, indicating that fixed correction rules do not generalize. We propose Spectral Alignment (SPA), a lightweight, guidance-based method that calibrates the power spectrum of intermediate predictions to a pre-computed prior. Our approach consists of two stages: (1) offline fitting of a parametric spectrum model from training data, and (2) inference-time guidance via efficient FFT-based gradient computation. SPA introduces minimal computational overhead (3-4\%) and is complementary to Classifier-Free Guidance (CFG). We demonstrate consistent improvements across diverse architectures, from pixel-space models (DDPM, ADM) to latent diffusion models (SD2.0, SDXL) and flow-matching models (SD3.5, FLUX). Our implementation is available at this https URL.

---


### 104. [Transforming Keystroke Noise to Text: Self-Supervised Acoustic Eavesdropping Attacks on Keyboards](https://arxiv.org/abs/2607.22094)

**<font color=#1a73e8>作者：</font>** Atsunori Okada, Akira Ito, Rei Ueno 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a self-supervised acoustic eavesdropping attack that reconstructs typed text solely from keystroke sounds, without requiring labeled data for the target device. The proposed attack enables stealthy eavesdropping in two real-world scenarios-physical spaces (public and semi-public) and online meetings. Our method combines unsupervised acoustic clustering with Transformer-based language model inference and iterative self-training, enabling stable character inference under highly uncertain acoustic-to-character mappings. We demonstrate that the proposed method achieves over 99% reconstruction accuracy with only 100-150 observed keystrokes under a close-proximity recording setup using a smartphone placed near the target device, significantly outperforming prior unsupervised baselines in low-data regimes. We further evaluate robustness across multiple laptop platforms and in realistic acquisition channels, including distance recording from approximately 3 meters away on the same desk, through-the-wall eavesdropping with a contact microphone, and background keyboard noise in online conferencing systems. Across these scenarios, the proposed method achieves high reconstruction accuracy (often exceeding 90%) with approximately 150-250 observed keystrokes. These results indicate that accurate text reconstruction from keystroke sounds is feasible in practice under an audio-only setting, even with limited observed keystrokes and without requiring device-specific labeled data, highlighting a realistic and previously underestimated privacy risk.

---


### 105. [InnoText: A Unified Model for Visual Text Generation and Editing](https://arxiv.org/abs/2607.22101)

**<font color=#1a73e8>作者：</font>** Haowei Liu, Runze He, Jian Lu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently achieved remarkable success in high-fidelity image synthesis, yet their application to visual text generation and editing remains relatively underexplored. Unlike general image generation, visual text tasks demand precise structural regularity and legibility, which may pose additional challenges for small-scale text and non-Latin scripts such as Chinese. Existing UNet-based models often struggle to produce clear and coherent text, while DiT-based models, though more expressive, are typically limited to a single task, which may lead to redundant training pipelines, inconsistent visual styles, and reduced cross-task generalization. To address these challenges, we propose InnoText, a unified DiT-based framework capable of performing both text generation and editing within a single model. We introduce a Font Size-Aware Modulation (FSAM) module to enhance representations across font scales, a Small-Character Aware Augmentation strategy to improve fine-grained fidelity, and a Task-Specific Region Weighted Loss for adaptive optimization. To support training and evaluation, we also construct a high-quality bilingual (English-Chinese) visual text dataset covering diverse fonts, sizes, and backgrounds. Experimental results demonstrate that our method achieves superior generation accuracy and editing quality, producing visually appealing and realistic text images.

---


### 106. [The machine can say it but cannot hear it. Designed affective patterns and the expressive-sensing asymmetry in human-machine communication](https://arxiv.org/abs/2607.22104)

**<font color=#1a73e8>作者：</font>** Jan K. Argasinski  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Affect-adaptive systems increasingly act as communicators that sense a user's emotion and respond with events meant to change it, closing an affective loop. This vision assumes both that a machine's affective messages are received and that the bodily channel it monitors carries an intelligible reply-assumptions rarely tested together. In a within-subjects virtual-reality study (N = 20), an autonomous system delivered six empirically derived affective patterns-scripted emotional events distilled from 104 practitioners' (first responders') critical incidents-while we recorded the human reply across felt emotion, felt arousal, and autonomic (electrodermal and cardiac) activity. Acting only as an author of designed messages, the machine reliably evoked strong, differentiated emotions: valence fell sharply for every pattern (|dz| = 1.1-1.7), and the patterns produced distinguishable, individually classifiable signatures of anger, fear, and sadness, functioning as a vocabulary of machine-to-human affective messages. Yet the channel the machine would read stayed largely silent. Self-reported arousal did not change, with Bayesian and equivalence evidence for no effect; sympathetic and cardiac arousal moved only for the most perceptually salient events, not for the messages experienced as most powerful; and within individuals, felt valence was decoupled from both bodily registers. This valence-arousal dissociation reveals an expressive-sensing asymmetry: machine agency extends to expression but not perception, and closed-loop designs regulate on a variable their messages neither reliably move nor are legible in. We draw out implications for theories of machine agency and for affect-adaptive design.

---


### 107. [Projection Pursuit CPCANet for Domain Generalization](https://arxiv.org/abs/2607.22117)

**<font color=#1a73e8>作者：</font>** Yu-Hsi Chen, Abd-Krim Seghouane  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain Generalization (DG) aims to learn representations robust to distribution shifts. Recent geometric alignment methods, such as CPCANet, extract domain-invariant structures through batch-wise Common Principal Component Analysis (CPCA). However, CPCANet suffers from rank-deficient covariance estimation due to the small-sample-size issue in mini-batch training. To address this limitation, we propose Projection Pursuit CPCANet (PP-CPCANet), a covariance-free framework that learns a global orthogonal basis on the Stiefel manifold and jointly optimizes it with network parameters via the Cayley transform. We further introduce a symmetry-breaking detached-median PP dispersion objective to extract common principal components (CPCs) with dense and robust optimization signals. Experiments on four DG benchmarks show that PP-CPCANet achieves SOTA performance while maintaining stable training.

---


### 108. [An AI-Driven Virtual Patient for Breaking Bad News: An Expert Formative Study on Facial Expression Intensity](https://arxiv.org/abs/2607.22118)

**<font color=#1a73e8>作者：</font>** Steffen Hauck, Theresa Schell, Sophie Jörg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interactive virtual patients driven by large language models (LLMs) offer scalable solutions for medical communication training, such as breaking bad news. However, designing their emotional expressiveness remains a challenge. This paper presents an AI-driven virtual patient framework combining LLM dialogue with real-time facial animation in virtual reality (VR). We conducted an exploratory, formative evaluation with seven medical experts to gather early feedback and elicit design requirements. The evaluation focused on how variations in facial expression intensity affect perceived realism and the virtual patient's emotion intelligibility. While descriptive quantitative ratings remained baseline across conditions, qualitative interviews provided deep insights into how experts perceive virtual emotional cues. The findings suggest that experts evaluate emotional realism holistically through multiple verbal and non-verbal channels; isolated facial adjustments are easily overshadowed by dialogue nuances and vocal prosody. Based on these insights, we present a roadmap for future medical training simulators, highlighting the need for synchronized, multi-modal pipelines incorporating body gestures, conversational pauses, and vocal dynamics.

---


### 109. [A Framework for Individual Tree Growth Reconstruction Using Multi-Platform Laser Scanning](https://arxiv.org/abs/2607.22129)

**<font color=#1a73e8>作者：</font>** Daniella Tavi, Valtteri Soininen, Lassi Ruoppa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate tree-level forest monitoring using laser scanning data requires reliable tree delineation, consistent tree correspondence across multitemporal point clouds, and accurate estimation of tree attributes and their change. Reconstructing tree growth in boreal forests is challenging due to the scarcity of historical stem-level data, propagation of errors from older sensors into change estimation, and growth rates with a magnitude of measurement uncertainty. This study investigates a framework for estimating individual tree diameter at breast height (DBH) and stem volume growth using 136 point clouds acquired between 2014--2025 with 11 scanners on airborne (ALS), mobile (MLS), and terrestrial laser scanning (TLS) platforms across boreal forest test sites. Trees were delineated from an MLS point cloud using deep learning-based segmentation which was transferred to the remaining point clouds, resulting in reliable multitemporal tree correspondence. Stem curves were derived from MLS/TLS data, with ALS data used for height estimation, enabling DBH and volume estimation and time series. A height growth-based scaling model was used to reconstruct stem attributes across time and estimate growth. Results showed that modeled growth achieved higher agreement with manual growth estimates than differencing independently estimated attributes from point clouds. The modeled-manual 5- and 10-year growth RMSEs were 55--111\% and 26--67\% for DBH, and 31--87\% and 21--67\% for volume, respectively, depending on plot difficulty. The scaling model was temporally robust, with errors remaining stable or stabilizing after 5--6 years, reaching maximum RMSEs of 8--12\% for DBH and 12--23\% for volume after 12 years. Combining MLS/TLS-derived stem measurements with multitemporal ALS-derived heights provided a robust framework for individual tree growth estimation without requiring multiple under-canopy scans.

---


### 110. [GLI-AL: A Multi-Modal Glioma MRI Label Resource with Unified Anatomy-Lesion Labels](https://arxiv.org/abs/2607.22135)

**<font color=#1a73e8>作者：</font>** Xingyu Xiang, Shuang Hao, Fan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing BraTS-GLI datasets provide a widely used benchmark for adult glioma MRI segmentation, but their task definition focuses on tumor subregions and does not systematically represent coexisting white matter hyperintensities (WMH). In joint segmentation settings, such unlabeled abnormalities introduce task-specific label noise by treating pathological regions as normal tissue. To address this limitation, we introduce BraTS-GLI Anatomy-Lesion, a controlled-access, labels-only derived resource built from the BraTS 2023-GLI training cohort. The resource provides 1,251 unified eight-class anatomy-lesion label sets aligned with the original four-modal MRI cases, including image-repair labels for 116 cases requiring repaired imaging inputs. The cohort is organized into a 394-case purified subset and an 857-case extended subset, with case-level metadata covering label source, image-repair requirements, quality-control status, access conditions, checksums, and release boundaries. Compared with the original BraTS-GLI annotations, the resource substantially expands foreground supervision by incorporating healthy brain tissues and previously unlabeled coexisting abnormalities within a unified label space. A validation study using MedNeXt and T1/FLAIR inputs suggests that WMH-aware supervision preserves healthy-tissue segmentation performance across both in-domain GLI and external WMH datasets, while improving sensitivity to coexisting lesions relative to noisy-control training. The resource is intended for scientific research and supports joint anatomy-lesion supervision, label-noise analysis, and reproducible evaluation. Data are available at this https URL, and code is available at this https URL. The data resource DOI is this https URL.

---


### 111. [Dynamic Commonsense Coordination for Empathetic Response Generation](https://arxiv.org/abs/2607.22136)

**<font color=#1a73e8>作者：</font>** Zhengyu Qi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Empathetic Response Generation (ERG) requires models to recognize users' emotions and generate empathetic responses. Commonsense knowledge has been shown to support such reasoning, yet existing approaches typically reuse fixed commonsense representations across understanding and generation, limiting their ability to coordinate such knowledge across different stages. We propose DCC, a Dynamic Commonsense Coordination Framework with three complementary modules: residual-based commonsense interaction (SCE-AttnRes) to integrate contextual and situational commonsense representations, Association-Guided Commonsense Filtering (AGCF) to down-weight low-relevance commonsense relations, and Iterative Commonsense-Aware Decoding (ICAD) to dynamically retrieve commonsense memories during generation. Experiments on the Empathetic-Dialogues benchmark show that DCC improves emotion classification accuracy and response diversity over the CEM baseline while maintaining comparable perplexity. An LLM-based blind evaluation further demonstrates that DCC generates responses with better relevance, coherence, and informativeness. The code and implementation details will be publicly available at this https URL.

---


### 112. [CARDIAG: A Dense Segment Classification Benchmark of Deep Learning Architectures for Coronary Angiography](https://arxiv.org/abs/2607.22139)

**<font color=#1a73e8>作者：</font>** Dominik Bernard Lau, Hubert Malinowski, Jerzy Szyjut 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate pixel-level classification of coronary angiograms is critical for cardiovascular disease assessment, yet the field lacks standardized evaluation protocols. In this work we demonstrate a new benchmark for the assessment of deep learning models which densely classify pixels of coronary angiograms to one of SYNTAX classes (or background). The evaluation covers 24 distinct architectures starting with classic convnets to recent state-space-based vision algorithms. We release CARDIAG - a multi-center, multi-label dataset which we carefully split to reliably compute metrics, accounting for diameter error, overlap, centerline quality and calibration. The data contains SYNTAX labels, binary, uncertainty and segmentation masks as well as intermediate frames together with the selected non-sensitive DICOM metadata. From the multitude of algorithms, we nominate ConvNeXt V2 encoder with DeepLab V3 Plus decoder as the best performing, achieving macro $F_1=0.456$, which we then ensemble with Mamba U-Net and Feature Pyramid Network, for an increased $F_1=0.479$. We demonstrate all the architectures to be well calibrated and determine the generalization of the top 5 methods, together with the data efficiency of these architectures. We highlight the importance of both high-resolution and low-resolution features in encoding. We also demonstrate the model correctness in the context of patient demographic, vessel sides and projection angle configurations. Overall the released benchmark allows for future studies to robustly and rigorously assess the proposals, not only for SYNTAX segmentation, but lesion detection and many more.

---


### 113. [TriGlue: a Biology-Inspired Generative Model for Generating Molecular Glue-Induced Ternary Complex](https://arxiv.org/abs/2607.22143)

**<font color=#1a73e8>作者：</font>** Yuliang Yan, Shuo Yan, Haochun Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular glue degraders have emerged as a promising strategy for targeted protein degradation by inducing ternary complex formation between an E3 ubiquitin ligase and a target protein. Despite their therapeutic potential, computational design of molecular glues remains largely unexplored. Unlike conventional structure-based drug design, molecular glue design is governed by the unknown protein-protein interface and requires the simultaneous modeling of ligand generation, protein-protein docking, and ternary complex assembly. In this work, we formulate molecular glue design as a ternary complex generation problem and propose a biology-inspired generative framework, TriGlue. Motivated by the mechanism of molecular glue action, we decompose ternary complex generation into two coupled stages: interface estimation and interface-conditioned complex generation. First, we develop an SE(3)-equivariant interface estimation module that predicts a geometrically constrained protein-protein interface from unbound monomer structures. Second, we introduce an interface-conditioned ternary flow matching network that jointly generates the molecular glue and predicts the rigid-body transformation required to assemble the ternary complex. Extensive experiments demonstrate that TriGlue generates chemically valid molecules and produces plausible ternary complexes, which highlight the potential of biology-inspired generative modeling for accelerating molecular glue discovery. Our code is available at this https URL.

---


### 114. [Visual Relocalization from Sparse Views in Aliased and Low-Texture Environments via Novel View Synthesis](https://arxiv.org/abs/2607.22147)

**<font color=#1a73e8>作者：</font>** Maria Peribañez, Javier Civera, Rudolph Triebel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual localization becomes extremely challenging in planetary-like terrains characterized by low texture, perceptual aliasing, harsh illumination, and sparse, weakly overlapping viewpoints induced by forward rover motion and unconstrained driving directions. Under these conditions, state-of-the-art image-to-image and image-to-map matching pipelines suffer significant performance degradation. In this work, we propose a visual relocalization method that departs from classical correspondence-based pipelines by directly estimating camera poses against a differentiable map representation built with 3D Gaussian Splatting (3DGS). Our key contribution is a geometry-aware training strategy that combines photometric and geometric losses, where the geometric supervision is provided for the first time by combining multi-view stereo (MVS) and LiDAR depths. We show that this joint optimization produces a 3DGS model that better fits the underlying scene geometry, leading to improved photometric and geometric consistency and more robust, accurate single-image 6-DoF pose estimation. Extensive experiments on data acquired in planetary-analog environments validate the effectiveness of our approach, showing substantial gains in relocalization accuracy under challenging conditions. Code is available at this https URL.

---


### 115. [dRAE: Representation Autoencoder with Hyper-Spherical Codes](https://arxiv.org/abs/2607.22148)

**<font color=#1a73e8>作者：</font>** Tianren Ma, Lin Long, Chuyan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we aim to discretize the high-dimensional visual representations to bridge the gap with language models - a non-trivial challenge, as existing quantization methods suffer from codebook collapse, failing to scale while preserving semantic coherence. We identify the root cause as metric mismatch: standard Euclidean codebook objectives are fundamentally misaligned with the anisotropic geometry of representation space, leading to codebook embeddings with high-variance magnitude scales and uneven angular distributions that hinder scalability. To address this, we propose Hyper-Spherical Quantization (HSQ), which decouples semantic content from feature magnitude via angular routing, preventing code assignment from being dominated by scale rather than meaning. The resulting discrete Representation Autoencoder (dRAE) achieves high-fidelity reconstruction while preserving semantic integrity and supporting scalable codebook budget. Extensive experiments demonstrate consistent performance gains as the vocabulary size scales to 131{,}072, along with 100\% codebook utilization, simplified training pipeline, and strong performance across understanding and generation tasks.

---


### 116. [Unbiased Open World Regularization for Fair Self-Supervised Learning](https://arxiv.org/abs/2607.22149)

**<font color=#1a73e8>作者：</font>** L{é}o Nicollier, Marc Pic, Pablo Mus{é} 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite recent advances, self-supervised learning (SSL) models and Joint-Embedding Predictive Architectures (JEPAs) remain susceptible to learning spurious biases in the dataset. These techniques rely on regularization, which prevents representation collapse by enforcing a global target distribution such as a multivariate Gaussian or a uniform distribution on the sphere. However, these global constraints are insufficient to prevent bias entanglement, as task-irrelevant features can still segregate the latent space into distinct sub-regions. While recent approaches like Entangling and Disentangling (EnD) and Fair Supervised Contrastive Learning (FSCL) empirically debias the latent space, we show that they act as partial approximations of conditional distribution matching. To enforce this matching explicitly, we propose Unbiased Open World Regularization (UOWReg), an encoder-only framework. We show that this shift from a global to a conditional objective guarantees statistical independence between the learned representations and the targeted attributes, regardless of the chosen target distribution. We empirically validate this framework across both Gaussian and spherical latent spaces, using statistical measures to enforce these target distributions. While conditional matching successfully mitigates bias with both distributions, we demonstrate that enforcing conditional uniformity on the sphere yields a lower linearprobing classification error. Empirically, UOWReg reduces Equalized Odds violations on the CelebA benchmark while maintaining competitive classification accuracy compared to existing encoder-only baselines. Furthermore, we introduce the Synthetic Engraving Task-a novel setting in which a dominant macro-structure masks a fine-grained micro-signature. We show that UOWReg effectively prevents the subpopulation collapse observed in standard SSL, successfully isolating micro-signatures even when heavily entangled with the global structure.

---


### 117. [Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents](https://arxiv.org/abs/2607.22157)

**<font color=#1a73e8>作者：</font>** Valentin Tablan, Scott Taylor, Kristoffer Bernhem  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents encounter learning opportunities in every episode they run, and discard nearly all of them: the underlying models are frozen at deployment, so an agent that resolves a difficult request today starts from zero when it recurs tomorrow. Yet ordinary operation already produces feedback, in the form of outcome verdicts and after-the-fact corrections. We show that this feedback is a sufficient signal for continual learning when the frozen model is paired with an external memory that distils each episode into retrievable natural-language rules. On the banking domain of $\tau$-bench, against a static-RAG control retrieving over the complete policy corpus, learning from the one-bit outcome verdict lifts single-trial success to 1.6$\times$ the baseline, and learning from corrections to 2.6$\times$, converting 22 of the 84 tasks the baseline never solves. The result spans the deployment spectrum, measured on Mistral Large, an open-weights model that organisations with data sovereignty requirements can self-host, and replicated on a frontier model, Claude Sonnet 5. The accumulated memory also transfers: each model, reading the store built by the other, rises above its own no-memory baseline. The harness, protocol, and data are released.

---


### 118. [JustDepth: Real-Time Radar-Camera Depth Estimation with Single-Scan LiDAR Supervision](https://arxiv.org/abs/2607.22172)

**<font color=#1a73e8>作者：</font>** Wooyung Yun, Dongwook Kim, Soomok Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate yet low-latency depth is essential for radar-camera perception in autonomous systems. Cameras provide rich appearance but lack metric scale, whereas automotive radar offers metric range but is sparse and noisy. Many pipelines are multi-stage or depend on auxiliary annotations, increasing latency and limiting portability. We introduce JustDepth, a single-stage radar-camera depth estimator trained only with radar, camera, and single-scan LiDAR. All radar returns are aggregated into a fixed-width 1D representation, decoupling runtime from point count. A Height Fusion Block fuses modalities, a lightweight GNN propagates depth globally, and a training-only confidence decoder stabilizes learning with zero test-time cost. We mitigate stripe artifacts via simple augmentations and quantify them using the Vertical-Horizontal Gradient Ratio (VHGR). On nuScenes, compared to recent state-of-the-art methods, JustDepth maintains accuracy while reducing inference time by 39.7x and stripe artifacts by 66% as measured by VHGR.

---


### 119. [Bowel Obstruction Detection and Localization on Abdominal CT with Deep Learning](https://arxiv.org/abs/2607.22173)

**<font color=#1a73e8>作者：</font>** Moritz Vandenhirtz, Andrea Agostini, Dana Belde 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bowel obstruction is a common and potentially life-threatening gastrointestinal condition. In the face of rising diagnostic workloads, the automated diagnosis of bowel obstruction on CT scans supports radiologists by accelerating detection and improving patient outcomes. In this work, we propose a deep learning framework with a multi-task objective that jointly detects bowel obstruction and localizes its transition zone. Additionally, we extend the method with an inherently interpretable classification method that locates the suspected transition point within a slice. It does so by learning a probabilistic selection mask that faithfully bases the classifier's prediction solely on a small image region. The proposed method is evaluated on an internal dataset comprising 1,427 abdominal CTs. Here, the model achieves an obstruction detection test accuracy of 93% and a Hit@10 transition zone localization of 95%. As the first method to reliably localize the transition zone, this marks a significant step towards the automated identification of this critical clinical landmark.

---


### 120. [From Score Approximation to Distribution Approximation in Score-Based Diffusion Models](https://arxiv.org/abs/2607.22199)

**<font color=#1a73e8>作者：</font>** Lan V. Truong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based diffusion models have achieved remarkable empirical success in generative modeling, yet their approximation-theoretic foundations remain incomplete. In particular, although classical universal approximation theorems guarantee that neural networks can approximate score functions, it remains unclear whether such approximation guarantees translate into approximation of the probability distributions generated by reverse diffusion processes. In this paper, we establish a rigorous quantitative connection between these two notions. Specifically, we prove that if a neural network approximates the true score function sufficiently accurately, then the probability distribution generated by the corresponding reverse diffusion model is close to the target data distribution in Kullback-Leibler (KL) divergence, up to an irreducible mismatch between the terminal distribution of the forward diffusion process and the prior used to initialize the reverse process. More precisely, we derive an explicit upper bound on the distribution approximation error in terms of the score approximation error, the diffusion noise schedule, and the terminal prior mismatch. Our analysis combines Hornik's universal approximation theorem, Girsanov's theorem on path space, and the data processing inequality for relative entropy. Complementary to recent work that studies score approximation under finite-sample statistical settings and structural assumptions on the data distribution, our work develops an approximation-theoretic analysis based on classical neural network approximation theory. The resulting theorem provides a simple and explicit guarantee linking neural network approximation of score functions to approximation of the probability distributions generated by reverse diffusion models.

---


### 121. [LayoutLite: Token-Level Implicit Layout Analysis for Efficient Document OCR](https://arxiv.org/abs/2607.22200)

**<font color=#1a73e8>作者：</font>** Xudong Liu, Bicheng Wan, Yulin Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end OCR systems based on vision-language models have achieved strong performance in complex document OCR, but their efficiency is limited by the large number of visual tokens produced from document images. Many of these tokens correspond to blank margins or visually redundant regions, yet directly applying generic visual token compression methods may remove OCR-critical fine-grained details. In this paper, we propose LayoutLite, a lightweight plug-and-play module for efficient document OCR. Instead of relying on explicit document layout detection, LayoutLite performs implicit layout analysis at the token level between the vision encoder and the language decoder. It aggregates multi-layer visual representations from the vision encoder, and predicts an importance score for each visual token with a lightweight scoring network. Low-information tokens are then removed before entering the language decoder while preserving the original spatial positional information of retained tokens. To train LayoutLite without human annotations, we cast token selection as a reinforcement learning problem and optimize it with a group-relative policy optimization objective driven by OCR output consistency, together with an auxiliary layout supervision signal to stabilize training. Experiments on OmniDocBench demonstrate that LayoutLite can substantially reduce visual token length and inference cost with negligible degradation in recognition quality. We further evaluate LayoutLite on two OCR-specialized VLMs, FireRed-OCR and Logics-Parsing-V2. Under up to 50% token compression, LayoutLite preserves almost the same score on both models while reducing prefill latency, FLOPs, and KV cache memory by over 40%, with only a small additional inference overhead. These results show that token-level implicit layout analysis is an effective and practical approach for accelerating VLM-based OCR systems.

---


### 122. [Deep Convolutional Large-Margin $\ell_p$-SVDD for Visual Anomaly Detection](https://arxiv.org/abs/2607.22212)

**<font color=#1a73e8>作者：</font>** Alireza Dastmalchi Saei, Shervin Rahimzadeh Arashloo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual anomaly detection requires adaptive representations and reliable decision boundaries, particularly when anomalous training samples are scarce and class distributions are highly imbalanced. Classical kernel-based methods yield principled geometric decision regions but typically operate on fixed features, while deep detectors learn task-specific representations but often fail to provide an explicit margin-aware kernel boundary. In this study, we propose DLM-SVDD, a deep large-margin novelty-detection framework that jointly learns convolutional features and an explicit kernel-based decision boundary. By drawing on the large-margin $\ell_p$-Support Vector Data Description ($\ell_p$-SVDD) approach, the proposed method performs explicit margin maximization and nonlinear slack penalization while adapting the representation to the target task. To train the proposed model, we present an optimization scheme that alternates between a Frank--Wolfe--based update of the convex dual boundary and a CNN update step operating on a smooth margin-violation loss induced by the recovered boundary. To improve scalability, we analyze the efficiency--accuracy trade-offs for different kernel approximation strategies, deriving practical propositions for large-scale anomaly detection.
Extensive experiments on multiple standard benchmarks show consistent performance improvements over the baseline and strong overall performance compared with state-of-the-art methods while illustrating that the proposed joint representation--boundary learning scheme remains effective under severe imbalanced class distributions.

---


### 123. [Latent PDE mapping for efficient physics-informed learning across geometries with limited data](https://arxiv.org/abs/2607.22215)

**<font color=#1a73e8>作者：</font>** Ingvild Askim Adde, Mary M. Maleckar, Gabriel Balaban  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this study, we introduce latent PDE mapping, a broadly applicable physics-informed learning technique designed to enable efficient geometric generalization with sparse training data. Latent PDE mapping pulls back geometry-specific PDE residuals and boundary conditions to a predefined latent geometry via the deformation gradient, thereby enabling the automated calculation of geometry-consistent shape gradients that are missing in conventional physics-informed machine learning formulations. We demonstrate the utility of latent PDE mapping in solving the anisotropic Aliev-Panfilov PDE of cardiac electrophysiology using both physics-informed neural networks and physics-informed deep operator networks. The Aliev-Panfilov PDE serves as a challenging exemplar: a nonlinear, time-dependent PDE benchmark with sharp gradients that are expensive to capture using traditional numerical solvers. To represent the limited data regime, we train the networks using just fifteen geometric samples drawn from parameterized distributions in two and three spatial dimensions. While modest improvements appear for geometries parameterized by affine and shear deformations, latent PDE mapping demonstrates significant benefits on select geometric families, achieving a factor ~4-6 reduction in mean relative L2 error. Furthermore, our results show that the computational cost of applying latent PDE mapping was modest during network training, and negligible at inference. Taken together, our study highlights how latent PDE mapping facilitates the creation of generalizable physics-informed machine learning models from limited sets of training geometries.

---


### 124. [trasgoDP: An Open Source Framework for Releasing Noised Tabular Microdata under Local Differential Privacy](https://arxiv.org/abs/2607.22230)

**<font color=#1a73e8>作者：</font>** Judith Sáinz-Pardo Díaz, Álvaro López García  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> trasgoDP is a modular, open-source, and easy-to-use Python framework for releasing tabular microdata under {\epsilon}-local differential privacy guarantees, as well as location data under geo-indistinguishability assumptions, designed to be installed and integrated within standard data science workflows. The software enables systematic exploration of privacy-utility trade-offs across multiple mechanisms, data types, and {\epsilon} values. While differential privacy has been extensively studied for aggregate data, its application to row-wise microdata release remains underexploited in terms of reusable software tools, a gap that is even more pronounced in the case of metric privacy and location-based data. trasgoDP implements local-DP mechanisms for numerical and categorical attributes (Laplace, Gaussian, Exponential, and Randomized Response), a geo-indistinguishability mechanism for location data, and a set of utility metrics, including a novel correlation-loss measure, to quantify information loss as a function of the allocated privacy budget. The objective of this work is to provide the research community with a reproducible, open-source baseline for evaluating tabular and location-based data publication methodologies under formal local differential privacy guarantees.

---


### 125. [TRaM-VSR: Importance-Aware Token Routing and Merging for One-Step Diffusion Video Super-Resolution](https://arxiv.org/abs/2607.22231)

**<font color=#1a73e8>作者：</font>** Sicheng Gao, Zhuyun Zhou, Yixuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video super-resolution (VSR) using large-scale Diffusion Transformer (DiT) priors achieves exceptional perceptual quality but is often impractical due to the quadratic computational cost of processing dense spatio-temporal token sequences. Existing efficiency-oriented methods risk irreversible detail loss and temporal flickering, a vulnerability especially pronounced in one-step diffusion models. To address this, we propose TRaM-VSR, a Token Routing and Merging framework for adaptive token allocation, leveraging both context-aware video priors and network-level priors. First, token importance is estimated by fusing motion-sensitive temporal cues with semantic text similarity, isolating dynamic objects and structural boundaries. Next, this importance is further calibrated and adjusted by an offline planner to guide routing across optimally grouped network blocks. Technically, within each routed group, structurally critical tokens are processed in a high-fidelity local stream, while less informative tokens are aggregated into a compact global stream, both modulated by network depth and aligned with the multigranular nature of diffusion models. Extensive experiments show that TRaM-VSR accelerates inference significantly while preserving state-of-the-art reconstruction quality and robust temporal consistency. The code is available at this https URL.

---


### 126. [Optimization of time-consuming experimental conditions using pseudo-experimental data guided by adaptive polynomial regression](https://arxiv.org/abs/2607.22238)

**<font color=#1a73e8>作者：</font>** Hirotaka Sugawara, Yujin Taguchi, Kei Minagawa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) is an optimization method that sequentially proposes the next candidate explainable variables for optimizing target variables by balancing exploration and exploitation. BO is often used under a limited evaluation budget, such as hyperparameter tuning of deep learning. Despite its effectiveness, conventional BO may have poor convergence in practical experimental science where each evaluation is often costly and time-consuming. Recently, BO methods have been proposed that accelerate optimization by using pseudo-experimental data that simulate experimental data. However, when only a limited number of experimental data are available, the generated pseudo-experimental data may be of insufficient quality. In this study, we developed PolyBO to improve optimization time by generating high-quality pseudo-experimental data even when the number of trials is limited. PolyBO performs BO efficiently by generating pseudo-experimental data with an adaptively updated versatile parametric model. This low-capacity polynomial regression model is intended to enable efficient BO even with limited experimental data. PolyBO updates the BO surrogate model with a combined dataset consisting of experimental data and pseudo-experimental data and then performs optimization. Using synthetic benchmark functions with diverse landscapes, we found that PolyBO reduced the optimization time by a median of 42\%. For a real-world material composition optimization problem, PolyBO reduced the optimization time by a median of 96\% compared with conventional methods. Overall, PolyBO achieves efficient optimization in settings where each experiment requires a long time.

---


### 127. [From level set evolution to threshold optimization: A grayscale level set framework for image segmentation](https://arxiv.org/abs/2607.22255)

**<font color=#1a73e8>作者：</font>** Xingkai Li, Jiebao Sun, Fanghui Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The segmentation of multiple degradations has been a challenging problem in the field of image segmentation. Existing level set approaches commonly adopt a length regularization term to constrain the geometric shape of the segmentation contour. However, the introduction of the length term often results in numerical instability and high computational cost. In this paper, we show that the length term is not essential under certain smoothness constraints, and theoretically prove that the presence of the length term affects the property of $|\nabla \phi|=1$. Based on the finding, we define a class of smooth images, construct the grayscale level set, and propose a fast segmentation framework for degraded images, such as heavily noisy images and intensity inhomogeneous images. The framework transforms PDE evolution into one-dimensional threshold search, which has significant advantages in computational speed, especially on large-scale images. Experiments validate the segmentation performance of the proposed framework on various degraded images.

---


### 128. [Class-Balanced Softmax: A Bayes Theory-Based Method for Long-Tailed Recognition](https://arxiv.org/abs/2607.22258)

**<font color=#1a73e8>作者：</font>** Yi-Hang Zhu, Rajeev Raman, Shiqi Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models using traditional softmax classifiers have achieved remarkable success in various classification tasks. However, their performance degrades significantly on imbalanced datasets. Although Balanced Softmax is widely adopted as a state-of-the-art rebalancing method, it possesses inherent limitations, such as yielding disproportionately lower testing accuracy for tail classes. To mitigate these shortcomings, we propose the Class-Balanced Softmax (CBS). Rooted in a theoretical Bayesian framework and a heuristic power-law assumption, the CBS is a simple logit adjustment that is computationally inexpensive and easily integrated into existing pipelines. Furthermore, we characterise a fundamental phenomenon in models trained on imbalanced data, termed the preference issue, wherein models exhibit higher training error and a larger generalisation gap for classes with limited data. To quantify this issue, we introduce a novel metric and demonstrate that CBS effectively mitigates the preference issue. Extensive experiments on large-scale benchmarks show that CBS is highly scalable and outperforms existing methods, including Balanced Softmax.

---


### 129. [AI4PLE: A Methodology for Integrating AI into Product Line Engineering](https://arxiv.org/abs/2607.22260)

**<font color=#1a73e8>作者：</font>** Bedir Tekinerdogan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reuse-based development has become increasingly important in the creation of complex systems, offering significant opportunities to reduce costs, improve quality, and accelerate time-to-market. Product Line Engineering (PLE) provides a systematic approach to realizing this potential by enabling the efficient creation, management, and customization of product families by reusing shared assets and capabilities. PLE involves addressing numerous complex decisions, including feature selection, variability management, and configuration optimization, which are critical to the success of a product line. Despite its promise, the systematic integration of Artificial Intelligence (AI) into PLE processes has not yet been comprehensively explored. In this paper, we propose a methodological framework to support the systematic integration of AI into PLE and evaluate its effectiveness through a multi-case study conducted in an industrial context.

---


### 130. [Kalyna Block Cipher: From Design Space Exploration to ASIC Design](https://arxiv.org/abs/2607.22269)

**<font color=#1a73e8>作者：</font>** Carlos Gewehr, Levent Aksoy, Mariia Rodinko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Kalyna block cipher is a Ukrainian cryptography standard, selected through a national competition held between 2007 and 2010 and approved in 2015. Although its software implementations have been introduced, hardware-efficient implementations of the algorithm, i.e., accelerators, do not exist. In this paper, we explore various design architectures to implement its encryption, decryption, and unified encryption/decryption functions, considering the trade-off between area and latency. We present hardware reduction techniques and introduce alternative designs with low area, latency, and energy consumption, targeting an application-specific integrated circuit (ASIC). We present hardware-efficient designs that include countermeasures against side-channel analysis (SCA) and fault injection (FI) attacks, such as hiding, masking, and duplication techniques. We validate these implementations in a 65\;nm ASIC chip. Experimental results confirm the need for alternative designs that explore the design search space for different requirements. The proposed architectures enable hiding the power SCA leakage by randomizing the execution of operations, and the temporal duplication in designs with countermeasures against the SCA attacks can mitigate the FI attacks. The functionality of the ASIC test chip, including various Kalyna designs, is validated through measurements.

---


### 131. [An Insight on Evaluation Metrics Under the Imbalanced Case of Anomaly Detection](https://arxiv.org/abs/2607.22286)

**<font color=#1a73e8>作者：</font>** Romain Hermary, Nesryne Mejri, Djamila Aouada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection is inherently characterised by severe class imbalance, making the interpretation of evaluation metrics challenging. Although metrics such as AUROC, AUPR, F1-score, and MCC are widely used, their values convey different meanings depending on the anomaly ratio. In this work, we analyse the behaviour of those four common anomaly detection metrics under varying levels of imbalance. We focus on the study of metric landscapes, visualisations that relate metric values to true positive and true negative rates, providing an intuitive view of metric preferences and stability. Our analysis offers practical guidance for interpreting and comparing anomaly detection results across datasets with different imbalance ratios.

---


### 132. [Efficient Recommendations via Graph Coarsening and Label Propagation](https://arxiv.org/abs/2607.22287)

**<font color=#1a73e8>作者：</font>** Alessandro Sbandi, Federico Siciliano, Fabrizio Silvestri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-based recommendations are widely adopted in real-world industrial applications. However, graphs in these systems often reach a massive scale, posing notable scalability and efficiency challenges. This requires techniques that can effectively balance predictive quality with computational cost. One promising approach is graph coarsening, an adaptive graph reduction technique that offers a way to systematically construct smaller, yet structurally representative, versions of the original large-scale graphs.
In this work, we propose a flexible two-stage diffusion framework that combines graph coarsening with multi-step label propagation in the telecommunications domain. Domain-specific heuristics are applied to first aggregate nodes into meaningful communities, reducing graph size while preserving essential business-relevant relationships. An initial diffusion process done by a Label Propagation Algorithm (LPA) or a Graph Neural Network (GNN) propagates labels across the coarsened graph to produce coarse-grained predictions. Finally, a second LPA within subgraphs generates the final recommendations for individual users.
On a real-world telecommunications dataset, when using LPA in both stages, our method achieves up to +24% NDCG@5 over the full-graph LPA baseline. Incorporating a lightweight GNN in the first stage further boosts NDCG@5 by more than 50%, but requires substantial training and inference time. Through extensive experiments and a detailed ablation, we quantify these trade-offs and demonstrate that our coarsening-driven approach delivers an optimal balance between scalability, latency, and recommendation quality.

---


### 133. [Biomedical Machine Translation for Low-Resource Arabic-Script Languages via Cross-Lingual Transfer and LoRA Adapter Merging](https://arxiv.org/abs/2607.22300)

**<font color=#1a73e8>作者：</font>** Abdullah Alabdullah, Arash Eslamighayour, Sarp Harbalioglu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a systematic study of healthcare-domain cross-lingual transfer to address the scarcity of biomedical NMT resources for Arabic-script languages. We use Arabic and Persian as higher-resource pivots to improve translation for \textbf{four severely low-resource} targets: Dari (Afghan Persian, a standardised variety of Persian), Pashto, Sorani Kurdish (Central Kurdish, a major standardized variety of Kurdish), and Urdu (closely related to Hindi). Using LoRA fine-tuning on small decoder-only LLMs, we train \textit{domain-specific pivot adapters} and evaluate \textbf{three transfer strategies}: few-shot in-context learning, minimal supervised adaptation, and, to the best of our knowledge, for the first time in this setting, zero-data LoRA adapter merging. Supervised adaptation with just 500 sentences achieves near pivot-language quality for Dari (CHrF++ 41.01) and meaningful gains for Urdu (28.88), while adapter merging reaches within 3.5 CHrF++ of supervised adaptation for Dari at zero additional cost. Pashto and Sorani Kurdish remain insufficient for high-stakes clinical deployment exposing the limits of cross-lingual transfer when structural distance from the pivots is too great. LoRA adapter merging works surprisingly well for closely related languages, even without target-language biomedical data.

---


### 134. [fMRI2Face: A Full-HD fMRI-Video Dataset and Geometry-Guided Neural Decoding Framework for Dynamic Human Face Reconstruction](https://arxiv.org/abs/2607.22302)

**<font color=#1a73e8>作者：</font>** Jingyang Huo, Xiangru Huang, Chentao Shen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic human faces from brain activity provides a powerful way to study how the mind perceives identity, expression, and facial motion. However, progress in fMRI-based face decoding has been limited by scarce controlled, high-resolution neural datasets and by methods that struggle to recover both identity-specific appearance and time-varying facial dynamics. We present fMRI-Face, the first fMRI dataset paired with controllable full-HD digital human facial videos rendered at 1920$\times$1080 resolution. During scanning, participants watched photorealistic, background-free facial videos with controlled identity, expression, and head pose, while fMRI activity was recorded. The resulting dataset contains 62,856 paired fMRI-video samples, providing a structured resource for studying dynamic face perception and reconstruction. Building on this dataset, we propose fMRI2Face, a geometry-guided neural video decoding framework for reconstructing facial videos from fMRI signals. fMRI2Face derives two complementary neural controls from brain activity: Brain-derived Appearance Context, which captures global identity-related visual attributes, and Morphable 3D Facial Control, which provides explicit geometry-aware guidance for pose, expression, and non-rigid facial dynamics. These controls are integrated through Neural-Controlled Video Diffusion with auxiliary latent completion, enabling high-fidelity facial video reconstruction directly from brain activity. Experiments show that fMRI2Face consistently improves reconstruction fidelity, identity preservation, facial geometry, and motion consistency over representative neural decoding baselines. Together, fMRI-Face and fMRI2Face establish a controlled platform for studying dynamic face perception and provide a new benchmark for fMRI-based digital human reconstruction.

---


### 135. [Synthetic Speech, Real Signal: Paralinguistic Preservation and Cross-Lingual Augmentation via Voice Cloning](https://arxiv.org/abs/2607.22304)

**<font color=#1a73e8>作者：</font>** Roseline Polle, Owen Parsons, George Fairs 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data augmentation in speech is common practice for linguistic tasks like ASR, but has seen far less work for paralinguistic ones, especially clinical tasks where labelled data is expensive and some patient groups are underrepresented. Voice cloning is one such augmentation approach, but is typically evaluated on speech intelligibility (WER) or speaker similarity (SS) rather than on downstream performance, and it remains unclear whether these preserve the paralinguistic signal such tasks depend on. We benchmark eight voice cloning models on five paralinguistic tasks across public and clinical datasets, showing most preserve signal with modest degradation. We then clone English clinical speech into Japanese and find that training on cloned data outperforms raw cross-lingual transfer for depression and anxiety detection on real Japanese speech, suggesting voice cloning is a promising direction for augmenting clinical speech data in low-resource languages.

---


### 136. [Evolution-Aware MSA Reasoning for Subsampling via Factor Graphs](https://arxiv.org/abs/2607.22314)

**<font color=#1a73e8>作者：</font>** Zhangzhi Xiong, Minzhang Li, Haotian Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multiple Sequence Alignments (MSAs) provide protein language models with explicit evolutionary context, but their large depth makes subsampling unavoidable under limited token budgets. Existing strategies, including random selection, identity-based filtering, and diversity-driven sampling, are effective heuristics, yet provide limited control over the evolutionary signals retained in the subset. In this work, we recast MSA subsampling as an explicit optimization problem, where key evolutionary measures, including query identity and diversity, are treated as controllable objectives. Building on this view, we introduce AP-REASONER, an Affinity-Propagation-based factor-graph approach. With evolution-aware unary factors, exemplar-consistency factors, and two control knobs, AP-REASONER performs factor-graph reasoning through message passing to infer a fixed-budget MSA subset. Experiments on long-range contact prediction and conformational ensemble prediction show that AP-REASONER outperforms baseline subsamplers on structure-sensitive downstream tasks and enables controllable recovery of alternative protein conformations. These results highlight the value of modeling MSA subsampling as a controllable optimization problem, where factor-graph reasoning offers an effective alternative to heuristic selection.

---


### 137. [Geometric 2D Scene Graph Generation](https://arxiv.org/abs/2607.22325)

**<font color=#1a73e8>作者：</font>** Christoph Jahn, Urs Waldmann, Bastian Goldluecke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In production processes for consumer products, assembly instructions are essential not only for planning but also for executing the production process. Likewise in robotics, it is crucial for an assembly robot to understand how components fit together and can be assembled. To facilitate these tasks, we contribute a method for constructing scene graphs to represent and characterize assembly relationships between components. Our approach does not rely on semantic data and is capable of handling a very small dataset. To realize this, the output of a Faster R-CNN model is used to create geometric representations, which are then processed by a transformer architecture to generate an adjacency matrix. This matrix serves as input to a Siamese network that uses message passing based on an attentional graph convolutional network (aGCN) architecture to characterize the connections between the components. We validate our method on a study dataset of toy model components which can be assembled into transportation vehicles.

---


### 138. [SLIP: Segmentation with Low-latency Interactive Prompting for 3D Medical Images](https://arxiv.org/abs/2607.22332)

**<font color=#1a73e8>作者：</font>** Baptiste Podvin, Alexandre Ancel, Flavio Milana 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive deep image segmentation enables efficient medical image annotation by iteratively refining predictions from user prompts, such as positive and negative clicks. Recent patch-based methods, including nnInteractive, achieve strong segmentation performance but remain limited in annotation workflows by high interaction latency, limited responsiveness to successive interactions, and the lack of support for reversible prompting. Furthermore, evaluation relies predominantly on simulated rather than controlled real-user interaction studies. We present SLIP, an end-to-end trainable framework for interactive 3D medical image segmentation that decouples image encoding from prompt-guided refinement. Image features are computed once and reused, while a lightweight patch memory bank maintains an interaction-aware segmentation state shared across patches. This representation enables prediction updates by propagating interaction context throughout the image, supports reversible prompting without recomputing image features, and substantially reduces interaction latency. By separating image representation from interactive reasoning, SLIP remains compatible with a wide range of image encoders. We train a single SLIP model for general interactive segmentation across diverse anatomical structures and imaging modalities. Beyond standard simulated evaluation, we conduct a controlled prospective user study comparing manual segmentation, nnInteractive, and SLIP across three clinical annotation tasks, six expert participants, and subjective usability measures, addressing the limited human validation of interactive segmentation methods. SLIP achieves SOTA interactive segmentation performance across 13 public datasets while providing lower interaction latency, greater responsiveness, support for reversible prompting, and higher user preference than existing approaches.

---


### 139. [Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization](https://arxiv.org/abs/2607.22334)

**<font color=#1a73e8>作者：</font>** Hao Wang, Kun Yuan, Wenlin Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-weight language models from different families exhibit complementary capabilities, motivating their consolidation into a compact student through on-policy distillation (OPD). However, full-vocabulary OPD typically assumes a shared tokenizer, while existing cross-tokenizer methods may discard teacher probability mass or assign it to student tokens with unrelated content. We introduce Byte-Prefix Marginalization (BPM), which re-expresses the teacher's next-token distribution over the student vocabulary in a shared byte space. Specifically, BPM assigns each teacher token's probability to the longest student token whose byte representation is a prefix of the teacher token's bytes, aggregates mass mapped to the same student token, and places otherwise unmatched mass in an explicit residual category. This produces a vocabulary-complete, byte-aligned, and mass-preserving target for dense OPD. The target exactly recovers the teacher-induced byte-prefix marginal when the relevant prefix does not span multiple teacher tokens (a condition satisfied at more than 99% of training positions) and uses a mass-preserving, chain-factorized lower bound otherwise. Across Qwen3-32B, GLM-Z1-9B-0414, and MiniMax-M2.7 as teachers, BPM consistently outperforms current cross-tokenizer methods on six mathematics and programming benchmarks, improving six-benchmark avg@8 by 3.7-6.6 points over the strongest baselines.

---


### 140. [Beyond Binary Rooftop Mapping: A Four-Class Deep Learning Framework for Green Roof Potential Assessment from Open Swiss Geospatial Data](https://arxiv.org/abs/2607.22342)

**<font color=#1a73e8>作者：</font>** Htet Yamin Ko Ko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The development of effective urban climate adaptation strategies requires comprehensive spatial information on rooftops and buildings, since such information underpins the assessment of ecosystem services provided by green infrastructure, particularly for urban heat island (UHI) mitigation. Although green roofs are widely acknowledged as a promising measure for improving urban thermal comfort, most existing research maps either current green rooftops or rooftops with greening potential, but not both. This study presents a modified deep convolutional neural network rooftop classification framework based on Roofpedia, developed by the Urban Analytics Lab at the National University of Singapore. The proposed model combines high resolution aerial imagery with rooftop slope information derived from a digital surface model and relies entirely on publicly available Swisstopo datasets: SWISSIMAGE orthophotos, swissSURFACE3D elevation data, and swissTLM3D building footprints. Applied to Bern, Switzerland, the model labels rooftops into four categories: existing green roofs, rooftops suitable for green roof installation, rooftops with solar panels, and flat rooftops unsuitable for greening. The framework identifies realistic opportunities for green roof expansion and supplies urban planners with evidence-based information for green infrastructure deployment in Bern and other Swiss cities. Because it is fully open source, the framework is transferable to cities worldwide.

---


### 141. [IQ-JEPA: A Joint-Embedding Predictive Architecture with a Hermitian Vision Transformer for Sound Speed and Attenuation Estimation from Ultrasound IQ Data](https://arxiv.org/abs/2607.22351)

**<font color=#1a73e8>作者：</font>** Masashi Sode, Gianmarco Pinton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The speed of sound in tissue is a prerequisite for well-focused imaging and has diagnostic value, but recovering it from raw pulse-echo channel data is fundamentally a nonlinear inverse problem. Learned solvers are fast yet label hungry. Simulated sound-speed labels are expensive, while abundant real channel data is unlabeled. We propose IQ-JEPA to exploit both data types. An encoder is pretrained without labels to predict the latent representation of masked in-phase and quadrature (IQ) regions from visible context, then fine-tuned on simulated maps. Sound speed appears in the IQ signal as a phase difference, invariant to the constant phase offset. The encoder is a Hermitian vision transformer that operates on the complex signal directly. Its attention is equivariant to that phase and its conjugate-product feed-forward is invariant to it, so the encoder reads a quantity analogous to the one classical coherence methods use. On 79,293 Fullwave 2.5 simulations at 2.5 MHz, pretraining on the 63,435 unlabeled acquisitions reaches 15.60 m/s at 10,000 labels. This is a roughly threefold gain in label efficiency over supervised training, growing to over fourfold at 1,000 labels. It is about 2.2x below an InversionNet baseline, and 8.71 m/s at full labels. The gain still grows with more unlabeled pretraining data. Our comparisons point to self-supervision as the dominant factor. The same encoder transfers. Its frozen features expose sound speed and attenuation, and cross-distribution pretraining between layered and abdominal phantoms costs little accuracy. We see this as a first step toward a foundation model for quantitative ultrasound.

---


### 142. [SiPhy: Single-Image Physical Property Reasoning](https://arxiv.org/abs/2607.22355)

**<font color=#1a73e8>作者：</font>** Hoang Le, Joonwoo Kwon, Elkhan Ismayilzada 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inferring physical properties such as mass, stiffness, and elasticity from a single image is essential for simulation and embodied AI, yet most existing approaches rely on multi-view reconstruction or physics-based supervision. We introduce SiPhy, a unified framework for single-image physical property reasoning that aligns 3D-aware visual cues, depth with language-based material knowledge. From one RGB image, SiPhy samples pseudo-voxel points, extracts CLIP features, and grounds them to material candidates proposed by a VLM. A part-based contrastive aggregator enforces region consistency, while a heaviness-aware refinement improves thickness and volume estimation for dense objects. Across ABO-500, MVImgNet-100, and PhysXNet-100, SiPhy achieves state-of-the-art single-image performance, surpassing multi-view reconstruction methods by improving mass MnRE by up to 93% (vs. PUGS), reducing density MAE by 35.5% (vs. NeRF2Physics), and lowering Young's modulus error by 23.5%. We further validate SiPhy on real hand-object interaction datasets, demonstrating its potential as a data annotation engine for physical understanding from single-view imagery.

---


### 143. [Integrated Order Dispatching and Routing for Last-Mile Pickup via Deep Reinforcement Learning](https://arxiv.org/abs/2607.22356)

**<font color=#1a73e8>作者：</font>** Yida Xu, Zhaofang Mao, Yuheng Miao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, the growing complexity of last-mile pickup operations has increased the need for fast and accurate decision-making on logistics platforms. This challenge is fundamentally driven by two key and tightly coupled decision-making processes: order dispatching and routing. Solving them separately overlooks their interdependence, while fully end-to-end learning can be unstable and costly on large, variable-scale instances due to sparse rewards. To solve this problem, we propose an integrated optimization framework which couples a learned routing oracle with real-time dispatching heuristics. For the routing subproblem, we develop a Dynamic-Residual Graph Attention Network encoder with a Look-Ahead Courier-Personalized decoder. For the dispatching subproblem, we develop a routing-oracle-guided dispatching heuristic with local search, where the oracle provides near-optimal solutions to select candidate couriers while retaining real-time scalability. Extensive experiments on real-world datasets from Cainiao Logistics are used to test the performance of our approach, including an offline evaluation and an online rolling-horizon simulation. The experimental results show that our approach outperforms other benchmarks regarding solution quality and solving time, indicating it can effectively support logistics companies in solving real-time and large-scale last-mile pickup problems.

---


### 144. [Indexing: the Beginning and the End](https://arxiv.org/abs/2607.22361)

**<font color=#1a73e8>作者：</font>** Alexander Kozachinskiy, Vicente Opazo, Felipe Urrutia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study information bottlenecks in modern deep-learning architectures -- RNNs, softmax transformers, linear-attention transformers and state-space models -- through the lens of the indexing primitive. In this primitive, the input consists of $n$ bits and one integer $i$ from $1$ to $n$ called the index, and the output equals the value of the $i$-th bit.
We introduce causal complexity for masked architectures. We show that architectures with low causal complexity cannot solve the indexing primitive in any constant number of layers when the index appears at the end of the input. In particular, this limitation applies to low-parameter RNNs, SSMs and masked linear-attention transformers. In contrast, small softmax transformers can solve it in one layer, while non-masked linear-attention transformers can solve it in 2, which separates them from their masked counterparts. In turn, when the index appears at the beginning, we show that small RNNs are capable of solving this task in 1 layer, while all the other architectures require 2.
All our impossibility results are unconditional and apply even to models that employ infinite-precision real arithmetic. Moreover, experiments for up to $n=64$ qualitatively align with our theory: configurations with low-parameter theoretical solutions learn the indexing task easily, while configurations that do not admit such theoretical solutions struggle to learn as the sequence length grows.

---


### 145. [Learning Structural Convergence: A Neuro-Symbolic Benchmark for Temporal Reasoning](https://arxiv.org/abs/2607.22365)

**<font color=#1a73e8>作者：</font>** Michael Romei De Socio, Gian Luca Pozzato, Alessio Merlo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-complexity operational environments require methods that detect and anticipate temporally distributed patterns rather than classify isolated events. This paper introduces TRACTA (Temporal Reasoning and Capability-Trajectory Analysis), a controlled synthetic benchmark for temporal structural reasoning in high-complexity event-driven systems, instantiated through Multi-Domain Operations (MDO)-like scenarios. The benchmark includes three tasks: early_warning, pattern_detection, and run_classification, and compares raw-event neural models, a contract-lite semantic baseline, and a neuro-symbolic configuration operating on semantically grounded trajectories. Results show that raw event-level learning remains informative, but learned temporal modeling over semantic capability and contextual direct-impact trajectories achieves the highest aggregate point estimates, with the largest margins on the temporal tasks. Ablation analysis indicates that capability dynamics, contextual impacts, and temporal structure contribute complementary information. Shortcut diagnostics indicate that the most direct cross-run global-identifier shortcut is controlled in the primary neural input view, while residual shallow signals remain. Overall, the findings support a bounded methodological conclusion: in controlled synthetic settings, semantically grounded trajectories provide an effective representation for temporal structural reasoning, supporting further investigation of semantic interfaces between event data, structured representations, and temporal learning.

---


### 146. [Interior interpretability with attention rollout: contraction and propagation profiles in Transformers](https://arxiv.org/abs/2607.22367)

**<font color=#1a73e8>作者：</font>** Umberto Biccari, Qian Huang, Enrique Zuazua  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature-attribution methods assign scores relating input variables to a model's output, but do not by themselves characterize how explicitly defined interaction operators compose across its intermediate layers. We introduce \emph{interior interpretability}, a propagation-based perspective on internal model organization, and instantiate it for tabular Transformers using attention rollout. We interpret rollout as a row-stochastic operator encoding attention-mediated propagation between feature tokens. By applying classical Doeblin--Dobrushin contraction theory, we show that a rollout operator with a small Dobrushin coefficient is quantitatively close to a rank-one stochastic matrix whose common row is determined by its normalized column sums. This result gives a structural interpretation to the corresponding rollout propagation profile. In Transformers trained for metabolomic age prediction, the measured rollout contraction strengthens with depth. Trained and randomly initialized models also exhibit different propagation profiles, although the present experiments do not establish the predictive relevance of individual rollout-ranked variables. Exploratory comparisons with PCA and GradientExplainer approximations to SHAP reveal localized agreement among highly ranked variables but weak agreement across complete rankings. Attention rollout is therefore used here as a diagnostic of attention-mediated propagation, not as a causal explanation or faithful attribution of the complete Transformer.

---


### 147. [Active few-shot segmentation by reinforcing data selection](https://arxiv.org/abs/2607.22371)

**<font color=#1a73e8>作者：</font>** Chenlan Zhao, Benny Wong, Timothy F. Lundberg 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot learning enables medical image segmentation models to adapt to new tasks using only a small number of labelled examples. However, adaptation performance depends strongly on which examples are selected for the support set. Effective support sets should capture relevant variation within the target domain and be informative for adaptation, with constituent samples providing complementary information. Despite this, existing active data selection approaches largely prioritise samples individually and do not explicitly account for interactions between examples. In this work, we propose a reinforcement learning framework for support-set selection in few-shot medical image segmentation, enabling support sets to be optimised jointly rather than through independent sample scoring. Given a pool of unlabelled candidate images, an agent directly predicts a support set that maximises downstream segmentation performance. Experiments on a cross-institutional pelvic MRI dataset demonstrate improvements over random selection and current state-of-the-art methods. Our findings highlight the importance of support-set complementarity for effective adaptation and demonstrate the potential of reinforcement learning for optimising adaptation sets.

---


### 148. [A Factorial Study of Synthetic Data Generation for Low-Resource Machine Translation using Grammar Books](https://arxiv.org/abs/2607.22376)

**<font color=#1a73e8>作者：</font>** Varun Ghat Ravikumar, Sina Ahmadi, Lena Jäger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most endangered languages lack the parallel data required for machine translation, despite the existence of descriptive grammar books. We introduce a pipeline that uses large language models to extract grammatical rules, example sentences, and lexicons from grammar books and generate synthetic parallel corpora for fine-tuning-rather than feeding grammar content into prompts at inference time, as in prior work. Validated on three typologically diverse low-resource languages-Kalamang (Papuan), Tuatschin (Romance), and Mandan (Siouan)-we show that fine-tuning on synthetic data improves over seed-data baselines in 75% of configurations for Kalamang and 59% for Tuatschin, with best-case ChrF++ gains of +8.8, +5.3, and +3.3 respectively. Through a systematic factorial study across 96 configurations varying target part-of-speech, retrieval granularity, and sample volume, we identify which factor combinations drive gains and where they break down. Our results demonstrate that static linguistic documentation can be repurposed for machine translation fine-tuning, offering a practical path towards translation tools for severely under-resourced languages.

---


### 149. [Kutti AI: A Voice-First, Offline-Capable Learning Companion with Real-Time Struggle Detection for Visually-Impaired Children](https://arxiv.org/abs/2607.22377)

**<font color=#1a73e8>作者：</font>** Kadharmoideen Fadurudeen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Most educational technology for children is built around visual interfaces, which excludes the many children worldwide who live with visual impairment -- an estimated 1.4 million children are blind and many more have low vision. We present Kutti AI, a voice-first learning companion designed so that audio is the primary and sufficient interface: children learn curriculum concepts through spoken conversation, respond by speaking, and receive spoken feedback, with no reliance on visual elements. The system contributes three practical mechanisms for accessible, adaptive learning on commodity mobile hardware: (1) a multi-signal struggle-detection engine that combines response-latency analysis, wrong-attempt tracking, and keyword-based hesitation detection to decide, in real time, when to offer hints or simplify a question; (2) a multi-layered cross-language answer-matching pipeline that combines language-aware translation/transliteration, Levenshtein-based fuzzy matching, and text normalization so that children are not penalized for code-switching or pronunciation variation; and (3) an offline-first speech pipeline using an on-device automatic speech recognition (ASR) model, enabling use in low-connectivity settings common in underserved communities. We describe the architecture, the interaction flow, and the design decisions that prioritize accessibility, and we report qualitative observations from a hackathon prototype supporting English and Tamil. We discuss lessons learned and outline a path toward formal evaluation with target users. Kutti AI illustrates how a small, carefully-engineered voice-first system can lower both accessibility and financial barriers to early education.

---


### 150. [IR275K: A Benchmark for Infrared Multi-Frame Super-Resolution Toward Efficient Remote Sensing](https://arxiv.org/abs/2607.22380)

**<font color=#1a73e8>作者：</font>** Jie Deng, Heyang Wang, Changxin Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient processing is becoming increasingly important in infrared remote sensing, where satellite constellations produce large volumes of observations under constrained detector resolution, power, and downlink bandwidth. Multi-frame super-resolution (MFSR) offers a software-based route to spatial enhancement, but its evaluation in infrared sensing remains fragmented across private datasets and ad-hoc protocols. Existing benchmarks do not explicitly capture the thermal contrast, sensor noise, weak texture, and platform-induced frame-to-frame variation that characterize infrared video. We introduce IR275K, a curated benchmark containing 594 infrared video sequences and 275,196 frames. It provides sequence-level train/validation/test splits and a reproducible X4 evaluation protocol. As an initial architectural probe, we further evaluate CGMamba, a lightweight state-space model with 10.90M parameters and 112.14G FLOPs. CGMamba combines 2D rotary position encoding (2D~RoPE) with center-guided cross-Mamba (CGCM) fusion for implicit multi-frame reconstruction. It achieves 33.19dB PSNR, outperforming infrared single-image super-resolution references by 0.35--0.52~dB at substantially lower computational cost. Ablation results show that removing 2D~RoPE from CGCM causes a 1.53dB drop and severe grid-like artifacts. This indicates that explicit spatial anchoring is critical for stabilizing SSM-based cross-frame gating under infrared conditions. IR275K provides a reproducible foundation for accuracy--efficiency evaluation of infrared MFSR methods, while the architectural analysis offers a concrete starting point for spatially aware SSM design under resource-constrained infrared sensing. Dataset and evaluation resources are available at: this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-169](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
