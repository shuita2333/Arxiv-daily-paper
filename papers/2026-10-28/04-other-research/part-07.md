# 📦 其他研究 | 2026年10月28日

> 本类共 **446** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-446](./part-09.md)

---

### 301. [Rethinking Data Imbalance in Class Incremental Surgical Instrument Segmentation](https://arxiv.org/abs/2610.34925)

**<font color=#1a73e8>作者：</font>** Shifang Zhao, Long Bai, Kun Yuan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In surgical instrument segmentation, the increasing variety of instruments over time poses a significant challenge for existing neural networks, as they are unable to effectively learn such incremental tasks and suffer from catastrophic forgetting. When learning new data, the model experiences a sharp performance drop on previously learned data. Although several continual learning methods have been proposed for incremental understanding tasks in surgical scenarios, the issue of data imbalance often leads to a strong bias in the segmentation head, resulting in poor performance. Data imbalance can occur in two forms: (i) class imbalance between new and old data, and (ii) class imbalance within the same time point of data. Such imbalances often cause the dominant classes to take over the training process of continual semantic segmentation (CSS). To address this issue, we propose SurgCSS, a novel plug-and-play CSS framework for surgical instrument segmentation under data imbalance. Specifically, we generate realistic surgical backgrounds through inpainting and blend instrument foregrounds with the generated backgrounds in a class-aware manner to balance the data distribution in various scenarios. We further propose the Class Desensitization Loss by employing contrastive learning to correct edge biases caused by data imbalance. Moreover, we dynamically fuse the weight parameters of the old and new models to achieve a better trade-off between the biased and unbiased model weights. To investigate the data imbalance problem in surgical scenarios, we construct a new benchmark for surgical instrument CSS by integrating datasets. Extensive experiments demonstrate the effectiveness of the proposed framework, achieving significant performance improvement against existing baselines.

---


### 302. [Supervising the Visible State: Separating Representation from View Selection in Streaming Video](https://arxiv.org/abs/2610.34926)

**<font color=#1a73e8>作者：</font>** Yihao Hu, Pan Wang, Yitong Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An action seen once and the same action seen three times receive the same action-recognition label, so that supervision does not require a model to count. Answers shared across histories that differ in event order, accumulation, or relations leave those distinctions unconstrained; we call this state under-specification. Visible-State Supervision (ViSS) addresses it by training on source-grounded probes of event identity, order, accumulation, relation change, and answer sufficiency; under the same recent-frame interface it improves OVO-Bench over a strict-matched generic temporal supervision baseline while remaining comparable on StreamingBench, with the largest gain in hallucination detection. Test-Time Causal View Search (TVS) then adapts evidence access while keeping the learned model fixed, expanding from recent frames to sparse event and compact history views on demand. The two interventions separate representation from view selection: supervision particularly benefits hallucination detection and causal reasoning, access particularly benefits event recall and forward reasoning. Together they reach the best reported accuracy among the published systems compared here on StreamingBench and OVO-Bench at a fraction of the processed frames of exhaustive selection, and strict replay shows that most of the remaining gap to a three-view oracle is a correct answer that was later replaced. Streaming accuracy depends on what supervision asks the model to keep, what evidence inference exposes, and whether the model keeps a correct answer once it has one.

---


### 303. [A Certified Robustness Framework for Backdoor Poisoning Attacks using $f$-Divergences](https://arxiv.org/abs/2610.34934)

**<font color=#1a73e8>作者：</font>** Evan Rose, Alina Oprea  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning systems trained on untrusted data are vulnerable to data and backdoor poisoning attacks, in which an adversary corrupts training and test samples to manipulate predictions at inference time. Randomized smoothing yields provable defenses against such attacks, but existing applications to train-time robustness are limited to specific threat models and smoothing mechanisms. We propose a general framework that allows expressing complex adversary constraints on the number of corrupted training examples, feature and label perturbation magnitudes, and test-time corruptions. Our framework randomizes inputs by combining data subsampling with feature, label and test-sample noising. We develop a composable certification procedure based on $f$-divergences that handles arbitrary combinations of threat models and noising strategies, and recovers several prior certification regimes exactly as special cases. We demonstrate our framework experimentally by certifying, for the first time, robustness under general $\ell_p$-constrained poisoning adversaries under bagging with additive Laplace, Gaussian, and Uniform noises.

---


### 304. [Fed-MAPTrack: Federated Modality-aware Prompt Tuning for RGB-X Tracking](https://arxiv.org/abs/2610.34939)

**<font color=#1a73e8>作者：</font>** Xiangyu Liu, Yijie Shen, Yue Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-X tracking complements RGB appearance with thermal, depth, or event observations, but centralized training requires collecting multimodal videos at a single location. Federated training keeps raw videos local, but sensor heterogeneity can create a mismatch between parameter-sharing domains and the clients contributing to them. This mismatch is particularly relevant when RGB-only clients coexist with sensor-equipped clients: their RGB observations remain useful, but they provide no auxiliary measurements for learning sensor-dependent interactions. We propose Fed-MAPTrack, a modality-aware federated prompt tuning framework for RGB-X tracking. The pretrained tracking backbone and prediction head are frozen, and clients optimize and exchange only prompt-related parameters. The server aggregates RGB-shared parameters globally and maintains separate thermal, event, and depth banks for auxiliary-specific, fusion, and normalization parameters. Selective participation retains RGB-only clients' contributions to the global RGB bank while excluding their fusion and normalization updates from modality-specific aggregation. Across three matched training repetitions under a fixed client partition, Fed-MAPTrack improves the mean FedAvg scores by 2.35 AUC points on LasHeR, 3.45 SR points on VisEvent, and 2.11 F-score points on DepthTrack. Among the nine evaluated methods, it achieves the highest mean thermal AUC and depth F-score, while its mean event SR is 0.07 points below that of Independent FL. Controlled ablations show that extending the bucketing scope without a compatible participation rule can reduce performance. These results highlight the need to jointly define the sharing domain and eligible contributors for each parameter group.

---


### 305. [Stop or Clarify? Experience-Conditioned Active Fact Verification](https://arxiv.org/abs/2610.34941)

**<font color=#1a73e8>作者：</font>** Yuhang Dong, Jinghong Li, Xinyue Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fact-verification benchmarks score the final label, while an interactive verifier must first decide whether the available evidence is sufficient. We focus on that intermediate Stop-or-Clarify Decision. Uncertainty alone is insufficient, because the benefit of another evidence-acquisition step is unknown before the step is taken. Sequential Experience-Adaptive Clarification (SEAC) wraps a fixed verifier with a lightweight evidence-acquisition policy. For each claim, SEAC retrieves evidence, runs the verifier, forms a label-free decision state, and combines stop risk with an observational clarification-utility estimate from earlier executed trajectories. Clarification is requested only when this score exceeds the action cost and decision threshold. On SciFact, LIAR, and FEVER, SEAC improves mean accuracy and macro-F1 over the compared fact-verification and active-retrieval baselines. Equal-budget and formula-level diagnostics support selective clarification as a contributor to the gain, while the small SciFact split leaves its paired improvement inconclusive.

---


### 306. [Intellectual Property Protection of Hyperdimensional Computing Classifiers: Black-Box Ownership Verification via Model Watermarking](https://arxiv.org/abs/2610.34942)

**<font color=#1a73e8>作者：</font>** Hamed Poursiami, Farshad Soleiman, Ahmad Tahmasivand 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hyperdimensional computing (HDC) offers efficient learning and inference for resource-constrained systems, yet ownership verification of its models remains underexplored. We present the first systematic investigation of model watermarking in HDC by adapting backdoor-based embedding to three classifiers with different prototype-learning mechanisms. Across four benchmarks, with conventional neural networks as references, we examine whether watermarks can be learned without compromising task accuracy and whether they survive subsequent model modification and replication. The error-driven classifiers, AdaptHD and OnlineHD, support verification at a nominal trigger exposure of 1% with at most 0.58 percentage points of mean accuracy loss, whereas single-pass Vanilla HDC requires greater exposure and can incur substantial accuracy costs. The error-driven models retain verification under native continued training, but extraction produces surrogates that reproduce much of the task behavior without verifiable watermarks. Watermark overwriting readily embeds attacker watermarks into HDC prototypes and erodes the owner's watermark more strongly than in the neural network references, although the strongest erosion coincides with large accuracy losses. We further deploy watermarked AdaptHD on an FPGA and stress its execution through undervolting and overclocking. Verification survives substantial computation errors, whereas more severe stress either causes verification failure together with accuracy collapse or results in inference timeouts. These findings establish the feasibility of watermarking in HDC while identifying limitations in retention under extraction and sensitivity to overwriting.

---


### 307. [Relational Composition as Parallel Transport: What Per-Entity Frames Force in Attention](https://arxiv.org/abs/2610.34945)

**<font color=#1a73e8>作者：</font>** Aakash Sarkar, Ananya Mukherjee, Motoshige Sato  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A dot product means something only when both vectors share a coordinate system. Content words have one; a fresh entity does not: rotating its coordinates alone changes nothing. We take this per-entity frame freedom as a symmetry and ask what it forces in attention. For orthogonal transports, invariant scores depend only on norms and the transported inner product $\langle x_i,T_{ij}x_j\rangle$; equivariant messages lie in the span of $x_i$ and $T_{ij}x_j$. Endpoint channel count bounds transport rank, so with one vector per entity relations must be supplied; standard attention is the flat sector of a shared frame. Representation theory attaches an integer to each mechanism; the readout decides which. With orthogonal transitions, a convex-cell readout composes a finite group exactly only at or above its smallest faithful real representation dimension. At this minimum, exactness forces a faithful representation. An even readout can decode a cover at smaller width, and the gap is unbounded. Below its threshold, the part of the group a mechanism cannot see sets an accuracy ceiling computable before training. 17/17 fitting seeds at minimal width passed tests through length 1000, versus 7/18 at twice the width; 12 models carry correctness certificates to explicit lengths, from the weights alone. On $C_3\times A_4$ (faithful width 5), descent at width 4 learned the 72-state double cover under sign-blind attention (6/48 seeds; monotone 0/48); on a frozen cover the cross-entropy-optimal affine head is uniform, a quadratic head exact. On parsed CLUTRR, transported composition beats a matched transformer by 41 points at 4-10 hops, but forcing isometries costs 65 points; on StepGame's commutative algebra, isometries help. Static embeddings gave each word one vector; contextual models gave each occurrence its own; per-entity frames make each relation an operator, the unit in which relations compose.

---


### 308. [MINT: Mitigating Structural Inconsistency via Attentive Message Passing for Financial Anomaly Detection](https://arxiv.org/abs/2610.34950)

**<font color=#1a73e8>作者：</font>** Yin-Ju Wu, Bi-Cheng Yan, Berlin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Illicit account detection is a critical task for financial risk control systems, aiming to pinpoint malicious actors within transaction networks. Existing efforts typically recast transaction networks into directed multigraphs and leverage graph neural networks (GNNs) to detect anomalies via topological structures under the homophily assumption. However, directly grafting GNNs onto transaction graphs is faced with at least two pivotal challenges, i.e., structural inconsistency and label scarcity. The former arises from deceptive connections forged by malicious actors, while the latter stems from the lack of annotated data. In light of these, we introduce MINT, a novel graph neural framework that mitigates structural inconsistency via an attentive message-passing scheme on transaction graphs. Specifically, MINT introduces a discrepancy-aware feature propagation, which tracks malicious actors by quantifying deviations between nodes across bi-directional transaction flows. A transaction salience module is proposed to mitigate structural inconsistency by adaptively regularizing the interaction strength between nodes. Furthermore, to alleviate label scarcity, MINT is optimized via Positive-Unlabeled (PU) learning, which exploits only a minority of illicit nodes coupled with a majority of unlabeled ones. Extensive experiments conducted on three financial transaction benchmarks, including two large-scale public and one in-house real-world datasets, validate the superior effectiveness of MINT over several cutting-edge baselines.

---


### 309. [DimFlow: Bidirectional Grid-Expert Learning for Dynamic Gaussian Reconstruction](https://arxiv.org/abs/2610.34952)

**<font color=#1a73e8>作者：</font>** Gabriel Adineera, Jinoh Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic Gaussian reconstruction requires compact scene features to support coordinated changes in geometry and appearance. A factorized grid provides efficient local queries, but accurate interpolation alone does not ensure that the resulting dynamic attributes remain compatible across space and time. We introduce DimFlow, a framework that learns these features through bidirectional interaction between a multi-resolution grid and a coordinate-based expert branch. Feature-level adversarial alignment connects their distributions, adaptive fusion transfers complementary information, and activation-masked residual feedback refines the grid during training. Four attribute experts organize deformation, rotation, opacity, and temporal information before Gaussian rendering. In the aggregate comparison across D-NeRF, HyperNeRF, and DAVIS, DimFlow achieves 39.73 dB PSNR, improving on 4D-GS by 1.92 dB while matching its reported 85 FPS rendering speed. The model occupies 18.9 MB, compared with 18.3 MB for 4D-GS. Component and attribute-expert ablations reveal complementary contributions from feature alignment, adaptive exchange, and temporal processing.

---


### 310. [Decision Model Factory: Building Specialized Sovereign Decision Models](https://arxiv.org/abs/2610.34956)

**<font color=#1a73e8>作者：</font>** Yuma Ichikawa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision needs vary with each application, language, and deployment environment. The Decision Model Factory turns those needs into specialized, sovereign models on demand. A brief recipe guides the training, calibration, verification, and evaluation of a selected backbone, delivering a deployable decision model under the operator's control. The same workflow creates a new specialist whenever the requirements change. Across Japanese decision tasks, compact deployment, and long-context passage ranking, five factory-built models improve upon their backbones; three surpass the strongest results in a fixed public Japanese benchmark comparison. A dedicated runner computes only permitted-answer probabilities and reuses shared context, more than doubling serving speed on matched multi-question workloads with essentially unchanged decision scores. Together, the factory and runner make fast, task-specific decision models practical to build and deploy whenever needed.

---


### 311. [Beyond feature attribution: Recovering latent interaction structures in machine learning models via localized CBFI](https://arxiv.org/abs/2610.34962)

**<font color=#1a73e8>作者：</font>** Sejong Oh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Understanding individual predictions in complex tabular models remains challenging, as existing additive frameworks like SHAP and LIME often obscure structural logic by absorbing nonlinear interactions into individual feature scores. Exposing these latent interaction structures is essential for automated auditing in high-stakes environments where understanding the logic of model behavior is as essential as predictive accuracy. Methods: To address this limitation, we introduce the localized case-based feature importance (CBFI) framework. Unlike traditional numerical attribution, our method decomposes instance-specific predictions into structurally distinct components, effectively separating independent main effects (G1) from pure interactions (G4) to capture explicit feature synergies and provide a principled approach for diagnosing feature combinations. Results: Comprehensive experiments on wine quality classification and medical insurance regression demonstrate that localized CBFI successfully disentangles complex interactions hidden by additive models. Furthermore, fidelity tests and synthetic ground-truth benchmarks confirm that the identified interactions correspond precisely to the nonlinear structural dependency patterns embedded in complex architectures, including gradient boosting and deep neural networks, thereby successfully shifting the explainable AI paradigm from simple numerical attribution to the recovery of interaction-driven contributions.

---


### 312. [Guarded Agent-in-the-Loop Residual Adaptation for Evolving Wind Power Regimes](https://arxiv.org/abs/2610.34968)

**<font color=#1a73e8>作者：</font>** Yuhang Dong, Min Xia, Jinghong Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Wind power forecasting models are often deployed as fixed temporal backbones, but the errors they make can vary across meteorological regimes such as cold waves, heat-and-calm periods, productive typhoon, and destructive storms. We present a guarded Agent-in-the-loop residual adaptation framework that leaves the temporal backbone unchanged and adapts only a small set of scene-conditioned residual experts. An Agent layer interprets external scene information, identifies the current regime, selects residual experts, and applies a correction only when recent observed errors support it. New experts enter the pool after they outperform their initializations on a validation set, keeping model growth under explicit control. Backbone-only and Agent-enhanced forecasts are compared at lead times of 4, 8, 12, 24, and 48 across nine time-series backbones. Across these runs, the guarded framework lowers both MAE and RMSE for all 45 backbone-horizon combinations, with average MAE reductions ranging from 11.21% to 20.26% across backbones. Online-selection baselines, component ablations, and routing analyses identify the roles of residual experts, scene-aware routing, and the online acceptance rule. Candidate-scene runs evaluate the promotion path under controlled conditions; long-term unattended deployment was not evaluated.

---


### 313. [SVD-Attention: Efficiently Analyzing Attention Blocks in Transformers](https://arxiv.org/abs/2610.34971)

**<font color=#1a73e8>作者：</font>** Debopam Sanyal, Hongjie Chen, Riya Elizabeth Kuriyan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretrained transformers spend a large share of their inference compute inside self-attention, yet the per-head query-key interaction is structurally low-rank by construction. We ask a diagnostic question: across layers and architectures, which heads actually use the full rank budget on real data, and which do not? We propose SVD-Attention, a post-hoc method that decomposes the per-head interaction matrix $M_h$ and scores every singular mode by both its spectral magnitude and its activation variance across tokens on a small calibration set. The score keeps the modes the head can amplify and that real data actually activates, and discards the rest; the resulting factorization is exact for the retained modes and needs no finetuning. Across seven pretrained models and five task types, the diagnostic finds a task-dependent pattern: redundancy sits in the early to middle layers for sentiment and image classification and for generation, and in the late layers for dense prediction and extractive question answering. It is also predictive: truncating the layers it flags costs at most $1.75$ F1, while truncating the same number of layers elsewhere in the same model costs up to $50$ F1. SVD-Attention is an analysis tool rather than a compression method: acting on it reduces inference FLOPs by $0.8$-$1.5\%$ on its own and by $8$-$11\%$ when composed with weight pruning, with $0$-$4\%$ change in task quality.

---


### 314. [Sparse Recovery Bird's-Eye View Model Soup for Robust Camera-Based 3D Object Detection](https://arxiv.org/abs/2610.34976)

**<font color=#1a73e8>作者：</font>** Jinwoo Chung, Sangho An, Hyunsung Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based bird's-eye view (BEV) perception methods such as Fast-BEV have demonstrated promising results with fast inference speed and competitive accuracy. However, their robustness to real-world corruptions remains insufficiently explored, posing risks for autonomous driving deployment where environmental variations are inevitable. In this paper, we propose Sparse Recovery Bird's-Eye View Model Soup (SR-BEVS), a sparse recovery learning approach that simultaneously improves clean accuracy and corruption robustness without requiring additional data or architectural modifications. Our method identifies pruning candidates based on layer-wise weight magnitudes, applies random pruning to create diverse sparse models, and retrains each model with a randomly sampled learning rate. By averaging these diverse recovered models into a single dense model, we achieve enhanced robustness against various corruptions while introducing zero inference overhead. We further provide a mode connectivity analysis demonstrating that our pruning-based diversification preserves the connected low-loss basin necessary for stable weight averaging. Experiments on the nuScenes dataset demonstrate up to 33.8% improvement in corruption robustness and a 1.8% gain in clean accuracy over the Fast-BEV baseline, with consistent improvements across sensor noise, weather distortions, and illumination changes. Our simple yet effective approach may be applicable to other BEV models.

---


### 315. [More Memory, Better Videos? A Controlled Study of Visual Memory in Long-Video Generation](https://arxiv.org/abs/2610.35001)

**<font color=#1a73e8>作者：</font>** Yuzhuo Chen, Huafeng Shi, Xinyu Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video generators increasingly retrieve past visual observations to prevent identity drift. The intuition is compelling: more access to history should make future video more consistent. But an image can be faithful to the past and wrong for the present. Does visual memory always improve the generated story? We investigate this question through VMem-Bench, a two-track diagnostic study. Track-A measures which references are selected from 92 real films (16,548 segments), before generation and without generator confounds. Track-B compares four retrieval policies with no-memory and gold-informed last-seen controls on 30 causally generated stories (2,824 segments) using a shared generator. Retrieval increases entity recall from 0.559 to 0.628-0.693 and improves similarity to past appearances, but decreases precision from 0.977 to 0.915-0.938 and forbidden-entity avoidance from 0.968 to 0.845-0.898. It can also reinforce obsolete appearances after the story changes them. Conversely, high long-gap recall can arise without memory when the prompt itself supplies the appearance; an appearance-stripping analysis exposes this confound. These results distinguish historical fidelity from current-story correctness and show why retrieval relevance or final-video consistency alone does not establish memory utility.

---


### 316. [DUET4D: Self-Corrective Coupled Guidance for Sparse-View 4D Reconstruction](https://arxiv.org/abs/2610.35002)

**<font color=#1a73e8>作者：</font>** Beizhen Zhao, Nanjie Yao, Boyi Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view 4D reconstruction is highly under-constrained when only a few cameras are available. Generative priors can recover missing appearances, but video models are computationally impractical for iterative reconstruction, whereas single-view models produce temporally inconsistent pseudo-observations. Moreover, directly absorbing uncertain generative outputs into Gaussian optimization often creates redundant primitives and floating artifacts. To address these challenges, we propose DUET4D, a self-corrective coupled guidance framework for sparse-view 4D Gaussian splatting. The core of our approach is a self-corrective framework where the 4D representation guides generative prior for spatio-temporal consistent supervisions. We first construct sequential alignments from current Gaussian evidence to steer the latent restoration. Then we use Sequential Fidelity Resampling to lift generative supervisions into Gaussian space to selectively distinguish repeatedly supported primitives. The corrected representation then provides more reliable Gaussian evidence for the next restoration cycle. Extensive experiments demonstrate that DUET4D significantly improves rendering quality and rendering efficiency.

---


### 317. [Shifted Window Temporal Transformer for YOLO-Guided Phase Recognition in Laparoscopic Cholecystectomy Surgery](https://arxiv.org/abs/2610.35005)

**<font color=#1a73e8>作者：</font>** Sheekar Banerjee, Md. Shahabuddin, Md. Mahbub Hasan Akash 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intelligent operating rooms require accurate awareness of surgical workflow for better intra-operative decisions, teamwork, and surgical documentation. Therefore, accurately recognizing surgical phase during surgery is crucial. However, previous artificial intelligence-based methods provide fluctuating predictions for the transitions, restricting their clinical use. To address this challenge, we propose a clinically meaningful framework that integrates a Swin Transformer and Temporal Transformer Encoder (TTE) for effective surgical phase recognition and a parallel YOLOv11s network for real-time surgical instrument localization. To avoid phase flickering and to produce stable workflow predictions, a causal temporal smoothing is applied. The proposed framework is tested on the Cholec80 dataset for the simultaneous recognition of the surgical phases and instruments. The overall phase recognition accuracy of this model was 92%, and the macro average F1-score was 0.86. This performance surpasses CNN based methods such as EndoNet (81.7%) and SV-RCNet (85.3%), as well as temporal convolutional and transformer-based approaches including TeCNO (88.6%), Trans-SVNet (90.9%), and LoViT (91.5%). Besides, the module of instrument detection achieved mAP@0.5 = 0.863. The reliability of the results is confirmed, obtaining a high recognition rate of the workflows, and a high accuracy of the localization of the instruments. The proposed framework can serve as a foundation for intelligent surgical assistance, enriching situation awareness, and potential robotic surgery applications. Code will be made publicly available at: this https URL

---


### 318. [Zero-Shot Monocular Depth Estimation for Visual Perception in Lower-Limb Prostheses](https://arxiv.org/abs/2610.35018)

**<font color=#1a73e8>作者：</font>** Ishi Vijayvergiya, Marc Hölle, Youssef Dawoud 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation has advanced rapidly with the development of foundation models that demonstrate strong zero-shot generalisation across diverse visual domains. However, the applicability of these models to visual perception for lower-limb prosthetics remains largely unexplored. Reliable depth perception is particularly important for prosthesis users, who often experience significant challenges when navigating stairs, uneven terrain, and other complex environments. To address this gap, we introduce the Lower-Limb Prosthesis (LP) dataset, a benchmark designed to evaluate depth perception from an emulated knee-level prosthetic viewpoint. Using this dataset, we evaluate four state-of-the-art monocular depth estimation foundation models. Our results provide the first systematic benchmark of monocular depth estimation performance from a prosthetic viewpoint, while highlighting both the challenges and the potential of deploying foundation models in prosthetic perception systems. The code and dataset are available at this https URL.

---


### 319. [AutoPRL: Automated Path Representation Learning via a Learnable View Generator](https://arxiv.org/abs/2610.35032)

**<font color=#1a73e8>作者：</font>** Sean Bin Yang, Ying Sun, Yunyao CHeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning has emerged as a powerful paradigm for Path Representation Learning (PRL) in road networks. PRL aims to learn informative representations of paths traversed by moving objects, such as vehicles, where each path consists of a sequence of connected road segments. These representations are essential for various downstream tasks, including travel-time estimation and path ranking. However, existing methods often suffer from ineffective view generation and inefficient training procedures due to their reliance on heuristic augmentations and computationally intensive contrastive learning. To address these issues, we propose AutoPRL, an effective and efficient self-supervised PRL framework that integrates three key components. The Automatic Data Augmentation (AutoDA) module employs variational autoencoders to generate semantically meaningful and diverse feature-level path views by modeling each topology-aware node embedding with a Gaussian latent distribution, thereby mitigating information loss and enhancing representation quality. Second, the Cross-View Decoupled Contrastive (CVDC) learning mechanism improves training efficiency by disentangling the optimization of positive and negative pairs across node- and path-level views, enabling more stable contrastive learning. Third, an Adaptive Co-Training (ACT) module dynamically adjusts uncertainty-based loss weights to balance multiple objectives, ensuring efficient and scalable training. Extensive experiments on three real-world datasets demonstrate that AutoPRL achieves strong and consistent performance in both effectiveness and efficiency across multiple downstream tasks.

---


### 320. [Mapping the Solution-Set Structure of Grokking on Latin Squares](https://arxiv.org/abs/2610.35036)

**<font color=#1a73e8>作者：</font>** Zihan Gu, Lulu Zhao, Tianyi Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking is a delayed transition from memorisation to generalisation. A network first fits observed examples while remaining near chance on held-out inputs, then generalises abruptly. Prior work has focused mainly on this delay, finding that the network's main loss becomes weight decay after the fitting phase. We name the solution to this optimization problem as the minimum-norm endpoint, and study which tasks make all minimum-norm endpoints generalise from partial observations. Specifically, we model pairwise input tasks as edge colourings of $K_{q,q}$, with Latin colourings as our structured family, and classify each observed instance as all-good, mixed, or no-good by its endpoint set. Furthermore, we prove two contrasting results: (1) Finite-abelian-group families are asymptotically all-good from partial observations; (2) Under a uniform random Latin square, all-good tasks become asymptotically rare for observation-based learners, leaving mixed or no-good behaviour. Moreover, experiments show that relabellings of addition generalise despite their dense polynomial representations. Finally, on tasks of composite order, finite-training results suggest that predictors learn a coarse part of the output before the full label.

---


### 321. [Revealing Imaging Characteristics of Thermal Wakes from Underwater Vehicles Without Cooling-Water Discharge](https://arxiv.org/abs/2610.35038)

**<font color=#1a73e8>作者：</font>** Guoyi Zhang, Yanjin Du, Guangsheng Xu 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small uncrewed underwater vehicles are proliferating and threaten maritime security, yet evade sonar and magnetic sensors built for larger submarines. Infrared thermal wakes, generated by hydrodynamic displacement that modulates the cold-skin layer, offer a non-acoustic, non-magnetic alternative even without cooling-water discharge. Existing studies, however, rely on idealized simulations that fail to capture real-world backgrounds, offering limited guidance for target-background discrimination. We establish AVP-IR-Wake, the first large-scale, real-world, physically diverse benchmark of 161,485 frames collected over three years. We show that thermal wakes are extended structures of discrete vortices, violating the compactness assumption of conventional targets. We reveal local indistinguishability: individual wake vortices are statistically identical to wind-induced background vortices in temporal, frequency, and sparse domains, sharing low-frequency information and long-range correlations. This challenges the assumptions of compact, transient, high-frequency targets in conventional detection. Yet we establish global morphological separability: although locally inseparable, the wake as a whole is organized by vehicle trajectory, whereas background clutter is organized by wind-driven thermal fronts. This explains why representative detectors fail and shows that reliable detection must shift from local feature extraction to global trajectory-constrained physical modeling. Because the cold-skin layer varies globally and seasonally, forecasting wake observability will require integrating physical oceanography and atmospheric science, linking underwater surveillance to the changing ocean surface.

---


### 322. [DriveUniTok: A Unified Multimodal Tokenizer for Driving World-Action Models](https://arxiv.org/abs/2610.35044)

**<font color=#1a73e8>作者：</font>** Jingbo Xu, Hanchao Leng, JiaHui Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models are emerging as a fundamental component of policy learning for real-world agents, enabling agents to predict future world states and plan actions within a learned representation of the dynamic environment. Existing approaches, however, often model appearance, metric geometry represented by projected LiDAR depth, and ego motion either partially or independently, overlooking the fact that these modalities are different projections of a shared underlying world state. This separation can lead to information loss and cross-modal inconsistency, ultimately limiting downstream performance. Motivated by this unified view of the world, we propose DriveUniTok, a unified multimodal tokenizer for driving world-action models (WAMs) that encodes these modalities in a single decodable continuous latent. We freeze DriveUniTok and adapt a pretrained diffusion model, DriveUniWAM, to predict future unified latents; the tokenizer then decodes them into future appearance, projected LiDAR depth, and ego trajectories. Experiments on NAVSIM demonstrate that our unified design achieves better future prediction and planning performance at lower downstream computational cost than separate-stream alternatives. With reinforcement learning post-training, DriveUniWAM achieves a PDMS of 91.54, reaching state-of-the-art performance among the evaluated WAM-based planners.

---


### 323. [Risk-Aware Output Control Should be the Focus of Machine Unlearning](https://arxiv.org/abs/2610.35052)

**<font color=#1a73e8>作者：</font>** Yahya Alkhatib, Yuyang Xiao, Wee Peng Tay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Well-documented failure modes of machine learning (ML) systems, including bias, toxicity, hallucination, and leakage of sensitive information, has driven the rise of machine unlearning (MU). Most existing work, however, targets parameter-space indistinguishability, seeking unlearned models that are as close as possible to models retrained from scratch on retained data. In this paper, we argue that this objective is misaligned with practical and user-relevant concerns: MU should prioritize statistically guaranteed output-space control rather than parameter-space similarity. We contend that output control with statistical guarantees is the operationally meaningful notion of unlearning, as it supports rigorous and robust objectives, scales to modern deployment settings, and enables interpretable guarantees. We substantiate this position with empirical evidence and with recent theoretical results that, although not originally formulated in this framing, are consistent with it.

---


### 324. [Kronecker-Structured Video Completion with Cross-Fitted Self-Supervised Residual Learning](https://arxiv.org/abs/2610.35065)

**<font color=#1a73e8>作者：</font>** Qi Qi, Yanfei Wang, Yanjun Cui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tube-wise video completion reconstructs temporal trajectories at spatial locations unobserved in every frame. We propose a two-stage framework combining regularized masked Kronecker product decomposition (KPD) with cross-fitted self-supervised residual learning. First, we estimate a compact structural backbone directly from observed entries using cyclic component-wise least-squares updates, spatial and temporal factor regularization, and regularizer-optimal scale balancing. The exact updates yield a nonincreasing objective. Second, we address the mismatch between in-sample fitting errors and the prediction errors encountered at missing tubes. We partition observed tubes into folds and construct residual targets using backbone models fitted without the corresponding target tubes. A lightweight 3-D convolutional neural network then predicts corrections from the backbone, visible residual context, observation mask, and local detail features. Exact data consistency preserves observed measurements. Experiments include ablations, sensitivity analysis, grayscale and RGB video completion, and structured missing patterns. Our method achieves the highest mean PSNR and SSIM at the higher tested sampling rates on the grayscale benchmark. On eight selected DAVIS RGB sequences, it achieves the highest mean missing-region PSNR and full-frame SSIM and the lowest mean missing-tube temporal-gradient MAE at every evaluated sampling rate.

---


### 325. [A Diagnostic Protocol for GNNs in Electricity Load Forecasting: Separating Parameter Sharing from Neighborhood Access](https://arxiv.org/abs/2610.35074)

**<font color=#1a73e8>作者：</font>** Eloi Campagne, Yvenn Amara-Ouali, Yannig Goude 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A graph neural network (GNN) forecasting a collection of load series combines two mechanisms, sharing parameters across series and reading neighboring series, and a gain over a non-graph model may come from either; telling them apart decides whether a graph is worth maintaining. We propose a model diagnostic protocol that compares the GNN with three reference models: a per-node network, a network shared across nodes without neighbors, and the same GNN without edges. Degree-preserving rewiring tests whether neighbor identity matters. After a tuned benchmark on regional load in France and on low-voltage feeders in the UK, we apply the protocol to deliberately short node histories, as when non-stationary demand leaves only recent observations relevant: the feeders, within one week, and a public dataset of client consumption series. On the feeders, sharing parameters recovers most of the error gap between node-specific models and GNNs, about two thirds against a regularized one. Adding the edges to an otherwise identical backbone brings a smaller gain, half or more of which disappears under rewiring. On the client series, the neighbor mean degrades the per-node model on the shorter window and the edges' gain is not consistently distinguishable from zero; on the regions of France, where each node's own history is already informative, the ranking between per-node models and GNNs changes with tuning. A synthetic study points to noisy local measurements as one regime where neighbors help. In an exploratory online aggregation, graph and non-graph forecasters appear complementary, and the weight assigned to GNNs is not proportional to their contribution. In none of the three datasets do the edges account for most of a GNN's advantage over node-specific models, so a forecasting gain should be credited to the graph only after comparison with per-node and shared references.

---


### 326. [Blendshape Generation for Models with Disconnected Parts: Adding ARKit/MediaPipe Blendshapes to Anime-Style Character Models](https://arxiv.org/abs/2610.35076)

**<font color=#1a73e8>作者：</font>** Pramook Khungurn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blendshape generation for 3D models has been extensively researched, but very few works address generating blendshapes for models with multiple disconnected parts. We present a case study of generating fixed facial expression blendshapes for commercial anime-style 3D character models with up to 11 parts per face. To make sure that our system can handle models in a way that is agnostic to topology, we train neural networks to generate deformation fields around the input meshes. We employ at least one network to independently process each part, and the relative positions of their outputs are coordinated by having each network also process the geometry of an anchor part. We use two mechanisms to improve accuracy: having the networks predict whether the output displacement is zero or not, and classifying blendshapes into different size groups and dedicating a network to each group. We also introduce a method to improve blendshape quality by enhancing bilateral symmetry. Our method is simpler than recent neural-network-based works and solves a real problem of the user community of these models.

---


### 327. [A JiT-Based Denoising Defense Method Against Adversarial Examples for Radio Signal Automatic Modulation Classification](https://arxiv.org/abs/2610.35084)

**<font color=#1a73e8>作者：</font>** Shiwei Liu, Linyuan Wang, Nuolin Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic modulation classification (AMC) of radio signals is a core technology for spectrum monitoring and electromagnetic situational awareness. Deep neural networks (DNNs) play an important role in this field owing to their powerful feature extraction capabilities and end-to-end learning paradigm. However, their vulnerability to adversarial attacks poses serious security challenges to practical deployment. Adversarial training, a common defense, has limitations including poor generalization across attack types and high training costs. Inspired by Just image Transformers (JiT), a diffusion generative model that directly predicts clean images, this paper proposes a JiT-based denoising defense against adversarial examples for radio signal modulation classification. During training, a signal-specific 1D Transformer denoising network is optimized via flow matching to directly predict clean signal samples. It thereby learns a mapping that projects arbitrary examples back onto the low-dimensional manifold of clean signal examples. During inference, arbitrary examples are fed into the trained network and directly projected onto this manifold. This enables denoising defense without prior knowledge of attacks. Experiments on the RML2018.01A dataset were conducted without attack information, using a single empirically selected, fixed denoising start time. Compared with PGD-based adversarial training, the proposed method achieves a relative improvement of at least 20.58% in robust accuracy under PGD attacks. It also achieves a relative improvement of 10.20% in classification accuracy on clean examples. When evaluated against attack types unseen during adversarial training, the proposed method provides stronger defense than adversarial training. In particular, at higher attack strengths, it achieves a relative improvement of at least 39.72% in robust accuracy.

---


### 328. [Reading the Registers of Honorius III without Manual Line Transcription: Forced-Aligned HTR, End to End, Modular or Hybrid](https://arxiv.org/abs/2610.35085)

**<font color=#1a73e8>作者：</font>** Tamas Kovacs, Daniel Luger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unlocking medieval archives at scale is bottlenecked by the cost of line-level diplomatic transcriptions and manual abbreviation expansion. Focusing on the registers of Pope Honorius III (1216-1227) over 5,000 letters surviving in full only as manuscript images - we show that existing, line-break-free expert transcriptions (edition drafts) suffice to train end-to-end hand-written text recognition (HTR) that jointly transcribes and expands heavily abbreviated Latin. Using forced alignment on 860 unaligned edition entries across 394 pages of Reg. Vat. 9, we automatically bootstrap 13,122 training lines without manual alignment of segmented lines. While the generic CATMuS baseline struggles on this domain (18.9% CER) and a modular space-free HTR + word-segmentation pipeline (cf. Camps et al. 2021) plateaus at 15.6% WER, our from-scratch hybrid Conformer - combining CTC with bidirectional subword attention decoders, iterative self-realignment and n-best LM rescoring - achieves 4.7% CER and 8.7% WER (8.4% WER with ROVER system combination), nearly halving errors on clause-final words (22.7% to 12.2% WER). These figures are measured on the test lines that align with the transcription (86% of all test lines for the best hybrid). Furthermore, we address a tension between paleographic fidelity and editorial normalization: training on targets that preserve scribal name initials reduces the WER against the manuscript text on the 31 affected test lines from 13.3% to 9.2%, at a small cost against the expanded transcription (WER +0.3 points, CER +0.4). Finally, extensive ablations show that none of an auxiliary diplomatic CTC head, a copy mechanism, a permutation decoder or masked-image pretraining improves on direct end-to-end supervision, while strict padding-mask propagation and per-line beam termination make inference batch-invariant.

---


### 329. [Test-Time Prompt-Agnostic Decomposition](https://arxiv.org/abs/2610.35090)

**<font color=#1a73e8>作者：</font>** Junze Wang, Lei Fan, Dezheng Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-Time Prompt Tuning (TPT) adapts large pretrained models to unseen target distribution shifts by updating only lightweight prompt tokens. Existing TPT methods are effective, but they mainly optimize each prompt update locally. Across test-time steps, prompts updated at the current step are reused for the corresponding predictions and updates, so noisy or biased unlabeled objectives can accumulate and destabilize the prompt-update trajectory. We identify two failure modes: magnitude expansion, where updates move the prompt too far, and directional drift, where consecutive updates point in inconsistent directions. To analyze and control these failures, we propose Test-Time Prompt-Agnostic Decomposition ($\mathtt{TPD}$), which characterizes observed prompt-update trajectories from a dynamical-systems view and decomposes base prompt updates into magnitude and direction. $\mathtt{TPD}$ computes a spectral radius to measure update expansion and decomposes update directions into persistent, oscillatory, and residual components. Building on this decomposition, Adaptive Koopman Control ($\mathtt{AKC}$) regulates update magnitude by shrinking updates under expansive recent dynamics, while Hankel Update Router ($\mathtt{HUR}$) refines update direction by preserving persistent components and suppressing oscillatory and residual components. Together, $\mathtt{AKC}$ and $\mathtt{HUR}$ produce a stabilized prompt update. As a prompt-agnostic framework, $\mathtt{TPD}$ can be plugged into visual and text TPT methods without modifying the backbone, prompt architecture, or adaptation loss. Experiments on 15 datasets show that $\mathtt{TPD}$ consistently improves 10 baselines, with accuracy gains of $3$--$8\%$ for visual prompts and over $2\%$ for text prompts.

---


### 330. [Uncertainty Evaluation to Support Safety of the Intended Functionality Analysis for Determining the Applicability of Performance Targets Across Triggering Conditions in ML-Based LiDAR Object Detection](https://arxiv.org/abs/2610.35092)

**<font color=#1a73e8>作者：</font>** Milin Patel, Rolf Jung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For safety of the intended functionality (SOTIF) analysis according to ISO 21448, a machine learning object detector for light detection and ranging (LiDAR) point clouds can meet a performance target, a limit on the mean per-frame share of wrong detections among accepted detections, by rejecting detections above an uncertainty threshold. A threshold selected on data of one condition carries a statistical guarantee only for data distributed like its selection data, whereas SOTIF analysis covers every triggering condition. This paper presents an uncertainty evaluation in which the threshold is transferred into a triggering condition, a test decides at a stated error probability whether the target is applicable there, not applicable or not determined, and a lower bound counts the independent units an applicable outcome requires. For PointPillars ensembles on KITTI and nuScenes, counted in recorded sequences, as the dependence between frames requires, neither dataset held enough independent units for any target limit, and no transfer had a not applicable outcome. Counted in frames, the same data gave not applicable outcomes at limits fixed in advance after transfers into far distance, into rain and between two separately trained detectors, thresholds that met the target limit after a transfer rejected most correct detections, and in rain the area under the receiver operating characteristic curve did not decrease. A performance target met under one condition therefore counts as evidence under a triggering condition only after a test there, reported with its share of accepted correct detections and its number of independent recorded sequences.

---


### 331. [FlowGenesis: Representation-Driven Self-Organization of Neural Architectures](https://arxiv.org/abs/2610.35108)

**<font color=#1a73e8>作者：</font>** Maksim A Kazanskii  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks typically rely on architectures specified before training, despite the continuous evolution of their internal representations. We introduce FlowGenesis, a framework in which neural architectures adapt through neuron birth and pruning guided by Representation Flux, a local statistic capturing changes in minibatch mean activations. Neurons exhibiting persistently high Flux undergo splitting designed to approximately preserve the network function, while neurons with low Flux and low activity are pruned. This mechanism allows network capacity to evolve without prescribing a target architecture or performing a separate architecture search. Experiments on image and text classi- fication show that networks initialized with different sizes approach similar final neuron-count ranges within each dataset while maintaining comparable predictive performance. We further extend FlowGenesis to continual learning, where representation-guided structural adaptation reduces the neurons and parameters allocated to successive tasks while maintaining accuracy comparable to fixed-width Progressive Neural Networks in a task-incremental learning setting. These findings demonstrate that neural architectures can adapt through feedback between representation learning and structural change, suggesting an alternative to prescribing network capacity before training.

---


### 332. [Understanding and Repairing Cooperative Perception under Adverse Weather](https://arxiv.org/abs/2610.35110)

**<font color=#1a73e8>作者：</font>** Mengxu Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A cooperative 3D detector can miss a vehicle even when the LiDAR points on it remain unchanged. We study this failure under adverse weather as Weather-Induced Context Interference. To our knowledge, this is the first controlled study of how weather-related exterior changes remove cooperative benefits while preserving all points inside annotated objects. Controlled experiments on simulated and real roadside inputs show that exterior loss changes object representations before fusion and removes previously useful assistance. On real inputs, restoring object-neighborhood features recovers 30 of 31 induced failures; three equal-area exterior controls recover none. The failure condition also appears with a second fusion model. These findings motivate Adverse-Weather Cooperative Repair (AWCR), with separate implementations for the available supervision. Point Classifier filters added weather returns in simulation. On real inputs, Local Correction refines candidates and Quality Selection checks them against current measurements, without naturally paired clear/adverse-weather recordings. Candidate tracing shows that correction supplies accurate geometry for some targets that original candidates cannot localize at the evaluation threshold. On natural adverse-weather CoInfra development data, AWCR improves car bird's-eye-view (BEV) AP@0.7 by 4.66 points with V2X-ViT and 5.56 with AttFuse. On simulated V2X-R fog, it improves vehicle BEV AP@0.7 by 4.47 points at a fixed 4,096-candidate budget.

---


### 333. [Subspace Crystallization in Grokking: Rank Compression Tracks the Phase Transition](https://arxiv.org/abs/2610.35112)

**<font color=#1a73e8>作者：</font>** Shlok Mehendale, Paras Chopra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking describes understanding something deeply and intuitively. In neural networks, it is the phenomenon where a network generalizes long after memorizing its training data. This delay has been linked to a fall in the effective rank of the network's weight matrices, but whether this rank compression drives grokking or follows it is still unresolved. We study a mean-field MLP and a one-layer transformer trained on modular arithmetic and observe that: (i) Compression follows the onset, not memorization. Every transformer memorizes its training data within 250 steps, while the grokking onset (the first step at which test accuracy reaches 95%) varies from 6,500 to 21,000 steps. The steepest fall in effective rank comes about 900 steps after the onset, however late the onset occurs, and networks that memorize without grokking compress far less. (ii) Subspace crystallization. We call the span of the fewest top singular directions of a weight matrix that preserve 99% of test accuracy its sufficient subspace. Its size can shrink as the margin between the correct and the best wrong output grows, so we also count the directions needed to keep the outputs within 10%. In the transformer, this count falls during the transition from a quarter or more of the available directions to about a tenth, which we call subspace crystallization. (iii) Imposing low rank does not speed up grokking. Against a factorized full-rank control, capping the rank of the transformer's MLP input weights delays the onset, and capping the rank of its embedding stops 15 of 20 runs from grokking. Compression is therefore a signature of grokking rather than its cause.

---


### 334. [Quality over Quantity: Rethinking Data and Model Assumptions for Bengali Coreference Resolution](https://arxiv.org/abs/2610.35114)

**<font color=#1a73e8>作者：</font>** Zenith Biswas, Andrew Thomas Dyer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual transformer models are often assumed to generalise across languages, but their effectiveness for coreference resolution in low-resource settings remains unverified. We investigate this gap in Bengali, a language with over 250 million speakers but limited annotated coreference resources. We evaluate transformer-based pre-trained encoders under multiple settings, including zero-shot, fine-tuning, data augmentation, and cross-lingual transfer. Our results challenge several common assumptions about model generalisation and data efficiency in low-resource NLP. We demonstrate that a small amount of high-quality annotated data significantly outperforms larger mixed-quality datasets (p < 0.01). We find that data augmentation, particularly back-translation, does not improve performance and can degrade results in coreference resolution. Cross-lingual transfer is also inconsistent: transfer from a distant language like English reduces performance, and transfer from the related language Hindi provides no consistent benefit across models. Several widely used multilingual models exhibit collapsed embedding spaces, rendering them unsuitable for similarity-based clustering tasks. These findings highlight the importance of annotation quality over data quantity and provide empirical guidance for developing coreference resolution systems in low-resource languages.

---


### 335. [When Fusion Order Matters: Insights on Progressive Multimodal Representation Learning for Cross-modal Retrieval](https://arxiv.org/abs/2610.35125)

**<font color=#1a73e8>作者：</font>** Haoxiang Zhao, Bin Wang, Yaofei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal video retrieval combines visual, acoustic, and speech information, yet how their fusion order should depend on the data and the retrieval query remains unclear. We introduce Unified Progressive Representation Learning for Order Analysis, or UniPRO, to investigate this question through configurable fusion schedules with matched model components and training settings. Starting from text-to-video retrieval, we find that the tested one-by-one schedules outperform stacked fusion, while changing the order within one-by-one fusion also changes performance. To guide order selection, we examine two complementary considerations: learning difficulty under unequal modality availability and preservation of information relevant to the query. Complete-modality controls show that missing inputs alone cannot explain order sensitivity. At R@1, text and audio retrieval favor schedules that introduce the modality matching the query last. Controlled speech missingness during training and testing reverses the preferred order in both R@1 and SumR, with different crossover points. These findings motivate balancing the two considerations when selecting a fusion path. We then use them to predict a visual-last schedule for image queries, which achieves 97.9 R@1, the highest among the evaluated orders on MSR-VTT-9k. Main experiments on four text-to-video benchmarks establish the effectiveness of UniPRO, with component ablations assessing its supporting design. Together, the results identify fusion order as a task-dependent choice that should account jointly for modality availability and the retrieval query.

---


### 336. [STeP-TS: Shared Temporal Filters with Pruning for Time Series](https://arxiv.org/abs/2610.35128)

**<font color=#1a73e8>作者：</font>** Hanne Raum, Jasper Hoffmann, Joschka Boedecker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series forecasting requires capturing temporal dependencies across multiple scales while accounting for both shared and variable-specific dynamics. Compact forecasting models have emerged as an attractive alternative to increasingly large architectures, but preserving strong predictive performance within tight computational and memory budgets remains challenging. We propose a compact one-layer convolutional framework that learns a shared bank of multi-scale temporal filters of each variable. Lightweight variable-specific scalar weights determine the contribution of each temporal component, enabling the model to capture shared temporal structure while adapting to variable-specific dynamics. The learned weights and filter-output energy further provide a natural signal for structured pruning of convolutional filters, reducing computational complexity with minimal degradation in forecasting performance. We additionally introduce an amplitude-adaptive normalization mechanism that preserves variable-dependent temporal amplitudes. Experiments on multiple datasets demonstrate forecasting performance competitive with state-of-the-art methods while requiring substantially fewer parameters and inference FLOPs and achieving low per-sample latency.

---


### 337. [Domain-Adapted Latent Diffusion Models for CT-to-PET Image Translation](https://arxiv.org/abs/2610.35132)

**<font color=#1a73e8>作者：</font>** Yann Bourdé, Lea Bogensperger, Arnela Hadzic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Positron Emission Tomography (PET) provides important metabolic information for tumor detection and staging but remains significantly less accessible than Computed Tomography (CT) due to its high cost, infrastructure requirements, and reliance on injected radioactive tracers. CT-to-PET image translation using generative models aims to address this disparity, yet state-of-the-art diffusion-based methods are limited by the scarcity of paired training data. To overcome this, we propose a domain-adapted latent diffusion framework that transfers natural-image priors using a relatively small dataset of 21,930 paired CT/PET slices, incorporating a signed power transform to resolve extreme intensity sparsity in PET data. Compared to CPDM, a state-ofthe-art baseline for CT-to-PET image translation, our approach yields superior performance in pixel-wise reconstruction and localized tumor fidelity, demonstrating effective transfer of natural-image priors to the medical domain. We further provide a systematic analysis of evaluation metric reliability for sparse PET data, showing that standard full-image metrics can be misleading indicators of translated image quality, and propose background-filtered and mask-restricted metrics as more clinically meaningful alternatives.

---


### 338. [Sexual dimorphism and sex-specific features of pediatric hand bone shapes via statistical shape modeling](https://arxiv.org/abs/2610.35143)

**<font color=#1a73e8>作者：</font>** Edwin Tay, Amir A. Zadpoor, Nazli Tümer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding the envelope of shape variation encompassing both sexual dimorphism and growth-related changes in living tissue is a non-trivial task. In this work, we use statistical shape models (SSMs) and analyze demographic-stratified shape parameters to quantify sexual dimorphism and sex-specific shape changes. To this end, we developed a two-stage detection-segmentation framework that accurately segmented $n = 27664$ unique bone masks from a radiographic dataset of $n = 1456$ subjects with diverse ages and sexes (HD95 = $1.512 \pm 0.005$, ASSD $0.449 \pm 001$, Dice = $0.987 \pm 0.00004$, IoU = $0.975 \pm 0.0001$). Following SSM fitting, our follow-up analyses of stratified shape parameters highlighted the morphology of sexual dimorphisms for each bone and demonstrated sex-specific differences in shape development. Our results were consistent with existing literature and provided an unambiguous, data-driven methodology for characterizing tissue shape and its population-scale variation. This approach provides a potential methodological foundation for developing population-based models of anatomical variation and could be extended to investigate tissue growth and shape changes over time. Future work should evaluate the applicability of this methodology on alternative anatomical structures and imaging modalities, with the goal of validating these growth trajectories on longitudinal data.

---


### 339. [Locked In: Multi-Objective RL for the AI Data Center Build-Out](https://arxiv.org/abs/2610.35147)

**<font color=#1a73e8>作者：</font>** Satyapragnya Kar, Rajarshi Das, PR Panigrahi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI data center build-out is a multi-trillion-dollar, multi-decade infrastructure program. Yet siting, power procurement, and cooling decisions are still made with static, single-point scoring tools. These tools are evaluated once, on day-zero numbers. This is a poor fit. A site's water, power, and carbon profile drifts substantially over the 10 to 20 year asset life. The governing decisions are also irreversible, and they bind capital and physical plant for years. We formalize long-horizon build-out as a tiered multi-objective Markov decision process. Strategic commitments are gated to discrete windows, incur switching costs, and energize only after source-dependent lead times. Operational dispatch is restricted to capacity that physically exists. We solve the problem with a preference-conditioned multi-objective agent that has a semi-Markov manager and worker hierarchy. The agent recovers a family of policies that a planner can steer across cost, carbon, water, and reliability at inference time. We validate long-horizon dynamics with a lightweight counterfactual rollout model. Across three commitment regimes (irreversible, reversible, and commit-once) on real site data, preference conditioning yields a confirmed, steerable trade-off on both objective pairs in every regime. Imposing lock-in produces a more evenly covered frontier and a far more consistent rate of anticipatory retrofit ahead of a binding water-stress constraint than a freely reversible formulation. Finally, a compact counterfactual dynamics model tracks slow-moving state well. It is measurably outperformed by simple persistence on the water-stress axis. We report this limitation rather than obscure it. We release the environment, agents, baselines, and evaluation harness. All of them are grounded in real interconnection-queue, water-stress, and grid-emissions data.

---


### 340. [Temporal Slice Learning for AI-Generated Video Detection with 400$\times$ Fewer FLOPs](https://arxiv.org/abs/2610.35148)

**<font color=#1a73e8>作者：</font>** Wei Shang, Zhiyuan Li, Shengfeng He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative video models have improved visual realism, making detection increasingly dependent on subtle temporal inconsistencies. However, these signals are weak and spatially localized, while most of the video content is redundant. This creates a fundamental mismatch: existing detectors rely on heavy backbones to model full videos, which leads to high computational cost and limited scalability. In this work, we rethink AI-generated video detection from a representation perspective. Instead of modeling entire videos, we restructure them into compact temporal slice representations that isolate informative temporal evolution. We introduce a lightweight framework using frequency-aware temporal slice consistency learning, where informative spatial rows and columns are aggregated over time to form slice-domain inputs. This reparameterization suppresses redundant appearance while preserving discriminative temporal dynamics, enabling efficient and targeted detection. By constructing slices from both high- and low-frequency regions, our method exposes complementary temporal artifacts, including unstable details and abnormal motion smoothness. We instantiate this idea in a Temporal Slice Consistency Network, which integrates task-driven slice localization, hierarchical positional encoding, and a lightweight Transformer to model cross-slice and cross-frequency dependencies. We further introduce AI-Artist, a new benchmark with artist-curated videos from recent high-fidelity generators, including Seedance and Kling. Experiments on GenVideo and AI-Artist show that our method achieves strong performance while requiring over 400$\times$ fewer model-forward FLOPs and 3.6$\times$ faster model inference than the strong video-based baseline ReStraV (2.9$\times$ faster end to end, including preprocessing), enabling scalable and practical deployment.

---


### 341. [Complexity-guided Regularization for Generalizable Human Gaussian Splatting](https://arxiv.org/abs/2610.35152)

**<font color=#1a73e8>作者：</font>** Gun Ryu, Gi-Mun Um, Won-Sik Cheong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent studies on generalizable human Gaussian splatting have achieved the notable progress in synthesizing novel views of unseen human subjects from multi-view images. Despite this progress, existing methods still struggle to represent fine-grained details of human subjects, which inherently involve high geometric and textural complexity. This is because previous methods do not impose a constraint on how densely Gaussians are placed, which often leads to blurry rendering results in complex regions. To address this problem, we propose a complexity-guided regularization scheme. The key idea is to leverage a complexity prior computed via the local entropy in geometric and textural characteristics of a clothed human. This effectively prevents Gaussians from being coarsely placed in complex regions, which facilitates the faithful reconstruction of intricate structures. Furthermore, we sample local patches predominantly from complex regions according to this complexity prior, which allows the model to be sufficiently supervised by local details. Experimental results on benchmark datasets demonstrate that our method delivers state-of-the-art performance while maintaining the real-time inference speed in generalizable human Gaussian splatting. The code and model are publicly available at this https URL.

---


### 342. [Accelerating SO(2)-Equivariant Materials Models through Low-Precision Emulation](https://arxiv.org/abs/2610.35164)

**<font color=#1a73e8>作者：</font>** Denghui Lu, Alexander Maeder, Alexandros Nikolaos Ziogas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rotationally equivariant architectures improve the physical fidelity of machine-learned (ML) universal materials models based on graph neural networks (GNNs). However, their scalability is limited by the use of non-trivial, high-precision tensor operations during both training and inference. Adopting the reduced-precision formats of matrix multiplication units (MMUs), e.g., FP8 instead of FP32, provides massive increases in throughput, up to 30x (60x) on NVIDIA Hopper (Blackwell) GPUs, but may lead to drastic loss of accuracy. Here, we introduce tailored 'emulated' low-precision operations under the integer Ozaki scheme to accelerate the 'SO(2)-equivariant' processing layers of GNNs, which dominate the runtime of (1) many state-of-the-art ML interatomic potentials (MLIPs) and (2) most universal ML Hamiltonian (MLH) models. Our framework, FlashSO(2), outperforms TF32, the most accurate native low-precision MMU format, in throughput, accuracy, and memory footprint at once. At the SO(2) layer level, it reaches 40x (7x) the throughput of MALOQ's (UMA's) reference implementation, an MLH (MLIP) model, sustaining up to 236 (232) effective Tflop/s on an NVIDIA GH200, 3.5x the FP32 peak. At the model level, FlashSO(2) helps train MALOQ 3.9x faster than its pure-FP32 version while reducing peak memory by 58% at no loss in accuracy. In molecular dynamics simulations with UMA, the speedup factor is 3.3x, and the peak memory is reduced by 51%. FlashSO(2) thus pushes the speed-accuracy Pareto frontier of equivariant materials models beyond the native low-precision formats and substantially lowers the resources required to exploit their scaling laws.

---


### 343. [Biology-Guided Context-Aware Residual Propagation for Spatial Gene Expression Prediction from Histology](https://arxiv.org/abs/2610.35167)

**<font color=#1a73e8>作者：</font>** Vu Van An, Long D. Nguyen, Ho Viet Duc Luong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics provides spatially resolved molecular profiling, but its cost, limited throughput and experimental complexity hinder routine large-scale use. Predicting spatial gene expression from hematoxylin-and-eosin-stained histology images offers a scalable alternative, yet remains challenging because histology provides only an indirect morphological view of molecular activity. Existing methods typically decode expression from visual features in a single stage, even when enhanced with spatial aggregation, retrieval or multi-resolution fusion. This formulation is restrictive because spot-level expression reflects not only local morphology but also cellular identity, neighborhood composition and tissue-level organization. We propose BCARP, a Biology-guided Context-Aware Residual Propagation framework for histology-guided spatial transcriptomics prediction. Instead of directly predicting gene expression from histology embeddings, BCARP treats them as morphology visual priors and progressively refines spot representations in a transcriptomics-oriented latent space. Each refinement step integrates nuclei-guided local cellular context with prototype-guided global context propagation, enabling information exchange across both neighboring and spatially distant spots. A pattern-scale decoder further separates spatial expression into pattern prediction from raw expression with scale calibration. Evaluated on three ST datasets and ten HEST-1k cohorts, BCARP achieves the highest mean correlation-based performance against other baselines. Numerical results support biology-guided local-global residual propagation as an effective alternative to visual decoding for histology-to-transcriptomics prediction.

---


### 344. [DAC-Loop: Distillation-Aware Compression for Remote Sensing CNN](https://arxiv.org/abs/2610.35175)

**<font color=#1a73e8>作者：</font>** Rico Staedeli, Lorena Raichle, Konstantinos Tzevelekakis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While large-scale models achieve strong results in remote sensing scene classification, deploying them on edge devices remains difficult due to limited compute, memory, and energy budgets. Compact CNN backbones are therefore a practical choice in many real-world settings, offering efficient inference with well-optimized implementations on embedded hardware. To push this efficiency further, we investigate how far a knowledge-distilled student model can be compressed while preserving high accuracy. We propose a Distillation-Aware Compression Loop (DAC-Loop) that integrates (i) knowledge distillation applied both before and after structured channel pruning, and (ii) an iterative compression schedule that alternates structured pruning with unstructured sparsification. Across EuroSAT and NWPU-RESISC45, the DAC-Loop consistently improves the accuracy-compression trade-off relative to standard one-shot pruning and single-stage KD recovery, maintaining strong accuracy even beyond 90% parameter reduction. These results demonstrate that combining distillation and pruning in a unified iterative loop offers an effective path toward compact remote sensing models.

---


### 345. [LEAP: a Latent Embedding Anomaly Patch-Transformer for time-series anomaly detection](https://arxiv.org/abs/2610.35190)

**<font color=#1a73e8>作者：</font>** Cristhian Moya-Mota, Ignacio Aguilera-Martos, Diego García-Gil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series anomaly detection is dominated by reconstruction-based neural detectors, whose objective is structurally flawed. Since the target is also the input, an expressive model can learn to reconstruct anomalies too, leaving uninformative residuals. Recent large-scale benchmarks show that, on curated data, elaborate deep detectors rarely beat simple statistical baselines, while current leaders rely on representation learning. We propose LEAP (Latent Embedding Anomaly Patch-Transformer), which combines masked prediction with latent representation-based anomaly evidence, without relying on reconstruction or attention-based scoring. The model removes patches from a window and predicts them from the remaining temporal and cross-channel context, so prediction errors measure how well learned dynamics explain hidden segments. Deterministic complementary group masking ensures every time step is scored while hidden, with identical visible fractions during training and inference. LEAP adds three label-free evidence sources: latent-embedding novelty calibrated by local density, local temporal contrast, and per-channel novelty pooled over channels selected by six label-free criteria. Under the TSB-AD protocol, the full model achieves a VUS-PR of $0.5179 \pm 0.0022$ on $180$ held-out multivariate series. On TSB-AD-U, a univariate variant combining multi-scale masked-prediction scoring with latent novelty, without contrast or channel-pool novelty, achieves $0.6194 \pm 0.0016$ on $350$ held-out series. Both results average three random seeds. A five-stage ablation on TSB-AD-M, supported by paired Wilcoxon signed-rank tests, shows statistically significant gains from each successive component.

---


### 346. [Lost in Translation: Investigating Systematic Discrepancies between Parallel English and Chinese Names of American Chinese Restaurants](https://arxiv.org/abs/2610.35191)

**<font color=#1a73e8>作者：</font>** Hang Jiang, Nanxi Liu, Tiantian Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Given that the Chinese are one of the oldest ethnic groups to immigrate to the US, their cuisine have become central to the US dining scene and an interesting avenue to study how Chinese immigrants have culturally adapted into American life. In that regard, previous research has focused on analyzing the English names that Chinese restaurants adopt, e.g., finding the use of familiar and typical words. To investigate how Chinese immigrants have culturally integrated in the US depending on social, geographic and demographic contexts, we investigate in this work the under-explored relationship between the Chinese and English names of American Chinese restaurants. Specifically, we conduct a study on 3,172 Chinese restaurants (10% of the total on Google Maps) sampled across the US. We present 8-dimension name frames to capture the underlying meanings behind names and create the NameFrames dataset containing 884 annotated parallel Chinese/English names. We also built an NLP pipeline to analyze the semantic discrepancies between names with both frame-based and embedding-based distance metrics. Our frame analysis shows that English names more often emphasize Location and Specialty, while Chinese names more often emphasize Positivity and Ambiance. Furthermore, we observe that for Chinese restaurants located in urban areas, those in counties with a higher concentration of Chinese population, or those that are relatively new, the discrepancies between the English and Chinese names are noticeably larger. Finally, interviews with 10 Chinese restaurant owners reveal additional interesting insights regarding naming conventions.

---


### 347. [Trustworthy Recursive Self-Improvement in the Era of Large Models: Foundation, Risks, Evaluation and Open Challenges](https://arxiv.org/abs/2610.35193)

**<font color=#1a73e8>作者：</font>** Jiayue Pu, Ang Gao, Jinyi Bai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems built around large models increasingly use experience and feedback to make persistent changes to models, prompts, memories, tools, and workflows. Recursive self-improvement (RSI) extends this process to inductive biases and to the mechanisms that govern future updates, which can themselves be revised and reused across improvement cycles. Yet self-modification alone does not guarantee trustworthy improvement. Reported gains may reflect flawed evaluations, previously acquired capabilities may deteriorate, and compliance with behavioral constraints may weaken. Compromised artifacts or sensitive information may also persist in successor systems. Changes to improvement mechanisms may invalidate earlier verification results and make human oversight less effective. This survey presents an operational definition and process framework for RSI and organizes the requirements for trustworthy RSI into four interconnected themes: genuine and sustained improvement; behavioral constraints, alignment, and fairness; system security and privacy; and transparency and controllability. We examine these themes from three perspectives: Improvement Validity, Constraint Preservation, and Effective Oversight. This analysis covers improvement diagnosis, proposal generation, proposal evaluation, and update implementation (S1--S4), including the recursive application of these stages to improvement mechanisms (RI). We review risks, safeguards, and evaluation evidence for individual updates, effects inherited by successor systems, and revisions to improvement mechanisms, while distinguishing direct RSI findings from evidence in related systems. Finally, we examine evaluation settings, identify requirements for independent and longitudinal assessment, and discuss applications and open research problems.

---


### 348. [OrthoRF: Exploring Orthogonality in Object-Centric Representations](https://arxiv.org/abs/2610.35203)

**<font color=#1a73e8>作者：</font>** Despoina Touska, Bastiaan Onne Fagginger Auer, Alexandru Onose 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural synchrony is hypothesized to help the brain organize visual scenes into structured multi-object representations. In machine learning, synchrony-based models analogously learn object-centric representations by storing binding in the phase of complex-valued features. Rotating Features (RF) instantiate this idea with vector-valued activations, encoding object presence in magnitudes and affiliation in orientations. We propose Orthogonal Rotating Features (OrthoRF), which enforces orthogonality in RF's orientation space via an inner-product loss and architectural modifications. This yields sharper phase alignment and more reliable grouping. In evaluations of unsupervised object discovery, including settings with overlapping objects, noise, and out-of-distribution tests, OrthoRF matches or outperforms current models while producing more interpretable representations, and it eliminates the post-hoc clustering required by many synchrony-based approaches. Unlike current models, OrthoRF also recovers occluded object parts, indicating stronger grouping under occlusion. Overall, orthogonality emerges as a simple, effective inductive bias for synchrony-based object-centric learning.

---


### 349. [Same Story, Different Lens: A Multi-Agent System for Cross-Outlet News Framing Analysis](https://arxiv.org/abs/2610.35208)

**<font color=#1a73e8>作者：</font>** Affan Yasin, Yueqi Lyu, Rubia Fatima 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> News outlets covering the same event differ in what they emphasize and omit. \textit{Same Story, Different Lens} is an experimental research prototype for comparing these choices. It collects world and politics coverage from 17 outlets, groups reports about the same event, and produces structured analyses of sentiment, political lean, framing, loaded language, possible omissions, and model-estimated proportions of factual claims and opinion. Loaded-language entries include quotations and neutral rewordings. Three model roles (agents) handle article analysis, assessment of source support, and cross-outlet briefing generation. Analyses are stored in a JSONL archive. The evaluation compares outlet-level lean estimates with approximate, predefined reference ratings and summarizes the Critic's model-assigned grounding scores. These measures provide preliminary diagnostics. A grounding score reflects the model's assessment of support in the supplied text and does not establish factual accuracy or constitute independent verification.

---


### 350. [Understanding Practical Optimization in Machine Learning](https://arxiv.org/abs/2610.35209)

**<font color=#1a73e8>作者：</font>** Egor Shulgin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning relies on practical optimization methods that often differ from the algorithms studied in classical analyses: they train submodels, clip or normalize gradients, use layer-wise non-Euclidean directions, or approximate costly inner computations. This thesis analyzes the objective, assumptions, update, and computation defined by these procedures, rather than those of simplified proxies. For submodel training, we show that Independent Subnetwork Training can converge to a shifted fixed point because sketching before differentiation biases the update for the original objective. Model-Agnostic Sparsified Training instead incorporates the sketch distribution into its objective, which makes sketched gradients unbiased and admits convergence guarantees. For private optimization, we show that adaptive quantile clipping retains bias at any fixed quantile, while suitable quantile schedules recover near-optimal nonconvex rates under heavy-tailed noise. We then combine smoothed normalization with error compensation and obtain distributed private convergence guarantees under standard assumptions, without assuming bounded gradients. For optimizers based on linear minimization oracles, we develop and validate a layer-wise generalized smoothness model and build on it the Gluon framework for Muon- and Scion-style methods. We also show that the approximate orthogonalization in Muon matters: less precise orthogonalization calls for smaller stepsizes, so its precision should be tuned together with the learning rate. Overall, practical methods are better understood when theory retains the features that determine their optimization behavior.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-446](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
