# 📦 其他研究 | 2026年07月15日

> 本类共 **420** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-420](./part-09.md)

---

### 251. [The Singularity Space: A Generative Diffusion Framework for Signal Representation](https://arxiv.org/abs/2607.10930)

**<font color=#1a73e8>作者：</font>** Eli Bar-Yosef, Amir Averbuch, Eli Turkel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models often represent signals as dense grids of amplitudes, blurring sharp transients that are crucial for the correctness of physical signals. We introduce Singularity Space, a generative framework that represents signals through complex-plane singularities, rooted in the classical pole-residue representation of meromorphic functions. We learn a latent space of physically constrained, per-signal singularity configurations to solve an inverse problem from degraded or partial observations. The framework has three key properties: interpretability, in which each generated singularity configuration corresponds to a set of physical parameters; structural stability, which mitigates Gibbs artifacts at discontinuities; and resolution-free output reconstruction on arbitrary grids without retraining or interpolation. Our framework employs a transformer-based diffusion model that directly predicts samples at complex-plane singularity coordinates, subject to geometric constraints during sampling. As a controlled test case for sharp-feature recovery, we evaluate our framework on 1D Burgers shocks, where each shock is represented by 32 predicted singularities (an $8\times$ reduction versus a 1024-point grid signal). Our framework preserves signal structure ($\text{TV ratio} \approx 1$) under unseen test-time observation noise, achieves a $4.2\times$ lower reconstruction error in zero-shot sub-resolution generalization than a grid-based baseline, and recovers physical parameters to $10^{-4}$ absolute error in-distribution. These results suggest that singularity-based representations may provide a practical foundation for other transient-dominated signals such as speech and biomedical signals, with potential extension to higher-dimensional domains.

---


### 252. [Bandit PCA with Minimax Optimal Regret](https://arxiv.org/abs/2607.10936)

**<font color=#1a73e8>作者：</font>** Moïse Blanchard, Dmitrii Ostrovskii, Aadirupa Saha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the bandit-feedback version of online principal component analysis (Bandit PCA): in each round $t = 1,\dots,T$, the adversary selects a $d \times d$ symmetric gain matrix $G_t$ with spectrum in $[0,1]$ and rank at most $r$; the learner simultaneously selects a unit vector $w_t \in S^{d-1}$ and receives the reward $w_t^\top G_t w_t$. The learner receives no other feedback, and aims to minimize the regret against the best unit vector in hindsight. This problem was introduced by Kotlowski and Neu (2019), who gave an algorithm with regret $O(d\sqrt{rT \log T})$ and showed the lower bound of $\Omega(r\sqrt{T/\log T})$. We improve upon both of these bounds and essentially bridge the gap between them, establishing the minimax regret of order $r\sqrt{dT}$ up to polylogarithmic factors in $d$ and $T$. The upper bound is attained by a novel algorithm, which combines online mirror descent on the spectrahedron of (real) density matrices with a multiscale exploration scheme in which the eigenspaces with different spectral magnitudes are updated at different rates. For the lower bound, we construct an adaptive adversary that refines a hidden large-reward subspace based on the learner's actions, in such a way that low regret is impossible without estimating the subspace; as a result, lower-bounding the regret reduces to studying the arising subspace estimation problem. Finally, we discuss connections of Bandit PCA with adaptive-measurement quantum tomography.

---


### 253. [ARMOR-IMC: Adaptive Resource Mapping for Operational Robustness via Secure In-Memory Computing](https://arxiv.org/abs/2607.10938)

**<font color=#1a73e8>作者：</font>** Muhtasim Alam Chowdhury, Ramtin Zand, Soheil Salehi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The massive data-movement overhead in traditional architectures has led to the adoption of In-Memory Computing (IMC) for energy-efficient Deep Neural Network (DNN) processing. By leveraging emerging devices like Spin-Orbit Torque Magnetic Tunnel Junctions (SOT-MTJs), IMC bypasses the "memory wall" and reduces leakage power inherent in traditional CMOS. However, this shift introduces dual hardware threats: manufacturing Process Variation (PV) degrades reliability and increases vulnerability to fault injection, while power Side-Channel Attacks (SCAs) compromise security. Existing defenses address these threats in isolation. This work presents a posttraining framework that simultaneously hardens analog IMC accelerators against both threats without retraining the model. Implemented in the IMAC-Sim simulator, our approach uses the proposed Variation Impact Score (VIS) to guide the mapping of Fault Observation Windows (FOWs) and introduces the Leakage Per Inference (LPI) metric to quantify input-dependent power variability under stochastic injection and the resulting reduction in effective signal-to-noise ratio. Experiments show that PV-induced faults can degrade accuracy by over 50%, while our method restores near-baseline accuracy and mitigates the threat of correlation-based power analysis attacks.

---


### 254. [Unsupervised Detection of Entry and Exit Regions from Vehicle Trajectories for Camera-Agnostic Turning Movement Counts](https://arxiv.org/abs/2607.10949)

**<font color=#1a73e8>作者：</font>** Parikshit Singh Rathore, Vishwajeet Pattanaik, Punit Rathore  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Turning movement counts are essential for intersection-level traffic management, yet their collection remains predominantly manual due to the cost of per-camera region annotation. This paper presents an unsupervised pipeline that identifies entry and exit regions directly from raw vehicle trajectories extracted via object detection and multi-object tracking, requiring no manual annotation, camera calibration, or prior knowledge of intersection geometry. Unlike trajectory clustering methods that classify individual trajectories using pairwise similarity and must be re-executed on every new batch, the proposed pipeline clusters initial and terminal point locations to produce persistent spatial region polygons that classify future trajectories by point-in-polygon containment at linear cost. The pipeline comprises six sequential steps, each with configurable parameters evaluated through a systematic statistical analysis spanning 19,152 pipeline executions across 25 surveillance cameras capturing dense heterogeneous traffic in Bengaluru, India, and 10 sequences from the UA-DETRAC benchmark dataset. Both parametric and nonparametric testing frameworks identify three consistently significant parameters and yield an empirically grounded recommended configuration. Under this configuration, the pipeline achieves a median classification error of approximately 3% across all 25 cameras, including 16 held-out locations, with GEH values within accepted engineering thresholds. Compared with two trajectory clustering baselines, the proposed pipeline exhibits greater stability across camera views and lower computational cost, at the expense of higher median error. Extended evaluation demonstrates that calibration clips of at least 60 minutes and peak-traffic selection further improve region estimation quality.

---


### 255. [Sticky Jump Diffusions: A Unifying View of Masked, Continuous, and Hybrid Diffusion](https://arxiv.org/abs/2607.10951)

**<font color=#1a73e8>作者：</font>** Pascal Jutras-Dubé, Patrick Pynadath, Jeremy Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Sticky Jump Diffusions (SJDs), continuous-time Markov processes on $\mathbb R^d$ whose discrete anchors are token embeddings. In forward time, anchors release their mass at a hazard rate and the released mass diffuses in the continuous ambient space; time reversal couples a score-driven SDE with a sticky jump kernel whose rate and destination are fixed by flux balance with the forward law. We estimate the score and the per-anchor reverse hazards from a single denoising classifier via Denoising Hazard Matching, the hazard analogue of denoising score matching, with simulation-free cross-entropy training. SJD recovers masked diffusion, continuous diffusion, and hybrid diffusion as limits. Its reversal explains features that each family treats as given: the mask of masked diffusion carries no evidence about the source token because the unsticking kernel of every anchor collapses to the same absorbing point; the terminal projection of continuous diffusion is required due to the absence of atoms in its forward marginal, without which flux balance yields no reverse jumps; and the update rules of hybrid diffusion (commit rate, destination, and drift) all follow from flux balance rather than from separate design. Beyond these limits, the unsticking kernel becomes a design space: a cross-position blending corrupts each position toward a blend of its neighbors' clean values or embeddings, turning dependency structure such as spatial locality or a constraint graph into an inductive bias of the corruption itself, and improves over the identity-kernel hybrid on CIFAR-10, Text8, and Sudoku.

---


### 256. [Learning Anatomy-Grounded CT Vision-Language Representations with Organ-Hierarchical Report Knowledge](https://arxiv.org/abs/2607.10953)

**<font color=#1a73e8>作者：</font>** Guoliang You, Hongming Li, Yuanwang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language pretraining (VLP) from paired CT images and radiology reports enables scalable representation learning, but most existing methods align either whole scans with entire reports or local image regions with text fragments. These formulations underuse a key property of radiology reports: findings are organized around anatomical structures, with abnormalities described by organs, disease concepts, locations, and severity-related attributes. We propose OKA-CT, an organ-hierarchical knowledge-augmented framework for CT-report VLP. OKA-CT first converts free-text reports into organ-conditioned knowledge using radiology report parsing and LLM-assisted semantic structuring. The extracted hierarchy is used across two learning stages. Stage~1 injects anatomy-grounded evidence into the CT visual representation through fine-grained organ-conditioned supervision, while Stage~2 uses organ-specific report evidence to guide structured report-CT contrastive learning, where hierarchy-derived semantic soft targets treat non-paired cases with shared organ-level findings as weak semantic positives rather than uniform negatives. A lightweight query-based global branch further aggregates disease-relevant volumetric evidence for whole-scan representation. On CT-RATE and RAD-ChestCT datasets, OKA-CT achieves zero-shot abnormality diagnosis AUROCs of 84.9 and 72.2, outperforming prior CT VLP baselines. Retrieval and patch-occlusion analyses further show improved report-image alignment and stronger sensitivity to disease-associated anatomical regions.

---


### 257. [WSqD: A Horizon-Free Learning Rate Schedule for Large Model Training](https://arxiv.org/abs/2607.10959)

**<font color=#1a73e8>作者：</font>** Jianhao Ma, Yuxin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard learning rate schedules such as cosine annealing are tied to a fixed training horizon, limiting their ability to accommodate post hoc horizon extension. Warmup-stable-decay (WSD) partially addresses this issue by maintaining a long constant-rate phase before a short linear cooldown, allowing training to resume from a pre-decay checkpoint. However, its peak learning rate is still tuned based on the original training horizon and can become suboptimal when training is extended. Motivated by stochastic convex optimization, we propose WSqD (Warmup with Square-root base and linear Decay), a learning rate schedule that replaces WSD's constant stable phase with a shifted inverse-square-root base while retaining the final linear cooldown. In the stochastic convex setting, WSqD provably attains the minimax-optimal $O(1/\sqrt{T})$ last-iterate convergence rate. Importantly, its base learning rate schedule is horizon-independent, and the training horizon is needed only to determine when to begin the final cooldown. Empirically, on language-model pretraining using the SlimPajama corpus, WSqD matches or outperforms carefully tuned WSD and other baselines across multiple training horizons while reusing a single peak learning rate.

---


### 258. [Reinforcement Learning for Execution under Dynamic Fees in a Closed-Loop DEX Simulator](https://arxiv.org/abs/2607.10960)

**<font color=#1a73e8>作者：</font>** Wen-Ting Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trader-facing dynamic fees are increasingly proposed for automated market makers (AMMs), but historical data do not identify how order flow would respond: trader-facing fees do not vary, trader types are latent, and a replayed tape is not a sequential decision environment. We therefore construct a minimal closed-loop simulator in which the missing signal exists by construction: two constant-product pools repriced by an equilibrium-inspired dynamic-fee rule, fee-sensitive noise flow, and closed-form CEX--AMM arbitrage. Equilibrium is used as a closure principle, not as an object the trader learns. Against a tuned benchmark ladder of schedule, planning, lookahead, and tabular policies, a small DQN is the only evaluated valid policy whose paired improvement over tuned one-step routing excludes zero. On a reserved final block of 1{,}000 seeds with completion forced to 1.0 for every policy, it reduces implementation shortfall under every tested intra-step ordering, by $13.3\bps$ of order notional under the pre-specified agent-last ordering, and the edge is concentrated in, and learned from, dynamic-fee environments: under constant fees the paired difference is indistinguishable from zero. The result is model-conditioned counterfactual evidence about execution control in AMMs, not evidence about historical traders, equilibrium play, or deployable profit.

---


### 259. [Efficient Online Proportional Sampling with Applications to Smoothed Online Learning](https://arxiv.org/abs/2607.10963)

**<font color=#1a73e8>作者：</font>** Amirmahdi Mirfakhar, Maria-Florina Balcan, Hedyeh Beyhaghi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of efficient online proportional sampling from a high-dimensional domain under a $\sigma$-smoothed adversary, where the sampling distribution is induced by a dynamically evolving weight function defined over a sequence of piecewise-structured partitions. This setting captures a broad range of applications, including principal-agent games (e.g., pricing and contract design), and algorithm configuration and parameter tuning. The central challenge is maintaining an efficient data structure as the induced partition grows increasingly complex over time -- naively, the number of subregions can grow as $O(t^d)$ by round $t$ in $d$ dimensions. We design a data structure that supports efficient updates and proportional sampling while avoiding the cost of explicitly maintaining this exponential growth, where the discontinuities are structured from axis-parallel hyperplanes. Under a $\sigma$-smoothed adaptive adversary, we prove a tight $O(\sqrt{\sigma T})$ bound on the depth of our data structure, and an $O(\log T)$ bound under a random-order adversary -- to our knowledge, the first such results for this class of problems. We apply this framework to online learning with piecewise-structured rewards, obtaining efficient no-regret algorithms under both full-information and bandit feedback, with provable sublinear regret guarantees.

---


### 260. [SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in Reinforcement Learning](https://arxiv.org/abs/2607.10966)

**<font color=#1a73e8>作者：</font>** Mingyuan Wu, Jingcheng Yang, Shengyi Qian 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Self-Verified Reasoner (SVR-R1), a multi-turn RL framework that turns a model's own verification into a learning signal for multimodal reasoning. For each query, the model proposes an answer using the same weights, and issues a binary self-verdict (Yes/No). A 'No' triggers a second-chance rethink; a 'Yes,' or a turn cap, finalizes the output for computing the outcome-based reward. SVR-R1 is implemented with GRPO and an asynchronous multi-turn rollout framework and needs no external supervision or auxiliary critics. We evaluate SVR-R1 on vision-language reasoning benchmarks and show that it improves accuracy by a large margin over strong standard GRPO baselines. Training dynamics show decreasing reliance on verification-fewer verification turns, yet higher test accuracy-indicating that the gap between verification and generation narrows as the policy internalizes self-correction and chooses the most confident answer via our framework. SVR-R1 bridges the less explored intersection of inference-time self-refinement and RL training for VLMs, offering a simple yet effective recipe for bootstrapping multimodal reasoning. We will open-source \textbf{SVR-R1} to facilitate future research in VLMs.

---


### 261. [Enhanced Byzantine-Robust Federated Learning Via Truncated-Quadratic Loss for Heterogeneous Data](https://arxiv.org/abs/2607.10970)

**<font color=#1a73e8>作者：</font>** Zhi-Yong Wang, Hao Nan Sheng, Werner Stefan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning distributes data among $n$ clients, making it vulnerable to malicious attacks and data heterogeneity, which together pose challenges for robust learning. To tackle this issue, centered clipping and Huber aggregators have been exploited for Byzantine robustness. In this paper, we first demonstrate their equivalence via convex conjugate theory, and show that they can yield biased solutions in the presence of outliers, leading to failure under high data heterogeneity and a substantial fraction of outliers. Next, we propose a new robust aggregation rule that utilizes the truncated-quadratic (TQ) loss, effectively mitigating the biases of existing methods, such as centered clipping and Huber aggregators. We show that our aggregator achieves order-optimal Byzantine-robust learning under nonconvex loss functions and heterogeneous data, ultimately enhancing the reliability of federated learning systems. Additionally, we provide a robust deviation estimation strategy for TQ, demonstrating its effectiveness. Furthermore, we show that TQ maintains robustness even when only an estimate of the number of Byzantine clients is available. Finally, experimental results on MNIST, Fashion-MNIST, and CIFAR-10, indicate that our aggregator provides better robustness performance than the competing techniques.

---


### 262. [From Checker to Forecaster: Code-Owned Evaluation of Model-Generated Strategic Routes Under Delayed Ground Truth](https://arxiv.org/abs/2607.10972)

**<font color=#1a73e8>作者：</font>** Aleh Manchuliantsau  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many evaluations of model outputs rely either on contracts checkable at evaluation time or on feedback that arrives within the operating loop. We study the complementary setting in which ground truth is delayed, censored, or private, so deterministic code cannot check correctness at scoring time and must instead issue a code-owned provisional forecast. RouteCast instantiates this regime for model-generated typed strategic routes: models propose candidate routes and structured factors; point-in-time evidence, reference classes, and deterministic transformations produce a provisional forecast-ranking; later outcomes evaluate the forecast. In a retrospective venture pilot on 21 binary-outcome cases (6 positive, 15 negative), the whole-packet RouteCast score showed preliminary retrospective discrimination (AUC 0.756, 95% CI [0.471,0.980]), while a blind LLM judge reached AUC 0.678 [0.419,0.897] and an identity-exposed LLM judge reached AUC 0.761 [0.515,0.944], consistent with recognition- or outcome-related leakage risk. A preregistered decomposition ablation on the same binary subset found that converting the identical inputs into typed staged routes was indistinguishable from the whole-packet score (Delta AUC = -0.144, 95% CI [-0.471,0.176]) and from a deterministic heuristic (Delta AUC = -0.089, 95% CI [-0.412,0.278]). The pilot establishes an auditable feasibility result and exposes failure modes; it does not establish prospective calibration, causal decision improvement, route-decomposition advantage, or cross-domain validity.

---


### 263. [EquiFusion: Kinematics-Agnostic Human Motion Prediction via Equivariant Latent Diffusion](https://arxiv.org/abs/2607.10984)

**<font color=#1a73e8>作者：</font>** Cecilia Curreli, Florian Hofherr, Dominik Muhle 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Stochastic 3D Human Motion Prediction models are fundamentally constrained by hard-coding the skeleton kinematics, severely limiting generalization, preventing cross-dataset training, and requiring complex data retargeting. We introduce EquiFusion, the first kinematics-agnostic model to solve this bottleneck, implementing a latent diffusion model with a permutation equivariant architecture. EquiFusion treats the kinematics' connectivity as an explicit input parameter, ensuring its internal computations are inherently agnostic to joint ordering and graph structure. This novel design enables truly cross-dataset generalization to unseen kinematics and unlocks novel zero-shot directions, such as motion prediction from partial or occluded observations and targeted limb generation. EquiFusion achieves state-of-the-art results on major benchmarks, being up to 75% more compact than previous kinematics-specific methods, while achieving faster training and inference. EquiFusion thus establishes a new, flexible standard for robust human motion prediction. Model and training code are available at this https URL.

---


### 264. [MED-DSLC: Multi-Expert-Domain Classification via Domain Supervision and Logit Calibration](https://arxiv.org/abs/2607.10985)

**<font color=#1a73e8>作者：</font>** Zheng Zeng, Deepak Sridhar, Nuno Vasconcelos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) such as CLIP enable zero-shot classification by comparing image features with text prompts in a shared embedding space. A fundamental property underlying this capability is the global comparability of logits across arbitrary candidate classes. However, VLMs are often adapted to fine-grained domains using techniques such as LoRA. While this improves in-domain accuracy, out-of-domain accuracy degrades. This leads to a highly fragmented model ecosystem, with thousands of specialized models. Multi-Expert-Domain classification seeks to address this problem, by merging LoRAs trained independently on specialized domains. However, due to the independent training, the various domain experts no longer produce globally calibrated logits. As a result, when evaluating over the union of multiple domain-specific class sets, heterogeneous logit scales induce cross-domain interference and artificially high confidence for out-of-domain classes, inducing prediction errors. In this work, we identify domain supervision and cross-domain logit miscalibration as the key issue to scalable multi-domain zero-shot recognition. We propose MED-DSLC, combining domain supervised training and domain-wise logit scaling, to explicitly restore global logit comparability. MED-DSLC is a lightweight solution for MED classification, which is shown to preserve within-domain discrimination while reducing cross-domain logit interference with minimal data. Extensive experiments across diverse fine-grained benchmarks demonstrate that it substantially improves mean accuracy (+15\%), cross-domain robustness, and scalability in the size of MED classification problem. Our results show that restoring output-level calibration is essential under highly data imbalanced settings for achieving a truly zero-shot VLM under multi-domain specialization.

---


### 265. [MMA-Former: Multi-Window Mixture-of-Head Attention Transformer for Adaptive PNI Prediction in 3D MRI](https://arxiv.org/abs/2607.10988)

**<font color=#1a73e8>作者：</font>** Youngung Han, Induk Um, Kyeonghun Kim 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perineural invasion (PNI) is a critical prognostic factor in cholangiocarcinoma. Non-invasive prediction from 3D MRI is challenging, demanding models that efficiently capture both fine-grained details and global context. We propose the Multi-window Mixture-of-Head Attention Transformer (MMA-Former), a novel end-to-end 3D architecture featuring a Coarse-Fine Transformer (CFT) structure for parallel multi-scale feature extraction. We advance this structure by integrating a novel Window-Specific Mixture-of-Head attention (WS-MoH) mechanism. Unlike standard Multi-Head Self Attention (MSA), WS-MoH generates a representation for each 3D window and dynamically routes the entire window to specialized or common attention heads. This enables spatially adaptive feature extraction tailored to the local context of each window, enhancing specialization and reducing redundancy without increasing parameters. Evaluated on a retrospective dataset of 168 T1-weighted MRI scans, MMA-Former achieved an AUC of 0.752, outperforming other 3D architectures, including the best CNN (AUC of 0.708) and Transformer baselines (AUC of 0.681).

---


### 266. [TreeSoc: Tree-Structured Dynamic Reasoning and Tool Synergy for Soccer Video Understanding](https://arxiv.org/abs/2607.10990)

**<font color=#1a73e8>作者：</font>** Thanh-Nhan Vo, Thanh-Khoi Nguyen, Trong-Thuan Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated understanding of complex soccer scenarios from video remains a significant challenge for contemporary vision-language models (VLMs), which suffer from shallow cross-modal alignment and exhibit fundamental limitations in multi-step reasoning and coordinated tool integration. We present TreeSoc, a structured reasoning framework that reformulates soccer video question answering as a hierarchical search problem rather than a single-pass prediction. Specifically, TreeSoc employs a dynamic depth-first search (DFS) mechanism that decomposes complex queries into sequentially ordered sub-tasks, enabling iterative reasoning refinement through explicit intermediate states. This tree-structured decomposition naturally supports adaptive tool routing, wherein domain-specific modules are selectively activated and their outputs incorporated at each reasoning node to produce contextually grounded predictions. On SoccerBench, TreeSoc achieves state-of-the-art performance, with accuracies of 85.2%, 87.4%, and 82.2% on TextQA, ImageQA, and VideoQA, respectively. Additionally, TreeSoc further demonstrates strong cross-domain generalization, attaining 74.16% accuracy on NExT-QA. These results establish structured, tool-augmented tree reasoning as an effective paradigm for robust video understanding. Code is available at: this https URL.

---


### 267. [LoSA-Net: A Localized and Scale-Adaptive Network for Boundary-Sensitive Prediction of Perineural Invasion in 3D MRI](https://arxiv.org/abs/2607.10992)

**<font color=#1a73e8>作者：</font>** Youngung Han, Hyunsu Go, Kyeonghun Kim 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perineural invasion (PNI) is a clinically relevant indicator of tumor aggressiveness and can influence surgical decision-making, motivating interest in reliable preoperative assessment. The subtle MRI features of PNI, however, often resemble nearby anatomy, complicating noninvasive prediction. These fine perineural cues are easily attenuated by routine downsampling or overly global feature aggregation, reducing the effectiveness of conventional volumetric models. We present LoSA-Net, a localized and scale-adaptive architecture for boundary-sensitive PNI prediction in 3D MRI. Talking Neighborhood Attention (TNA) preserves nerve-aligned detail through localized self-attention with head-wise mixing, and Scale-Adaptive Feature Mixing (SAFM) modulates the receptive field using multi-scale depthwise processing. Cross-Scale Refinement and Alignment (CSRA) maintains consistency between semantic context and high-resolution boundaries across stages. In contrast-enhanced MRI scans from 168 patients with cholangiocarcinoma, LoSA-Net achieves an AUC of 0.7567 and outperforms representative convolutional and transformer baselines under matched preprocessing and optimization settings.

---


### 268. [Confidence Scores in Open-Vocabulary Detection Are a Biased Mixture of Scale and Semantics](https://arxiv.org/abs/2607.10993)

**<font color=#1a73e8>作者：</font>** Yi Tang Soon, Jun-Wei Hsieh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models such as CLIP have enabled open-vocabulary object detectors that generalise to novel categories via vision-language similarity. However, the confidence scores these detectors produce are not reliable localization probability estimates: they conflate visual scale and semantic query specificity with the true detection signal. Through controlled experiments on COCO across three foundation-model-based detectors (GroundingDINO, OWL-ViT, YOLO-World), with the scale-bias finding further replicated on LVIS (1,203 categories) using GroundingDINO, we show that s=cos(v,t) is a biased mixture of two effects. Scale bias (alpha = +0.064, r = 0.579, p = 1.29 x 10^-58) systematically inflates scores for large objects. Semantic bias (beta = -0.705, p = 5.23 x 10^-41) suppresses scores for generic queries. Both biases are structurally inevitable from CLIP's image-level pretraining. Threshold adjustment cannot remove them: oracle per-scale thresholding yields Delta F1 = +0.001 for small objects versus +0.102 for large. A parameter-free temperature scaling correction improves small-object Recall@10 by 19.6% (p < 0.01) without retraining. This comes at a modest, measurable cost to pooled-ranking precision, so the bias is partially, not freely, reversible at inference time. These findings reveal a fundamental limitation of adapting image-level foundation models to region-level detection tasks.

---


### 269. [AsySplat: Efficient Asymmetric 3D Gaussian Splatting for Long-Sequence Scene Modeling](https://arxiv.org/abs/2607.10995)

**<font color=#1a73e8>作者：</font>** Yingji Zhong, Dave Zhenyu Chen, Fuzhao Ou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent generalizable 3D Gaussian Splatting models have advanced long-sequence novel view synthesis (NVS), but at the cost of substantial redundant computation. We identify that the redundancy can be mitigated based on two observations: (i) high-precision geometry is not strictly required for high-quality NVS; (ii) appearance learning is generally easier than geometry recovery. Motivated by these insights, we propose an asymmetric architecture that decouples geometry and appearance modeling. The geometry branch processes coarse-grained tokens with most of the parameters for multi-view reconstruction, while the appearance branch operates on fine-grained tokens to capture details using significantly fewer parameters. The two branches interact through bilateral connections, enabling mutual guidance for their respective tasks. This task-aware asymmetry reduces the computational redundancy and allocates the computation more judiciously, thereby increasing parameter efficiency and enabling smaller models to achieve strong performance. On 32-view 960P inputs, our model matches optimization-based methods while delivering nearly 800x speedup, and surpasses the zero-shot performance of state-of-the-art generalizable models with markedly fewer parameters and reduced training/inference overhead, achieving an overall efficiency improvement.

---


### 270. [Temporal Feature Distillation for Label-Efficient Precise Event Spotting in Sports Videos](https://arxiv.org/abs/2607.10998)

**<font color=#1a73e8>作者：</font>** Hao Xu, Xinyu Wei, Sam Wells 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise Event Spotting (PES) requires distinguishing visually similar yet semantically distinct adjacent frames, making it fundamentally different from image classification and coarse action recognition. Although self-distillation methods such as DINO have shown strong representation learning ability in images, we find that directly applying them to PES is ineffective: without supervised guidance, subtle but crucial motion cues are often suppressed as noise, leading to representations that are insensitive to precise event boundaries. To address this, we propose Temporal Feature Distillation, a semi-supervised objective that aligns temporally informative backbone features, rather than projection-head outputs, to preserve motion-sensitive and boundary-aware cues for frame-level localization. A supervised warm-up with a ramp-up schedule further stabilizes training by ensuring that meaningful event cues are learned before unlabeled distillation begins. We also introduce Transformer Gate Shift, a multi-scale gated shifting module that injects motion-aware temporal information into Vision Transformers. Experiments on four fine-grained sports benchmarks show consistent improvements over fully supervised and semi-supervised baselines. Under 10\% supervision on FSPerf, our method improves mAP by 4.54 points over the strongest competing approach, and with only 80\% labeled data, it matches or surpasses the fully supervised 100\% baseline on two of the four datasets.

---


### 271. [SynCLIP: Synonym-Coherent Language-Image Pretraining for Robust Open-Vocabulary Dense Perception](https://arxiv.org/abs/2607.11008)

**<font color=#1a73e8>作者：</font>** Mingjie Xie, Guangjun He, Dongli Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary dense perception (OVDP) aims to localize objects unseen during training by leveraging textual knowledge. Despite the remarkable progress of recent CLIP-based approaches, we identify a critical limitation: synonym-induced grounding inconsistency, where semantically equivalent expressions yield disparate spatial attention patterns. This inconsistency undermines the robustness and performance of existing methods in real-world OVDP applications. To address this issue, we propose SynCLIP, a Synonym-Coherent Language-Image Pretraining framework that enhances synonym-robust grounding for OVDP. SynCLIP introduces a Semantic-consistent Spatial Attention alignment (SSA) module to enhance spatial attention consistency by minimizing discrepancies between attention maps of original and synonymous expressions. Furthermore, a Spatial Attention Refinement (SAR) module selectively strengthens the most semantically relevant spatial regions within aligned maps for more precise and stable grounding. To support synonym-coherent pretraining, we also construct a Synonym-Enriched Visual Corpus (SEViC), which augments each category with multiple synonyms and textual definitions. Extensive experiments on multiple benchmarks demonstrate that SynCLIP substantially improves grounding consistency under diverse linguistic variants and achieves state-of-the-art performance among CLIP-based OVDP methods. Code is available at this https URL.

---


### 272. [When the Reward Suite Is Leaky: A Preregistered Causal Contrast of Natural Verifier False Positives in RLVR](https://arxiv.org/abs/2607.11022)

**<font color=#1a73e8>作者：</font>** Chuyifei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The test suites used as RLVR rewards for code have natural false positives: per-task, persistent, asymmetric errors that accept the same wrong programs every time they appear, unlike the symmetric or resampled noise assumed by existing noise-robustness analyses. We run a preregistered two-arm causal contrast on a deployed suite: GRPO on identical MBPP tasks, seeds, and compute, rewarded by the original MBPP tests (leaky) versus the MBPP+ extra tests (hardened). Two further families replicate the design under a preregistration frozen before their data existed. [C] The average held-out effect is bounded: non-inferior under a preregistered 1.5-pt margin (gap 0.20 pt, one-sided 95% upper bound 0.75 pt). [C] Rewarded false-positive mass tracks a cheap static leakiness audit computed before training (Spearman 0.80), and the registered train-side test puts the leak-stratum FP share +43.8 pt above clean tasks. [E] Auditing every rewarded FP under signed, human-adjudicated rules finds a large residual of verified genuinely wrong code: 47.57% record-weighted; both replication families reproduce a large share. The reward paid for real bugs, not merely suite artifacts. [E] Mechanism evidence is consistent with selection of pre-existing error modes rather than learned exploitation: FP incidence does not grow within our horizon, and untrained base models already produce the same wrong outputs under the leaky filter. We then turn the same instrument on the frontier judges themselves: on their own false positives they self-assess only weakly, a same-author test is unresolved, and even the highest-scoring reader we probe stays far below its score on a weaker policy's errors -- two subjects on MBPP, licensing nothing about frontier models in general. A cheap static audit locates exposure before training; hardening the reward removes the measurement inflation, though here it buys little capability.

---


### 273. [Reference-Based Face Super-Resolution Using the Spatial Transformer](https://arxiv.org/abs/2607.11025)

**<font color=#1a73e8>作者：</font>** Varun Ramesh Jois, Antonella DiLillo, James Storer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face super-resolution is the task of increasing the resolution of an image containing a face thereby adding finer detail. It is a ubiquitous task in many computer vision applications and quite often the user isn't even aware that it is being performed. However, doing it with high fidelity is challenging as it is an ill-posed problem. In this paper we present a reference-based solution for face super-resolution that uses higher resolution reference images to aid in the task. We show an alignment module based on the spatial transformer that is considerably more stable than the popular deformable convolutions. We also show an aggregation function that can take good quality information from the reference images when available or suppress the function when such information is unavailable. Finally, we show that our relatively smaller model can achieve state of the art results on multiple datasets. The source code is available at this https URL.

---


### 274. [RTFVE: Realtime Face Video Enhancement](https://arxiv.org/abs/2607.11034)

**<font color=#1a73e8>作者：</font>** Varun Ramesh Jois, Antonella DiLillo, James Storer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> There's been a surge in adoption of video conferencing applications for both personal and business use cases. However, the bandwidth limitations faced by many users worldwide may restrict the optimal use of such applications. Although deep learning offers a solution for enhancing low bit rate videos, most models today are either hard to incorporate with modern compression standards or require specialized hardware to run such as significant GPUs making these models impractical. To address these issues, we introduce the Realtime Face Video Enhancement (RTFVE) model which can be easily incorporated with any video decoder and can run in realtime on ordinary CPUs. Experiments show that our model improves perceptual quality over the compressed video baseline at multiple low bitrate settings. The source code will be made available at this https URL.

---


### 275. [Same Stories, Different Journeys: From Social Comparison to Sensemaking in AI-Mediated Peer Career Exploration](https://arxiv.org/abs/2607.11039)

**<font color=#1a73e8>作者：</font>** Pengping Tan, Baoquan Zhao, Zhenhui Peng  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Young job seekers frequently turn to social media to compare themselves with peers and make sense of career possibilities. However, passive feed browsing creates a paradox: the authentic peer content that provides emotional grounding also triggers potentially detrimental upward social comparison and cognitive overload. Previous work has either structured online user-generated content to reduce noise without changing the passive browsing modality, or built AI-powered career exploration systems that disregard authentic human experiences. To address this gap, we developed JobMate, an interactive system that transforms real social media career posts into persona-grounded conversational AI agents, shifting the interaction from passive scrolling to active, personalized dialogue. We conducted a between-subjects study ($N$ = 24, three disciplines) comparing JobMate with native RedNote browsing. Our study shows that JobMate's AI-mediated dialogue redirected social comparison from potentially detrimental upward comparison toward constructive self-reframing, while promoting sensemaking through active conversational engagement. However, users still relied on the authenticity of real peer content for emotional grounding. We discuss design implications for AI systems that augment authentic online user-generated content consumption across social comparison contexts.

---


### 276. [FSFVE: Few Shot Compressed Face Video Enhancement](https://arxiv.org/abs/2607.11040)

**<font color=#1a73e8>作者：</font>** Varun Ramesh Jois, Antonella DiLillo, James Storer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Videocalling has become a popular form of communication in the world today, with many companies providing free services for it. However, there are still millions of people around the world that experience poor quality videocalls due to limitations in bandwidth. This despite, most people having the required hardware. In this paper we present a novel framework for enhancing highly compressed videocalls. We show, that with as little as 10 frames of the face, we can rapidly (in under 100 seconds) train a model to enhance that instance of the videocall. The model can be trained either prior to or during the call, enhancing the rest of the call by producing better quality video. The video conferencing application need not be modified - it can be off the shelf with our system as a layer on top that trains quickly then simply lets the video conferencing application (e.g. Zoom) run as usual, where our system intercepts and improves images before they are displayed. The model is designed to run in realtime on low-compute devices such as a typical laptop CPU. Experimentally, we show that the model significantly improves quality of compressed face video both quantitatively as well as perceptually. Code can be found at this https URL.

---


### 277. [Domain-Aware Scaling Laws Uncover Data Synergy](https://arxiv.org/abs/2607.11052)

**<font color=#1a73e8>作者：</font>** Kimia Hamidieh, Lester Mackey, David Alvarez-Melis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning progress is often attributed to scaling model size and dataset volume, yet the composition of data can be just as consequential. Empirical findings repeatedly show that combining datasets from different domains yields nontrivial interactions. For instance, adding code improves mathematical reasoning, while certain mixtures introduce interference that reduces model performance. We refer to these effects collectively as data synergy, where the contribution of multiple domains exceeds or falls short of the sum of their isolated contributions. In this work, we formalize and quantify data synergy in language model pretraining. Leveraging observational variation across open-weight LLMs with diverse pretraining mixtures, we estimate both direct domain-to-benchmark synergy (how one domain contributes to performance on another) and a second-order domain-domain synergy (capabilities that require co-occurrence of multiple domains). Our framework improves predictive accuracy over domain-agnostic scaling laws and recovers stable synergy estimates. We validate these estimates by training models on predicted optimal and predicted anti-optimal mixtures and confirm that our synergy estimates correctly predict performance rankings.

---


### 278. [AdvNav: Behavior-Guided Black-Box Adversarial Attacks on Vision-Language Navigation](https://arxiv.org/abs/2607.11063)

**<font color=#1a73e8>作者：</font>** Chenyang Li, Kaige Li, Zeyu Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite progress in Embodied AI, Vision-and-Language Navigation systems remain vulnerable to adversarial visual disturbances. Most existing methods rely on white-box access to target model gradients, which is often unrealistic for real-world deployed systems and computationally exhaustive due to recursive backpropagation for optimization, limiting their applicability. While previous black-box methods predominantly target single-step, instantaneous decision tasks, they struggle to handle the task complexities and temporal dependencies. This highlights the need for a gradient-free attack method that can effectively disrupt the multistep sequential perception-action loop using only observable inputs and outputs. Therefore, we propose AdvNav, a behavior-guided black-box adversarial attack framework that disturbs an agent's first-person views during navigation. To construct an informative surrogate objective for effective optimization guidance in gradient-free search under the black-box setting, we design a dual-granularity behavior-based feedback, aggregating a trajectory-level performance score representing overall navigation degradation, an action-level reward score considering the potential decision risk, and a deviation indicator, all of which are extracted from the agent's self-output behaviors. This feedback guides a hybrid optimization strategy that heuristically tunes perturbation strength via adaptive updates and evolves noise spatial structure genetically, to iteratively discover the most disruptive noise configuration. Evaluated against Transformer-based HAMT and LLM-based MapGPT with two types of backbones on R2R dataset, AdvNav achieves 49.70/65.96/87.30% Attack Success Rate. The result demonstrates the effectiveness and generality of AdvNav, reveals critical perception vulnerabilities and offers insights for the design of future resilient VLN models.

---


### 279. [WiFi-JEPA: Self-supervised Learning for WiFi-CSI 3D Human Pose Estimation](https://arxiv.org/abs/2607.11064)

**<font color=#1a73e8>作者：</font>** Doeon Kim, Jungyoon Lee, Seongsin Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> WiFi Channel State Information (CSI) enables privacy-preserving human pose sensing in camera-denied environments, but existing WiFi-based pose estimators often fail under environment shifts and rely on costly camera-based annotation pipelines that limit scale. We propose WiFi-JEPA, a self-supervised framework that learns CSI-native representations by predicting masked latent embeddings instead of reconstructing raw CSI signals that may contain hardware-specific artifacts. WiFi-JEPA makes three contributions: (i) CSI-specific tokenization and link masking tailored to the CSI tensor over channel, time, and link (C,T,L); masking entire Tx-Rx antenna links forces the model to predict one spatial link view from others, capturing cross-link correlations informative of 3D spatial structure. (ii) A ray-tracing CSI simulation pipeline that generates diverse unlabeled CSI from randomized geometric primitives, providing scalable pre-training data without pose annotations. (iii) State-of-the-art results on Person-in-WiFi-3D: WiFi-JEPA outperforms prior WiFi-CSI baselines on both single- and multi-person 3D pose estimation under the same evaluation protocol. We also show that simulated CSI provides complementary pre-training signal to real CSI, and that four vision-native SSL objectives degrade performance below training from scratch, whereas WiFi-JEPA consistently improves downstream pose estimation.

---


### 280. [DDR-Net: Haze-Aware Dual-Domain Refinement for Single-Image Dehazing](https://arxiv.org/abs/2607.11071)

**<font color=#1a73e8>作者：</font>** Xinye Zheng, Ye Yu, Qiang Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image dehazing aims to recover clear scenes from haze-degraded images. It remains challenging due to the atmospheric scattering and the complexity of real-world haze distributions. Although recent end-to-end networks have achieved promising performance, two issues still limit their effectiveness: insufficient feature refinement at the bottleneck stage and weak local structural representation in encoder-decoder architectures. Thus, we propose a Haze-Aware Dual-Domain Refinement Network (DDR-Net) for single-image dehazing. Our method is built upon three modules: Haze Prior Extractor (HPE) provides multi-scale haze-aware priors by operating directly on downsampled hazy images; Detail-Enhanced Blocks (DE Blocks) serve as the core feature extraction units, capturing multi-scale structural information and enhancing edge and texture recovery via gradient-aware convolutions; and Spatial-Frequency Bottleneck Refinement (SFBR) at the bottleneck jointly exploits spatial and frequency information to refine bottleneck features. DDR-Net achieves more effective feature representation and reconstruction for haze removal. Extensive experiments on real-world benchmarks demonstrate that our method outperforms existing dehazing approaches. It achieves competitive performance on synthetic datasets.

---


### 281. [AeroMELD: A Linear Embedding of Aerosol Populations for Diagnostics and Latent Dynamics](https://arxiv.org/abs/2607.11073)

**<font color=#1a73e8>作者：</font>** Ehsan Saleh, Saba Ghaffari, Wenhan Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurately representing atmospheric aerosol populations is essential for simulating aerosol-cloud interactions, radiative forcing, and ice nucleation, yet existing reduced schemes impose structural assumptions that limit their ability to capture composition diversity and mixing state. Machine-learning approaches offer more flexible representations, but standard autoencoders do not preserve the mathematical structure of aerosol populations and therefore cannot support physically meaningful process operators. We introduce AeroMELD (Aerosol Measure Embedding for Latent Dynamics), a mathematically grounded framework for constructing low-dimensional latent variables that retain this structure. We show that any permutation-invariant linear encoder must take a scale-shape decomposition, with total number concentration represented explicitly and latent shape given by a barycentric combination of per-particle embeddings. This aggregated latent state retains the diagnostic expressiveness of a Deep Sets model by moving the nonlinear post-aggregation stage into the learned diagnostic map while preserving latent linearity. Using particle-resolved data as ground truth, we encode weighted particle populations directly rather than binned aerosol states; size-resolved mass and number distributions serve only as diagnostic targets and visual summaries. The latent space accurately reconstructs these distributions, CCN spectra, optical coefficients, and immersion-freezing behavior while preserving the linear population structure needed for hybrid ML-physics models. Although the experiments focus on diagnostic reconstruction, the embedding is designed so that emissions and mixing can be represented exactly and nonlinear microphysical processes learned in a controlled latent space. This work establishes a foundation for learning aerosol-process evolution directly in latent space.

---


### 282. [Link Adaptation Using Joint-Thompson Sampling](https://arxiv.org/abs/2607.11075)

**<font color=#1a73e8>作者：</font>** Vignatha Vinjam, Manjunath Kolavennu, Myna Vajha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The choice of Modulation and Coding (MCS) type for a particular channel condition is made through link adaptation (LA) algorithms that operate at the MAC layer. These algorithms rely on the ACK/NACK statistics and the channel quality index (CQI) feedback. Several existing works model LA as a multi-armed bandit (MAB) problem across cellular and Wi-Fi links. In the MAB formulation, each available MCS is a Bernoulli arm parameterized by its transmission success probability, and the goal is to design a selection strategy that accrues maximum reward. Several popular MAB algorithms, such as upper confidence bound (UCB) and Thompson Sampling (TS), have been proposed in the literature. Using the fact that MCS success probabilities are ordered, we propose the Joint-Thompson Sampling (Joint-TS) algorithm. Unlike classical TS, which assumes independent Beta distributions for each arm, Joint-TS utilizes a multivariate ordered Beta distribution as the prior to preserve the inherent monotonicity of success probabilities. Our simulation results show that while existing MAB algorithms fail in specific scenarios, Joint-TS delivers competitive throughput with robust, consistent performance in all scenarios.

---


### 283. [Controlling Motion Transfer in Diffusion Transformers via Attention Heads](https://arxiv.org/abs/2607.11081)

**<font color=#1a73e8>作者：</font>** Sunyoung Jung, Jiwoo Park, Yoonseok Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have advanced video generation with high-quality, temporally coherent results. However, extending them to motion transfer, which requires following reference motion while aligning with a target prompt, remains challenging due to limited understanding of motion and structure representations within DiTs. We analyze video DiTs at the attention-head level and identify distinct heads specialized for motion and spatial structure. Based on this insight, we propose a head-aware controllable motion transfer framework that requires no parameter updates. Our method refines motion cues from motion-specialized heads via semantic correspondence guidance and preserves structure through selective feature injection. This head-level control not only enables accurate motion transfer but also provides an interpretable foundation for controllable video generation with DiTs.

---


### 284. [NVAITC AI Scientist: A Governed End-to-End Research System -- A Hypertension GWAS Case Study](https://arxiv.org/abs/2607.11084)

**<font color=#1a73e8>作者：</font>** Eddie Huang, Ken Liao, Iven Fu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic research systems are emerging as a new paradigm for coordinating scientific workflows beyond isolated model inference, code generation, or statistical analysis. However, deployment in institutional biomedical environments requires governed mechanisms for research planning, data access, workflow orchestration, evidence tracking, reproducibility, and human oversight. We present NVAITC AI Scientist (NAIS), a governed end-to-end agentic research system designed to support domain-general scientific workflows while keeping protected data within institutional privacy boundaries. NAIS integrates proposal review, execution planning, governed computational routing, reproducible workflow orchestration, evidence generation, and scientist-in-the-loop oversight. We validate NAIS in a real-world hypertension genome-wide association study (GWAS) using hospital-linked genotype and electronic health record (EHR) data from 286,422 individuals under an aggregate-only data policy. The agent planned cohort extraction, orchestrated GWAS execution, generated quality-control summaries, and drafted publication-oriented outputs. Human-AI review identified phenotype discrepancies and enabled iterative refinement of the hypertension definition. After reconciliation, the agent-orchestrated GWAS reproduced established hypertension loci, including FGF5, ATP2B1, CNNM2, FTO, and GRB14, with the strongest signal at FGF5 reaching $-\log_{10}(p) \sim 70$. As a secondary demonstration, NAIS also supported a drug-induced liver injury prediction workflow, achieving a multimodal graph neural network AUC of 0.842. These results demonstrate that governed agentic research systems can support scalable AI-assisted biomedical discovery while producing outputs comparable to expert-led workflows.

---


### 285. [Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability](https://arxiv.org/abs/2607.11086)

**<font color=#1a73e8>作者：</font>** Pei Chen, Baichao An, Mengying Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) has rapidly established itself as a standard interface for enabling LLM-based agents to interact with external tools and services. As MCP servers are increasingly entrusted with security-sensitive operations, understanding their real-world risks has become critical. In practice, due to the absence of large-scale runtime MCP servers, such understanding largely relies on security scanners applied to a small number of cases, yet the reliability of these assessments remains unclear.
In this study, we revisit how MCP security is measured. We present MCPZoo, the largest collection of MCP servers for dynamic analysis to date. MCPZoo is constructed through a multi-agent framework for transforming in-the-wild static repositories into dynamic services. The framework emulates how human experts build, diagnose, and iteratively repair deployment and runtime defects by combining environment inference with feedback-driven refinement. To ensure practical interactivity at runtime, the servers are validated via real protocol interactions. As a result, MCPZoo contains 64,611 unique MCP servers (113,927 in total), with more than 37,288 supporting dynamic analysis. Leveraging MCPZoo, we conduct the first ecosystem-scale measurement of MCP servers and the scanners that analyze them. While existing scanners report that 96.89% of servers are risky, we find that these signals are unreliable. In particular, manual validation shows that less than 50% of sampled alerts are true positives, and scanner outputs exhibit clear inconsistency across scanners. Overall, MCPZoo enables large-scale, reproducible measurement of MCP server security and exposes limitations of current scanning practices. We further release a public query interface to support practical risk assessment of MCP servers.

---


### 286. [CUST: Clustered Unit-level Similarity Transformer for Lightweight Image Super-Resolution](https://arxiv.org/abs/2607.11088)

**<font color=#1a73e8>作者：</font>** Jeongsoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, Vision Transformer (ViT)-based models have exhibited remarkable performance in image super-resolution. However, the quadratic computational complexity of ViTs with respect to spatial resolution severely constrains their efficiency, leading to high latency and massive memory consumption. To alleviate this, various window-based attention mechanisms have been proposed; yet, they inherently compromise the long-range dependency modeling that is the primary advantage of ViTs. To overcome these limitations, we propose the Clustered Unit-level Similarity Transformer (CUST), a novel architecture that efficiently integrates global and local information. Specifically, CUST enables each patch to aggregate and attend to similar patches within a broadened regional scope outside its local window, thereby capturing extensive contextual understanding. Furthermore, it employs overlapping attention windows to capture local dependencies, while explicitly extracting high-frequency details by computing the residual difference between the original features and their downsampled-upsampled counterparts. Comprehensive experiments demonstrate that our proposed model achieves a practical balance between computational efficiency and restoration performance. It achieves a lower memory footprint and faster inference speed compared to recent global context or lightweight models under realistic constraints. Code is available at [this https URL].

---


### 287. [Why Low-Light Cameras Go Color Blind: Removing Color Bias in Raw Denoising](https://arxiv.org/abs/2607.11090)

**<font color=#1a73e8>作者：</font>** Mohammad Mohammadi, Sina Honari, Stavros Tsogkas 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Raw images inherently suffer from noise due to the stochastic nature of light and sensor hardware imperfections. As real photon counts fall, the ratio of this noise to the signal degrades; consequently, for low-light conditions, robust denoising is especially vital for high-quality results. While recent data-driven methods achieve strong performance, they typically rely on large-scale noisy-clean image pairs that are costly and difficult to collect. Alternatively, parametric noise models can generate synthetic training data, but this necessitates precise camera calibration, which is often impractical for unknown devices. In this work, we propose a camera-agnostic, calibration-free paradigm for low-light raw denoising. We identify that color bias from black-level error is a primary source of performance degradation and causes severe color shifts. To mitigate this, we introduce a bias estimator network that predicts the black-level error as a global feature of the noisy input. We evaluate our approach across the ELD, SID, and LRID datasets, demonstrating superior performance among blind denoisers, particularly in terms of color correction. In many cases, we are competitive with-or can even surpass-methods with stronger supervision. Furthermore, we reveal that the widely used SIDD dataset contains significant color bias in its ground-truth images, which yields unrealistic color reproduction in trained models. We introduce a new ground-truth extraction framework to resolve this issue and provide a benchmark of existing methods on the corrected dataset.

---


### 288. [Adapting Evidential Neural Networks to Test-Time Neighbor Fusion Improves Molecular Property Prediction](https://arxiv.org/abs/2607.11091)

**<font color=#1a73e8>作者：</font>** Cameron Gruich, Weichi Yao, Yixin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A trained molecular property model can be refined at test time by correcting each prediction with the measured labels of the most similar training molecules, a retraining-free procedure we call neighbor fusion; evidential neural networks make it principled by using their aleatoric and epistemic uncertainty to parameterize a Bayesian update. Our main contribution, PG-EVIKAL, learns a property-distance metric to re-rank structurally similar neighbors by their property relevance before fusion, building on EVIKAL (scalar Kalman filter) and GP-EVIKAL (Gaussian process variant handling correlated neighbors). Evaluated on 16 molecular datasets, PG-EVIKAL reduces RMSE relative to the evidential model baseline on 14 of them, with a median reduction of 19.4%, and improves calibration; in sequential-assay scenarios it further incorporates newly measured molecules, refining predictions as they arrive without retraining. This work demonstrates that evidential uncertainty decomposition is not merely a calibration objective but an actionable inference resource that enables test-time refinement of molecular property predictions.

---


### 289. [Multi-dimensional training-priority weighting based on physical information propagation paths: a unified residual-weighting framework for physics-informed neural networks](https://arxiv.org/abs/2607.11094)

**<font color=#1a73e8>作者：</font>** Zhangyi Lian, Xinda Dong, Wenxuan Huo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) have shown promise for solving partial differential equations (PDEs); however, their synchronous optimization treats residuals of different regions and constraints equally, which is inconsistent with the progressive "from source to response" physical information propagation path, degrading training stability and accuracy. Existing causal training methods focus mainly on the temporal dimension, lacking a unified characterization of spatial and boundary dimensions. To address this, we define a unified class of training priorities according to the physical information propagation path: premise regions should be learned before dependent regions; temporal, spatial, and boundary priorities are instances of this principle. Using neural tangent kernel (NTK) dynamics, we theoretically analyze why standard PINNs do not obey this priority: their residual convergence order is governed by the NTK spectrum and is independent of the propagation path. Accordingly, we propose a unified multi-dimensional priority-constraint framework that partitions the domain along the propagation path and constructs negative-exponential residual weights, converting the physical propagation order into a training priority. For cases with coexisting priorities, we introduce a directional compatibility coefficient to clarify that "orthogonal directions can be coupled multiplicatively in synergy, whereas coaxial opposite directions cannot." Benchmark cases show that this method consistently improves the convergence behavior and prediction accuracy of PINNs on problems with clear propagation paths or constraint-dominated structures, without modifying the network architecture and with controllable additional computational cost.

---


### 290. [Difference-Driven Gating: Adaptive Feature Fusion for U-Net Decoder](https://arxiv.org/abs/2607.11096)

**<font color=#1a73e8>作者：</font>** Kai Li, Xuechao Zou, Jiashen Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The U-Net style models have been widely used in many applications. A critical step in these models is to reconstruct the lower-level features using a top-down decoder. This reconstruction requires precise fusion of high-level semantics and low-level details. Existing attention-based fusion methods typically derive attention weights from the top-down decoder features (global) alone or the correlation between the top-down decoder features and the bottom-up encoder features (local), then modulate the encoder features using these weights. In this work, we explore a different paradigm: deriving attention weights from the difference between the two feature streams. To this end, we propose two difference-based gating approaches: Feature-difference gating (FDG), which directly uses the absolute difference between global and local features to generate adaptive gating maps, and Entropy-difference gating (EDG), which measures the representational certainty of each stream via information entropy and uses their signed entropy difference to derive the attention weights. Both methods produce coupled gating maps that simultaneously modulate the global and local features. Experiments on different tasks including medical image segmentation, remote sensing image cloud removal and speech separation showed that both methods outperformed existing attention-based fusion methods, and EDG performed better. The results suggested a new paradigm for multi-scale feature fusion in the U-Net style structures.

---


### 291. [Revisiting Matching Response and Swept Feature Volumes for Wide-baseline Omnidirectional Stereo](https://arxiv.org/abs/2607.11097)

**<font color=#1a73e8>作者：</font>** Seungjin Jeon, Jongwoo Lim, Changhee Won  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a training strategy for confidence estimation in omnidirectional stereo, targeting the ambiguous matches that frequently occur in wide-baseline setups. Reinterpreting the matching responses produced by the 3D encoder decoder block, we show that their expectation values provide intrinsic confidence signals. Building on this, our method directly penalizes ambiguous responses without auxiliary heads, multi-pass inference, or additional modules, resulting in more efficient and generalized predictions. Beyond confidence, we introduce swept feature volume resampling, where response features produced by 3D CNNs are resampled using regressed positive matching indices and then processed by 2D CNNs to predict meta-information such as surface normals. This joint learning introduces auxiliary geometric regularization and improves depth coherence by leveraging additional contextual cues during response aggregation stage. Experimental results demonstrate that our approach enhances both confidence estimation and surface normal prediction while maintaining deployment practicality for autonomous mobility applications.

---


### 292. [FlowPET: Physics-Informed Symplectic Flow Matching for Low-Count PET Reconstruction](https://arxiv.org/abs/2607.11104)

**<font color=#1a73e8>作者：</font>** Zheng Zhang, Hao Tang, Yingying Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-count Positron Emission Tomography (PET) reconstruction is severely hindered by the dissipative nature of prevailing generative models, where the inherent phase-space contraction leads to the numerical extinction (``wash-out'') of weak but diagnostically critical lesion signals. To overcome this geometric limitation, we propose \textbf{FlowPET}, a physics-informed framework that reformulates reconstruction as volume-preserving transport in a symplectic phase space. By parameterizing the posterior dynamics via a Separable Hamiltonian System, our approach guarantees a divergence-free vector field by construction, theoretically immunizing weak signals against probability mass collapse. To steer this conservative flow, we introduce conjugate boundary conditions based on the Range-Null space decomposition of the PET operator; this strictly enforces data consistency in the range space while confining stochastic uncertainty injection to the unobserved null space. We train the model via symplectic flow matching and perform inference using a symplectic leapfrog integrator. Extensive experiments on BrainWeb, clinical pediatric, and UDPET datasets demonstrate that \textbf{FlowPET} not only surpasses state-of-the-art deterministic and stochastic baselines in SSIM and PSNR but, more crucially, exhibits superior recovery of low-contrast lesions. The results confirm that imposing Hamiltonian structural constraints offers a robust geometric safeguard for medical inverse problems in high-noise regimes.

---


### 293. [A Novel Graph Fraud Detector via Grouped Attribute Completion and Confidence-Aware Contrastive Learning](https://arxiv.org/abs/2607.11107)

**<font color=#1a73e8>作者：</font>** Junpeng Wu, Ye Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph fraud detection plays a pivotal role in safeguarding the security and integrity of modern digital ecosystems. Graph Neural Networks (GNNs) are commonly adopted for graph fraud detection. However, the practical performance of existing GNN-based detectors is severely hindered by incomplete node attributes and extreme class imbalance within graphs. To mitigate these limitations, this paper proposes a novel framework for Graph Fraud Detection with Grouped attribute completion and Confidence-aware Contrastive learning, named GFD-GC. Specifically, it first imitates heterogeneous neighborhood structures to implement group-wise aggregation, which obtains informative complete node features by capturing fine-grained graph contextual patterns. Further, it introduces a confidence-aware supervised contrastive learning strategy to augment scarce labeled fraud nodes with high confidence pseudo-fraud nodes, which enhances the compactness of fraud representations and their separability from non-fraud nodes. Extensive experiments demonstrate the superiority of the proposed GFD-GC over state-of-the-art baselines on the graph fraud detection task, thereby providing an effective solution for real-world fraud scenarios.

---


### 294. [Neural Discovery of Memory and Nonlocal Kernels in Integro-Differential Equations with Constrained Kolmogorov--Arnold Networks](https://arxiv.org/abs/2607.11110)

**<font color=#1a73e8>作者：</font>** Aruzhan Tleubek, Salah A Faroughi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discovering the memory or nonlocal kernel governing an integro-differential equation (IDE) from sparse and noisy observations is an ill-posed inverse problem. Existing identification methods often rely on problem-specific analytical derivations, specialized observation requirements, or restrictive assumptions about the kernel, limiting their applicability across different classes of IDEs. In this work, we propose a differentiable-solver-based framework for discovering memory and nonlocal kernels directly from spatiotemporal observations. Within the solver, the unknown kernel is represented using a constrained Kolmogorov--Arnold Network (KAN) parameterization, with the physical constraints imposed through two different approaches: a Bernstein-polynomial-based Monotone--Convex KAN (MC-KAN), whose coefficient constraints enforce positivity, monotonic decrease, and convexity by construction, and a Chebyshev-based KAN (Cheb-KAN), in which the same properties are encouraged through soft penalty terms. After training, symbolic regression is applied to the learned kernels to obtain interpretable closed-form representations. We evaluate both methods on benchmarks spanning a one-dimensional Volterra equation, a one-dimensional viscoelastic wave partial integro-differential equation, and a two-dimensional nonlocal reaction-diffusion equation with an anisotropic coupled kernel. For the 1D problems, both methods recover the correct kernel functional form and achieve comparable solution-reconstruction accuracy. In contrast, for the sparse and noisy 2D nonlocal problem, the hard-constrained MC-KAN consistently achieves lower kernel reconstruction errors than the soft-constrained Cheb-KAN. Our results demonstrate that enforcing physically motivated shape constraints by construction provides greater robustness than soft penalties for multidimensional kernel discovery from sparse and noisy observations.

---


### 295. [CA-DGCL: Dynamic Graph Continual Learning via Condensation and Attachment](https://arxiv.org/abs/2607.11112)

**<font color=#1a73e8>作者：</font>** Tingxu Yan Ye Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic graph continual learning (DGCL) is an effective manner for handling catastrophic forgetting in dynamic graphs. However, existing DGCL methods underutilize temporal information across graph snapshots. To address this critical issue, we propose a novel framework for Dynamic Graph Continual Learning via Condensation and Attachment (CA-DGCL). Specifically, CA-DGCL first condenses historical graph snapshots into compact semantic representations efficiently. Further, a cross-timestamp node chains is built to construct a third-order tensor and Tucker decomposition is applied to this tensor for obtaining stable node features, which encapsulate historical knowledge. Finally, these node features are used to generate new nodes and attached to the current graph for replaying of past information without compromising the new patterns. In addtion, a refined forgetting measure is introduced to make it more suitable for dynamic graph settings. Extensive experiments demonstrate that CA-DGCL outperforms baselines in forgetting suppression as well as maintain competitive accuracy, proving its efficacy for dynamic graph continual learning.

---


### 296. [The Equilibrium Is the Initialization: Lazy Identity Collapse in Physics-Structured Deep Equilibrium Reasoning](https://arxiv.org/abs/2607.11116)

**<font color=#1a73e8>作者：</font>** Joyjeet Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep equilibrium models promise input-adaptive implicit computation: harder problems should demand more solver iterations, and the solved equilibrium should encode the result of genuine iterative inference. We report a cautionary study of a port-Hamiltonian DEQ with a learned initialization on two reasoning tasks -- ProofWriter entailment over frozen DeBERTa embeddings and a BFS-verified graph-reachability benchmark -- in which the implicit computation is a silent no-op. Across tasks, seeds, and controlled ablation arms, the solved equilibrium equals the solver's start point to numerical precision, and bypassing the solver entirely changes test accuracy by +0.00 percentage points in 18 of 19 training runs. Controlled interventions falsify the tempting explanation: removing the anchoring term reproduces every result, and retraining with noise-decoupled starts yields a solver that converges to the noisy start while the decoder learns to ignore it. The single escaping run diverges instead ($\|h^{*}-z_0\|=171$), producing a co-adapted noise channel whose removal improves accuracy. Iteration counts are uncorrelated with ground-truth difficulty ($r=0.009$), and the full apparatus never outperforms a two-layer MLP on either task. We trace the mechanism to gradient starvation along two distinct routes, show that the standard zeroing ablation is confounded and gives wildly seed-dependent answers where the correct substitution test gives a stable zero, and distill a four-test diagnostic protocol for auditing claimed implicit computation. All experiments run on a single free Colab GPU; code, raw logs, and analysis scripts are released.

---


### 297. [GHOST: Geometry-Guided Hallucination of Opaque Surface Textures](https://arxiv.org/abs/2607.11118)

**<font color=#1a73e8>作者：</font>** Langxu Zhao, Zuan Gu, Tianhan Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transparent objects pose a fundamental challenge for depth estimation and 3D reconstruction due to their violation of Lambertian assumptions, leading to severe geometry degradation in downstream tasks. To address this, we propose a novel geometry-guided preprocessing framework \textbf{GHOST} that leverages visual foundation models to transform transparent regions into opaque, structurally consistent representations without requiring downstream model retraining. Specifically, our pipeline utilizes (1) \textbf{TransDINO} and (2) \textbf{TransDecomp} to disentangle masks and transparency physical properties, while (3) \textbf{DAF-Net} recovers surface normal priors to encode geometric curvature. Subsequently, (4) \textbf{GeoSemTransNet} integrates these multi-modal cues to synthesize a texture-rich opaque RGB image that preserves the transparent object's 3D structure. Extensive experiments demonstrate that our method significantly enhances the accuracy of state-of-the-art depth estimation and reconstruction models on transparent objects by restoring essential photometric cues.

---


### 298. [Simple Features and Honest Calibration for Ambivalence and Hesitancy Recognition in Video](https://arxiv.org/abs/2607.11120)

**<font color=#1a73e8>作者：</font>** Vikas Kumar, Aditya Mishra, Haroon R. Lone  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address ambivalence and hesitancy (A/H) recognition in the ABAW 2026 BAH Challenge: given a short interview video, predict whether the person shows signs of A/H. Our system combines affect-specialised text, audio, and visual representations with a small set of readable linguistic hesitation cues, fused by a reliability gate we call Affective Marker Fusion (AMF), and finished with a simple AP-weighted ensemble at a fixed decision threshold. We also introduce \emph{ASR-erased time}: speech recognisers delete fillers and hesitation pauses from the transcript, but the chunk timestamps keep the time those events took, and sixteen features built from these gaps form the strongest and most independent non-verbal channel we measured (AP $0.718$, correlation $0.11$--$0.36$ with all other members). Across controlled experiments we find three things: cross-modal conflict design does not reliably help on BAH; language is by far the strongest channel while affect-specialised audio is a useful second; and calibration matters more than architecture. Fitting ensemble weights and a threshold on the small validation split overfits: it scores $0.741$ macro-F1 on validation but only $0.690$ on the untouched test set. AP-weighting at a fixed threshold instead reaches $\mathbf{0.731}$ on test.

---


### 299. [Learning Subgroup Relations Using Siamese Graph Neural Networks](https://arxiv.org/abs/2607.11140)

**<font color=#1a73e8>作者：</font>** Tal Weissblat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Determining whether one finite group is isomorphic to a subgroup of another is a fundamental problem in computational group theory. In this work, we propose a Siamese Graph Neural Network (Siamese GNN) for subgroup prediction using Cayley graph representations of finite groups. Each input group is represented by its undirected Cayley graph and encoded by one branch of a Siamese GNN to produce a graph embedding. The resulting graph embeddings are combined with algebraic features derived directly from the input groups to construct a joint feature vector, which is processed by a fully connected classifier to predict subgroup relations between finite groups. By integrating graph-based structural representations with algebraic features, the proposed framework provides a unified approach for learning subgroup relations from finite groups. Experimental results demonstrate the effectiveness of the proposed architecture, achieving a test accuracy of 95.9% (47/49) on an independent test set and illustrating the potential of geometric deep learning for subgroup prediction.

---


### 300. [Rank-Conditioned Sample Reuse for the Plackett--Luce Best-of-$K$ Objective](https://arxiv.org/abs/2607.11146)

**<font color=#1a73e8>作者：</font>** Melveena Jolly, Midhun Xavier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the coupled objective J_K^WOR = E_{S ~ PL-WOR_K}[max_{i in S} R_i]: the expected maximum reward of a size-K Plackett-Luce draw without replacement, the law of Gumbel-Top-K / Stochastic Beam Search decoding. This estimand differs from the conventional i.i.d. objective J_K^iid = E[max_{i<=K} R_i] targeted by existing sample-reuse Max@K estimators, and reusing their i.i.d. weights under the coupled sampler is provably biased (a closed-form three-item instance gives E[g_iid] = (4/5) grad J_K^WOR exactly; pass@K under the coupled sampler is the binary-reward special case). Generic joint-score REINFORCE is already unbiased for J_K^WOR; what it lacks is sample reuse. Our contribution is to instantiate standard rank-conditioned Horvitz-Thompson estimation for the J_K^WOR subset total: from one Gumbel-Top-n pool (n>K) and its observed priority threshold we build an estimator that reuses all C(n,K) embedded K-subsets, unbiased with an unbiased exact score-function surrogate gradient, plus a reward-sorted Max-specific dynamic program that collapses the C(n,K)-term subset sum (with K!-cost set probabilities) exactly to a one-dimensional integral. A fixed-Q quadrature evaluation costs O(n log n + nKQ) arithmetic and is numerically, not algebraically, exact; no epsilon-approximation rate is certified. Each nonzero degree-K Horvitz-Thompson term has finite second moment exactly when n >= 2K; under the same assumptions the full surrogate gradient has finite second moment whenever n >= 2K (sharpness there is open). At K=1 the construction recovers classical priority sampling. All quantities require only the values and differentiable computation graphs of the n+1 drawn items' probabilities, so finite structured sequence policies sampled by exact SBS are covered. A certified finite-Q quadrature bound and countably infinite support remain open. Validation code is included as ancillary files.

---


> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-420](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
