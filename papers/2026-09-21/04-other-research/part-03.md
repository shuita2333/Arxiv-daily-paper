# 📦 其他研究 | 2026年09月21日

> 本类共 **247** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-247](./part-05.md)

---

### 101. [Graph-Based Stochastic Power-UCT: Monte-Carlo Graph Search with Power Mean Estimation](https://arxiv.org/abs/2609.19956)

**<font color=#1a73e8>作者：</font>** Tung Tran, Viet Bao Mai, Hoang Ta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tree-based Monte-Carlo Tree Search (MCTS) duplicates the same state when it is reached through different trajectories, which can waste simulations in stochastic MDPs. We introduce Graph-Based Stochastic-Power-UCT (GS-Power-UCT), which shares states reached at the same planning depth while keeping separate values for states reached at different depths. This design applies to general stochastic MDPs, including problems with cycles. We prove that for a fixed planning horizon, the root estimate converges to the finite-horizon value at rate $O(n^{-1/2})$, matching tree-based Stochastic-Power-UCT while reusing samples across shared states. We also study two full-state variants: GS-Power-UCT-F, which stores one node per physical state to increase sample sharing but may mix values from different remaining horizons, and GS-Power-UCT-F$^+$, which uses an adaptive horizon to control this bias. The latter converges to $V^{\star}(s_0)$, the optimal infinite-horizon discounted value at the root state $s_0$, when the remaining cross-depth gap vanishes. Experiments on stochastic planning benchmarks show improved sample efficiency over tree-based and graph-based baselines.

---


### 102. [Neuro-Symbolic Agentic AI for Networked Low-Altitude UAVs](https://arxiv.org/abs/2609.19961)

**<font color=#1a73e8>作者：</font>** Yuqi Ping, Tianhao Liang, Nanchi Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Networked low-altitude unmanned aerial vehicles (UAVs) need reliable and adaptive decision-making capabilities to operate under uncertain observations, dynamic environments, and intermittent connectivity, while many existing agentic systems remain limited by hallucination risks, data dependence, and weak generalization. This article investigates neuro-symbolic agentic AI (NSAAI) as a framework for combining neural grounding, symbolic reasoning, and closed-loop agentic interaction to support more reliable and adaptive UAV autonomy. We first examine its capability foundations in data efficiency, compositional generalization, continual learning, and zero-shot transfer, and then develop a reference architecture integrating task and goal management, neuro-symbolic planning, verification and metacognition, skill execution and network interaction, and shared knowledge and memory. An urban fire-inspection case implemented in LAESim illustrates how a UAV can coordinate sensing and cloud access under intermittent connectivity, reuse a verified image-delivery skill, and satisfy explicit evidence conditions before completing the mission. The results illustrate the potential of NSAAI to support reusable skills, evidence-grounded decision-making, and adaptive mission execution in networked UAV systems. We further discuss key research directions in uncertainty-aware reasoning, knowledge and skill expansion, adaptive self-monitoring, and standardized evaluation.

---


### 103. [Enhanced Knowledge Distillation for Detection Transformer via Teacher Prediction Refinement](https://arxiv.org/abs/2609.19964)

**<font color=#1a73e8>作者：</font>** Yitong Xing, Yuhao Cheng, Yanping Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detection Transformers (DETRs) achieve strong performance in object detection but remain challenging to deploy on edge devices due to their high computational cost. Existing DETR distillation methods mainly focus on aligning distillation points, while largely overlooking the quality of the teacher's supervision itself. We observe that due to stage-wise non-monotonic prediction behavior in DETRs, well-localized or correctly classified predictions from earlier stages may degrade in later ones, and some negative predictions become increasingly overconfident. As a result, relying solely on the current stage's predictions yields inaccurate and inconsistent supervision. To address this issue, we propose Teacher Prediction Refinement Distillation (TPRD), a plug-and-play module that refines teacher predictions before distillation by exploiting stage-wise prediction information. TPRD improves supervision quality through Positive Prediction Correction (PPC), which corrects degraded positive predictions by restoring more accurate ones from earlier stages, ensuring reliable localization and classification signals, and Negative Prediction Suppression (NPS) suppresses the influence of overconfident negatives, preventing them from providing misleading supervision to the student. To preserve informative dark knowledge, we further introduce Maximum Dark Knowledge Preservation (MDKP), which selectively refines target-class logits while retaining non-target relations. Extensive experiments on MS COCO and PASCAL VOC demonstrate the effectiveness and robustness of the proposed method. Our code is available at this https URL.

---


### 104. [Beyond the Foreground: FOV-Aware Polyp Image Synthesis via Lesion-Guided Adaptive Mucosal Context Propagation](https://arxiv.org/abs/2609.19966)

**<font color=#1a73e8>作者：</font>** Tong Wang, Yuting He, Bin Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic image and mask pairs can alleviate scarce colonoscopy annotations, but realistic synthesis requires preserving the supplied lesion while generating compatible mucosa. Existing foreground-guided methods treat all non-foreground pixels as background and rely mainly on local integration. Directly applying them to colonoscopy causes two problems: non-mucosal black regions contaminate generated tissue, and local reasoning produces inconsistent mucosal texture and illumination. We propose LAMP, the first foreground-guided framework for polyp image synthesis based on lesion-guided adaptive mucosal context propagation. LAMP explicitly separates the lesion, valid mucosa, and camera exterior using a field-of-view (FOV) mask. Lesion-to-Mucosa cross-attention extracts lesion appearance conditions for valid-mucosa locations, while FOV-constrained multidirectional Vision Receptance Weighted Key Value propagates them over legal tissue support. An adaptive gate then controls their residual fusion into the diffusion U-Net. Extensive experiments on five polyp datasets demonstrate that LAMP substantially outperforms existing methods in overall generation quality and consistently improves five downstream segmentation models. Our code will be released at this https URL.

---


### 105. [CellRFT: Reinforcement Fine-Tuning for Single-Cell Perturbation Modeling](https://arxiv.org/abs/2609.19970)

**<font color=#1a73e8>作者：</font>** Jie Yan, Li Liu, Hanze Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting cellular responses to perturbations supports the study of gene function, disease mechanisms, and therapeutic strategies. Despite advances in single-cell perturbation modeling, existing models typically optimize surrogate losses that do not directly reflect the biological criteria used for evaluation, so better data fitting need not yield better biological predictions. To address this mismatch, we introduce \textbf{CellRFT}, a reinforcement fine-tuning framework that uses biological evaluation as direct training feedback. CellRFT uses policy-gradient optimization to learn from non-differentiable evaluations of generated cell populations and integrates multiple biological rewards through hierarchical reward aggregation. Comprehensive experiments demonstrate CellRFT's applicability across different pretrained models and effectiveness in improving perturbation prediction, reveal that optimizing one biological criterion can help or hinder others, and show that complementary rewards can improve criteria beyond those directly optimized, offering a way to probe how biological metrics shape model behavior, with the potential to inform evaluation design. Code will be made available.

---


### 106. [An Event Preserving Velocity Invariant Representation for Event Cameras](https://arxiv.org/abs/2609.19973)

**<font color=#1a73e8>作者：</font>** Mikihiro Ikura, Luna Gava, Jiahang Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras provide low-latency, high temporal resolution perception for real-time vision tasks such as this http URL novel circuitry (i.e. asynchronous, independent pixels) that enables these advantages also introduces new algorithmic challenges. Velocity-invariant representations alleviate missing observations under slow motion and motion blur under fast motion, but most discard temporal information by converting events into image-like representations. We propose Set of Centre Active Receptive Fields (SCARF), a real-time velocity-invariant representation that preserves raw events while consistently handling fast motion, stationary scenes, and independently moving objects. SCARF achieves state-of-the-art performance in both computational efficiency and representation quality.

---


### 107. [JANUS: Denial-of-Service Attack Against Beam Hopping in LEO Satellite Networks](https://arxiv.org/abs/2609.19977)

**<font color=#1a73e8>作者：</font>** Yuval Aviv, Roee Idan, Roy Peled 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Low Earth orbit (LEO) satellite networks are increasingly used to provide global connectivity. However, each satellite has limited resources that need to be allocated according to demand, which varies geographically and over time. Beam hopping addresses this challenge by dividing a satellite's service area into geographic cells. Rather than illuminating every cell simultaneously, it dynamically assigns available beams to a selected subset based on demand. This reliance on observed traffic demand as an input to beam-selection decisions creates a new attack surface whose security implications have received little attention. In this paper, we present JANUS, a novel targeted denial-of-service attack against beam-hopping systems in LEO networks. We show that a small botnet of compromised terminals can inject legitimate user traffic into carefully selected non-victim cells to manipulate the beam-hopping scheduler's view of demand. This manipulation alters beam-allocation decisions and redirects service away from the targeted victim area. We evaluate JANUS across different system configurations, schedulers, attack horizons, and attacker-knowledge settings to characterize the attack's effectiveness, required resources, and resulting service disruption over time. Against a rank-based KMAX scheduler, JANUS achieves complete service denial for up to approximately 95% of evaluated victims. Against DRL, JANUS can exclude the victim from approximately 92% of scheduling decisions. Finally, we evaluate mitigation strategies that reduce the attack effectiveness.

---


### 108. [Past, Future, All at Once: Mitigating Stability-Plasticity Dilemma via Post-hoc JANUS Rectification](https://arxiv.org/abs/2609.19985)

**<font color=#1a73e8>作者：</font>** Zhilong Zheng, Letian Tao, Yang Guan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning foundation models on new tasks inevitably suffer from catastrophic forgetting. While existing works attempt to mitigate this on the basis of parameter-efficient fine-tuning methods, they adopted an overly restrictive Subspace Orthogonality condition. In this paper, we introduce a purely post-hoc and tuning-agnostic weight rectification framework that achieves Parameter Space Orthogonality, which is the necessary and sufficient condition for preserving historical performance to the first order. By projecting parameter updates into the JAcobian NUll Space (JANUS), our method significantly recovers compromised historical knowledge without interfering with the underlying fine-tuning process. To overcome the local validity of the Jacobian approximation, we further propose a Multi-step Adaptive Rectification mechanism that utilizes the JANUS shift to dynamically verify the valid trust region and adjust step sizes. Coupled with our proposed ghost projection, ghost orientation comparison, and sequence-level singular value decomposition compression techniques, JANUS also achieves great temporal and spatial efficiency. Experiments demonstrate that JANUS seamlessly integrates with various fine-tuning methods, significantly mitigating the stability-plasticity dilemma by recovering historical knowledge while preserving downstream task adaptation.

---


### 109. [Customizable and Jointly Optimized Route Planning: A Deep Architecture Enabling Differentiable Shortest-Path Search](https://arxiv.org/abs/2609.19996)

**<font color=#1a73e8>作者：</font>** Rui Zhao, Chao Chen, Longfei Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the widespread use of online navigation and ride-hailing services, achieving optimal route planning for diverse user preferences has recently attracted increasing attention. Classic graph algorithms for pathfinding use heuristic cost functions to define edge weight, thus providing no optimality guarantee of route quality. Prior data-driven approaches equating ground truth of the optimal route with user trajectory, which is however moderately influenced by the navigation service, suffers from the feedback loop problem. To address these issues, we propose a deep architecture that is able to jointly optimize cost functions and route-ranking model towards any route preference. First, we run a multi-objective Dijkstra algorithm offline to collect the set of Pareto optimal routes, deeming it as the complete candidate set. Exploiting the property of such a set, we design a neural network structure that emulates shortest-path search and route ranking in an end-to-end differentiable manner. Second, we define route preference as a task of constrained optimization of route attributes, and propose a novel loss function that optimizes a single-objective variable, with other variables strictly under constraints. We conduct extensive experiments on real-world datasets. The results show that our architecture significantly outperforms state-of-the-art methods in route quality and customizability.

---


### 110. [E-AVI: Evidence-Grounded Multimodal Assessment for Automated Video Interviews](https://arxiv.org/abs/2609.20001)

**<font color=#1a73e8>作者：</font>** Haoshen Wang, Dongbo Che, Zeyi Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated video interview assessment integrates verbal content, acoustic delivery, and visual behavior, yet numerical predictions alone provide limited inspectable support. We present E-AVI, an evidence-grounded framework that extracts timestamped multimodal evidence and integrates dimension-conditioned evidence attention with source-level embeddings for scoring. A shared evidence pool further supports natural-language feedback and follow-up question answering. On RecruitView and a private hospitality dataset, E-AVI consistently outperforms fine-tuned multimodal baselines in rank correlation. Ablation, evidence-deletion, bootstrap, human-audit, and QA analyses characterize the predictive contribution, grounding, and practical utility of the evidence pathway. Together, these results demonstrate that our proposed E-AVI framework improves predictive performance while providing inspectable support for assessment, feedback, and interactive analysis.

---


### 111. [Dynamic Generalized Gromov-Wasserstein Optimal Transport](https://arxiv.org/abs/2609.20008)

**<font color=#1a73e8>作者：</font>** Junda Ying, Zhiwei Zeng, Peijie Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gromov--Wasserstein optimal transport (GW-OT) extends classical optimal transport by introducing structure-aware transport cost. This is particularly relevant for spatial transcriptomics, where dynamical reconstruction should preserve tissue structure in addition to matching expression patterns. While static formulations have been widely used for such structure-aware alignment, a general dynamic formulation for reconstructing continuous trajectories is still missing. We introduce Travelling Pair Dynamical Alignment and Trajectory Estimation (TP-DATE), a theoretical and computational framework to generalize GW-OT dynamically in a simulation-free manner. We formulate a broad class of static and dynamic Quadratic-form OT (QOT) through path actions and prove the static dynamic equivalence. We further develop travelling-pair flow matching, which allows interacting conditional paths and marginalizes their interactions into a single vector field. On synthetic and real spatial transcriptomics data, TP-DATE better preserves spatial structure and improves continuous 3D dynamics reconstruction.

---


### 112. [XIR: A Framework for Interoperability across Cross-Chain Protocols Based on a Verifiable Intermediate Representation](https://arxiv.org/abs/2609.20010)

**<font color=#1a73e8>作者：</font>** Yushen Li, Linpeng Jia, Jiaying Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cross-chain protocols enable applications to exchange messages across blockchains. Under point-to-point configurations, communication depends on a direct connection between the source and destination blockchains, limiting blockchain reachability and requiring additional configurations to connect more blockchains. To quantify this problem, this paper analyzes approximately 25 million mainnet cross-chain transaction events collected from six protocols (Axelar, CCIP, Hyperlane, LayerZero, Relay, and Wormhole) between January and October 2025. The resulting graph covers 286 active blockchains and 11,935 directly connected ordered blockchain pairs. These connections provide a direct reachability of 14.64%, while full direct connectivity would require 81,510 point-to-point configurations. We present XIR, a framework for interoperability across cross-chain protocols based on a verifiable intermediate representation. This representation binds an application message to an ordered record of authenticated cross-chain protocol deliveries, preserving message identity and verification history across protocol boundaries. XIR Gateways and XIR Adapters use this representation to compose existing connections into same-protocol and cross-protocol multi-hop paths. We implement an XIR prototype integrating Hyperlane and LayerZero and evaluate it in local and public-testnet environments. Theoretical analysis and evaluation show that, with correctly configured cross-chain protocol connections, XIR avoids 67,018 additional point-to-point configurations, equivalent to 84.88% of the total required by a point-to-point configuration baseline serving the same reachable pairs, and increases reachability from 14.64% to 96.86% of all ordered blockchain pairs.

---


### 113. [GRF-Recon: Global Ray-Field Optimization for Long-Sequence Feed-forward Reconstruction](https://arxiv.org/abs/2609.20012)

**<font color=#1a73e8>作者：</font>** Enpeng Li, Yunzhou Zhang, Zhiyao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction provides an efficient paradigm for scene modeling from image sequences. Scaling these models to large monocular scenarios are constrained by excessive GPU memory footprint, degraded local geometry, and long-term trajectory drift. Existing chunk-based optimization strategies provide limited geometric constraints and fail to maintain global consistency over extended trajectories. We present a unified framework for stable and scalable feed-forward 3D reconstruction from long monocular sequences. Our approach builds on coarse-to-fine trajectory alignment augmented by lightweight geometric prior injection. Distilling monocular geometric cues into the feed-forward backbone via LoRA adaptation improves depth accuracy on fine structures while preserving inference efficiency. We introduce a hybrid-weight sparse ray-field optimization that leverages high-frequency geometric features to guide local point-cloud refinement and enforce consistent inter-frame ray constraints. Unlike prior chunk-based methods, this establishes strong cross-frame geometric coupling while maintaining scalability. Finally, an efficient trajectory stitching strategy with joint ray-error optimization explicitly reduces accumulated drift. Extensive experiments show that our approach achieves competitive trajectory accuracy compared with representative SLAM systems, while maintaining globally consistent 3D reconstruction in large-scale scenarios.

---


### 114. [FedeRICo: Federated Region-Influenced Coupling for Traffic Flow Prediction](https://arxiv.org/abs/2609.20026)

**<font color=#1a73e8>作者：</font>** Fermin Orozco, Man Luo, Johan Wahlström  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban traffic forecasting often relies on information distributed across stakeholders who may be unable to share raw data due to privacy or commercial constraints, motivating federated spatial-temporal approaches. In such federated settings, each client observes traffic over a distinct sensor subgraph with its own spatial topology and temporal dynamics, leading to significant heterogeneity across clients. Existing federated spatial-temporal methods typically rely on model parameter aggregation and provide limited mechanisms for recovering spatial dependencies across client boundaries. This introduces two key limitations. Specifically, parameter aggregation across heterogeneous graph domains tends to dilute client-specific representations, while road network partitioning breaks the propagation of traffic dynamics across client boundaries. To address these challenges, we propose FedeRICo, a federated traffic forecasting framework that combines gradient-level collaboration with boundary-aware residual communication. FedeRICo employs a dual-branch forecasting architecture in which a globally guided branch captures transferable forecasting structure, while a private residual branch preserves client-specific corrections and incorporates boundary residual signals. The global branch is coordinated through gradient alignment across all clients, enabling collaborative optimisation without destructive parameter interference. To recover cross-client spatial dependencies, boundary messages are extracted through a trend-residual decomposition that suppresses periodic structure and communicates only transient spatial-temporal residual signals between physically adjacent clients. Experiments across four real-world traffic forecasting benchmarks demonstrate that FedeRICo consistently outperforms state-of-the-art federated spatial-temporal baselines while maintaining competitive training runtime.

---


### 115. [Astronex-World 1.0: Real-Time Interactive World Model Foundation](https://arxiv.org/abs/2609.20034)

**<font color=#1a73e8>作者：</font>** Xin Zhou, Cong Miao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Astronex-World 1.0, an open controllable video world-model foundation. Given a text prompt (text-to-video) or an initial observation (image-to-video), the model predicts future visual states under frame-aligned camera trajectories, continuous actions, and an embodiment identifier, and accepts text events inserted at a specified position of a rollout. The family provides a bidirectional model for full-context generation and a causal model with block-causal attention and cross-block KV caching for persistent generation, both built on the Wan2.2-TI2V-5B prior. PRoPE injects camera intrinsics and extrinsics, while a 64-dimensional action stream modulates every Transformer layer. A five-stage training path develops bidirectional camera and action control, converts the backbone to block-causal generation, distills a few-step student, restores mixed-domain dynamics, and applies asymmetric DMD/DMD2 distribution matching. The causal model generates 832x480 video at 24 fps. All five training stages run on two NVIDIA L20 48 GB GPUs, and the causal model streams in real time on one. It scores 73.5 on WBench Navi and 70.0 on WBench Full. On Full, this 5B model is above the 13.6B LongCat-Video and the 14B Helios, within one point of the 22B LTX-2.3, and above YUME 1.5, which is post-trained from the same 5B prior on NVIDIA A100 GPUs. The reserved action input and output interfaces allow post-training for embodied intelligence and autonomous driving.

---


### 116. [DART: Distillation-Aware Reparameterization for Training-Free LoRA Reuse in Few-Step Video Diffusion Models](https://arxiv.org/abs/2609.20051)

**<font color=#1a73e8>作者：</font>** Shihong Li, Juntao Xu, JinCao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Step distillation reduces the cost of video generation, but reusing a LoRA trained for a longer trajectory can alter its functional effect or degrade target quality. Static parameter compatibility offers one perspective on this problem; our observations show that similar measured geometry can coexist with different adapter behavior under a shortened denoising schedule. We propose DART, a training-free method that combines low-rank coordinate transport with target-schedule response calibration using forward evaluations and no source training videos. On a four-step Wan2.2 target, DART-F improves the joint quality score from 0.9029 to 0.9227 and changes macro functional retention from -0.4644 to +0.1349. Component analysis shows that calibration accounts for most of the quality improvement, while coordinate transport provides complementary gains when combined with calibration. Adapter-level results reveal positive functional effects for some adapters and strong attenuation with reduced negative functional effects for others. Evaluations on two additional targets show the same aggregate trend. These results motivate evaluating distilled-model LoRA reuse jointly through functional preservation and negative-transfer avoidance, without assuming recovery for every adapter.

---


### 117. [MAGMA-GEN: Validated Recovery Supervision from Ambiguous Failures via Counterfactual Re-Execution](https://arxiv.org/abs/2609.20056)

**<font color=#1a73e8>作者：</font>** Loan Bernat, Matthieu Grard, Ariane Herbulot 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hierarchical robotic systems executing long-horizon manipulation tasks must make high-level semantic decisions that orchestrate stochastic low-level skills. In this setting, failed rollouts are ambiguous: a poor downstream state may reflect an invalid high-level decision, partial observation, or a valid decision whose physical execution failed. Traditional supervised learning lacks data for such recovery states, while reinforcement learning struggles with sparse rewards and non-local credit assignment. We propose MAGMA-GEN, an on-policy data-generation pipeline that converts ambiguous failed rollouts into validated recovery supervision. MAGMA-GEN first uses a privileged coach to hypothesize an early decision-level error and propose localized correction or recovery actions. Because this diagnosis is fallible, candidates are retained only if re-execution from the same state under matched conditions improves downstream progress. This produces supervised examples from the agent's own failure distribution without per-step human demonstrations. Evaluated on interactive long-horizon manipulation tasks, MAGMA-GEN improves task success and recovery capabilities, against distillation and trajectory-repair baselines under evolving task constraints in both simulation and real-robot execution.

---


### 118. [Evaluating Explanation Methods by the Predictors They Induce](https://arxiv.org/abs/2609.20058)

**<font color=#1a73e8>作者：</font>** Jacob Selbæk, Hugo L. Hammer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explanations of machine learning models are usually judged by criteria that are hard to compare. We propose a simpler test: if an explanation really describes how a model uses its features, it should be possible to rebuild the model's predictions from it. We turn each explanation into a predictor by reading each feature's effect and adding them up, and measure how well that predictor reproduces the model on unseen data. Nothing is fitted, so the score reflects the explanation itself. The test applies to any explanation that can be written as a function of the features; we demonstrate it on partial dependence plots (PDP), accumulated local effects (ALE), SHAP and LIME. We prove that summing partial dependence curves gives the best possible additive summary of a model when its features are independent, and that this fails when they are dependent. Across 13 real datasets and 9 synthetic designs and four model families, which method scores best depends entirely on feature dependence: where features are independent SHAP is slightly worse than PDP, exactly as the theory predicts; on dependent real data SHAP leads. Some widely used quality metrics even prefer a damaged explanation to an intact one.

---


### 119. [AI Should Facilitate Democratic Deliberation at Scale](https://arxiv.org/abs/2609.20059)

**<font color=#1a73e8>作者：</font>** José Ramón Enríquez, Jiaxin Pei, Alex Pentland  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI systems can strengthen democracy by supporting deliberation at scale by addressing cognitive, social, platform-design, and market-driven frictions, while preserving human agency. Unlike proposals such as liquid democracy that restructure representation through vote delegation, in this position paper, we argue that AI-assisted deliberation offers a more promising path by lowering barriers to meaningful engagement without substituting machine judgment for human choice. Drawing on evidence from online deliberation platforms and experimental research, we identify four guiding principles: preserving agency and autonomy, encouraging mutual respect, promoting equality and inclusiveness, and augmenting rather than substituting active citizenship. We also address critical challenges, including alignment, sycophancy, training bias, and over-reliance on AI systems. We call on the machine learning community to develop deliberation-focused AI systems evaluated not on engagement metrics but on their capacity to facilitate informed, representative, and friction-robust discourse.

---


### 120. [PointEvent: Rethinking Event-based Tiny Object Detection via Serialized Motion Evidence Accumulation](https://arxiv.org/abs/2609.20066)

**<font color=#1a73e8>作者：</font>** Zongze Wu, Baofeng Jia, Weiqi Yan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras offer high temporal resolution and motion sensitivity for tiny UAV detection, yet distant targets generate sparse and fragmented events that are easily overwhelmed by clutter and ego-motion. Existing methods mainly rely on dense event representations or local sparse spatiotemporal modeling, resulting in redundant computation or fragmented modeling of motion continuity across distant asynchronous events. To address this limitation, we introduce serialized motion evidence accumulation, which treats motion continuity as an ordered evidence propagation process. Specifically, the same event stream is organized into locality-preserving spatiotemporal paths and chronology-preserving temporal paths through the latent complementary serializations. Based on this principle, we propose PointEvent, a lightweight event-wise state-space framework that alternates serialized scans across the complementary orders, progressively consolidating fragmented motion evidence beyond fixed local neighborhoods. A high-resolution event branch preserves fine-grained target responses, while compact context modulation suppresses interference. Experiments demonstrate that PointEvent achieves SOTA with the fewest parameters and fastest measured inference among the compared methods. Code: this https URL

---


### 121. [FCA-Guided Counterfactual Explanations for Multi-Modal Breast Cancer Diagnosis: A Framework Achieving Perfect Validity with Emergent Sparsity](https://arxiv.org/abs/2609.20067)

**<font color=#1a73e8>作者：</font>** Abdullahi Isa, Souley Boukari, Muhammad Aliyu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning models for multi-modal breast cancer diagnosis achieve high predictive accuracy but remain clinically unacceptable without actionable, counterfactual explanations. Attribution-based methods (LIME, SHAP) are categorically inapplicable to this purpose, as they generate no alternative instances and thus cannot be evaluated on counterfactual quality metrics. This investigation provides empirical evidence that FCA-Guided Counterfactual (FCA-CF) framework that uses a Formal Concept Analysis (FCA) concept lattice as a hard structural constraint on counterfactual search, operating over a multi-modal TCGA-BRCA dataset. We benchmark against four genuine counterfactual methods: Wachter-style CF, DiCE, FACE, and NICE, evaluated on 60 benign-predicted TCGA-BRCA instances. The FCA-CF framework achieves Validity = 1.0000 (100% of counterfactuals successfully flip the prediction), Sparsity = 2.37 features changed (best among all valid methods), and Proximity = 0.900 (normalised L2-based, matching NICE as joint best). The classifier achieves Accuracy = 0.980, F1 = 0.976, ROC-AUC = 0.9947. Ablation analysis confirms that the FCA lattice constraint is the primary sparsity driver (removing it increases sparsity by +40%, p < 0.001, Cohen's d = 0.78), while Phase C greedy refinement accounts for the largest individual contribution (+113% sparsity increase when disabled, p < 0.001, d = 5.01). FCA-guided counterfactual generation achieves a clinically important Pareto-dominant outcome; it is simultaneously the sparsest and among the most proximate of all valid methods, with perfect validity. The emergent sparsity property arising from lattice topology rather than numerical penalty terms constitutes a structurally novel contribution to the counterfactual explanation literature.

---


### 122. [Competition, Collusion, and Corruption: The Spectrum of MEV Attacks on DAG-Based BFT Consensus Protocols](https://arxiv.org/abs/2609.20069)

**<font color=#1a73e8>作者：</font>** Iliya Mirzaei, Heer Patel, Chenyuan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Byzantine Fault-Tolerant (BFT) protocols guarantee safety and liveness despite the malicious failure of nodes. However, they do not prevent adversarial manipulation of transaction order, where the order a proposer assigns diverges from the order in which clients submitted their transactions. Exploiting this discretion for profit is known as maximal extractable value (MEV), and it is intensified in DAG-based BFT protocols, where every replica proposes blocks concurrently rather than routing transactions through a single designated proposer each round. The proliferation of MEV attacks on DAG-based BFT protocols has made the resulting landscape difficult to navigate: attacks are reported individually, on different protocols, and under different metrics, making it unclear whether two attacks differ fundamentally or merely in how they are described. This paper closes that gap by presenting an attack space for MEV on DAG-based BFT protocols, organized around four families: the adversary, the protocol, the target, and the deployment. For each family, we identify the dimensions that shape an attack's impact. Each point in the attack space fixes one value per dimension, thereby representing a distinct, potential MEV attack, which can then be instantiated on a specific DAG-based BFT protocol. We perform a set of experiments, each isolating a single dimension where the protocol permits it, to empirically measure its effect on the success rate of MEV attacks against six production DAG-based BFT protocols. Our experimental evaluation reveals that every protocol we evaluate is vulnerable to at least a subset of the MEV attacks in this space, and that which attacks succeed is mostly dictated by the protocol's own design rather than by attacker effort.

---


### 123. [A Proposal for an Agentic AI Architecture to Support Multi-Domain Decision-Making in the Brazilian Armed Forces](https://arxiv.org/abs/2609.20080)

**<font color=#1a73e8>作者：</font>** Gioliano de Oliveira Braga, Sidnei Barbieri, Ágney Lopes Roth Ferraz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing complexity of multi-domain operational environments (land, aerospace, naval, cyber, and electromagnetic spectrum) has increased the volume and velocity of data reaching command-and-control (C2) centers, straining the observe-orient-decide-act (OODA) decision cycle. Artificial Intelligence (AI) systems currently employed in defense are, in general, reactive and isolated tools that still rely heavily on human operators to integrate information, assess scenarios, and formulate courses of action. This paper proposes a conceptual Agentic AI architecture for AI systems that can plan, access data sources, execute tools, and act autonomously and audibly, aimed at supporting decision-making across the three Brazilian Armed Forces (Navy, Army, and Air Force). Four application fronts are discussed (decision support, situational analysis, feasibility studies, and countermeasure suggestion), as well as the data and sensor access requirements and the security and permission safeguards necessary for responsible employment across administrative, strategic, operational, and tactical contexts.

---


### 124. [SETTer: Sparse-Encoder Transformer for Long-term Multivariate Time Series Forecasting](https://arxiv.org/abs/2609.20086)

**<font color=#1a73e8>作者：</font>** Abraham Ezema, Chijioke Eze, Ferdinanda Ponci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term multivariate time series plays a significant role in many application areas such as power systems, trading, etc. However, their accurate prediction is quite difficult for conventional forecasting methods as they often exhibit high dimensionality and complex relationships. Recent works show that transformer-based approaches are quite effective for long-term forecasting thanks to their attention mechanism. However, in the presence of complex high-dimensional inputs, they show evidence of oversmoothing, limited capacity, and opacity. To this end, this paper introduces SETTer, a transformer-based model that addresses these challenges by incorporating novel techniques for decoupled self-attention and hybrid masking. The proposed techniques enable SETTer to effectively capture the dominant short- and long-term patterns across the temporal and channel dimensions. In addition, we enrich the model layers with simple explainable structures that indicate the discriminative pattern of SETTer. We show that with a single-layer transformer architecture, SETTer can effectively model long-term dependencies in the presence of varying data complexities. Extensive experiments on real-word benchmark datasets for long-term multivariate time series forecasting demonstrate that SETTer outperforms state-of-the-art models in 88% of the scenarios.

---


### 125. [G^2RA-NET: Graph-based Cross-Slice Relation Modeling with Attention Gating for Medical Image Segmentation](https://arxiv.org/abs/2609.20088)

**<font color=#1a73e8>作者：</font>** Shengye Wang, Zonglin Wu, Liang Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation supports quantitative clinical analysis and computer-aided diagnosis. Recent methods for medical image segmentation have improved both local feature representation and volumetric context modeling. However, existing methods still strug- gle to efficiently model cross-slice relations in anisotropic volumet- ric images, limiting segmentation consistency and accuracy. This pa- per proposes G^2RA-Net, a medical image segmentation framework that combines graph-based cross-slice relation modeling with atten- tion gating. Graph-Based Slice Relationship Modeling (GSRM) cap- tures anatomical dependencies across consecutive slices by repre- senting each slice as a graph node and propagating semantic con- text through graph message passing. The Cross-Slice Attention Gate (CSAG) then selects relevant neighboring context and emphasizes target anatomical regions through attention-guided feature modula- tion. Experiments on brain MRI and abdominal CT datasets demon- strate that G^2RA-Net outperforms representative methods in seg- mentation accuracy and boundary quality. Ablation studies further validate the proposed design.

---


### 126. [Solving Minimum Span Antibandwidth and Cyclic Antibandwidth Labeling Problems](https://arxiv.org/abs/2609.20091)

**<font color=#1a73e8>作者：</font>** Hieu Truong Xuan, Khanh To Van  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Antibandwidth and Cyclic Antibandwidth problems are NP-hard graph labeling problems that aim to maximize the minimum (cyclic) distance between labels assigned to adjacent vertices. Extensive research on these problems has resulted in a variety of mathematical formulations and computational approaches. However, their minimum span perspective, in which a prescribed minimum (cyclic) distance is fixed and the objective is to minimize the label span, has received comparatively little attention. In this paper, we consider this complementary perspective by introducing the Minimum Span Antibandwidth/Cyclic Antibandwidth Labeling (MSABL/MSCABL) problems and developing a unified Boolean Satisfiability (SAT)-based framework for solving them. The SAT-based framework formulates MSABL/MSCABL as a sequence of decision problems and exploits their monotonicity to accelerate the search process. We also consider two SAT solving strategies, parallel and incremental SAT solving: the former examines multiple candidate spans concurrently, while the latter reuses a single SAT instance while progressively restricting the label domain. The proposed approaches are evaluated on benchmark instances from the Harwell-Boeing Sparse Matrix Collection and compared with CPLEXCP, CPLEXMIP, and Gurobi. The results show that SAT-based approaches are highly competitive in solution quality, with the parallel approach performing best overall for MSCABL and the incremental approach for MSABL. With the no-hole constraint, they remain competitive with CPLEXCP and significantly outperform CPLEXMIP and Gurobi, particularly for MSCABL. These results demonstrate the effectiveness of SAT solving as an exact approach for MSABL and MSCABL.

---


### 127. [A Scalable Trust Discovery Architecture for the Internet of Agents](https://arxiv.org/abs/2609.20095)

**<font color=#1a73e8>作者：</font>** Song Zhang, Jiankang Yao, Hongtao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Internet of Agents is expected to enable large numbers of autonomous agents to discover, verify, and collaborate with each other across heterogeneous platforms. However, current agent protocols mainly address tool invocation and inter-agent communication, leaving scalable agent registration, trustworthy identification, and capability-oriented discovery largely unresolved. To address this, this paper proposes a scalable trust discovery architecture for the Internet of Agents. The proposed architecture adopts a hierarchical and distributed design consisting of three layers: Agent Root for trusted registry governance, Agent Registry for agent registration and metadata publication, and Agent Resolver for distributed capability discovery and trust-aware resolution. The architecture further introduces a registry-suffix-anchored composite identity scheme, which binds an agent native identifier to a trusted registry suffix to generate a globally discoverable identity. It also incorporates a dual-certificate and multi-level authentication mechanism to strengthen identity trust among agents. We implement a prototype and evaluate it through large-scale agent registration and resolution experiments. The prototype achieves an average registration latency of 58ms and an average discovery latency of 25ms, and it supports more than 19,000 registration requests per second and more than 29,000 agent discovery requests per second. These results demonstrate the feasibility of the proposed architecture, providing a practical approach toward scalable and identity-trusted agent ecosystems in the Internet of Agents.

---


### 128. [CARE-VI: Conservative Adaptive Reliability Estimation for Value Improvement in Off-Policy Actor-Critic Learning](https://arxiv.org/abs/2609.20098)

**<font color=#1a73e8>作者：</font>** Xiang Zou, Shengzhu Shi, Junqi Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable temporal-difference targets are central to off-policy actor-critic learning. Direct value improvement refines the next-state target with alternative actions, but the reliability of this refinement depends on how candidate actions are ranked, reviewed, and weighted. Noisy rankings may force premature candidate commitment, reusing selection scores may bias target valuation, and fixed enhancement weights may amplify weak evidence. To address these risks, we develop Conservative Adaptive Ranking and Screening (CARS), which retains an ordered candidate prefix within a preset budget and narrows it only when the observed boundary gap exceeds a disagreement-scaled uncertainty radius. Selector-Evaluator Value Assessment (SEVA) uses selector critics to order candidates and a separately parameterized evaluator critic to review the selected value, then caps the reviewed value at the selector reference. Dynamic Adaptive Risk-aware Enhancement (DARE) then regulates each residual correction using candidate reliability, the gap between selector and evaluator signals, and a finite stage factor. Together, CARS, SEVA, and DARE form CARE-VI, an evidence-regulated target construction framework that preserves the backbone interfaces for critic regression and actor updates. The analysis bounds the CARS boundary error, the SEVA selected-value overestimation, and the one-sided deviation of the DARE residual displacement from its population counterpart, and establishes fixed-policy recovery after the finite-stage perturbation ends. Experiments with SAC, TD3, and TD7 on four MuJoCo tasks show that CARE-VI achieves the highest mean return in all twelve settings. Grouped ablations and scalar diagnostics support the roles of the three components in improving target reliability.

---


### 129. [A Smaller Transformer in Your Transformer](https://arxiv.org/abs/2609.20100)

**<font color=#1a73e8>作者：</font>** Dhananjay Tomar, Marius Aasan, Andreas Kleppe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent findings indicate that Vision Transformers settle into locally similar computational phases, implying a level of depthwise computational redundancy. However, existing methods to exploit this redundancy either fail to reduce inference compute or severely degrade model expressivity. In this work, we formalise a unified view of block redundancy that decouples the geometry from specific surrogate interventions. We then introduce Transformer-Within-Transformer (TWT), a post-hoc method that fuses contiguous groups of redundant layers into a single learned surrogate layer. TWT reduces parameter count and inference compute while remaining competitive with original models using half the depth on natural images, and in several downstream histopathology settings, TWT matches or even improves on the original baseline.

---


### 130. [Design of the IBM Granite 5.0 TurboCTC ASR Model](https://arxiv.org/abs/2609.20104)

**<font color=#1a73e8>作者：</font>** Brian Kingsbury, George Saon, Masayuki Suzuki 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe the architecture, training methodology and inference speedups of Granite 5.0 Turbo CTC, a 470 million parameter encoder-only model with an excellent speed-accuracy tradeoff. The architecture uses pyramidal temporal subsampling within Conformer blocks using strided depthwise convolutions, block-diagonal (chunk-wise) self-attention, and conditioning on intermediate predictions from the middle layer. Training highlights are the use of only publicly available data, the novel use of a Muon optimizer, and balanced data sampling. Inference speedups include replacing 1 x 1 convolutions with linear layers and optimizing the attention computation in the Conformer blocks. Collectively, these result in a model that is on the speed-accuracy Pareto frontier of the Open ASR leaderboard for English short-form ASR while being twice as fast as the fastest competitor. The model can be used under a permissive license and downloaded from this https URL.

---


### 131. [AnyviewMeter: Adapting Robotic Reward Models with Camera Geometry and Multi-View Attention](https://arxiv.org/abs/2609.20106)

**<font color=#1a73e8>作者：</font>** Yuang Tu, Runjia Tan, Yujie Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic reward models evaluate task execution from visual observations, but their predictions can change with camera viewpoint and occlusion even when the underlying task state is unchanged. Adapting a pretrained reward model to a local task therefore requires accounting for how that task is observed. We introduce AnyviewMeter, a geometry-conditioned adaptation framework for robotic reward models that represent task progress as a scalar reward signal. It combines low-rank fine-tuning with token-aligned Plucker rays and synchronous block attention: ray conditioning incorporates camera geometry into visual features and attention queries and keys, while block attention fuses synchronized views inside the pretrained decoder. The framework supports both single-view reward prediction and joint multi-view evaluation through parameter-efficient adaptation of a pretrained Robometer model. On PickCube, single-view adaptation improves progress prediction in every camera group and reduces mean absolute error under a changed field of view by approximately 21% relative to RGB fine-tuning. Across simulated manipulation tasks, joint multi-view prediction reduces progress error by 41-69% compared with averaging single-view RGB predictions and improves temporal ordering in approximately 88% of task-camera groups. On real tasks with fixed and wrist-mounted cameras, mean absolute error decreases by approximately 21% relative to averaged RGB fine-tuning. These results support camera geometry and joint visual evidence as useful components of task-specific robotic reward adaptation.

---


### 132. [QoS-Aware Federated Learning for Multimodal In-Cabin Interaction in Smart Vehicles](https://arxiv.org/abs/2609.20123)

**<font color=#1a73e8>作者：</font>** Baran Can Gül, Mert Nakıp, Nasser Jazdi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern smart vehicles leverage multimodal sensors, ranging from high-bandwidth vision systems to low-rate physiological monitors, to provide personalized in-cabin services. However, integrating high-fidelity multimodal fusion with collaborative training is often hindered by the heterogeneous and time-varying Quality of Service (QoS) constraints of vehicular networks. Standard Federated Learning (FL) approaches enforce rigid synchronous rounds that fail to account for these resource asymmetries, leading to safety-critical timing violations and energy exhaustion. In this paper, we propose FedQoS, a novel asynchronous, event-triggered FL framework that decouples local computation from global communication via a two-phase gating mechanism. First, we introduce a resource-aware training gate that initializes local learning only when sensing buffers and energy reserves meet safety thresholds, preventing ML tasks from compromising core vehicle mobility. Second, a QoS-aware transmission policy gates uplink updates based on an efficiency score that balances model novelty against instantaneous latency and energy costs. Locally, clients optimize an objective featuring a staleness-aware proximal term that dynamically adjusts the global anchor strength based on update age. Extensive experiments on multimodal vehicular datasets demonstrate that FedQoS achieves competitive personalized accuracy with only marginal performance loss compared to FedAvg, while substantially reducing QoS violations, cutting communication overhead by 76.7\%, and lowering latency cost by 26.0\%, demonstrating a highly favorable accuracy and efficiency balance for real-world vehicular deployments.

---


### 133. [Fast-varying Natural Frequencies and Damping Ratio Identification for Linear Time-Varying System](https://arxiv.org/abs/2609.20138)

**<font color=#1a73e8>作者：</font>** Melisa Bozaci, Alice Cicirello  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work proposes a physics-enhanced machine learning approach for the system identification of Linear Time-Varying (LTV) systems under time-varying operating conditions in terms of fast-varying natural frequencies and damping ratios by combining a long short-term memory network with an Extended Kalman Filter (EKF). The proposed approach uses vibration data (displacement and velocity measurements), domain knowledge of modal damping ratios, and a physics-based model that can yield an approximate natural frequencies time-dependency model. The approach is validated using synthetic data generated from a finite element model of a 2-blade offshore wind turbine under realistic environmental and operating conditions. This system displays fast time-varying frequencies due to operating conditions, whose identification is particularly challenging because of the wind and wave loading. The robustness of the proposed approach is assessed under assumed incorrect system information (e.g. damping ratio). The proposed approach is evaluated across different environmental and operating conditions to show its applicability to different operating regimes. The results show the approach can accurately identify the selected fast-varying natural frequency, 1st Fore-Aft (FA-1) mode, with a maximum root mean square error of 0.0012 Hz. The results demonstrate that the model trained on EKF estimates depends on accurate damping values, whereas the model trained on physics-based data exhibits robustness to incorrect damping assumptions. The approach is extended to damping ratio identification for the selected mode by estimating the root mean square error between models trained on EKF estimates and physics-based data. The results show that the approach can yield a good approximation of the FA-1 mode damping ratio using grid search, offering an improvement over covariance-driven stochastic subspace identification.

---


### 134. [Bridging Modalities on the Cortex: Surface-based MRI to PET Translation with a Diffusion Bridge](https://arxiv.org/abs/2609.20147)

**<font color=#1a73e8>作者：</font>** Yitong Li, Alexandra Samoylova, Fabian Bongratz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cortical hypometabolism measured by Fluorodeoxyglucose Positron Emission Tomography (FDG-PET) is a highly sensitive biomarker for dementia diagnosis. However, high costs, radiation exposure, and limited accessibility constrain its clinical utility. While cross-modal synthesis from Magnetic Resonance Imaging (MRI) offers a promising alternative, existing volumetric generation methods do not explicitly account for the highly folded cortical geometry, where disease-related patterns predominantly reside. To address this, we introduce a novel surface-based diffusion bridge framework DB-SUiT for MRI-to-PET translation that operates natively on the cortical manifold. A conditional Spherical U-shaped vision Transformer (SUiT) is specifically designed to model the intricate cross-modal relationships while preserving surface topology. It combines spherical convolutional encoders for multi-scale surface feature extraction with bottleneck Transformers to capture long-range spatial dependencies, while incorporating demographic and subcortical conditions to refine the synthesis. Evaluated on two datasets, including subjects with different dementia types, DB-SUiT demonstrates high-fidelity synthesis that substantially outperforms other baselines. In automated dementia classification, synthesized PET surfaces improve performance over MRI by 14.2% and PET volumes by 11.3%, approaching the performance of real PET surfaces. In a blinded reader study, synthetic PET achieved 85.5% diagnostic accuracy, compared with 75.8% for MRI and 95.2% for real PET. This further demonstrates cross-cohort and cross-pathology generalization, as the model was evaluated without retraining on an external cohort that included a dementia subtype not represented during training. Our code is available at this https URL.

---


### 135. [Task-Oriented Semantic Feature Transmission for Multi-Task Satellite Remote Sensing over Low-SNR Channels](https://arxiv.org/abs/2609.20150)

**<font color=#1a73e8>作者：</font>** Shuoyuan Sun, Hongyu Wang, Mugen Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional satellite remote sensing transmission follows a reconstruct-then-infer paradigm that optimizes pixel-level fidelity, creating an objective mismatch with downstream tasks such as classification and detection, especially at low SNR. This paper investigates a task-oriented framework that bypasses image reconstruction and directly transmits semantic features extracted by a multitask-pretrained backbone. A lightweight channel adaptation module (CAM) compresses feature dimensionality for bandwidth reduction, and a feature restorer recovers task-relevant structure after channel corruption. With the backbone frozen, the CAM and task-specific downstream heads are jointly optimized with task and feature-level supervision under random-SNR training. Under the adopted AWGN setting, experiments on scene classification and object detection show consistent gains over reconstruction-oriented JSCC baselines across different SNR conditions, with the largest improvements in the low-SNR regime.

---


### 136. [Ischemic Stroke Segmentation and Net Water Uptake Quantification on Multicenter Non-Contrast CT Using Supervised Target-Domain Adaptation](https://arxiv.org/abs/2609.20151)

**<font color=#1a73e8>作者：</font>** Linus Britt, Maximilian Nielsen, Susan Klapproth 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objectives: Quantitative assessment of infarct hypodensity on non-contrast computed tomography (NCCT), including net water uptake (NWU), requires manual or semi-manual lesion delineation, often guided by CT perfusion or diffusion-weighted MRI, limiting clinical applicability. Automated segmentation on NCCT could enable efficient biomarker extraction such as NWU but remains challenging across heterogeneous multicenter data. This study aimed to develop and externally test a domain-aware deep learning framework for ischemic stroke segmentation on NCCT and assess its suitability for NWU quantification.
Materials & Methods: In this retrospective multicenter study of 801 patients from four datasets, an nnU-Net-based model was trained on NCCT scans from the University Medical Center Hamburg-Eppendorf and the Acute Ischemic Stroke Dataset. To adapt to new domains, the model was fine-tuned on target-domain subsets from Boston (n=11) and ISLES (n=75), with evaluation on held-out cases not used for fine-tuning. Automated segmentations and NWU values were compared with expert references.
Results: For lesions $\geq$ 30 mL, median Dice was 0.68 (Boston) and 0.56 (ISLES). Including smaller lesions, which predominated in ISLES, median Dice was 0.54 (interquartile range [IQR] 0.30-0.70) for acute lesion segmentation (Boston dataset) and 0.20 (IQR 0.03-0.41) for NCCT lesion segmentations when compared to post-treatment infarct (primary target of the ISLES challenge). Automated NWU mean absolute error was 1.37 percentage points (SD 1.61, Boston).
Conclusion: Target-domain adaptation supported NCCT-only infarct segmentation across heterogeneous external cohorts, although performance varied across domains. The approach enabled low-error NWU quantification from baseline NCCT without advanced imaging, supporting further prospective clinical evaluation.

---


### 137. [QUALS: Corpus Equilibrium for Universal Forecasting via Pattern Quantization and Learnability Synchronization](https://arxiv.org/abs/2609.20156)

**<font color=#1a73e8>作者：</font>** Yujie Li, Zezhi Shao, Chengqing Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ubiquitous time series data across diverse domains enables critical applications in areas such as transportation systems and power grids. Recently, training foundation models on massive datasets to achieve accurate zero-shot forecasting has emerged as a major research focus. However, current studies predominantly prioritize architectural innovations while insufficiently addressing data diversity, often relying on simple data sampling strategies that fail to manage complex data distributions effectively, leading to inefficient use of training data and suboptimal performance. To address this, we propose QUALS, a large-scale time series corpus equilibrium framework. QUALS significantly enhances data efficiency, i.e., enabling existing models to achieve superior performance using only a small fraction of the original training data. Specifically, QUALS operates through two core mechanisms. First, a pattern quantization framework systematically decodes heterogeneous patterns from mixed corpora via vector quantization and uniform binning. Second, a learnability synchronization framework calibrates sampling weights for heterogeneous patterns, bridging the optimization gap between simple and complex motifs to maximize overall training efficiency. Extensive benchmarks demonstrate that pre-training on QUALS consistently achieves superior zero-shot performance, even under substantially reduced training budgets.

---


### 138. [Needles in a Raystack: Ultra-Sparse LiDAR Occupancy Detection for Bat Tracks](https://arxiv.org/abs/2609.20160)

**<font color=#1a73e8>作者：</font>** Nico Klar, Pankaj Rana, Nizam Gifary 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monitoring flying animals is important for understanding and protecting biodiversity, but nocturnal species such as bats are difficult to observe in the field. Using LiDAR, bat movements at night result in ultra-sparse 3D spatio-temporal data in which standard reconstruction losses tend to predict only background and miss real flight paths. We study this problem as voxel-wise occupancy detection in sensor-centric LiDAR raystacks. A lightweight 3D U-Net is proposed that preserves temporal resolution, uses skip connections for spatial detail, and combines weighted binary cross-entropy with Dice loss to handle the strong class imbalance.
In real LiDAR recordings of bats over open fields, cross-checked with acoustic monitoring, a reconstruction-based 3D convolutional autoencoder baseline fails to recover foreground trajectories. In contrast, the proposed U-Net recovers sparse foreground occupancy in diagnostic experiments and produces coherent occupancy patterns along bat flight trajectories, providing a practical basis for validation-scale experiments, later clustering of flight tracks, and future integration of bat activity information into biodiversity-aware turbine curtailment strategies.

---


### 139. [A Noise Optimum in Rehearsal-Free Continual Learning: Isolation, Mechanism, and Scope](https://arxiv.org/abs/2609.20162)

**<font color=#1a73e8>作者：</font>** Gunner Levi Howe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Injecting stochastic noise into a consolidation rule can improve a network's retention of earlier tasks up to an optimal level, then degrade it -- an inverted-U in retention vs. noise. This paper isolates what produces that optimum and maps where it holds, entirely in simulation. (1) Phenomenon: the retention inverted-U appears on several related-task continual-learning benchmarks (Split-MNIST, FashionMNIST, continual Yin-Yang). (2) Isolation: a magnitude-matched ladder shows the effect requires coherent restoring toward the consolidated weights -- a random-direction force of identical magnitude produces no optimum, and a coherent force toward the wrong target actively hurts. (3) Active ingredient: most of the optimum is recovered by coupling the anchor gain to the injected-noise variance sigma^2 -- a one-line rule that neither Ornstein-Uhlenbeck Adaptation (fixed gain) nor MESU (posterior-variance gain) implements. A forced Ornstein-Uhlenbeck calculation derives the rising flank and predicts that the optimal noise rises with per-task interference g -- confirmed out-of-sample in direction against pre-existing measurements (the exponent is unresolved at our grid). The barrier-conditioning of the originating Doob h-transform is a low-sigma safety net that bounds forgetting where the coupled gain is too weak. (4) Scope: the optimum requires shared task structure -- it is absent on permuted-MNIST, and a controlled rotated-vs-permuted comparison localizes the boundary to task structure; the precise governing quantity is left open. (5) Length: at matched severity the advantage persists but attenuates with task count, and we show no rotation family can attribute the trend (a compact-group identity). A single-seed BrainScaleS-2 demonstration of the originating rule is reported separately (Howe, arXiv:2607.06924); this paper makes no hardware claim.

---


### 140. [Small Enough to Know Everything: The Fully-Enumerable Transformer as an Instrument for the Science of Delayed Generalization](https://arxiv.org/abs/2609.20166)

**<font color=#1a73e8>作者：</font>** Yoshiyuki Ootani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tiny transformers trained on fully-enumerable tasks occupy an unusual position in the study of grokking: every input can be evaluated, every generalization ceiling can be computed exactly, and hundreds of seeds cost minutes. We argue this regime is a scientific instrument with four capabilities that approximate settings cannot offer: (a) exact, falsifiable generalization ceilings; (b) task surgery that manipulates one structural variable while provably fixing all others; (c) direct observation of every weight; and (d) survival-time statistics over many seeds that recast "does not grok" as a censored observation. The obvious objection is that laws characterized at 10^4 parameters may not mean anything beyond them. We answer it with a preregistered conservation study: three task-side laws established at 12K parameters -- a recoverability-ceiling law, a role-conflict delay law, and a weight-decay response law -- are re-measured under an identical from-scratch protocol at 12K, 1M, and 50M parameters (a 4,000x span; 360 runs plus a 44-run control arm). The ceiling law and the delay law are conserved (0/144 Holm-corrected ceiling violations; Spearman rho >= 0.75 at every scale, permutation p < 1e-4), while the weight-decay law deforms systematically, steepening with scale. Preregistered controls show the 50M role-conflict deficit survives learning-rate adjustment and a tripled budget. Conservation was tested against criteria frozen before data collection, and one law's deformation shows the test could have failed. These results license the fully-enumerable transformer as a model organism for the task-side laws of delayed generalization: what it measures exactly, larger models largely obey -- and where they deviate, the deviation is itself lawful and measurable.

---


### 141. [Support Thresholds, Not Algorithms, Limit Rare-Association Recovery in Co-Purchase Networks](https://arxiv.org/abs/2609.20171)

**<font color=#1a73e8>作者：</font>** Xiao Han, Zhen Zhang, Xin Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The support threshold of the Apriori algorithm involves a trade-off in conducting market basket analysis: the associations that occur frequently are noted with high threshold; however, the low ones lead to generating the large amount of rules. The paper compares five methods for co-purchase edge filtration on two grocery datasets: i.e., Instacart (3.2 million baskets) and Dunnhumby (208 thousand baskets), including Apriori, Apriori + lift post-filtering, top-$K$ ranking based on lift, and two methods based on networks, noise-corrected (NC) and disparity filter (DF). The top-$K$ method ensures the maximum average lift, while the NC achieves similar lift level by means of a single value of the significance parameter ($\alpha$). These two methods recover substantially more rare high-lift associations than Apriori (80-100% against 22-28%). NC and top-$K$ select meaningfully different edges (18-29% non-overlapping): NC retains statistically validated pairs, while top-$K$ retains rare pairs with high lift but low statistical significance. A rolling-origin holdout evaluation shows that top-$K$ edges recur at higher rates at every split, but NC edges are ~12 pp more likely to remain statistically significant in the held-out network.

---


### 142. [Robust Federated Q-Learning with Almost No Communication](https://arxiv.org/abs/2609.20174)

**<font color=#1a73e8>作者：</font>** Sreejeet Maity, Aritra Mitra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider a federated reinforcement learning setting involving $M$ agents, all of whom interact with a common Markov Decision Process (MDP). The agents exchange information via a central server to learn the optimal value function. Our goal is to understand to what extent one can hope for collaborative sample-complexity speedups in such a setting, when a small fraction of the agents are adversarial and can act arbitrarily. To that end, we propose Robust Fed-Q}, a federated Q-learning algorithm that blends ideas from both model-based and model-free RL, along with the median-of-means device from robust statistics. We prove that despite corruption, with high-probability, Robust Fed-Q (i) guarantees exact convergence to the optimal value function in the limit of infinite samples, and (ii) enjoys near-optimal finite-time rates that benefit from collaboration. In addition, our approach requires just $\tilde{O}(1)$ rounds of communication to achieve each of the above guarantees, a feature of independent interest in FL where communication is the major bottleneck.

---


### 143. [PaGNet: A Panel-Aware GBDT--Neural Network for Multi-Target Corporate Tax Avoidance Proxy Forecasting](https://arxiv.org/abs/2609.20177)

**<font color=#1a73e8>作者：</font>** Wonho Song, Hyungjoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting corporate tax avoidance proxies from firm--year panel data is challenging because predictive signals are distributed across short firm histories and related targets, while screening-oriented use requires transparent model behavior. We propose PaGNet (Panel-Aware GBDT--Neural Network), a two-branch hybrid that combines a LightGBM branch using panel-temporal summaries with a Panel-MLP branch using attention-pooled temporal aggregation and shared-trunk multi-task learning. A per-target validation-optimal blender produces both the final prediction and a compact branch-reliance diagnostic without trainable fusion parameters. On the KoTaP panel of 1{,}754 Korean listed firms from 2011--2024, PaGNet is evaluated under a leakage-free, shared-hyperparameter protocol across four feature regimes. In the direct-proxy-lag-excluded FS1 regime and the tax-history-augmented FS2 regime, accrual targets (TSTA, TSDA) route stably to the LightGBM branch, where PaGNet raises explained variance over the strongest of six baselines by roughly $0.08$--$0.11$ on the primary split. GETR often leans toward the neural branch, while CETR exposes a validation--test branch-selection mismatch rather than a stable branch assignment. A panel-flatten control shows that most accrual gains come from observed multi-year base-panel values, with PaGNet's panel-aware representation adding a smaller but directionally consistent refinement. Rolling-origin analysis confirms stable accrual routing, bounds ETR diagnostics to split-specific behavior, and identifies a far-horizon split where supervised models underperform naive persistence. PaGNet is therefore best viewed not as a universally superior tabular learner, but as a proxy-aware panel model that combines competitive forecasting with explicit per-target branch-reliance reporting.

---


### 144. [MTF-Net: Multi-Modal Temporal Feature Fusion Network for Pedestrian Intention Prediction](https://arxiv.org/abs/2609.20178)

**<font color=#1a73e8>作者：</font>** Md Mahfuzur Rahman, Pengzhan Zhou, A. F. M. Abdun Noor 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately predicting pedestrian intentions is crucial for ensuring safe and proactive interaction between autonomous vehicles and pedestrians. However, existing approaches often depend on architectures that either model temporal dependencies within individual modalities or fuse modalities only at coarse semantic levels. To address these limitations, we propose MTF-Net, a novel Multi-Modal Temporal Feature Fusion Network that jointly models kinematic, appearance, and contextual cues for pedestrian intention prediction. MTF-Net integrates four complementary modalities-bounding-box dynamics, human pose keypoints, local context, and scene-level semantics within a recurrent fusion framework enhanced by gated linear units (GLUs). These GLU-based modules adaptively regulate cross-modal information flow, enabling interpretable and efficient feature interaction across temporal scales. Through three dedicated temporal encoding branches and an attention-guided fusion head, the proposed model robustly anticipates pedestrian crossing intentions several frames before they occur. Extensive evaluations on the PIE and JAAD benchmarks demonstrate that MTF-Net surpasses recent transformer- and graph-based models, achieving up to 0.95 AUC on PIE and 0.94 AUC on JAAD, while maintaining real-time performance. The results highlight that reliable pedestrian intention prediction arises from principled multi-modal fusion rather than excessive architectural complexity.

---


### 145. [Sequential Contextual Fit Predicts Human Behavioural and Neural Dynamics Across Domains](https://arxiv.org/abs/2609.20179)

**<font color=#1a73e8>作者：</font>** Kun Sun, Rong Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human perception, action and decision making unfold in sequences, but computational predictors are often domain-specific. This study computes and tests sequential contextual fit (SCF), an embedding-based measure of how well a current information state matches its recent context. The metric uses a simple recency-weighted similarity kernel and can be applied to words, sounds, visual scenes, affective states, choices, actions and neural representations. Across language processing, music-evoked emotion, a subset of audiovisual emotion EEG data, gambling decisions, human activity recognition and decision-related EEG, lower contextual fit predicted longer processing times, larger affective or behavioural transitions and stronger neural-state changes. These effects remained after controlling for established predictors including surprisal, reinforcement-learning prediction error, acoustic change, visual change and sensor change. SCF therefore provides a computational measurement layer for relating contextual compatibility to behavioural processing and cognitive/neural state-transition dynamics.

---


### 146. [MoSSGate: Memory-Modulated State-Space Gating for Skin Lesion Segmentation](https://arxiv.org/abs/2609.20181)

**<font color=#1a73e8>作者：</font>** Anum Awan, Mahnoor Buriro, Muhammad Younas Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate skin lesion segmentation is crucial for reliable computer-aided dermatological diagnosis, yet existing convolutional and transformer-based models often struggle to jointly capture long-range spatial dependencies and fine boundary details under limited computational budgets. This trade-off between global context modeling and boundary-aware localization frequently leads to over-segmentation, fragmented predictions, or missing thin peripheral structures. To address this challenge, we propose MoSSGate, a plug-and-play module for U-Net that integrates (i) boundary-aware spatial gating to restrict long-range propagation to informative regions, (ii) an external memory modulator that provides sample-adaptive dynamic control, and (iii) parallel 2D state-space modeling for efficient global context aggregation with linear complexity. The proposed design enables adaptive, context-aware information propagation while preserving sharp and accurate lesion boundaries. Extensive experiments on the ISIC 2017 and ISIC 2018 benchmarks demonstrate state-of-the-art accuracy with strong efficiency, achieving 86.3% and 85.9% mIoU and 92.6% and 90.6% Dice, respectively, while requiring substantially fewer FLOPs than most competing CNN-based methods. These results highlight a favorable accuracy efficiency trade-off for high-resolution medical image segmentation.

---


### 147. [When Does Retrieval Help Time-Series Forecasting?](https://arxiv.org/abs/2609.20193)

**<font color=#1a73e8>作者：</font>** Mert Onur Cakiroglu, Elham Buxton, Mehmet Dalkilic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval plug-ins supply a deep forecaster with information its lookback window cannot carry. Published evaluations report consistent gains, and each credits its own mechanism. We show that the benefit belongs instead to the operating point: the relation between window length $S$ and dominant seasonal period $L$, an axis the standard protocol never varies. Stratifying the evaluation by that relation exposes the regime. At $S{=}12$, a simple control that repeats the last observed period beats the six standard backbones, in aggregate, on four of seven benchmarks by $8\%$ to $44\%$ of MSE. It beats the strongest plug-in we run on ETTm1 and matches it on ECL. It is worse by up to $25\%$ on the three datasets whose training-split spectra lack a concentrated, shared period. A controlled synthetic sweep of horizon, period, and window shows the benefit boundary tracks the period (correlation $+0.71$), not the horizon ($-0.23$). A paired control with no phase to recover nearly erases the effect, consistent with phase starvation. Zero-shot pretraining does not escape it: a foundation model trails trained backbones by $22\%$ to $50\%$ on the periodic benchmarks. Within our instrument, exact lookup matches graph diffusion: the payoff is consulting the record, not the machinery on top. Two interpretable statistics, a trend test and a staleness rate, predict the sign of the per-cell benefit at $0.76$ accuracy under leave-one-dataset-out evaluation, a suggestive margin over the $0.69$ majority rule, where a 22-feature stack manages $0.57$. We propose no new plug-in. The contribution is the regime map, the protocol that reveals it, and two statistics that screen it before deployment. Code: this https URL.

---


### 148. [SoftTri: Smooth Triangular Membership Functions for Adaptive Fuzzy Inference Systems](https://arxiv.org/abs/2609.20194)

**<font color=#1a73e8>作者：</font>** Babak Sarani, Rahman Ardakanian, Ali Mousavi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Triangular membership functions (MFs) are widely used in fuzzy systems because of their interpretability, low parameterization complexity, and strong locality properties. However, their inherent nondifferentiability at knot points limits the effectiveness of gradient-based optimization in adaptive neuro-fuzzy architectures, often necessitating subgradient approximations or heuristic smoothing techniques. In this paper, we propose \emph{SoftTri}, a differentiable triangular membership function constructed using a smooth soft-hinge mechanism inspired by Swish-type activations. The proposed formulation preserves the geometric structure and localized behavior of classical triangular MFs while providing $C^\infty$ smoothness with respect to both the input variable and the membership parameters $(a,b,c)$ for any finite sharpness parameter $\beta>0$. Closed-form analytical gradients are derived to enable efficient and fully differentiable backpropagation-based learning. SoftTri is integrated into a Takagi--Sugeno fuzzy neural network with grid-partitioned rules and evaluated on multiple one-dimensional and two-dimensional nonlinear approximation benchmarks as well as a real-world regression task using the Airfoil Self-Noise dataset. Experimental results demonstrate that SoftTri consistently improves optimization stability and approximation accuracy compared with classical triangular membership functions, while achieving performance comparable to or better than Gaussian MFs under identical rule structures and training settings. The proposed approach provides an effective compromise between interpretability and differentiable optimization in modern neuro-fuzzy learning systems.

---


### 149. [Towards a Unified Modality-Agnostic Multimodal Framework for Cognitive Workload Assessment](https://arxiv.org/abs/2609.20199)

**<font color=#1a73e8>作者：</font>** Stefanos Gkikas, Christian Arzate Cruz, Calvin Joseph 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cognitive workload reflects the mental effort required during task performance and is central to the design of adaptive human-machine systems. The use of biosignals to measure cognitive workload has been extensively researched and documented; however, studies examining the effects of combining heterogeneous biosignal modalities for this purpose remain limited. To provide insight into this area, we developed a unified, modality-agnostic, hierarchical Transformer-based architecture to process heterogeneous biosignal modalities within a single model. We use this framework in a pilot study evaluating all $31$ possible combinations of five modalities: Electrocardiogram (ECG), Electrodermal Activity (EDA), Respiration (RESP), Peripheral Oxygen Saturation (SpO$_2$), and Electroencephalogram (EEG), under leave-one-subject-out validation across three cognitively distinct tasks: abstract reasoning (IQ), arithmetic problem solving (MATH), and a game task (GAME). In this pilot setting, the results suggest that: (i) EEG is the strongest single modality, ranking highest in IQ, GAME, and the pooled ALL setting, where samples from all three tasks are combined; (ii) adding more modalities does not consistently improve performance; (iii) the full five-modality combination achieves the highest \textit{Average} score of $73.02%$ on IQ and $68.08%$ when the \textit{Average} scores are averaged over the four evaluation settings: IQ, MATH, GAME, and ALL; and (iv) the proposed method reduces model size by approximately $50%$ compared with late-fusion alternatives while maintaining a lower inference time.

---


### 150. [JointMatch: A Unified Heterogeneous Graph Neural Solver for Large-Scale Ride-Sharing Matching](https://arxiv.org/abs/2609.20200)

**<font color=#1a73e8>作者：</font>** Kun Zhao, Xu Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ride-sharing platforms must continuously decide which open requests to bundle into shared trips and which idle vehicles should serve them. The dominant academic approach decomposes this into two sequential matching problems -- request pairing first, then vehicle assignment -- and applies a separate solver to each. This decomposition is convenient computationally but loses revenue and scales poorly because the first stage commits to ride bundles before the available vehicles are known. We propose JointMatch, a learning-based framework that handles request pairing and vehicle assignment together on a single graph. The graph is sparsified by spatial proximity so that its size grows linearly rather than quadratically with the number of vehicles and requests, and a graph neural network scores all candidate decisions in one forward pass. On the New York City Yellow Taxi data, the framework already exceeds both the classical Blossom heuristic and a faithfully-trained two-stage GNN baseline -- often by a wide margin -- and at city scale (fleet 10000) it runs more than $20\times$ faster per dispatch epoch than either. A supervised training stage closes most of the remaining revenue gap, and a policy-gradient fine-tune aligns the trained model with realised revenue.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-247](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
