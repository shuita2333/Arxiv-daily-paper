# 📦 其他研究 | 2026年08月12日

> 本类共 **445** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-445](./part-09.md)

---

### 301. [OGG-FR: Orthogonal Gradient Gaming and Frequency Rectification for Unmanned Aerial Vehicle Infrared Image Super-Resolution](https://arxiv.org/abs/2608.09150)

**<font color=#1a73e8>作者：</font>** Yongsong Huang, Qingzhong Wang, Xiaofeng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) infrared image super-resolution aims to recover weak thermal structures for deployment on resource-constrained platforms; lightweight models are therefore preferred, but multi-loss training can be unstable. A common strategy combines pixel-domain and frequency-domain objectives; however, low contrast, limited high-frequency content, and sensor-specific noise often make their gradients weakly aligned or conflicting. To address this optimization ambiguity, we propose Orthogonal Gradient Gaming and Frequency Rectification (OGG-FR), a plug-and-play optimization framework that decomposes the frequency gradient into a redundant parallel component and an orthogonal innovation component relative to the pixel gradient. In the conflict regime, OGG-FR computes a safe base gradient using the Multiple Gradient Descent Algorithm (MGDA) and adds a variance-rectified orthogonal innovation; in the compatible regime, it discards redundant parallel information and injects the orthogonal innovation according to a confidence score estimated from the high-frequency residual. Experimental results on the UAV thermal benchmark show broad gains under BI and BD degradations at $\times 4$ and $\times 8$ scales, while gradient analyses support the effectiveness of the proposed conflict-aware update rule.

---


### 302. [LightAIR: Lightweight Action Inversion and Riemannian Rectification for Text-based Person Anomaly Search](https://arxiv.org/abs/2608.09152)

**<font color=#1a73e8>作者：</font>** Yulun Zhang, Zixu Li, Zhiwei Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional Text-based Person Search (TPS) is typically limited to matching static appearance attributes, severely neglecting dynamic action information. The Text-based Person Anomaly Search (TPAS) task bridges this gap, requiring models to locate micro-level specific abnormal behaviors while matching macro-level appearance of pedestrians. However, current TPAS methods face fundamental limitations: external explicit pose estimators are fragile in unconstrained surveillance scenarios, and implicit learning encounters visual decoupling failure under pixel-level entanglement, causing dominant appearance information to easily swallow and contaminate subtle action features. Furthermore, performing contrastive optimization on hard negative samples (``same appearance, different actions'') in conventional Euclidean spaces induces severe shortcut learning. To address these, we propose the Lightweight Action Inversion and Riemannian rectification network (LightAIR). First, it introduces textual semantic priors as anchors via a lightweight action inversion operator to extract pure action features, thereby overcoming visual-inherent coupling. Subsequently, it employs orthogonal null-space projection to constrain appearance features within the orthogonal complement space of action features, guaranteeing strict forward decoupling. Finally, we designed a gradient rectification module that computes the Riemannian gradient to constrain the backpropagation trajectory, forcing the gradient flow to update strictly along the tangent space that preserves decoupling properties, thereby cutting off harmful shortcuts. Extensive experiments on the widely used TPAS and TIPR datasets demonstrate that LightAIR significantly outperforms existing state-of-the-art methods. Codes are available at this https URL

---


### 303. [TRACE: TRajectory Attribution for Automated Context Engineering](https://arxiv.org/abs/2608.09153)

**<font color=#1a73e8>作者：</font>** Yikai Zhao, Pradeep Kumar Misra, Saurabh Pandey  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production AI agents fail when their context sources -- system prompts, knowledge bases, tool descriptions, and procedural skills -- contain errors or gaps. Current maintenance relies on manual log review and ad-hoc debugging, creating a scalability bottleneck as interaction volume grows.
We present TRACE (TRajectory Attribution for Automated Context Engineering), an automated feedback loop that mines historical agent trajectories to diagnose and remediate context failures. Our key insight is that trajectories are rich with implicit dissatisfaction signals -- user corrections, rephrasing, abandonment cues -- that reveal precisely where context sources failed, without explicit feedback collection. Unlike model fine-tuning, TRACE operates on the context layer, enabling rapid iteration without retraining.
We make four contributions: (1) a trajectory mining framework that systematically extracts diagnostic information from historical agent executions; (2) multi-component causal attribution that extends textual gradients from monolithic prompt optimization to heterogeneous context sources (skills, knowledge bases, tools, prompts); (3) exploratory verification, where agents actively read context sources to distinguish content gaps requiring CREATE from stale content requiring UPDATE, achieving 96% operation accuracy; and (4) a reusable simulation methodology and verifiable benchmark addressing the absence of open datasets for context debugging, with a six-category fault taxonomy, ground truth annotations, and a cross-layer verification protocol.
On 60 dissatisfaction traces spanning three complexity tiers (up to 16 execution nodes), TRACE achieves 72.7% root cause attribution and 82% end-to-end fix effectiveness, showing that over 80% of context-layer failures can be automatically diagnosed and remediated by mining historical trajectories, an overlooked resource in production systems.

---


### 304. [Diagnosing Performance in Invasion-Based Esports: The Esports Performance Screening (EPS) Framework](https://arxiv.org/abs/2608.09156)

**<font color=#1a73e8>作者：</font>** Michael Trotter, Frauke Kubischta, Matthew Watson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Coaching in esports continues to become more common, yet conceptual tools for coaches to analyse performance breakdowns in esports remain limited. Existing approaches lack a way to distinguish between mental errors (i.e., mistakes relate to strategy and tactics), and physical slips (i.e., motor execution). This paper introduces the Esports Performance Screening (EPS) framework, that integrates several frameworks and models from sport and computing science which can be used to analyse mental and motor performance in esports. The EPS framework organises performance into five interconnected levels: strategy, tactics, tasks, actions and operations. Across these levels, teams pursue forms of superiority that influence transitions between stability and instability during invasion-based esports competition. The framework supports two complementary modes of screening use: diagnostic during reflective review and real-time screening during live play. Through illustrative esports scenarios, we demonstrate how instability can originate at different hierarchical layers and how misattribution of failure can obscure underlying causes. The purpose of the EPS framework is to help coaches systematically diagnose performance breakdowns, and act as heuristics to aid gameplay analysis during a match. The paper contributes a theoretically grounded, title-agnostic esports framework to support systematic performance analysis and pedagogical development in invasion-based esports.

---


### 305. [Tabular Numeric Stretch Transformation](https://arxiv.org/abs/2608.09162)

**<font color=#1a73e8>作者：</font>** Zihao Ye, Juyong Kim, Johnna Sundberg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data presents unique challenges for deep learning due to its heterogeneous nature, where numeric features exhibit diverse distributions, scales, and statistical properties. Although recent advances have improved how models learn from tabular data, how numeric data are transformed into model-friendly representations remains comparatively underexplored. We introduce the stretch transformation framework, which formulates numeric feature preprocessing as an optimization problem to make the target function smoother and thus more learnable. Our framework has two variants: (1) unsupervised stretch, which uniformly redistributes feature density via minimax optimization, and (2) supervised stretch, which optimizes target-aware numeric feature transformations from the perspective of target-function smoothness by minimizing the target function's Dirichlet energy in the transformed space. Our theoretical analysis further connects this framework to several popular transformations: unsupervised stretch is closely related to Piecewise Linear Encoding through a shared piecewise-linear geometry and approaches the empirical CDF transformation as the number of bins grows, while supervised stretch becomes closely related to target encoding in the fine-binning limit. Comprehensive experiments on 38 datasets from the TALENT benchmark demonstrate that supervised stretch consistently outperforms all baselines. These results show that explicitly optimizing for target function smoothness is a powerful and underexplored strategy for tabular deep learning.

---


### 306. [Intuitive Hand Positional Guidance Using McKibben-Based Surface Tactile Sensations to Shoulder and Elbow](https://arxiv.org/abs/2608.09167)

**<font color=#1a73e8>作者：</font>** Kenta Yokoe, Yuki Funabora, Tadayoshi Aoyama  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Hand positional guidance with intuitive perception is crucial for enhancing user interaction and task performance in immersive environments. However, conventional hand positional guidance methods, relying on tactile sensations, lack intuitiveness. Consequently, users require instruction on the relationship between the tactile sensation and target position of the guidance before using these methods. Additionally, the user needs training to become familiar with tactile sensations. This study presents a hand positional guidance system with intuitive perception that leverages McKibben-based surface tactile sensations directed to the shoulder and elbow. We developed a wearable fabric actuator that provides McKibben-based surface tactile sensations to induce six specific movements: elbow flexion, extension, shoulder abduction, adduction, horizontal abduction, and horizontal adduction. The effectiveness of the actuator was experimentally validated, demonstrating its high accuracy in intuitively inducing six movements. An algorithm based on the equilibrium point hypothesis and Weber-Fechner law was implemented to regulate the intensity of the tactile sensations for hand positional guidance. Furthermore, the accuracy and speed of the proposed system were compared with that of conventional guidance methods utilizing synthesized speech and vibrotactile guidance.

---


### 307. [A Time-Frequency Dual-Domain Multi-Scale Convolutional Neural Network for Bearing Fault Diagnosis under Strong Noise](https://arxiv.org/abs/2608.09174)

**<font color=#1a73e8>作者：</font>** Yanxi Ding, Tingyue Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To address the degradation of bearing fault diagnosis accuracy under strong noise, this paper proposes a time-frequency dual-domain multi-scale convolutional neural network. The time-domain branch employs three parallel convolutional kernels to capture multi-scale impulse features, while the frequency-domain branch applies the Fast Fourier Transform to extract noise-robust spectral structure information. Features from both branches are fused for fault classification, yielding a compact model of 110,122 parameters. Experiments on the CWRU bearing dataset across seven signal-to-noise ratio levels demonstrate that the proposed method achieves 99.75% accuracy under clean conditions and maintains 92.50% at -4 dB SNR, representing a 7.25 percentage-point improvement over the single-domain baseline with monotonically increasing gains under stronger noise. Ablation experiments validate the independent performance contributions of the time-domain multi-scale branch and the frequency-domain branch. Comparative experiments against WDCNN, DRSN-CW, MCNN, and 1D-LeNet confirm the superiority of the proposed method under strong noise conditions.

---


### 308. [Intuitive Directional Sense Presentation to the Torso Using McKibben-Based Surface Haptic Sensation in Immersive Space](https://arxiv.org/abs/2608.09177)

**<font color=#1a73e8>作者：</font>** Kenta Yokoe, Tadayoshi Aoyama, Yuki Funabora 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In recent years, systems that utilize immersive space have been developed in various fields. Immersive spaces often contain considerable amounts of visual information; therefore, users often fail to obtain their desired information. Therefore, various methods have been developed to guide users toward haptic sensations. However, many of these methods have limitations in terms of the intuitive perception of haptic sensation and require practice for familiarization with haptic sensation. Fabric actuators are wearable haptic devices that combine fabric and McKibben artificial muscles to provide wearers with surface haptic sensation. These sensations can be provided to a wide area of the body with intuitive perception, instead of only to a part of the body. This paper presents a novel air pressure adjustment method for whole-body motion guidance using surface haptic sensations provided by a wearable fabric actuator. The proposed system can provide users with a directional sense without visual information in an immersive space. The effectiveness of the proposed system was evaluated through subject experiments and statistical data analysis. Finally, a directional sense presentation was conducted for users performing micromanipulations in a mixed-reality space to demonstrate the applicability of the proposed system for teleoperation.

---


### 309. [Rethinking Medical Landmark Localization with Prototype Learning-based Progressive Offset Correction](https://arxiv.org/abs/2608.09182)

**<font color=#1a73e8>作者：</font>** Jingxian Xu, Yuhao Huang, Rusi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate landmark localization in medical images is a fundamental step for quantitative clinical measurement and downstream analysis. Existing localization methods have advanced, among which multi-stage refinement is a superior solution. Although this strategy mitigates the anatomical ambiguity inherent in single-stage global predictions, its high computational cost limits practical applicability. In this work, we propose a parameter-economic model, PPOC-LL, which leverages Prototype learning-based Progressive Offset Correction for Landmark Localization. Our contribution is three-fold. First, to drive coarse-to-fine landmark optimization, we introduce a multi-scale dynamic perception strategy for patch-level feature pyramid modeling. Second, to effectively handle anatomically similar patterns, we design a similarity-driven prototype learning mechanism that captures informative local semantics for robust offset prediction. Last, to stabilize the model learning and improve the overall performance, we incorporate a novel error-aware reliability regularization via tolerance-based balancing. We collected a large validation cohort, including two public and one private datasets spanning X-ray and ultrasound modalities, covering cephalometric, symphysis-fetal head, and fetal heart landmarks. Extensive experiments demonstrate that PPOC-LL achieves satisfactory performance with a favorable trade-off between accuracy and model complexity.

---


### 310. [Structure-Preserving Uncertainty Propagation in First-Order Proof Search](https://arxiv.org/abs/2608.09190)

**<font color=#1a73e8>作者：</font>** Tanel Tammet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GK is a query-directed first-order prover that extends ordinary resolution-based proof search with explicit positive and negative claims, numerical confidence values, and prioritized default rules with exceptions. It works directly with non-ground clauses, including equality and function terms. Candidate proofs are found by bounded first-order proof search; exception conditions of defaults are checked by further bounded searches, recursively when exceptions themselves depend on defaults. This avoids requiring a finite global grounding, while allowing incomplete searches to be reported as such.
This paper adds structure-preserving quantitative reporting to that framework. Retained proof histories are used in two calculations. The first reconstructs the uncertain ground premises used by each proof and computes the probability that at least one retained proof is available, without counting shared premises independently. The second resolves positive and negative support at intermediate atoms before that support is propagated through later rules; the same calculation evaluates uncertain exception conditions for individual rule applications. Reports separate positive support, negative support, conflict, and ignorance and identify detected incomplete calculations or fallbacks. The implementation performs bounded reconstruction and dependency traversal after proof search and still requires no global grounding. Analytic examples and independent simulators reproduce the reference calculations on their stated fragments. Comparisons with probabilistic logic, probabilistic ASP, default logic, and goal-directed ASP identify cases of agreement, semantic difference, unsupported translation, and incomplete computation.

---


### 311. [NBA_Streaming: A Large-Scale Benchmark for Fine-Grained Basketball Commentary Generation in Continuous Streams](https://arxiv.org/abs/2608.09200)

**<font color=#1a73e8>作者：</font>** Lifang Wu, Yuyang Wu, Yangdong Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Live basketball commentary generation requires determining when an event is sufficiently observable and describing it before subsequent events unfold. However, existing methods are primarily designed for pre-segmented clips or complete videos, making them unsuitable for continuous streams. Existing datasets also provide limited supervision for player identities, fine-grained actions, event attributes, and coherent event chains, restricting the factual richness of generated commentary. To address these limitations, we introduce NBA_Streaming, a large-scale benchmark for online fine-grained basketball commentary generation. It contains 307 hours of basketball broadcasts and approximately 35K temporally aligned events, with annotations of event boundaries, player identities, fine-grained actions, event chains, and natural-language commentary. By moving from isolated clips to continuous streams, NBA_Streaming enables unified evaluation of event localization, response reliability, factual grounding, and commentary quality under causal constraints. We further propose a causal two-stage framework that combines completion-first localization with ball-centric semantic grounding, enabling the system to identify complete events from observed streams and organize scene, event, identity, and action cues for commentary generation. Extensive experiments reveal the difficulty of NBA_Streaming, where existing baselines struggle with online timing, factual grounding, and fine-grained description. Our framework consistently improves over strong alternatives, while the remaining gap highlights NBA_Streaming as a valuable benchmark for streaming sports video understanding and generation.

---


### 312. [FedA2L: Adaptive layer-wise learning rate adjustment in decentralized federated learning](https://arxiv.org/abs/2608.09208)

**<font color=#1a73e8>作者：</font>** Van Truong Vo, Khoa Nguyen, Taehong Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized intelligence systems with heterogeneous devices and limited coordination increasingly rely on decentralized federated learning (DFL). However, DFL suffers from convergence inefficiency under data heterogeneity due to the use of a uniform learning rate (LR) that ignores layer-specific optimization needs. Foundational layers are responsible for maintaining network consensus, while specialized layers adapt to local data characteristics, leading to conflicting gradients and degraded performance under non-IID conditions. To address this fundamental tension, this work introduces FedA2L, a method that dynamically adjusts layer-wise LRs based on model divergence signals. By leveraging local update intensity and network consensus constraints, FedA2L seamlessly integrates into existing DFL protocols without additional communication or coordination. Extensive evaluations across DFL algorithms, various model architectures, and datasets demonstrate that FedA2L achieves up to 4.94 times faster convergence than vanilla DFL and reduces communication rounds by up to 59% compared to scheduler-based baselines. Furthermore, FedA2L exhibits resilience to severe data heterogeneity, larger network sizes, and sparse topologies, reducing communication overhead and establishing it as a versatile optimization tool for resource-constrained or large-scale distributed learning in edge and IoT deployments. The code is released at this https URL.

---


### 313. [Online Learning of Scale Parameters in Score-Driven Filters](https://arxiv.org/abs/2608.09218)

**<font color=#1a73e8>作者：</font>** Fabrizio Lillo, Giulia Livieri, Gianluca Palmari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-driven filters multiply a scaled log-likelihood score by a gain that controls the update magnitude. We treat this gain as a decision variable and study its online learning. Conditional on the current state, observation, score, and scaling rule, each admissible gain induces a reachable next state and a one-step-ahead predictive density: scalar gains govern distance along a line, while diagonal gains govern coordinatewise transmission. Gain selection is therefore a conditional predictive decision problem with a Kullback-Leibler objective. For a scalar unscaled gain, the negative raw product of consecutive scores is the stochastic gradient of this loss; positive aGAS scaling only rescales the effective step. Monotone differentiable gain links induce mirror-descent geometries on bounded gain domains, while persistence yields a Bregman pull towards a reference gain. Under convexity, compactness, and regularity conditions, we establish dynamic-regret bounds for projected and discounted mirror updates relative to time-varying, current-information comparators. Simulations illustrate the roles of scaling, link geometry, persistence, and coordinatewise transmission rates. An out-of-sample panel of equity-index volatilities shows that the bounded mirror gain generally matches or outperforms a constant gain while avoiding the extreme spikes of a nominally unbounded exponential link, with the strongest improvements observed in multi-crisis markets.

---


### 314. [FedTVD: Balancing Data Quality and Quantity for Robust Federated Learning](https://arxiv.org/abs/2608.09221)

**<font color=#1a73e8>作者：</font>** Radwan Selo, Majid Kundroo, Taehong Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative model training across distributed client devices while preserving data privacy. However, FL faces significant challenges due to data heterogeneity, particularly in terms of label distribution skewness and variations in dataset sizes, which can lead to biased model updates and hinder convergence. To address this, we propose FedTVD, a novel FL algorithm that weights client contributions during aggregation by considering both data quality and quantity. Unlike traditional FL approaches such as FedAvg, which rely solely on dataset size for client weighting, FedTVD integrates Total Variation Distance (TVD) to measure the divergence between each client's local label distribution and a uniform global distribution. Clients with highly skewed distributions receive lower weights, preventing unbalanced datasets with imbalances from disproportionately influencing the global model. At the same time, dataset size is incorporated to ensure scalability and fairness. This dual-weighting mechanism effectively mitigates the impact of data imbalance, leading to more stable and generalized global models. Experimental results show that FedTVD consistently outperforms state-of-the-art methods across all datasets (FMNIST, CIFAR-10, and CIFAR-100) and all levels of data heterogeneity. Notably, it achieves up to 10.6% improvement over FedAvg on CIFAR-10 under highly skewed data, while maintaining top performance even under moderate and IID settings.

---


### 315. [PatchHead: Learning Spatial Patch Evidence for Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2608.09223)

**<font color=#1a73e8>作者：</font>** Shengbo Qi, Hongyi Fang, Benjia Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated image detectors generalize poorly when their training and test images originate from different generators or datasets. Despite the rich spatial representations produced by vision foundation models like DINO, existing detectors typically classify images using only the globally aggregated CLS token. We hypothesize that globally aggregating DINO features into a single CLS token obscures spatially distributed generation traces. To test this hypothesis, we introduce PatchHead, a lightweight spatial aggregation head that preserves the two-dimensional organization of DINO patch tokens and integrates evidence across neighboring regions. During training, we freeze the pretrained DINO backbone and optimize only the inserted LoRA adapters, PatchHead, and auxiliary projection head. Across nine cross-dataset benchmarks spanning manually curated and in-the-wild settings, PatchHead ranks first on seven datasets and second on the remaining two. It improves the strongest prior method from 91.6% to 94.6% in average balanced accuracy (+3.0 points) and raises the worst-case accuracy from 82.4% to 89.4% (+6.9 points), while introducing only 8.6% more trainable parameters and 0.08% additional FLOPs. Further qualitative analysis suggests that PatchHead (i) reduces class-conditional domain discrepancy, and (ii) redirects the representation from content-dominated saliency toward spatially distributed authenticity evidence. Together, these observations provide a representation-level account of why spatial patch aggregation transfers more reliably across generators and datasets than a single CLS-based global representation. Our code and models will be made available upon acceptance.

---


### 316. [RL-Native Distillation: Exploiting Scored Trajectories for Few-Step Image Generation](https://arxiv.org/abs/2608.09226)

**<font color=#1a73e8>作者：</font>** Yuhan Li, Fangao Zeng, Sicong Kang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient text-to-image generation requires both reinforcement-learning (RL)-based reward alignment and few-step distillation, yet these procedures are typically performed sequentially, increasing training cost and risking the loss of reward gains during compression. We instead take an RL-native perspective: diffusion RL already generates reward-scored finite-step trajectories, whose intermediate states provide a natural source of distillation supervision rather than a disposable byproduct of sampling. Based on this insight, we propose REST (Reward-Enhanced Scored-Trajectory Distillation), a single-stage RL-distillation co-training framework that attaches a decoupled student to an arbitrary RL teacher. The student learns segment-wise from the teacher's evolving rollout trajectories while leaving the original teacher optimization unchanged. To prevent uniform imitation from preserving undesirable low-reward behaviors, we further introduce Advantage-Modulated Distillation (AMD), which transforms rollout advantages into signed weights over a base distillation loss. AMD strengthens supervision from preferred trajectories and mildly repels the student from low-reward ones. The resulting framework is lightweight and plug-and-play, requires no extra image rollouts, no separate distillation dataset, and no adversarial training. Experiments on compositional generation, visual text rendering, and human-preference alignment show that REST enables few-step CFG-free inference that matches or surpasses its 40-step RL teacher, with an overall additional training cost below 25% over pure RL. REST improves DrawBench PickScore over RTDMD by 0.82 while requiring only one-fifth of the training iterations.

---


### 317. [Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation](https://arxiv.org/abs/2608.09228)

**<font color=#1a73e8>作者：</font>** Yuki Ichihara, Naoto Iwase, Mohammad Atif Quamar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-Policy Self-Distillation (OPSD) is commonly interpreted as the transfer of privileged information: a teacher observes the verified solution to the target problem and supervises the student's trajectory. However, this interpretation conflates two effects. The reference solution not only reveals the answer to the current instance but also changes the context under which the teacher provides token-level supervision. We investigate the role of target-specific privilege with $\mathrm{OP}^{2}\mathrm{SD}$ (On-Policy Self-Distillation from Other Problems), which replaces the paired reference with a problem and solution from a different example, while preserving the student rollout, teacher, and distillation objective. Across three models and three mathematics benchmarks, $\mathrm{OP}^{2}\mathrm{SD}$ improves over the base model, remains competitive with OPSD. The success of $\mathrm{OP}^{2}\mathrm{SD}$ implies that OPSD gains do not necessarily come from access to the reference solution, and that the teacher's context-induced behavior is an important factor.

---


### 318. [BAG: Budget-Aware Gating for Diffusion Caching](https://arxiv.org/abs/2608.09231)

**<font color=#1a73e8>作者：</font>** Tong Zhao, Mingkun Lei, Yucheng Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion caching is a lightweight strategy that accelerates Diffusion Transformers (DiTs) by reusing intermediate features across denoising steps, but existing paradigms face a fundamental trade-off: online heuristics lack global budget awareness, whereas static schedules lack instance adaptivity and fail to flexibly adapt to varying runtime budget constraints. To bridge this gap, we present BAG (Budget-Aware Gating), a novel caching policy that unifies global budget pacing with dynamic, instance-adaptive feature reuse. Rather than relying on hand-crafted rules, BAG employs a lightweight gating network that dynamically decides whether to execute a full computation or reuse cached features at each step by jointly conditioning on the budget state and local trajectory feedback. We train this policy via offline-to-online schedule distillation, transferring the decision-making of offline-searched schedules into a compact online gate. Extensive experiments on FLUX.1-dev and Wan2.1 demonstrate that BAG consistently outperforms state-of-the-art caching methods across various speedup tiers while remaining robust across different resolutions, seeds, and guidance scales. Code will be released.

---


### 319. [Label Granularity Skew in Federated Learning with Hierarchical Image Classification](https://arxiv.org/abs/2608.09236)

**<font color=#1a73e8>作者：</font>** Jaeheon Kim, Hokeun Kim, Bong Jun Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning enables privacy-preserving collaboration across distributed devices without centralizing local data. However, clients may differ not only in data distributions but also in domain knowledge and annotation capabilities. In this paper, we introduce label granularity skew, a new form of statistical heterogeneity in federated hierarchical classification, in which clients provide taxonomy-consistent labels at different levels of detail within a shared class hierarchy. To model this heterogeneity, we generate client-specific local label hierarchies using a probabilistic relational neighbor classifier and construct a WordNet-guided hierarchy via silhouette score-based coarsening. Our analysis shows that strongly coupled hierarchical models are sensitive to incomplete supervision, while the conditional softmax classifier is more robust. Based on this insight, we propose Branch-wise Decoupled Fine-Tuning (BDFT) and its federated version, FedBDFT, which fine-tune branch-wise classifiers and aggregate them through federated optimization. Experiments on CIFAR-100, TinyImageNet, and ImageNet show that FedBDFT substantially improves robustness under severe label granularity skew, with average gains of 27.9% and 56.4% at skewness levels of 0.6 and 0.9, respectively. Zero-shot results further indicate that FedBDFT better preserves hierarchical representations for unseen fine-grained classes. These findings demonstrate its effectiveness for federated hierarchical classification with heterogeneous label granularities.

---


### 320. [RealDenseFace: Real-time Monocular 3D Face Reconstruction from Dense UV-space Priors](https://arxiv.org/abs/2608.09238)

**<font color=#1a73e8>作者：</font>** Linzhou Li, Tianjia Shao, Kun Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent monocular 3D face reconstruction methods achieve high fidelity by fitting a 3D Morphable Model (3DMM) to dense priors predicted by networks, but the optimization stage is computationally expensive, often taking tens of seconds per image. We present RealDenseFace, a real-time optimization-based 3D face reconstruction method with dense UV-space network predictions. Our key idea is to formulate 3DMM fitting as a nonlinear least-squares problem and solve it with a tailored Gauss-Newton solver that converges in only a few iterations. The reconstruction is conducted in two stages. In the first stage, the network predicts two dense UV-space maps from a single RGB image: a correspondence map for UV-to-image alignment, and a relative-depth map for geometric constraints along the viewing direction. In the second stage, the solver fits per-vertex targets sampled from these maps at the vertex UV coordinates. The solver supports all three reconstruction settings: single-image fitting, offline sequence reconstruction, and online tracking. Our method achieves state-of-the-art accuracy on the NeRSemble SVFR benchmark. The online tracker runs at 80+ FPS, and the offline sequence reconstruction is over 20 times faster than previous optimization-based baselines.

---


### 321. [Multimodal Federated Learning under Dual-Axis Modality Missingness](https://arxiv.org/abs/2608.09240)

**<font color=#1a73e8>作者：</font>** Adiba Orzikulova, Jaehyun Kwak, Jaemin Shin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal federated learning (FL) supports collaborative modeling in privacy-sensitive health-sensing and medical settings, but realistic deployments often exhibit dual-axis modality missingness: clients have different modality sets, and individual samples may contain only subsets of the modalities available locally. Existing methods typically address these two axes separately. We propose Flux, a multimodal federated learning framework built around two complementary components. First, modality-aware confidence tempering learns sample-specific confidence for each modality through mask-aware unimodal supervision and fuses the confidence estimates from observed modalities into a sample-adaptive temperature that adjusts predictive sharpness according to evidence quality and completeness. Second, gradient-decoupled private adaptation applies this temperature only to a client-private prediction pathway, while training the shared federated model with a standard, untempered objective. This enables sample-specific, client-local confidence adaptation without allowing confidence-dependent gradients to perturb shared representation learning. Across four multimodal datasets, Flux achieves the highest average macro-F1 on every dataset, outperforming the strongest dataset-specific baseline by 0.8~2.2 points and by 1.6 points on average. Additional analyses demonstrate favorable calibration, temperature sensitivity to both modality missingness and input corruption, and more stable shared optimization under private-only tempering. Our code is available at this https URL.

---


### 322. [In-Loop Model Adaptation with Coupled Latent-Noise Guidance for High-Fidelity Subject-Driven Text-to-Image Generation](https://arxiv.org/abs/2608.09244)

**<font color=#1a73e8>作者：</font>** Yushun Tang, Weiming Chen, Siyi Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models have achieved remarkable success in generating high-quality images from a given text prompt. Subject-driven generation aims to synthesize customized images to mimic the appearance of subjects in given reference images within different visual contexts specified by the text prompts. The central challenge here is that, when the reference image changes, the diffusion model cannot efficiently adapt to different visual contexts while consistently maintaining the subject identity. Existing methods either train the model with a large domain-specific dataset or fine-tune the model using the reference image for hundreds of iterations before actual image generation. In this work, we explore a new approach, called \textit{In-Loop Model Adaptation} (IMA), which adapts the core diffusion model at each generation step during the actual process of image generation, without being trained on the reference image before the generation process. To this end, we establish a DDIM inversion chain that maps the reference image to a sequence of latent, as well as a text-to-image generation chain which generates the image from the text prompt only. We then introduce a masked latent consistency loss and a noise regularization loss to characterize the latent-noise difference between the diffusion model and these two chains at each generation step. This coupled latent-noise loss is used to guide the in-loop model adaptation to preserve the subject identity specified by the reference image while maintaining accurate alignment with the text prompt, resulting in high-fidelity text-to-image generation. Our extensive experiments demonstrate that our proposed IMA method significantly improves the performance of subject-driven text-to-image generation.

---


### 323. [An Explainable GNN Framework for Component-Level Anomaly Diagnosis](https://arxiv.org/abs/2608.09246)

**<font color=#1a73e8>作者：</font>** Sena Ozgunay, Louise Travé-Massuyès, Jean-Michel Loubes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial processes are complex systems composed of multiple interacting sensors that generate multivariate time series (MTS). Detecting anomalies in such systems is critical for reliability and safety, yet understanding their origin is equally important. Existing Graph Neural Network (GNN)based methods for anomaly detection primarily focus on sensor-level deviations and either attribute anomalies directly to the deviating sensors. When diagnosis is attempted, generally, the most deviated sensor is identified as a root cause of a system fault. However, in many industrial systems, anomalies do not arise from faulty sensors but from disruptions in the influences governing the system dynamics. We propose an explainable GNN-based anomaly detection framework that shifts the perspective from sensor-level anomalies to component-level diagnosis, hypothesizing that anomalous measurements are symptoms of altered inter-sensor influences. Experiments show that the method effectively identifies and prioritizes the true faulty components, providing interpretable insights into system failures.

---


### 324. [Track me if you can: Ephemeral coin tracing](https://arxiv.org/abs/2608.09249)

**<font color=#1a73e8>作者：</font>** Ignacio Amores-Sesar, Christian Cachin, Rohit Chatterjee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving payment systems are well understood, yet their adoption in regulated settings, such as central bank digital currencies (CBDCs), institutional stablecoins, and other compliant payment infrastructures, has been limited by concerns over their potential misuse for illicit activities. Regulators counter financial crime with a toolbox of complementary measures to identify, trace, and stop criminal actors. Tracing is one key tool: acting on outside evidence that a user is implicated in a crime such as money laundering, law enforcement follows the suspect's funds through the ledger to uncover laundering routes and accomplices. The tracing schemes proposed in the literature, however, grant authorities unbounded capabilities: once initiated, tracing propagates through the transaction graph or persists across all future transactions of a user, and may eventually deanonymize the entire ledger. Only the goodwill of the authority, or the honesty of a committee, keeps surveillance targeted and temporary.
We introduce ephemeral coin tracing (ECT), a primitive whose tracing capacity is bounded by construction, both in the number of simultaneously traced users and in the number of hops each trace survives. The authority issues tracing tags that degrade at each hop; after a protocol-defined number of hops, a tag collapses into a value indistinguishable from that of an untagged coin. Within a tracing period the bound is absolute: no authority, however motivated, can follow a tag past its budget. We formalize ECT, define its security and privacy guarantees, and give two constructions, one over exponential ElGamal and one over Damgård--Jurik encryption.

---


### 325. [FEAST: Federated Shared-Space Training for Resource-Heterogeneous Clients](https://arxiv.org/abs/2608.09250)

**<font color=#1a73e8>作者：</font>** Bostan Khan, Masoud Daneshtalab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) must serve devices with varying computational capabilities. A fixed model cannot suit all devices, while training one model per deployment limit is costly. Federated supernet training instead learns one elastic model with differently sized subnetworks, then deploys a suitable one to each device. When client inference budgets differ, however, parameters exclusive to high-cost subnetworks are reachable by fewer clients. We propose FEAST, a federated shared-space training framework that counters this imbalance by jointly training multiple subnetworks within each client's limit. Budget-tailored sub-supernet routing sends only the relevant supernet portion, and sparse aggregation merges the returned parameter slices. The trained supernet directly serves the subnetworks used during federation and supports post-hoc extraction of additional subnetworks without federated retraining. We further show that independently assigning clients' training-data volumes and inference budgets can distort accuracy--inference-cost comparisons in heterogeneous FL simulations, and introduce a one-parameter $\gamma$-allocation protocol to control this coupling. In our experimental setup, the SuperFedNAS and DeepFedNAS supernet training procedures remain near chance at 25M and reach at most $17.09\%$ at $596$M inference MACs; FEAST reaches $71.06\%$ at $596$M, $2.4$ points above the strongest model-heterogeneous weight-sharing baseline at its largest tier. Across CIFAR-100, CINIC-10, and TinyImageNet-200, FEAST achieves the highest population-averaged accuracy among the evaluated weight-sharing methods when each client receives its largest affordable subnetwork. Sub-supernet routing reduces aggregate model-parameter traffic by $6.8\times$ relative to full-supernet transmission.

---


### 326. [Full-Feature versus Limited-Input Machine Learning for Residential Energy Estimation: A Comparative Analysis of RECS and ResStock Under Realistic Input Constraints](https://arxiv.org/abs/2608.09255)

**<font color=#1a73e8>作者：</font>** Aditya Ramnarayan, Fatih Evren, Patti Gunderson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residential energy estimates are often needed before detailed envelope characteristics, equipment efficiencies, infiltration, sensor, or billing data are available. This study quantifies the trade-off between predictive accuracy and input accessibility using two nationally representative U.S. residential-energy datasets: the survey-based Residential Energy Consumption Survey (RECS) and the simulation-based ResStock dataset. Full-feature models were first used to establish dataset-specific performance benchmarks. For total-energy estimation, the models were subsequently restricted to ten low-burden variables obtainable from occupants, administrative records, or location-based weather data without an on-site energy audit. Among CatBoost, XGBoost, LightGBM, Random Forest, and Neural Networks, CatBoost consistently achieved the highest predictive performance for the full-feature analysis, reaching R2 = 0.90 for ResStock and R2 = 0.73 for RECS. When the feature set was restricted to ten homeowner-accessible inputs to simulate realistic deployment conditions, model performance converged to R2 = 0.61 for RECS and R2 = 0.62 for ResStock, showing that algorithmic complexity cannot fully compensate for missing physical and behavioral information. However, for a more homogeneous ResStock cohort consisting of single-family detached, natural-gas-heated homes in Climate Zone 6A constructed between 2000 and 2010, a reduced-input model improved accuracy to R2 = 0.85, demonstrating the value of targeted modeling for homogeneous populations. The results indicate that tree-based ensemble models can serve as high-fidelity emulators of national-scale residential energy datasets. However, careful consideration of feature availability, dataset origin (empirical vs. synthetic), and applicable use cases are also important.

---


### 327. [Distributed Team Orchestration via Supervisor Networks: Convergence, Optimality, and Resilience](https://arxiv.org/abs/2608.09256)

**<font color=#1a73e8>作者：</font>** Juntian Zhu, Guanpu Chen, Tongtian Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In this paper, we study zero-sum potential team games with a supervisor network, where agents rely on supervisor-provided belief information rather than accurate common beliefs. The main challenge is that such belief information can be inaccurate because of supervisors' belief-estimation errors and the misreporting of joint actions by Byzantine teams. We propose the distributed team-orchestrating algorithm (DTOA), which combines team fictitious play with supervisor-based distributed belief learning. We prove the convergence of supervisors' belief estimates and establish that the induced learning dynamics converge to a near team-Nash equilibrium (TNE) in terms of the team-Nash gap (TNG). In the Byzantine setting, we consider a misreporting attack model and develop a Byzantine-resilient DTOA. We further provide probabilistic guarantees for Byzantine-team identification and establish an asymptotic bound on the honest TNG. Numerical experiments illustrate the theoretical findings, compare DTOA with baseline learning methods, and evaluate its performance in a Markov decision process setting.

---


### 328. [Privileged Likelihood Is Not Automatically Value: Three Checks for Token Credit in On-Policy Self-Distillation](https://arxiv.org/abs/2608.09263)

**<font color=#1a73e8>作者：</font>** Xuan-Phi Nguyen, Shrey Pandit, Yiran Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Outcome verifiers score completed reasoning traces but do not assign credit to intermediate tokens. Privileged self-distillation attempts to fill this gap by rescoring a model's own rollout with training-only information. A token likelihood change, however, is not automatically outcome credit. We separate three questions: whether the score tracks better actions, whether feedback construction changes what is compared, and what behavior the training loss reinforces. We establish these distinctions formally. When a rollout is scored using hindsight feedback written about that same rollout, its content determines both the tokens and the scoring context, creating direct self-dependence. Using feedback from another rollout of the same problem removes this dependence but does not guarantee a useful score. In matched experiments with a 20B model on AIME 2025, the implemented additive score is near chance (AUC=0.505) and slightly favors incorrect traces after length adjustment. In the paired comparison, the outcome-only control records 64.2\%, versus 24.2\%--33.9\% for five token-score variants. The results motivate validating score meaning, feedback construction, and training behavior separately before calling a likelihood signal credit.

---


### 329. [Task-Adaptive 3D Cross-Field MRI Translation via Field-Conditioned Content-Style Pretraining](https://arxiv.org/abs/2608.09264)

**<font color=#1a73e8>作者：</font>** Haowen Pang, Yingqi Hao, Pengli Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic field strength is a major source of domain shift in magnetic resonance imaging (MRI), affecting signal-to-noise ratio, tissue contrast, spatial detail, and the visibility of anatomical boundaries. The MRIxFields 2026 challenge investigates this problem through cross-field MRI translation across acquisitions at 0.1T, 1.5T, 3T, 5T, and 7T. Its three tasks, Any-to-7T, 0.1T-to-High, and Any-to-Any synthesis, require the generation of target-field image characteristics while preserving subject-specific anatomy. This problem is particularly challenging because paired acquisitions of the same subject across multiple field strengths are rarely available for training. We propose a 3D unpaired cross-field MRI translation framework based on field-conditioned content-style pretraining. The proposed framework first learns controllable field-to-field translation across all available field strengths by disentangling anatomical content from field-dependent contrast characteristics. The pretrained backbone is then adapted to task-specific target domains. Our model comprises a 3D content encoder, a 3D style encoder, a field-conditioned style generator, an AdaIN-modulated decoder, and a multi-field discriminator. Adversarial learning encourages realistic target-field appearance, while cycle-consistency, identity, content, style, and diversity constraints promote anatomical fidelity and controllable translation. We evaluate the proposed method on MRIxFields data spanning five field strengths and three MRI modalities. Experiments on paired test data demonstrate that the framework can adapt to the three challenge settings while preserving three-dimensional anatomical structure in the synthesized volumes. The implementation code is publicly available at this https URL.

---


### 330. [Did the Grid Erase the Event? EndoClock for Auditing Medical World-Model Pipelines](https://arxiv.org/abs/2608.09266)

**<font color=#1a73e8>作者：</font>** Yarin Udi, Tom Sharon-Shahak, Roee Masad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical world models commonly learn from multimodal recordings synchronized onto a fixed-rate grid. This preprocessing resamples each native stream onto a shared time axis. Each stream has an observation clock that governs when observations are emitted or updated. When this clock depends on the latent or acquisition state, it is endogenous. In such settings, synchronization may not be neutral and can erase task-relevant evidence before the model sees the data. We introduce a four-regime taxonomy that characterizes where the evidence needed to distinguish a target event or state survives. The relevant witness may remain in the sampled values, in grid-cell update patterns, in native timing, or only in an external acquisition channel. EndoClock operationalizes this taxonomy as a conservative pretraining audit. It reports the lowest witness-bearing representation supported by the available evidence, or unresolved when no regime can be established. We illustrate this failure in echocardiography, where B-mode video write-outs cease during pulsed-wave Doppler acquisition while the corresponding measurement events remain recorded only in an external acquisition log. This work is a preliminary failure alert and executable audit. Its practical message is to preserve the native observation process long enough to determine whether synchronization has erased information required by the intended task.

---


### 331. [GRASP: Granularity-Aware Region Alignment and Semantic Prototype Learning for Fine-Grained Cross-Modal Understanding in Drone Views](https://arxiv.org/abs/2608.09270)

**<font color=#1a73e8>作者：</font>** Jiahui Cui, Yan Zhao, Kan Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained cross-modal understanding in drone views is essential for aerial vision-language navigation. However, the inherent wide field of view and overhead perspective of drone scenarios impose dual challenges on vision-language understanding. At the macro level, overwhelming background clutter in visual representations leads to Cross-Modal Focus Misalignment, where the model prioritizes global environmental similarities over specific object details. At the micro level, Visual Isomorphism creates ambiguity, where candidates share similar geometric structures yet differ only in subtle attributes. To address these challenges, we propose the Granularity-Aware Region Alignment and Semantic Prototype (GRASP) learning framework, enhancing discriminative capability through two synergistic strategies. Specifically, we introduce Region-Focused Alignment (RFA) to promote object-centric cross-modal alignment while suppressing background interference. Concurrently, to tackle visual isomorphism, we propose Semantic Perturbation Enhanced Matching (SPEM), which leverages a foreground-purified Semantic Prototype Codebook (SPC) to construct semantically perturbed negatives for fine-grained semantic discrimination. Extensive experiments on the GeoText-1652 benchmark and the unseen ERA dataset demonstrate that GRASP achieves competitive performance in drone-view fine-grained image-text retrieval, validating its effectiveness for cross-modal understanding in aerial scenarios. Our code implementation is available at this https URL.

---


### 332. [Verifiably grounded machine interpretation of lunar geology](https://arxiv.org/abs/2608.09276)

**<font color=#1a73e8>作者：</font>** Tom Sander, Kay Wohlfarth, Christian Wöhler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Planetary geology relies on historical, interpretive reasoning to reconstruct past events from diverse observations. Here, we present a step toward an automated "machine intelligence geologist" by embedding this distinct methodology of geologic knowledge discovery and inference into a multimodal vision-language architecture. Focusing on the stratigraphy of lunar basaltic mare volcanism, we train a model to generate verifiably grounded geologic interpretations directly from co-registered topographic, spectral, and geologic maps. We demonstrate that while the system successfully balances established geological priors with local visual evidence to accurately describe stratigraphy and terrain, numeric age dating derived solely from vision defaults to memorized priors. Integrating an open-book retrieval mechanism resolves this, enabling the model to faithfully cite published chronologies. Our findings delineate the necessary architecture for automated geologic inference: site evidence must be visually interpreted from local data, while quantitative historical context must be retrieved from the scientific record.

---


### 333. [Is the ACL Responsible NLP Checklist a Box-Ticking Exercise? A Large-Scale Analysis of EMNLP 2025](https://arxiv.org/abs/2608.09280)

**<font color=#1a73e8>作者：</font>** Nusrath Jinnath, Wei Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Responsible NLP practice includes a) transparency, b) ethics, and c) societal impacts. The Responsible NLP Checklist aims to push these goals, and promote responsible practice. Recently, ACL released the EMNLP 2025 Checklists to aid transparency on the current research practice, which we focus on. We curate and release the first two datasets of: a) all the checklist responses and justifications from the EMNLP 2025 Main and Finding tracks; b) checklist reference linking to paper sections. We also provide the first analysis of recent EMNLP Checklists, by examining $73,922$ responses and justifications to them. For the Main track, we find that authors isolate ethics questions of the Checklist from the paper's bulk, mimicking the trend of ethics being an afterthought. We then examine \texttt{NO} responses. We find $44.9\%$ of justifications are poor or bad-faith, being brief or empty. Then, we find significant issues with the checklist design and effort of authors, namely that $6\%$ of all checklists contained logical contradictions between parent and child responses. We also find evidence of surface compliance for responsible ethics, with $53\%$ authors dismissing potential risks or social impacts of their work, for which there should be none. We compare this to the Findings track, noticing a similar trend in both tracks. Lastly, we discuss the implications of the checklist design and provide recommendations for future checklist iterations. Including: a) enforcing a minimum word count, b) enforcing more scrutiny on the risks of appliances.

---


### 334. [VeinCast: Physics-Guided Dynamic Field Graphs with Graph-Conditioned Fusion for Global Medium-Range Weather Forecasting](https://arxiv.org/abs/2608.09286)

**<font color=#1a73e8>作者：</font>** Zhisheng Chen, Jinhan Li, Yuxuan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global medium-range weather forecasting requires modeling structured yet state-dependent interactions among heterogeneous atmospheric fields. Existing data-driven models largely learn these interactions implicitly, whereas equation-level physical constraints may inherit approximation and model-form biases. We present VeinCast, a physics-guided dynamic field graph and graph-conditioned fusion framework that jointly forecasts 69 surface and upper-air fields. Within each local window, its Physics-Guided Dynamic Field Graph combines predefined atmospheric relations with state-dependent Top-K residual edges and adapts Earth-window attention using the resulting graph context. Graph-Conditioned Latent Fusion further employs graph context and source-node centrality to guide field-to-latent aggregation, while bounded feedback preserves field-specific information. On the $1.5^\circ$ ERA5 benchmark, VeinCast demonstrates competitive forecasting performance across all 69 meteorological fields at lead times of up to 14 days, compared with representative global weather forecasting models including FuXi, Pangu-Weather, GraphCast, FengWu, and ARROW. Ablations confirm that the two modules provide complementary gains, demonstrating the effectiveness of relational-level physical guidance for data-driven weather forecasting.

---


### 335. [UniDFKD: A Unified Semantic Prior Framework for Architecture-Agnostic Data-Free Knowledge Distillation](https://arxiv.org/abs/2608.09287)

**<font color=#1a73e8>作者：</font>** Xuewan He, Tong Chu, Zihan Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data-Free Knowledge Distillation (DFKD) transfers knowledge from a pretrained teacher model to a compact student model by synthesizing semantically informative data, eliminating the need for access to the original training dataset. Existing DFKD methods rely heavily on architecture-specific statistical priors (e.g., Batch Normalization statistics) to guide data synthesis, however, such architecture-dependent priors are often absent in modern architectures such as Vision Transformers (ViTs), resulting in degraded semantic quality of the synthesized data and consequently catastrophic performance degradation. In this paper, we propose \emph{UniDFKD}, a unified data-free knowledge distillation framework that replaces architecture-specific statistics with explicit, architecture-agnostic semantic priors. \emph{UniDFKD} governs the entire synthesis-distillation pipeline along three dimensions: (1) Categorical Semantic Conditioning (CSC) defines \emph{what} to synthesize by persistently modulating the generator with language-derived embeddings to capture semantic diversity; (2) Spatial Semantic Anchoring (SSA) dictates \emph{where} evidence belongs by anchoring the teacher's spatial attributions to a Gaussian prior; and (3) Spatial Semantic Distillation (SSD) controls \emph{how} knowledge is transferred by explicitly aligning teacher-student spatial evidence alongside predictions. Extensive experiments across CNNs and ViTs demonstrate that UniDFKD establishes a new state-of-the-art, outperforming existing methods by an average absolute margin of over 20\% in both homogeneous and heterogeneous settings.

---


### 336. [CADEngBench: It Looks Like CAD, but Does It Work? Evaluating Parametric Design, Assembly Reasoning, and Physics Simulation](https://arxiv.org/abs/2608.09296)

**<font color=#1a73e8>作者：</font>** Harmanjot Singh, Abhra Dubey, Jorge Alejandro Amador Herrera  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A CAD model is not engineering-grade merely because it looks correct. It must satisfy design requirements, respond predictably to parameter changes, support controlled edits, match a reference structural response under a declared analysis, and connect to other parts through valid joints. We present CADEngBench, a two-track benchmark for these capabilities. CADEngBench-P evaluates 300 parametric parts, each used for one zero-to-CAD task and one functional-editing task (600 tasks in total), through boundary-representation (B-Rep) validity, engineering and DFM checks, parameter-family perturbations, functional editing, and matched linear-static FEA in CalculiX. CADEngBench-A evaluates 150 body pairs through ranked joint retrieval, exact face-and-edge grounding, joint-frame prediction, and kinematic verification. Across eight multimodal, code-capable models, editing supplied CAD is substantially easier than generating it, while complex edits and matched FEA remain difficult. Assembly predictions often locate the relevant region but fail to recover the recorded joint or mating entities. These results show that CAD evaluation must test engineering behavior rather than appearance alone.

---


### 337. [Linearized 2-Simplicial Attention](https://arxiv.org/abs/2608.09307)

**<font color=#1a73e8>作者：</font>** Aritra Das, Dhruman Gupta, Debayan Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a linearized form of 2-simplicial attention by rewriting the trilinear score as an inner product between a composite query and a key, so that the sum over one token axis takes the same form as ordinary softmax attention. We then approximate this sum with positive random features and store the entire past in a fixed-size state, while the second axis stays explicit over a short window of recent tokens. This enables us to achieve linear cost in sequence length combined with a global reach that windowed 2-simplicial attention lacks. We implement it with custom Triton kernels and combine it with Kimi Delta Attention to build a model with no softmax attention at all. Under matched compute, this model achieves the highest mean downstream accuracy among the compared architectures, and at 16k context it improves mean accuracy over a KDA hybrid while lowering LAMBADA perplexity from 715.6 to 602.6.

---


### 338. [Degraded Infrared Small Object Detection via Degradation-Adapted Physics-Guided Restoration](https://arxiv.org/abs/2608.09311)

**<font color=#1a73e8>作者：</font>** Xinkai Lu, Wenjun Chen, Yi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small object detection has made significant progress in recent years. However, degradations such as fog and nonuniformity can suppress target-background contrast, substantially increasing detection difficulty. Existing methods mainly rely on image restoration as preprocessing, but they are typically designed for specific degradation types and fail to generalize to varying degradations. To alleviate this, we propose DAISOD, a degradation-adapted infrared small object detection framework for robust detection under different degradations. DAISOD first identifies the type and severity of degradations, then adapts the processing via dedicated branches, and finally fuses the results for subsequent detection. Moreover, a physics-guided restoration mechanism is incorporated to explicitly estimate degradation parameters and remove degradation effects through physical models, avoiding excessive restoration that may erase small targets. Moreover, we construct a degraded infrared small object detection dataset covering diverse degradation types and levels. Extensive experiments show that DAISOD outperforms state-of-the-art methods under various degradation conditions.

---


### 339. [Targeted Label-Flipping and Oversampling Attacks on Federated Conditional GANs](https://arxiv.org/abs/2608.09314)

**<font color=#1a73e8>作者：</font>** Panav Shah, Avishek Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In a federated learning setup for GANs, several adversarial attacks are possible. One such attack is label flipping, in which malicious clients deliberately alter label information during local training in order to manipulate the global generator. The objective of this attack is to skew the learned generation distribution so that samples conditioned on a target label are instead mapped to a source class. In this work, we investigate the effectiveness of label flipping attacks in federated GANs through both theoretical analysis and empirical evaluation. We further consider an oversampling based variant, in which malicious clients upweight poisoned samples during local training to amplify their influence on the aggregated global model. We quantify the resulting distributional shift by computing the Kullback Leibler divergence between the clean and poisoned class conditional distributions, and show both analytically and on FEMNIST, MNIST, and CIFAR10 that the semantic damage of the attack grows linearly in the effective poisoning strength while deviation from the true target distribution grows only quadratically, making the attack effective yet difficult to detect from label agnostic metrics.

---


### 340. [ASPaeroFlow: Decomposition Heuristics for Joint Air Traffic Flow & Capacity Management](https://arxiv.org/abs/2608.09315)

**<font color=#1a73e8>作者：</font>** Alexander Beiser, Markus Hecher, Nysret Musliu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While mathematical models act as vital decision support systems for operational Air Traffic Flow and Capacity Management (ATFCM), existing approaches isolate Air Traffic Flow Management (ATFM) from Dynamic Airspace Configuration (DAC). This separation introduces an unresolved circular dependency between fixed-demand and fixed-capacity assumptions. Although joint optimization resolves this gap, the enlarged search space renders exact models computationally intractable for medium- to large-scale instances. To bridge this gap, we propose ASPaeroFlow: a heuristic for the joint ATFCM; it combines instance-space decomposition heuristics with a local exact approach using Answer Set Programming. We benchmark ASPaeroFlow from small to industry-sized instances and compare it with exact and alternative approaches. The results indicate that (1) the heuristic provides a computational middle ground between exact methods and operational baselines; (2) simultaneous optimization can outperform sequential optimization on joint ATFCM; and (3) an ablation study indicates that DAC has a larger impact on solution quality than flow measures.

---


### 341. [Warp-free Cross-view Geo-localization via Feature-space Consensus Mining](https://arxiv.org/abs/2608.09321)

**<font color=#1a73e8>作者：</font>** Zhuo Song, Lian Xu, Runqing Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view geo-localization is challenging due to drastic viewpoint changes and large appearance discrepancies between street-level and satellite imagery. Although existing methods often use geometric warping to expose co-visible cues, such transformations rely on restrictive spatial assumptions and inevitably introduce severe visual distortions under view-dependent visibility, yielding noisy supervision and fragile correspondences. To overcome this, we propose a novel joint-view consensus-guided learning framework that entirely bypasses explicit geometric warping. Instead of forcing rigid spatial alignment, we dynamically mine and adaptively strengthen a semantic consensus directly within the feature space. Specifically, an auxiliary joint-view pathway during training enables direct cross-view interaction, allowing each view to selectively aggregate corroborative evidence into a unified consensus representation. To resolve feature heterogeneity among the single- and joint-view streams, we introduce global pattern probes acting as a semantic dictionary to project divergent modalities into a strictly aligned metric space. Guided by a consensus-mediated contrastive objective, single-view embeddings are explicitly pulled toward the joint-view anchor during training, distilling this consensus-mining capability into the single-view encoders for robust retrieval at inference. Extensive experiments demonstrate that our method achieves state-of-the-art performance across four standard benchmarks, underscoring the importance of discovering cross-view semantic consensus for reliable geo-localization.

---


### 342. [Diffusion Image Editing via Asynchronous Token Decoding](https://arxiv.org/abs/2608.09322)

**<font color=#1a73e8>作者：</font>** Yang Shi, Liangsi Lu, Minzhe Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided diffusion image editing aims to modify semantic attributes of an image while preserving its identity, layout, and background. However, naïvely switching the text condition during sampling often causes global drift, as denoising dynamics propagate changes across tokens and can disrupt unedited regions. To address this issue, we propose \textbf{A}synchronous \textbf{T}oken \textbf{D}ecoding \textbf{Edit} (ATDEdit), an inference-time framework that views each sampler step as a parallel update of a globally coupled token matrix and enables token-indexed condition switching with differentiated update policies. Instead of applying synchronous target-conditioned updates to all tokens, ATDEdit estimates editable locations using token-wise conditional surprisal and applies target-conditioned corrections to the selected token set. It supplies source key/value memory at keep-token positions and projects selected keep-token latent rows back to their source values; these operations promote background preservation but do not constitute a pixel-level invariance guarantee. This approach combines local editing and background preservation without external or user-provided spatial masks and without model fine-tuning. On PIE-Bench, ATDEdit achieves the strongest reported preservation metrics, including 27.44~dB PSNR and 0.055 LPIPS, while retaining competitive semantic alignment.

---


### 343. [CoRE: Consensus Rewards via Equilibrium for Test-Time Reinforcement Learning](https://arxiv.org/abs/2608.09324)

**<font color=#1a73e8>作者：</font>** Ambuj Mehrish, Sebastiano Vascon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On unlabeled test data, reinforcement learning lacks a ground-truth reward; test-time RL methods derive one from the model's own roll-outs, rewarding those that match the majority vote over $N$ sampled answers. That vote discards a correct answer whenever it is a minority and scores every majority-matching roll-out identically. We replace it with \emph{CoRE} (Consensus Rewards via Equilibrium): the $N$ roll-outs form a graph whose edges combine answer agreement, reasoning similarity, and generation confidence, and replicator dynamics extract its dominant set, yielding a refined pseudo-label, a graded per-roll-out reward, and a per-question cohesiveness gate. CoRE strictly generalizes voting: majority voting is recovered as a special case; a block-value analysis gives a sharp threshold for when consensus recovers a correct minority against a larger wrong plurality; and confidence calibration provably lowers that threshold multiplicatively. Across seven backbones and five benchmarks (42 model--benchmark cells, three seeds each), \emph{CoRE} improves the untrained base by $+21.7$ points on average versus $+20.4$ for majority-vote TTRL, wins wherever agreement is contestable with margins over the vote of up to $+7.5$ points, and reaches the voting baseline's plateau accuracy in $54$--$70$\% fewer steps. Consensus, not counting: treating the roll-out group as a graph rather than a ballot box turns a brittle vote into a calibrated, graded, self-supervised reward at no extra roll-out cost.

---


### 344. [MaxModShift: Model Privacy via Designed Shifts](https://arxiv.org/abs/2608.09328)

**<font color=#1a73e8>作者：</font>** Nomaan A. Kherani, Urbashi Mitra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model learning by an eavesdropper is treated as an estimation problem in a federated environment. The Fisher Information Matrix for the eavesdropper's estimation problem is driven to singularity through a signaling design; this ensures that the eavesdropper cannot learn the model. Herein, the innovation of prior designs is that model shifts are designed to maximize the difference in the model learned by Eve and the central server while satisfying a transmission power constraint for the agents. Two shift schemes are provided. MaxModShift outperforms a prior ModShift design while requiring lesser transmission power. Compared to a noise injection scheme, MaxModShift performs better while requiring a lower bandwidth secret channel and a reduced average power consumption.

---


### 345. [Hallucinations and Constraints : Regulating surgical workflow recognition beyond accuracy](https://arxiv.org/abs/2608.09332)

**<font color=#1a73e8>作者：</font>** John S. H. Baxter, Pierre Jannin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hallucinations are a major concern for the integration of artificial intelligence into medicine, although less explored in the realm of medical image processing. Unlike problems in natural text understanding and reasoning therewith, determining whether or not predictions derived from biomedical images and signals is less intuitively clear. This article suggests that topological errors could constitute hallucinations in a way that can be more readily measured and thus regulated. Certain of these properties for certain types of problems, such as biomedical signal segmentation, can be rephrased as linear temporal logic predicates, a number of which can be explicitly enforced using probabilistic graphical models. Our simulations show the potential of these explicitly constrained predicates for the case of automatic surgical phase recognition in robot-assisted hysterectomy, improving accuracy by approximately 10% while removing the vast majority of topological errors, suggesting that mathematical guarantees of correctness can supplement other empirical forms of regulating machine learning in medical image computing and computer-assisted interventions.

---


### 346. [Control-Oriented Scenario Tree Construction through Reinforcement Learning](https://arxiv.org/abs/2608.09335)

**<font color=#1a73e8>作者：</font>** Fabio Pavirani, Bert Claessens, Pierre Pinson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multistage stochastic model predictive control (MPC) handles uncertainty by optimizing over a scenario tree, a finite branching approximation of future outcomes constructed from sampled forecasts. To build such a tree, conventional methods focus on matching the underlying probability distribution---e.g., via Wasserstein-based scenario reduction---but improved distributional accuracy does not necessarily yield better control performance. We propose a control-oriented approach that learns scenario tree construction directly from its impact on downstream decisions. Fixing the tree topology, we formulate tree construction as a sequential assignment of sampled scenarios to leaves. This assignment is parameterized by an attention-based policy over the scenario set and trained using reinforcement learning, with closed-loop control profit as the objective. Training is stabilized by an asymmetric critic that leverages realized future trajectories. We evaluate the method on a risk-averse battery arbitrage problem. Across a range of forecast set sizes, the learned construction consistently achieves the highest profit, outperforming classical forward and backward reduction methods and certainty-equivalent (single-trajectory forecast) control. The learned policy also exhibits greater robustness on challenging instances, consistently demonstrating better tail-risk characteristics. Analysis of the resulting trees indicates that our method constructs compact, selectively branching structures that capture high-impact events while keeping most trajectories nearly deterministic. These findings highlight that the value of a scenario tree depends critically on the decisions it supports, and provide an effective framework to train scenario tree constructors merely based on the closed-loop control optimization signal.

---


### 347. [Revisiting the Current Frame: Physical-Trace-Guided Network Output Correction for Video Restoration](https://arxiv.org/abs/2608.09342)

**<font color=#1a73e8>作者：</font>** Yifeng Lin, Liuxiang Qiu, Guangming Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video restoration methods exploit temporal information to recover information missing from degraded observations. However, reference frames within the sequence may introduce inconsistent degradation, content discrepancy, or reconstruction errors due to physical image-formation variations, occlusion, and imperfect temporal aggregation. Existing approaches mainly focus on improving restoration networks, while the reliability of the generated outputs at different spatial locations remains largely unexplored. In this work, we propose ANCHOR, a model-agnostic framework that revisits the low-quality current frame as a temporally aligned anchor for video restoration correction. Specifically, ANCHOR estimates a spatial trust field from heterogeneous physical-trace evidence and adaptively balances the restoration proposal with the original observation. Experiments on High Dynamic Range video reconstruction and video deraining demonstrate consistent improvements across various state-of-the-art restoration models, validating the effectiveness of reliability-aware output correction for video restoration.

---


### 348. [One-Time Training for All Grains: Open-Set Grain Recognition and Quantitative Analysis](https://arxiv.org/abs/2608.09345)

**<font color=#1a73e8>作者：</font>** Qihe Su, Mengyu Sun, Yuxi Ke 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in crop breeding have introduced an increasing number of grain varieties, creating a growing demand for efficient variety recognition and quantitative analysis. However, existing methods are typically trained on a fixed variety set, and incorporating newly introduced varieties requires additional data collection and model retraining. To address this limitation, we propose GROW, a framework for Grain Recognition and quantitative analysis in Open sets Without retraining. GROW first performs class-agnostic grain localization, converting mixed-grain images into individual instances for variety-wise counting and phenotypic measurement. It then combines visual embeddings and morphological descriptors into fused grain descriptors stored in an extensible GrainBank. Query grains are recognized through rank-similarity weighted top-k retrieval, and newly introduced varieties are incorporated by appending their descriptors without updating the deployed models. Extensive experiments under progressive variety expansion, varying grain densities, and background domain shifts demonstrate the scalability, robustness, and adaptability of GROW. Compared with joint retraining, GROW reduced the average category-registration time from 4153 s to only 39 s while maintaining competitive recognition performance. These results demonstrate that GROW provides an efficient and maintainable solution for extensible grain recognition, counting, and phenotypic analysis without repeated model retraining.

---


### 349. [In-Context Density Estimation for Tabular Data](https://arxiv.org/abs/2608.09348)

**<font color=#1a73e8>作者：</font>** Patryk Marszałek, Jacek Tabor, Marek Śmieja  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Density estimation underlies many unsupervised tasks on tabular data such as anomaly detection, out-of-distribution detection, and data augmentation. Although all these problems reduce to questions about where probability mass lies, they are typically solved individually by fitting a separate model to each dataset, with its own hyperparameters and tuning budget. We introduce ICED, an in-context, energy-based density estimator that removes this per-dataset cost. ICED is a transformer-based model pretrained once on a synthetic prior built specifically for density estimation under an objective that fits log-density where it is informative and preserves its ordering elsewhere. In the inference, it reads a dataset as context and returns an unnormalized log-density for any query point in a single forward pass, with no fitting, sampling, or hyperparameter selection. A single frozen ICED model then drives four tasks usually handled by four specialized pipelines: density estimation, out-of-distribution detection, unsupervised anomaly detection, and generative augmentation. Across all four, it is competitive with the strongest task-specific method, while being the only approach that needs no retraining, no tuning, and no labels to move between them. The code is available at this https URL.

---


### 350. [Alpha as an Efficiency Signal: Visibility-Routed RGBA Image-to-Video Generation](https://arxiv.org/abs/2608.09355)

**<font color=#1a73e8>作者：</font>** Zhe Li, Honghao Qiao, Zhixin Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGBA videos combine RGB appearance with an alpha channel, enabling animated assets to be applied across arbitrary backgrounds, which are heavily used in gaming industry. However, generating high-quality RGBA animations for games remains challenging for two reasons. First, most existing RGBA video datasets are dominated by photorealistic content, with limited coverage of game assets. Second, the traditional generate-then-matte pipelines estimate alpha only after RGB synthesis, so semi-transparent regions are often blurred by background, resulting in unstable matting outputs. More recently, many methods have begun to model RGB and alpha jointly, but existing approaches are mostly text-conditioned, and still have unresolved issues in efficiency and quality. To address these challenges, we introduce GameAlpha-2.4K, a 2.4K-clip game-style RGBA video dataset built with matte-friendly synthesis, multi-hypothesis alpha recovery, and compositing-based quality gates. Using this dataset, we train a reference-conditioned RGBA video generator that jointly produces RGB frames and alpha mattes in a single pass. To improve efficiency, we propose a visibility router that identifies transparent tokens in an early stage and bypasses their later DiT updates, while x_0-lock guides them along the original flow-matching schedule toward self-predicted endpoints. Our model obtains lower FVD than traditional two-stage pipelines, and the visibility router skips 35% of token evaluations in the final two DiT denoising steps, providing a 1.2x backbone speedup with negligible quality degradation compared to dense inference.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-445](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
