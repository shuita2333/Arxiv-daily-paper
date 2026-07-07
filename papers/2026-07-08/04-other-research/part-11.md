# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-550**（第 11/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-571](./part-12.md)

---

### 501. [Toward Personalized Social Robots for Child Well-being: Data Requirement Principles from a Recommender-System Perspective](https://arxiv.org/abs/2607.05110)

**<font color=#1a73e8>作者：</font>** Jin Huang, Eric Nichols, Fethiye Irmak Dogan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social robots are increasingly deployed in clinical settings to support the well-being of children, where effective support must be personalized to each child. Personalization, choosing the robot action best suited to each child, can be framed as a recommendation problem, and a recently proposed recommender-system framework for social robots offers a principled approach through user profiling, ranking, and responsible computing. Instantiating it, however, is blocked not by the model but by the data, which is hard to gather. A child's state shifts within and across visits, so no fixed description of the user holds. Within a session, the few signals of whether the robot's actions helped are weak and indirect. Across sessions, children are rarely seen more than once, and anonymization breaks the identity needed to link visits. Because care cannot be randomized, existing data is observational, biased toward whatever was already done. Each is a familiar recommender-system problem, and we propose four data principles in response: an integrated profile, effectiveness signals, linkable coverage, and an exposure record logged at collection time. We identify which of these principles each capability requires, and frame them as concrete guidelines for data collection.

---


### 502. [From Multiplicity to Vulnerability: Privacy Amplification Risk from One-Dataset-Multiple-Model Exposure](https://arxiv.org/abs/2607.05111)

**<font color=#1a73e8>作者：</font>** Qirui Huang, Na Li, Hongsheng Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> To efficiently exploit a valuable data source (e.g., facial or medical images), it is frequently harnessed to fulfill multiple learning objectives (e.g., facial recognition, age estimation, and race classification). Each trained model is then deployed as an independent API service for corresponding inference. However, the privacy risk introduced by this one-dataset-multiple-model (ODMM) paradigm is completely overlooked by the community.
For the first time, this work reveals that the ODMM setting substantially amplifies privacy leakage. We establish a theoretical framework that proves that privacy leakage accumulates as more ODMM models are exposed, a phenomenon we term ODMM privacy composition. Guided by this theoretical foundation, we propose PRIME (Privacy Amplification RIsk from One-Dataset-Multiple-Model Exposure) to systematically assess this risk and quantify the resulting leakage using membership inference attacks (MIAs). Under black-box access to ODMM models, we design an aggregation mechanism that collectively captures carefully identified privacy signals leaked by individual ODMM models, and construct an attack meta-classifier over the aggregated meta-information to infer the membership status of a given sample jointly. Our results provide strong evidence that dataset reuse across ODMM models strikingly jeopardizes privacy, which is consistently evident across five privacy-sensitive image and textual benchmark datasets and diverse model architectures (from ResNet and ViT to Qwen3-1.7B), spanning three domains: facial analysis, medical imaging, and textual attribution analysis. While mitigations such as differential privacy can reduce the effectiveness of PRIME with trade-offs, our attack still consistently outperforms single-task MIAs.

---


### 503. [Agent Data Injection Attacks are Realistic Threats to AI Agents](https://arxiv.org/abs/2607.05120)

**<font color=#1a73e8>作者：</font>** Woohyuk Choi, Juhee Kim, Taehyun Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents act on behalf of user prompts, consuming external data and taking actions based on the agent context. Prior research on AI agent security has primarily focused on indirect prompt injection (IPI). Its most well-studied category is instruction injection, where attacker-controlled untrusted data is interpreted as an instruction. In response, many mitigations have been proposed to prevent instruction injection attacks. In this paper, we introduce a new category of IPI, agent data injection attacks (ADI). ADI injects malicious data disguised as trusted data, such as security-critical metadata (e.g., resource identifiers or data origins) or agent context data (e.g., tool call and response formats). As a result, agents unknowingly execute unintended actions based on attacker-controlled data. ADI has similar attack impacts as instruction injection attacks, because it causes agents to misbehave and execute unintended actions. Despite the similar impact, ADI remains underexplored and easily bypasses existing IPI defenses. We found several critical vulnerabilities in real-world agents that allow an attacker to launch various attacks: arbitrary click attacks on web agents (Claude in Chrome, Antigravity, and Nanobrowser), and remote code execution and supply-chain attacks on coding agents (Claude Code, Codex, and Gemini CLI). We evaluate ADI vulnerabilities across off-the-shelf models and AI agents, and find that ADI is effective in both standalone LLMs and AI agent settings. ADI exposes a critical gap in agent security, signifying that current AI agents do not employ a fundamental security principle: current agents do not isolate trusted data from untrusted data.

---


### 504. [Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies](https://arxiv.org/abs/2607.05122)

**<font color=#1a73e8>作者：</font>** Adrian Szvoren, Dimitrios Kanoulas, Nilufer Tuptuk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.

---


### 505. [ASSEMCAD: Production-Ready CAD Assembly Generation from Natural Language](https://arxiv.org/abs/2607.05123)

**<font color=#1a73e8>作者：</font>** Yurui Dong, Shu Zou, Siqi Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models and programmatic CAD have significantly improved Text-to-CAD generation for individual parts. However, production-ready mechanical assembly generation remains largely unsolved. Unlike single-part modeling, assemblies require coordinated reasoning over multiple components, functional interfaces, assembly relations, engineering principles, and physical consistency. Consequently, directly generating executable CAD code is insufficient for constructing mechanically valid and reusable assemblies. We present AssemCAD, an axiom-grounded framework for production-ready CAD assembly generation from natural language. Instead of representing an assembly as monolithic CAD code, AssemCAD first constructs an axiomatic Assembly Specification consisting of typed parts, geometry-backed ports, executable mates, and engineering axioms. Each assembly relation is explicitly grounded in one or more engineering principles, making the resulting specification interpretable, reusable, and verifiable. To realize this specification, AssemCAD introduces a port- and mate-based CAD assembly library that executes symbolic assembly relations through deterministic mate transformations and validates declared interfaces using concrete B-Rep geometric evidence. Built on this representation and library, AssemCAD further supports on-demand synthesis of reusable parametric component factories for both standard and open-world geometries. Experiments on AssemBench show that AssemCAD substantially improves assembly preservation and physical validity over code-centric CAD generation baselines, while generalizing across different foundation-model backbones. By combining axiom-grounded assembly reasoning with deterministic geometric execution, AssemCAD extends Text-to-CAD from isolated part generation toward production-ready mechanical assembly design.

---


### 506. [TacReasoner: A Dynamic Tactile-Language Framework for Interactive Reasoning in Real-World Scenarios](https://arxiv.org/abs/2607.05131)

**<font color=#1a73e8>作者：</font>** Kailin Lyu, Di Wu, Long Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Among the five primary human senses, tactile is arguably the most fundamental to survival, as it enables the perception of physical contact and interaction in real-world environments. In this paper, we explore two key challenges of integrating tactile sensing into intelligent systems for multimodal reasoning: (i) insufficient modeling of dynamic tactile signals, which restricts reasoning over temporally evolving properties, and (ii) hallucination in tactile foundation models caused by the absence of explicit reasoning mechanisms, leading to unstable real-world inference. To address these challenges, we propose TacReasoner, a dynamic tactile-language framework for interactive reasoning in real-world scenarios. First, TacReasoner incorporates a Dynamic-aware Tactile Encoder to enhance the perception and representation of dynamic tactile signals. More importantly, we introduce TouchCoT-10k, the first tactile chain-of-thought dataset for structured reasoning over tactile inputs. Upon it, we establish DynTac-Bench to systematically evaluate dynamic tactile perception and real-world commonsense reasoning. Experimental results demonstrate that TacReasoner achieves competitive performance against state-of-the-art models across multiple datasets. Notably, despite using only 7B parameters, TacReasoner outperforms the 14B VTV-LLM model on most subtasks, highlighting its effectiveness and efficiency in tactile commonsense reasoning.

---


### 507. [UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation](https://arxiv.org/abs/2607.05133)

**<font color=#1a73e8>作者：</font>** Mengmeng Liu, Diankun Zhang, Jiuming Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) have shown strong potential for improving action generalization in autonomous driving by using future video prediction as dense supervision for scene dynamics and temporal causality. However, it remains unclear which architecture better transfers video-modeling benefits to trajectory generation. Existing cascaded or dual-DiT designs separate video imagination from action prediction, weakening the transfer of video-learned world dynamics to the trajectory branch: the action model may still overfit dataset-specific driving priors, while the video model only indirectly regularizes planning. We propose UNIVERSE, a unified video-action model built upon a single mask-modulated Diffusion Transformer. By co-training future video latents and ego-trajectory tokens within shared generative parameters, UNIVERSE allows dense video supervision to directly shape trajectory denoising, leading to stronger cross-domain action generalization. To ensure causal validity and efficient deployment, we introduce a Modality-Decoupling Visibility Mask, which shares historical context across modalities while blocking mutual attention between future video and trajectory tokens. This prevents future-target leakage and enables trajectory-only inference by removing future-video denoising at test time, achieving a $4.3\times$ speedup over joint video-action rollout while maintaining comparable planning accuracy. The same model also supports video-only and joint video-action rollouts. Experiments show that UNIVERSE achieves 91.0 PDMS on NAVSIM (vs. 89.6 for the Two-DiT variant), and demonstrates strong zero-shot transfer to nuScenes and Bench2Drive without fine-tuning, while ablations confirm the importance of single-DiT unification, video co-training, and mask-based modality decoupling.

---


### 508. [Fully Rotation-Equivariant Spectral-Spatial Learning for Multispectral Object Detection](https://arxiv.org/abs/2607.05148)

**<font color=#1a73e8>作者：</font>** Peng Zhang, Tingfa Xu, Shuaihao Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing multispectral detectors are limited by discrete spectral processing, a scale-dependent shift in the relative reliability of spectral and spatial cues across pyramid levels, and the lack of explicit rotation-equivariant geometric priors for arbitrarily oriented objects. To tackle these limitations, we propose FressDet, a fully rotation-equivariant spectral-spatial learning framework for multispectral object detection, capable of capturing the continuous, ordered nature of spectral structure and enabling reliable spectral-spatial fusion across pyramid levels under arbitrary in-plane rotations. FressDet integrates three complementary components. Spectral Implicit Warp (SpeIW) enables query-based spectral resampling via a coordinate-conditioned implicit field, yielding a monotone, order-preserving warp. Rotation-Equivariant Consistency Weighting (ReCoW) adaptively fuses spectral and spatial branches based on branch reliability, reinforcing informative cues while suppressing noise across pyramid levels. The oriented-aware head exploits group-indexed features to stably predict oriented objects without parameter replication. Taken together, FressDet learns more discriminative and robust spectral-spatial representations even under rotational perturbations. By achieving state-of-the-art performance with 93% fewer parameters on three public benchmarks, FressDet demonstrates its effectiveness and generalizability.

---


### 509. [Claim-Level Rubric Rewards for Video Caption Reinforcement Learning](https://arxiv.org/abs/2607.05150)

**<font color=#1a73e8>作者：</font>** Mingqi Gao, Hongyuan Dong, Yifei Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce Claim-Level Rubric Rewards (CuRe), a structured reward framework designed to address the reward-design bottleneck in reinforcement learning for dense video captioning. Existing reward designs generally fall into two categories: holistic response-level judgment across heterogeneous criteria, or alignment-based evaluation against reference captions. However, both paradigms suffer from fundamental limitations. Holistic rewards struggle to ensure factual accuracy and are prone to stylistic reward hacking, while reference-based rewards overly rely on rigid textual alignment, failing to preserve the completeness and diversity inherent to open-ended generation tasks. To address these challenges, CuRe reformulates reward modeling as fine-grained claim-level verification. Specifically, CuRe decomposes captions into category-aware atomic claims through a structured rubric, converting holistic evaluation into simpler and more reliable claim-level verification.

---


### 510. [EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments](https://arxiv.org/abs/2607.05155)

**<font color=#1a73e8>作者：</font>** Deyao Zhu, Xin Zhou, Shengling Qin 等 47 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretraining scaling laws reveal that model capability improves predictably with data and compute. But learning from real world environments after deployment remains far less understood. Analyzing roughly 38,000 hours of agent interaction with the environment across 134 real world tasks, we find, to the best of our knowledge, the first evidence that overall performance during environment learning follows a log-sigmoid scaling law with remarkably high precision, reaching R^2 = 0.998. Across model generations, we also find that agent learning speed roughly doubles every three months. This discovery stems from EdgeBench, a suite of 134 real world tasks with ultra-long horizons, spanning scientific discovery, software engineering, combinatorial optimization, professional knowledge work, formal mathematics, and interactive games. Each task sustains at least 12 hours of continuous agent operation under rich, multilevel feedback, and is built through substantial expert effort. We publicly release 51 tasks and our full evaluation framework to accelerate the study of how agents learn from real world experience.

---


### 511. [Physiological Noise Augmentation Improves Non-Invasive Brain-to-Speech](https://arxiv.org/abs/2607.05165)

**<font color=#1a73e8>作者：</font>** Benjamin Ballyk, Teyun Kwon, Miran Özdogan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-invasive brain-to-speech decoding aims to restore communication to patients suffering from neurodegenerative disease, without the risks of neurosurgery. Existing MEG- and EEG-based methods, while scalable, continue to suffer from high word error rates driven by relatively low signal-to-noise ratios compared to invasive recordings. We propose physiological noise augmentation (PNA), a data augmentation method that explicitly trains decoders to become invariant to task-agnostic artifacts (e.g. ocular and cardiac activity). PNA draws inspiration from automatic speech recognition systems, where environmental noise (e.g. dogs barking, city traffic) is added to clean speech to improve robustness. Analogously, we decompose brain recordings into clean data and noise artifacts using independent component analysis (ICA), before scaling and remixing to generate biophysically realistic, label-preserving training examples. We show that PNA approximates anisotropic regularization, penalizing decoder sensitivity along artifact-dominated directions. On MegNIST, a 12k-trial imagined-digit MEG dataset, PNA with 10-trial averaging improves EEGNet decoding accuracy by 4.7 percentage points (absolute) over training on real data alone. Our results suggest that artifact-aware augmentation and trial averaging are complementary tools for improving robustness in non-invasive speech BCIs.

---


### 512. [MeGA-MP: Metric Graph Advection Message Passing -- A Physics-Informed Message Passing Operator for Advection-Dominated Metric Graphs](https://arxiv.org/abs/2607.05167)

**<font color=#1a73e8>作者：</font>** Janine Strotherm, Luca Hermes, André Artelt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world systems are organized as networks where spatio-temporal dynamics unfold along connections and not discretely between nodes. Examples include utility networks such as water distribution systems or gas networks, electrical grids, and traffic flow networks. Such systems are naturally modeled as metric graphs, where edges correspond to one-dimensional Euclidean subspaces connected at vertices. Metric graphs are independent of an underlying global Euclidean space, limiting direct application of typical PINNs and operator-learning methods. Especially transport dynamics like advection require a methodology able to capture antisymmetric and long-range dependencies on graphs, which is itself a challenge. We propose a novel physics-informed message passing operator that encodes linear advection on metric graphs as an inductive bias. In the purely advective setting, the operator provably recovers the exact dynamics up to a theoretically derived discretization error without any training. Combined with trainable components like MLPs, our message passing operator extends to realistic advection-reaction dynamics in water distribution systems, where we achieve superior performance compared to baselines and zero-shot generalization across different graph topologies.

---


### 513. [The Changing Role of Symbolic Methods in Artificial Intelligence](https://arxiv.org/abs/2607.05168)

**<font color=#1a73e8>作者：</font>** Jun Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Why do intelligent systems need to perform explicit symbolic reasoning? Computer science has traditionally regarded symbolic reasoning as a defining component of intelligence. Yet the remarkable success of modern foundation models raises a fundamental question: if increasingly capable AI systems can operate with little explicit symbolic reasoning, what role do symbolic methods actually play?
This article argues that explicit symbolic reasoning is not a fundamental property of intelligence, but a computational consequence of operating on simplified models of reality. We propose the Compression Principle: every computational model is a simplified representation of reality, and explicit symbolic reasoning compensates for information omitted during model construction. From this principle, we derive the Modeling--Reasoning Trade-off: as computational models preserve richer representations of the world, the need for explicit symbolic reasoning correspondingly decreases. This perspective provides a unified explanation for both the historical success of symbolic methods and the remarkable effectiveness of modern foundation models.
Paradoxically, the same development makes symbolic methods increasingly important for humans. As intelligent systems become more capable and more opaque, symbolic representations increasingly serve as interfaces through which humans specify requirements, verify behavior, regulate autonomous systems, and establish trust. We therefore argue that the future of symbolic methods lies not primarily as the computational engine of intelligent systems, but as the symbolic interface between increasingly capable AI systems and the humans who build, govern, and depend upon them.

---


### 514. [Platonic Projection Structures: Operator-Induced Observability in Representation Learning](https://arxiv.org/abs/2607.05175)

**<font color=#1a73e8>作者：</font>** Kazuo Ishii, Bishnu Prasad Gautam, Jieling Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We characterize observability in representation learning through Platonic Projection Structures (PPS), an operator-theoretic framework for analyzing representation accessibility under partial observation. Rather than treating observable outputs as direct reflections of latent representations, PPS models observation through a self-adjoint positive semidefinite operator acting on a latent representation space. A system is represented as a triple $(H, \Pi, O)$, where $H$ is a latent representation space, $\Pi \succeq 0$ is an observation operator, and $O(v)=\langle v,\Pi v\rangle$ defines an induced scalar observable. Observability is characterized by the quotient geometry $H/\ker(\Pi)$, representing equivalence classes of latent states indistinguishable under observation. We show that quantum measurement and representation inference under linear observation models share this operator-theoretic structure while differing in the algebraic properties of their observation operators; the correspondence is structural rather than physical. Representation transfer and knowledge distillation can likewise be interpreted as approximate preservation of observable geometry through $\Phi \Pi_T \approx \Pi_S \Phi$. PPS also reveals a structural limitation of output-based interpretability: latent components in $\ker(\Pi)$ are inaccessible from induced observables, imposing intrinsic constraints on attribution and explanation methods. Controlled empirical validations demonstrate kernel-invariant observability, projection-induced attribution gaps, and rank-controlled observable geometry in latent representation spaces. PPS thus provides an explicit characterization of observability through operator-induced quotient geometry and a unified perspective on representation accessibility, interpretability, and projection-mediated inference.

---


### 515. [FSDC-DETR: A Frequency-Spatial Domain Collaborative DETR for Small Object Detection](https://arxiv.org/abs/2607.05176)

**<font color=#1a73e8>作者：</font>** Aiwen Liu, Chengguang Zhu, Gang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small object detection (SOD) remains a challenging task in real-world applications. Despite recent advances, existing detectors remain limited by rigid processing that entangle spatial aggregation with implicit frequency aliasing and truncation, leading to inadequate preservation of high-frequency components for SOD. To tackle these limitations, we propose a Frequency-Spatial Domain Collaborative Detection Transformer (FSDC-DETR), a novel collaborative framework that explicitly models complementary spatial and frequency representations. Specifically, we first introduce Dual-Branch Frequency-Spatial Adaptive Fusion (DBFSAF) to enhance frequency diversity and adaptively capture frequency-spatial domain discriminative representations. Building on these representations, a frequency-spatial interaction scheme is further explored within the hybrid encoder to enable progressive feature propagation to the decoder. In particular, structure-aware frequency-spatial aggregation is achieved through Shunt Frequency-Spatial Feature Fusion (SFS-FF), establishing bidirectional interaction and progressive cross-scale propagation between frequency and spatial representations for coherent discriminative modeling. Meanwhile, informative high-frequency responses are preserved during scale transitions through Frequency-Spatial Dynamic Downsampling (FSD-Down), thereby minimizing frequency degradation throughout multi-scale fusion for the precise SOD. Experimental results demonstrate that FSDC-DETR achieves state-of-the-art performance, improving AP by 6.4 on VisDrone-DET2019 and 6.6 on AITODv2, with gains of 6.8 and 6.9 AP for small objects. The code is available at this http URL.

---


### 516. [CP-WSP: A Declarative CP-SAT Framework for Configurable Multi-Constraint Workforce Scheduling](https://arxiv.org/abs/2607.05177)

**<font color=#1a73e8>作者：</font>** Vipul Patel, Anirudh Deodhar, Dagnachew Birru  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Workforce scheduling is an NP-hard combinatorial optimization problem requiring simultaneous satisfaction of labor regulations, coverage requirements, employee preferences and operational objectives. Existing CP formulations typically model simplified instances with 6-12 constraints at shift-level granularity and critically lack explicit support for: mandatory break scheduling with midpoint placement control; acuity weighted workload equity; sub-shift temporal granularity enabling demand-driven staffing; inter-week schedule stability; and cross-midnight shift patterns common in 24-hour operations. This paper presents CP-WSP: a declarative CP-SAT framework enforcing 14 hard constraints as mathematically inviolable requirements (zero regulatory violations by construction) while optimizing 15 soft objectives through a unified weighted penalty function -- all configurable via a JSON specification with no code changes required. Key contributions include: a shift-window variable decomposition enabling mandatory break scheduling with centrality control; acuity-weighted workload equity; multi-granularity temporal resolution from 30 minutes to 2 hours; inter-week schedule stability; a grid-offset preprocessing technique for cross-midnight shifts; and a reproducible 36-configuration benchmark suite for community comparison. Evaluated on INRC-II benchmarks at both hourly and shift-level granularity and on 36 synthetic configurations.

---


### 517. [Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed Railway Markets](https://arxiv.org/abs/2607.05179)

**<font color=#1a73e8>作者：</font>** Enrique Adrian Villarrubia-Martin, David Muñoz-Valero, Luis Rodriguez-Benitez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In liberalised railway systems, operators must set prices dynamically in an environment with partial observability, as they retain private information about their objectives and performance, where regulatory constraints prohibit communication or direct information exchange between competitors to prevent explicit collusion. Consequently, agents must learn to infer strategic interactions only from observable market data which presents a significant challenge for multi-agent reinforcement learning, where standard approaches typically treat observations as unstructured vectors, ignoring the underlying market topology that governs strategic interactions. To address this, an entity graph modelling approach is proposed, which represents the environment as a graph of operational units, rather than decision-making agents or static infrastructure, encoding competition, coordination, and connectivity relations between entities. Then, an extension of the multi-agent twin delayed deep deterministic policy gradient algorithm with graph-based representation learning processes the features of the entities through a multi-layer relational graph convolutional network and aggregates them via a learnt attention mechanism. Experimental results in a rail pricing reinforcement learning environment show that this novel framework achieves higher revenue and stability in two different settings of increasing market complexity compared to a representative selection of relational and non-relational baselines. The code is publicly available at: this https URL

---


### 518. [Rethinking On-Policy Self-Distillation for Thinking Models](https://arxiv.org/abs/2607.05184)

**<font color=#1a73e8>作者：</font>** Simran Kaur, Narutatsu Ri, Yinghui He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-distillation is a promising recipe for self-improvement in language models. In this setting, a model can serve as its own teacher when given privileged information, such as a solution to a math problem. This seems especially appealing for thinking models, which can use test-time reasoning to absorb the privileged information. Surprisingly, we show that privileged self-distillation degrades thinking models on long reasoning traces: across five Qwen3 and OLMo thinking models evaluated on AIME24, AIME25, and HMMT25, privileged-context distillation causes a relative drop of up to 17% in avg@16 accuracy. The degradation scales with the amount of privileged context withheld from the student and is most pronounced at long rollout budgets, where thinking models otherwise obtain their largest gains. This failure mode is not specific to self-distillation: on-policy distillation (OPD) improves thinking models, but privileged OPD reverses these gains. Our diagnostics link this failure mode to how privileged teacher context reshapes learning at high-entropy forking positions, where multiple continuations remain plausible and may lead to different reasoning paths. Privileged context lowers fork rates in thinking-model rollouts but not in instruction-model rollouts. This leads to an interesting dichotomy, where privileged context can help instruction-tuned models but hurts stronger thinking models. The effect is visible when the student begins a self-correction branch, where privileged OPD penalizes sampled reconsideration tokens that vanilla OPD supports. Thinking models trained with a privileged teacher produce fewer verification, backtracking, and hedging markers, even after length normalization. These findings indicate that self-distillation for strong thinking models requires attention to token-level signal, especially around correction and reasoning steps.

---


### 519. [ClassicLogic: A Knowledge-Driven Benchmark of Classic Puzzle Games for Evaluating Compositional Generalization](https://arxiv.org/abs/2607.05185)

**<font color=#1a73e8>作者：</font>** Mahnoor Shahid, Hannes Rothe  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compositional generalization, the ability to understand and produce novel combinations of known components, remains a fundamental challenge for modern artificial intelligence. While few benchmarks exist, many focus on linguistic tasks and lack complex, explicit compositional structures. We introduce ClassicLogic, a new benchmark suite designed to evaluate an agent's ability to learn and compose problem-solving strategies. The benchmark consists of four classic logic puzzles: Sudoku, KenKen, Kakuro, and Futoshiki. Its core innovation is a hierarchical, explicit knowledge base for each game, where complex solving strategies are formally defined as compositions of simpler, foundational strategies. This structure allows for fine-grained evaluation of an agent's reasoning capabilities, from learning basic rules to applying multi-step compositional strategies to solve puzzles of increasing, mathematically validated difficulty. The open-source benchmark provides a challenging new testbed for advancing neuro-symbolic and other advanced AI reasoning systems.

---


### 520. [SMART: A Machine Learning and Monte Carlo Framework for Rapid Analysis of Stochastic Transistor Aging and Process Variation in Digital Circuits](https://arxiv.org/abs/2607.05187)

**<font color=#1a73e8>作者：</font>** Arash Esshaghi, Siavash Es'haghi, Gholamreza Shahabadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As CMOS technology scales into the deep nanometer regime, digital circuit reliability is increasingly threatened by the combined stochastic effects of Bias Temperature Instability (BTI) and Process Variation (PV). Traditional reliability analysis methods, which rely on computationally intensive simulations or extensive lookup tables, fail to scale efficiently for large designs, creating a critical bottleneck in design space exploration. To address this, we propose SMART, a novel framework that integrates Machine Learning (ML) with Monte Carlo simulation to enable rapid, high-fidelity reliability analysis. SMART employs Random Forest regression to predict gate delay distributions directly, bypassing time-consuming atomic model parameter extractions. Crucially, the model utilizes Bayesian Optimization for automated hyperparameter tuning, ensuring maximum predictive robustness across diverse libraries. Experimental validation on ISCAS85 benchmark circuits demonstrates that SMART achieves a 94.54% reduction in analysis time compared to state-of-the-art methods, while maintaining a remarkable average accuracy error of just 1.63%. By shifting computational complexity to an offline training phase, the proposed framework offers a scalable, accurate solution for designing resilient, reliability-aware digital systems.

---


### 521. [Latent Programming Horizons in Coding Agents](https://arxiv.org/abs/2607.05188)

**<font color=#1a73e8>作者：</font>** André Silva, Han Tu, Martin Monperrus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A coding agent solving a software-engineering task spends dozens of steps reasoning, editing code, and running tests, yet little is known about what the underlying language model internally represents about the program it is working on. We show that the residual streams of language models under coding agents linearly encode properties of the evolving program: a logistic-regression probe on hidden states is able to decode whether the current code parses, passes its test suite, reduces the number of failing tests, and introduces regressions, reaching AUC up to 0.83 for correctness across two models and two benchmarks. Our second finding is more surprising: these representations run ahead of the agent's own edits. Probes trained to predict the outcome of future edits (before they are materialized and written on disk) achieve performance above chance up to roughly 25 steps in advance. We call this the agent's latent programming horizon. As a proof of external validity, we show that the probes transfer across benchmarks without retraining. Our positive results open calls for more research in mechanistic interpretability of coding agents.

---


### 522. [When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents](https://arxiv.org/abs/2607.05189)

**<font color=#1a73e8>作者：</font>** Yechao Zhang, Shiqian Zhao, Jiawen Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Persistent personal agents combine long-term memory with access to users' external environments, enabling personalized foreground assistance and proactive background execution. This integration also creates a new path to compromise: untrusted external content can be silently written into persistent memory and later reused as trusted state. We study this threat as stealth memory injection, in which a remote black-box adversary delivers a single email payload that must induce the agent to write poisoned memory, stay hidden in the agent's response to the user, and affect future behavior.
We introduce WhisperBench, a 108-case benchmark spanning five risk categories and both fact and preference poisoning. Built on a real IMAP/SMTP workflow and an authentic email agent skill, it enables full-cycle evaluation of stealth memory injection attacks. To enable this black-box attack under single-email delivery and without runtime feedback, we propose MemGhost, a one-shot payload generation framework. MemGhost uses an environment proxy to emulate persistent-agent execution and an objective proxy to convert memory adoption and conversational stealth into dense rubric-based rewards, then trains the attacker policy with supervised fine-tuning and reinforcement learning.
Across 56 held-out test cases, MemGhost achieves 87.5% end-to-end success on OpenClaw with GPT-5.4 and 71.4% on Claude Code SDK with Sonnet 4.6. It also transfers across personal-agent architectures (NanoClaw and Hermes Agent) and memory backends (filesystem and vector-based Mem0), and remains effective against input-level, model-level, and system-level defenses. These results suggest that persistent memory can turn ordinary external processing into a practical pathway for long-term agent compromise.

---


### 523. [Noisy-Channel Minimum Bayes Risk Decoding](https://arxiv.org/abs/2607.05198)

**<font color=#1a73e8>作者：</font>** Yusuke Sakai, Hidetaka Kamigaito, Taro Watanabe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Minimum Bayes Risk (MBR) decoding yields more robust and higher-quality text generation than maximum a posteriori (MAP) decoding by selecting hypotheses that maximize expected utility over sampled pseudo-references. However, there exists a discrepancy in the design: hypothesis selection calculates expected utility scores conditioned on given pseudo-references, while commonly used evaluation metrics, e.g., BLEU and COMET, are asymmetric. Therefore, it is important to consider both hypothesis-to-reference and reference-to-hypothesis directional effects. In this study, we introduce a noisy channel decomposition of MBR decoding that naturally incorporates bidirectional effects to account for these asymmetries. We decompose MBR decoding into four interacting components: hypothesis-to-reference likelihood, reference-to-hypothesis likelihood, hypothesis prior, and reference prior. This decomposition provides a unified interpretation of existing MBR variants and enables metric- and task-specific interpretability by isolating the contribution of each channel. Our comprehensive analysis reveals that channel-wise contributions exhibit distinct characteristics across metrics while remaining consistent across tasks, and suggests that appropriate channel weighting may lead to improvements over original MBR decoding.

---


### 524. [FlatManifold: Robust Continual Learning under Severe Label Noise and Domain Shifts via Intrinsic Manifold Flattening](https://arxiv.org/abs/2607.05201)

**<font color=#1a73e8>作者：</font>** Rai Hisada, Kanji Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In non-stationary streaming environments, simultaneously adapting to complex, non-linear domain shifts via continual learning while mitigating the catastrophic effects of severe, uncalibrated label noise poses a fundamental mathematical challenge. In this paper, we propose \FlatManifold{}, a novel, streamlined robust continual learning framework that utilizes a Nyström manifold flattening map based on the kernel trick and projection onto an orthogonalized Reproducing Kernel Hilbert Space (RKHS).
Unlike traditional methods that rely on complex, error-prone sample-filtering pipelines, the proposed approach exploits the intrinsic mathematical robustness of the flattened space itself. By mapping feature distributions onto a fixed orthogonal target topology with a ridge regularizer, the framework naturally smoothes and counteracts the influence of extreme label noise during the optimization process. Concurrently, catastrophic forgetting is prevented via a continual topology brake term that leverages the covariance matrix of past experiences.
Extensive evaluation on real-world multi-session robotics datasets demonstrates that even under severe conditions featuring 40\% symmetric label noise, \FlatManifold{} successfully mitigates gradient corruption. Under extreme cross-session domain shifts spanning various seasons and lighting conditions, the proposed framework establishes high generalization capabilities, significantly outperforming standard sequential optimization baselines and proving that structural linearization itself serves as a powerful mathematical barrier against distributed label corruption.

---


### 525. [EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](https://arxiv.org/abs/2607.05202)

**<font color=#1a73e8>作者：</font>** Xingze Gao, Chuanrui Hu, Hongda Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent self-evolution in long-horizon LLM systems is largely procedural: useful experience is not merely stored information, but reusable procedures for searching, debugging, and verification. Yet current evaluations do not isolate this form of transfer. Agent benchmarks test single-episode task solving; memory benchmarks target information retention rather than procedural reuse. We introduce EvoAgentBench, a benchmark for agent self-evolution via Ability-guided transfer across four agentic domains: web research, algorithmic reasoning, software engineering, and knowledge work. EvoAgentBench extracts trace-grounded Abilities from agent executions, canonicalizes them into operational units, and builds domain-specific Ability Graphs linking tasks that share procedural overlap. By design, every test task is backed by verified training-side Ability support. Across a 528/267 train/test split, two scaffolds, and three backbones, curated Ability content transfers reliably across model families, but no current automatic method sustains positive gain in all settings. EvoAgentBench shifts self-evolution evaluation from aggregate accuracy comparison to fine-grained diagnosis of experience encoding, routing, and uptake. The benchmark is publicly available at this https URL.

---


### 526. [Causal-RetiGraph: Cross-Cohort Retinal Support and Same-Subject Pathway Analysis for Diabetic Retinopathy](https://arxiv.org/abs/2607.05204)

**<font color=#1a73e8>作者：</font>** Inam Ullah, Imran Razzak, Shoaib Jameel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diabetic retinopathy (DR) is a local retinal lesion process and a visible manifestation of systemic microvascular injury. Modern retinal AI can grade images accurately, but often leaves unanswered how local lesion evidence, retinal vascular structure, and systemic disease pathways are connected. This paper introduces \emph{Causal-RetiGraph}, a compact biomedical informatics framework that links retinal graph phenotypes with NHANES-anchored pathway modelling. The retinal-image fold constructs an interpretable $X1234$ phenotype from vessel maps, lesion evidence, image embeddings, and AutoMorph biomarkers through spatial $X_{12}$ and Jacobian $X_{34}$ branches. The NHANES fold models systemic exposures, covariates, a same-subject retinal mediator family $R^*$, and downstream outcome families. $X1234$ is used for retinal support and pathway prioritisation, while $R^*$ is used for participant-level pathway summaries. On the retinal fold, $X1234$ achieves 0.9055 binary DR accuracy and 0.9711 AUROC, with graded DR QWK of 0.8312. The results show that lesion and biomarker streams improve contextual retinal representation under scarce and imbalanced data. In NHANES, HbA1c, urine albumin, pulse pressure, fasting glucose, and systolic blood pressure are the strongest binary DR anchors. Participant-level pathway analysis identifies glycaemic--renal and glycaemic--haemodynamic pathways as the clearest mediator-style signals. These results suggest that retinal graph phenotypes can help prioritise systemic pathways in DR while preserving the distinction between image-derived support and same-subject mediation.

---


### 527. [An event-driven framework for fly-inspired visual motion detection](https://arxiv.org/abs/2607.05205)

**<font color=#1a73e8>作者：</font>** Qinbing Fu, Jingyu Huang, Yan Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fast and reliable motion detection is essential for machine vision and autonomous systems operating in dynamic environments. This work integrates emerging event-based sensing with biologically structured neural computation to establish an efficient computational paradigm for visual motion detection. The proposed framework is built upon a recently developed fly-inspired neural network that emulates motion-processing circuits in the optic lobe. Owing to its feed-forward and training-free architecture, the neural model requires only a small number of interpretable parameters and is well suited for real-time embedded implementation. Event cameras provide low-latency, low-power, and high-dynamic-range visual sensing by asynchronously transmitting brightness-change events. However, their performance can be degraded by event noise, including temporal noise and junction-leakage-induced activity, particularly under low-light conditions. Moreover, effective integration between event-based visual representations and biologically inspired neural processing remains under-explored. To address these challenges, we propose an event-driven computational framework that combines time-surface encoding for front-end event representation with a fly optic-lobe-inspired neural network for foreground motion-direction estimation. A bottom-up attention mechanism is further incorporated to suppress background motion and enhance the saliency of foreground targets. The proposed method is evaluated on real-world ground-vehicle datasets and compared with a baseline frame-based model and an optimization-based approach. Experimental results demonstrate that the framework effectively combines the temporal advantages of event-driven vision with the efficiency and interpretability of bio-inspired neural processing.

---


### 528. [Probing Geospatial SSL Representations with Environmental Signals](https://arxiv.org/abs/2607.05207)

**<font color=#1a73e8>作者：</font>** Rohita Mocharla, Vishal M. Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) is designed to learn generic, transferable representations rather than representations optimized for a single task. Most geospatial benchmarks evaluate representations solely through downstream tasks, providing limited insight into the information encoded within the representation itself. We ask a different question: do SSL representations of satellite imagery preserve statistical associations with environmental variables that co-vary with the imaging process? To answer this question, we probe SSL representations using co-located ERA5 reanalysis variables, a global dataset of physically consistent environmental variables, including temperature, precipitation, surface solar radiation, surface pressure, and volumetric soil water. These variables are physically related to the spectral reflectance and radar backscatter recorded by Sentinel-1 and Sentinel-2, making them meaningful evaluation targets despite not being used during SSL pretraining. We complement this probing analysis with intrinsic representation metrics to characterize representation geometry and investigate how these properties relate to downstream performance and the encoding of environmental signals. Using DINO, MAE, and MoCo models trained under identical conditions, we show that representation-level metrics distinguish models with similar downstream benchmark performance, providing complementary information beyond task-driven benchmarks. We further find that the linear accessibility of environmental signals is associated with performance on environmentally dependent tasks in the PANGAEA benchmark. Finally, we release ERA5 annotations co-located with the SSL4EO dataset to enable physically grounded representation evaluation for future geospatial foundation models.

---


### 529. [Progressive Refinement: An Iterative Pseudo-Labeling Approach for Mandarin-English Code-Switching ASR](https://arxiv.org/abs/2607.05224)

**<font color=#1a73e8>作者：</font>** Qu Yang, Cakra Wardhana, Tim Ng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code-switching (CS), alternating languages within the same utterance, poses significant challenges for automatic speech recognition (ASR) due to limited CS training data. This paper applies an iterative pseudo-labeling training approach to CS-ASR for the first time, demonstrating its effectiveness in leveraging unlabeled data to improve CS-ASR performance. The approach comprises three phases: pseudo-label generation, two-stage bilingual model training, and iterative improvements. It begins by generating pseudo-labels from a large unlabeled corpus, creating a semi-supervised dataset. This dataset supports a two-stage training framework where the model is pre-trained and then fine-tuned on supervised CS data. Iterative refinements further enhance the model's accuracy in handling complex CS scenarios. Our approach significantly advances CS-ASR systems, achieving notable Mix Error Rate (MER) reductions on SEAME's devman (6.35%) and devsge (8.29%) subsets.

---


### 530. [Video-based detection of cessation of breathing in pre-term infants using machine learning](https://arxiv.org/abs/2607.05230)

**<font color=#1a73e8>作者：</font>** Dineo Serame, Lionel Tarassenko, Mauricio Villarroel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-term infants are susceptible to potentially harmful apnoea-related cessations of breathing due to immature respiratory control. However, reliable respiratory monitoring in the neonatal intensive care unit (NICU) remains challenging because motion artefacts, sensor displacement, and skin fragility can compromise contact-based measurements. Non-contact video monitoring offers a complementary approach that does not depend on adhesive sensors while providing additional respiratory information.
We investigated whether camera-based signals can detect apnoea-related cessation of breathing (COBE) and provide complementary information to routinely acquired physiological signals. Using video and clinical recordings from 30 pre-term infants, respiratory motion was extracted from dynamically tracked torso regions to generate camera-derived time-series signals. Camera-only models were trained using residual network (ResNet) architectures, while hybrid models combined video-derived signals with impedance pneumography (IP), ECG-derived respiration (EDR), and the PPG-derived respiratory envelope.
Camera-only models achieved a balanced accuracy of 76.9%, demonstrating the feasibility of non-contact COBE detection. Combining video-derived features with IP improved balanced accuracy to 90.6%, outperforming either modality alone and indicating that video provides respiratory information beyond standard physiological signals.
These findings show that video-derived signals contain clinically relevant respiratory features and enhance COBE detection when combined with conventional physiological signals. This supports non-contact video as a complementary modality for automated COBE detection and highlights its potential to improve the robustness of neonatal respiratory monitoring.

---


### 531. [CanniUplift: A Holistic Framework for Mitigating Seller and Incentive Cannibalization in E-commerce Uplift Modeling](https://arxiv.org/abs/2607.05242)

**<font color=#1a73e8>作者：</font>** Zuwang He, Shihao Shu, Yuli Qu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized incentive allocation is vital for e-commerce, where uplift modeling is the standard for estimating Individual Treatment Effects (ITE). However, traditional models often fail in complex multi-seller environments with violations of the Stable Unit Treatment Value Assumption (SUTVA). We identify two critical challenges: Seller-level Cannibalization, where incentives shift expenditure between shops without growing the platform, and Incentive-level Cannibalization, where organic conversions or alternative rewards introduce significant noise into incrementality estimation. In this paper, we propose CanniUplift, a unified framework to mitigate these dual-source cannibalization effects. Specifically, we design Platform-level Global Alignment (PGA) to capture cross-shop substitution through global GMV consistency constraints. To tackle incentive-driven noise, we introduce Redemption-based Decomposition Denoising (RDD), which uses redemption behavior to decompose treated outcomes and reduce attribution noise within an entire-space framework. Furthermore, a Treat-Attention mechanism is designed to model intricate interactions between users' historical behaviors and current treatment options. Extensive experiments on both synthetic and large-scale industrial datasets demonstrate that CanniUplift significantly outperforms state-of-the-art baselines. Ablation studies confirm that the integration of PGA and RDD consistently improves wAUUC and wQINI. Successfully deployed online, our framework achieved a 4.08% relative increase in platform-wide incremental GMV (Delta GMV) over the production baseline and improved ROI in online A/B tests, proving effective in driving global platform growth.

---


### 532. [GUSH3R: Everyone Everywhere All at Once as Gaussians](https://arxiv.org/abs/2607.05243)

**<font color=#1a73e8>作者：</font>** Keito Abe, Kaede Shiohara, Takashi Otonari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic human-scene environments from monocular videos is a challenging problem that requires jointly modeling scene geometry, camera motion, and non-rigid human dynamics while enabling photorealistic rendering. Recent feed-forward methods can efficiently predict geometry, but they are often limited to non-photorealistic representations such as point clouds and meshes, or they fail to handle non-rigid objects, particularly dynamic humans. To fill this gap, we present GUSH3R (Gaussian-Unified Scene Human 3D Reconstruction), a feed-forward framework for online dynamic human-scene reconstruction. From a monocular human-scene video, our method reconstructs dynamic humans (everyone) and static scenes (everywhere) in a single forward pass (all at once) as 3D Gaussian Splatting (3DGS) primitives (as gaussians), which are geometrically consistent and capable of novel view synthesis. Experiments on monocular human-scene datasets demonstrate that our approach achieves competitive novel view synthesis quality while significantly improving inference efficiency compared to optimization-based methods.

---


### 533. [Vision Pretraining for Dense Spatial Perception](https://arxiv.org/abs/2607.05247)

**<font color=#1a73e8>作者：</font>** Zelin Fu, Bin Tan, Changjiang Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense spatial perception is essential for physical intelligence, where visual systems are expected to recover structured, metric, and actionable representations from pixel observations. Modern visual foundation models tend to prioritize semantic invariance, often at the expense of detailed spatial understanding. In this work, we study vision pretraining through a boundary-centric lens, motivated by the premise that boundaries and shape discontinuities offer essential cues for perceiving geometric properties. Concretely, we propose masked boundary modeling, a self-supervised paradigm that dynamically learns sub-pixel boundary representations and subsequently leverages the discovered boundary-bearing tokens as masked targets to facilitate dense visual token learning. By scaling this framework, we develop LingBot-Vision and demonstrate its efficacy across a diverse set of downstream vision tasks with DINOv3 as a strong baseline. Remarkably, LingBot-Vision drives the progression from LingBot-Depth 1.0 to LingBot-Depth 2.0 for depth completion, and thereby yields enhanced depth estimation, a key pillar for embodied artificial intelligence. Our findings reveal that boundary modeling goes beyond simple line segments and instead serves as a scalable pretraining principle for learning spatially structured visual representations.

---


### 534. [Streaming Neural Speech Codecs through Time-Invariant Representations](https://arxiv.org/abs/2607.05250)

**<font color=#1a73e8>作者：</font>** Kélian Estève, Salima Mhdaffar, Mickael Rouvier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural speech codecs are increasingly used as intermediate representations in codec-based speech generation systems. TiCodec introduces a factorized representation that separates time-varying speech content from time-invariant information through a Time-Invariant Representation Extraction (TIRE) module, potentially reducing the amount of information that must be modeled at the frame-level.
In this work, we investigate the nature of the information captured by TIRE representations and their suitability for low-latency speech processing. Using a series of probing tasks, we analyze the influence of the encoder layer and show that intermediate layers capture complementary speaker- and environment-related information while containing little linguistic content. We further study several segment selection strategies for TIRE training and demonstrate that cross-file sampling improves the robustness of invariant representations. Based on these findings, we propose Dual-TIRE, a multi-level architecture that exploits the complementarity of different encoder layers and improves speech reconstruction quality and speaker similarity.
Finally, we evaluate TiCodec in a streaming inference setting using successive 660ms processing blocks. Results show that streaming operation can be achieved without significant degradation in reconstruction performance, highlighting the potential of factorized neural codec representations for future low-latency speech generation systems.

---


### 535. [Privacy-Preserving Robustness Verification for Neural Networks](https://arxiv.org/abs/2607.05251)

**<font color=#1a73e8>作者：</font>** Nianyun Song, Xiaokun Luan, Yu Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Neural network verification and data privacy are inherently in tension: verification demands full access to model parameters and input data, yet both are increasingly restricted by privacy regulations and intellectual property constraints. This tension has left robustness verification impractical in privacy-sensitive domains. In this work, we address this gap with SecureCROWN, the first framework for privacy-preserving neural network robustness verification. Built upon secure two-party computation (2PC), our framework enables a model owner and a data owner to jointly compute certified robustness bounds -- revealing only the final result while provably protecting both parties' private data under the semi-honest security model. A key challenge is securely computing the conditional operations in Linear Bound Propagation, where the data-dependent branching is incompatible with standard secure computation protocols. We eliminate branching by formulating conditional logic as continuous arithmetic operations. Additionally, we introduce a Newton--Raphson refinement method to improve numerical stability. Extensive analysis and experiments show that SecureCROWN strictly matches plaintext verification results, while completing in 0.1--200s across varied model sizes and communication settings (LAN/WAN), demonstrating the feasibility of privacy-preserving neural network verification.

---


### 536. [FUSE: FK-Steered Multi-Modal Flow Matching for Efficient Simulation-Based Posterior Estimation](https://arxiv.org/abs/2607.05252)

**<font color=#1a73e8>作者：</font>** Weichen Qin, Yufan Xie, Peihao Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulation-Based Inference (SBI) is critical for scientific discovery, with generative models offering a promising path toward efficient inference. However, existing methods struggle with effective multimodal modeling. They often rely on brute-force fusion strategies that ignore the structural disparities between parameters and observations, thus limiting estimation fidelity. In this work, we introduce FUSE (Feynman-Kac steered mUlti-modal flow matching for efficient Simulation-based posterior Estimation). Unlike prior work, FUSE employs a dual-track architecture that preserves the distinct features of multimodal inputs while facilitating dynamic interaction. Additionally, we propose an FK-steered sampling strategy that leverages intermediate observation likelihoods to guide the generative trajectories, effectively improving the sample quality during inference. Our approach outperforms state-of-the-art baselines on standard SBI benchmarks, producing posteriors that closely match ground-truth MCMC. Furthermore, in a real-world exoplanet orbital estimation task, FUSE successfully resolves complex parameter degeneracies that challenge existing methods, highlighting its potential to accelerate complex scientific discoveries in astrophysics and beyond.

---


### 537. [Repurposing CLIP to Localize at Pixel Level](https://arxiv.org/abs/2607.05253)

**<font color=#1a73e8>作者：</font>** Jiaxiang Fang, Shiqiang Ma, Jing Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale Vision-Language Models like CLIP have demonstrated impressive open-set localization capabilities at the image level. However, adapting this capability to pixel-level dense prediction poses challenges due to global feature biases. In this paper, we introduce CLIPix, a simple yet effective framework that repurposes CLIP to perform pixel-level localization. By tracing back CLIP's classification process, CLIPix identifies object-specific attentive regions and repurposes them as pixel-level localization cues. To address noise introduced by global biases, we propose a Noise-Resistant Correction strategy, refining these cues for more precise segmentation. Additionally, we introduce a Localization Embedding strategy to integrate both localization and enriched detail information, enabling accurate, high-resolution segmentation. Our approach preserves CLIP's generalization strength and unlocks its potential for segmenting arbitrary objects. Extensive experiments on the PASCAL and COCO datasets demonstrate that CLIPix achieves state-of-the-art performance, underscoring its effectiveness.

---


### 538. [GeoFlow: Geo-Aware Modeling of Inter-Area Relationships in Origin-Destination Flow Prediction and Generation](https://arxiv.org/abs/2607.05257)

**<font color=#1a73e8>作者：</font>** Zherui Huang, Guanjie Zheng, Hao Xue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Origin-destination (OD) flow modeling underpins urban planning and mobility analysis, but prevailing graph-based methods often neglect salient geographic attributes, limiting their ability to model long-range and multi-area dependencies. In this paper, we introduce GeoFlow, a novel framework that (i) augments area representations with geospatial attributes, including relative positions, k-hop and geodesic distances, (ii) employs a specialized geometric-intrinsic fusion encoder design that combines graph attention for intrinsic area signals with coordinate-aware encoders for global structure, and (iii) adopts an axial-global attention decoder to capture OD-specific competitive dependencies. For OD flow generation, GeoFlow is paired with flow matching models to produce more authentic and diverse mobility samples. Empirically, GeoFlow achieves superior performance in predictive accuracy, while substantially improving generative fidelity and diversity. Ablation and analytical studies confirm the contribution of each component. Code is available at this https URL.

---


### 539. [SalAngaBhava: A Sinhala Market Dataset for Aspect-based Sentiment Analysis](https://arxiv.org/abs/2607.05259)

**<font color=#1a73e8>作者：</font>** Lakshani Galwatta, Nisansa de Silva, Sarangi Aththanayake 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentiment analysis has been a primary domain under Natural Language Processing (NLP) from its inception as it plays a vital role in both real-world and research applications. In high-resource languages, this has been extended a step further, and instead of predicting sentiment at the sentence level, models have been developed to detect more fine-grained sentiments at aspect level. However, in order to conduct this fine-grained Aspect-based Sentiment Analysis (ABSA), datasets annotated with aspects and sentiments toward the said aspects is required. Such datasets are lacking for low-resources languages among which, we can count Sinhala, an Indo-Aryan languages used primarily in Sri Lanka. In this work, we introduce, SalAngaBhava, a new Sinhala Aspect-based Sentiment Analysis dataset which contains Sinhala product reviews that are manually labeled with aspect terms and the associated sentiments (positive, negative, neutral). The data was collected from domain-relevant sources such as user-generated reviews and comments, and was annotated following carefully defined guidelines to ensure consistency and quality. The dataset consists of sentences and aspect-sentiment pairs, encompassing a considerable range of aspects from several domains. The analysis confirms that the dataset is well-structured and sufficiently balanced for ABSA research. This dataset can be used as a benchmark and facilitates further studies related to Sinhala natural language processing, and low-resource sentiment analysis tasks.

---


### 540. [Shifting from Discrete to Continuous Reference Data: QSM-Derived Horizontal Tree Biomass Distribution for Deep Learning Biomass Estimation](https://arxiv.org/abs/2607.05260)

**<font color=#1a73e8>作者：</font>** Nils Griese, Christoph Kleinn, Nils Nölke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional modeling approaches for LiDAR-based above-ground biomass (AGB) estimation rely on discrete plot-level inventory aggregates. This methodology introduces boundary-effect uncertainties that may severely degrade model performance within small field plots. To solve this limitation, we evaluate a Horizontal Biomass Distribution (HBD) reference mapped continuously from Quantitative Structure Models (QSMs). We trained a sparse 3D U-Net on simulated broadleaved forest structures using three AGB reference types: a standard forest inventory (FI) plot-level aggregate, an edge-effect-free QSM plot-level aggregate, and a continuous HBD mapping. Evaluating training plot sizes scaling from 100 to 2500 $m^2$ , QSM-based models systematically outperformed FI approaches at small plot sizes. Specifically, for 100 $m^2$ plots, the HBD reference reduced the relative root mean square error (RRMSE) by 16.84 $\pm$ 4.37 % and increased $R^2$ by 0.22 $\pm$ 0.05 against the FI baseline. By replacing plot level aggregates with HBDs as AGB reference, this methodology corrects for edge-effects and shows that using an HBD-based reference enhances model performance for small plot sizes.

---


### 541. [FlowMark: Mask-Guided Video Watermarking](https://arxiv.org/abs/2607.05261)

**<font color=#1a73e8>作者：</font>** Vishal Asnani, Shruti Agarwal, John Collomosse  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FlowMark, a video watermarking framework guided by automatically predicted object masks. In contrast to prior region-based approaches that require user-supplied mask guidance, FlowMark learns to identify optimal regions for watermark embedding through a dedicated Mask Predictor network. Our end-to-end trainable architecture combines region-aware encoding with noise-augmented training to ensure robustness against compression, geometric transformations, and content variation, while preserving high perceptual quality. Our content-adaptive masking keeps watermark signals coherent with natural video dynamics, effectively eliminating perceptual flicker. Beyond compression robustness, FlowMark maintains reliable watermark recovery under video-native temporal edits (e.g., frame swap, insertion, deletion, resampling, and interpolation) and real-world social media distribution pipelines (e.g., YouTube and Facebook re-encoding). Experimental results on both image and video datasets show that FlowMark reliably embeds $128$-bit messages with up to $50.08$ dB PSNR, offering strong performance for content provenance, temporal authenticity verification, and video integrity protection.

---


### 542. [Learning Probabilistic Embeddings for Unsupervised Action Segmentation](https://arxiv.org/abs/2607.05263)

**<font color=#1a73e8>作者：</font>** Shuai Li, Duc Manh Vu, Juergen Gall  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper concerns the problem of unsupervised temporal action segmentation for long, untrimmed videos. Recent successful approaches follow a joint representation learning and clustering paradigm, where optimal transport (OT) is adopted to produce pseudo labels for learning frame representations. These approaches alternate between estimating pseudo labels using OT and optimizing the parameters with gradient descent during training, where OT is used for obtaining the final temporal action segmentation. A major limitation of these works is that they learn a deterministic embedding for frame representations. The iterative procedure between learning deterministic embeddings based on pseudo labels and estimating pseudo labels from the learned embedding can thus get quickly stuck in a local optimum. As an alternative, we thus propose to learn a probabilistic embedding for frame representations. The embeddings are modeled by Gaussian distributions and we sample from the distributions before estimating the pseudo labels. We evaluate our approach on several challenging temporal action segmentation datasets and achieve results comparable to, and in some cases, better than the state of the art. Compared to baselines with deterministic embeddings, our approach improves MoF up to 20.7\% and F1-score up to 19.0\%. Our code is available at this https URL.

---


### 543. [Target-Guided Selective Reweighting for Physics-Informed Neural Network Inverse Problems: A Transfer Learning Approach](https://arxiv.org/abs/2607.05271)

**<font color=#1a73e8>作者：</font>** Qian Hu, Bin Fan, Yao Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) encounter ill-posed optimization, loss competition, and parameter compensation in partial differential equation (PDE) inverse problems. Transfer learning can reuse representations from source tasks, but direct fine-tuning may introduce negative transfer when dominant physical mechanisms, governing parameters, or observation noise differ between source and target domains: the model achieves low field error yet recovers incorrect target physical parameters. To mitigate, we propose Target-Guided Selective Reweighting PINN (TGSR-PINN), a target-evidence-driven representation correction method for PINN inverse transfer learning. TGSR-PINN transfers only the weights and biases from the source PINN, while target physical parameters are independently initialized; after a short target-adaptation phase, the method computes neuron target scores using first-order Taylor sensitivity and pre-activation variance on fixed scoring batches, and converts evidence associated with low-scoring neurons into continuous weak-adaptation signals via a Gaussian mixture model (GMM) with rank fallback. TGSR-PINN then applies selective soft decay to input weight rows and biases of low-scoring neurons instead of hard pruning or random resetting. In experiments, TGSR-PINN improves target parameter recovery while maintaining comparable field accuracy in the high-Péclet 2D advection-diffusion task and in the Allen--Cahn to Burgers cross-PDE-family transfer task; a 5%-noise reaction--diffusion case provides supplementary evidence under milder source-target mismatch. Ablation studies suggest that neuron target scoring, weak-adaptation signal estimation, layer protection, and selective soft decay jointly contribute to the benefits.

---


### 544. [Adaptive Inference Batching using Policy Gradients](https://arxiv.org/abs/2607.05272)

**<font color=#1a73e8>作者：</font>** Ruslan Sharifullin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference serving systems must balance throughput and latency under bursty, heterogeneous workloads, yet the industry standard remains static batching policies that require manual tuning and cannot adapt to shifting traffic. We investigate whether reinforcement learning (RL) can learn adaptive batching and routing policies that outperform these heuristics, training REINFORCE and PPO agents on a discrete-event simulator validated against queuing theory and production traces (Azure Functions, BurstGPT). We formulate the problem as an MDP over queue state, request type and GPU availability, evaluating across standard Poisson traffic, extreme bursts, real-world traces and heterogeneous multi-GPU routing.
Our central finding is a clear boundary condition for RL's value in systems problems. In single-GPU settings, a well-tuned static batching policy is already near-optimal under Poisson-like arrivals and RL offers only marginal gains (+0.1% to +1.0%). In multi-GPU heterogeneous routing, however, where fast and slow requests compete for shared resources, the agent discovers a workload-segregation policy that eliminates Head-of-Line blocking, yielding a 3.5x (348%) improvement over Round-Robin and a 48% improvement over the strongest heuristic baseline (Shortest-Queue), with 60% higher throughput and 25% lower latency while respecting SLA constraints. The policy generalizes to unseen bursty and real-world traffic despite training only on synthetic Poisson arrivals and an attention-augmented policy network converges roughly 20% faster than an MLP baseline.
These results suggest RL's advantage over engineered heuristics concentrates in combinatorial, multi-resource decisions rather than single-resource temporal scheduling, a practical distinction for deciding where learned policies justify their engineering cost in production inference infrastructure.

---


### 545. [Erasing Without Collateral Damage: Precise Concept Removal in Diffusion Models](https://arxiv.org/abs/2607.05274)

**<font color=#1a73e8>作者：</font>** Parth Upman, Nishita Jain, Shreyank N Gowda  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free concept erasure is an attractive mechanism for controlling text-to-image diffusion models, but precise erasure often comes at the cost of damaging semantically related non-target concepts. Existing value-space methods remove the component of each cross-attention value along the target concept direction, implicitly treating target identity and shared visual structure as the same signal. We argue that this is the source of much of the collateral damage in prior preservation. We introduce CARE, a closed-form concept erasure operator that replaces the raw target direction with a kept-subspace-aware direction computed from a small bank of retained concept anchors. The resulting edit is applied directly in cross-attention value space, requires no model fine-tuning, and adds only a negligible offline computation. A single shrinkage parameter controls the erase-preserve trade-off. We further show that the operator admits a minimum-disturbance interpretation and, in its projection form, leaves the kept subspace invariant. Experiments under the standard concept-erasure protocol show that our method preserves non-target concepts more faithfully while maintaining competitive erasure across instance, style, and celebrity concepts. Code: this https URL

---


### 546. [Untrusted Content Masking for Web Agents with Security Guarantees](https://arxiv.org/abs/2607.05277)

**<font color=#1a73e8>作者：</font>** Kristina Nikolić, Egor Zverev, Javier Rando 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Defenses that provide security guarantees against prompt injection attacks rely on strict isolation between trusted instructions and untrusted data. In text-based environments such as tool-use APIs, this separation arises naturally: agents can reason from interface definitions without ever processing untrusted content. Extending these guarantees to web agents faces a fundamental challenge: to perceive and interact with their environment, web agents must first observe the rendered page, which intermingles trusted content with untrusted content. This structural entanglement removes the trust boundary on which security guarantees depend, undermining provable defenses for web agents. In this paper, we present Untrusted Content Masking (UCM), a simple and effective approach that restores this boundary in web environments. We leverage a key structural insight: a webpage's Document Object Model (DOM) encodes sufficient information to distinguish trusted from untrusted regions without reading their content. Our framework exploits this by redacting untrusted regions before they reach the agent and routing interaction through a sandboxed interface with strict privilege separation, thereby enabling agents to observe and interact with their environment while remaining isolated from adversarial content. The code is publicly available.

---


### 547. [Advances in Neural Controlled Differential Equations](https://arxiv.org/abs/2607.05280)

**<font color=#1a73e8>作者：</font>** Benjamin Walker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world systems evolve continuously, yet most machine learning models interpret time series as discrete sequences. Continuous-time approaches instead treat time series as samples from an underlying input path, a formulation that naturally accommodates irregularly sampled or oversampled data. Among these, Neural Controlled Differential Equations (NCDEs) are a maximally expressive class of models that parametrise a vector field using a neural network and evolve their hidden state by solving a dynamical system driven by the input path. NCDEs typically use a non-linear vector field, so their expressive power and continuous-time flexibility come at the cost of a forward pass that is both computationally expensive and inherently sequential, limiting their scalability and practical applicability.
This thesis advances the training and scalability of NCDEs through three complementary contributions. First, building on neural rough differential equations, Log-NCDEs apply the Log-ODE method to efficiently approximate an NCDE's solution during training, improving both computational speed and empirical performance. Second, Linear NCDEs replace the non-linear vector field with a linear one, enabling closed-form solutions and parallel-in-time computation without sacrificing theoretical expressivity. Third, Structured Linear NCDEs use structured linear vector fields to further enhance efficiency while maintaining theoretical expressiveness and empirical performance.
Collectively, these methods reduce the time per training step for an NCDE by up to three orders of magnitude while achieving state-of-the-art performance across diverse time series benchmarks.

---


### 548. [Air Quality Downscaling with Station-Guided Pseudo-Supervision](https://arxiv.org/abs/2607.05292)

**<font color=#1a73e8>作者：</font>** Guorun Wang, Simone Foti, Andreas D. Demou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Super-resolving coarse atmospheric fields to local PM$_{2.5}$ variations is uniquely challenged by a mismatch in spatial support: while pixels represent regional averages, ground-truth observations are discrete, unaligned samples of a continuous spatial signal. To bridge this gap, we present a station-guided framework for high-resolution PM$_{2.5}$ downscaling over Europe. Taking coarse CAMS atmospheric composition fields alongside heterogeneous side information (i.e., human activity, land cover, elevation, satellite aerosol observations, and wind fields) our framework jointly super-resolves ($\times 40$, $\approx$ 1 km) and bias-corrects CAMS rasters, without relying on temporal sequence modelling. To address the challenge of densely supervising our multi-scale transformer network with sparse in-situ data, we introduce a time-agnostic propagation strategy that utilises spatial Gaussian blending of interpolated OpenAQ observations. Extensive qualitative and station-level evaluations across Europe demonstrate that our model recovers fine-grained spatial structures and effectively mitigates localised CAMS biases.

---


### 549. [Biologically Informed Deep Neural Networks for Multi-Omic Integration, Pathway Activity Inference and Risk Stratification in Cancer](https://arxiv.org/abs/2607.05306)

**<font color=#1a73e8>作者：</font>** Pedro Henrique da Costa Avelar, Le Ou-Yang, Min Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrating complex, multi-omics data presents significant challenges. Existing approaches often face a trade-off between model interpretability and representational capacity, with most either relying on post-hoc interpretation or use linear models that may overlook complex interactions. We report Pathway Activity Autoencoders for the multi-omics setting, which embed prior knowledge via pathway-informed architectural constraints, fostering interpretability, while preserving representational power. Our multi-omic framework is applied in the context of breast cancer and is evaluated in survival prediction and subtype classification with results indicating a positive effect of integration. We conduct analysis of individual omics layer impact on end-task performance, revealing that gene, protein, and microRNA expression layers provide the strongest contribution. Repeatability studies indicate that, while dropout improves model robustness and consistency, excessive regularisation can reduce predictive performance. Finally, visualizations of the learned feature space illustrate the framework's intrinsic transparency and clinical relevance. The results underscore the value of multi-omic integration and delineate the impact of individual omics layers, establishing practical guidelines for integration within our framework. Overall, our pathway activity autoencoder frameworks yield superior latent representations that are biologically meaningful and are directly translatable into clinically relevant insights.

---


### 550. [Topological Shape Representation for Aneurysm -- Bifurcation Detection](https://arxiv.org/abs/2607.05317)

**<font color=#1a73e8>作者：</font>** Akshay Gokhale, Mansi Dhamne  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated detection of intracranial aneurysms (IAs) from CT angiography (CTA) is severely hindered by high false-positive rates. Convolutional neural networks (CNNs) rely on local pixel intensities, causing systematic confusion between saccular aneurysms and vascular bifurcations -- a problem especially acute for small lesions (<3 mm), where detection sensitivity falls below 60%. We propose a plug-and-play, topology-aware false-positive reduction framework evaluating the Smooth Euler Characteristic Transform (SECT) -- a directional representation encoding global 3D vascular geometry independently of intensity -- against persistence-based summaries (Persistence Images and Landscapes), tested on a stratified subset of the RSNA 2025 dataset. SECT achieves an AUC of 0.943, substantially outperforming direction-agnostic methods (AUC ~0.68), and exhibits a clinical performance inversion: it excels on the sub-3 mm cohort, maintaining 0.943 AUC and 78.5% sensitivity at 95% specificity. The representation is also scanner-agnostic, achieving 0.927 mean AUC under leave-one-scanner-out (LOGO) validation across four manufacturers. By capturing asymmetric geometric invariants rather than intensity profiles, SECT reliably resolves the primary structural confounder in IA detection, positioning it as a robust downstream filter for hybrid deep-learning diagnostic pipelines.

---


> [!TIP]
> 当前位于：**501-550**（第 11/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
