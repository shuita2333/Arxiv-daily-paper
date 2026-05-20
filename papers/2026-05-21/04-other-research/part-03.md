# 📦 其他研究 | 2026年05月21日

> 本类共 **338** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-338](./part-07.md)

---

### 101. [How Far Are We From True Auto-Research?](https://arxiv.org/abs/2605.19156)

**<font color=#1a73e8>作者：</font>** Zhengxin Zhang, Ning Wang, Sainyam Galhotra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent auto-research systems can produce complete papers, but feasibility is not the same as quality, and the field still lacks a systematic study of how good agent-generated papers actually are. We introduce ResearchArena, a minimal scaffold that lets off-the-shelf agents (Claude Code using Opus 4.6, Codex using GPT-5.4, and Kimi Code using K2.5) carry out the full research loop themselves (ideation, experimentation, paper writing, self-refinement) under only lightweight guidance. Across 13 computer science seeds and 3 trials per agent-domain pair, ResearchArena yields 117 agent-generated papers, each evaluated under three complementary lenses: a manuscript-only reviewer (SAR), an artifact-aware peer review (PR) in which agents inspect the workspace alongside the manuscript, and an human conducted meta-review. Under SAR alone the picture is optimistic: Claude Code obtains the highest score, outperforms Analemma's FARS, and matches the weighted-average human ICLR 2025 submission, suggesting that minimally scaffolded agents can produce papers that look competitive on manuscript-only review. Manual inspection, however, reveals this picture is overstated: SAR scores are poorly aligned with its actual acceptance decisions and reward plausible framing without verifying experimental substance. Under artifact-aware PR scores drop sharply, and manual auditing identifies experimental rigor as the major bottleneck, decomposing into three failure modes (fabricated results, underpowered experiments, and plan/execution mismatch) that are highly agent-dependent: Codex 5%/8% paper-vs-artifact mismatch / fabricated references versus Kimi Code 77%/72%, a $\sim$15$\times$ spread that tracks distinct research personas the agents develop. None of the 117 agent-generated papers reaches the acceptance bar of a top-tier venue. This suggests that we are still gapped from the true auto-research.

---


### 102. [On the Geometric Limits of Transformer Defenses against Obfuscation Attacks: Latent Embedding Collapse & Performance Robustness Gap](https://arxiv.org/abs/2605.19159)

**<font color=#1a73e8>作者：</font>** Becky Mashaido, Tapadhir Das  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection attacks pose significant risks to language model safety, yet existing defenses are typically evaluated using classification performance. We show that high detection performance does not imply representational robustness. Specifically, multi-operator obfuscated prompts (combining homoglyphs, zero-width characters, and punctuation or emoji noise) can partially collapse onto the embedding manifold of clean prompts, a phenomenon we term latent embedding collapse. Results indicate that across multiple BERT family encoders with varying depth and capacity, detectors achieve near-perfect classification performance, yet the minimal clean-obfuscated margin delta = 1.02, indicating near-overlap of obfuscated and clean embeddings. Obfuscated embeddings further exhibit elevated intra-class variance (3.33 +/- 6.23), indicating severe latent-space instability despite high performance. These results reveal a substantial perf ormance-robustness gap, demonstrating that standard evaluation metrics fail to capture latent embedding collapse and underlying geometric fragility. Our findings show that increasing model capacity does not eliminate latent embedding collapse, motivating geometry-aware robustness analysis as a necessary complement to performance-based evaluation for prompt-injection defenses.

---


### 103. [Bridge: Retrieval-Augmented Spatiotemporal Modeling for Urban Delivery Demand](https://arxiv.org/abs/2605.19172)

**<font color=#1a73e8>作者：</font>** Yihong Tang, Tong Nie, Junlin He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting urban delivery demand becomes substantially more challenging when newly added service regions lack historical records. Existing spatiotemporal forecasters effectively model spatial dependence once sufficient node histories are available. Still, they remain parametric and therefore struggle to recover short-term operational dynamics in cold-start regions. Geospatial embeddings help identify where a region is and what function it serves, yet they do not directly reveal how a similar region behaves under a comparable temporal context. We propose Bridge, a retrieval-augmented spatiotemporal graph framework that combines an inductive contextual graph backbone with a time-aware memory of region-time windows. For each target region, Bridge retrieves future demand patterns from the memory using both regional context and recent dynamics, and refines the backbone forecast through a gated fusion mechanism. To align retrieval with forecasting utility, we further train the retriever with a future-aware objective that favors entries whose future trajectories best match the target. Experiments on four real-world delivery datasets show that Bridge consistently improves over competitive spatiotemporal baselines in both within-city cold-start and cross-city transfer with partial observations. The results show that retrieval augmentation provides a useful operational memory for cold-start urban demand forecasting when parametric graph generalization alone is insufficient.

---


### 104. [Planner-Admissible Graph-PDE Value Extensions for Sparse Goal-Conditioned Planning](https://arxiv.org/abs/2605.19185)

**<font color=#1a73e8>作者：</font>** Shiheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse goal-conditioned planning with few cost-to-go labels can be viewed as a graph-PDE Dirichlet extension problem: extend sparse labels on a goal-dependent boundary to unlabelled graph vertices so that greedy rollouts reach the goal. We study which graph value extensions are planner-admissible under the operational argmin-Q planner. Our main result is a local action-gap certificate: if the surrogate value error along the rollout stays below half the true action gap, then the greedy rollout reaches the goal. Absolutely Minimal Lipschitz Extension (AMLE), the p=infinity endpoint of the graph p-Laplacian family, instantiates this certificate through a comparison-principle fill-distance bound. Harmonic extension, by contrast, can mis-rank local actions because its values reflect boundary hitting probabilities rather than shortest-path greedy order.
On 120 AntMaze layout-derived graph configurations, harmonic extension achieves 0.584 aggregate rollout success, while AMLE reaches 0.970. Finite high-p methods also enter a high-success regime, with success 0.903 for p=4, 0.973 for p=8, and 0.982 for a fixed-budget p=16 solver, though the p=16 row is not used as a converged endpoint ranking due to incomplete solver certification. Mechanism audits show that many rollout decisions occur in AMLE-compatible but harmonic-incompatible local geometry, and that AMLE corrects most harmonic inversions on the rollout-weighted decision scope.

---


### 105. [MMoA: An AI-Agent framework with recurrence for Memoried Mixure-of-Agent](https://arxiv.org/abs/2605.19194)

**<font color=#1a73e8>作者：</font>** Rui Chu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Mixture-of-Agents (MoA) framework has shown promise in improving large language model (LLM) performance by aggregating outputs from multiple agents. However, existing MoA systems often rely on static routers that do not fully capture temporal and contextual dependencies across aggregation layers. To address this limitation, we propose MMoA, a recurrent MoA architecture that integrates LSTM-based gating into the agent selection process. The recurrence router adaptively modulates agent contributions based on both current inputs and historical routing decisions, enabling more context-aware aggregation. We evaluate MMoA on standard instruction-following benchmarks, including AlpacaEval 2.0, MT-Bench, and Arena-Hard. The results show that MMoA achieves comparable accuracy to traditional MoA while reducing computational overhead by dynamically activating fewer agents. For example, on AlpacaEval 2.0, MMoA achieves a win rate of 58.0%, compared with 59.8% for MoA, while improving runtime efficiency by up to 4.6%. These results suggest that MMoA provides a scalable and efficient approach for adaptive multi-agent LLM systems.

---


### 106. [On-Device Continual Learning with Dual-Stage Buffer and Dynamic Loss for Point-of-Care Pneumonia Diagnosis](https://arxiv.org/abs/2605.19201)

**<font color=#1a73e8>作者：</font>** Danu Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models detect pneumonia from chest X-rays with high accuracy, but the performance declines under domain shifts caused by differences in devices, patients, or institutions. We present PneumoNet, a domain-incremental learning method for point-of-care pneumonia diagnosis in resource-limited settings. PneumoNet combines a lightweight CNN for on-device prediction, a dual-stage balanced buffer for class-balanced replay, and a dynamic class-weighted loss to correct training-batch imbalances. Evaluated on a domain-shifted PneumoniaMNIST dataset simulating five realistic domain change scenarios, PneumoNet achieves 86.6% accuracy with 1.4% forgetting while being smaller and faster than existing baselines. These results highlight PneumoNet's potential to enable adaptive, privacy-preserving diagnostic AI directly on point-of-care medical devices in real-world and pandemic-ready healthcare.

---


### 107. [Quantized Machine Learning Models for Medical Imaging in Low-Resource Healthcare Settings](https://arxiv.org/abs/2605.19207)

**<font color=#1a73e8>作者：</font>** Sumanth Meenan Kanneti, Aryan Shah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models have shown strong performance in medical image analysis, but deploying them in low-resource clinical environments remains difficult due to computational, memory, and power constraints. This paper presents a multi-strategy compression framework for brain tumor classification from MRI, encompassing quantization-aware training, knowledge distillation from a DenseNet-101 teacher to a compact DenseNet-32 student with low-bit post-training quantization, and Float16 post-training quantization on a lightweight MobileNetV2 backbone.
Using a multi-class brain tumor MRI dataset containing glioma, meningioma, pituitary tumors, and healthy controls, we provide full experimental validation of the MobileNetV2-based pipeline, training the classifier through a three-stage transfer learning process and applying Float16 quantization via TensorFlow Lite. The DenseNet-based distillation and quantization-aware training strategies are described as complementary compression approaches within the framework, with their complete empirical evaluation reserved for future work.
Experimental results on the MobileNetV2 pipeline show that the quantized model achieves 82.37 percent validation accuracy compared to the 82.20 percent full-precision baseline, reducing model size from 35.34 MB to 5.76 MB, a 6.14x compression ratio with no meaningful accuracy loss. Per-class evaluation confirms that quantization preserves diagnostic performance uniformly across all four tumor categories. These findings demonstrate that lightweight quantized models can deliver clinically viable brain tumor screening in resource-constrained healthcare settings.

---


### 108. [D-Convexity: A Unified Differentiable Convex Shape Prior via Quasi-Concavity for Data-driven Image Segmentation](https://arxiv.org/abs/2605.19210)

**<font color=#1a73e8>作者：</font>** Shengzhe Chen, Hao Yan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convexity is a fundamental geometric prior that underlies many natural and man-made structures, yet remains challenging to impose effectively in end-to-end trainable segmentation networks. We revisit convexity from a functional perspective and propose a unified, threshold-free convexity prior based on the quasi-concavity of the network's output mask function u. Instead of constraining a single binary segmentation, we require all super-level sets of u to be convex, transforming global shape constraints into local, differentiable inequalities on u and its derivatives. From this principle, we derive zero, first, and second-order characterizations, yielding respectively a local midpoint convexification algorithm, a gradient-based condition linked to supporting hyperplanes, and a sufficient second-order inequality expressed as a quadratic form on the tangent plane. The first and second-order formulations produce a compact convolutional loss that can be densely applied across the image without thresholding. Our quasi-concavity losses integrate seamlessly with modern segmentation networks via the proposed convex gradient projection module (CGPM). They consistently enforce convexity and improve shape regularity across multiple datasets, outperforming networks tailored for retinal segmentation and surpassing previous shape-aware methods. Remarkably, our analysis unifies a wide spectrum of previous convex shape models, from discrete 1-0-1 line constraints and graph-cuts convexity formulations to curvature or signed distance Laplacian based level-set priors, within a single continuous and differentiable framework.

---


### 109. [Smartphone-based Circular Plot Sampling for Forest Inventory](https://arxiv.org/abs/2605.19213)

**<font color=#1a73e8>作者：</font>** Su Sun, Jui-Cheng Chiu, Nabin Khanal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Circular sample plots are a cornerstone of forest inventory, yet accurate measurement of tree diameter at breast height (DBH) and spatial location within such plots remains challenging. Conventional approaches rely either on costly terrestrial LiDAR systems or labor-intensive manual methods involving calipers and compass bearings, limiting their scalability and accessibility in large scale environments. We present a lightweight, smartphone-based pipeline that enables complete plot sampling based tree measurement from a single walkthrough video, requiring no specialized hardware beyond a consumer smartphone mounted on a portable stand. The proposed method integrates pretrained monocular depth estimation and tree instance segmentation with a simultaneous localization and mapping (SLAM) framework to jointly refine camera trajectories and depth across the video sequence. Tree positions and DBH estimates are recovered by fusing SLAM-derived camera poses with segmented depth maps, with absolute real-world scale anchored via a calibrated reference length.
The system was evaluated in both managed forest plots and natural forest plot, achieving a mean absolute error of 1.51 cm (MARE 3.98%) and 2.30 cm (MARE 5.69%) respectively, with consistent performance across varying starting directions and positions. Cross-video consistency analysis further demonstrated stable and reproducible tree localization across measurements initiated from different starting positions. The proposed approach achieves accuracy comparable to established field methods while substantially reducing equipment cost and operational complexity, making it accessible to both professional researchers and non-expert forest managers in diverse operational settings.

---


### 110. [Worst-Group Equalized Odds Regularization for Multi-Attribute Fair Medical Image Classification](https://arxiv.org/abs/2605.19214)

**<font color=#1a73e8>作者：</font>** Nikhil Cherian Kurian, Victor Caquilpan Parra, Abin Shoby 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diagnostic performance in medical AI varies systematically across demographic groups, yet subgroup AUC can mask clinically important disparities. At a fixed inference-time operating point, some groups may exhibit over-diagnostic behaviour, characterized by elevated true and false positive rates, while others show under-diagnostic patterns with reduced true and false positive rates. These opposing tendencies can cancel in aggregate AUCs while producing meaningful inequities in clinical decision-making. Motivated by the need to assess and mitigate such disparities at the operating point and across multiple demographic attributes simultaneously, we propose a worst-group equalized-odds margin regularizer. The proposed regularizer explicitly targets subgroup-level deviations on both the true positive and false positive sides at inference. At each update, the method identifies subgroups defined by explicit demographic attributes (e.g., age, sex, and race) that exhibit the most extreme margin deviations and applies a unified penalty, enabling fairness optimization across multiple demographic axes without requiring explicit intersectional constraints. Across two medical imaging datasets in realistic multi-label settings, our method consistently reduces disparities in Equalized Odds and Equalized Opportunity with minimal impact on AUC, preserving diagnostic performance while improving fairness.

---


### 111. [Not all uncertainty is alike: volatility, stochasticity, and exploration](https://arxiv.org/abs/2605.19215)

**<font color=#1a73e8>作者：</font>** Payam Piray  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adaptive decision-making in biological and artificial intelligence requires balancing the exploitation of known outcomes with the exploration of uncertain alternatives. Although prior work suggests that uncertainty generally promotes exploration, it has typically treated distinct sources of environmental uncertainty as equivalent. We consider environments with latent reward states that drift over time (volatility) and are observed through noisy outcomes (stochasticity). Both increase posterior uncertainty, yet we show they drive optimal exploration in opposite directions: volatility enhances it, stochasticity suppresses it. We establish this asymmetry formally by extending the Gittins index framework to Gaussian state-space bandits with latent dynamics. We further derive Cause-Aware Uncertainty-Sensitive Exploration (CAUSE), a closed-form exploration bonus obtained via control-as-inference that inherits the same monotonicities. CAUSE outperforms standard exploration strategies in environments with heterogeneous noise structure, and also improves on a Gittins-per-arm policy whose rested-bandit optimality does not transfer to restless settings. Learning and exploration are governed by the same noise-inference asymmetry, and the framework predicts that pathological noise inference produces \emph{reversed} rather than merely impaired exploration, with implications for computational accounts of psychiatric conditions.

---


### 112. [Token by Token, Compromised: Backdoor Vulnerabilities in Unified Autoregressive Models](https://arxiv.org/abs/2605.19227)

**<font color=#1a73e8>作者：</font>** Tobias Braun, Jonas Henry Grebe, Hossein Shakibania 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Unified autoregressive models (UAMs) are transformer models that generate text as well as image tokens within a single autoregressive pass. Shared parameters and a multimodal vocabulary simplify the training pipeline and facilitate flexible multimodal generation, yet might introduce new vulnerabilities. In particular, we are the first to show that this unified architecture enables multimodal backdoor attacks, where a trigger can propagate malicious effects across multiple output modalities. Specifically, we present the Token by Token Backdoor Attack (ToBAC), the first backdoor attack targeting UAMs, exploring both data-based and model-based poisoning strategies. We demonstrate that innocuous characters or even common words can be transformed into triggers that elicit harmful behavior in autoregressive image generation. ToBAC can jointly manipulate visual outputs and accompanying text, increasing the perceived authenticity of fabricated content. With model access, ToBAC enables attacks on the unified Liquid model in which a subtle word (e.g., ``cool'') induces modality-aligned brand promotion or ideological influence in 55% of generations. Without model access, ToBAC can be induced through data poisoning, achieving an average success rate of 63.1% against JanusPro.

---


### 113. [Robust Mitigation of Age-Dependent Confounding Effects via Sample-Difficulty Decorrelation](https://arxiv.org/abs/2605.19230)

**<font color=#1a73e8>作者：</font>** Nikhil Cherian Kurian, Victor Caquilpan Parra, Abin Shoby 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Age dependent performance disparities in medical image classification often arise because age acts as a confounder, linking imaging morphology with disease prevalence. In practice, disparities can manifest as overdiagnosis at ages where disease prevalence is higher and underdiagnosis at ages where prevalence is lower, and can worsen under train test shifts in the age distribution. Conventional mitigation approaches that enforce strict age invariance may suppress diagnostically meaningful information encoded in age. We therefore propose a robust framework that mitigates the effects of age-dependent confounding by targeting spurious age linked trends rather than enforcing invariance. Following a warm-up phase, we characterize sample difficulty and model its age-dependent trends in a label-conditioned manner. We decorrelate age from dominant age difficulty trends using robust, Huber weighted affinity weights, attenuating confounding-driven shortcuts while preserving clinically meaningful, nonlinear age information. We further introduce an Age Coverage Score that scales the decorrelation penalty by minibatch age variance to ensure stable optimization under limited age diversity. Across two radiology datasets, our approach reduces age dependent true and false positive disparities with minimal AUC impact and remains robust to increasing train test age distribution shifts.

---


### 114. [DeRegiME: Deep Regime Mixtures for Probabilistic Forecasting under Distribution Shift](https://arxiv.org/abs/2605.19231)

**<font color=#1a73e8>作者：</font>** Kieran Wood, Stefan Zohren, Stephen J. Roberts  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce DeRegiME -- Deep Regime Mixture of Experts -- a direct multi-horizon probabilistic forecaster that separates latent uncertainty regimes from the underlying signal and softly assigns each forecast location to learned recurring regimes using a sparse variational Gaussian process (GP) whose nonstationary regime-mixing kernel and Student-t likelihood combine per-regime sub-kernels and noise processes via a shared gate. This yields a single sparse-GP posterior, not a mixture of GP experts. DeRegiME addresses a key limitation of neural forecasters: point forecasts discard residual uncertainty, and probabilistic heads -- whether single marginals, uninterpreted mixtures, quantile sets, or diffusion samples -- rarely expose the regime structure of the residual. Yet distribution shift in noisy heteroskedastic time series may be abrupt, gradual, or horizon-dependent and often appears in residual uncertainty rather than the conditional mean. DeRegiME yields an interpretable mean-residual-noise decomposition with a direct-sum feature-space representation that anchors regimes as clusters of residual similarity whose transitions surface as implicit changepoints. The effective number of regimes is pruned by the stick-breaking gate. We prove kernel validity and predictive-density propriety, and across ten benchmarks and three encoder grids DeRegiME improves negative log predictive density (NLPD) by 20.3% over the strongest encoder-matched baseline, a DeepAR/GluonTS-style dynamic Student-t head, with parallel gains on CRPS (3.0%) and MSE (4.7%). Improvements are consistent across all datasets, which span abrupt, gradual, and seasonal shifts.

---


### 115. [Devilray: A Systematic Adversarial Model Revealing Blind Spots in Fake Base Station Detection](https://arxiv.org/abs/2605.19232)

**<font color=#1a73e8>作者：</font>** Taekkyung Oh, Duckwoo Kim, Hansung Bae 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fake Base Station (FBS) detection has been a critical focus of cellular security research for over two decades. However, significant financial and regulatory barriers to accessing commercial FBS (C-FBS) devices have limited direct visibility into real-world operations, forcing detection systems to be designed and evaluated around self-built prototypes. In this paper, we present Devilray, a reconfigurable and reference-grade adversarial baseline designed to systematically explore the realistic adversarial space and identify adversarial blind spots in current detection -- regions of realistic adversarial behavior excluded by prevailing threat models. We establish an empirical ground truth through the first academic analysis of a C-FBS and extend these observations into specification-driven operational variants permitted by 3GPP standards. Devilray enables the systematic exploration of 2,592 feasible and realistic FBS instances, capturing a wide range of operational possibilities. Using Devilray, we evaluate seven representative accessible FBS detectors and uncover coverage gaps across all seven, revealing blind spots rooted in assumption-bound design and evaluation. Our work provides the first robust adversarial model grounded in real-world behavior and specification analysis, enabling the community to develop and evaluate future detection mechanisms in a rigorous manner.

---


### 116. [Quantum Machine Learning for Cyber-Physical Anomaly Detection in Unmanned Aerial Vehicles: A Leakage-Free Evaluation with Proxy-Audited Feature Sets](https://arxiv.org/abs/2605.19233)

**<font color=#1a73e8>作者：</font>** Carlos A. Durán Paredes, Javier E. León Calderón, Nicolás Sánchez Perea 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicles (UAVs) are cyber-physical systems whose attack surface spans networked avionics and on-board sensor fusion: a compromised GPS or battery module can mimic a benign mission segment and evade naive anomaly detectors. We present a leakage-free evaluation of quantum machine learning for UAV anomaly detection on the multi-sensor TLM:UAV benchmark. Three contributions support the study. (i) A group-aware temporal protocol (B2) partitions the dataset into ten contiguous TimeUS blocks and evaluates over ten seeds, eliminating the inflation produced by random stratified splits that mix neighbouring samples. (ii) A three-mode feature audit (full/loose/strict) quantifies how much accuracy stems from instantaneous physical signals versus contextual proxies (cumulative energy, battery state, GPS trajectory). (iii) A hybrid XGBoost + Data Reuploading (DRU) classifier is benchmarked against five paired non-linear controls (raw, PCA, polynomial-2, random-RBF, and an untrained DRU map) under identical budgets. The standalone DRU does not consistently match the strongest classical baseline across seeds; however, the trained-DRU hybrid is the only model whose mean F1 macro shifts upward from full to strict (+0.05), a directional signal that the per-seed standard deviations prevent from being interpreted as a statistically established difference. The trained-DRU hybrid also records the lowest mean false-alarm rate under proxy-free evaluation, subject to the inter-seed variance reported. We frame this as an incremental, reproducible quantum-enhanced hybrid benefit, and provide an open Qiskit 2.x implementation as a benchmark for cybersecurity analytics in NISQ-era aerospace systems.

---


### 117. [AI Technologies in Language Access: Attitudes Towards AI and the Human Value of Language Access Managers](https://arxiv.org/abs/2605.19234)

**<font color=#1a73e8>作者：</font>** Miguel A. Jiménez-Crespo, Stephanie Rodriguez, Alejandro Jaume Losa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid emergence of AI technologies is reshaping translation practices and theory across the board. This paper deals with the impact of AI in language access. This area is characterized by the need to serve broad and diverse user populations, within a context where efficiency and access are shaped by legal mandates, ethical and commercial tensions, and safety concerns. This paper reports on the attitudes and perceptions of language access managers towards the AI and the human value in the AI age. Methodologically, this paper presents an analysis of a subset of a broader study on language access and technology, specifically a qualitative thematic analysis of ten semi-structured interviews with language access managers in the USA working in healthcare, court, public service and local government contexts. The results indicate that language access managers show conditional optimism towards the inevitable AI implementations, are strongly risk aware, and deeply committed to the human value and human oversight of AI implementations and output.

---


### 118. [GAE Falls Short in Imperfect-Information Self-Play Reinforcement Learning](https://arxiv.org/abs/2605.19235)

**<font color=#1a73e8>作者：</font>** Zhiyuan Fan, Gabriele Farina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Competitive multi-agent reinforcement learning in imperfect-information games requires agents to act under partial observability and against adversarial opponents, necessitating stochastic policies. While self-play reinforcement learning with Proximal Policy Optimization (PPO) has achieved strong empirical success, its standard advantage estimator, generalized advantage estimation, suffers from additional variance due to the sampling of stochastic future actions. This variance is amplified in equilibrium self-play because of the stochastic nature of the equilibrium policy and persists even when the critic is exact. We address this bottleneck by introducing $Q$-boosting, a variance-reduced advantage estimator based on a centralized action-value critic, and propose Variance-Reduced Policy Optimization (VRPO), incorporating this new estimator. The algorithm replaces sampled multi-step backups with a multi-step Expected SARSA$(\lambda)$ trace, computing policy expectations at each step to average out action-sampling noise, while retaining PPO's clipped objective and on-policy actor updates. Empirically, VRPO consistently achieves strong performance from mid-sized to large-scale games including Dou Dizhu and Heads-Up No-Limit Texas Hold'em.

---


### 119. [Euclidean Embedding of Data Using Local Distances](https://arxiv.org/abs/2605.19243)

**<font color=#1a73e8>作者：</font>** Dimitris Arabadjis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of recovering a globally consistent Euclidean embedding of data, given only a local distance graph and propose a method that optimally represents these distances. The method operates solely on a neighborhood graph weighted by pairwise distances, without requiring any prior vector representation of the data. The embedding is obtained by solving a variational problem that matches local, on-graph distances to the Euclidean metric, induced by the differentials of the embedding functions. The resulting Euler-Lagrange equations are derived in a coordinate-free form, enabling direct evaluation of all operators from the distance graph alone. Though non-linear and missing an explicit expression for their non-linearity, these equations are shown to be resolved as an iteratively updated sparse linear problem. The main contributions of the proposed approach are (a) the derivation of the functional equations governing the optimal Euclidean embedding in the continuum, (b) a representation-free formulation that requires only a neighborhood distance graph and no feature vectors and (c) an estimation procedure based exclusively on local graph operations. We experimentally evaluate the resulting non-parametric algorithm on synthetic manifolds and real datasets, demonstrating consistent preservation of local metric structure and neighboring relations, while approximating the global isometric embedding.

---


### 120. [Beyond Extrapolation: Knowledge Utilization Paradigm with Bidirectional Inspiration for Time Series Forecasting](https://arxiv.org/abs/2605.19249)

**<font color=#1a73e8>作者：</font>** Liu Chong, Yingjie Zhou, Hao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting is critical in various scenarios, such as energy, transportation, and public health. However, most existing forecasters rely primarily on one-way inference, \textit{i.e.}, mapping \textbf{history} to \textbf{target}, and overlook the structural information provided by a revised natural chain (``\textbf{history} (model input) -- \textbf{target} (ground-truth output) -- \textbf{post-target continuation}''). The post-target continuation records how trajectories evolve after the target, which can help stabilize forecasting, but it is not observable at inference time. In this work, we aim to obtain an approximate proxy of the post-target continuation for the current input, providing structural knowledge for bidirectional forecasting. This idea is instantiated as KUP-BI (Knowledge Utilization Paradigm with Bidirectional Inspiration), a new time-series modeling paradigm that distills continuation-style knowledge (as an approximate post-target continuation proxy) from a \emph{train-only} historical library and integrates it into standard forecasting backbones. The input stream and the continuation-proxy stream are fused via a lightweight feature-level gating module. This design does not introduce information beyond what is already contained in the training trajectories; instead, it provides a structured inductive bias that helps backbones exploit typical continuation patterns rather than relying solely on parametric extrapolation. Experimental results on six public datasets show that KUP-BI consistently improves the forecasting performance of state-of-the-art models, with small additional overhead.

---


### 121. [Detecting and Mitigating Backdoor Attacks in OTA-FL Systems: A Two-Stage Robust Aggregation Scheme](https://arxiv.org/abs/2605.19253)

**<font color=#1a73e8>作者：</font>** Xiaoyan Ma, Seohyun Lee, Taejoon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Over-the-air federated learning (OTA-FL) improves communication efficiency by exploiting the superposition property of wireless channels, but this same property also creates a critical security vulnerability: the parameter server (PS) cannot access individual local updates, making it difficult to identify and exclude poisoned gradients. The challenge is further exacerbated under non-independent and identically distributed (Non-IID) training data, where benign gradient drift can closely resemble malicious updates. In this paper, we propose a two-stage robust aggregation framework for defending against backdoor attacks in OTA-FL. Under our scheme, each client is first assigned a modality-aware multi-indicator trust score, where the specific indicators are selected according to the data modality (e.g., waveform, text, image) and model architecture to capture the most discriminative footprint of backdoor updates. Based on this score, the PS then performs trust-based multiple access (TBMA) to separate clients into trusted, suspicious, and malicious categories. Suspicious clients are further examined through PS-side layer-wise inspection and a longitudinal reputation mechanism. Experimental results on several datasets demonstrate that the proposed methodology effectively suppresses stealthy backdoor attacks, including bounded-scaling attacks, Euclidean-constrained attacks, Cosine-constrained attacks, and Neurotoxin, while maintaining competitive main-task accuracy.

---


### 122. [Distribution Matching Distillation without Fake Score Network](https://arxiv.org/abs/2605.19256)

**<font color=#1a73e8>作者：</font>** Youngjoong Kim, Deokyeong Lee, Jaesik Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution Matching Distillation (DMD) provides an effective distribution-level correction for few-step generation, while relying on an auxiliary fake-score network to track the evolving generative distribution. Recent work combines DMD-style objectives with flow-map generators to exploit both forward-divergence training and reverse-divergence correction. The fake-score estimator remains an additional component with memory and update overhead. In this work, we study whether this explicit tracker can be avoided when the generator itself has a flow-map structure. We propose Fake-Score-network-Free DMD (FSF-DMD), a DMD formulation for flow-map generators that replaces the auxiliary fake-score estimator with a generator-induced pseudo-velocity surrogate. The key observation is that the endpoint pseudo-velocity of a flow-map generator provides a tractable proxy for fake-velocity estimation, allowing the generator itself to supply the reverse-divergence signal. Building on this observation, we derive a practical objective, extend it with flow-map-consistent backward simulation, and introduce a self-teacher variant for training from scratch. In our ImageNet-1K $256 \times 256$ experiments, FSF-DMD improves flow-map baselines, reaches lower FID than the listed DMD2 comparisons in the flow-map-initialized setting, and remains effective under flow-matching initialization and training from scratch.

---


### 123. [ExECG: An Explainable AI Framework for ECG models](https://arxiv.org/abs/2605.19258)

**<font color=#1a73e8>作者：</font>** Jong-Hwan Jang, Yong-yeon Jo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has enabled ECG diagnostic models with strong performance in tasks such as arrhythmia classification and abnormality detection. However, accuracy alone is insufficient for clinical deployment because it does not explain why a specific output was produced, limiting justification, error analysis, and trust. Although ECG XAI has been extensively investigated and steadily improved, practical pipelines and reporting conventions vary across studies, hindering reuse and reproducibility. To address these issues, we present Explainable AI framework for ECG models (ExECG), a Python framework that provides a three-stage pipeline: Wrapper standardizes access across heterogeneous ECG formats and intermediate representations, Explainer unifies diverse XAI methods under a shared execution protocol, and Visualizer supports consistent cross-method comparison within a unified interface. We demonstrate end-to-end usage with concise examples and two case studies, highlighting interoperable and reproducible ECG explainability.

---


### 124. [AQuaUI: Visual Token Reduction for GUI Agents with Adaptive Quadtrees](https://arxiv.org/abs/2605.19260)

**<font color=#1a73e8>作者：</font>** Yuankai Li, Tinghui Zhu, Ha Min Son 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Multimodal Models (LMMs) have recently emerged as promising backbones for GUI-agent models, where high-resolution GUI screenshots are introduced to the prompts at each iteration step. However, these screenshots exhibit highly non-uniform spatial information density: large regions may carry little information and are visually homogeneous, while key text and icons may require high visual fidelity. Existing approaches to this problem either require additional training or rely on attention-based token compression, ignoring the structured layout and spatial redundancy of GUI screenshots. To fill the gap, this paper proposes AquaUI, a training-free inference-time token reduction method for GUI agent models that utilizes the non-uniform information density in screenshots. AQuaUI constructs an adaptive quadtree on each screenshot input and keeps one representative merged token per leaf of the quadtree. AQuaUI preserves the spatial positions of retained tokens throughout the pipeline to ensure that all position-encoding stages remain consistent. To further improve temporal consistency across multi-step GUI interactions, we propose a conditional quadtree algorithm that leverages the continuity between consecutive screenshots within a single request. Specifically, it refines the current quadtree using previous quadtrees as references, helping preserve fine-grained regions across static or mildly shifted GUI states. We implement AQuaUI on state-of-the-art GUI agent models and conduct experiments on standard grounding and navigational benchmarks. AQuaUI consistently shows improved accuracy-efficiency trade-offs over prior baselines. Notably, on GUI-Owl-1.5-32B-Instruct, AQuaUI achieves up to 13.22% speedup and 29.52% fewer visual tokens while retaining 99.06% of full-token performance, suggesting that the spatial redundancy of GUI screenshots can be exploited at inference without retraining.

---


### 125. [From Simple to Complex: Curriculum-Guided Physics-Informed Neural Networks via Gaussian Mixture Models](https://arxiv.org/abs/2605.19263)

**<font color=#1a73e8>作者：</font>** Jianan Yang, Yiran Wang, Shuai Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) offer a mesh-free framework for solving partial differential equations (PDEs), yet training often suffers from gradient pathologies, spectral bias, and poor convergence, especially for problems with strong nonlinearity, sharp gradients, or multiscale features. We propose the Curriculum-Guided Gaussian Mixture Physics-Informed Neural Network (CGMPINN), which integrates Gaussian mixture modeling with dynamic curriculum learning. Specifically, a GMM is periodically fitted to the PDE residual distribution to quantify spatially varying learning difficulty. A smooth curriculum schedule progressively shifts training focus from easy to harder regions, while precision-based variance modulation suppresses unreliable clusters during early optimization. This dual curriculum is governed by a shared curriculum parameter and can be combined with self-adaptive loss balancing. We further establish theoretical guarantees, including sublinear convergence of the gradient norm for the induced time-varying loss, uniform equivalence between the curriculum-weighted and standard PDE losses, and a generalization bound with an explicit weighting-induced bias characterization. Experiments on six benchmark PDEs spanning elliptic, parabolic, hyperbolic, advection-dominated, and nonlinear reaction-diffusion types show that CGMPINN consistently achieves the lowest relative $L_2$ and maximum absolute errors among all compared methods, reducing relative $L_2$ error by up to 97.8\% over the standard PINN at comparable cost. Our code is publicly available at this https URL.

---


### 126. [Swimming with Whales: Analysis of Power Imbalances in Stake-Weighted Governance](https://arxiv.org/abs/2605.19264)

**<font color=#1a73e8>作者：</font>** Yuzhe Zhang, Manvir Schneider, Qin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Voting methods weighted by stakes are the fundamental governance paradigm in Proof-of-Stake (PoS) blockchains. Such a paradigm is known to be prone to power distortions: a few users possessing large stakes may completely control decision making, even without owning the totality of the stakes. We study this phenomenon through the lens of computational social choice, focusing on the extent of power imbalances in stake-weighted voting when power is quantified using the Penrose-Banzhaf power index. Our work presents both analytical and empirical contributions. Analytically, we demonstrate that while a perfect alignment between power and relative stake ownership is generally unattainable, it can be approximated in expectation under specific conditions. Empirically, using data from a real-world on-chain governance system (Project Catalyst), we provide a more fine-grained understanding of the power imbalances that are likely to occur in current stake-weighted governance systems.

---


### 127. [FormalASR: End-to-End Spoken Chinese to Formal Text](https://arxiv.org/abs/2605.19266)

**<font color=#1a73e8>作者：</font>** Wanyi Ning, Yinshang Guo, Haitao Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems are typically optimized for verbatim transcription, which preserves disfluencies, filler words, and informal spoken structures that are often unsuitable for downstream writing-oriented applications. A common workaround is a two-stage ASR+LLM pipeline for post-editing, but this design increases latency and memory cost and is difficult to deploy on-device. We present FormalASR, two compact end-to-end models (0.6B and 1.7B) that directly transcribe spoken Chinese into formal written text. To enable this setting, we build WenetSpeech-Formal and Speechio-Formal, two large-scale spoken-to-formal datasets constructed by LLM-based rewriting and quality filtering. We then fine-tune Qwen3-ASR at two scales (0.6B and 1.7B) with supervised fine-tuning. Experiments on WenetSpeech-Formal and Speechio-Formal show that FormalASR achieves up to 37.4% relative CER reduction over verbatim baselines, while also improving ROUGE-L and BERTScore. FormalASR requires no post-processing LLM at deployment time, providing a lightweight, on-device solution for spoken-to-formal transcription.

---


### 128. [CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs](https://arxiv.org/abs/2605.19269)

**<font color=#1a73e8>作者：</font>** Han Guo, Jack Zhang, Arjun Menon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer training systems are built around dense linear algebra, yet a nontrivial fraction of end-to-end time is spent on surrounding memory-bound operators. Normalization, activations, residual updates, reductions, and related computations repeatedly move large intermediate tensors through global memory while performing little arithmetic, making data movement an increasingly important bottleneck in otherwise highly optimized training stacks. We introduce CODA, a GPU kernel abstraction that expresses these computations as GEMM-plus-epilogue programs. CODA is based on the observation that many Transformer operators exposed as separate framework kernels can be algebraically reparameterized to execute while a GEMM output tile remains on chip, before it is written to memory. The abstraction fixes the GEMM mainloop and exposes a small set of composable epilogue primitives for scaling, reductions, pairwise transformations, and accumulation. This constrained interface preserves the performance structure of expert-written GEMMs while remaining expressive enough to cover nearly all non-attention computation in the forward and backward pass of a standard Transformer block. Across representative Transformer workloads, both human- and LLM-authored CODA kernels achieve high performance, suggesting that GEMM-plus-epilogue programming offers a practical path toward combining framework-level productivity with hardware-level efficiency.

---


### 129. [Lost in Interpretation: The Plausibility-Faithfulness Trade-off in Cross-Lingual Explanations](https://arxiv.org/abs/2605.19274)

**<font color=#1a73e8>作者：</font>** Somnath Banerjee, Pranav Jha, Rima Hazra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs deployed multilingually are often audited via English explanations for non-English inputs. We evaluate extractive explanations ''where the model identifies input token spans as evidence alongside a generated rationale'' and uncover a systematic trade-off: English-pivot explanations can achieve higher span agreement with human rationales while their evidence becomes less causally grounded in the model's prediction, as measured by both comprehensiveness and sufficiency. Across 3 tasks, 5~languages, and 2~multilingual LLM families, we find that English explanations frequently produce fluent but loosely anchored rationales, with comprehensiveness degrading by up to 5.7x relative to native-language conditions - even as task accuracy remains stable across settings. For socially nuanced classification, English pivots also fail to preserve pragmatic cues, reducing both faithfulness and span agreement. We recommend auditing explanations in the input language, reporting multi-faceted faithfulness metrics beyond lexical overlap, and treating English rationales as communication summaries rather than faithful decision traces.

---


### 130. [FPED: A Functional-Network Prior-Guided Mixture-of-Experts Framework for Interpretable Brain Decoding](https://arxiv.org/abs/2605.19279)

**<font color=#1a73e8>作者：</font>** Yudan Ren, Pengcheng Shi, Zihan Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual image reconstruction from functional Magnetic Resonance Imaging (fMRI) is a fundamental task in brain decoding, providing a crucial pathway for understanding human perceptual mechanisms and developing advanced brain-computer interfaces (BCIs). However, most current methods simply flatten fMRI signals from localized visual cortices into one-dimensional (1D) vectors, mapping them directly into latent spaces such as that of Contrastive Language-Image Pre-training (CLIP). This paradigm not only disrupts the inherent network topology of the brain-leading to limited neuroscientific interpretability-but also overlooks the synergistic contributions of other distributed functional networks in processing high-level visual semantics. To address these limitations, we propose FPED, a Functional-Network Prior-Guided Mixture of Experts (MoE) framework for interpretable brain decoding. FPED explicitly models different functional brain networks as specialized experts and employs adaptive routing to capture their complementary contributions to visual semantic understanding. Unlike conventional homogeneous decoding paradigms, our framework incorporates neurobiologically grounded priors to enable structured and interpretable network-level representation learning. Experimental results demonstrate that FPED achieves highly competitive semantic reconstruction performance with only 0.68B parameters. The learned routing dynamics reveal biologically meaningful correspondence between functional brain networks and modality-specific semantic processing, providing transparent neuroscientific interpretability. This suggests that brain network-aware expert modeling is a promising direction for bridging neural decoding and biologically inspired artificial intelligence.

---


### 131. [EviTrack: Selection over Sampling for Delayed Disambiguation](https://arxiv.org/abs/2605.19283)

**<font color=#1a73e8>作者：</font>** Omer Haq  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential prediction is challenging in regimes of delayed disambiguation, where early observations are ambiguous and multiple latent explanations remain plausible until sufficient evidence accumulates. Standard approaches based on marginal inference struggle in this setting, either collapsing uncertainty prematurely or failing to recover once informative evidence arrives.
We introduce EviTrack, a test-time inference framework that operates over latent trajectories rather than marginal states. EviTrack maintains a set of competing trajectory hypotheses and applies evidence- and likelihood-ratio-based selection to delay commitment until supported by data, drawing inspiration from hypothesis management in multiple hypothesis tracking and track-before-detect.
To evaluate this setting, we construct a controlled synthetic benchmark with known latent ground truth that explicitly exhibits delayed disambiguation. At matched inference budget, EviTrack substantially outperforms sampling-based baselines, achieving faster post-disambiguation recovery.
These results show that, in delayed disambiguation regimes, moderate trajectory-level selection is more effective than increasing sampling coverage, highlighting selection over sampling as a key principle for reliable sequential inference.

---


### 132. [What Makes Synthetic Data Effective in Image Segmentation](https://arxiv.org/abs/2605.19289)

**<font color=#1a73e8>作者：</font>** Jinjin Zhang, Xiefan Guo, Yizhou Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driven by rapid advances in large-scale generative models, synthetic data has emerged as a promising solution for visual understanding. While modern diffusion models achieve remarkable photorealistic image synthesis, their potential in complex visual segmentation tasks remains underexplored. In this work, we conduct a systematic analysis of synthetic images from state-of-the-art diffusion models to uncover the factors governing their utility. In particular, synthetic images characterized by dense scene composition and fine instance fidelity demonstrate distinctive benefits, yielding significantly more discriminative spatial representations. Building on these insights, we propose SENSE, a unified framework that leverages flexible and scalable synthetic data to substantially enhance segmentation performance. Notably, SENSE is model-agnostic, compatible with diverse architectures (e.g., DPT and Mask2Former), and scales effectively across models with varying parameter capacities. Extensive experiments on Cityscapes, COCO, and ADE20K validate the effectiveness and generalization capability of our approach. Code is available at this https URL.

---


### 133. [Cross-Paradigm Knowledge Distillation: A Comprehensive Study of Bidirectional Transfer Between Random Forests and Deep Neural Networks for Big Data Applications](https://arxiv.org/abs/2605.19299)

**<font color=#1a73e8>作者：</font>** Mahdi Naser Moghadasi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The exponential growth of big data has intensified the need for efficient and interpretable machine learning models that can handle diverse data characteristics while maintaining computational efficiency. Knowledge distillation has primarily focused on neural network-to-neural network transfer, leaving cross-paradigm knowledge transfer largely unexplored. This paper presents the first comprehensive study of bidirectional knowledge distillation between Random Forests (RF) and Deep Neural Networks (DNN), addressing critical gaps in ensemble learning and model compression for big data applications. We propose novel methodologies including progressive multi-stage distillation, multi-teacher ensemble distillation from diverse tree models, and uncertainty-aware cross-paradigm transfer mechanisms. Through 144 comprehensive experiments across 6 diverse datasets encompassing classification and regression tasks, we demonstrate that bidirectional RF-DL distillation achieves competitive performance while providing complementary benefits: interpretability from tree models and expressiveness from neural networks. Our results show that multi-teacher ensemble distillation consistently outperforms traditional approaches, with NN-COMPACT achieving 98.13% classification accuracy and NN-WIDE reaching 92.6% R^2 score in regression tasks. The proposed framework enables deployment flexibility in big data environments, allowing optimal model selection based on computational constraints and interpretability requirements. This work establishes a new research direction in cross-paradigm knowledge transfer with significant implications for interpretable AI and scalable model deployment in resource-constrained big data systems.

---


### 134. [MMGS: 10$\times$ Compressed 3DGS through Optimal Transport Aggregation based on Multi-view Ranking](https://arxiv.org/abs/2605.19304)

**<font color=#1a73e8>作者：</font>** Beizhen Zhao, Sicheng Yu, Ziran Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Gaussian Splatting (3DGS) has revolutionized 3D reconstruction, it suffers from significant overhead due to massive redundant primitives. Existing compression methods typically rely on local sampling or fixed pruning thresholds, which often struggle to balance redundancy reduction with high-fidelity rendering. To address this, we propose a novel framework that formulates Gaussian optimization as a global geometric distribution matching problem. Specifically, our approach integrates three components: (1) we introduce a multi-view 3D Gaussian contribution ranking mechanism that filters primitives using geometric consistency instead of local heuristics; (2) we propose a global Optimal Transport (OT)-based aggregation algorithm that merges redundant primitives while preserving the underlying geometry; and (3) we design an OT-based densification operator that maintains the Gaussian's distributional properties for stable optimization. Our approach achieves state-of-the-art rendering quality with only \textbf{10$\%$} primitives and \textbf{10$\times$} accelerated training speeds compared to vanilla 3DGS.

---


### 135. [A Two-Phase Adaptive Balanced Penalty Method for Controllable Pareto Front Learning under Split Feasibility Conditions](https://arxiv.org/abs/2605.19306)

**<font color=#1a73e8>作者：</font>** Nguyen Viet Hoang, Dung D. Le, Tran Ngoc Thang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the open problem of training hypernetworks for Controllable Pareto Front Learning (CPFL) under split feasibility conditions with rigorous theoretical guarantees. We reformulate the constrained Pareto problem as a Bi-Level Scalarized Split Problem (BSSP) and propose the Adaptive Balanced Penalty (ABP) algorithm, whose three gradient components -- optimality, set feasibility, and image feasibility -- are blended through an adaptive indicator driven by a computable lower bound. Using a novel convex surrogate technique, we prove full-sequence convergence under standard convexity and Robbins-Monro step-size assumptions. The ABP penalty structure is then translated into a two-phase, feasibility-first training strategy for Hyper-MLP and HyperTrans architectures (ABP-HyperNet). To evaluate constrained CPFL, we introduce the Expected Feasible Hypervolume (EFHV), which jointly captures solution quality and constraint satisfaction. Experiments on five multi-objective benchmarks validate the ABP solver against ground truth, while three multi-task learning datasets demonstrate that ABP-HyperNet achieves up to 2.3x higher EFHV than unconstrained baselines by raising feasibility from 36-49% to 87-100%.

---


### 136. [How Do Document Parsers Break? Auditing Structural Vulnerability in Document Intelligence](https://arxiv.org/abs/2605.19309)

**<font color=#1a73e8>作者：</font>** Yue Chen, Yihao Wang, Ziyi Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document Layout Analysis (DLA) pipelines provide structured page representations for retrieval-augmented generation, long-document question answering, and other document intelligence systems, yet their robustness evaluation remains largely area-centric. We identify this Footprint Bias and propose a lightweight output-level auditing framework that decouples probe construction, policy-driven targeting, and structure-aware diagnosis. The framework combines Block-level Structural Loss Rate (B-SLR), granularity-aware exposure descriptors, and pathway attribution to analyze where perturbations interact with layout structure and how failures propagate. Across MinerU and PP-StructureV3 on 1,000 pages, affected area weakly tracks perturbation-induced OCR instability (R^2=0.384/0.110), whereas B-SLR aligns much more closely with it (R^2=0.727/0.916). Exposure descriptors further separate occlusion- and topology-dominant pathways, and small structurally targeted probes cause downstream QA/retrieval degradation comparable to larger-footprint perturbations. These results shift DLA robustness evaluation from footprint-based stress testing toward structure-aware vulnerability auditing.

---


### 137. [An Objective Performance Evaluation of the LSTM Networks in Time Series Classification](https://arxiv.org/abs/2605.19311)

**<font color=#1a73e8>作者：</font>** Sooraj Sunil, Balakumar Balasingam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of deep learning has increasingly led to data-driven models replacing classical model-based algorithms, even in domains governed by well-understood physical laws. While data-driven models, such as long short-term memory (LSTM) networks, have become a popular choice for time-series analysis, their performance relative to model-based approaches in structured environments is rarely evaluated objectively. This paper presents a performance evaluation framework comparing an LSTM classifier against a model-based expectation maximization (EM) classifier for binary time-series classification. The evaluation is conducted on two scalar linear Gaussian state space models differing only in their noise statistics, where the Kalman filter likelihood ratio test with true parameters serves as a reference for the best achievable classification this http URL Monte Carlo simulations, the classifiers are evaluated across three axes: task difficulty, controlled by the separation in process or measurement noise between the two models; sequence length; and training dataset size. The results show that the EM classifier, which exploits the known model structure, performs strongly when the data conform to the assumed model class. The LSTM classifier requires a larger separation in noise statistics to achieve reliable classification, and its performance saturates below the reference classifier when the models differ only in measurement noise, regardless of sequence length or training dataset size.

---


### 138. [MultiBallot: Verifiable and privacy-preserving E-Collecting in the Swiss setting](https://arxiv.org/abs/2605.19312)

**<font color=#1a73e8>作者：</font>** Florian Moser, Léo Louistisserand  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As part of the political process, citizens may participate in signature collections to influence policy changes. In Switzerland, this even results in legally binding acts, similar to an election system. In this work, we first derive a realistic setting for e-collecting in Switzerland, based on the setting established for e-voting. Then, we propose a secure protocol in this setting, achieving both privacy and verifiability under realistic trust assumptions. Notably, participation privacy is guaranteed without assuming an anonymous channel, by considering the fact that at any given point in time, many collections are active in parallel.

---


### 139. [Inference-Time Scaling in Diffusion Models through Iterative Partial Refinement](https://arxiv.org/abs/2605.19317)

**<font color=#1a73e8>作者：</font>** Taegu Kang, Jaesik Yoon, Sungjin Ahn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time scaling has emerged as a major approach for improving reasoning capabilities, and has been increasingly applied to diffusion models. However, existing inference-time scaling methods for diffusion models typically rely on external verifiers or reward models to rank and select samples, limiting their scalability to settings where such evaluators are available and reliable. Moreover, while recent diffusion models perform sequential inference with region-wise, mixed-noise conditioning, inference-time scaling tailored to this setting remains relatively underexplored. We propose Iterative Partial Refinement (IPR), an inference-time scaling method for sequential diffusion that requires no external verifier. Starting from an already-generated sample, IPR re-noises a subset of regions and regenerates them conditioned on the remaining regions, enabling the model to revise earlier decisions under a richer context than was available during the initial generation. This iterative partial refinement produces more globally consistent samples without external verification. On reasoning tasks requiring global constraint satisfaction, IPR consistently improves performance: on MNIST Sudoku, the valid solution rate increases from 55.8% to 75.0%. These results show that iterative partial refinement alone can serve as an effective inference-time scaling strategy for diffusion models in sequential, mixed-noise settings. Code is available at: this https URL

---


### 140. [BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics](https://arxiv.org/abs/2605.19324)

**<font color=#1a73e8>作者：</font>** Siddharth Viswanath, Panayiotis Ketonis, Chen Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient neural network models that generate brain-like dynamic activity can be a valuable resource for generating synthetic data, analyzing differences in brain transients under conditions such as testing perturbation activity or inferring the underlying generative dynamics. However, large language models (LLMs) or standard recurrent neural networks (RNNs) ignore the anatomical organization and therefore do not produce components that align with brain regions. On the other hand, graph-based networks often have very simple message passing rules that are not sufficiently expressive for brain-like dynamics. To address this, we introduce BrainDyn, a sheaf neural ordinary differential equation (neural ODE) model for continuous-time dynamics on structured brain graphs. BrainDyn encodes the recent activity history of each brain region using a long short-term memory (LSTM) model over a sliding temporal window to produce hidden states, or stalks, that are projected through learnable restriction maps into edge-specific shared spaces. Discrepancies between neighboring nodes in these shared spaces are characterized by a sheaf Laplacian that can facilitate message passing between neuronal units. The output of these messages is then fed to a neural ODE that governs the continuous-time evolution of neuronal activity. We evaluated BrainDyn on resting-state fMRI (PNC dataset), scalp EEG with focal epilepsy (TUSZ dataset), and simulated activity from the NEST spiking network simulator. BrainDyn achieves strong forecasting ability across modalities, and the resulting representations support downstream tasks including in silico perturbation prediction.

---


### 141. [An Exterior Method for Nonnegative Matrix Factorization](https://arxiv.org/abs/2605.19325)

**<font color=#1a73e8>作者：</font>** Qiujing Lu, Tonmoy Monsoor, Ehsan Ebrahimzadeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonnegative matrix factorization (NMF) seeks a low-rank approximation $X \approx UV^T$ with nonnegative factors and is commonly solved using interior methods that enforce feasibility throughout optimization. We show that such constraint-driven approaches can impede progress in the nonconvex landscape, leading to slow convergence or convergence to suboptimal stationary points. We propose an exterior framework for NMF (eNMF) that separates low-rank approximation from nonnegativity enforcement. Our method initializes from the optimal unconstrained factorization and introduces a rotation procedure that maps unconstrained factors to an exterior point closest to the nonnegative orthant. This viewpoint yields an algorithmic framework in which simple iterative updates converge to KKT-satisfying stationary points on the boundary of the positive orthant. The exterior formulation also enables a geometric interpretation of NMF solutions, clarifying equivalence classes of factorizations under permutation and orthogonal transformations. An intriguing numerical result, involving 400 NMF experiments across both real and synthetic datasets, show that in 99% of the cases, different algorithms tend to converge towards equivalent factor matrices. We benchmark eNMF against 9 state-of-the-art NMF algorithms with 9 initialization schemes across 3 real-world and 2 synthetic datasets. eNMF consistently outperforms all 81 competitors, achieving up to 30% lower reconstruction error under equal-time settings and up to 150% speedup under equal-error settings. The downstream experiments further demonstrate substantial performance gains in audio processing and recommendation tasks, corroborating the practical benefits of the proposed exterior optimization framework. Code is available at this https URL

---


### 142. [RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents](https://arxiv.org/abs/2605.19328)

**<font color=#1a73e8>作者：</font>** Doguhuan Yeke, Yanming Zhou, Leo Y. Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent advances in Vision-Language Models (VLMs) facilitate a new class of embodied AI systems, where these models are integrated into physical platforms, e.g. robots and autonomous vehicles, to interpret visual scenes and execute natural language commands in diverse environments. Previous research has introduced jailbreak attacks and defenses for embodied AI. Their evaluations, however, rely on ad-hoc datasets, limited metrics, and emphasize attack success while neglecting the trade-off between security and the ability to follow benign commands. Existing benchmarks and evaluation frameworks either target traditional chat-based models or focus on non-adversarial safety evaluation for embodied AI; neither captures the adversarial risks, inputs, consequences, and evaluation criteria necessary for jailbreak attacks in embodied AI systems. In this paper, we address this gap with RoboJailBench, which consists of three core components. We establish a security taxonomy derived from ISO standards, regulatory rules, and documented incidents. This effort yields 18 categories of security violation consequences for embodied AI. We introduce an intent contrast dataset pipeline that augments existing datasets with paired adversarial and benign goals to measure both security and utility. Lastly, we provide an evolving repository with standardized metrics and a unified process for assessing and integrating new attacks and defenses. With this benchmark, we construct a new taxonomy-balanced dataset and augment five existing datasets. We integrate four attacks and two defenses to evaluate their performance on leading embodied VLMs. This benchmark provides the first standardized evaluation framework for jailbreak attacks in embodied AI and supports future research. We release our code, datasets, and artifacts, and maintain a leaderboard at this https URL.

---


### 143. [MOCHA: Multi-Objective Chebyshev Annealing for Agent Skill Optimization](https://arxiv.org/abs/2605.19330)

**<font color=#1a73e8>作者：</font>** Md Mehrab Tanjim, Jayakumar Subramanian, Xiang Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents organize behavior through skills - structured natural-language specifications governing how an agent reasons, retrieves, and responds. Unlike monolithic prompts, skills are multi-field artifacts subject to hard platform constraints: description fields are truncated for routing, instruction bodies are compacted via progressive disclosure, and co-resident skills compete for limited context windows. These constraints make skill optimization inherently multi-objective: a skill must simultaneously maximize task performance and satisfy platform limits. Yet existing prompt optimizers either ignore these trade-offs or collapse them into a weighted sum, missing Pareto-optimal variants in non-convex objective regions. We introduce MOCHA (Multi-Objective Chebyshev Annealing), which replaces single-objective selection with Chebyshev scalarization - covering the full Pareto front, including non-convex regions - combined with exponential annealing that transitions from exploration to exploitation. In our experiments across six diverse agent skills - where all methods share the same multi-objective mutation operator and baselines receive identical per-objective textual feedback - existing optimizers fail to improve the seed skill on 4 of 6 tasks: 1000 rollouts yield zero progress. MOCHA breaks through on every task, achieving 7.5% relative improvement in mean correctness over the strongest baseline (up to 14.9% on FEVER and 10.4% on TheoremQA) while discovering twice as many more Pareto-optimal skill variants.

---


### 144. [STAR-PólyaMath: Multi-Agent Reasoning under Persistent Meta-Strategic Supervision](https://arxiv.org/abs/2605.19338)

**<font color=#1a73e8>作者：</font>** Jiaao Wu, Xian Zhang, Hanzhang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Frontier AI models and multi-agent systems have led to significant improvements in mathematical reasoning. However, for problems requiring extended, long-horizon reasoning, existing systems continue to suffer from fundamental reliability issues: hallucination accumulation, memory fragmentation, and imbalanced reasoning-tool trade-offs. In this paper, we introduce STAR-PólyaMath, a multi-agent framework that systematically addresses these challenges through meta-level supervision and structured Reasoner-Verifier interaction. STAR-PólyaMath is structured as an orchestrated state machine with nested challenge-step-replan loops, governed by a reasoning-free Python orchestrator that separates control from inference and bounds error propagation through trace-back and re-planning. Our key innovation is a persistent Meta-Strategist that maintains cross-attempt memory and exercises meta-level control by issuing high-level strategic guidance or mandatory directives, so the system can escape unproductive loops rather than stagnate or over-rely on tools. STAR-PólyaMath achieves state-of-the-art results on all eight top-tier competition benchmarks: AIME 2025-2026, MathArena Apex Shortlist, MathArena Apex 2025, Putnam 2025, IMO 2025, HMMT February 2026, and USAMO 2026. It obtains perfect scores on AIMEs, Putnam, and HMMT, and shows its largest margin on Apex 2025, scoring 93.75% compared with 80.21% by the strongest baseline GPT-5.5. Ablation studies show that the gains arise from the framework's orchestration rather than from model-level diversity since removing key components or substituting in mixed backbones consistently weakens performance. Code is available at this https URL.

---


### 145. [Semantic-Enriched Latent Visual Reasoning](https://arxiv.org/abs/2605.19342)

**<font color=#1a73e8>作者：</font>** Tianrun Xu, Yue Sun, Qixun Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal latent-space reasoning aims to replace explicit thinking with images by performing visual reasoning directly in a compact latent space. However, existing approaches largely rely on visual supervision and produce latent representations that lack sufficient semantic richness, limiting their ability to support diverse region-level reasoning tasks. In this work, we introduce Semantic-Enriched Latent Visual Reasoning (SLVR), a two-stage learning framework that enriches latent representations with attribute-level visual semantics and aligns them with diverse reasoning objectives. In the first stage, SLVR learns semantically enriched region-centric latents under fine-grained attribute supervision. In the second stage, we design Multi-query Group Relative Policy Optimization (M-GRPO) to align latent representations across multiple queries grounded in the same region. To support this framework, we construct SLV-Set, comprising approximately 400K region-level attribute annotations and 800K multi-query question answering samples, and introduce SV-QA, a benchmark that evaluates latent reasoning under semantic variation. Experiments demonstrate that SLVR improves the robustness and semantic consistency of latent visual reasoning compared to existing baselines.

---


### 146. [What Makes a Representation Good for Single-Cell Perturbation Prediction?](https://arxiv.org/abs/2605.19343)

**<font color=#1a73e8>作者：</font>** Wenkang Jiang, Yuhang Liu, Yichao Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell perturbation modeling is fundamental for understanding and predicting cellular responses to genetic perturbations. However, existing approaches, from causal representation learning to foundation models, often struggle with an overlooked challenge: gene expression is dominated by perturbation-invariant information, while perturbation-specific signals are intrinsically sparse. As a result, learned representations either entangle invariant and perturbation-specific information, leading to spurious and non-generalizable predictors, or suppress perturbation-specific signals altogether, rendering them ineffective for prediction. To address this, we propose PerturbedVAE, a general framework designed to resolve this signal imbalance. The framework explicitly separates perturbation-specific information from dominant invariant structure and recovers causal representations to effectively utilize such information for prediction. We further provide an identifiability analysis that characterizes the conditions under which sparse perturbation effects can be reliably recovered, thereby clarifying how the framework can be concretely specified under such conditions. Empirically, PerturbedVAE achieves state-of-the-art performance on a widely used benchmark across multiple evaluation settings, yielding significant gains on out-of-distribution combinatorial predictions and uncovering interpretable perturbation-response programs.

---


### 147. [Retrieval-Augmented Linguistic Calibration](https://arxiv.org/abs/2605.19344)

**<font color=#1a73e8>作者：</font>** Yi-Fan Yeh, Linwei Tao, Minjing Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linguistic cues such as "I believe" and "probably" offer an intuitive interface for communicating confidence, yet a generalisable, principled calibration framework for linguistic confidence expressions remains underexplored. In particular, co-occurring linguistic cues, contextual variation, and subjective audience interpretation pose unique challenges. We therefore model linguistic confidence as a distribution over plausible perceived probability values that a statement is correct, capturing interpretation variability that scalar representations discard. Within this distributional framework, we introduce faithfulness as a complementary evaluation dimension and present Faithfulness Divergence (FD), an information-theoretic metric quantifying the surprise induced in audience beliefs upon truth revelation. Building on these foundations, we present Retrieval-Augmented Linguistic Calibration (RALC), a lightweight post-hoc pipeline that propagates calibrated confidence signals back into natural language via retrieval-augmented rewriting. Across three QA benchmarks and five LLM families, RALC improves in-domain faithfulness and calibration up to 66% and 58%, respectively, outperforming black-box and grey-box calibration baselines.

---


### 148. [IMLJD: A Computational Dataset for Indian Matrimonial Litigation Analysis](https://arxiv.org/abs/2605.19346)

**<font color=#1a73e8>作者：</font>** Joy Bose  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present IMLJD, an open dataset of 3,613 Indian court judgments covering matrimonial disputes under IPC Section 498A, the Protection of Women from Domestic Violence Act, and CrPC Section 482. The dataset covers the Supreme Court of India from 2000 to 2024 (1,474 cases) and the Karnataka High Court from 2018 to 2024 (2,139 cases), with structured outcome labels, metadata-derived indicators, and a knowledge graph. We find that 57.6% of quashing petitions succeed at the Supreme Court level compared to 39.7% at the Karnataka High Court level. On a matched 2018 to 2024 period, the SC quash rate is 59.3%, widening the differential to 19.6 percentage points and confirming the finding is robust to temporal adjustment. The dataset, code, and knowledge graph are released openly at this https URL and this https URL.

---


### 149. [PAVE: A Cognitive Architecture for Legitimate Violation in Generative Agent Societies](https://arxiv.org/abs/2605.19351)

**<font color=#1a73e8>作者：</font>** Ahmad Yehia, Abduallah Mohamed, Kun Qian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Generative agents based on large language models reproduce believable human behavior in cooperative settings, but how they should reason in situations where rule-breaking may be required, such as fire evacuation or authority-supervised emergency, remains poorly characterized. We propose PAVE (Perception, Assessment, Verdict, Emulation), a novel four-module cognitive architecture that addresses this gap end to end: (i) Perception extracts a structured context with explicit authority distance, peer behaviors, and severity-tagged situational cues; (ii) Assessment scores the context along five scalars including an explicit legitimacy judgment that checks necessity, proportionality, and absence of alternatives; (iii) Verdict decides to comply or violate under a hard legitimacy gate, with a per-agent threshold elicited from the persona; (iv) Emulation enacts the verdict and scopes the violation to the rule the trigger justifies. We instantiate PAVE in Voville, a tile-based traffic environment forked from Smallville, and evaluate across three scenarios, four LLM backbones, and a focused ablation. PAVE agents satisfy four properties simultaneously: legitimate violation (only when a trigger justifies it), authority deference (officer instructions override even high legitimacy), bounded scope (violations confined to the targeted rule), and recovery (baseline restored once the trigger ends). PAVE agents make more structured and interpretable decisions than vanilla across all four properties, and human evaluators rate them as more plausible. Ablating the legitimacy gate reproduces vanilla-like failures. We release Voville, the PAVE prompts and code, and the evaluation pipeline.

---


### 150. [MAM-CLIP: Vision-Language Pretraining on Mammography Atlases for BI-RADS Classification](https://arxiv.org/abs/2605.19359)

**<font color=#1a73e8>作者：</font>** Halil Ibrahim Gulluk, Olivier Gevaert  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning methods have demonstrated promising results in predicting BI-RADS scores from mammography images. However, the interpretation of these images can vary, leading to discrepancies even among radiologists. Given the inherent complexity of mammograms, training classification models solely on image labels often yields limited performance. To address this challenge, we curated 2313 mammogram images and their corresponding captions from two mammography atlases. Our proposed approach employs a multi-modal model that uses a pretrained PubMedBERT as the language component. By training this model on image-text pairs with contrastive learning, we enable the vision encoder to absorb the rich information contained in the captions, thereby improving its understanding of mammography findings. We then fine-tune the vision encoder on two datasets for BI-RADS prediction, achieving superior performance compared with models trained without this pretraining, particularly when labeled samples are scarce. The improvement in the 3-class average F1 score ranges from +1% to +14%: a +1% increase with 40K training samples, and a +14% increase with 1K samples. Furthermore, our experiments reveal that 2K image-text pairs from mammography atlases can be more informative than 2K labeled samples for label prediction, with an average margin of +1.1% when more than 10K training samples are available. Overall, our work provides a vision-language model for mammography and highlights the value of textual information from mammography atlases. In addition, we publicly release preprocessed mammography images of the TEKNOFEST dataset. The training code, pre-trained model weights, data extraction scripts, and the released dataset are publicly available at: this https URL

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-338](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
