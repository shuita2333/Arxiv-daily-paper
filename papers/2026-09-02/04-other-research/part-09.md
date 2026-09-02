# 📦 其他研究 | 2026年09月02日

> 本类共 **485** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-485](./part-10.md)

---

### 401. [Learning Materials Properties from Scarce Labels and Unlabeled Crystals](https://arxiv.org/abs/2608.30682)

**<font color=#1a73e8>作者：</font>** Wentao Li, Yizhe Chen, Jiangjie Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning materials properties from scarce labels and unlabeled crystals is a central challenge for data-driven materials discovery. We present SemiMat, a controlled benchmark for semi-supervised materials property regression, and MatRank, a reliability-weighted objective for continuous pseudo-label uncertainty. SemiMat fixes labeled and unlabeled crystal inputs, graph-backbone interfaces, validation-only checkpoint selection, held-out test reporting, normalized MAE (NMAE), and method-rank summaries across six scarce-label tasks, four graph backbones, and five predefined split runs. MatRank builds pseudo-targets from labeled anchors, weights them by local reliability and weak-prediction agreement, trains weak and strong graph views consistently, and adds ranking signals so that unlabeled crystals shape both values and candidate order. Across the retained 24 backbone-task blocks, one fixed MatRank objective gives the lowest aggregate held-out test NMAE (0.896) and best average method rank (2.208). The component, OOD, and generated-pool diagnostics identify where the gain is reliable and where further screening evaluation remains necessary. Code is available at this https URL.

---


### 402. [UFPR-PEs: A Brazilian Face Recognition Benchmark with Self-Declared Race/Color Labels](https://arxiv.org/abs/2608.30688)

**<font color=#1a73e8>作者：</font>** Alexandre Diano, Bernardo Biesseck, Gabriel Polo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While face recognition systems are widely deployed, ensuring their demographic reliability and robustness under uncontrolled visual conditions remains a critical challenge. To bridge this gap, we present UFPR-PEs, a benchmark for face recognition bias evaluation using public videos of elected Brazilian politicians annotated with official self-declared race/color categories. The dataset adopts the Brazilian census taxonomy, including the parda category, which has no direct equivalent in the U.S.- or Europe-centric schemas commonly used in prior benchmarks. Our benchmark is built from compressed public video and preserves difficult samples so that performance can be analyzed under realistic conditions. We describe the construction pipeline, report dataset statistics, and evaluate face recognition performance across verification and (closed- and open-set) identification settings, including subgroup analysis by race/color and difficulty level. The results show that recognition performance varies substantially with image quality, and that subgroup gaps must be interpreted jointly with visual difficulty rather than in isolation. Overall, UFPR-PEs provides a reproducible and demographically grounded setting for studying face recognition bias under challenging public video conditions.

---


### 403. [CANVAS: Consistency-Aware Navigation via Visual Adaptive Sampling for Long-Context Text-to-SVG Generation](https://arxiv.org/abs/2608.30689)

**<font color=#1a73e8>作者：</font>** Yichen Wu, Haoxuan Qu, Yihang Lou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive large models have recently advanced Text-to-SVG generation from simple icons to complex, long-context graphics, yet standard autoregressive decoding often fails to maintain global consistency across geometry, layout, occlusion, and composition. We introduce CANVAS (Consistency-Aware Navigation via Visual Adaptive Sampling), a training-free, render-aware inference framework that combines power-sharpened trajectory likelihood with visual feedback from rendered futures and derives a stroke-wise navigation rule. It effectively estimates each candidate stroke's future value under a limited generation and rendering budget and adaptively allocates samples according to candidate uncertainty, decision influence, and rollout cost. Experiments across multiple autoregressive SVG backbones and complementary benchmarks demonstrate improvements in global consistency, which includes sound geometric relationships, spatial layouts, occlusion ordering, and overall composition, without additional training, demonstrating the effectiveness and generalization ability of our framework.

---


### 404. [Failure or Drift? Evaluating Monocular SLAM under Synthetic and Real-World Corruptions](https://arxiv.org/abs/2608.30690)

**<font color=#1a73e8>作者：</font>** Abhay Skaria Thomas, Shashank Agnihotri, Margret Keuper  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual SLAM is commonly evaluated on clean trajectories, although deployment failures are often caused by adverse weather, illumination, blur, and sensor artifacts. Controlled corruptions are attractive because they isolate such factors, but a synthetic stress test is useful only when it leads to the same engineering conclusion as the condition it is intended to approximate. This work examines that question for monocular SLAM. We evaluate a classical feature-based system and two learned trackers under image-space, geometry-aware, and compound corruptions, and compare their behavior with adverse conditions from 4Seasons. Rather than reducing robustness to a single trajectory error, the evaluation separates explicit tracking failure from drift accumulated by methods that remain active. The results show that learned trackers largely replace catastrophic loss with sustained, and sometimes severe, drift. More importantly, the apparent ordering of the learned systems changes with the physical fidelity of the corruption: structured rain and fog proxies preserve the real-world ordering, whereas a simple illumination proxy does not. Code is available at: this https URL.

---


### 405. [Liquid Gated Attention](https://arxiv.org/abs/2608.30695)

**<font color=#1a73e8>作者：</font>** Yiheng Jiang, Yuanbo Xu, Yongjian Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time series often exhibit irregular sampling and extended temporal horizons, requiring models to capture continuous-time dynamics across arbitrary intervals without prohibitive scaling costs. Discrete-time methods collapse variable time intervals into static positional steps; solver-dependent continuous-time models preserve temporal structure but rely on sequential integration, precluding parallelization; and solver-free approximations avoid this cost yet none couples observed time intervals with input-driven state modulation. We propose Liquid Gated Attention (LGA), a solver-free parallel temporal operator. By parameterizing an input-driven gating mechanism with observed time intervals, LGA introduces a continuous-time inductive bias and formulates hidden state evolution as a fast-weight associative memory, enabling parallel computation across the temporal dimension. Using matrix associativity in non-causal encoding and a prefix scan in causal encoding, LGA attains linear temporal complexity in sequence length in both modes. A sequence-level normalization bounds cumulative temporal decay for stable long-horizon optimization. Building on LGA, we instantiate LFormer, a modular backbone for continuous-time representation learning. Across six tasks and sixteen datasets spanning up to 17,984 steps, LFormer demonstrates long-range dependency modeling, fine-grained state tracking, and trajectory reconstruction from sparse and noisy observations, while delivering competitive performance against state-of-the-art discrete-time and continuous-time baselines with linear scaling efficiency.

---


### 406. [Learning Dynamics of Logits Debiasing for Long-Tailed Semi-Supervised Learning](https://arxiv.org/abs/2608.30699)

**<font color=#1a73e8>作者：</font>** Yue Cheng, Jiajun Zhang, Xiaohui Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-tailed distributions are prevalent in real-world semi-supervised learning (SSL), where pseudo-labels tend to favor majority classes, leading to degraded generalization. While many long-tailed semi-supervised learning (LTSSL) methods have been proposed, the mechanisms by which they implicitly debias logits remain poorly understood. In this work, we revisit LTSSL through the lens of learning dynamics and provide a theoretical characterization of logits debiasing. Specifically, we derive a step-wise decomposition of the logits updates, showing that predictions are dominated by class-imbalance bias that reliably reflects label priors. To expose this effect, we use the logits of a task-irrelevant baseline image as an indicator of accumulated bias and prove that they converge to the class prior. This provides a unified view where LTSSL remedies such as logit adjustment, reweighting, and resampling correspond to reshaping gradient dynamics. Based on this insight, we propose DyTrim, a principle-based dynamic pruning framework that reallocates gradient budget through class-aware pruning on labeled data and confidence-based soft pruning on unlabeled data. We provide theoretical guarantees that DyTrim reduces class bias and improves generalization. Extensive experiments on standard LTSSL benchmarks show consistent gains across architectures and methods. Code available at: this https URL

---


### 407. [RailSyn: Diagnosis-Guided Image Generation for Traceable Data Completion in Railway Foreign Object Detection](https://arxiv.org/abs/2608.30709)

**<font color=#1a73e8>作者：</font>** Quan Hao, Chenxi Zhang, Ziyang Tao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Railway foreign object detection (RFOD) is critical to safe railway operation, yet scarce real positive samples incompletely represent task-relevant variations in object scale, intrusion relation, railway scene, illumination, and adverse weather. Existing synthetic augmentation can improve RFOD detection, but its gains lack an explicit account of the task-relevant deficiencies complemented by the generated data. We therefore introduce RailSyn, a diagnosis-guided framework comprising a real-referenced Inspector and a requirement-aligned Generator. The Inspector constructs a variable-radius empirical cover from finite real observations to localize candidate completion regions and profile synthetic pools. The resulting audit identifies railway-context, intrusion-semantic, and visual-consistency requirements; the Generator addresses them through domain adaptation, agent-planned placement and physical contact relations, and plan-consistent conditional refinement. Using the Inspector, we further trace representation-space changes across generation variants; the complete system attains a local-shell occupation of $C_{gap}$ to 13.64%, which measures generated coverage of real-derived completion regions. Extensive experiments show AP50--95 gains of up to 4.9 points and consistent improvements across nine mainstream detectors, demonstrating broad cross-architecture utility.

---


### 408. [Kolmogorov--Arnold against bounded translations](https://arxiv.org/abs/2608.30710)

**<font color=#1a73e8>作者：</font>** Sviatoslav V. Dzhenzher  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Historically originating from Hilbert's 13th problem, the Kolmogorov-Arnold representation theorem (KART) has recently experienced a major revitalisation through its applications to neural networks, specifically Kolmogorov-Arnold Networks (KANs). While the exact representation is well established, its stability under continuous adversarial perturbations of the hidden layer remains a critical open question. In this paper, we investigate the robustness of KART against bounded adversarial translations. We provide an explicit, self-contained, and constructive proof of an approximate representation using fixed, piecewise linear inner functions. Crucially, our construction employs a single outer function that remains invariant for all summands and is independent of the specific adversarial translation, provided its maximum bound is known a priori.

---


### 409. [SegWave: Wavelet-Driven Segmentation of Tampered Regions](https://arxiv.org/abs/2608.30714)

**<font color=#1a73e8>作者：</font>** Siddhi Pravin Lipare, Vishesh Kumar, Akshay Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Verifying image authenticity is increasingly difficult, posing serious risks across journalism, law enforcement, and political domains. Most existing forensic methods rely on high-level visual artifacts and treat frame detection as a simple binary task. To address this, we propose SegWave, a hybrid framework that jointly leverages spatial and frequency-domain cues for image tampering detection. SegWave integrates a transformer-based architecture with the Discrete Wavelet Transform (DWT) to capture localized, multi-scale frequency inconsistencies indicative of manipulation. To further improve localization effectiveness, we introduce an Adaptive Sub-band Attention module (ASA) that dynamically highlights the informative high-frequency wavelet components. Extensive experiments on multiple benchmark datasets demonstrate that SegWave consistently outperforms state-of-the-art tampering detection methods in challenging evaluation settings.

---


### 410. [Mind the Gap: Theory-of-Mind-Grounded Friction for Epistemic Alignment](https://arxiv.org/abs/2608.30719)

**<font color=#1a73e8>作者：</font>** Yifan Zhu, Kyeongmin Rim, James Pustejovsky  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Productive dialogue alignment requires distinguishing \emph{surface coordination} (acknowledgments and smooth task progression) from \emph{epistemic alignment} (convergence of belief states); standard preference-based methods typically optimize response-level preferences without explicitly modeling the latter. We operationalize Theory-of-Mind (ToM) inference as a control signal within Frictive Policy Optimization by extracting, at each referring expression, a four-part belief structure: the speaker's intended referent, the addressee's interpretation, and each participant's model of the other's belief. This makes friction mechanically computable from epistemic-state comparisons, capturing \emph{silent divergence}, where both participants proceed confidently while grounding to different referents. We evaluate the signal at two levels. At the representation level, ablating the second-order channel reduces misunderstanding recall from $65\%$ to $26\%$. At the policy level, reward-shaping (FAR) and trust-region (FTR) variants improve intervention F1 and warranted-context calibration over DPO, with Brier scores independently supporting the calibration gains. Across three training runs, FAR and FTR remain substantially more stable, whereas DPO varies widely and can degrade intervention competence already present in the base policy. Thus, ToM-grounded friction provides a trainable signal for context-sensitive intervention under referential belief divergence.

---


### 411. [Where Do Multilingual Vision-Language Encoders Fail on Low-Resource Languages?](https://arxiv.org/abs/2608.30725)

**<font color=#1a73e8>作者：</font>** Donghoon Han, SungHyun Moon, Aidyn Zhakatayev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent multilingual vision--language encoders cover hundreds of languages in a single model, yet on two state-of-the-art instances retrieval on low-resource languages (LRL; e.g. Swahili) trails high-resource ones (HRL; e.g. English) by $30^+$\,pp. We ask where in the trained encoder this gap is located. Prior modality-gap and cross-lingual subspace work suggests a linear language direction at the output crowds out alignment-relevant geometry. We falsify this: LEACE drives the linear language classifier from $>99\%$ to near chance and iterated INLP to $37$--$50\%$ while LRL retrieval moves within $\pm 1.5$\,pp and all tier means within $2.2$\,pp, tracking random controls. The linear bias is a \emph{symptom}, not the cause. Instead, the alignment-causal factor lies along the encoder's forward path: the EOS (end-of-sequence) hidden state's per-language trajectory diverges with depth. Substituting the EOS with its parallel English value three blocks before the projector lifts Swahili from $22.1\%$ to $69.1\%$ on one encoder (and reproduces on the other); three controls rule out pooled-position tautology and English specificity. A front-layer trunk that pulls each language's projection toward the parallel-content centroid corroborates the diagnosis at training time, recovering $+9.6$ / $+17.1$\,pp on LRL XM3600 retrieval (1{,}000-image subset), with consistent gains across three further benchmarks while preserving HRL performance.

---


### 412. [RailGen: Improving Railway Intrusion Detection via Agent-Guided Small-Scale Foreign Object Generation](https://arxiv.org/abs/2608.30727)

**<font color=#1a73e8>作者：</font>** Quan Hao, Ziyang Tao, Chenxi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small-object detection under long-tailed data distributions is a fundamental yet challenging problem in multimedia. Railway Foreign Object Detection (RFOD) epitomizes this challenge with easily confused small intrusions and scarce samples. To address these issues, we propose a generative-augmented detection paradigm that leverages multimodal image generation to enrich the feature space of rare and small objects. We first construct RailGen, a multimodal image generation agent based on large models. Under semantic constraints, RailGen automatically invokes tools to generate railway scenes, calibrate intrusion positions, extract foreign objects, and fuse them into realistic intrusion effects. This process produces high-quality synthetic samples that effectively densify the feature representations of tail classes and complete the small-object feature space. Within this paradigm, we further propose FocalDEIM, a detection framework designed to enhance training with generated data. FocalDEIM improves dense matching with Focal Modulation for better small-object discrimination and adopts Focal Loss to emphasize hard samples, thereby alleviating blurred inter-class boundaries in complex railway scenes. Experimental results demonstrate that RailGen can generate high-quality small-scale foreign objects, reducing the object pixel area by up to 58x and 13.85x on average. Equipped with these challenging samples, our paradigm surpasses the baseline DEIM by 5.6% and 7.5% in mAP@50 and mAP@(50-95), respectively, and outperforms existing state-of-the-art methods. Ablation studies verify RailGen's feature-space enrichment and FocalDEIM's boundary discrimination. The paradigm provides an effective multimodal generative solution for long-tailed small-object detection in safety-critical applications.

---


### 413. [Not All Fallbacks Are Failures: Understanding and Recovering from Fallbacks in Mobile Voice Assistants](https://arxiv.org/abs/2608.30738)

**<font color=#1a73e8>作者：</font>** Phillip Schneider, Alexandre Mercier, Joshua Oehms 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Robust understanding of user input is a core requirement for voice assistants deployed in real-world environments. In practice, these systems encounter heterogeneous fallback situations caused by noisy audio input, transcription errors, ambiguous requests, incomplete utterances, or unintended activations. Existing systems typically respond with generic fallback messages, which do not resolve the underlying interaction failure and can degrade user experience. We study fallback handling in a deployed smartwatch-based voice assistant for general health support in everyday environments. Our analysis is based on six months of real-world usage data from more than 500 users, yielding a dataset of 3,030 anonymized, naturally occurring fallback-triggering utterances. We contribute (1) an operational taxonomy and the annotated VoxFallbacks dataset of these interactions, (2) a comparative evaluation of different models within a classification pipeline under practical deployment constraints, and (3) practical lessons for designing robust and cost-efficient fallback mechanisms. Results show that lightweight embedding-based classifiers outperform larger generative models on most classification tasks while requiring substantially fewer computational resources.

---


### 414. [Functional Degeneracy in Neural Networks: Measurement and Pruning](https://arxiv.org/abs/2608.30741)

**<font color=#1a73e8>作者：</font>** Maria Matveev, Pascal Esser, Ayush Bharadwaj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central question in modern machine learning is how much a trained model can be compressed without changing its behavior, to reduce the memory, compute and energy required to deploy it. To study this, we quantify functional degeneracy through the behavioral recovery rank, defined as the number of leading behavioral-Hessian eigendirections required to recover a trained model's performance. Using the behavioral recovery rank as a geometric benchmark for compression, we find that structural and magnitude pruning retain more degrees of freedom, even after the task is saturated. This gap suggests that functional redundancy is distributed across parameter directions and is not exposed by individual weights or neurons.

---


### 415. [TDDM-Melatt: A Decoupled Memory and Diffusion Framework for Generalizable Encrypted Traffic Classification](https://arxiv.org/abs/2608.30745)

**<font color=#1a73e8>作者：</font>** Ze Chen, Qiming Yu, Zijia Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of encrypted traffic poses severe challenges to current security situational awareness systems based on network traffic monitoring. In existing dataset-driven training and testing studies, limitations such as shortcut learning induced by spurious feature correlations and sample imbalance caused by the long-tail distribution of real-world traffic result in weak generalization of traffic identification performance to real-world network traffic. To address these limitations, we propose TDDM-Melatt, a disentangled memory-based traffic classification framework with diffusion-based data augmentation. First, we design Melatt, a memory-decoupled traffic representation model, which employs Competitive Gating Long Short-Term Memory (CG-LSTM) to construct the encoder and decoder. We design a spurious-correlation-free pre-training and inference paradigm, employing strict topology anonymization and a frozen pre-trained encoder strategy to cut off the model's learning pathways for spurious features. During inference, classification is performed efficiently by a downstream classifier on the frozen representations. Second, we propose a Traffic Denoising Diffusion Model (TDDM) tailored to the characteristics of traffic data. Extensive experiments are conducted on 4 representative public benchmark datasets. Under strict flow-level splitting and anonymization, TDDM-Melatt outperforms 6 basic classification models and 6 SOTA representation learning models. The proposed method provides a new and effective technical pathway for encrypted traffic classification in real-world network environments.

---


### 416. [Which Rules Matter Now? Policy-Centroid Routing Before an Intelligent System Acts](https://arxiv.org/abs/2608.30757)

**<font color=#1a73e8>作者：</font>** Thomson D. Nguy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before an intelligent system can decide whether an action is allowed, it must first know which rules the action has approached. A single proposed action can implicate several policy regimes at once. Their requirements may stack, overlap, or qualify one another, yet many remain written in natural language while the action itself arrives as an incomplete description of intent. The first problem is not judgment. It is attention.
Policy-centroid routing creates a layer before adjudication. It compresses expressions within each policy regime into one or more representative centroids, places the proposed action in the same semantic space, applies a declared measure, and routes every regime crossing a declared threshold to authoritative review. Several regimes may trigger at once. The output is a review agenda, not permission, prohibition, legality, breach, compliance, certification, or enforcement.
The paper develops six falsifiable propositions and seven follow-on studies comparing the hypothesis with structured workflows, lexical and semantic retrieval, hierarchical and direct classification, and selective prediction under matched review burden. The studies are designed to identify where policy geometry recovers applicable regimes, where compression loses rare or overlapping obligations, and where the mechanism should abstain. The paper includes a synthetic worked example and reports no empirical efficacy result.

---


### 417. [ChessQueries: Toward Better Chess Board Recognition](https://arxiv.org/abs/2608.30762)

**<font color=#1a73e8>作者：</font>** Joël Seytre  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chess board recognition is the task of mapping the image of a chess board to the information of which piece is on which square. So far this task has two established benchmarks: ChessCog is synthetic, and ChessReD comes from smartphone pictures of a single chess board setup. We introduce ChessQueries, a new method combining a ViT encoder with a DETR-style decoder, which outperforms existing methods. On the ChessReD benchmark, we improve the state of the art from 15.3% to 99.2%, and demonstrate strong capabilities on out-of-distribution datasets. Our method saturates the task on the two datasets, with an average 0.01 wrong squares per board (vs. SotA: 3.4 / 0.15 respectively). We also share a new, harder public dataset, parsed from broadcasted top-level chess tournaments. Code, model weights and the SLCC data will be released.

---


### 418. [T3S: Improving Multi-Task Reinforcement Learning with Task-Specific Feature Selector and Scheduler](https://arxiv.org/abs/2608.30765)

**<font color=#1a73e8>作者：</font>** Yuanqiang Yu, Tianpei Yang, Yongliang Lv 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task reinforcement learning (MTRL) is a technique to train multiple tasks simultaneously, where previous works usually train a single model to solve different tasks by sharing parameters across various tasks. However, these methods are faced with inter-task interference since what parameters should be shared across tasks is not addressed, dramatically reducing learning efficiency. To solve these problems, we propose a novel MTRL framework called Task-Specific feature Selector and Scheduler (T3S), which consists of two components: a feature selector and a task scheduler. Specifically, the feature selectors employ hypernetworks to construct task-specific soft masks, which can be applied by globally shared representation to construct task-specific features. The task scheduler selects tasks for learning through two metrics, where the selection probability is inversely proportional to task progress (e.g., success rate) and task learning speed. Experimental results show that T3S consistently outperforms the state-of-the-art MTRL algorithms on various robotics manipulation tasks.

---


### 419. [CORAL: A Benchmark for Structure-aware and Brain-wide Neuron Reconstruction in Light Microscopy](https://arxiv.org/abs/2608.30768)

**<font color=#1a73e8>作者：</font>** Zekang Yang, Jiamin Li, Zhenghua Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic neuron reconstruction from light microscopy images is a central problem in computational neuroanatomy. While recent methods have achieved encouraging results on local image blocks, it remains unclear whether such progress translates to reconstruction that is both structurally accurate and scalable to the whole-brain scale. We present CORAL, the first benchmark for structure-aware evaluation of automatic neuron reconstruction from light microscopy images at both local and whole-brain scales. Built on a high-quality whole-brain fMOST dataset with carefully curated annotations, CORAL establishes two progressive tasks: block-level reconstruction, which evaluates reconstruction methods under limited spatial context, and brain-wide reconstruction, which assesses complete neuron reconstruction at the whole-brain scale. To account for topological correctness beyond geometric distance similarity, we introduce a structure-aware metric based on fiber prediction. To further achieve complete neuron reconstruction across the entire brain, we develop a brain-wide neuron tracing framework that extends arbitrary local reconstruction methods to the whole-brain scale through an iterative local-to-global process. Using this benchmark, we provide the first structure-aware comparison of mainstream methods for local neuron reconstruction and further evaluate their performance in brain-wide reconstruction. Our results underscore the importance of structure-aware evaluation and the need for more robust methods for complete neuron reconstruction.

---


### 420. [Reciprocity Separates Gradient Flow from Rotation in Conservative Physical Learning](https://arxiv.org/abs/2608.30778)

**<font color=#1a73e8>作者：</font>** Ruiwu Niu, Xiaowen Bi, Michaël Antonie van Wyk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical learning lets a trainable material or network use its own physical response to carry error signals, reducing the need for a separately programmed backward computation. We ask what determines whether such a system follows conventional gradient descent or evolves along a genuinely different learning trajectory. Our canonical model is a directed layered transport network in which every node redistributes a fixed amount of flow, so learning preserves positivity and total mass. In this model, conservation constrains only the allowable learning directions. Within the matched response class studied here, adjoint matching gives the physical output response a symmetric form. Non-negative mode-wise feedback then produces a reciprocal closed-loop response and a reweighted gradient flow. Adding an antisymmetric boundary component makes the closed-loop response rotational: the learning path can turn while the error driving that update still decreases at that moment. Turning is not automatically beneficial. Its finite-step effect is set by local curvature, and its accumulated effect also depends on step selection and on the new states visited along the path. Numerical consistency checks reproduce the exact response structure, predict the sign of the local effect across new network families, and show how trajectory drift can negate a local advantage. These results separate the roles of conservation, reciprocity, and nonreciprocity in physical learning.

---


### 421. [PixelIR: Fidelity-Perception Decoupling via Pixel-Space Image-Residual Flow Matching for Efficient One-Step Real-World Super-Resolution](https://arxiv.org/abs/2608.30782)

**<font color=#1a73e8>作者：</font>** Bingtian Qiao, Yue Shi, Yong Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image super-resolution (Real-ISR) aims to preserve structures supported by the degraded observation while reconstructing perceptually realistic details. However, existing Real-ISR methods largely optimize fidelity and perceptual quality within a shared network, causing the two objectives to interfere throughout training and making their balance difficult to control. Recent one-step methods reduce sampling steps, yet often inherit both this coupled optimization behavior and the expensive high-resolution backbone of their multi-step predecessors. We argue that efficient Real-ISR requires not only a shorter sampling trajectory, but also specialized modeling of faithful reconstruction and perceptual detail synthesis. Based on this insight, we propose PixelIR, a fidelity-perception decoupling framework built upon pixel-space image-residual flow matching. PixelIR first learns an image flow that maps the degraded observation to a faithful reconstruction. Then, a residual flow synthesizes the missing perceptual details from noise without repeatedly relearning or overwriting the complete restoration solution. We further distill the teacher into a deployment-oriented one-step student within a coarse-to-fine pyramid architecture. Extensive experiments show that PixelIR achieves leading PSNR, SSIM, and LPIPS on both RealSR and DRealSR. The final model completes pixel-space restoration in a single evaluation with only 32.9M parameters, 89.7G MACs, and 8.5ms latency, demonstrating a strong practical fidelity-perception-efficiency balance.

---


### 422. [Camera trap classification with deep learning under ground truth uncertainty](https://arxiv.org/abs/2608.30789)

**<font color=#1a73e8>作者：</font>** Leonard Hockerts, Peter S. Stewart, Sarthak Arora 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised deep learning methods enable the rapid processing of ecological image data, but depend on a costly annotation process. Consequently, training labels are commonly derived from volunteer citizen science projects. However, disagreement among volunteers introduces uncertainty in the "ground truth" data that are assumed to be correct for model training and validation. Using two datasets containing camera trap images with associated volunteer and expert classifications, we investigated the effects of training under higher ground truth uncertainty. We observed improved overall test accuracy, particularly for images that were more difficult for volunteers. Species-level accuracy also generally improved, but generalisation to a different dataset did not. The benefits of ground truth uncertainty were enhanced by pre-training on ImageNet. Pre-training also reduced the number of training epochs required; further reductions in computational cost, but not gains in accuracy, resulted from additional pre-training on other camera trap images. With unbalanced training data, we still observed a clear benefit of increased ground truth uncertainty for overall accuracy, especially on difficult images. Class imbalance improved accuracy for common species, reduced rare species accuracy, and changed patterns of misclassification to more closely resemble mistakes made by volunteers. Our findings have implications for applying deep learning across ecological image types with multiple labels. Practitioners can improve accuracy, especially on difficult examples, by including moderate levels of label disagreement during training and using models pre-trained on general image data. In addition to improving the use of citizen science-derived labels in model training, our study suggests avenues for more effectively integrating human and deep learning classifications in combined workflows. (abridged)

---


### 423. [LipCoder: Voice-Enabled Coding Toolkit](https://arxiv.org/abs/2608.30793)

**<font color=#1a73e8>作者：</font>** Hayoon Kim, Sungho Lee, Juhwi Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-assisted programming environments have accelerated software development, giving rise to new paradigms like vibe coding. However, their benefits remain largely inaccessible to visually impaired programmers, as existing screen readers and assistive tools offer limited support for these emerging workflows. We introduce LipCoder, a voice-centric programming toolkit designed to deliver editor-level functionality through auditory and speech-based interfaces. LipCoder offers features comprising speech feedback and earcon cues for comprehension and validation, as well as natural language input for navigation and modification. In an exploratory evaluation, 5 visually impaired programmers performed a series of coding tasks comparing LipCoder with a baseline of VSCode, Copilot, and VoiceOver. Quantitative trends and qualitative feedback point to directions for auditory-first design that may broaden accessibility in speech-driven coding environments.

---


### 424. [Geometric Attractor Monitoring: A Robust and Frugal Framework for Multi-modal Industrial Robotic Cycles](https://arxiv.org/abs/2608.30804)

**<font color=#1a73e8>作者：</font>** Martin Bonsergent-Brachet, Jesse Read, Dany Abboud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monitoring the health of heterogeneous industrial robot fleets is severely challenged by the multi-modal nature of their operational cycles and a persistent scarcity of run-to-failure data. Standard data-driven approaches, particularly deep learning architectures relying on sequential reconstruction, often struggle in this specific setting; they tend to over-smooth complex dynamics, masking early signs of degradation. To address these industrial constraints, we reframe the monitoring problem through a framework based on Phase Space Reconstruction (PSR). Instead of predicting temporal sequences, this framework transforms univariate sensor data into a geometric attractor, explicitly unfolding the mechanical states independently of their temporal occurrence. By evaluating various anomaly scoring techniques within this space, we demonstrate that discrete support estimation provides an effective and computationally frugal Health Indicator (HI). Validated on a real-world dataset of 21 heterogeneous robots over three years and a synthetic Langevin system, our approach outperforms standard deep learning baselines. We show that aligning the algorithmic bias with the geometric properties of the target system yields a pragmatic, traceable and easily deployable approach perfectly tailored to the realities of industrial constraints.

---


### 425. [What Emerges and What Breaks in Self-Play Driving](https://arxiv.org/abs/2608.30819)

**<font color=#1a73e8>作者：</font>** Laur Sisask, Ardi Tampuu, Tambet Matiisen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training autonomous driving policies through pure self-play has recently shown promising results. Following Gigaflow and Puffer- Drive, we train driving policies in a similar self-play fashion, but extend the models from MLPs to Transformers and train on the high-definition map of a real city, where we ultimately aim to deploy them. On the CARLA and Waymax benchmarks, our policies fall short of Gigaflow, and we trace the gap to specific failure modes, including reward hacking at traffic lights and a missing incentive to stop at stop signs. We further analyze which traffic rules emerge from self-play and how closely they match human driving, and we confirm that reward conditioning yields the intended diversity of driving behaviors. A demonstration of a trained policy is available at this https URL.

---


### 426. [RealOOB: A Definition-Consistent Real-World Oriented Occlusion Boundary Benchmark](https://arxiv.org/abs/2608.30820)

**<font color=#1a73e8>作者：</font>** Lintao Xu, Yinghao Wang, Chenchu Rong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Occlusion boundaries (OBs) are pixel-level image boundaries corresponding to surface visibility discontinuities caused by occlusion. Through precise boundary localisation and occlusion orientation, OBs encode local surface layout and depth ordering, providing geometry-driven mid-level cues for scene understanding. However, progress in pixel-level OB estimation has been limited by fragmented supervision: Existing benchmarks often suffer from limited coverage, category-specific designs, missing self-occlusion annotations, or inconsistent annotation definitions. Meanwhile, modern edge detectors and monocular depth estimators have become strong boundary and geometry predictors, yet their relationship to definition-consistent OBs remains underexplored. We introduce RealOOB, a carefully annotated real-world benchmark with 4.26M definition-consistent, geometry-grounded OB labels covering both inter-object and self-occlusion boundaries, together with validity-aware occlusion-orientation maps that restrict supervision to pixels whose cross-boundary depth ordering is reliably measurable. Based on RealOOB, we evaluate forty OB estimators and edge detectors alongside six monocular depth estimators. Our evaluation reveals a clear gap in occlusion reasoning: modern edge detectors perform competitively with OB methods in localisation, whereas orientation prediction remains challenging for all evaluated methods. Meanwhile, even strong depth estimators often fail to exhibit measurable geometry at true OBs. We believe RealOOB provides a strong reference benchmark for the OB estimation community and a real-world testbed for assessing depth discontinuities and geometry fidelity in broader low-level vision tasks. Dataset and code will be released.

---


### 427. [Whole-Body MRI Classification via Prompt-Based Clinical Conditioning](https://arxiv.org/abs/2608.30824)

**<font color=#1a73e8>作者：</font>** Laura Daza, Marta Hasny, Cristina González 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Combining whole-body magnetic resonance imaging (WB-MRI) with clinical variables has the potential to improve systemic disease diagnosis by leveraging complementary sources of patient information. However, structured clinical variables are often incomplete or missing, limiting the applicability of conventional multimodal fusion methods that assume fixed inputs. In this work, we propose TACTIC (Tabular-Attribute Conditioned Transformer for Image Classification), a prompt-based multimodal framework that integrates WB-MRI and structured clinical data through conditional visual feature learning. By encoding clinical attributes as prompts, TACTIC supports an arbitrary number of tabular inputs and naturally handles missing data without requiring imputation or fixed input structures. We evaluate TACTIC on five WB-MRI classification tasks spanning systemic and oncologic applications, including diabetes, chronic obstructive pulmonary disease (COPD), breast cancer, prostate cancer, and metastasis diagnosis. Across all tasks, TACTIC consistently improves performance over image-only baselines when clinical information is available while maintaining strong predictive capability under incomplete tabular inputs. Our results demonstrate the effectiveness of prompt-based models as a flexible approach for improving WB-MRI analysis using clinical context. The model weights and code are available at this https URL

---


### 428. [Opinionated, Hesitant and Stressed: Three Studies of How Politicians Speak in Four Slavic Parliaments](https://arxiv.org/abs/2608.30828)

**<font color=#1a73e8>作者：</font>** Ivan Porupski, Nikola Ljubešić  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present three large-scale studies of spoken parliamentary speech across four Slavic languages (Croatian, Czech, Polish, Serbian), drawing on over 6,000 hours from the ParlaSpeech 3.0 corpus. The first study examines how utterance-level sentiment shapes acoustic realisation: negative speech is consistently produced with higher pitch, greater intensity, and faster rate across all four parliaments, with a secondary arousal-driven upturn at the most positive extreme. The second study models filled pause frequency using negative binomial GEE, finding that speech rate, age, and sentiment are robust cross-lingual predictors, while gender effects reverse between South Slavic (men produce fewer filled pauses) and West Slavic parliaments (no gender difference) - a pattern invisible to single-language designs. The third study investigates primary stress variation in Croatian, showing that speaker-level preferences for early versus late stress cohere across verbs, adjectives, and nouns but decouple for adverbs and proper nouns. We conclude with a research agenda spanning corpus phonetics, disfluency modelling, and political rhetoric.

---


### 429. [Reliable Benchmarking of Artifact Detection in Computational Pathology: A Reproducibility and Uncertainty Analysis](https://arxiv.org/abs/2608.30835)

**<font color=#1a73e8>作者：</font>** Konstantinos Moutselos, Ilias Maglogiannis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background and Objective: Quality control is a prerequisite for whole-slide image analysis, yet the benchmarks on which quality-control methods are compared share four properties that make their reported differences hard to interpret: few independent slides, annotation concentrated in a minority of them, pooled ratio metrics with no closed-form standard error, and a single inherited train/test partition. We propose a reliability protocol for such benchmarks. Methods: The protocol quantifies four sources of variability - test-set sampling, training stochasticity, partition composition, and undocumented preprocessing - a claim is reportable only if it survives all four; three of the four cost minutes of compute. We apply it to an independent reconstruction of a published diffusion-based artifact detector, evaluated on the original 24-slide partition and against a supervised baseline. Results: The method's central mechanism reproduces: the auxiliary contrastive term improves pooled F1 from 0.673 to 0.688 and replicates under a second seed (+0.0156, p = 0.031; +0.0190, p = 0.005), although it acts on pen marking rather than the artifact types cited to motivate it. Its comparative claims do not: differences between design variants, and against the supervised baseline, fall inside the uncertainty of the evaluation. Four of 24 slides carry 70% of scored annotated pixels, giving an effective sample size of 6.2, and the inherited partition sits at the 7th percentile. An unreported tissue-restriction step excludes 41.4% of out-of-focus annotation against 2.6% of air bubble; such a gate is confounded with blur by construction. Conclusions: Small-cohort benchmarks support far weaker conclusions than current reporting implies. The four checks are cheap enough to accompany any evaluation on such a resource and separate reproducible effects from differences the evaluation cannot resolve.

---


### 430. [Physical Adversarial Examples for Person Detectors in Thermal Images Based on 3D Modeling](https://arxiv.org/abs/2608.30839)

**<font color=#1a73e8>作者：</font>** Xiaopei Zhu, Siyuan Huang, Zhanhao Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal Infrared detection is widely used in autonomous driving, medical AI, etc., but its security has only attracted attention recently. We propose infrared adversarial clothing designed to evade thermal person detectors in real-world scenarios. The design of the adversarial clothing is based on 3D modeling, which makes it easier to simulate multiangle scenes near the real world compared to 2D modeling. We optimized the black patch layout pattern of 3D clothing based on the adversarial example technique and made physical adversarial clothing using the aerogel. The idea is to paste a set of square aerogel patches, which display black squares in thermal images, in the inner side of clothing at specific locations with specific orientations. To enhance realism, we propose a method to build infrared 3D models with real infrared photos and develop texture maps for 3D models to simulate varied infrared characteristics over time and location. In physical attacks, we achieved an attack success rate of 80.11\% indoors and 76.85\% outdoors against YOLOv9. In contrast, randomly placed patches yielded much lower success rates (26.53\% indoors and 23.03\% outdoors). The adversarial clothing also showed good transferability to unknown detectors with an ensemble attack method, demonstrating the effectiveness of our approach.

---


### 431. [Pretrained, Curriculum-Tuned, and Ensembled: A Tracer-Aware Interactive Segmentation Pipeline for AutoPET V](https://arxiv.org/abs/2608.30844)

**<font color=#1a73e8>作者：</font>** Xinglong Liang, Chunyao Lu, Tianyu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive lesion segmentation in whole-body PET/CT requires a model to provide a strong initial prediction while also responding efficiently to sparse corrective scribbles during inference. This setting is particularly challenging because tracer distributions, physiological uptake patterns, lesion appearance, and acquisition characteristics differ substantially between FDG and PSMA studies. We present TRIAGE, Tracer-aware Refinement via Interactive Anatomy-Guided sEgmentation. The core backbone is a 3D STU-Net initialized through masked autoencoding pre-training with an asynchronous masking strategy, aiming to learn transferable anatomical and cross-modal representations before task-specific fine-tuning. In parallel, we train an auxiliary organ segmentation model whose predictions provide explicit anatomical context and help distinguish physiological uptake from malignant lesions. A dedicated tracer classifier first routes each study to an FDG- or PSMA-specific branch. Within each branch, a first-stage segmentation model consumes CT, PET, and organ context to generate an initial lesion mask. The initial prediction is then combined with cumulative foreground/background scribbles and refined by a second interactive segmentation network. The FDG and PSMA branches share the same overall processing pipeline but are trained independently to account for tracer-specific appearance and error modes. We additionally employ curriculum-style training and model ensembling to improve robustness across interaction steps and heterogeneous cohorts. Experiments are conducted using the official AutoPET V data and ten-fold split; quantitative results, ablations, and final test-set performance are left as placeholders to be completed after the challenge evaluation. Code: this https URL.

---


### 432. [VFR-Audit: Verdict-Level Reliability for Fairness Audits in Hospital Length-of-Stay Prediction](https://arxiv.org/abs/2608.30846)

**<font color=#1a73e8>作者：</font>** Md Jannatul Rakib Joy, Viet Vo, Caslon Chua  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fairness audits in clinical Artificial Intelligence convert continuous fairness metrics into binary pass-or-fail verdicts against operational thresholds, where hospital governance boards, payers, and regulators act on the resulting verdicts. Such audits are repeated over time and across hospital sites, thus the same verdict can flip between pass and fail across audits. Existing uncertainty methods such as Bayesian posteriors, bootstrap confidence intervals, and permutation tests address verdict instability only at the continuous-metric level. Converting metric-level uncertainty into a verdict-stability claim remains a manual step that scales poorly across the (model, metric, attribute) cells an audit covers. Existing uncertainty methods also leave open whether bias-mitigation steps, such as reweighing or per-group threshold shifts, yield a stable passing verdict at the cost of model discrimination measured as AUROC or this http URL address this verdict-stability gap, we propose VFR-Audit, a framework built around the Verdict Flip Rate (VFR), a scalar bounded between 0 and 0.5 that measures the probability of verdict reversal under stratified bootstrap resampling. VFR-Audit reports VFR alongside three reliability axes, namely within-cohort resampling stability, audit-size sensitivity, and cross-hospital verdict agreement via Fleiss' kappa.

---


### 433. [Linguistic Distance Segregates Latent Representations in Automatic Speech Recognition Systems](https://arxiv.org/abs/2608.30853)

**<font color=#1a73e8>作者：</font>** Ting-Hui Cheng, Line Katrine Harder Clemmensen, Sneha Das  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While automatic speech recognition (ASR) models have achieved remarkable improvements in recent years, performance disparities persist across different speaker populations. One such disparity is for speakers whose first languages (L1) are from families distant from English. This paper investigates the relationship between first language background and English ASR performance. Through empirical analysis, we observe that the correlation between speakers' L1 distance and ASR error rates yields a systematic effect on English Speech, with its strength varying across datasets and models. This association is statistically significant in a follow-up analysis accounting for dataset-level variation in Tweedie mixed-effects models ($p<0.001$ across evaluated models). In addition, analysis of the latent space reveals a L1-based spatial segregation across deeper acoustic layers in the majority of evaluated architectures

---


### 434. [TAMI: Temporally Aligned, Missingness-Aware, and Interpretable Multimodal Fusion for Mental Health Assessment in Older Adults with Mild Cognitive Impairment](https://arxiv.org/abs/2608.30857)

**<font color=#1a73e8>作者：</font>** Merna Bibars, Bolaji Omofojoye, Allan I. Levey 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depression and anxiety in older adults with Mild Cognitive Impairment (MCI) are frequently underdiagnosed due to limited access to care. Multimodal analysis of remote clinical interviews is a scalable screening approach, but existing methods have three limitations. First, they do not correct temporal misalignment across multimodal features extracted at different resolutions, inducing spurious cross-modal associations. Second, remote recordings exhibit uneven modality dropout, but missing values are often zero-filled, making them indistinguishable from valid near-zero measurements. Finally, they do not jointly attribute predictions to modalities, questions, and interview moments, limiting fine-grained clinical interpretation. We propose a Temporally-Aligned, Missingness-Aware, Interpretable (TAMI) multimodal fusion framework. TAMI aligns speech, language, facial, and physiological features within question-answer segments on a shared timeline, encodes modality-level missingness over time, and conditions fusion on question context. In interviews with 49 older adults with MCI, TAMI achieved area under the receiver operating characteristic curve (AUROC) scores of 0.68 (depression) and 0.69 (anxiety). Fine-grained temporal alignment of multimodal features produced the largest performance gain ($\Delta{\geq}0.1$). Multi-level interpretability analysis revealed that depression classification relied on eyegaze and open-ended questions, while anxiety classification depended on eyegaze and head pose, with attribution uniformly distributed across questions. Using only responses to the open-ended questions (5.1min), the depression model achieved an AUROC score of 0.67, which was not significantly different from using the full interview (19min) ($p>0.05$). Our findings support designing interview protocols centered on open-ended questions for depression screening in older adults with MCI.

---


### 435. [Predicting Residential Rents in Dakar Using Machine Learning](https://arxiv.org/abs/2608.30865)

**<font color=#1a73e8>作者：</font>** Amadou Tidiane Kassa Diallo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dakar's residential rental market remains poorly documented despite its economic and social importance: 54.4% of households are renters, compared to 23.3% nationally. This study develops a complete machine learning pipeline to predict residential rents in Dakar, from data collection to model interpretation. An original dataset of 1,507 rental listings was built through systematic web scraping and a documented cleaning pipeline, then enriched with four purpose-built features, including a luxury score and a keyword-based quality score. Five models were compared: linear regression, Random Forest (baseline), XGBoost, and LightGBM optimized through Bayesian optimization with Optuna, using leakage-free KFold target encoding for location. The optimized XGBoost model achieved the best performance with an $R^2$ of 0.847, an MAE of 210,902 XOF, and an RMSE of 324,195 XOF. Feature importance was assessed using native XGBoost gain and SHAP values, revealing a substantial difference in the ranking of location, which appears as a minor predictor by gain but as the second most influential variable by SHAP. This result carries methodological implications for hedonic studies using target-encoded categorical variables. This study provides an interpretable benchmark for Dakar's rental market and highlights several avenues for improvement, including the integration of geospatial features and conformal prediction.

---


### 436. [Beyond Good Intentions: When Does the Framing of Multilingual and Low-Resource NLP Research Become a Caricature?](https://arxiv.org/abs/2608.30866)

**<font color=#1a73e8>作者：</font>** Nedjma Ousidhoum, Noopur Zambare, Mohamed Abdalla  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building language technologies and conducting NLP research for low-resource languages---particularly when led by native speakers or involving participatory research practices---are often framed as means of addressing inequality, serving local communities, and, at times, contributing to *decolonisation*. In this paper, we examine recently published NLP and ML papers, focusing on the narratives used to characterise multilinguality, low-resource languages, and underrepresented cultures. We propose a framework for analysing research framings and identify recurring rhetorical patterns that may hinder accountability and constrain equitable knowledge production for---and by---underserved communities. We further assess the evidential basis of assertions regarding community benefit and find that such statements are often weakly supported or left unsubstantiated. Although community ownership and participation are frequently presented as key objectives, our analysis, supported by statistics from the ACL Anthology, suggests that research outputs more often prioritise resource creation and benchmarking---important but distinct goals---over evidence of broader structural change. We conclude by offering practical recommendations to help authors, reviewers, and readers critically assess these assertions and avoid potentially misleading framings.

---


### 437. [VCAR: Training-Free 3DGS Segmentation via View Completeness and Axis-Aware Boundary Refinement](https://arxiv.org/abs/2608.30870)

**<font color=#1a73e8>作者：</font>** Kun Cao, Di Wang, Haibin Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation in 3D Gaussian Splatting (3DGS) is crucial for advancing 3D scene understanding. Existing methods predominantly rely on feature distillation, which incurs substantial per-scene training overhead and often yields blurred segmentation boundaries. We identify that these boundary artifacts are driven in part by insufficient viewpoint coverage and boundary overflow of anisotropic Gaussian primitives. To address these challenges, we propose VCAR, a training-free coarse-to-fine segmentation strategy based on View Completeness and Axis-aware Boundary Refinement. In the coarse stage, a visibility-based weighted multi-view voting scheme rapidly localizes the target. In the fine stage, an object-centric sphere derived from the coarse result generates supplementary viewpoints via Spherical Spiral Sampling (SSS), allowing multi-view voting on the augmented views to precisely refine object boundaries and suppress irrelevant 3D Gaussians. Moreover, we introduce Axis-aware Boundary Refinement (ABR) to mitigate artifacts from anisotropic primitives. By decomposing the projected 2D covariance into per-axis contributions, ABR identifies the dominant axis responsible for boundary leakage and applies targeted anisotropic compression exclusively along that axis. Extensive experiments on NVOS and LERF demonstrate that VCAR achieves state-of-the-art segmentation accuracy and efficiency without training. Our code is available at this https URL.

---


### 438. [SurgSkill-Bench: A Benchmark for Multimodal Surgical Skill Assessment](https://arxiv.org/abs/2608.30872)

**<font color=#1a73e8>作者：</font>** Chaohui Dang, Zheheng Jiang, James Glasbey 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective assessment of surgical technical skill is important for surgical training and structured feedback, but current workflows remain dependent on labor-intensive expert review. Existing automated approaches primarily focus on visual inputs and provide limited support for jointly studying operative performance, structured skill scores, and evaluator feedback. We introduce SurgSkill-Bench, an initial video-score-text benchmark-style dataset containing 214 surgical training simulation videos, six-dimensional OSATS scores, and expert free-text comments. We define two evaluation settings: video-only OSATS prediction for automated assessment and post hoc expert-comment-assisted prediction, where evaluator comments are available as auxiliary information. We provide controlled baseline experiments using representative frozen visual backbones, content-adaptive key-frame sampling, and a simple video-text co-attention fusion module. Under internal video-level validation, content-adaptive sampling improves video-only performance in this dataset, while evaluator comments provide additional score-related signal in the assisted setting. The best mean AUROC reaches 0.88 under dataset-specific median dichotomization. We further discuss evaluation constraints related to dataset scale, metadata completeness, and the interpretation of comment-assisted prediction. Code will be released publicly at a later date.

---


### 439. [A Controlled Evaluation of Model Rankings and Input Reliance in Surface Water Segmentation](https://arxiv.org/abs/2608.30895)

**<font color=#1a73e8>作者：</font>** Kittipat Phunjanna, Kristóf Karacs, Chayut Ngamkhanong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Performance evaluation for surface-water segmentation commonly uses an aggregate metric such as global intersection-over-union (IoU) to rank model configurations. However, a configuration ranking does not by itself establish why one system performs better, whether a close ordering is stable, or how strongly predictions rely on individual inputs. We examine these distinctions primarily on Sen1Floods11 through repeated configuration comparisons, paired test-chip analysis, fixed-checkpoint input stress tests, and geographic reweighting, with a targeted secondary evaluation of supervised input configurations on GEOID-Flood. The cross-modal student achieves the highest three-seed mean IoU on Sen1Floods11, but close orderings vary across seeds and geographic weighting, while ancillary-input rankings differ between Swin-UNet and U-Net. The GEOID-Flood evaluation shows substantial agreement in supervised ancillary-input effects, although the exact architecture ordering remains configuration dependent. Fixed-checkpoint tests further establish reliance on terrain and WorldCover without establishing a clean-input performance benefit, while target semantics and the later WorldCover prior restrict the evaluation to retrospective all-water segmentation. These results show that aggregate metrics remain useful for ranking complete configurations, but ranking stability, component attribution, input reliance, and deployment scope require distinct evidence. Performance evaluation should therefore match the evidence reported to the claim being made.

---


### 440. [Rad-R: A Raw-ADC Radar Dataset and Capture-Invariant SSM for Hardware-Fault Diagnosis](https://arxiv.org/abs/2608.30896)

**<font color=#1a73e8>作者：</font>** Mainak Mallick, Junghwan Yim, Seung-Kyum Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automotive mmWave radar can develop vibration, antenna misalignment, radome blockage, and receive-channel degradation that corrupt the signal before perception begins. Data for these faults are scarce because each condition must be induced and measured on physical hardware. We introduce Rad-R, a raw-ADC dataset captured with a 4-chip 77GHz TI MMWCAS-RF-EVM cascade (192 virtual channels). Unlike existing raw-radar datasets, Rad-R pairs each recording with a controlled hardware fault at a calibrated severity, an independent physical severity measurement, and frame-synchronised IMU, temperature, GPS, and camera streams. Rad-R is a single-session dataset, so our generalisation claims are confined to a controlled cross-severity protocol in which train and test use physically distinct captures. A reproducible benchmark evaluates seven representative vision backbones and the proposed raw-IQ Mamba SSM (RadrNet) under within-clip, chirp-wise anytime, few-shot cross-capture, and controlled cross-severity protocols. Within-clip performance is near-saturated ($>0.98$ macro-F1), whereas cross-severity generalisation remains difficult: the absolute-phase RadrNet-DS falls to $0.49$ macro-F1. RadrNet-DS-CI replaces absolute phase with per-frame-standardised magnitude and relative chirp-to-chirp phase and ranks first on the controlled benchmark ($0.663$ vs. $0.628$ for the strongest RD-CNN; three seeds); the RadrNet family also leads on the anytime and few-shot budgets. A descriptive cross-modal analysis further finds that radar micro-Doppler covaries with independently measured IMU vibration energy (pooled Spearman $\rho=0.41$ across conditions). The complete dataset and code will be released publicly under permissive licences.

---


### 441. [CAER: Causal Action Effect Reweighting for World Model Training](https://arxiv.org/abs/2608.30897)

**<font color=#1a73e8>作者：</font>** Jianjie Fang, Xvyuan Liu, Ziyou Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are becoming core infrastructure for embodied intelligence, with action-conditioned video generation providing controllable predictions of how scenes evolve after agent interventions. Yet existing models are commonly trained with space-time-uniform mean squared error, allowing abundant background tokens to dominate the gradient while sparse interaction dynamics remain under-optimized; such uniform fitting rewards reconstructing appearance rather than learning how actions change the world. We introduce Causal Action Effect Reweighting (CAER), a general training paradigm that redistributes supervision toward the tokens whose predicted future is causally affected by the action. CAER contrasts the model's own predictions with and without action conditioning to localize these tokens online, then normalizes the resulting effect map into a weight that preserves the total coefficient mass and changes only where it is spent. This online signal requires no external annotations or offline preprocessing, avoids additional data-processing time, and scales naturally with model and dataset size. Experiments across heterogeneous action-conditioned world-model tasks show that CAER converges to better solutions than uniform MSE training, with consistent improvements in the physical consistency, controllability, and visual quality of generated videos.

---


### 442. [Uncertainty-Aware Trajectory Forecasting from Imperfect Tracking](https://arxiv.org/abs/2608.30899)

**<font color=#1a73e8>作者：</font>** Stephane Da Silva Martins, Victor Petrovic, Emanuel Aldea 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most trajectory forecasting models are trained on clean annotated histories, and are often evaluated under the same idealized assumption, although practical deployments rely on trajectories produced by imperfect multi-object trackers. The real-world observations exhibit localization jitter, missed or unstable detections, and data-association ambiguity, which are usually either ignored or removed through denoising. This paper instead treats tracking-derived reliability cues as an informative signal to be propagated to the predictor. We propose a plug-in uncertainty-aware formulation in which each observed state is encoded as an uncertain state representation, modeled by a Gaussian distribution whose covariance combines detection-level localization uncertainty and association-level ambiguity through the law of total variance. Existing backbones are adapted with minimal architectural changes: input trajectories are represented as Gaussian observations, and predicted trajectories are produced as Gaussian forecasts rather than deterministic coordinates. To train predictors that remain robust under structured observation noise, we combine temporally correlated Ornstein-Uhlenbeck perturbations with response-based knowledge distillation from a teacher trained on clean trajectories. Experiments on Oxford Town Centre and VIRAT using real tracker outputs, together with a complementary ETH/UCY pseudo-detection protocol, show that the proposed formulation improves displacement accuracy and the reliability-sharpness trade-off of probabilistic forecasts.

---


### 443. [Fine-Tuning Low-Bit Models with Gradient in Quantized Code Space](https://arxiv.org/abs/2608.30908)

**<font color=#1a73e8>作者：</font>** Shiguang Wu, Zhouchen Lin, Quanming Yao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning Low-bit models aims to adapt a quantized model while keeping the final deployed checkpoint in the same low-bit form. This setting is practically important as it reduces memory and inference cost for storage and deployment. Under this constraint, adaptation becomes an optimization problem over quantization codes and scales. Existing continuous low-bit training is efficient, but it can be distorted by straight through estimation error or by post-quantize gap; discrete search is deployment-faithful, but it is often too inefficient under a finite training budget. We propose code surrogate gradient as the first order signal in deployable code space to acceleate optimization, and performing guided search to preserve deployment faithfulness. Experiments across arithmetic reasoning, instruction following, and structured language understanding show that GradCodes consistently improves fine-tuning low-bit models across different quantization datatypes. Code is provided at this https URL.

---


### 444. [Responsible Integration of AI in Cancer Genomics: Barriers, Risks, and Pathways to Trustworthy Clinical Translation](https://arxiv.org/abs/2608.30912)

**<font color=#1a73e8>作者：</font>** Bahar İlgen, Yiannos Tolias, Denise Kühnert 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) and natural language processing (NLP) are increasingly used to extract, integrate, and interpret biomedical knowledge relevant to cancer genomics, yet their translation into routine clinical oncology has been comparatively slow. The central challenge is not computational capability alone, but trustworthy integration into clinical workflows. This review examines how NLP and AI support the cancer genomics pipeline, from literature mining and automated variant interpretation to clinical trial matching, knowledge graph construction, and multimodal data integration. We identify four interrelated translational failure domains: evidence inconsistency, explainability and uncertainty, data governance and reproducibility, and interoperability. Rather than considering these challenges in isolation, we take a systems-level view, focusing on their interaction across the translational pathway. We propose a conceptual framework and roadmap for addressing these domains through rigorous validation, uncertainty-aware methods, interoperable infrastructures, regulatory alignment, and human oversight across the AI lifecycle. Progress toward routine clinical use will depend less on further improving model capability than on systematically addressing these interacting failure domains from development through deployment and post-deployment monitoring.

---


### 445. [Selection-Aware Stress Testing for Interactive Agents](https://arxiv.org/abs/2608.30916)

**<font color=#1a73e8>作者：</font>** Yang Xu, Chenang Li, Jiefu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agent evaluations often use one benchmark to choose a workflow and then search for task types where its advantage weakens, so both conclusions are selected from the same data. We introduce Selection-Aware Semantic Stress Testing (\SASST{}), which learns a task reweighting from pre-execution features on discovery tasks and evaluates the same paired comparison on separate confirmation tasks. The protocol checks support and stability, uses joint bounds for all planned claims, and can return no claim. We prove conditional asymptotic validity under stated cluster assumptions. A forty-cluster audit finds Gaussian undercoverage and conservative Bonferroni $t$ bounds. In one 480-episode $\tau$-bench study, a $3.75$ point discovery gain vanished on confirmation. A second-model study likewise confirmed neither a workflow benefit nor a stable stress rule.

---


### 446. [Towards Stream Learning on Embedded Systems: Benchmarking the Memory Consumption of Stream Learning Methods](https://arxiv.org/abs/2608.30923)

**<font color=#1a73e8>作者：</font>** Sebastian Buschjäger, Nuwan Gunasekara, Heitor Murilo Gomes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stream learning is commonly evaluated through predictive performance and adaptation to concept drift. However, sustained operation of a stream learner also requires predictable and bounded resource usage even on long streams. This requirement becomes even more critical when learning moves from servers to near-sensor embedded systems where memory and processing are scarce resources. In state-of-the-art stream learning, however, we perceive a strong focus on concept drift adaptation, whereas resource usage is often an evaluation byproduct. To close this gap, we benchmark seven representative stream classifiers on 13 real and synthetic streams under model-size budgets from 128\,KiB to approximately 8\,MiB. Our benchmark comprises a total of 6,463 experiments. We measure failure-aware accuracy, peak model size, time to budget exhaustion, and prediction-plus-update latency. The results reveal two distinct resource failure modes. Adaptive ensembles can exceed small budgets almost immediately because of their initial footprint, even when their size remains stable thereafter. Incremental trees can fit initially but grow throughout a long stream, with HoeffdingTrees (HT) and Extremely Fast Decision Trees (EFDT) increasing by median factors of 7.37 and 5.87. Explicitly compact methods remain the only viable option under the smallest budgets, but are usually overtaken as larger budgets make adaptive ensembles competitive. Hence, many state-of-the-art methods are only partially applicable in embedded systems or for long-running systems. We therefore call on the stream-learning community to make bounded resource usage a first-class design objective alongside drift adaptation, and propose concrete steps toward this goal, including an API through which stream learners can explicitly expose and respect resource budgets.

---


### 447. [Nonparametric Contextual Pricing and Inventory Learning under Censored Demand](https://arxiv.org/abs/2608.30944)

**<font color=#1a73e8>作者：</font>** Zean Han, Jing Liang, Ruihan Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In online retailing, when a product sells out, a retailer often sees only the units sold, not how many customers would have bought it had inventory been available. However, the inventory level determines how much demand is revealed, and this information can influence subsequent decisions and future profits. We study an online selling problem in which, in each round, the seller observes a market context and then makes pricing and stocking decisions based on censored sales data from previous rounds. The challenge is to learn a context-dependent pricing and stocking policy without assuming a particular formula for demand or observing realized profit. To overcome this difficulty, we propose a Mean-Calibrated Kernel UCB (MCK-UCB) algorithm that turns each incomplete sales record into a reliable guide for both inventory and price decisions, using data from past rounds with similar market conditions. This design allows us to learn while serving customers, without a separate exploration phase or the need to recover all demand hidden by stockouts. We prove the minimax optimality of the proposed algorithm, with strictly faster rates when expected profit varies more smoothly with price. Comprehensive numerical experiments have been conducted to confirm the effectiveness of the proposed algorithm.

---


### 448. [Reproducible macroscopic dynamics in a closed-loop human-AI learning system](https://arxiv.org/abs/2608.30946)

**<font color=#1a73e8>作者：</font>** Minlin Wu, Xu Fang, Yicheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Closed-loop human-AI systems generate high-dimensional behavioural trajectories whose collective dynamics remain obscure. Using 297,915 learners' adaptive-tutoring histories, we define semantic order variables before model fitting and test them in user-disjoint cohorts. The state exhibits reproducible basin-like flow and operationally defined, state-heterogeneous metastable-like kinetics. A construction-matched null distinguishes normalised-memory relaxation from a reproducible excess field. A four-term conditional mechanism recovers population drift (r = 0.946; learner-bootstrap 95% CI, 0.935-0.955). Predictive event-level self-supervised learning recovers the state and learned-plane flow; null-referenced corrections retain directional, partial-amplitude excess-field structure without full calibration. Shuffled-order training reverses learned-plane flow on ordered trajectories; support-alignment randomisation selectively reduces inward transport. Both axes remain linearly accessible without state supervision. Without cross-model fitting, the models share leading population drift (r = 0.866; learner-bootstrap 95% CI, 0.857-0.875) and persistence ordering; residual directions remain model-specific. These results identify an externally anchored leading-order effective field linking empirical dynamics, an interpretable mechanism and neural computation.

---


### 449. [Audio-Driven Adversarial Defense for 3D Talking Face Generation with totally Visual Fidelity Preservation](https://arxiv.org/abs/2608.30951)

**<font color=#1a73e8>作者：</font>** Rui-Qing Sun, Chen-Hao Cui, Hui-Yang Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid development of generative portrait models has raised growing concerns about privacy leakage and identity misuse. In particular, audio-driven 3D talking face generation can reconstruct a reusable 3D portrait of a target person from a monocular video and animate it with arbitrary speech, making realistic identity impersonation alarmingly practical. Existing proactive defenses mainly operate in the visual domain by injecting subtle perturbations into acial regions to disrupt identity acquisition. However, such perturbations often compromise visual quality due to the strong structural priors and social sensitivity of human faces, and are easily weakened by common real-world transformations such as resizing. To overcome these limitations, we propose an imperceptible audio defense for audio-driven 3D talking face generation by shifting protection from the visual modality to the audio modality. Specifically,we exploit psychoacoustic masking to hide protective perturbations within perceptually masked frequency regions of the speech signal, thereby reducing perceptual distortion while suppressing reliable facial animation. Extensive experiments demonstrate that the proposed method effectively degrades 3D talking face generation while preserving favorable perceptual quality. These findings highlight psychoacoustically guided audio perturbations as a practical and promising direction for privacy-preserving portrait protection.

---


### 450. [Learning Action Models with Conditional and Quantified Effects via Uncertainty-Guided Exploration](https://arxiv.org/abs/2608.30955)

**<font color=#1a73e8>作者：</font>** Jeffrey Jewett, William Solow, Sandhya Saisubramanian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate action models are critical for effective planning. Existing action-model learning methods largely assume simple action representations or become computationally intractable when learning conditional and quantified effects. We present Online Hypothesis-Driven Conditional Action Model Learning (OHCAM), an online approach for learning action models with conditional and quantified effects from limited interactions with the environment. OHCAM maintains a belief over hypothesized action models and actively selects informative actions to reduce uncertainty by maximizing disagreement among competing hypotheses, while being robust to noisy observations. To enable scalability, OHCAM begins with a small set of simple action model hypotheses and expands to more complex conditions only when the current hypotheses become inconsistent with the data. Experiments on six benchmark planning domains demonstrate that OHCAM is sample efficient in learning action models that solve substantially more tasks than baselines, even with observation noise. We validate OHCAM on two tasks using a Kinova Gen3 robot, demonstrating the real-world applicability of our approach.

---


> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-485](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
