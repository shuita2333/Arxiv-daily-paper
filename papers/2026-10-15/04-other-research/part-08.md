# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 351. [Interpretable Graph Partitioning for Spatial Prediction](https://arxiv.org/abs/2610.16063)

**<font color=#1a73e8>作者：</font>** Yuta Shikuri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial prediction estimates unobserved values from spatially distributed observations. Although flexible predictive models are increasingly available, their practical use remains limited when interpretability is essential. In this study, we formulate a graph partitioning problem to construct a global surrogate model that approximates black-box predictions with simpler representations. Specifically, we select connected subgraphs to minimize within-cluster residuals in vertex-level predictions. Although this formulation can be viewed as a variant of spatial regionalization, it operates on model-based predictions at individual locations rather than predefined areal units. With many locations, this point-level formulation may produce artificial connections between regions, reducing interpretability. We therefore introduce a constraint that excludes such connections while retaining flexible partition boundaries. We theoretically analyze how this constraint affects the resulting partition. We also develop a computational procedure for adjusting partition boundaries. Experimental results show that the proposed method yields spatially coherent partitions with flexible boundaries.

---


### 352. [PIGEONS: Incremental Long-Video Captioning with Persistent Identity Gallery and Evolving Overarching Narrative Summary](https://arxiv.org/abs/2610.16066)

**<font color=#1a73e8>作者：</font>** Xinlong Chen, Weihong Lin, Yuanxing Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detailed video captioning has become an essential semantic interface for multi-modal understanding and generation. While existing methods mainly target short videos, extending them to long videos remains challenging, primarily due to limited context windows of current video understanding models. A naive solution is to adopt segment-wise captioning followed by concatenation, yet this paradigm often suffers from inconsistent subject references and fragmented long-range narratives. To mitigate these issues, we introduce PIGEONS, an incremental long-video captioning model built upon a Persistent Identity Gallery and an Evolving Overarching Narrative Summary. Before caption generation, PIGEONS scans the entire video to construct an identity gallery that captures key subjects along with their visual references, thereby providing a stable referential anchor. The model then performs clip-by-clip captioning conditioned on the persistent gallery and an evolving overarching narrative summary, which compactly maintains and updates essential long-range contextual information after each captioning step. To enable these capabilities, we develop a three-stage training strategy that integrates supervised fine-tuning and reinforcement learning. Extensive experiments demonstrate that PIGEONS markedly improves long-video captioning performance, achieving superior accuracy, completeness, and subject referential consistency over existing methods, while maintaining competitive performance on short-video captioning.

---


### 353. [Understanding and Reducing Misalignment in Persuasion Optimization](https://arxiv.org/abs/2610.16070)

**<font color=#1a73e8>作者：</font>** Boyi Wei, Ruta Desai, Peter Henderson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier models are now trained for complex multi-agent tasks, from running a company to engaging in negotiations. These tasks necessitate training models to be persuasive. But what does this optimization pressure mean for model alignment? In this work, we study how reinforcement learning (RL) training for persuasion affects models' use of misaligned strategies such as evidence fabrication and belief coercion, and what techniques can reduce such misalignment. We find that optimizing sender models solely for receiver belief shifts causes the average number of distinct misaligned strategies used per game to increase by more than 25%, and fabrications per game increase to more than 4 times relative to pre-RL models. We compare various mitigation approaches, including stronger strategy guidance, clean demonstrations, penalizing misaligned strategy usage, and improving the model's ability to detect fabrications. We find that navigating the persuasiveness-misalignment trade-off in this setting is challenging, with the best trade-offs coming from combining guidance on aligned persuasion strategies with reward penalties on misalignment. Overall, our work provides a testbed for assessing misalignment stemming from RL-based persuasion training and shows concrete paths for reducing misalignment. Importantly, it highlights that without direct intervention, persuasion-involved RL environments are likely to naturally lead to large increases in the use of misaligned strategies.

---


### 354. [Beyond Single-Pathogen Forecasts: Predicting Shared Respiratory Hospital Burden from Influenza, COVID-19, and RSV](https://arxiv.org/abs/2610.16074)

**<font color=#1a73e8>作者：</font>** Gaurob Saha, MinJae Woo, Lior Rennert  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Co-circulating influenza, COVID-19, and respiratory syncytial virus (RSV) create a shared hospital-admission burden, because beds, staff, testing capacity, and respiratory support are allocated to total demand rather than to one pathogen at a time. This makes respiratory forecasting a target-construction problem as well as a modeling problem: disease-specific forecasts preserve attribution, whereas hospitals also need a single planning signal for combined burden. We developed a supervised 1- to 4-week-ahead framework for weekly admissions and compared two total-burden strategies: summing independently generated pathogen-specific forecasts and forecasting the combined admission target directly. Evaluation included retrospective held-out testing and prospective operational forecasts issued before the corresponding admission weeks were observed, with performance summarized using MAE and Percent Agreement (PA; the smaller of model-generated and observed counts divided by the larger). In retrospective total-burden evaluation, the combined-burden model had PA values of 0.85, 0.78, 0.74, and 0.76 and MAE values of 80.63, 200.09, 183.97, and 156.13 from week 1 to week 4 ahead, compared with summed-forecast PA values of 0.85, 0.80, 0.69, and 0.69 and MAE values of 100.14, 200.06, 205.65, and 217.57. Prospectively, the combined-burden model had higher PA and lower MAE at all four horizons, with the largest separations at weeks 3 and 4 ahead. These results support layered respiratory forecasting: pathogen-specific forecasts remain necessary for etiologic interpretation, while combined-burden forecasts better align with hospital preparedness and shared-capacity planning.

---


### 355. [Regime-Aware Router Learning for Multi-Domain Medical Image Generation with Diffusion Experts](https://arxiv.org/abs/2610.16082)

**<font color=#1a73e8>作者：</font>** Yaoshuai Ma, Wei Yao, Yongxiang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Heterogeneous medical image data motivate domain-specialized diffusion experts, but expert specialization alone does not determine how their predictions should be combined during sampling. Learning a global router is particularly challenging when the server has limited, potentially unrepresentative images. We study two router-learning strategies for a fixed expert pool. Server-Only learns input- and timestep-dependent expert assignments from server images with component labels. Anchor-Delta (AD) uses the same images and frozen experts to obtain additional evidence from denoising losses. It distills targets that combine this evidence with the current router's assignments, while a proxy gate controls a subsequent refinement step. Component labels describe data origin; expert losses measure empirical prediction performance. We evaluate these distinct signals through routing analyses and paired medical image generation. An AD-trained router improves generation metrics over Server-Only in a heterogeneous four-domain setting, and a separate server-data study shows gains in held-out routing over a corrected-routing comparator. Additional paired evaluations show that the effect of inference-time evidence mixing varies across benchmarks. These findings establish server-data availability and expert performance as distinct considerations in learning routers for multi-domain diffusion models.

---


### 356. [Confidential Error-Correcting Codes](https://arxiv.org/abs/2610.16087)

**<font color=#1a73e8>作者：</font>** Tianrui Wang, Anyu Wang, Tianshuo Cong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce Confidential Error-correcting Codes (CECs), a new cryptographic primitive that enables reliable decoding from perturbed codewords while preserving message confidentiality. We formalize this primitive through three security properties: confidentiality, robustness, and soundness. To realize this goal, we develop a general framework for constructing CECs based on a Randomness-Security Separation (RSS) structure, which first encodes a nonce to introduce randomness and then masks the encoded payload with a pseudorandom function. Based on our RSS framework, we instantiate CECs, called Conc-CEC, using concatenated Reed-Muller and Reed-Solomon codes. The resulting Conc-CEC admits provable guarantees for all three properties. Notably, compared to PRCs (CRYPTO'24), another recent cryptographic primitive with error-correcting capability, CECs achieve significantly stronger concrete security guarantees under practical parameter settings. As a primary application of CECs, we further present CECMark, a watermarking scheme for AI-generated images. Our experiments on real-world generative image models show that CECMark consistently outperforms state-of-the-art watermarking methods, including Gaussian Shading (CVPR'24), PRCMark (ICLR'25), and T2SMark (NeurIPS'25). In particular, CECMark achieves higher robustness across all 56 evaluated perturbations and ensures a false positive rate below $10^{-5}$ without introducing side effects. Taken together, our work lays a novel cryptographic foundation for trustworthy watermarking schemes that, for the first time, unify provable security guarantees with strong practical reliability.

---


### 357. [Memorization in image classification: test set behavior and scaling laws](https://arxiv.org/abs/2610.16090)

**<font color=#1a73e8>作者：</font>** Jeevesh Attri, Florentin Guth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are capable of both learning generalizing solutions on natural tasks and memorizing arbitrary mappings. We argue that understanding the former requires understanding the latter, which is much less studied. In what ways do networks that generalize or memorize differ in their behavior or their training dynamics? Do memorizing networks simply function as a lookup table where input-output mappings are stored independently? We investigate these questions in the context of CNNs trained on image classification tasks with randomized labels or pixels. We first study the behavior of such memorizing networks on unseen images. We find that independently initialized networks trained on the same random labels learn different predictive functions: they make different predictions on test examples, in contrast with generalizing networks. We then examine the effect of dataset size on memorization through the required network capacity and training time to interpolate the training set. Counter-intuitively, we find that the number of presentations of a given example required for complete memorization can decrease with dataset size even when input-output pairs share no common structure. Although memorizing networks do not learn a universal solution, they exhibit interesting behaviors which call for further investigations into the underlying mechanisms.

---


### 358. [HDKEM: Authentication Allocation for Deniable Hybrid Key Exchange](https://arxiv.org/abs/2610.16100)

**<font color=#1a73e8>作者：</font>** Kazi Hassan Shakib, Muhammad Asfand Hafeez, Arslan Munir  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deniable authenticated key exchange (DAKE) establishes a shared key without leaving transferable evidence that a party participated. We study DAKE protocols that authenticate each fresh session with one ring signature and show that their deniability mechanisms fall into three authentication allocations: sharing an authentication witness, hiding the signing witness under a fixed ring, or varying the verified ring between real and simulated executions. For fixed-ring protocols, witness hiding yields a necessary relation between the ring signature's witness-indistinguishability gap and the protocol's $(\mu,\delta)$ deniability parameters. We instantiate witness hiding in HDKEM, a three-slot hybrid that combines ML-KEM-768, X25519, and an optional pairwise information-theoretic source through a split-key PRF. HDKEM binds all public session values, including a QKD key identifier when present, into authentication and key derivation. Under the stated component models, it achieves eCK key indistinguishability, forward secrecy, and strong local deniability.
We evaluate HDKEM with FalconRS and Gandalf. Across 2,000 primitive operations, median signing/verification times are 9.20/1.02 ms for FalconRS and 18.61/0.97 ms for Gandalf in our reference environment. In source-backed mode, the corresponding TCP-application costs are 8,607 B and 8,555 B per handshake. A separate 500-session server experiment exercises the complete FalconRS source-backed path and reports a median server time of 16.29 ms including local I/O.

---


### 359. [Silence and Noise: Resolving Suppression and Overvaluation in Multimodal Entity Alignment](https://arxiv.org/abs/2610.16106)

**<font color=#1a73e8>作者：</font>** Xizhe Zhang, Jingfeng Zhang, Meng-Fen Chiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal entity alignment (MMEA) is fundamental to integrating heterogeneous knowledge graphs (KGs), yet existing paradigms remain critically vulnerable to incomplete modalities and cross-graph structural asymmetries. This paper exposes a fundamental oversight in current MMEA research: treating feature missingness and topological discrepancies as isolated preprocessing or denoising challenges, which overlooks their destructive coupling during multimodal fusion. We systematically formulate and evaluate two newly identified failure modes: 1) Detail Missing (DM)-induced overvaluation, where the absence of local modality details causes models to overemphasize uninformative, blurred representations; and 2) Context Imbalance (CI)-induced suppression, where topological discrepancies across KGs allow dense structural contexts to overwhelm weaker but highly discriminative modal signals, triggering high-level semantic drift. To break this cycle of degradation, we introduce ALMEA, a generative and calibration framework that establishes a bidirectional feedback loop between low-level feature reconstruction and high-level latent space alignment. Specifically, Cross-Modality Imputation (CMI) synthesizes missing modality details to mitigate overvaluation, while Latent Semantic Calibration (LSC) aligns cross-graph joint embeddings to suppress topology-driven semantic drift. Under sparse supervision, we develop Controlled Iterative Selection (CIS) to adaptively acquire representative and diverse pseudo-labeled pairs, optimizing latent calibration under constrained budgets. Extensive evaluations on standard benchmarks demonstrate that ALMEA consistently outperforms state-of-the-art baselines. At a 20% supervision rate, ALMEA yields substantial absolute improvements of up to 5.20% in MRR and 6.40% in Hits@1, maintaining robust gains across higher supervision thresholds.

---


### 360. [GUIDE: Computationally Augmented Consensus for Trustworthy Clinical Practice Guidelines](https://arxiv.org/abs/2610.16108)

**<font color=#1a73e8>作者：</font>** Yuanfan Lin, Jie Di, Xujin He 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Maintaining up-to-date clinical practice guidelines (CPGs) is essential for evidence-based medicine, but rapid evidence growth and complex expert consensus formation limit timely updates. We developed GUIDE, a multi-agent copilot system for human-AI collaborative guideline generation and updating. GUIDE delegates labor-intensive tasks to specialized AI agents while preserving expert judgment and final arbitration. In 12 NICE ophthalmology datasets, GUIDE achieved 88.85% literature recall, 86.06% alignment in certainty-of-evidence ratings, and 91.67% recommendation agreement, requiring 162.17 minutes per dataset on average (28.68% human intervention). Performance remained stable across 20 additional datasets from cardiology, endocrinology, gastroenterology, and respiratory medicine. Ablation analysis showed that removing expert intervention reduced performance in judgment-intensive steps such as Risk-of-Bias assessment. In six post-cutoff datasets, GUIDE maintained robust end-to-end performance on unseen evidence. Prospective real-world validation showed that GUIDE reduced expert workload and produced more clinically acceptable recommendations than the original decade-old guideline (mean score, 3.73 vs. 1.53; agreement, 66.7% vs. 13.3%), with outcomes comparable to human-only updating (P = 0.588) but substantially less time and effort. GUIDE offers a practical framework for timely, trustworthy, expert-centric guideline development and validates computationally augmented consensus.

---


### 361. [Constructed regional photovoltaic generation fields improve ultra-short-term distributed solar forecasting](https://arxiv.org/abs/2610.16110)

**<font color=#1a73e8>作者：</font>** Dayin Chen, Xiaodan Shi, Xin Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ultra-short-term forecasting of densely distributed photovoltaic (PV) systems remains challenging because external meteorological and satellite products may not adequately resolve rapid local variations, while heterogeneous PV systems exhibit different generation responses under similar atmospheric conditions. Meanwhile, dense PV fleets provide spatially distributed measurements that reveal regional generation dynamics. Here, we reformulate fleet-level PV forecasting from modeling discrete station time series to predicting explicit, spatially structured regional PV generation fields. We develop SatPV-Field, a regional-to-local forecasting framework that transforms distributed PV measurements into image-like generation fields and models their spatiotemporal evolution. By combining historical PV fields with satellite-derived future shortwave radiation guidance and meteorological forecasts, the framework predicts future regional generation states, which subsequently provide location-specific guidance for individual-station forecasting. Experiments involving 496 distributed PV systems, including 446 source stations and 50 held-out target stations, demonstrate that these regional fields can be effectively forecast and used to improve station-level predictions. The proposed approach reduces station-level MAE by approximately 10.0% relative to the best-performing single-station temporal baseline and by 2.5% relative to a graph-based regional forecasting approach using the same source fleet. These findings establish an explicit spatial-field modeling paradigm that connects regional generation dynamics with individual-site forecasting.

---


### 362. [Geometry-Guided Semantic Reconstruction for 3D Instance Segmentation](https://arxiv.org/abs/2610.16122)

**<font color=#1a73e8>作者：</font>** Yuanhao Su, Shaofeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D instance segmentation requires representations that are both geometrically structured and semantically discriminative. Pure 3D encoders model spatial structure well but often lack strong appearance semantics, while directly lifting 2D priors into 3D by concatenation injects rich semantics without ensuring that they align well with the underlying 3D structure. In this paper, we address this problem by formulating 2D-to-3D semantic transfer as a \textbf{masked semantic reconstruction} task. Specifically, we mask a subset of background lifted 2D priors and train the 3D encoder to recover the missing semantic priors, providing explicit supervision for distilling rich 2D semantics into the 3D backbone. We further propose \textbf{geometry-modulated semantic injection}, which uses raw 3D geometry to modulate lifted 2D priors before sparse encoding, so that geometry explicitly controls semantic injection and alleviates the distribution gap between 2D semantic features and 3D geometric features. Experiments on two baseline frameworks demonstrate that the proposed method achieves state-of-the-art results in both full-data and few-shot settings on ScanNetV2 and ScanNet200. Code is publicly available at this https URL

---


### 363. [Imitation Holds a Key to Evolution: Localized Repair and Verified Skill Acquisition for Adaptive Agents](https://arxiv.org/abs/2610.16125)

**<font color=#1a73e8>作者：</font>** Kai Hu, Hua Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent can retain successful trajectories without learning which part of an experience should repair a new discrepancy. We formulate passive imitation (PI) as an architectural loop that localizes a violated contract, extracts a local goal, proposes an effect-matched skill, tests a small patch, and retains evidence after full-task verification. We instantiate this loop as a deterministic symbolic controller and analyze its finite repair-query complexity under explicit identifiability and noninterference assumptions. Across ten simulated tool worlds, PI solves all 600 cold held-out composition tasks with three allowed small trials, compared with 6.17% for a whole-trajectory control, while an equally expressive compositional repair control matches PI. On an unseen tool revision, PI achieves 70.0% success versus 24.0% without small trials and 79.0% with self-trial enumeration; an exploratory 24-task adaptation stream subsequently raises first-submission success to 100%, supporting a limited correction-and-retention mechanism rather than a unique incentive advantage or general intelligence. The CPU-only implementation, integrity checks, and reproducible results are available at this https URL.

---


### 364. [A Concept-informed Interpretable Artificial Intelligence Framework for Breast Ultrasound Diagnosis](https://arxiv.org/abs/2610.16128)

**<font color=#1a73e8>作者：</font>** Shengzhou Zhong, Ziying Wang, Liang Li 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing artificial intelligence systems for breast ultrasound rely primarily on image-driven prediction, with limited incorporation of the knowledge from the Breast Imaging Reporting and Data System (BI-RADS) and the intermediate assessment processes underlying radiologists' workflow, thereby constraining their interpretability and alignment with clinical practice. We curated, to our knowledge, the largest multicenter collection of breast ultrasound images paired with structured BI-RADS descriptors, comprising 9,941 patients across 20 independent datasets. Across 14 testing datasets, IBUS demonstrated consistent generalization performance across different clinical centers and imaging conditions. Incorporating BI-RADS descriptors enabled fine-grained risk stratification, while cross-checking predicted BI-RADS grades against malignancy probabilities identified internally discordant predictions that may warrant additional clinical review. In a reader study involving eight radiologists, IBUS assistance increased diagnostic sensitivity among both junior and senior readers, with the potential of guiding radiologists to make targeted revision in risk stratification. Overall, IBUS exhibits its potential as a second-stage decision-support system that complements radiologists by providing additional risk estimates and interpretable evidence for diagnostically challenging cases. The demo video of IBUS platform is publicly available at this https URL.

---


### 365. [XForecast: The KDD 2026 Finance Day Challenge on News-Grounded Financial Forecasting](https://arxiv.org/abs/2610.16131)

**<font color=#1a73e8>作者：</font>** Jaehoon Lee, Jun Seo, Seunghan Lee 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial forecasting has traditionally relied on numerical time-series (TS) signals, while textual information such as news remains largely underutilized. We introduce XForecast, a benchmark and competition for news-grounded financial forecasting, where the task is to predict stock price movements four weeks ahead using both historical price data and paired news signals. XForecast combines stock price data with curated financial text generated using FinTexTS, a multimodal dataset generation method. It covers 100 large-cap stocks from 2019--2023, with training on 2019--2022 and evaluation on 2023. To better evaluate models that leverage textual signals, we adopt a weighted hit rate metric that places greater emphasis on instances where news information is expected to have stronger influence. The XForecast Challenge, hosted on Kaggle as part of KDD 2026 Finance Day, aims to benchmark methods for integrating financial TS and textual information.

---


### 366. [ProMoDD: Dataset Distillation for 3D Human Motion via Prototype-Conditioned Diffusion Models](https://arxiv.org/abs/2610.16134)

**<font color=#1a73e8>作者：</font>** Yijin Wei, Yawen Zou, Wenqi Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation (DD) aims to retain the training utility of a large dataset in a much smaller set of examples. For skeleton-based action recognition, this requires capturing discriminative motion variation without disrupting the geometry and temporal continuity of articulated bodies. Directly optimizing joint coordinates can violate these constraints, while plausible motion generation alone does not ensure useful training examples. We propose Prototype-Conditioned Motion Dataset Distillation (ProMoDD), which conditions a motion diffusion model on class-wise prototypes of temporally resolved recognition features. We further tailor diffusion training to motion data, enabling the generator to model both skeletal configurations and their temporal evolution. We then construct each compact training set through budget-aware hybrid selection: representative real sequences cover densely populated regions of the pooled recognition space, while selected generated candidates complement them in less-populated regions. This couples prototype-guided generation with feature-space selection, balancing the reliability of observed motions with the variation of synthesis under a fixed per-class sequence budget. Across five difficulty-stratified subsets of the single-person classes in NTU RGB+D 60, ProMoDD achieves its largest gains under tight distillation budgets, reaching 40.32% top-1 accuracy on Full49 with three sequences per class, 4.57 percentage points above class-wise k-means. These gains reflect the complete framework. The same distilled sets train ST-GCN, MS-G3D, and CTR-GCN without regeneration.

---


### 367. [All-St3R SLAM: Real-time RGB Dynamic SLAM with Pixel-wise Motion Masking](https://arxiv.org/abs/2610.16143)

**<font color=#1a73e8>作者：</font>** Yewon Kim, Paul Hongsuck Seo, Sang Chul Ahn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> SLAM (Simultaneous Localization and Mapping) is a core technology in autonomous systems that enables them to estimate their own position and build a map of unknown environments simultaneously. SLAM systems in dynamic environments are of great practical importance. However, existing dynamic SLAM approaches still have several limitations like over-removal and high computational costs. To address these limitations, we propose a real-time RGB Dynamic SLAM framework that precisely removes moving objects at the pixel level without relying on predefined labels or segmentation models. Our system combines pixel motion predicted by ego-motion using DUSt3R with point tracking from All-Tracker, removing only actually moving pixels by analyzing discrepancies between the two motion sources. Unlike object-level masking methods, our approach eliminates only currently moving regions, allowing temporarily static parts to be utilized for tracking. Operating at approximately 10 FPS, the system achieves real-time performance on standard 30 FPS video streams by subsampling every 3 frames. Relying solely on RGB inputs, this significantly improves upon state-of-the-art dense dynamic SLAM approaches (0.5-3 FPS), presenting a highly practical solution.

---


### 368. [Pollard: Governed Semantic Execution Trees for Framework-Independent AI Agent Control and Replay](https://arxiv.org/abs/2610.16145)

**<font color=#1a73e8>作者：</font>** Muntaser Syed, Marius C. Silaghi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent frameworks can persist checkpoints, trace tool calls, and limit resource use, but these facilities often assign different identities to execution, governance, and replay. We present Pollard, a framework-independent runtime based on governed semantic execution trees. A step identity commits to canonical input, kind, attempt, and parent identity; the same tree records completion, refusal, resource settlement, and branch history. Strict replay returns a verified stored result without invoking the wrapped operation, while a transactional store coordinates reservations across concurrent workers. Under a signed deterministic freeze, two state-model replicas each executed the evaluation transitions without an invariant violation, retained-lease PostgreSQL groups were tested against exact limits, strict replay avoided external calls, and all semantic mutations were detected with no false alarms on the controls. A multi-pair framework matrix preserved reference behavior and verified the trees. A separate cost-capped hosted study exercised live provider paths, and every completed Pollard trial produced a verified tree. Together, the studies support the core mechanisms under explicit lease, boundary, and seal-custody assumptions.

---


### 369. [BARTER: Compact Dynamic Sparse Training with Standard Dense Kernels](https://arxiv.org/abs/2610.16147)

**<font color=#1a73e8>作者：</font>** Yueyuan Sui, Payal Mohapatra, Qi Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic sparse training (DST) aims to reduce training costs while maintaining accuracy. Existing DST methods mask out parameters but keep matrix dimensions unchanged. Training speedups therefore depend on specialized support, such as sparse kernels. We introduce BARTER, a structured DST framework that reduces training cost using standard dense kernels by keeping training tensors physically compact while dynamically reallocating capacity across layers. Unlike existing works that require computing gradients for all parameters, BARTER instead uses statistics collected only from active units during ordinary backpropagation to prune and clone attention heads and feed-forward channels under separate fixed global budgets. At each topology update, it resizes the affected parameter tensors and remaps their optimizer states, so subsequent training steps operate directly on the compact model. Training and fine-tuning experiments with Transformer-based vision models on two image classification benchmarks at densities from $0.1$ to $0.7$ show competitive Top-1 accuracy relative to full-tensor DST baselines. On an NVIDIA L40, BARTER achieves speedups of up to $6.29\times$ in measured training segments and reduces peak allocated GPU memory by up to $81.3\%$ relative to these implementations. An iPhone 13 Pro Max training benchmark additionally shows a $2.78\times$ speedup over the full-tensor DST baseline.

---


### 370. [ML-Assisted Power Side-Channel Attacks on ML Accelerators in Shared FPGAs](https://arxiv.org/abs/2610.16164)

**<font color=#1a73e8>作者：</font>** Anthony Etim, Kenan Erol, Jakub Szefer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud providers offer on-demand access to Field-Programmable Gate Arrays (FPGAs), and multi-tenant FPGAs let multiple users share one device to improve utilization. This sharing introduces security risks: an adversary co-located with a victim on the same FPGA can mount power side-channel attacks against the victim's Machine Learning (ML) accelerator. Prior on-chip attacks on such accelerators based on Time-to-Digital Converter (TDC) sensors have recovered only small, MNIST-scale grayscale inputs, including with ML-assisted reconstruction. This work is the first on-chip, TDC-based attack to produce full-scale color reconstructions of ImageNet-scale inputs, by combining ML-based upscaling and recoloring with TDC measurements of a remote victim's ML accelerator. We frame this as a proof-of-concept leakage study: the victim implements the first convolution layer of a CNN processing 224x224 ImageNet inputs on a shared FPGA, which we isolate to characterize the input-dependent leakage, and we quantify how much of each reconstruction reflects genuinely recovered information versus ML-generated post-processing. As a preliminary countermeasure, we study a pixel-substitution defense that replaces each pixel value, within a fixed intensity budget, with one of different Hamming Weight, producing a different TDC signature. We find that this transformation costs the victim's own model more accuracy than it costs the attacker and, because it applies the same fixed, publicly reconstructable mapping to every image, is largely defeated by an attacker retrained on the transformed data; robust defenses will require randomized or input-dependent transformations.

---


### 371. [Esports World Model Dataset](https://arxiv.org/abs/2610.16166)

**<font color=#1a73e8>作者：</font>** Weiyu Ma, Zeyuan Gong, Xuhui Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive world models must capture how multiple participants jointly change a shared environment while observing different parts of it. Competitive games make this challenge concrete: players cooperate and compete, while fog of war, team vision and camera placement determine what each can see. Modeling these interactions requires data that connect individual observations and actions to shared state and events. We introduce the Esports World Model Dataset (EWM), a collection of human gameplay spanning StarCraft II, Dota 2 and Counter-Strike 2, with 3,053 games and maps and approximately 4,880 player-view hours, including estimated hours for the ongoing CS2 extension. It includes 4,628 completed StarCraft II views, all ten perspectives for 303 Dota 2 matches, and up to ten views per round in CS2. Across these views, replay-clock alignment connects rendered video with game-native actions, structured state and events from the same match. The three games expose complementary observation conditions: private fog of war, shared team vision and first-person viewpoints. In StarCraft II, player-specific entity records further distinguish live observations from remembered snapshots and link co-observed entities across opposing views. Together with temporal alignment, these records allow researchers to distinguish legitimate information differences from disagreement about shared state. By connecting human decisions, shared dynamics and player-specific information, EWM supports research toward jointly controlled multiplayer world models and interactive environments populated by teammates and opponents learned from human play.

---


### 372. [Interactive 4D Volumetric Liquid Forecasting under Moving-Solid Interaction](https://arxiv.org/abs/2610.16167)

**<font color=#1a73e8>作者：</font>** Jongwon Ryu, Sunjae Yoon, Junyeong Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose the task of Interactive 4D Volumetric Liquid Forecasting: predicting the spatiotemporal evolution of a future dense 3D liquid velocity field conditioned on how a solid object moves through it. This task provides an upstream physical forecasting primitive for systems that need to reason about motion-conditioned liquid response, including robotic liquid manipulation, digital twins, and rigid-fluid video generation. Existing works have made efforts in predicting flow around static or prescribed solid geometries and synthesizing visually plausible fluid motion. Yet these approaches provide limited coverage for interactive liquid dynamics, as they are not capable of forecasting how a moving solid induces a future full-domain liquid response. In this forecasting scenario, the hydrodynamic effect is condensed near an evolving liquid-solid interface, but the prediction target is a global spatiotemporal rollout. To address this challenge, we propose a two-level recurrent forecasting framework, TIDE/TIDES: TIDE isolates localized interface-driven forecasting, while TIDES adds transport-aware coupling and explicit stabilization to reduce accumulated rollout error. Across adapted neighboring baselines, controlled component ablations, motion/size OOD tests, and long-horizon evaluation, TIDES achieves the best forecasting performance and the ablations identify localized interaction, transport coupling, and stabilization as the key contributors. Together, our task formulation, benchmark, and TIDE/TIDES study establish a controlled foundation for moving-solid-conditioned dense liquid forecasting. The code is publicly available at this https URL.

---


### 373. [DeepThink: A Conceptual Model for Knowledge-Addressable Recurrent Language Modeling](https://arxiv.org/abs/2610.16171)

**<font color=#1a73e8>作者：</font>** Weiguo Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This manuscript presents DeepThink, a knowledge-addressable framework for recurrent language modeling. A Knowledge Bank stores typed Knowledge Units, a Knowledge Activator selects units from the current execution state, Knowledge Assembly produces an executable configuration, and a Shared Thinking Operator updates that state. An output stage then organizes generation. This organization exposes knowledge capacity, activation width, and recurrent depth as separate design variables, supporting both complete parameter packages and fine-grained expert or low-rank modules. We formalize the interfaces and their execution semantics, including state-dependent selection, parameter-space assembly, and thinking followed by generation. For compatible templates and complete runtime-state configurations, we establish an exact Fixed-Schedule Realization of an existing fixed-depth model. Exact shared-base reparameterization and pretrained output-tail reuse provide complementary initialization constructions. Together, these results define a route from pretrained models to dynamically selected and assembled recurrent computation. A synthesis of conditional computation, recurrent models, modular parameters, and knowledge interfaces positions DeepThink within the research landscape and identifies the design questions arising from their integration.

---


### 374. [Exploring Mixed Reality for Engagement in Robotics: A Comparison of Robot Control Methods](https://arxiv.org/abs/2610.16186)

**<font color=#1a73e8>作者：</font>** Samantha Edvell, Dinh Tung Le, Gavin Paul  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents a Mixed Reality (MR) robotics experience that provides an accessible introduction to interacting with a physical robot. The application combines a TurtleBot with a virtual animal-tending activity and three control methods: Joystick, Waypoint, and Path-Drawing. A mixed-methods user study with 10 participants investigated changes in robotics interest and confidence following the experience and how the control methods influenced engagement, workload, and preference. Confidence increased following the experience, with the exploratory analysis indicating a significant pre--post difference, while the increase in interest was not statistically significant. The control methods produced clear differences in perceived workload and ease of use, with Path-Drawing generally more demanding and difficult to use. Joystick was preferred by eight of ten participants and was associated with better perceived performance and lower frustration. However, no statistically significant differences were detected in the other engagement dimensions, suggesting that the most preferred method was not necessarily more engaging across all aspects of the experience. These findings highlight the importance of considering both usability and engagement when designing how users interact with robots in introductory MR experiences.

---


### 375. [VGGA: Geometry-Grounded Autoencoder for Video Generation](https://arxiv.org/abs/2610.16204)

**<font color=#1a73e8>作者：</font>** Chaofan Gan, Yian Zhao, Shijie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoencoders are the core component of latent video generative models, compressing high-dimensional videos into compact latent spaces for downstream generation. However, existing video autoencoders are primarily optimized for pixel-level reconstruction, providing limited supervision for learning structured latent representations. We argue that videos should not be treated merely as signals to be reconstructed, but rather as 2D projections of dynamic 3D worlds that exhibit explicit and well-structured geometric properties. Building on this insight, we propose \textbf{V}ideo \textbf{G}eometry \textbf{G}rounded \textbf{A}utoencoder (\textbf{VGGA}), a geometry-aware video autoencoder that explicitly incorporates geometric constraints into the reconstruction process. Specifically, VGGA grounds the learned representations along three complementary geometric dimensions: \emph{Structural Depth}, \emph{Motion Correspondence}, and \emph{Projective Warping}. These objectives are unified within a Video Geometry Decoder, which employs a shared spatio-temporal upsampling trunk to jointly optimize geometric learning and RGB reconstruction. Through these geometry-grounded objectives, VGGA encourages the latent representations to capture the underlying 3D structure and motion of dynamic scenes. VGGA consistently improves video generation across both geometry-centric and human-motion domains, reducing gFVD by 28.1\% on RealEstate10K and 37.7\% on Taichi-HD. Notably, these substantial generation improvements are achieved while maintaining comparable reconstruction quality, demonstrating that geometry-grounded representation learning yields a more effective latent space for video generation.

---


### 376. [{Access|Use|Sustain|_}-ability: Exploration and Quantification of a Linguistic Structure and Its Use in HCI](https://arxiv.org/abs/2610.16206)

**<font color=#1a73e8>作者：</font>** Alarith Uhde, Paul Haimes  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Language plays a crucial role in research and technology design, throughout problem formulation, method descriptions, analysis of findings, and interpretation. In this paper, we focus on a particular, trending linguistic pattern in the Human-Computer Interaction literature, which we call -abilities. Examples include usability, accessibility, and explainability. These -abilities have become increasingly popular, with potential impacts on the discipline. They take a verb, turn it into an adjective, and finally nominalize it. We approach the -abilities phenomenon with a survey of the HCI literature between 1988 and 2025. All in all, we identified 349 different -abilities. Moreover, the use of -abilities notably increased since the late 2000s, both in the absolute number of different -abilities and the frequency of use of the most popular ones. The majority of -abilities we found had a positive notion, and most -abilities with a negative notion are prefixed counterparts of their positive opposite (e.g., un+sustainability). We critically discuss implications of their increased use. First, -abilities change the literal meaning of design intentions. For example, acceptability reduces the concrete verb accepting into only its potential (acceptable), and finally nominalizes it, claiming the existence of acceptability as a somewhat stable and real, abstract characteristic of a technology. Second, the prefix-based opposite construction can weaken the design goal. Un+sustainability avoids clarification of the -ability's meaning (here e.g., ecological or financial), and does not spell out the expected impact of designs that are not sustainable (e.g., the destruction of nature). Future work should compare the use of -abilities in English with other languages to better understand the ways in which they transform meaning.

---


### 377. [MP-MNCA: Morphology-Prior Masked Neighbor Cross-Attention for Efficient Spatial Domain Identification](https://arxiv.org/abs/2610.16212)

**<font color=#1a73e8>作者：</font>** Sidharthan Sivacoumar Chitra, Sanjeev Manivannan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics jointly captures molecular state, tissue morphology, and spatial organization, yet spatial-domain methods are typically compared only at late training checkpoints, obscuring differences in convergence efficiency. We introduce MP-MNCA, a morphology-prior masked neighbor cross-attention framework that preserves the full 3,000 dimensional highly-variable-gene representation while selectively routing molecular information across spatial neighbors, with histological similarity incorporated as a continuous attention prior under a self-supervised masked neighbor-contrastive objective. Across 12 heterogeneous human dorsolateral prefrontal cortex (DLPFC) sections, MP-MNCA is evaluated against established spatial-domain baselines using both convergence trajectories and epoch-wise spatial-domain visualizations. Our results show that MP-MNCA (i) reaches coherent spatial-domain structure in substantially fewer training epochs, as reflected quantitatively by convergence curves and qualitatively by progressive spatial grids, and (ii) maintains strong clustering quality, achieving a mean peak refined ARI of 0.546 versus 0.549 for the strongest baseline (STAIG), while attaining the highest mean refined NMI of 0.657 versus 0.640. Moreover, MP-MNCA outperforms STAIG on 7 of 12 sections in ARI and 11 of 12 in NMI, demonstrating faster convergence without sacrificing spatial-domain quality.

---


### 378. [OneShot: Label-Efficient Detector Weighting for Time Series Anomaly Detection](https://arxiv.org/abs/2610.16219)

**<font color=#1a73e8>作者：</font>** Seunghan Lee, Jun Seo, Jaehoon Lee 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series (TS) anomaly detection (AD) lacks a universal detector, with the best choice determined by the series rather than by the algorithm. Existing methods therefore either select one detector for each series or average a pool of them. However, both assume that no label ever arrives, while a deployed monitor does receive them, since an operator confirms the alarms it raises. In this paper, we propose ONESHOT, which uses a single confirmed anomaly to weight the pool rather than to choose one detector from it. Specifically, we score each detector on the confirmed anomaly, and those scores become the weights of a soft mixture over the whole pool. We show that a single confirmed anomaly is enough to come close to the best detector for the series. Across 152 univariate and 73 multivariate series, ONESHOT outperforms the strongest single detector, averaging the whole pool, and even picking the best detector on the confirmed event. Code is available at: this https URL.

---


### 379. [When Participant Disjoint Validation Is Not Enough to Establish Generalization in Parkinson's Gait Classification](https://arxiv.org/abs/2610.16220)

**<font color=#1a73e8>作者：</font>** Md. Sifat, Sania Akter, Akif Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Participant-disjoint cross-validation prevents direct participant overlap, but it may still produce optimistic estimates when acquisition site and diagnosis are structurally dependent. We examined Parkinson's disease classification using 159 pressure-walkway summary features from 133 WearGait-PD participants, including 65 participants with Parkinson's disease and 68 controls. The cohort was non-factorial: two sites contained only one diagnostic group, whereas VA-Seattle was the only site containing both groups. In repeated participant-level nested cross-validation, site alone achieved an area under the receiver operating characteristic curve (AUC) of 0.955 plus or minus 0.003, exceeding the gait-feature model (0.882 plus or minus 0.014). Under the evaluated logistic-regression pipelines, adding gait features to site, age, and sex produced no measurable improvement in pooled discrimination. More site-controlled evaluations produced lower and imprecise estimates: VA-Seattle same-site AUC was 0.668 (95% bootstrap confidence interval 0.477 to 0.836), and the JHOC + Bayview-to-VA-Seattle transport stress test achieved 0.576 (0.375 to 0.770). Supporting within-diagnosis site-prediction and site-conditioned permutation analyses showed that the gait representation retained substantial acquisition-site structure. These findings indicate that participant-disjoint pooled validation did not isolate disease-related discrimination from site-associated variation. They encourage careful examination of site-label dependence and, where possible, support for pooled results through within-site or independent validation before broader claims are made about generalization across institutions.

---


### 380. [AutoNovo: Agentic Program Search Discovers Transferable Nucleic Acid Design Algorithms](https://arxiv.org/abs/2610.16232)

**<font color=#1a73e8>作者：</font>** Joel Shor, Subhashini Venugopalan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-silico optimization of nucleic acids relies on predictive oracles that imperfectly capture biological function, so sequences optimized against one model may exploit model-specific artifacts and fail to generalize to independent models. Recent studies have shown that not all designers generalize equally well to independent models. In this work, we use agentic program search to iteratively propose, execute, evaluate, and revise code for nucleic-acid designers. We describe the successful strategies used to prompt the search. AutoNovo designers achieved the best observed mean among the evaluated methods on 3/3 DNA-design tasks in terms of in-silico performance, and 6/6 transfer tasks in terms of independent models. The designers come from a family of discovered nucleic acid designers rather than a single universal best designer. We plan to release the resulting designers. These results are the first steps in creating nucleic acid designers that maximize cross-model generalization, and thus improving the odds that in-silico designed sequences reflect real biology.

---


### 381. [Seg2Click: Learning Pixel-Level Action Masks for GUI Visual Grounding](https://arxiv.org/abs/2610.16234)

**<font color=#1a73e8>作者：</font>** Jingchao Wang, Dingjiang Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding is a central challenge for GUI agents, requiring an instruction to be mapped to a target within a crowded screenshot. Coordinate generation with single-point supervision reduces a spatially extended target to one position, despite the presence of many valid click locations. Region-based patch scoring alleviates this ambiguity, but its spatial decisions remain tied to visual-token footprints that may span the target, neighboring controls, and background. To address these limitations, we propose Seg2Click, which reformulates GUI grounding as executable-region prediction: identifying where a click can validly execute the given instruction. Using bounding-box supervision, Seg2Click predicts an executable-region mask and computes the final click point through a deterministic rule. This formulation captures the spatial extent of valid click locations and enables finer localization beyond the visual-token grid, making it well suited to small, densely arranged controls without requiring a verifier or zoom-in pass. Experiments across five backbone configurations from two model families demonstrate the effectiveness of Seg2Click. Seg2Click-9B achieves 92.06\%, 94.10\%, and 55.22\% on ScreenSpot, ScreenSpot-v2, and ScreenSpot-Pro, respectively, while matched-backbone comparisons show improvements over both coordinate generation and patch-based grounding. Code will be available at this https URL.

---


### 382. [Reflected Proximal Dynamics for Accelerated High-Accuracy Log-Concave Sampling](https://arxiv.org/abs/2610.16248)

**<font color=#1a73e8>作者：</font>** Bo Yuan, Wei Guo, Yongxin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study sampling from $\pi(x)\propto\mathrm{e}^{-V(x)}$ on $\mathbb{R}^d$, where $V$ is $\alpha$-strongly convex and $\beta$-smooth with condition number $\kappa=\beta/\alpha$. For this problem, the proximal sampler preserves the target exactly and recovers overdamped Langevin dynamics in the small-step limit, but its Gaussian resampling step discards directional information. Underdamped Langevin dynamics retains such information through momentum to accelerate exploration, motivating a proximal construction that combines target preservation with directional persistence. We introduce \textit{reflected proximal dynamics}, which combines proximal sampling with an exact reflection of the auxiliary variable, conditional kinetic motion, and controlled refreshment. We develop two realizations: a flux-resampled underdamped half-turn and a persistent-momentum quarter-turn. From a warm start with constant $\chi^2$ divergence, both methods achieve total variation error $\varepsilon$ using $\widetilde O(\sqrt{\kappa}d^{1/4})$ expected oracle queries. We further remove the supplied warm-start assumption by combining either sampler with existing posterior samplers in a proximal initialization stage with an optimized coarse step size. Accounting for both initialization and sampling yields $\widetilde O(\kappa^{6/7}d^{1/4})$ expected oracle queries. In both regimes, the dependence on the target accuracy $\varepsilon$ is $\mathrm{polylog}(1/\varepsilon)$, making reflected proximal dynamics a promising framework for accelerated high-accuracy log-concave sampling.

---


### 383. [MFlowHOI: Whole-Body Human-Object Interaction Generation via Part-Aware MeanFlow](https://arxiv.org/abs/2610.16252)

**<font color=#1a73e8>作者：</font>** Qiang He, Yonghao Zhang, Yinda Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-body human-object interaction (HOI) generation requires coordinating body and finger motion, object trajectories, and time-varying contacts. Existing methods typically rely on iterative diffusion or test-time optimization, resulting in high inference costs. Direct one-step generation is highly desired in downstream applications due to efficient inference. However, it is challenging because these HOI components differ substantially in structure and scale. We present MFlowHOI, an efficient one-step framework for whole-body HOI generation. A Contact-Aware Multipart RVQVAE organizes body, hand, object, and contact signals into a structured latent space, with a shared decoder preserving their global coordination. An ST-DiT then models temporal and cross-part dependencies in this space and generates a complete interaction in a single MeanFlow evaluation. Predicted object-local contact correspondences further enable geometric refinement and interaction-preserving transfer to photorealistic 3D Gaussian avatars with different body proportions. Experiments demonstrate that MFlowHOI outperforms existing base generators in motion quality and text alignment while substantially reducing inference time.

---


### 384. [EgoWholeView: Camera-Only Head-Mounted Capture of Body and Bimanual Hand Motion for Embodied Demonstrations](https://arxiv.org/abs/2610.16256)

**<font color=#1a73e8>作者：</font>** Yaoqing Hu, Xuguo He, Daohan Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Head-mounted body and bimanual motion capture supports self-avatars, teleoperation, and embodied demonstrations. However, a single egocentric camera is vulnerable to a limited field of view, scale ambiguity, and hand-object occlusion. We present EgoWholeView, a wearable capture system of six synchronized wide-angle RGB cameras with a role-specialized pipeline. The outward views localize the rig in a world frame, while an overlapping downward pair independently predicts SMPL-X body and MANO hand parameters. Both predictors are adapted to egocentric fisheye data. To combine the two, reliability cues measured from the predictions themselves weight the fusion of body and hand joint rotations, while shape is aggregated across views and frames. The pair's baseline fixes metric scale, and triangulation recovers root translation. Relative to monocular prediction, fusion reduces PA-MPJPE by 3.7% for the body and 11.2% for the hands, and temporal refinement lowers angular-acceleration magnitude by 32.2% and 31.0%, respectively. On our six-camera recording, the pipeline produces body and hand states in a shared world frame using benchmark-fitted gates without retuning, and temporal refinement lowers hand acceleration magnitude by 41.08%. Using only RGB cameras and no third-person view, EgoWholeView offers a low-cost, portable route to egocentric interaction data.

---


### 385. [Hardware-Friendly Token-Group Activation Quantization for Low-Bit Mamba Super-Resolution](https://arxiv.org/abs/2610.16261)

**<font color=#1a73e8>作者：</font>** Jinwoo Chung, Jangho Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mamba-based super-resolution models are efficient alternatives to Transformer-based restoration backbones, but their low-bit post-training quantization remains challenging because selective scan, Mamba's input-dependent state-space operator, induces different activation ranges across spatial tokens. Thus, a single layer-wise clipping range poorly matches all tokens. We propose Token-Group Quantization, a hardware-friendly activation PTQ framework that statically approximates a hardware-unfriendly post-scan grouping oracle, where tokens with similar preferred clipping ranges are assigned to the same group. To avoid runtime post-scan grouping in static low-bit inference, a lightweight predictor infers the groups from pre-scan features available before the quantized scan path. During calibration, we form pseudo-labels by clustering post-scan activation descriptors that capture similar rounding--clipping behavior. At inference, the frozen predictor maps pre-scan features to groups and selects entries from offline-calibrated group-wise clipping-bound tables, without runtime statistics collection, dynamic clipping updates, or post-scan group assignment. To address low-bit restoration degradation, we further introduce a Frequency-Preserving Refinement (FPR) objective for clipping-bound calibration. FPR aligns Fourier amplitude and phase between full-precision teacher and quantized student outputs to preserve high-frequency structures. Across PTQ protocols, bit-widths, backbones, and tasks, our method consistently outperforms prior Mamba and SR PTQ baselines, transfers to Transformer SR and Vision Mamba classification, composes with rotation-based quantization, and achieves 2.23x speedup on Jetson Orin Nano over FP16. Code is available here.

---


### 386. [Spectral Considerations on Unsupervised Time-domain EEG Representation Learning with Deep Networks](https://arxiv.org/abs/2610.16264)

**<font color=#1a73e8>作者：</font>** David Aquilué-Llorens, Abel Puigseslloses, Angel Blanco 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is a non-invasive, scalable source of quantitative biomarkers for the early diagnosis of brain disorders, and deep representation learning has become a powerful paradigm for extracting information-rich latent features from raw signals. However, neural networks tend to under-represent high-frequency information, a concern that is especially acute for EEG given its oscillatory nature and characteristic $1/f^\chi$ power decay, which risks masking disease-relevant high-frequency signatures. In this study, we systematically investigate the spectral constraints of unsupervised time-domain feature extraction across three autoencoder architectures (LSTMVAE, VAEEG, Transformer) and a state-of-the-art EEG foundation model. Using synthetic experiments and empirical validation, we show that while autoencoders capture macro-scale shifts such as alpha slowing, they remain biased against higher frequencies due to a magnitude-driven masking effect induced by the Mean Squared Error loss under 1/f-decaying spectra. Increasing latent dimensionality mitigates this attenuation but sacrifices latent compactness and generative stability. We argue that, as the field advances toward large-scale foundation-level feature extractors, it is imperative to move beyond simple time-domain reconstruction and to integrate spectral-domain loss terms and gradient-balancing techniques, so that the subtle high-frequency transients critical for diagnosing complex brain disorders are preserved in the latent representation.

---


### 387. [Error Correction in Trained TTT Layers](https://arxiv.org/abs/2610.16268)

**<font color=#1a73e8>作者：</font>** Yuhe Hu, Wen Jia Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time-training (TTT) layers update fast-weight memory while processing an input sequence. A gradient-based update, however, does not by itself establish how the memory revises an existing association. We study the structure and empirical role of prediction-derived updates in released TTT implementations. For dot-product objectives, we characterize the absence of a prediction-error residual and establish conditions under which inner-loop ascent and descent are equivalent after reparameterization. For the LayerNorm-based squared-error objective used by TTT-Linear and TTT-MLP, we derive the inner gradient and identify a prediction-derived component that cancels at the released initialization in the zero-epsilon limit. We then measure the full normalized prediction's contribution on three trained checkpoints. Removing this contribution while retaining the LayerNorm Jacobian gives a mean gradient norm ratio of 0.25 to 0.32 across the models. On 100,303 tokens from War and Peace, the same intervention with local per-token norm matching raises perplexity by 2.8-2.9% on TTT-Linear-760M and 1.3B, whereas freezing all fast-weight updates raises it by factors of 4.2-4.5. Separate synthetic tests illustrate the dependence of plain delta-rule overwriting on step size. The results distinguish a prediction-derived update from its behavioral value and show why implementation analysis and live interventions are both needed to assess test-time memory.

---


### 388. [Graph3R: Unifying View Graph Initialization with Feed-Forward Reconstruction](https://arxiv.org/abs/2610.16272)

**<font color=#1a73e8>作者：</font>** Jingwen Yu, Hengli Wang, Jianhao Jiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward reconstruction recovers camera poses and dense geometry from image sets whose views are assumed to come from a single scene. In practice, uncurated image collections often contain views from disjoint scenes, and reconstructing these views jointly can corrupt camera poses and geometry. Existing pipelines typically resolve view associations in separate stages before final reconstruction, leaving view graph initialization and reconstruction inference only loosely coupled. We introduce Graph3R, which unifies view graph initialization with feed-forward reconstruction through a shared geometric representation. A lightweight verification head predicts pairwise covisibility from the multi-view features of $\pi^3$ to construct a view graph. This graph classifies the input views into scene groups. For each group, we mask the shared features before decoding camera poses and dense geometry. Reusing the multi-view features allows Graph3R to reconstruct disjoint scenes separately with a single backbone pass. Across three benchmarks, Graph3R improves average maximum recall at 100% precision by upto 8.99 percentage points over the baseline, while improving reconstruction quality on mixed-scene inputs. Regarding the multi-session mapping task, Graph3R improves cross-session localization and achieves competitive pose estimation accuracy, while delivering a runtime speedup of approximately $35.9\times$ over the baseline when reconstructing the query group. By integrating learned view association with geometric inference, our approach takes a step toward end-to-end reconstruction from uncurated image collections.

---


### 389. [Deep Speech Representations Track Word Timing along a Low-Dimensional Circular Trajectory](https://arxiv.org/abs/2610.16273)

**<font color=#1a73e8>作者：</font>** Burin Naowarat, Hao Tang, Sharon Goldwater  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech timing is fundamental for speech models to recognize words accurately, but how word-timing information is represented in speech models remains underexplored. We study this question using the framework of representational geometry, which investigates whether and how concepts are represented in low-dimensional subspaces of the representation space. Prior work in cognitive neuroscience has shown that when HuBERT feature sequences are averaged across words of the same duration, they form near-circular trajectories from word onset to word offset in a two-dimensional "temporal subspace." Here we show that this circular structure of word timing is a general property of deep speech representations, by demonstrating its emergence in nine additional speech models covering both supervised and self-supervised. We then move beyond averaged word segments and show that in HuBERT, the circular trajectories are consistent enough at the level of individual words to perform word segmentation. Our approach, Rotary Segmentation (RoSeg), achieves 64.3% boundary F-score on Librispeech by detecting word boundaries when cycles complete in the temporal subspace. Although supervision is needed to identify a good subspace, nevertheless this result demonstrates much stronger implicit word knowledge in HuBERT than has previously been shown.

---


### 390. [A Survey of Flow Matching in Reinforcement Learning](https://arxiv.org/abs/2610.16275)

**<font color=#1a73e8>作者：</font>** Nabuat Zaman Nahim, Fairoz Nower Khan, Peizhong Ju  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow Matching (FM) has recently emerged as a principled and efficient generative modeling framework for reinforcement learning (RL), enabling expressive, multimodal policy parameterizations via deterministic probability transport. Compared to diffusion-based policies that rely on stochastic denoising chains, FM uses sampling based on ordinary differential equations (ODEs), with learned velocity fields, which can substantially reduce inference latency and simplify the incorporation of RL objectives. As research in flow-based RL rapidly accelerates across offline continuous control, online fine-tuning, and foundation model alignment, the literature has become highly fragmented. In this survey, we provide a comprehensive taxonomy of flow-matching approaches in reinforcement learning. We organize the literature along two axes: the target distribution being modeled (e.g., action policies, value critics, transition dynamics) and the mechanism of RL signal integration (e.g., energy-weighted regression, flow-based policy gradients, and group relative policy optimization). Furthermore, we survey emerging frontiers such as discrete and non-Euclidean action spaces, provide a systematic comparative analysis against Gaussian and diffusion baselines, and outline critical open problems. Ultimately, this survey serves as a foundational roadmap for the next generation of generative reinforcement learning and alignment.

---


### 391. [FlowAvatar: Real-Time Full-Body Avatars from Sparse Egocentric Inputs on Consumer XR Devices](https://arxiv.org/abs/2610.16277)

**<font color=#1a73e8>作者：</font>** Chenfeng Gao, Taeyoung Yeon, Sungheon Park 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prior avatar embodiment research has studied tracking completeness (how faithfully the body, hands, and face are sensed and reproduced) and personalized appearance in isolation, each requiring specialized lab equipment. How these factors interact on consumer hardware remains an open question, because no existing system unifies body pose, face, hands, and personalized appearance on a standalone headset. We present FlowAvatar, a system enabling real-time personalized look-alike avatars with full-body pose, hand articulation, facial expression, and eye gaze tracking from sparse egocentric inputs on consumer XR devices (Meta Quest Pro). Our pose model achieves competitive spatial accuracy and state-of-the-art temporal consistency on the AMASS benchmark against prior works with comprehensive spatial and temporal losses validated through architecture and loss ablations, while running in real-time. Two user studies (N=12, N=10) provide converging evidence that tracking completeness and personalized appearance serve complementary roles: tracking completeness broadly improves perceived motion quality, while only their combination achieves positive total embodiment.

---


### 392. [DepthTile: Depth-Guided Existing-Image Self-Tiling with Input-Side Tileability Assessment](https://arxiv.org/abs/2610.16278)

**<font color=#1a73e8>作者：</font>** Rui Wang, Xi Chen, Hui Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing-image self-tiling aims to transform a given image into a seamlessly repeatable tile while preserving its original semantics and local details. This task requires weak editing to retain the source but leave periodic seams, whereas strong editing improves tileability at the large risk of content this http URL diffusion-based tiling pipelines alleviate boundary discontinuities, yet lack awareness of which regions are geometrically important to preserve. In this work, we propose DepthTile, a depth-guided self-tiling method whose generation module requires no retraining of the diffusion backbone. It converts monocular depth into a spatial preservation prior and integrates it into the timestep-dependent masking mechanism of Tiled Diffusion. DepthTile converts depth into a spatial editability map and fuses it with the differential diffusion mask. This strengthens source preservation in near-field regions indicated by the monocular depth prior while retaining editing flexibility near compatible background boundaries. To access when self-tiling is feasible, we introduce the Self-Tiling Ability Score (STAS), a lightweight input-side predictor based on RGB, gradient, depth, and depth-gradient cues. On a 335-image benchmark, relative to the default Tiled Diffusion pipeline, DepthTile reduces MAE, LPIPS, and Tiling Score by 12.8%, 26.7%, and 8.4%, respectively. STAS reliably enables difficulty-aware analysis and further supports compatibility-aware pairwise image tiling.

---


### 393. [agent-risk: Risk Assessment for Changes to AI Agents](https://arxiv.org/abs/2610.16280)

**<font color=#1a73e8>作者：</font>** Yue Zhao, Zixiang Xu, Angela Huyue Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before changing a deployed AI agent (a stricter safety gate, a new model), organizations must approve the change, starting from existing logs. Extending classical risk analysis to partial records and partial changes to running systems, agent-risk replays logged episodes, assuming nothing else changes and the agent does not anticipate the change. The log settles episodes acting as before, a declared stop value settles stopped ones, and the rest need logged support, a saved-state rerun, or a bound. We prove what logs must record for exact replay and which saved states serve a gate family. For independent episodes, we bound the reruns a decision needs and tolerable drift from live behavior. In a bash sandbox, a 7,200-episode log alone decided neither of two retry gates, which let the agent act after refusals the log never shows. Rerunning only each gate's blocked episodes from saved states reached both live decisions at half the agent calls of a live test sized post hoc for them, given the log. Without per-step harm, a stopping gate's certified harm ceiling rose up to 2.5-fold, since the log hides whether harm preceded the stop. Approval thus needs evidence designed in advance: log fields, saved states, targeted reruns.

---


### 394. [3D Gaussian Splatting for Fine-grained Urban Scene Reconstruction via Semantic-guided Density Control and Loss Design](https://arxiv.org/abs/2610.16292)

**<font color=#1a73e8>作者：</font>** Yueling Liao, San Jiang, Xing Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has been becoming a promising 3D reconstruction technique because of its advantage of high-fidelity rendering effect with high efficiency. However, it still suffers from coarse density control and semantically blind loss functions when reconstructing the fine-grained structures in complex urban scenes. Thus, this study proposes SG-GS, a semantic-guided 3DGS method for fine-grained structure reconstruction. It takes the semantic segmentation deduced by the Segment Anything Model (SAM) as a constraint and systematically integrates it into both Gaussian density control and loss function design. On the one hand, a semantic-constrained adaptive density control mechanism is constructed, which dynamically allocates gradient thresholds to different semantic regions of the scene and introduces an additional boundary-enhanced densification strategy, so that new Gaussians are directed to structurally critical regions. On the other hand, a multi-feature guided loss function is designed, and fine-grained supervision signals are gradually introduced through a phased progressive training strategy, alleviating the artifacts caused by the lack of semantic constraints in the basic loss. Experiments on three datasets show that the proposed method consistently improves reconstruction accuracy. Compared with the original 3DGS, the PSNR increases by approximately 2.7% to 5.2%, while artifacts on linear structures and boundary blurring are effectively mitigated. The method can serve the fine-grained 3D reconstruction of urban scenes.

---


### 395. [ClothAtlas: Joint Garment Identification and State Estimation under Self-Occlusion](https://arxiv.org/abs/2610.16293)

**<font color=#1a73e8>作者：</font>** Jens Lundell, Alberta Longhini, Lei Shu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Garment manipulation requires inferring both garment identity and complete configuration from partial, self-occluded observations. This creates a chicken-and-egg problem: completing a partial observation requires a garment-specific deformation prior, while identifying the garment requires a configuration that explains the observation. We introduce ClothAtlas, which jointly identifies garments and estimates their complete configurations from partial point clouds and a library of canonical meshes. A shared graph-conditioned flow-matching model samples configurations for each candidate mesh and ranks candidates by observation fit. The model accommodates different mesh shapes, vertex counts, and connectivities, allowing new garments to be added from canonical meshes alone without retraining. On held-out DexGarmentLab garments, ClothAtlas ranks the correct mesh first among 221 candidates for all 22 test garments from a single flat observation. From a single self-occluded observation, it identifies 15/22 garments, compared with 8/22 for a deterministic graph estimator. Persistent vertex identities support grasp-target localization on real garments, reducing mean error from 15.4 to 6.4 cm overall and from 17.0 to 8.3 cm on occluded targets compared with dense descriptor matching. Project page: this https URL

---


### 396. [Memory-Efficient Integer-Only Training of Deep Neural Networks](https://arxiv.org/abs/2610.16298)

**<font color=#1a73e8>作者：</font>** Hazem Hesham Yousef Shalby, Fabrizio Pittorino, Manuel Roveri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training neural networks in reduced precision can yield significant efficiency gains, yet all existing methods that scale to standard computer vision benchmarks retain floating-point in at least one stage, typically the weight update or optimizer state. We present a training algorithm that scales to modern deep neural networks, in which every tensor (weights, gradients, and activations) is stored as INT8, and every operation (forward pass, backward pass, weight update, optimizer update) is performed in integer arithmetic. Specifically, tensors are stored as signed integer mantissas paired with explicit power-of-two exponents, on which integer-only operations are performed using five custom composable building blocks (products, sums, divide-by-constant, nonlinear functions, and weight updates). This allows complete implementation of trainable integer layers, including convolutions, batch and layer normalization, softmax, and GELU. A per-group velocity mechanism with independent exponent tracking preserves gradient precision across neurons and channels with diverse magnitudes. As every tensor fits in INT8, training memory is roughly 4x smaller than the FP32 baseline. We validate our training algorithm on CNNs (ResNet-18/34/50/101, MobileNetV2) and Vision Transformers (ViT-Ti / B), demonstrating for the first time that training neural networks with INT8 tensors and integer arithmetic can achieve competitive accuracy on CIFAR-10, CIFAR-100 and ImageNet at a reduced memory budget.

---


### 397. [RAR: Rate-Adaptive Rollout for Time-Consistent Interactive World Models](https://arxiv.org/abs/2610.16302)

**<font color=#1a73e8>作者：</font>** Yaoyang Liu, Dongyu Yan, Yihua Du 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-based interactive world models aim to enable real-time, user-controllable environments. Yet most existing systems are trained and rolled out at a fixed temporal rate, limiting both runtime-rate adaptation and physical-horizon coverage -- a limitation we term temporal-rate coupling. Specifically, when runtime generation throughput differs from the learned temporal rate, the generated world evolves unintentionally more slowly or quickly. Moreover, using a single temporal rate imposes an inherent trade-off between temporal granularity and physical horizon: higher rates capture finer motion but cover a shorter duration under a fixed context window. To address both limitations, we introduce Rate-Adaptive Rollout (RAR), a framework that enables interactive world models to roll out at controllable temporal rates. At its core, Stride-RoPE aligns latent frames sampled at different rates on a shared physical-time coordinate, enabling consistent multi-rate rollout, unseen-rate generalization, and online rate switching without discarding history. Meanwhile, RAR uses multi-stride video sampling to enable joint learning of fine-grained dynamics and long-horizon evolution. Across action- and camera-controlled environments, RAR achieves temporally consistent multi-rate rollout and online rate switching while preserving high-rate generation quality and extending physical horizons under matched training budgets. RAR also transfers to pretrained world models while preserving perceptual quality.

---


### 398. [HyWe: Unifying Search and Operation for Real-World Hybrid Web Tasks](https://arxiv.org/abs/2610.16319)

**<font color=#1a73e8>作者：</font>** Zijian Cai, Haowei Liu, Kailai Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world hybrid web tasks need both information gathering and page interaction, yet search-based and operation-based agents are developed and evaluated separately. To bridge this gap, we introduce HyWe, a framework that unifies both capabilities within one model and trajectory. Its two modes use dedicated prompts and tool sets to sustain sub-goal execution; explicit switching selects the needed capability, and shared history lets each mode build on the other's findings. To provide demonstrations of these behaviors, we develop HyWeCollector, a fully automatic pipeline that uses task prototypes, four switching patterns, and multi-agent synthesis to produce verified hybrid trajectories. We train HyWe-35B on these demonstrations to unify efficient information gathering and browser interaction in a single 35B web agent. To evaluate hybrid task completion, we introduce HyWeBench: 100 human-written tasks on websites distinct from training, with human-written sub-goal checklists and an outcome-based evaluation pipeline. Hybrid training enables HyWe-35B to achieve 47.0% success on this benchmark, improving on the untrained base model by 19.0 percentage points and outperforming existing search-based and operation-based agents. Even before training, the same base model solves 28.0% of tasks with HyWe, versus 11.0% with all tools under one prompt. Beyond hybrid tasks, HyWe-35B achieves 59.0% and 88.3% success on Online-Mind2Web and WebVoyager, outperforming existing open-source baselines and cutting action cost per successful task by 48.3% and 51.9% compared with Fara-7B.

---


### 399. [Probabilistic Simulation of Gas-Liquid Interfaces with Coupled Flow Matching on Spherical Harmonics](https://arxiv.org/abs/2610.16327)

**<font color=#1a73e8>作者：</font>** Kiet Bennema ten Brinke, Rachna Ramesh, Douwe Orij 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bubbly flows involve strongly coupled bubble motion, deformation, and hydrodynamic interactions, making high-fidelity simulation computationally expensive. We propose a neural surrogate that jointly predicts bubble trajectories and interface deformation in a compact, shared representation, replacing costly mesh-resolved simulation with fast generative inference. Because two-phase flow dynamics is nonlinear and chaotic, we treat forecasting as a conditional generative problem rather than deterministic regression, predicting entire future windows in a single pass. We train and evaluate the surrogate on BubbleSH, a Front-Tracking dataset of rising deformable bubble swarms, assessing performance using trajectory, shape, and distributional metrics over kinematic, morphological, and interaction-based properties. The surrogate reproduces key flow statistics while running several orders of magnitude faster than the underlying DNS solver.

---


### 400. [Explicitly Aligned Multi-View Breast Cancer Risk Prediction from Variable-Length Screening Histories](https://arxiv.org/abs/2610.16329)

**<font color=#1a73e8>作者：</font>** Solveig Thrun, Zijun Sun, Suaiba A. Salahuddin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate breast cancer risk prediction from screening mammography is essential for improved risk stratification and personalized screening. It can benefit from both temporal breast tissue changes across longitudinal examinations and complementary anatomical information from craniocaudal (CC) and mediolateral oblique (MLO) views. Leveraging longitudinal information requires identifying corresponding tissue regions across examinations, yet most approaches rely on implicit feature alignment without explicitly enforcing spatial consistency. Recent work has demonstrated the benefits of explicit temporal alignment; however, existing methods model each view independently, preventing them from exploiting complementary CC and MLO information. Furthermore, explicit approaches have been limited to a single prior examination. To fill these gaps, we propose (this http URL), a breast-wise longitudinal multi-view framework that jointly models CC and MLO views across screening examinations while accommodating a variable number of prior examinations. FlexLMV-Net explicitly aligns longitudinal feature maps and integrates complementary views through cross-view temporal fusion and a dual-stream attention block. Evaluated on EMBED and CSAW-CC, FlexLMV-Net consistently outperforms existing approaches across breast density, cancer subtypes, and demographic subgroups, highlighting the benefits of explicit longitudinal alignment, multi-view modeling, and flexible use of available screening history. We further introduce (this http URL), an open-source benchmark that unifies state-of-the-art single- and multi-timepoint breast cancer risk prediction models under standardized preprocessing, training, inference, and evaluation protocols, enabling fair and reproducible comparison of existing methods.

---


> [!TIP]
> 当前位于：**351-400**（第 8/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
