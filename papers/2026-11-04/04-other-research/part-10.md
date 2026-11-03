# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

---

### 451. [SYNC: A Training-Free Inference Controller for Dynamic Layer Selection in Multi-Persona Alignment](https://arxiv.org/abs/2611.02636)

**<font color=#1a73e8>作者：</font>** Yosef Nuraga Wicaksana, Muhammad Reza Qorib, Fadhil Muhammad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Steering vectors align a model at inference time without touching its weights, but eliciting several personas at once is a different problem from eliciting one. Prior multi-persona steering approaches predetermine both how persona vectors are combined and the specific layers at which they are injected. Moreover, this static commitment introduces substantial offline search costs to identify suitable target layers, despite the fact that optimal intervention strengths vary dynamically across both decoding steps and distinct personas. We introduce SYNC (SensitivitY-guided iNference Control), a novel training-free inference control framework compatible with pre-existing steering vectors. SYNC dynamically estimates each layer's sensitivity to every persona via cosine similarity trajectories, assigning each persona to its optimal injection layer at every decoding step. Across two models, two persona profiles and steering vectors from both unsupervised and supervised extraction, SYNC leads on 21 of 28 persona configurations, significantly on 15. Code is available at \href{this https URL}{this https URL}.

---


### 452. [Where Is a Prediction Model Miscalibrated, and for Whom? Local Audits in Outcome-Learned Pockets](https://arxiv.org/abs/2611.02639)

**<font color=#1a73e8>作者：</font>** Bernardo Modenesi, Taoyi Chen, Sima Najafzadehkhoei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Overall and group-level averages, and ranking metrics such as the AUC, can hide sets of observations for which a prediction model systematically over- or under-predicts. We present an audit that asks where a model is miscalibrated (in which sets of similar observations it over- or under-predicts on average) and for whom (whether its average prediction error differs between demographic groups, such as by race or sex, within the same set). It groups observations into pockets using random-forest similarity, which weighs each feature by its importance for predicting the outcome, with a ridge-regression grouping alongside. Pockets are learned on one sample and tested on another, with simultaneous confidence intervals that allow for correlation within units such as hospitals; the audit needs only features, outcomes and fixed predictions. In 17 simulation scenarios with an error planted for one group, the combined audit located it better than the strongest alternative grouping in 15, with false-alarm rates near or below 5%; with a local error planted for everyone, it won in 12 of 15 scenarios at the smaller error size and lost when the error was unrelated to the outcome. In public synthetic data from the care-management algorithm studied by Obermeyer et al., it found no detectable overall error but under-prediction of illness in the sickest pockets and over-prediction elsewhere, and distinguished Black patients' concentration where the score under-predicted for everyone from a Black-White gap within pockets. For APACHE IVa, an exploratory analysis located its previously reported over-prediction of ICU mortality in a mostly ventilated pocket and a low-risk pocket, with none detected in a moderate-risk one. Two chest X-ray classifiers showed offsetting local errors behind no detectable overall error. Code: this https URL

---


### 453. [InterFuse: Interaction-Guided Adaptive Fusion of Heterogeneous Models for Payment Risk Ranking](https://arxiv.org/abs/2611.02640)

**<font color=#1a73e8>作者：</font>** Haoyu Jiang, Weiyu Han, Ze Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Payment platforms use view-specific models trained on transaction attributes, behavioral histories, and relational structures to rank transactions under limited review budgets. However, existing fusion methods often focus on prediction scores or interactions among model representations, with less attention to how these interactions should guide aggregation using each model's original prediction and input coverage. To address this limitation, we propose InterFuse, a fusion framework that uses a shared fusion state from cross-model interaction to guide transaction-adaptive aggregation. InterFuse encodes each model's representation, prediction score, and input coverage as a model-specific token, using learned states for unavailable outputs. Availability-aware attention updates these tokens and produces a shared fusion state. This state then guides aggregation over available models using their updated representations, original predictions, and input coverage. We evaluate InterFuse on an industrial payment replay and three public financial benchmarks using the same upstream models across fusion methods. InterFuse achieves the highest top-ranked recall and AUC on all four datasets, improving Recall@1% by 1.11-8.09 percentage points over the strongest baselines. Ablations show the benefits of cross-model interaction and adaptive aggregation, while industrial analyses find larger interaction gains when model predictions disagree. Additional analyses examine robustness to missing outputs and the trade-off between ranking gains and fusion latency.

---


### 454. [ReinSeg: Retrieval-Guided Bounded Multimodal Refinement for 3-D Road Anomaly Segmentation](https://arxiv.org/abs/2611.02648)

**<font color=#1a73e8>作者：</font>** Haifa Zhang, Yijing Wang, Zhiqiang Zuo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3-D road anomaly segmentation is essential for risk-aware perception in autonomous driving. Its central challenge is to rank sparsely observed hazards ahead of abundant normal road structures while preserving point-wise metric localization. LiDAR provides accurate 3-D point support, whereas surround-view imagery offers complementary semantic context for separating unexpected hazards from challenging normal structures. We propose ReinSeg, a retrieval-guided bounded multimodal refinement framework for point-wise road anomaly segmentation. Occupied LiDAR bird's-eye-view cells retrieve scene-specific context from a shared memory of eight surround-view images without supplying calibration variables to the retrieval module. A relative-norm-bounded residual returns this context to the LiDAR point features, so the frozen LIDO anomaly-scoring interface is preserved, and the refinement is optimized with in-distribution semantic labels only. On the Spotting the Unexpected (STU) benchmark, ReinSeg improves validation average precision from 27.54\% to 35.67\% and reduces the false-positive rate at 95\% anomaly recall from 34.85\% to 10.61\%, shrinking the high-recall screening set from 67.54 to 20.55 million points. Relative to REL, AP is 24.99 percentage points higher and FPR95 is 0.99 points lower. Matched interfaces and component isolation show that retrieved scene imagery and the relative-norm bound are both essential, and ReinSeg stays above LiDAR-only performance under missing, corrupted, or misaligned camera inputs while running at 21.8 frames per second. These results establish bounded retrieval of scene-specific visual evidence as an effective route to reliable 3-D road-hazard perception.

---


### 455. [Computer Vision Applications for Art History: Reflections and paradigms for future research](https://arxiv.org/abs/2611.02649)

**<font color=#1a73e8>作者：</font>** Amalia Foka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One of the contributing factors to the continuing debate among art historians over the use of computational methods in art history research is that they do not consider the core of today's art history research questions. The lack of close collaboration between the two involved research communities makes the definition of contemporary art-historical methods as well-defined computer vision problems extremely difficult. For that purpose, it is devised as a methodology to study articles in art history journals from a computer science perspective. The objective is to identify which image features art historians utilise within their research and describe them in immediate and meaningful terms to the computer vision research community. Finally, some paradigms that could serve as a new starting point for exploring how computer vision applications for art history can address the core of today's art history research are given.

---


### 456. [Probe-Guided Gradient Balancing for Multimodal Learning](https://arxiv.org/abs/2611.02651)

**<font color=#1a73e8>作者：</font>** Vu Vo, Haytham M. Fayek, Thuy Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Jointly trained multimodal networks frequently underutilize weaker modalities, as faster-learning modalities dominate the shared fusion objective and suppress gradients reaching slower ones. Most existing approaches throttle dominant modalities, whereas directly boosting weaker modalities often fails because monitoring signals derived from the joint loss remain dominated by stronger modalities. We propose Probe-Guided Gradient Boosting (PGGB), a gradient modulation approach that boosts weaker modalities while preserving the strength of dominant ones. PGGB attaches lightweight linear classifiers to stop-gradient features from each modality to estimate representation quality independently. The gap between these scores, termed the utilization gap, provides an imbalance signal used to adaptively scale weaker-modality gradients through bounded and smoothed modulation. PGGB is composable with throttling methods, as it leaves the loss function and fusion architecture unchanged. Experiments across eight benchmarks spanning four domains and 2-4 modalities demonstrate that PGGB outperforms state-of-the-art methods on highly imbalanced multimodal datasets while remaining competitive under low or negligible imbalance. We further establish bounded scaling, self-attenuation, and a descent bound for standard SGD under smoothness and bounded-variance assumptions. Code is available at this https URL.

---


### 457. [VerdictAD: Few-Shot Anomaly Detection via Decision-Guided Refinement](https://arxiv.org/abs/2611.02654)

**<font color=#1a73e8>作者：</font>** Shangquan Sun, Wenjun Luo, Yuanzhi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting defects in real-world industrial inspection often requires learning from only a few normal images per category. Recent few-shot anomaly detection methods have achieved strong performance by measuring feature differences between query images and normal references. However, visual differences do not always indicate genuine defects, as normal appearance variations can also produce high anomaly scores. Conversely, structural or logical anomalies may not produce strong local feature differences, making them difficult to detect. To address this limitation, we introduce VerdictAD, a training-free framework that refines existing anomaly detectors through visual decisions. Rather than replacing existing detectors, VerdictAD adopts a typed decision model to assess the query image and its local regions against a few normal references. By directly producing structured decision probabilities without text generation, the model provides complementary evidence for refining anomaly responses at different spatial scales. Building on this capability, we introduce two modules: Global Verdict Refinement (GVR) uses image-level decisions to refine the overall anomaly score, while Local Verdict Refinement (LVR) aggregates regional decisions to refine the anomaly map. Combined with a simple DINOv2-based detector, VerdictAD achieves competitive performance in one-shot and few-shot anomaly detection. More importantly, as a plug-and-play framework, it consistently improves existing anomaly detectors across MVTec AD, VisA, and MVTec LOCO AD, achieving strong results across one-shot and few-shot settings. Our code and experimental logs are publicly available at this https URL.

---


### 458. [OctreeSplat: Hierarchical Octree-Guided Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2611.02658)

**<font color=#1a73e8>作者：</font>** Yibin Zhao, Yihan Pan, Wenli Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has shown considerable potential for novel view synthesis (NVS) and 3D reconstruction. Feed-forward methods avoid costly per-scene optimization, but fixed image or spatial resolutions limit their ability to allocate primitives according to local complexity. We present OctreeSplat, a hierarchical octree-guided feed-forward Gaussian splatting. OctreeSplat extracts multi-view features and geometric priors from a frozen visual foundation model (VFM), constructs a hierarchical octree, and predicts densification scores. The resulting representation allocates Gaussian primitives at spatially varying densities according to local complexity. Stochastic solids volume rendering improves depth rendering, strengthens geometric supervision, and supports surface reconstruction. When camera parameters are available, an optional test-time optimization (TTO) module improves agreement between predicted and ground-truth parameters. Training updates only 76 million additional parameters and requires 35 GPU-hours. Experiments on Replica, TUM, Tanks and Temples, and DTU demonstrate competitive RGB view synthesis, depth synthesis, and surface reconstruction. OctreeSplat reduces the number of Gaussian primitives while maintaining high reconstruction quality.

---


### 459. [TME-ContextNet: Class-Conditioned Spatial Supervision and Grouped Decoding for Joint Nuclei Instance Segmentation and Classification](https://arxiv.org/abs/2611.02671)

**<font color=#1a73e8>作者：</font>** Rukang Ma, Bingxue Wang, Liwen Zou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint nuclei instance segmentation and classification requires precise boundaries and neighborhood information that helps distinguish morphologically similar cell types. We present TME-ContextNet, a multi-task framework that learns class-conditioned spatial context from existing nuclear annotations and organizes decoding into geometry-related and semantic task groups. Class-conditioned spatial supervision extends nuclear labels into a dense target using Euclidean distance transforms, requiring no additional tissue-region annotation. We derive its nearest-region interpretation and characterize its stability to small annotation perturbations. A local--global context module combines dilated convolution and self-attention, while a grouped task decoder reduces redundant computation. The spatial head supplies training supervision and is omitted during inference. Experiments on PanMix, CoNSeP, and PanNuke yield Dice scores of 80.23%, 65.32%, and 79.13%, and mean multi-class panoptic quality (mPQ+) scores of 67.62%, 35.50%, and 43.74%, respectively. PanNuke results are averaged across three test folds. Target and decoder controls support the combination of distance-based supervision and grouped decoding while identifying their dependence on task configuration. The framework uses 36.40 million parameters, compared with 54.74 million for HoVer-Net. These findings support a compact, context-aware formulation for joint nuclei analysis in computational pathology.

---


### 460. [Reap: Uncovering Monte Carlo proof search with a lightweight model](https://arxiv.org/abs/2611.02678)

**<font color=#1a73e8>作者：</font>** Yutong Wang, Xuanzhi Ren, Tianyi Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Reap, an open framework for learning and analyzing formal proof search in Lean4. Reap implements policy-value-guided Monte Carlo Tree Search directly in Lean, sharing proof-state transitions, AND-OR search, and replay verification between inference and training rollouts. Structured action logs expose how neural predictions and tactic execution interact during search. Using this framework, we train Reaper-1, a 1.7B-parameter policy-value model, through continued pre-training, supervised tactic learning, and iterative search-based reinforcement learning. Using a separate premise selector, the final system solves 79.9% of miniF2F-test at pass@32, establishing state-of-the-art performance among open provers of comparable size while remaining competitive with substantially larger models. Beyond improved solve rates, our results suggest that RL strengthens the prover's ability to organize proofs around useful intermediate results, favoring substantial advances over repeated local adjustments. This more directed proof construction is accompanied by increasingly elaborate tactic programs: fewer explicit search decisions are needed, while more work is performed within each decision. The resulting trade-off between search effort and tactic execution cost provides insight into how learning changes the prover's problem-solving strategy.

---


### 461. [HistoTx: Early fusion of H&E images and spatial transcriptomics at varying spatial transcriptomics resolution with self-supervised learning](https://arxiv.org/abs/2611.02681)

**<font color=#1a73e8>作者：</font>** Alice Driessen, Emil Malmsten, Steffen Wolf 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics maps gene expression across tissue sections and, when integrated with whole slide images, jointly captures both morphological architecture and molecular activity to provide a rich, multimodal view of tissue biology. ML approaches combining spatial transcriptomics and WSIs typically learn a mapping from morphological features to molecular profiles via contrastive alignment or supervised fine-tuning of pathology foundation models. In both cases, transcriptomics serves as a training signal rather than a true input modality, leaving inference fundamentally image-driven. We propose an early-fusion vision transformer architecture in which transcript tokens are constructed at arbitrary spatial resolution, merged with image patch tokens, and jointly processed through a shared transformer stack for deep cross-modal interaction. Starting from a pretrained vision-only pathology foundation model, we train HistoTx by continuing self-supervised pretraining on paired image and spatial transcriptomics data and demonstrate that: 1) at inference with image only, performance remains on par with the baseline on most tasks while improving on tasks that inherently benefit from molecular knowledge, such as gene expression prediction; 2) when both modalities are available at inference, jointly providing image and transcript inputs outperforms either modality alone.

---


### 462. [Geometry-Constrained Dynamic Hypergraph Convolutional Network with Contrastive Score Refinement for Skeleton-Based Action Recognition](https://arxiv.org/abs/2611.02685)

**<font color=#1a73e8>作者：</font>** Minh Ta Tran Nhat, Yuning Ye, Yuseok Ban  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based action recognition is a pivotal task in computer vision; however, conventional Graph Convolutional Networks (GCNs) are often constrained by pairwise joint modeling, which fails to capture the intricate high-order interactions inherent in human movement. While recent hypergraph-based methods attempt to address this limitation, they typically rely on static structures derived from anatomical priors, lacking the flexibility to capture dynamic, action-specific joint correlations. To this end, we propose DyGCN, a Geometry-Constrained Dynamic Hypergraph Convolutional Network for skeleton-based action recognition. At the core of DyGCN is the Dynamic Hypergraph Construction Network with Contrastive Score Refinement (DyGCT) block, which comprises two novel components: the Geometry-Constrained Dynamic Hypergraph Construction (GeoHC) module and the Contrastive Score Refinement (CSR) module. Specifically, GeoHC dynamically constructs action-specific hyperedges by leveraging geometry-constrained second-order compatibility, transcending the limitations of static hyperedge structures. Furthermore, CSR explicitly refines the pairwise compatibility scores during hypergraph construction through prototype-based contrastive learning, fostering more discriminative action-specific hyperedges, with zero inference-time overhead as CSR operates only during training. Extensive experiments on NTU RGB+D, NTU RGB+D 120, and Northwestern-UCLA validate the effectiveness of DyGCN, achieving state-of-the-art performance on widely used benchmarks. The source code is available at this https URL.

---


### 463. [Discovering Semantic Granularity in Images through Clustering of Pretrained Visual Representations](https://arxiv.org/abs/2611.02686)

**<font color=#1a73e8>作者：</font>** Ying Dai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic granularity, which refers to the levels at which visual representations organize image content into meaningful entities, is fundamental to image understanding. However, whether pretrained visual representations inherently encode semantic structures at multiple granularities remains poorly understood. This paper presents a representation-driven approach for discovering semantically meaningful image regions at different granularities through clustering of pretrained visual representations without semantic supervision. Specifically, we concatenate selected feature maps extracted from a pretrained visual model and apply a singular value decomposition (SVD)-based projection to derive pixel-wise principal representation maps (PRMs). The resulting PRMs capture implicit semantic structures embedded in pretrained visual representations, making them accessible to subsequent semantic clustering. We then introduce the semantic continuity rate (SCR), based on the silhouette principle, to quantify the coherence of pixel-wise representations within and between clusters at different candidate granularities. Furthermore, we analyze the signal-to-noise ratio (SNR) of SCR profiles to assess representation suitability for discovering semantic regions at multiple granularities. Our results indicate that PRMs exhibiting higher SNR values over an initial range of cluster numbers tend to yield more semantically meaningful regions across multiple granularities. We evaluate the proposed approach on the COCO-2017 and VOC-2012 validation datasets using Hungarian-matched intersection over union (HIoU). The results demonstrate competitive segmentation performance among the compared methods, supporting the feasibility of discovering useful semantic granularities through clustering PRMs without semantic supervision.

---


### 464. [Human-Oriented World Model](https://arxiv.org/abs/2611.02690)

**<font color=#1a73e8>作者：</font>** Saihui Hou, Zengyun Mou, Chunshui Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supporting a person over repeated interactions requires interpreting their current state in context and anticipating its subsequent evolution. We formulate the \emph{Human-Oriented World Model} (HOWM) as a conceptual framework centered on task-relevant human states and their evolution. HOWM connects current observations and individual history with environmental and social context to organize continuing state estimation, personalized dynamics prediction, and action support. Dynamic expectations and new observations jointly inform the current estimate, which in turn anchors personalized forecasts based on shared knowledge and individual experience. An external policy relates forecasts under alternative conditions to the person's goals, preferences, and constraints when considering support. Actual responses and outcomes provide evidence for revising the state estimate and personal dynamic patterns, thereby informing subsequent estimation, prediction, and support. We illustrate the framework through hypothetical training and learning scenarios. Our research agenda asks whether accumulated interaction experience improves subsequent estimation and prediction, and whether using the model helps the person pursue their goals over time.

---


### 465. [3L-D: A Low-Light Level Dataset from a Sensor-Agnostic, Alignment-Preserving Acquisition Framework](https://arxiv.org/abs/2611.02695)

**<font color=#1a73e8>作者：</font>** Léo Rueff, Maurgène Ghezal, Valentin Gorse 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised low-light image and video enhancement has achieved remarkable progress, yet current models remain fundamentally constrained by the limitations of existing datasets. Prevailing methods typically rely on uncontrolled ambient captures, camera parameter manipulation (e.g., exposure or ISO adjustments), or neutral density filters, failing to replicate authentic night-sky near-infrared spectral content and genuine low-photon noise distributions. Furthermore, capturing dynamic paired sequences without introducing warping artifacts or sensor-specific biases remains an open challenge. In this paper, we introduce 3L-Dataset, a physically calibrated low-light image and video dataset generated using a modular, sensor-agnostic acquisition framework. Our test bench faithfully reproduces the standardized Midavaine night level scale from Level 1 (full moon, approximately 1000 mlx) down to Level 5 (overcast moonless night, approximately 0.1 mlx), spanning the visible to near-infrared spectrum across diverse realistic environments, including countryside, forest, urban, and desert scale models. Using high-precision programmable mechanical actuation, our acquisition framework guarantees sub-pixel spatial alignment across synchronized sextuplets, each composed of one reference image and five corresponding images acquired at the five standardized night levels, without post-processing image warping. We evaluate multiple representative deep learning baselines across varying night levels, revealing critical trade-offs between reconstruction fidelity, perceptual quality, and inference latency under severe photon starvation. The modular acquisition framework can be adapted to different cameras, optical systems, sensor technologies, and resolutions, enabling the dataset to be continuously expanded.

---


### 466. [Beyond Answers, Traces, and Efficiency: Evidence for Adaptive Reasoning](https://arxiv.org/abs/2611.02704)

**<font color=#1a73e8>作者：</font>** Sejin Kim, Sundong Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current AI systems are evaluated as reasoners through final-answer accuracy, reasoning traces, process supervision, and computational or human-relative efficiency. Yet these measures do not establish whether reasoning adapts when tasks or evidence change. We distinguish across-task adaptivity, where acquired abstractions transfer or recombine across novel problems, fromwithin-task adaptivity, where hypotheses and actions are revised in response to new observations, feedback, or counterexamples. Using ARC-AGI as a diagnostic case study rather than an alignment benchmark, we examine what existing measures leave unresolved when test-time search, sampling, or adaptation affects performance. We propose intervention-oriented evaluation that tests abstraction transfer and hypothesis revision under controlled changes to tasks and evidence, with explicit reporting of test-time procedures and budgets. This perspective supports evaluating systems for robustness, responsiveness to corrective feedback, and auditability under changing conditions.

---


### 467. [MicroMouse: Masking Harmful Supervision in Long CoT via Relative Potential](https://arxiv.org/abs/2611.02710)

**<font color=#1a73e8>作者：</font>** Xiaowei Zhu, Hengzhu Tang, Zhenyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Even successful long CoTs may contain harmful supervision, motivating the need for methods that can automatically identify and mask such signals during SFT. Inspired by the MicroMouse maze-solving process, we view a long CoT as a search trajectory from the input problem toward the target answer. This perspective motivates maintaining a goal-relative measure, analogous to a MicroMouse's spatial coordinates, to quantify how close the current reasoning state is to the target answer. Building on this perspective, we propose MicroMouse, an automated selective-SFT framework for masking harmful supervision in long CoTs. In MicroMouse we introduce a Relative Potential (REP) to measure how closely each reasoning state supports the gold answer. Unlike the perplexity of the gold answer alone, REP measures relative support by contrasting the gold answer with a matched foil. This contrast cancels likelihood variations shared by the pair, yielding a more stable signal of progress toward the target answer. By tracking the REP trajectory, MicroMouse identifies consecutive potential decreases as erroneous exploration and post-peak reasoning as redundant wandering, and masks these harmful supervision during SFT. Extensive experiments across multiple student model scales and reasoning benchmarks show that MicroMouse consistently outperforms Full-CoT SFT and existing selective-SFT baselines, yielding average relative gains of 5.5% in greedy accuracy and 2.6% in Pass@1 relative to Full-CoT SFT. Meanwhile, MicroMouse improves reasoning efficiency by reducing average output length by 8.8%, while identifying harmful supervision in only 1.7 seconds per long CoT on average.

---


### 468. [MURFormer: Attention-Based Lightweight Multi-Scale Uncertainty-Guided Refinement Framework for PPG Denoising](https://arxiv.org/abs/2611.02715)

**<font color=#1a73e8>作者：</font>** Haram Kwon, Chaeeun Hwang, Seayul Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Photoplethysmography (PPG) is a widely used physiological signal for its convenience but is highly susceptible to motion artifacts that degrade waveform quality and limit downstream analysis. This paper proposes MURFormer, a lightweight multi-scale uncertainty-guided refinement framework for PPG denoising through noisy-to-clean PPG mapping. MURFormer employs a newly proposed Multi-Scale Attention-Conv Fusion (MACF) block, which is designed to efficiently capture multi-scale temporal dynamics of PPG, as the fundamental building block and performs uncertainty-guided two-pass refinement prioritizing unreliable regions. The method was evaluated on the publicly available CIME dataset and on a Daily Activities dataset collected in this work, comprising paired noisy-clean PPG recordings from 24 subjects. Experimental results show that MURFormer improves both signal quality and physiological fidelity over the raw noisy input, yielding 129\% and 105\% relative signal-to-noise ratio (SNR) improvements, and 66\% and 81\% relative reductions in heart-rate mean absolute error (MAE), on the Daily Activities and CIME datasets, respectively. MURFormer also outperforms an existing denoising baseline on both datasets with a relatively small parameter count while preserving beat-level timing and waveform morphology. In addition, the model maintains strong denoising performance across varying input window lengths, suggesting that MURFormer is an effective and robust framework for practical PPG denoising. The implementation of MURFormer is publicly available at this https URL

---


### 469. [The Staged Pandora's Box: Reservation Indices for Multi-Fidelity Bayesian Optimization](https://arxiv.org/abs/2611.02722)

**<font color=#1a73e8>作者：</font>** Long Vu, Jongseong Brad Choi, Binoy Ravindran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A staged search must decide which candidate to advance next and when to stop. Some observations only inform later decisions; others can be kept as results. We formulate these choices as a staged Pandora's box with a designated set of collectable stages. For independent finite-stage candidates with bounded readings and positive bounded own-history costs, an exact covered-call recursion gives the reservation index, the optimal value and the loss of every advance or stop; advancing an index-maximal candidate while its index exceeds the incumbent is optimal. The representation recovers classical single-stage search, nested inspection and the all-collectable Markov setting, and prices changes in the problem: enlarging the collectable set or lowering costs raises the value by an explicit covered-call overshoot. Resumption can be valuable even when future reward laws do not change, but has no value for deterministic readings. With information sharing across candidates, no rule using only their separate remaining-reading laws is universally optimal, and making an intermediate reading collectable can change which candidate is inspected first. Under a coherent joint path law with own-history costs, an approximate-planning bound controls the recomputed index's regret by changes in untouched candidates' local values; a common-component specialization bounds those changes through predictive total-variation dispersion. Exact finite-law experiments check the representation, the loss accounting and the bounds.

---


### 470. [Attention Residual U-Net for Enhanced Cross-Dataset Polyp Localization in Endoscopy](https://arxiv.org/abs/2611.02726)

**<font color=#1a73e8>作者：</font>** Romil Imtiaz, Dimitris K. Iakovidis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise localization of pathologies in endoscopy is a critical task in medical imaging, with deep learning (DL) frameworks now serving as the primary methodology for automated lesion detection. Today, generic object detection methods, such as YOLO, provide state-of-the-art performance in this context. However, their robustness often decreases under real-world clinical conditions due to variations across endoscopic devices, intestinal content, dataset bias, and the presence of small or low-contrast lesions. Motivated by these challenges, we propose a novel polyp detection framework based on a Attention Residual U-Net offering enhanced polyp localization. Instead of directly regressing bounding boxes from global feature representations, the proposed method learns lesion-focused spatial representations and converts them into bounding-box predictions during inference. Unlike conventional encoder-decoder localization frameworks that directly propagate all encoder activations into the decoding pathway, the proposed method selectively suppresses irrelevant background responses before feature reconstruction. This encourages the network to focus on lesion-relevant spatial evidence under heterogeneous imaging conditions. To achieve this, the framework integrates residual feature propagation, attention-guided encoder filtering, and multi-scale contextual learning. The proposed framework was evaluated on multiple public endoscopic datasets acquired using different devices. The comparative experimental results validate its effectiveness over the relevant state-of-the-art methods, with an improvement up to 22.0% in terms of the area under the receiving operating characteristic (AUC).

---


### 471. [Feature extraction for LSTM-based finger-joint angle estimation from sEMG](https://arxiv.org/abs/2611.02736)

**<font color=#1a73e8>作者：</font>** Gerda de Jager, Marelie H Davel, Ian Thomson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous estimation of finger-joint angles from surface electromyography (sEMG) is a promising approach for controlling dexterous myoelectric prostheses. Deep time series models have been applied successfully in this context, typically relying on feature extraction rather than raw signals, given limited subject-specific data. Various time-domain and frequency-domain features can be used, extracted for a given window and step size. This study systematically investigates these three design choices for Long Short-Term Memory (LSTM) regression on the Ninapro DB2 dataset. Window sizes from 300 to 1200 ms and step sizes from 10 to 100 ms were evaluated in combination with six time- and frequency-domain features. Models were evaluated using regression performance metrics, inference time, and memory footprint to assess feasibility on embedded microcontroller hardware suitable for a prosthetic device. A 300 ms window with a 100 ms step, paired with either the Mean Absolute Value (MAV) or Root Mean Squared (RMS) feature, yielded the best performance (test PCC of 0.779 +/- 0.080 / 0.779 +/- 0.085). Window size, step size, and feature choice were found to interact non-trivially: jointly tuning them can improve both accuracy and computational feasibility for real-time, embedded myoelectric control.

---


### 472. [MoviEdit: Long-form Multi-Shot Video Editing Made Easy](https://arxiv.org/abs/2611.02737)

**<font color=#1a73e8>作者：</font>** Suhyeon Lee, Zhengang Li, Soo Ye Kim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-form multi-shot video editing requires an intended edit to remain coherent across abrupt changes in scene, viewpoint, and subject appearance, while processing substantially longer visual context than conventional single-shot editors. We introduce MoviEdit, an end-to-end framework for scalable long-form multi-shot video editing that jointly addresses the challenges of data, modeling, and evaluation. To provide cross-shot supervision data at scale, we develop automatic data-generation pipelines spanning synchronized multi-view footage, real-world multi-shot videos, and generated multi-shot content, yielding 87K paired editing videos without manual annotation. Architecturally, MoviEdit employs a cascaded bidirectional-autoregressive design: a lightweight bidirectional stage first establishes a globally coherent editing draft over a spatiotemporally compressed representation, which is then autoregressively propagated and refined over the full video. We further introduce MoviEdit-Bench, a dedicated benchmark for systematic evaluation of long-form multi-shot video editing. Extensive experiments show that MoviEdit substantially outperforms existing open-source models and performs on par with industry frontier models across text-guided and image-guided editing. Visit our project page for complete results and to access the benchmark: this https URL

---


### 473. [Beyond Monotonicity: Stochastic Online Optimization under Semi-Bandit Feedback](https://arxiv.org/abs/2611.02739)

**<font color=#1a73e8>作者：</font>** Tsubasa Harada, Yasushi Kawase, Hanna Sumita  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study stochastic online optimization (SOO) under semi-bandit feedback: in each of $T$ rounds, a policy adaptively observes $n$ independent random variables with unknown distributions, learning only from observed values. First-order stochastic dominance (FSD) monotonicity enables general reductions for learning SOO, but can fail when observations change future feasibility, resource use, or reference points. Our algorithm runs the dynamic program for the optimal policy, replacing each expectation by its most optimistic value over a confidence set of distributions. Its regret depends on the level-set complexity $s_i$ of the computed values as functions of the $i$th variable: the number of intervals needed to describe their superlevel sets. For rewards in $[0,1]$, the regret is $\tilde{O}(\sqrt{ST})$ without this monotonicity, where $S=\sum_{i=1}^n\min\{s_i,k_i\}$ and $k_i$ is the support size of the $i$th distribution, which may be infinite when $s_i$ is finite. For constant level-set complexities, regret is $\tilde{O}(\sqrt{nT})$, even for continuous distributions. The algorithm requires no knowledge of $s_i$, $k_i$, or the supports, and it also achieves regret $\tilde{O}(\sqrt{nkT})$ for supports of size at most $k$ without any level-set condition, which improves the previous bound $\tilde{O}(n(\sqrt{kT}+k))$ for FSD-monotone problems. We also prove a lower bound of $\Omega(\min\{T,\sqrt{ST}\})$ for all positive integers $s_1,\ldots,s_n$ with $k_i=2s_i+1$, which holds even under full feedback and matches the upper bound up to logarithmic factors. We obtain $\tilde{O}(\sqrt{nT})$ regret for these problems, all nonmonotone under FSD: stochastic Boolean function evaluation, the full-information secretary problem, optimal stopping with loss aversion, scheduling with deadlines and correlated stochastic knapsack with unimodal rewards, and overbooking with group reservations.

---


### 474. [Subspace Representations for Synthetic-to-Real Transfer in 3-D Surface Inspection](https://arxiv.org/abs/2611.02744)

**<font color=#1a73e8>作者：</font>** Abdulla Nasir Chowdhury, Naish Ibrahim, Gulpi Qorik Oktagalu Pratamasunu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies what subspace representations contribute to synthetic-to-real transfer in 3-D surface inspection, where models learn from synthetic defects and the only real data before deployment are scans of good parts. We use three classical constructions as instruments: the nearest-subspace classifier, one-class template subspaces and the generalized difference subspace (GDS). On 1,197 MVTec 3D-AD scans without target annotation we find that every decision rule ranks real defects at a similar window AUC, that image-level detection stays at chance, and that no rule keeps its in-domain threshold. We show that the margin of a nearest-subspace rule moves by at most the part of the feature shift outside its class subspaces, and that this leakage, measured from unlabeled good scans, bounds the displacement observed on unseen scans. On 597 Real3D-AD objects, a one-class subspace of registered templates evaluated at every location on frozen features reaches point AUROC 0.957 on pre-registered scans and a category-mean object AUROC of 78 to 81 with no training on the benchmark. Our results suggest that a subspace helps under shift in proportion to the shift it spans, and that in reference-based inspection the reference and its registration matter more than the subspace.

---


### 475. [Pair-Relative Partial Equivariance for Rotation-Robust Keypoint Descriptor Matching](https://arxiv.org/abs/2611.02751)

**<font color=#1a73e8>作者：</font>** Jongmin Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned keypoint descriptors trained on upright imagery often fail under large in-plane rotation. Steerers address this by applying a single exact SO(2) representation to the descriptor space, but this global group constraint can be too rigid for keypoint descriptors, whose angular responses need not follow a single group representation. We propose pair-relative partial equivariance, which measures equivariance under the empirical distribution of relative rotations in image pairs, and PaSteer, a relaxed descriptor-steering framework that allows the steering map to leave the exact representation manifold while retaining the lightweight, backbone-free design of steering. PaSteer instantiates this relaxation with two variants: an identity-preserving residual steerer (PaSteer-soft) and a free-form Fourier steerer (PaSteer-free). We show that the per-angle optimal linear steerer for a fixed non-equivariant descriptor generally does not obey the group composition law, explaining why exact representations can be suboptimal in the frozen-descriptor regime. On Roto-360, MegaDepth-1500, AIMS, and IMC-PT, PaSteer consistently improves rotation-robust matching over an exact steerer on frozen DeDoDe descriptors, especially under large relative rotations, with minimal upright degradation.

---


### 476. [DINOFAS: Bonafide-Centric Representation Learning for Face Anti-Spoofing](https://arxiv.org/abs/2611.02756)

**<font color=#1a73e8>作者：</font>** Shakeel Muhammad Ibrahim, Muhammad Sohail Ibrahim, Muhammad Shahid Jabbar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face anti-spoofing (FAS) models often learn attack- and dataset-specific cues that degrade performance under unseen acquisition conditions and presentation attacks. We present DINOFAS, a DINOv3-based framework that formulates FAS as bonafide-centric representation learning. The proposed framework combines parameter-efficient DINOv3 adaptation using low-rank adaptation (LoRA), an attention style-content disentanglement (ASCD) module for reducing domain-specific appearance variations, and a dual-branch architecture that separates prototype-based liveness learning from attack-semantic supervision. The model is jointly optimized using a bonafide-centric prototype objective, an attack-semantic classification loss applied to detached features, and orthogonality regularization. DINOFAS achieves an average HTER of 9.09\% under the standard OCIM leave-one-domain-out protocol, where training is performed on three source datasets and evaluation is conducted on the held-out unseen domain. We further evaluate synthetic-to-real generalization by training exclusively on SynthASpoof and testing on four unseen real-world datasets, where DINOFAS achieves the lowest average HTER of 21.41\% and the highest average AUC of 86.14\% among the compared methods. Evaluations on OULU-NPU and SiW-Mv2 additionally demonstrate robustness to variations in acquisition conditions, devices, and unseen presentation attacks.

---


### 477. [GaussFlaw: Fine-Grained Perceptual Diagnosis for 3D Gaussian Splatting](https://arxiv.org/abs/2611.02767)

**<font color=#1a73e8>作者：</font>** Shaocheng Shen, Zihan Zheng, Kejin Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables photorealistic novel- view synthesis with real-time rendering, yet fine-grained di- agnosis of its rendering artifacts remains challenging. These artifacts are typically spatially localized and exhibit diverse degradation patterns, making them difficult to character- ize using global quality metrics and image-level assessment benchmarks, which provide no explicit indication of where they occur or what types of artifacts they represent. To ad- dress this limitation, we introduce GaussFlaw-80K, the first large-scale dataset for fine-grained perceptual diagnosis in 3DGS. Constructed through a model-assisted human-in-the- loop pipeline, GaussFlaw-80K contains 80,049 artifact re- gions across 14,289 rendered images, each annotated with a pixel-level mask and one of eight flaw labels spanning ge- ometric, blending, and photometric degradations. These an- notations turn 3DGS artifact diagnosis into an explicit and measurable task. Building on this dataset, we propose Ge- oCritic, a geometry-guided multi-task model that integrates RGB appearance with depth-derived cues to jointly localize artifacts and classify their flaw types. Beyond evaluation, we further demonstrate the downstream benefits of fine-grained diagnosis through three complementary targeted operations: Gaussian densification, attribute correction, and outlier prun- ing. Experiments show that GeoCritic achieves an AUC-J of 0.9507 and an Acc@1 of 80.08%, while diagnosis-guided re- finement improves all reported global and crop-level metrics across diverse datasets and 3DGS backbones.

---


### 478. [Stage-aware Multimodal Brain Graph Contrastive Learning for Neurodegenerative Disorder Diagnosis](https://arxiv.org/abs/2611.02771)

**<font color=#1a73e8>作者：</font>** Jingjing Zhou, Chenxuan Meng, Ciyuan Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neurodegenerative disorders are characterized by their progressive nature, with distinct stages that require precise identification and tracking of progression trajectories for accurate diagnosis. However, existing diagnostic methods often fail to fully capture the unique brain patterns associated with different stages, limiting their ability to effectively target specific stages of the disorders. To address this issue, we propose a Stage-aware Multimodal Brain Graph Contrastive Learning (smBGC) method. Specifically, smBGC introduces a stage-aware feature enhancement strategy to capture stage-specific features across all progression stages, enabling the generation of stage-aware multimodal brain graph representations. In addition, smBGC incorporates a stage-adaptive brain graph augmentation approach within a graph contrastive learning framework, facilitating multimodal fusion and improving the model's capability to distinguish between different disorder stages. Experiments on two real-world datasets demonstrate the superior performance of smBGC in various neurodegenerative disorder diagnosis tasks compared with state-of-the-art methods.

---


### 479. [DIKT: A Diagnostic and Interpretable Knowledge Tracing Framework for Prediction and Model-based Learning Analysis](https://arxiv.org/abs/2611.02774)

**<font color=#1a73e8>作者：</font>** Yi-Qiang Wua, Shaohui Chen, Hanlin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge tracing is a key component of intelligent educational systems. However, most existing methods mainly focus on response prediction, providing limited support for explaining predicted outcomes and improving students'learning states. This paper proposes Diagnostic and Interpretable Knowledge Tracing (DIKT), which integrates response prediction, skill-level diagnosis, and model-based learning analysis. DIKT generates bounded cognitive-state trajectories and decomposes the final response probability into skill-wise probabilities. The trajectories reveal students'evolving strengths and weaknesses, while the skill-wise probabilities identify the skills that most strongly constrain the prediction. Based on these diagnostic results, DIKT supports direct cognitive-state intervention and effective-learning-duration-based what-if analysis to examine how hypothetical adjustments affect current predictions and subsequent state evolution. DIKT combines Bayesian multi-head attention, conditional variational recurrent inference, a logistic-growth decoder, and multiplicative skill-wise prediction. Experiments on three benchmark datasets show that DIKT outperforms all evaluated baselines, with an average absolute AUC gain of 2.04 percentage points. Other experiments further demonstrate that DIKT supports educationally meaningful diagnostic analysis and provides informative diagnostic indicators for downstream applications, extending knowledge tracing from response prediction to interpretable diagnosis and model-based learning analysis.

---


### 480. [Risk-Constrained Evaluation of Financial Document Recognition: A Formal Framework for Evidence, Critical Errors, and Selective Automation](https://arxiv.org/abs/2611.02775)

**<font color=#1a73e8>作者：</font>** Subodh Lonkar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Financial document recognition is commonly evaluated using character and word error rates, which do not adequately represent the consequences of errors in financial workflows. This paper formalizes financial document recognition as a risk-constrained evidence-recovery problem. It defines typed, evidence-linked financial facts and a multi-layer quality model spanning text, layout, tables, fields, semantic relations, calibration, robustness, and operational performance. It introduces non-compensatory acceptance gates based on upper confidence bounds for critical-field errors, and formulates selective automation as a constrained risk-coverage problem with review-capacity limits. The paper also specifies annotation requirements, leakage-resistant benchmark splits, statistical estimands, and a reproducibility card. Formal propositions establish why aggregate scores cannot certify critical-field reliability and why zero observed errors do not imply zero risk. A synthetic example illustrates the decision rule. The work is theoretical; no empirical benchmark or model performance claim is presented.

---


### 481. [LipLingo: CNN Model for Lip Reading](https://arxiv.org/abs/2611.02776)

**<font color=#1a73e8>作者：</font>** Mahmoud S. Mayaleh, Liban Ali Achkir, Nijat Mehdiyev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lip reading plays a crucial role in applications such as speech recognition, assistive technologies for the hearing-impaired, and biometric authentication. However, performance often degrades when the speaker varies and when certain speech sounds are visually similar. To address these challenges, we propose LipLingo, a robust lip-reading system based on the LipNet architecture, enhanced with a standardized preprocessing pipeline for consistent mouth-region representation, a rotational validation strategy for improved generalization to unseen speakers, and a flexible similarity evaluation for more reliable sentence-level assessment. The model architecture combines 3D convolutional layers for spatio-temporal feature extraction and bidirectional recurrent layers for sequence modeling, optimized using the Adam optimizer and Connectionist Temporal Classification (CTC) loss. On the GRID dataset, LipLingo achieved 95.0\% character-level accuracy (CER 4.99\%) and 87.2\% sentence-level accuracy. At the corpus level, the system obtained a (WER 13.1\%), outperforming the baseline LipNet and demonstrating competitive performance relative to recent 3D-ResNet + Bi-GRU + MixUp approaches. These results provide insights into strategies that enhance lip-reading robustness and highlight directions for future work toward real-world deployment.

---


### 482. [Spectral Degeneration of Self-Attention under Isotropic Score Geometry](https://arxiv.org/abs/2611.02778)

**<font color=#1a73e8>作者：</font>** Mengda Li, Jianfeng Yao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the spectral structure of the self-attention matrix in Transformer models through an idealized spectral model for the pre-softmax score matrix. Motivated by the rotational isotropy of query and key representations, our model replaces the random token-space orientation of the score matrix by its canonical singular-value representative with a logarithmic spike--bulk separation. Empirical diagnostics on pretrained vision and language transformers motivate this model: token-space singular matrices have nearly uniform eigen-angle distributions, and score spectra are dominated by a small number of effective directions. We then prove that the row-wise softmax map transforms this structure into a degenerate attention matrix: dominant modes are preserved, whereas the bulk spectral distributions concentrate at zero. Stable rank remains bounded for bidirectional attention but grows logarithmically for causal attention. Within the canonical model, these results explain how attention can preserve a small number of dominant directions while compressing the remaining bulk modes.

---


### 483. [Local-Global Joint Modeling for Point Cloud Super-Resolution Guided by Multi-Scale Spatial Priors](https://arxiv.org/abs/2611.02786)

**<font color=#1a73e8>作者：</font>** Wang Yang, Wenyi Ge  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Range-image-based point cloud super-resolution provides an effective way to reconstruct sparse outdoor point clouds by projecting low-resolution LiDAR scans into a regular 2D representation. However, current methods still face three challenges. First, range images exhibit pronounced vertical nonuniformity, with sparse observations in distant regions and denser observations in nearby regions. Some cross-scale fusion mechanisms do not account for the varying reliability of features at different vertical positions, allowing invalid values and noise from distant sparse regions to propagate into the decoder. Second, a single convolutional or sequence-modeling architecture often struggles to preserve both local high-frequency geometric details and global long-range dependencies, resulting in over-smoothed reconstructions. Third, smooth transition depths near foreground-background boundaries can produce spike artifacts when the 2D range image is back-projected into 3D. To address these issues, we propose a point cloud super-resolution method based on multi-scale spatial priors and joint local-global modeling. The design comprises a spatially gated fusion module, a multi-granularity local-global cooperative perception module, and 2D median-residual denoising. Experiments on KITTI-360 and nuScenes demonstrate effective reconstruction, with IoU scores of 0.4703 and 0.3593, respectively, supporting the feasibility of the proposed method for range-image super-resolution.

---


### 484. [MultiMental-IAS: A Multimodal Driver Mental State Analysis Dataset for Context-Aware Non-IID Evaluation](https://arxiv.org/abs/2611.02790)

**<font color=#1a73e8>作者：</font>** Baran Can Gül, Nagendra Pal Singh, Anjana Arvind Naik  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Robust driver-state modelling requires synchronized physiological, behavioural, and contextual signals, yet existing open resources typically target a single cognitive state, omit continuous vehicle context, or do not define evaluation protocols that expose inter-subject heterogeneity. We present Multimental-IAS, a multimodal driver mental-state dataset collected in a cockpit-in-the-loop simulation built on CARLA. It contains vehicle telemetry with scenario-context channels, four-channel EEG and three-channel PPG from a Muse 2 headband, and cabin-facing video from 23 participants, recorded in 148 trials (11.6 hours) under six induced states: Normal, Distracted, Alerted, Stressed, Relaxed, and Drowsy. We document the acquisition pipeline in detail and provide a benchmark with one protocol for all models: chronological within-subject splits, participant-disjoint cross-subject folds, validation-based model selection, and ablations over modalities, scenario-context channels, and signal normalization. Multimodal fusion reaches a macro-F1 of 0.94 for drivers seen during training. For unseen drivers, fusing driving dynamics with per-window normalized EEG/PPG raises macro-F1 from 0.408 (telemetry alone) to 0.485, consistently across all five folds, while the gap between the two protocols quantifies the inter-driver heterogeneity that personalized models must address. Multimental-IAS thus provides a concrete testbed for non-IID generalization, personalization, and federated learning in driver monitoring.

---


### 485. [SelfImprove-Bench: Evaluating Generalization in Self-Improving Agents](https://arxiv.org/abs/2611.02797)

**<font color=#1a73e8>作者：</font>** Bangrui Xu, Jie Yang, Sidi Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursively self-improving (RSI) systems are increasingly viewed as a promising means of accelerating progress toward artificial general intelligence. They aim to autonomously improve their capabilities by refining their working pipelines and recursively improving the strategies that guide subsequent refinements, with gains generalizing to unseen this http URL, existing evaluations lack reliable metrics to distinguish capability gains from scenario fitting, sustainable and extensible protocols for unseen tasks and difficulties, and fine-grained attribution of improvement to evolution traces. To this end, we propose SelfImprove-Bench,an RSI evaluation framework that organizes tasks into three primary capabilities (i.e., Exploring, Planning, Reasoning) as scenarios for guiding model evolution. We instantiated the tasks on games for controllability and reproducibility, and pairs them with scalable generation and orchestration driven by task templates and difficulty coefficients. Beyond task-level scores, SelfImprove-Bench organizes evaluation into generalization ladder levels G0 to G4 that measure how far gains transfer from training conditions. Experiments reveal that the evolutionary gains of existing RSI methods are inconsistent across generalization levels.

---


### 486. [Analysing the Narrative Paradox through Formal Models and Properties in Interactive Narrative](https://arxiv.org/abs/2611.02801)

**<font color=#1a73e8>作者：</font>** Jules Clerc, Mohamed Sallak, Domitile Lourdeaux 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive narratives aim to let players influence the unfolding of a story while preserving a coherent and satisfying narrative progression. This creates a central tension, commonly described as the narrative paradox, between player autonomy and narrative control. Experience Managers (EMs) manage the story by determining how the narrative progresses in response to player behaviour. Although this paradox is widely discussed, it is rarely modelled in a way that supports systematic analysis, simulation, and comparison across management strategies. This paper proposes a formal framework for modelling and analysing the narrative paradox as a trade-off between interdependent properties shaped by EM decisions. We represent interactive narrative behaviour through an extended state-transition system in which world states are connected by player actions and system events. From this model, we formalize key properties involved in the paradox such as the player agency, EM controllability, author intent, and robustness, and define quantitative indicators derived from simulated plans. These indicators make it possible to compare EM strategies according to their ability to balance freedom, control, and narrative satisfaction. A case study compares different EM policies, showing how simulations can reveal correlations and conflicts between properties and identify compromise zones in the design space. This work contributes a reusable modelling and analysis framework for studying the narrative paradox and evaluating heterogeneous interactive narratives on shared formal grounds, with a focus on supporting the comparison and testing of EM strategies.

---


### 487. [SynForecast: Controlled Synthetic Time Series for Forecasting Research](https://arxiv.org/abs/2611.02802)

**<font color=#1a73e8>作者：</font>** Olivier Sprangers, Cristian Challu, Jan Rathfelder 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic time series constitute a substantial share of the training corpora of several recent forecasting foundation models. Existing studies report benefits at small data budgets and modest synthetic proportions, but each evaluates individual combinations of model and generator. Studying these benefits systematically requires generators that support controlled configuration, perturbation, reproducibility and mechanism-level ablation, and the 11 existing generators we review show gaps in this combined support.
We present SynForecast, an open-source Python library with 32 generators, 19 of which implement named mechanisms with a published source in econometrics, quantitative finance, statistical physics and point-process theory. Perturbations and mechanism families can be varied while everything else is held fixed, output comes in the long format that forecasting libraries accept, and output does not depend on the number of parallel workers.
We evaluate SynForecast on M4 at five frequencies with a neural network and a gradient-boosted ensemble. A classical baseline attains the lowest error in nine of ten frequency-history combinations. A synthetic prior outperforms the same network trained from scratch at a fixed budget by up to 34% with a few dozen observations, but loses to it at full history at every frequency, and none of three pre-specified rescalings of history predicts where the sign changes. At the hourly frequency, where the prior fails at every history, the corpus lacks daily cycles; adding them reduces zero-shot error by 43 to 63% for both models. Fine-tuning outperforms training from scratch by up to about 15%, but at short histories a fixed 300-step fine-tune is worse than the pretrained model used as is. Removing the classical mechanism family costs about 2% for both models; every other family has a smaller effect outside the hourly frequency.

---


### 488. [CARE: Contrastive Representation Learning with Environment-Invariance Regularization for Behavioural Intention Prediction](https://arxiv.org/abs/2611.02806)

**<font color=#1a73e8>作者：</font>** Shang Gao, Zhixin Huang, Franz Götz-Hahn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory-based behavioural intention prediction faces environmental variation, and representations learned with a pooled contrastive objective may retain environment-specific regularities. We present CARE, a self-supervised trajectory-learning framework that couples temporally asymmetric contrastive views with an invariant-risk-minimisation (IRM)-style gradient penalty on environment-wise contrastive risks. Each input window yields an anchor, a partially masked positive view, and a temporally perturbed negative view. Masked reconstruction and observability-aware evidence consistency complement this objective by promoting temporal information retention under partial input. On an IMPTC-derived four-class intention task, CARE achieves 0.840 accuracy and 0.023 expected calibration error (ECE) under IID fine-tuning, and 0.806 accuracy with a Brier score of 0.308 on the reported held-out environment. Under frozen-encoder linear probing, reconstruction provides the largest individual held-out accuracy gain, whereas the complete objective yields the lowest held-out ECE (0.049) among tested variants. These results support the combined objective as a competitive representation-learning approach under the evaluated shift, while the IRM-style regulariser is not taken as evidence of formal invariance.

---


### 489. [Offline Approximate Value Iteration: A Reinforcement Learning Approach for Satellite Constellation Deployment](https://arxiv.org/abs/2611.02809)

**<font color=#1a73e8>作者：</font>** Tristan Leuridan, Yiping Fang, Adam Abdin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces a reinforcement learning-based approximate dynamic programming approach to optimize the deployment of Walker-type satellite constellations under uncertainties, including launch failures and satellite malfunctions. We formulate the problem as a Markov Decision Process that incorporates low-injection orbit launches, continuous low-thrust orbit raising, and variable satellite loads. We adopt the offline approximate value iteration solution method, using linear function approximation with basis functions and action pruning strategies to substantially reduce the computational and memory requirements for finding optimal decision policies. Preliminary results demonstrate convergence to policies with low expected costs and deployment times, both of which are lower than those of a rolling-horizon baseline, showcasing a novel application of approximate dynamic programming in space logistics.

---


### 490. [When Is Tracking Affordable? A Movement-Budget Feasibility Threshold for Dynamic Regret](https://arxiv.org/abs/2611.02812)

**<font color=#1a73e8>作者：</font>** Ridham Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic regret measures an online learner against a moving comparator, and standard analyses assume the learner may move freely at every round. We study what happens when it may not: the learner is given a hard budget $S$ on its total movement $\sum_t \|x_t - x_{t-1}\|$. Our main result is that a movement budget creates a feasibility barrier. On a domain of diameter $D$ with $G$-Lipschitz convex losses, for every comparator path length $P_T \in [D, DT]$ we exhibit a deterministic adversary that forces $R_d = \Omega(GDT)$ on every budget-feasible algorithm whenever $S \le c P_T$ for a universal constant $c>0$. This barrier is caused by the budget rather than by a volatile environment: for fixed $D$, it applies when $P_T = o(T)$, where the unconstrained minimax rate $\Theta(G\sqrt{D(D+P_T)T})$ is sublinear, so the same instances are learnable with an unbounded budget and unlearnable without one. Conversely, projected online gradient descent with a budget-aware step size is budget-feasible and attains $o(GDT)$ once $S = \omega(D + P_T)$. Thus the critical movement scale is $D+P_T$: linear regret is unavoidable below a sufficiently small constant multiple of $P_T$, while sublinear regret is achievable when $S/(D+P_T)\to\infty$ in the learnable regime. The construction rests on a distinction we make explicit: what makes a comparator expensive to track under a movement budget is the distance it forces the learner to travel, not its path length. Above the threshold we give a budget-dependent upper bound and identify the tight minimax rate in this region as an open problem rather than claiming a product law. Experiments support the predicted transition location and the $1/S$ decay.

---


### 491. [Efficient Detailed Scheduling of Multiproduct Pipelines using Action-Decoupled Deep Reinforcement Learning](https://arxiv.org/abs/2611.02823)

**<font color=#1a73e8>作者：</font>** Kai Shao, Ling Jian, Liming Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multiproduct pipelines transport refined products to delivery stations in sequential batches, and their detailed scheduling must meet market demand while respecting nonlinear hydraulic constraints. Retaining the full hydraulic nonlinearity yields a mixed-integer nonlinear program that is computationally intractable, while the linearization commonly adopted for solver-based optimization degrades hydraulic accuracy without resolving the heavy computational burden. This paper develops an action-decoupled proximal policy optimization (PPO) framework that efficiently produces detailed schedules while preserving hydraulic fidelity. The scheduling process is cast as a semi-Markov decision process (SMDP) with flexible action durations. To handle the discrete-continuous hybrid action space, a cascaded dual-actor architecture decouples the discrete operating duration from the continuous flow decisions, eliminating the gradient interference that destabilizes conventional coupled-action policies and thereby yielding high-quality schedules far more efficiently. Validated on a real-world multiproduct pipeline in China and benchmarked against a single-actor baseline and a linearized MILP solved by Gurobi, the proposed framework achieves delivery accuracy close to the exact optimum while substantially improving flow rate stability and substantially reducing solution time.

---


### 492. [GraTED: Graph--Tensor EEG Decoding for Passenger Hazard Perception in Autonomous Vehicles](https://arxiv.org/abs/2611.02827)

**<font color=#1a73e8>作者：</font>** Yuxuan Gu, Yingkai Yang, Qiyu Rao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Passenger electroencephalography (EEG) can reveal road risk through anticipatory responses before hazardous events and neural reactions around their onset. However, existing EEG decoding methods often map physiologically meaningful arrangement of electrodes onto artificial 2D grids and thus flatten the higher-order time-feature representations into matrices, obscuring meaningful structure in the data. To preserve and exploit the spatial and time-feature structure of EEG recordings, we propose the Graph-Tensor EEG Decoding Model (GraTED) for passenger risk prediction (RP) and danger identification (DI) in autonomous-vehicle scenarios. GraTED models the electrode arrangement as an undirected graph based on their scalp locations, using graph convolution to capture spatial dependencies and low-rank tensor classification to preserve the multidimensional time-feature structure, while controlling model complexity. Evaluated on the PassengerEEG dataset, comprising 11 participants and 45 hours of recordings, GraTED achieves the highest balanced accuracy, compared to the state-of-the-art, across all three evaluation settings, while requiring the fewest learnable parameters among seven baseline methods.

---


### 493. [Window-Aware Scheduling for Health Messaging under Platform Delivery Constraints: Evidence from an AI-Powered WhatsApp Maternal and Infant Health Chatbot in Nigeria](https://arxiv.org/abs/2611.02834)

**<font color=#1a73e8>作者：</font>** Jeremiah Moyondafoluwa Adepoju, Samuel Omolaiye, Thanni Adewuyi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> WhatsApp lets a business send free-form messages only within 24 hours of a user's last message; outside this customer service window, only pre-approved templates are delivered. Health chatbots inherit this rule, but its cost is rarely measured. We analyse 98,607 messages sent to 3,696 mothers by a WhatsApp maternal health chatbot in Nigeria, with a largely separate export as replication. No free-form message failed with the window open (0 of 35,500), and failure jumped by 93.0 percentage points (95% CI 87.0 to 99.1) at exactly 24 hours. Two flows produced 66.1% of failures, including an offer to speak with a medical professional that, as built, reached 0.3 in 100 mothers whose window had closed. We formalise window-aware scheduling as a decision problem with an action of known zero value. Model-based offline evaluation, with bounds for unconfirmed delivery, estimates that sending the offer as an approved template would reach 81.5 to 86.8 in 100 such mothers, against 16.6 for waiting and 11.6 for a reply prompt. In a calibrated simulation, tabular Q-learning converges to the same template rule and does not beat it in any of 13 stress tests, and opting out does not rise with message volume. The main gain comes from respecting the platform rule, and it needs no learning. All outcomes are deliveries, not health outcomes.

---


### 494. [Omni-Life: Benchmarking Omnimodal Real-Time AI Assistants in People's Daily Lives](https://arxiv.org/abs/2611.02835)

**<font color=#1a73e8>作者：</font>** Mengze Hong, Ziwei Shang, Di Liang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-time omnimodal assistants are expected to support people in everyday life, but audiovisual understanding alone does not establish whether they can provide timely and appropriate help. We introduce Omni-Life, a benchmark grounded in real-world user needs, deployment scenarios, and device-dependent observations. It combines controlled video synthesis for hazardous situations and edge cases with annotated real-world videos under a shared temporal protocol. The benchmark contains 400 videos: 290 requiring assistance, with 555 required intervention events, and 110 requiring silence throughout to test whether models can withhold unnecessary responses when no assistance is needed. We evaluate twelve configurations featuring mainstream real-time omnimodal models, jointly assessing event coverage, response content, timing, and unwanted output. At most 4.48% of videos requiring assistance are handled completely correctly. To examine practical deployment strategies, we study task reminders and response-latency tolerance. Reminders can improve recall by 17.12 percentage points but add approximately 4.6 unwanted responses per minute of reference silence. Increasing latency tolerance by 10s improves recall by at most 5.95 percentage points. These results show that existing models remain insufficient to deliver reliable assistance in real-life applications, calling for tailored model optimization in instruction following, timely proactive intervention, and withholding responses when assistance is not needed.

---


### 495. [CARE: Grounded Recursive Self-Improvement for Production Customer-Service Agents](https://arxiv.org/abs/2611.02839)

**<font color=#1a73e8>作者：</font>** Yanbei Jiang, Chao Lei, Rena Gao 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) in production agents involves transforming accumulated experience into reliable model updates while adapting to evolving business policies. We present CARE (Customer-service Agent Retrospective and Evolve), a grounded RSI framework that operationalizes this process in customer service. Its goal is to replace a frontier proprietary incumbent with an in-house mid-sized model that continues learning after deployment. After a one-time cold start on governed production traces, the current model serves production traffic alongside the incumbent, and its own failures drive the next update. A 24/7 inspection process establishes failures through evidence-blinded, independently reviewed judgments. Attribution separates model errors from defects in Skills, tools, or the harness, routing component failures to repair. Model-attributable trajectories are truncated at the first erroneous decision and paired with verified repairs. On-policy self-distillation (OPSD) then updates the model using the same model as teacher, with the diagnosis and repair supplied as privileged information unavailable to the student. To support continued evolution as business requirements change, training mixes failures from different Skill/SOP versions, each judged against the policy in force when it occurred. Candidates run an executable simulation test compiled from the latest SOP and then frozen, followed by offline inspection of the resulting traces. Promotion requires a combined simulation-and-inspection score at least at parity with the deployed version, confirmation through an online comparison with the incumbent, and human approval.

---


### 496. [Iterated Narrow Networks: Turing Completeness at Width 4 on Convex Input Spaces and the Complexity of Verification](https://arxiv.org/abs/2611.02840)

**<font color=#1a73e8>作者：</font>** Olivier Bournez, Johanne Cohen, Adrian Wurm  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the iterates of a fixed ReLU network $N$ of width 4, that is, the discrete-time system $x_{k+1} = N(x_k)$ on $[0,1]^4$. Equivalently, $x_k$ is the output of a weight-tied network made of $k$ copies of $N$, or of a recurrent network with no external input, started at $x_0$. We prove that every deterministic Turing machine $M$ admits such a network $N_M$. The network can be constructed in polynomial time from $M$. Each iteration has depth $\mathrm{poly}(|M|)$. The iterates of $N_M$ simulate $M$ exactly on every encoded tape. The number of iterations is proportional to the running time of $M$. Moreover, the fourth coordinate irreversibly flags every point of the convex cube $[0,1]^4$ whose simulation reads an invalid digit. This flag is the certificate that makes hardness reductions sound on convex input regions, the regime of practical verifiers. Convex regions were previously inaccessible because of a continuity obstruction inherent to ReLU networks. The correspondence has three consequences. First, reachability for iterated width-4 ReLU networks spans the full complexity hierarchy along the single axis of the time bound: it is NP-complete for a unary bound, NEXP-complete for a binary bound and RE-complete (undecidable) with no bound. Second, two extra neurons of width suffice to extend the hardness to every common smooth activation: at width 6, the robust verification problem (a promise problem with $\delta/2\delta$ gap) is NP-complete for $\tanh$, sigmoid, GELU, Swish, ELU, and any polynomial-time-computable continuous non-polynomial activation with a polynomial-time-computable Lipschitz constant. Third, the whole spectrum transfers to discretized Neural ODEs in dimension 5.

---


### 497. [NIR: Approximate Neural Instance Retrieval for ALCIQ](https://arxiv.org/abs/2611.02842)

**<font color=#1a73e8>作者：</font>** N'Dah Jean Kouagou, Pritilata Saha, Caglar Demir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instance retrieval is the main bottleneck of concept-learning systems based on refinement operators. We present NIR, a family of neural instance retrievers for ALCIQ that output graded membership scores from knowledge graph embeddings. We compare tokenization-based encoders (GRU, LSTM, Transformer) with a Compositional encoder that mirrors DL operators via primitive sub-networks. On eight benchmarks, all variants approximate Pellet closely on complete knowledge bases, while the Transformer model is most robust under incompleteness. The source code of our approach is at this https URL.

---


### 498. [Aerial Content-Aware Sample-Adaptive Classifier for Urban Photogrammetric Point Cloud Segmentation](https://arxiv.org/abs/2611.02844)

**<font color=#1a73e8>作者：</font>** Chong Liu, Yonghua Lu, Zhanglin Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban photogrammetric point clouds are commonly processed as local 3D patches, limiting the context available for distinguishing geometrically similar categories. Orthographic projection of the same data yields a co-registered digital orthophoto map (DOM)/RGB-D representation that supports efficient large-context modeling but compresses vertical geometry. Existing projection--point methods mainly fuse these two representations at the feature level while retaining a classifier shared across all samples. We present the Aerial Content-Aware Sample-Adaptive Classifier (ACASAC), which complements feature fusion with decision-level adaptation. A point-aligned aerial region bridges the full aerial crop and local 3D patch. ACASAC models scene-to-local variation within the projection and the representation discrepancy between aligned 2D and 3D supports, then transfers both relations to refine the local point class representation. The refined representation, scene-level aerial context, and fixed fused-head prior jointly form a classifier for the current sample. ACASAC improves the fixed dual-representation head by 2.1 and 2.7 mIoU points on SensatUrban and UrbanBIS, respectively, and by 2.1--2.3 points across four tested encoder combinations.

---


### 499. [Scaling Action-Free Video Latent Prediction for Transferable Representations in End-to-End Autonomous Driving](https://arxiv.org/abs/2611.02853)

**<font color=#1a73e8>作者：</font>** Xingtai Gui, Xubin Zhou, Yucheng Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end autonomous driving policies require effective visual representations that capture both spatial scene structure and temporal dynamics. Video latent prediction has emerged as an effective paradigm for learning spatiotemporal visual representations, yet it remains unclear whether scaling this objective with action-free driving videos can yield representations that benefit end-to-end planning. We study action-free video latent prediction as a scalable pretraining objective and introduce ScaleDrive, a driving-oriented framework pretrained exclusively on large-scale internet open-world driving videos, without action annotations or benchmark-specific data. We keep the pretrained video encoder frozen during downstream end-to-end planning training to isolate the transferability of representations learned from internet driving videos. Ego-motion and depth probes show that scaling action-free video pretraining progressively strengthens the temporal and geometric information encoded in the frozen representation. We systematically study the visual representation transfer across different end-to-end driving policies and closed-loop benchmarks, where ScaleDrive consistently improves downstream performance and demonstrates that scaling action-free video latent prediction yields representations that generalize across both planning policy architectures and evaluation scenarios and protocols.

---


### 500. [Task Adaptation Through Guidance in Frozen Feature Upsampling](https://arxiv.org/abs/2611.02854)

**<font color=#1a73e8>作者：</font>** Pingan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting features before upsampling can improve dense prediction, but the gains may arise from changes in feature values, spatial aggregation, or both. We investigate this ambiguity by comparing matched residual adapters before and after a frozen JAFAR upsampler under a shared parent. We construct a readout-null intervention that preserves a frozen linear classifier's coarse logits while allowing spatial attention weights to adapt. Guidance/value exchanges on trained models and retrained fixed-guidance controls test the utility of this adaptation route. In three-seed experiments on PASCAL Visual Object Classes (VOC) and Cityscapes, adaptation before upsampling improves mean intersection over union (mIoU) by 0.807 and 1.413 percentage points, respectively, over adaptation after upsampling. Across both datasets and the JAFAR and AnyUp upsamplers, readout-null adaptation produces mean gains of 1.379-1.987 points over the corresponding frozen linear baselines. Retrained controls further support the benefit of adaptive spatial guidance. These findings explain how dense predictions can improve despite unchanged coarse classifier outputs and identify spatial guidance as a useful target when adapting frozen feature upsampling systems.

---


> [!TIP]
> 当前位于：**451-500**（第 10/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
