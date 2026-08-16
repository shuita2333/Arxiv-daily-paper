# 📦 其他研究 | 2026年08月17日

> 本类共 **199** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-199](./part-04.md)

---

### 101. [DiCoR: Decoupled Referent Disambiguation and Contour Recalibration for Efficient Referring Remote Sensing Image Segmentation](https://arxiv.org/abs/2608.12980)

**<font color=#1a73e8>作者：</font>** Ziyang Gao, Zhizhuo Jiang, Jingjing Chang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring remote sensing image segmentation (RRSIS) aims to delineate targets specified by natural language expressions in remote sensing imagery. Existing methods mainly follow joint fusion segmentation (JFS) or decoupled prompt segmentation (DPS). JFS is efficient but often suffers from limited accuracy because referent localization and mask delineation are optimized under a unified objective, whereas DPS separates localization from mask generation using spatial prompts and foundation segmenters at the cost of higher memory consumption and inference latency. To bridge this gap, we propose DiCoR, a decoupled referent disambiguation and contour recalibration framework built on an efficient JFS pipeline. DiCoR addresses two key challenges: distinguishing the correct referent from ambiguous candidates and refining coarse masks after localization. A disambiguation-aware localization guidance strategy ranks salient candidate regions with adaptive linguistic cues and injects the resulting localization prior into fused features. A lightweight contour recalibration module further predicts residual corrections to coarse logits under localized contour supervision, improving mask quality with limited computational overhead. Experiments on RefSegRS, RRSIS-D, and RISBench show that DiCoR achieves the best segmentation accuracy across all three benchmarks. On RefSegRS, it improves mIoU and gIoU by 5.28% and 2.87% over a competitive JFS method while running 4.7% faster than a representative DPS method, demonstrating a favorable accuracy-efficiency trade-off. Code is available at this https URL.

---


### 102. [Learning the Mathematical Property for Designing Low Mutual Coherence Binary Sensing Matrices](https://arxiv.org/abs/2608.12982)

**<font color=#1a73e8>作者：</font>** Rekha, Santosh Singh, S. K. Neogy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this research work, we are constructing the sensing matrix, which is essential for the success of the compressive sensing technique. We have chosen a learning-based technique for the construction of the sensing matrix. The novelty and uniqueness of the proposed technique is that it does not use any data set and also does not use a specific application. It uses the mathematical property/constraint for the construction of the sensing matrix for the perfect recovery of the signal. The perfect recovery of signals is an old and still very challenging problem in real-world applications. In late 2000, compressive sensing became a popular mathematical tool for the perfect recovery of sparse signals. The core of the compressive technique is the construction of the sensing matrix, which satisfies certain special properties such as restricted isometry property (RIP), null space property (NSP), and spark property (SP). All these properties are NP-hard problems and hence computationally challenging to solve. For all practical purposes, the construction of the sensing matrix needs to achieve low mutual coherence to achieve the perfect recovery of the signals. We have used a neural network for the construction of the sensing matrix, and this framework constructs a binary sensing matrix with low mutual coherence. The entries in the matrix are generated through a shared underlying rule. The proposed architecture is simple and does not use large-scale training data sets. Such uniqueness and novelty bring a drastic reduction in computational cost, and also, for the first time in literature, the use of a mathematical property for defining the loss function. In this proposed research work, the mutual coherence property has been used in the neural network framework. Such a neural network framework brings generality, robustness, and reduces storage requirements.

---


### 103. [Balanced Adaptive Prototype Selection for Scalable TabPFN Inference on Large-Scale Tabular Data](https://arxiv.org/abs/2608.12989)

**<font color=#1a73e8>作者：</font>** Mahboobe Jadid, Melika Rezaye Garkani, Ali Mousavi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained tabular foundation models have demonstrated strong predictive capability; however, their application to large-scale datasets remains constrained by the limited inference context. This paper introduces Balanced Adaptive Prototype Selection (BAPS), a framework for constructing compact, information-preserving contexts for scalable TabPFN inference. Without modifying or retraining the pretrained model, BAPS jointly preserves representative structure, informative decision boundaries, local density, class balance, and feature-space diversity. Experiments on the million-row HIGGS and SUSY datasets show that 512 prototypes retain strong predictive performance and reliable calibration, corresponding to an approximately 1,953-fold context compression. All experiments were conducted on an Intel Core i7 CPU with 16 GB RAM and no GPU acceleration. These findings establish effective context construction as a practical mechanism for extending pretrained tabular foundation models to million-scale datasets.

---


### 104. [OGR-MARL: Option-Guided Residual Multi-Agent Reinforcement Learning for Heterogeneous USV Cooperative Pursuit in Constrained Port Waterways](https://arxiv.org/abs/2608.12995)

**<font color=#1a73e8>作者：</font>** Mao Jiayang, Wang Lanfeng, Peng Zhao-Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Heterogeneous USV cooperative pursuit in constrained port waterways requires evader interception under navigation, traffic, and role constraints. This paper proposes OGR-MARL, an option-guided residual multi-agent reinforcement learning framework that is decoupled from a specific MARL algorithm. OGR-MARL integrates shared evader belief, role-conditioned option targets, adaptive rule penalties, and residual policy learning, allowing different MARL algorithms to learn corrective actions on top of rule-guided behaviors rather than exploring constrained port environments from scratch. We instantiate OGR-MARL with representative continuous-control MARL backbones, including MADDPG, MATD3, MAPPO, and MASAC, yielding OGR-MADDPG, OGR-MATD3, OGR-MAPPO, and OGR-MASAC. Experiments in an abstract Xiazhimen port-waterway scenario show that the OGR-MASAC instantiation achieves a 75.0% capture rate, promising mission-effective rule compliance, and the best heterogeneous coordination among the tested methods. Without retraining, zero-shot transfer to a QGIS/AIS-informed Xiazhimen map achieves promising results, demonstrating the generalization potential of OGR-MARL in more complex port scenarios.

---


### 105. [ATOBench: Tracing How Autonomous Penetration-Testing Agents Verify Vulnerabilities When Target Evidence Lies](https://arxiv.org/abs/2608.12996)

**<font color=#1a73e8>作者：</font>** Qiyang Chen, Yixi Li, Fengwei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous penetration-testing agents rely on target responses. These responses guide both subsequent actions and the final report. A deceptive response can therefore redirect both the attack trajectory and the agent's verification process. However, final reports reveal little about how an agent interprets conflicting evidence, changes course, decides to stop, or turns observations into a vulnerability claim. We introduce ATOBench, an evaluation framework that makes this verification process observable. ATOBench injects registered response transformations at runtime and pairs each transformed episode with a native episode under the same environment. Each pair is aligned at the first affected response. A source-linked reconstruction then follows later actions, evidence recovery, stopping, and report support. Three frozen observation contracts cover exploit proof, resource ownership, and reusable artifacts. We evaluate five model routes over 450 episodes. The analysis shows that increased activity can mask a broken verification chain, while successful recovery depends on finding usable evidence and preserving it through reporting. ATOBench turns deceptive target observations into a reproducible probe of evidence handling in autonomous penetration testing. This process-level view extends offensive pentest agent evaluation beyond final outcomes by revealing how untrusted observations shape actions, verification, and reporting.

---


### 106. [PixSDS: Why Latent SDS Makes Noisy Pixels](https://arxiv.org/abs/2608.12997)

**<font color=#1a73e8>作者：</font>** Vsevolod Skorokhodov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Score Distillation Sampling (SDS) enables text-to-3D generation by optimizing rendered images with a pretrained diffusion prior, but latent SDS often produces structured color artifacts and high-frequency texture noise. We identify a failure mode of latent SDS caused by VAE-induced pixel drift: the optimized image can move along pixel-space directions that are weakly constrained by the VAE encoder, so its latent representation remains clean and semantically meaningful while the image itself accumulates visible artifacts. We support this diagnosis with controlled 2D SDS experiments, VAE-only optimization, and a simplified analysis showing that encoder-like latent objectives can amplify image-space noise when the inverse mapping to pixels is underconstrained. Motivated by this observation, we propose PixSDS, a lightweight VAE-consistent gradient repair method. PixSDS decodes a latent SDS lookahead step and uses the decoded image as a clean direction for pixel-space optimization, reducing motion in VAE-inconsistent directions without retraining the diffusion model, changing the renderer, or replacing the SDS objective. Experiments in 2D optimization and text-to-3D generation show that PixSDS substantially reduces structured artifacts while preserving semantic content. Code is publicly available at this https URL.

---


### 107. [EviReform: Evidence-Guided Query Reformulation for Multi-Hop Graph Retrieval](https://arxiv.org/abs/2608.13006)

**<font color=#1a73e8>作者：</font>** Xinlong Xu, Yoshua Y. Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop retrieval must recover passages that provide sufficient evidence together. An initial passage often resolves an entity or relation implicit in the question, making the missing evidence easier to describe only after retrieval begins. Graph retrieval improves access to related evidence through stored corpus structure, but its retrieval signal is commonly derived from the original question. Complementary evidence must then be reached through stored relations even when an observed passage provides a more direct semantic cue. We introduce EviReform, which separates revising the retrieval request from aggregating evidence in the graph. Retrieved source passages formulate residual queries for the unresolved information need. The original and residual retrieval signals are normalized separately, combined, and propagated between propositions that share entities. On 2WikiMultiHopQA, HotpotQA, and MuSiQue, EviReform exceeds the strongest baseline by up to 5.59 Recall@5 points and 4.50 F1 points. These results show that observed evidence can guide graph retrieval toward the part of a supporting chain left underspecified by the original question. Code is available at this https URL.

---


### 108. [Structure-aware Riemannian Growth Fields for 4D Plant Modeling](https://arxiv.org/abs/2608.13007)

**<font color=#1a73e8>作者：</font>** Meng-Yu Jennifer Kuo, Ryo Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce a novel framework for 4D plant growth modeling that reconstructs the continuous geometric and topological evolution of plants from sparse temporal observations. Existing methods mainly rely on dense registration, yet reliable dense sequences are hard to obtain due to scanning constraints and self-occlusions, leaving these approaches struggling under large temporal gaps where rapid organ emergence violates local rigidity. To overcome this, we bridge these gaps by formulating plant morphogenesis as a continuous procedural process on a structure-aware Riemannian growth field; this jointly models topology evolution and geometric deformation, preserving botanical hierarchies and stable spatio-temporal correspondences across distant timepoints. Our key idea is to ground symbolic growth rules within a continuous geodesic flow, where organ development follows biologically modulated trajectories that preserve structural coherence under topological changes. We further contribute a 10-day dual-species dataset with dense geometric and semantic annotations. Experiments demonstrate that our method accurately tracks individual organ growth over time and significantly outperforms state-of-the-art baselines in both geometric accuracy and correspondence consistency.

---


### 109. [OmniSphinx: Active Mix Networks (Extended Version)](https://arxiv.org/abs/2608.13008)

**<font color=#1a73e8>作者：</font>** Daniel Schadt, Christoph Coijanovic, Shabi Shabani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mix networks are an important tool to implement anonymous communication, which protects not just the content but also the metadata of messages. Over time, various packet formats for mix networks have been proposed, usually with single, specific goals in mind. These formats are incompatible with each other, requiring separate software and infrastructure to be set up. In this paper, we propose a new format, OmniSphinx, which solves this issue. In OmniSphinx, senders embed code in their packets that determines how they must be processed. The resulting active mix network can emulate any other mix format within a single deployment. Our empirical evaluation shows that emulation in OmniSphinx incurs reasonable overhead compared to native execution for typical mix network use cases: For Sphinx, the most compact format, computation time increases by around 90{\mu}s, while headers increase by 33% in size.

---


### 110. [EgoPHI: Estimating Contact and Force from Egocentric Vision](https://arxiv.org/abs/2608.13014)

**<font color=#1a73e8>作者：</font>** Andela Ilic, Rachel Schuchert, Yijing Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding hand-object interaction from egocentric vision is essential for modeling how people physically engage with the surrounding world. Yet reasoning about physically grounded interaction requires estimating the forces acting on hands and objects, beyond localizing contact. We present EgoPHI, the first method that jointly estimates dense contact maps and 3D force distributions on hand and object meshes from a single monocular RGB image and object geometry. To address the lack of scalable ground-truth force annotations, we introduce a physics-based simulation pipeline that augments existing hand-object datasets with dense per-vertex force supervision. EgoPHI then learns dense 3D contact and force on interacting hand and articulated object meshes, extending vision-based force estimation beyond image-space or planar settings. Our evaluation on in-distribution and out-of-distribution benchmarks shows that EgoPHI improves force estimation over existing approaches while generalizing to unseen datasets. To evaluate sim-to-real transfer, we constructed two physical objects that capture dense object contact and force magnitude and used them to record a dataset of interactions from eight participants across diverse touch and grasp types. Our results demonstrate that EgoPHI recovers meaningful 3D contact and force distributions in simulated, out-of-distribution, and real-world settings, advancing egocentric hand-object understanding from contact localization toward physically grounded interaction reasoning.

---


### 111. [Foundations of MT-PDCL: Measure-Theoretic Probabilistic Definite Clause Logic](https://arxiv.org/abs/2608.13018)

**<font color=#1a73e8>作者：</font>** Costin Bădică, Amelia Bădică  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Standard probabilistic logic programming frameworks typically rely on grounding logic programs into discrete propositional representations. This operational requirement restricts exact inference to finite domains and discrete probability distributions. In this paper, we introduce Measure-Theoretic Probabilistic Definite Clause Logic (MT-PDCL), a generalized foundational framework that eliminates this finite-domain restriction. By explicitly defining stochastic variables over bounded index domains and equipping the interpretation space with standard Borel $\sigma$-algebras, MT-PDCL allows logical variables to operate natively over continuous measurable spaces. Building on Continuous Distribution Semantics, MT-PDCL models probabilistic rules as mutually independent causal events. However, rather than aggregating these derivations via finite boolean circuits, declarative entailment is formally defined through exact Lebesgue integration over the continuous measure space. We introduce a continuous immediate consequence operator that unifies the integration of continuous prior distributions with the evaluation of exact continuous observations. We demonstrate that this approach replaces the combinatorial bottleneck of discrete grounding with exact, algebraic, and structurally differentiable inference. While this transition trades discrete combinatorics for the geometric curse of dimensionality, it achieves the expressive power of continuous probabilistic models while preserving the pure declarative syntax of definite clause logic.

---


### 112. [Incremental Evaluation and Training in Relational Deep Learning](https://arxiv.org/abs/2608.13023)

**<font color=#1a73e8>作者：</font>** Jakub Peleška, Gustav Šír  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational Deep Learning (RDL) models multi-tabular databases as temporal heterogeneous graphs to enable end-to-end representation learning. However, prevailing RDL evaluation practices rely on static, single-episode dataset snapshots, overlooking the continuous, time-evolving nature of real-world databases. Consequently, current RDL benchmarks fail to capture how model performance changes as new data accumulates over time. To address this limitation, we introduce an incremental, multi-episode evaluation and training paradigm to assess and improve the temporal robustness and adaptability of state-of-the-art RDL models. Using established large-scale datasets, we examine data evolution and model training dynamics, demonstrating that temporal concept drifts occur in the majority of predictive tasks. We present multiple incremental training regimes for fine-tuning the models and demonstrate that transfer learning is both feasible and highly effective in the RDL setting. Alongside a new temporal evaluation metric that prioritizes near-future accuracy, we show that our incrementally fine-tuned models consistently outperform the standard, expensive, from-scratch trained baselines.

---


### 113. [RGB-D Video Generation for Improving Human-to-Robot Object Handover Prediction](https://arxiv.org/abs/2608.13028)

**<font color=#1a73e8>作者：</font>** Tianyu Sun, Zhoujie Fu, Zihui Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-to-robot (H2R) object handover is a fundamental capability for human-robot collaboration, yet progress is hindered by the scarcity of large-scale, human-centric datasets and the significant sim-to-real gap. To address these challenges, we introduce Hand2Bot, an RGB-D video dataset that provides rich contextual information such as body posture and facial expressions, specifically collected for handover scenarios with real-world noise patterns. We further propose PassGen, a generative pipeline that leverages stable video diffusion and an Intention-Aware Temporal Face Encoder to synthesize realistic handover sequences while ensuring hand-object consistency. To bridge the sim-to-real gap, we implement a morphology-based depth editing strategy that replicates realistic sensor noise found in physical depth maps. Experimental evaluations demonstrate that our framework achieves high intention identification accuracy and low false trigger rates in both ablation studies and real-world deployment on a physical robot platform. Our results confirm that training on PassGen allows for robust zero-shot transfer and earlier intention anticipation compared to traditional hand-centric baselines, effectively enabling socially aware robotic behavior in shared workspaces.

---


### 114. [Spatially-Grounded Text-to-Video Generation via Inference-Time Gradient-Free Optimization](https://arxiv.org/abs/2608.13037)

**<font color=#1a73e8>作者：</font>** Guillaume Jeanneret, Mathis Koroglu, Hugo Caselles-Dupré 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformer Text-to-Video models have achieved remarkable synthesis quality, yet fine-grained spatial controllability remains a significant challenge. While existing training-free methods produce solid overall results in spatially grounded generation, \ie, placing a specific object in a designated location, they rely on gradient-based optimization techniques that incur prohibitive computational overhead, a bottleneck amplified in modern large-scale architectures. To address this limitation, we present Gradient-free Analytical Trajectory Optimization Video Generation (GATO-Vid), a novel training-free and gradient-free approach for precise spatial guidance. Rather than relying on costly backward passes, we introduce an alternative cross-attention score and solve it analytically to obtain an exact, closed-form solution. To use our analytical solution, we propose an on-the-fly injection mechanism tailored to the topological manifold of the transformer's latent space. Our experiments demonstrate that GATO-Vid significantly outperforms existing baselines in localization accuracy while introducing minimal computational overhead.

---


### 115. [On the global feature importance for interpretable and trustworthy heat demand forecasting](https://arxiv.org/abs/2608.13039)

**<font color=#1a73e8>作者：</font>** Milan Zdravković  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The paper introduces the ante-hoc Explainable AI methodology to assess the global feature importance of the Machine Learning models used for heat demand forecasting in intelligent control of District Heating Systems, with motivation to facilitate their interpretability and trustworthiness, hence addressing the challenges related to adherence to communal standards, customer satisfaction and liability risks. Methodology includes use of four different approaches, namely intrinsic interpretability of Gradient Boosting method and selected post-hoc methods, namely Partial Dependence, Accumulated Local Effects and SHAP. None of the selected methods assume feature permutation or perturbations which can introduce bias due to introduction of random unrealistic values of data instances. Discussion of results is provided, including the assessment of complementarities where applicable, with specific interpretations in context of the district heating processes.

---


### 116. [InSPECtor: Improving SLEIGH Processor Specification Veracity via Proxy](https://arxiv.org/abs/2608.13042)

**<font color=#1a73e8>作者：</font>** Michael Chesser, Paul Quirk, Douglas Cooke 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Processor specifications underpin critical security and program- analysis tools such as disassemblers, decompilers, and emulators, yet, their correctness is rarely examined. Errors in specifications distort program behaviour, obscure vulnerabilities, and enable analysis-evasion techniques. Validating processor specifications is a non-trivial task. Our study is a significant undertaking to enable, for the first time, the systematic validation of open-source SLEIGH language specifications, predominantly used by Ghidra. We design and implement a testing framework based on an automated oracle validation strategy by proxy. Our approach leverages the structure encoded in a specification itself to enumerate decodable instruction forms and generate targeted initial states. Then differentially test the successful decoding and emulation of those instructions by comparing emulators exercising the processor specification against hardware references.
Applying InSPECtor across diverse, open-source specifications---x86-64, AArch64, ARM/Thumb, RISC-V, MSP430---embedding differences in specification styles, author preferences, and instruction set architecture designs, we uncovered over 38,920 discrepancies that led to 125 unique bugs with proposed fixes, identifying decoding and semantic defects as well as cross-vendor inconsistencies. We distill our findings into 8 concrete recommendations to drive future improvements. Our work underscores the importance of specification correctness and provides a practical tool to substantially improve the fidelity of SLEIGH processor specifications, strengthening the reliability of downstream security and analysis tools.

---


### 117. [From Local Mismatch to Global Impact: Optimizing Cache Reuse Policy for Efficient Diffusion](https://arxiv.org/abs/2608.13043)

**<font color=#1a73e8>作者：</font>** Xichen Ye, Yifan Wu, Zhikang Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved dominant performance in visual generation but suffer from substantial inference overhead. While cache-based acceleration has emerged as a promising solution, existing policies rely on local similarity heuristics, which we identify as being significantly misaligned with final generation quality. This discrepancy stems from the non-uniform propagation and accumulation of errors along the denoising trajectory. To address this, we propose Global-Impact Cache (GCache). We first establish a rigorous theoretical characterization of the error propagation upper bound. Recognizing that this bound can be overly conservative for complex, highly non-convex diffusion models, we further reparameterize the propagation exponent with a Bernstein form and reformulate cache policy search as a bilevel optimization problem. In detail, GCache identifies an optimal reuse policy in the inner objective while aligning the error-weighting function with generation quality loss in the outer objective. This framework effectively reconciles theoretical rigor with empirical performance, learning to prioritize computation where it most impacts visual fidelity. Extensive experiments demonstrate that GCache consistently outperforms prior caching strategies on both video and image generation. Notably, on the state-of-the-art Wan2.1 video diffusion model, GCache maintains a 2.17x speedup while significantly enhancing generation quality, reducing LPIPS from 0.1095 to 0.0316.

---


### 118. [P2Fusion: Prompt-based Progressive Infrared-Visible Image Fusion via Dual-Prior Distillation](https://arxiv.org/abs/2608.13045)

**<font color=#1a73e8>作者：</font>** Yi Shi, Huichao Xie, Yuqing Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared-visible image fusion (IVIF) is pivotal for multimodal perception, yet reconciling the inherent information disparity between thermal and textural features remains a fundamental challenge. Existing prior-guided methods often rely on static constraints that induce optimization conflicts or utilize extrinsic semantic priors from large-scale foundation models (e.g., CLIP/DINO), which frequently fail to exploit the intrinsic modality characteristics essential for high-fidelity fusion. To address these issues, we propose P2Fusion, a prior-guided distillation-based framework that reformulates IVIF via dual intrinsic prompts. Instead of imposing hard-coded penalties, we distill image-intrinsic priors, thermal saliency and spatial quality, into learnable dynamic regulators. Specifically, a Teach-to-Fuse mechanism provides dual-granularity progressive guidance, coupled with a Gated Dynamic Expert Recalibration (GDER) module for decoupled feature refinement. This design enables the network to adaptively mediate modal competition through expert specialization. Extensive experiments demonstrate that P2Fusion achieves state-of-the-art performance across five mainstream datasets. Notably, our framework demonstrates consistent performance advantages in fusion quality, achieving state-of-the-art results in 14 out of 20 key evaluation metrics across 5 benchmarks. Furthermore, it effectively contributes to the robustness of downstream perception, such as +3.2% mAP on MSRS, +0.5% mAP on M3FD and +0.9% mAP on DroneVehicle for object detection. Our code will be available at this https URL

---


### 119. [BoardroomAI: Dependency-Aware Human-Steerable Multi-Agent Deliberation through Evolving Decision Graphs](https://arxiv.org/abs/2608.13046)

**<font color=#1a73e8>作者：</font>** Sanjeev Manivannan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizational decisions are co-created while evidence, constraints, and human priorities continue to evolve. In conventional transcript-based multi-agent systems, humans typically provide an initial problem, agents deliberate internally, and the system returns a final response. BoardroomAI instead treats the human as a persistent participant who can intervene by challenging assumptions, modifying constraints, changing priorities, introducing evidence, or redirecting the decision process. We operationalize this human--agent coexistence through four components: (i) a typed decision graph representing evidence, assumptions, constraints, claims, objections, alternatives, risks, decisions, semantic dependencies, and specialist responsibility; (ii) an intervention compiler that converts confirmed human actions into explicit graph updates; (iii) dependency-aware propagation that identifies affected subgraphs, preserves unaffected artifacts, and selectively reactivates relevant specialists; and (iv) an evaluation framework measuring intervention impact, repair coverage, preservation, recomputation, and decision validity. Across 600 generated decision-DAG interventions, propagation matched exhaustive impact computation while inspecting only 14.59% of nodes. In a 12-case exploratory pilot, selective repair recomputed 62.11% of canonical nodes, preserved all gold-unaffected nodes, and produced valid updated decisions in six cases while abstaining in the remaining six. These abstentions show that correct intervention routing may still provide insufficient context for synthesis, motivating a \emph{decision-sufficient context closure} for human-steered multi-agent deliberation. All results are synthetic and prototype-level.

---


### 120. [Topology-Unified 2D Pose Estimation across Intact, Residual and Prosthetic Limbs](https://arxiv.org/abs/2608.13047)

**<font color=#1a73e8>作者：</font>** Tianye Qi, Tengyue Zhang, Jiaying Ying 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driven by the availability of large-scale datasets, Human Pose Estimation (HPE) plays a critical role in numerous downstream tasks. However, mainstream benchmarks exhibit severe representation bias, predominantly featuring able-bodied individuals. While a few pioneering datasets have attempted to address limb differences, their annotation protocols fail to generalize, struggling to represent specialized mechanical structures like running blades or unprosthetized residual limbs. To bridge this gap, we introduce ProPose, a large-scale benchmark featuring a novel annotation protocol that unifies the topological representation of biological limbs, diverse prostheses, and physical absences within a single framework. Because real-world prosthetic images are inherently scarce and exhibit extreme long-tail distributions, we design a Real-to-Synthetic data expansion pipeline to explicitly synthesize and expand the underrepresented cases. However, simply training existing models on this enriched dataset often leads to suboptimal solutions, as they estimate each keypoint independently and might hallucinate non-existent joints on mechanical structures. To resolve this, we propose ProLoss, a structure-aware objective that enforces keypoint dependencies within a single limb to prevent unrealistic limb predictions. Extensive experiments demonstrate that our approach improves the classification accuracy of long-tail prosthetic joints by 2% to 6% without compromising spatial coordinate localization performance. This work sets a foundation for inclusive pose estimation, unlocking new possibilities for understanding the interactions between human bodies and assistive devices.

---


### 121. [Tracing Methamphetamine abuse in under-treatment drivers: How biomechanical and oculomotor features help detect at-risk drivers?](https://arxiv.org/abs/2608.13054)

**<font color=#1a73e8>作者：</font>** Hamed Salmanzadeh, Alireza Mortezapour, Iman Tahbazzadeh Moghaddam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While the detrimental impacts of driving under the influence of stimulants such as methamphetamine are well-documented, the driving performance of individuals currently under-treatment has received considerably less attention. This study compared the behavior of individuals with a history of stimulant abuse (across two distinct treatment phases) with a control group of healthy drivers using a driving simulator. Oculomotor and biomechanical data were continuously collected via an eye-tracker and a Kinect sensor, respectively. These parameters were utilized to train a K-Nearest Neighbors (KNN) classification model designed to detect high-risk behavioral patterns in drivers undergoing methamphetamine rehabilitation. Through the evaluation of various feature combinations and neighborhood configurations, the optimized model successfully discriminated between normal drivers and those with a history of abuse with an accuracy of 90%. Detecting at-risk drivers through technologies embedded in Advanced Driver Assistance Systems (ADAS) by continuously monitoring physiological and behavioral parameters, facilitates a proactive safety strategy. Issuing real-time alerts to the driver, passengers, and external monitoring networks can ultimately mitigate the risk of traffic collisions.

---


### 122. [Uniform Herding: Exemplar Replay with Representation Refresh](https://arxiv.org/abs/2608.13061)

**<font color=#1a73e8>作者：</font>** Krishna Subedi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the feature representation changes, replay must preserve the earlier classes. However, only a bounded active exemplar set can be replayed. We propose Uniform Herding, which allocates the current active set across observed classes and uses a bounded candidate pool to refresh their chosen exemplars in the current representation. On CIFAR-100 with ten class-incremental tasks, a ResNet-18 backbone, active budget $M=2{,}000$, retrieval budget $b=64$, and three seeds, Uniform Herding obtains $44.00\pm0.51\%$ final average accuracy and $17.22\pm0.43\%$ forgetting, compared with $42.33\pm1.20\%$ and $24.87\pm1.11\%$ for iCaRL. Within the Uniform Herding protocol, final accuracy decreased when NME or herding was replaced with the tested alternatives, while forgetting increased when distillation was removed. Changing the retrieval budget has a smaller effect across the tested range than changing the active budget. The comparison with iCaRL is end-to-end. It does not isolate the effect of refresh from the other protocol differences. These results are limited to the tested protocol.

---


### 123. [Learning Unified Video and Image Representation for Video Face Forgery Detection](https://arxiv.org/abs/2608.13064)

**<font color=#1a73e8>作者：</font>** Haotian Liu, Yang Liu, Guoying Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face forgery detection is crucial for preserving the security and integrity of facial data given the rapid developments in face manipulation techniques and deep generative models. Existing methods for video face forgery detection typically assume that all frames in a forged video are manipulated, while detecting partially forged videos that contain only a subset of altered frames remains challenging. To address this issue, we propose a novel framework, UVIF, that utilizes additional annotated images to provide fine-grained supervision for detecting partial forgeries in videos. UVIF employs a unified encoder and a multi-task learning paradigm to jointly model facial videos and images for boosted video face forgery detection. A 2D backbone with temporal fusion modules is employed as the unified encoder. A pseudo labeling process is designed for video frames to bridge their representations with those of static images. A video-oriented feature alignment strategy is further introduced to reduce the distribution gap between videos and images. Extensive experiments on benchmark datasets demonstrate the effectiveness of our framework, which outperforms state-of-theart methods in detecting partially forged videos while introducing no additional computational overhead. Our code is available at this https URL.

---


### 124. [A Multispectral Framework for the Detection of Calcium Carbide-Induced Ripening and Shelf-Life Estimation in Climacteric Fruits](https://arxiv.org/abs/2608.13073)

**<font color=#1a73e8>作者：</font>** Gurbhit Chaurakoti, Harshit Kumar, Hani Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Significant health risks are associated with the illegal, yet commonly practiced use of industrial-grade Calcium Carbide (CaC2) for ripening climacteric fruits like mango and banana, which leaves behind trace residues of arsenic and phosphorus. To address this, the proposed study explores a novel, non-invasive multispectral framework for distinguishing safely ripened fruits (naturally ripened and ethephon-induced) from calcium carbide-ripened samples, while also estimating their ripening progression (in percentage) and remaining shelf life (in days). The spectral profiles of mango (Mangifera indica) and banana (Musa acuminata) at 18 discrete wavelengths in the visible-near infrared (NIR) range (410 nm - 940 nm) are studied using the AS7265x spectral triad sensor. CaC2-treated samples exhibit sharper spectral intensity drops in the visible region, consistent with accelerated chlorophyll degradation and carotenoid development. To characterize these physiological changes, the feature engineering strategy integrates inter-method spectral variance, intensity ratios at distinct wavelengths, and environmental parameters including temperature and humidity. Dimensionality reduction using Principal Component Analysis (PCA) retains >90% of spectral variance within the first 5-7 components. The resulting feature set is used to train three independent eXtreme Gradient Boosting (XGBoost)-based learning algorithms for ripening method classification, along with quantitative estimation of remaining shelf life and ripening progression. A classification accuracy of 95% along with carbide class recall of 0.67 is observed for mango samples, while the model achieves an accuracy of 81% and carbide class recall of 0.74 for banana. This instrumentation and data-driven approach demonstrates the effectiveness of the proposed non-invasive framework.

---


### 125. [Learning Discrete Decisions for MIPs with Constraint-Aware Diffusion](https://arxiv.org/abs/2608.13079)

**<font color=#1a73e8>作者：</font>** Vincenzo Di Vito, Mehdi Taghizadeh, Deepjyoti Deka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a novel learning-based approach to approximately solve instances of mixed-integer optimization problems. These problems are computationally challenging, as they require jointly determining discrete and continuous decisions while satisfying complex combinatorial constraints. The proposed method relies on a graph-based generative diffusion model that learns the discrete component of mixed-integer optimization problems while integrating a training-free feasibility projection operator directly into the reverse diffusion process to steer intermediate samples toward the feasible set throughout generation. Once the discrete decisions are generated, the remaining optimization reduces to a continuous problem that can be solved efficiently (relative to the original problem) using existing numerical methods. The resulting framework named Constrained Graph Diffusion (CGD), is problem-agnostic and can accommodate a broad class of mixed-integer optimization problems through suitable projection operators. We evaluate CGD on optimal transmission switching for ACOPF and discrete portfolio optimization, demonstrating substantial improvements in feasibility and solution quality over learning-based baselines while achieving speedups of up to $425\times$ over state-of-the-art numerical solvers for MINLPs.

---


### 126. [Sampling Luck Masquerades as Allocation Gain: Auditing Test-Time Budget Allocation for Neural Combinatorial Optimization](https://arxiv.org/abs/2608.13087)

**<font color=#1a73e8>作者：</font>** Jinhyung Bae  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural combinatorial optimization (NCO) solvers report the best of many sampled solutions per instance, and the sample count is, by convention, identical for every instance. Whether a non-uniform allocation of a fixed total budget would buy anything has not been measured. We measure it, and we audit the measurement itself.
First, on in-distribution workloads the allocation headroom is not detectable. Across three pretrained solvers (POMO, AM, SymNCO) on uniform TSP-100, an oracle allocation computed and evaluated on the same stored samples reports a 2.2-2.6% gain with intervals excluding zero; measured out of sample the same gain is indistinguishable from zero (0.457, 0.015, -0.512 percent). Following the customary in-sample procedure, all three solvers would have supported a published 2%-level gain that does not exist. We calibrate this bias against an instance-wise null in which the true gain is zero by construction; over the ranges we test it does not shrink with more samples or more instances.
Second, the same correction that removes the phantom gains preserves a real one. Under distribution shift (a workload mixing uniform and clustered instances), a pre-registered confirmatory experiment finds that allocation guided by held-out sample statistics improves best-of-k by 11.5% (AM, primary endpoint; 95% CI [7.4, 19.7]) and 12.0% (SymNCO, replication) at equal evaluation budget, with the signal-acquisition cost not charged; a pre-registered negative control (POMO, an order of magnitude more robust to shift) shows -0.3% [-0.7, 0.24]. The gain exceeds a frozen distribution-label baseline by 4.2 points [1.9, 7.7]. An exploratory policy charging a 20-sample probe against the same budget retains 3.4% (AM) and 4.6% (SymNCO).
We give a correction procedure and a reporting checklist, and release all data, code, and the pre-registration record.

---


### 127. [Paths: Prompt-aware Spatio-temporal Transformer with Hierarchical Multi-modal Fusion for RGB-Event Video Person Re-Identification](https://arxiv.org/abs/2608.13092)

**<font color=#1a73e8>作者：</font>** Yakun Huo, Yingquan Wang, Yangyang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-Event Video Person Re-Identification (RE-VReID) aims to retrieve specific person across non-overlapping cameras with complementary RGB videos and event streams. However, existing methods often decouple spatial and temporal modeling, which limits their interaction. In addition, global-level RGB-Event fusion fails to fully exploit fine-grained discriminative cues. To address these issues, we propose Paths, a unified framework with spatio-temporal modeling and hierarchical multi-modal fusion for RE-VReID. Specifically, we first design a Memory-Augmented Backbone (MAB) to maintain modality-specific identity prototypes for stable intra-modal representation learning. Then, we propose a Prompt-aware Spatio-temporal Transformer (PST) to jointly model spatial and temporal cues within a unified Transformer. Finally, we introduce a Hierarchical Multi-modal Fusion (HMF) to integrate RGB and event features at global and local levels. With these modules, our framework can learn robust and discriminative representations for RE-VReID. Extensive experiments on three public RE-VReID benchmarks including EvReID, MARS and iLIDS-VID, demonstrate the effectiveness of our proposed method. The code is available at this https URL.

---


### 128. [FlowLOB: Efficient and Controllable Limit Order Book Generation with Flow Matching](https://arxiv.org/abs/2608.13096)

**<font color=#1a73e8>作者：</font>** Zhuohan Wang, Andreea Bacalum, Ollie Olby 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Limit order book (LOB) simulators are most useful to practitioners when they combine realistic market dynamics, computationally efficient sampling, controllable scenario generation, and the ability to generalize beyond the instruments seen during training---properties that existing agent-based and deep generative simulators provide only partially. We present \textbf{FlowLOB}, a conditional \textbf{flow}-matching generator of \textbf{LOB} trajectories, trained on multiple Hong Kong Exchange (HKEX) symbols at three sampling frequencies ($0.1$s, $1$s, $10$s) in tick-relative representation that transfers to unseen instruments. Because flow and diffusion models admit a common formulation, we train both with identical data, architecture, and budget, and sample both through the same fixed-step ODE solvers, yielding a controlled comparison of sampling efficiency and fidelity. Flow matching attains its best quality with only $10$ ODE-solver steps, whereas diffusion needs many more function evaluations to approach the same fidelity. At this efficient operating point, FlowLOB improves realism over baselines, two learned and two agent-based models, in most distributional metrics at the two finer sampling frequencies. We evaluate counterfactual controllability with a distributional test that asks whether changing a scenario condition moves the generated statistic toward the corresponding real tail regime; FlowLOB satisfies this criterion in most tested settings. Both realism and control effects transfer zero-shot on a held-out symbol. We additionally conduct ablation studies on the network architecture and the learning rate.

---


### 129. [Multi-Layer Context Camouflaging: A Semantic Superposition and Contextual Lamination Framework for Malpractice-Resilient Online Assessment](https://arxiv.org/abs/2608.13100)

**<font color=#1a73e8>作者：</font>** Gupta Lovi Raj, Kaur Kamalpreet, Dama Sri Ram 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contemporary online assessment systems rely primarily on browser lockdown, webcam monitoring, and behavioural analytics, yet remain vulnerable to attacks that extract the assessment content itself through screenshots, screen sharing, optical character recognition, and automated scraping. This paper extends the Multi-dimensional Spatio-Temporal Context Camouflaging Model (MSCCM) within the MARS (Multi-modal Assessment Resilience Suite) by introducing the Multi-Layer Context Camouflaging Theory (MCCT), a mathematical framework that protects rendered assessment content through semantic superposition. Authentic assessment content and synthetically generated camouflage are represented as a unified rendering while remaining recoverable only by legitimate candidates. The framework models the adversarial extraction process through an explicit extraction-channel operator and develops six coupled constructs: the Context Inversion Operator, Contextual Lamination Operator, Separation Channel, Human Readability Functional, Computational Ambiguity Functional, and Context Camouflage Tensor. Computational ambiguity is formulated using conditional entropy, yielding a closed-form expression that quantifies uncertainty during unauthorized extraction, while legitimate recovery is guaranteed through an exact filtering identity. We further establish theoretical properties governing ambiguity, camouflage density, semantic preservation, multi-observation leakage, and temporal multiplexing, and present a rendering algorithm with computational complexity and a pre-registered evaluation protocol. MCCT provides a mathematically rigorous foundation for behaviorally adaptive, accessibility-aware, and computationally resilient digital assessment by securing rendered assessment content while preserving readability for legitimate users.

---


### 130. [RbFT-Net: Rectify-Before-Fuse Temporal Radar Anchors for 4D Radar-Camera Depth Completion](https://arxiv.org/abs/2608.13102)

**<font color=#1a73e8>作者：</font>** Wentao Zhao, Shouxuan Wu, Yongtao Cen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense metric depth prediction from cameras and millimeter-wave radar offers a cost-effective sensing solution for autonomous systems. However, radar measurements are inherently sparse and susceptible to clutter, multipath reflections, and projection errors. While aggregating multiple radar frames provides denser metric cues, it also introduces temporal misalignment and dynamic-object interference. Directly propagating such unreliable measurements can therefore corrupt large regions of the predicted depth map. To address this issue, we propose RbFT-Net, an end-to-end rectify-before-fuse framework for multi-frame 4D radar-camera depth completion. Rather than assuming accumulated radar returns to be accurate, RbFT-Net treats them as noisy temporal anchor candidates. An image-conditioned rectification module jointly corrects their image-plane locations and metric depths while estimating pointwise reliability. The rectified anchors are then selectively propagated before high-level multi-modal fusion, suppressing the influence of unreliable measurements. Experiments on ZJU-4DRadarCam and a newly collected 4D radar-camera-LiDAR dataset show that RbFT-Net consistently outperforms the evaluated independent radar-camera methods and remains competitive with plug-in pipelines using auxiliary monocular depth models. Cross-platform evaluation and component analyses further support the effectiveness of the proposed rectification and reliability-aware propagation strategy.

---


### 131. [Online Learning of Correspondences between Images](https://arxiv.org/abs/2608.13104)

**<font color=#1a73e8>作者：</font>** Michael Felsberg, Fredrik Larsson, Johan Wiklund 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a novel method for iterative learning of point correspondences between image sequences. Points moving on surfaces in 3D space are projected into two images. Given a point in either view, the considered problem is to determine the corresponding location in the other view. The geometry and distortions of the projections are unknown as is the shape of the surface. Given several pairs of point-sets but no access to the 3D scene, correspondence mappings can be found by excessive global optimization or by the fundamental matrix if a perspective projective model is assumed. However, an iterative solution on sequences of point-set pairs with general imaging geometry is preferable. We derive such a method that optimizes the mapping based on Neyman's chi-square divergence between the densities representing the uncertainties of the estimated and the actual locations. The densities are represented as channel vectors computed with a basis function approach. The mapping between these vectors is updated with each new pair of images such that fast convergence and high accuracy are achieved. The resulting algorithm runs in real-time and is superior to state-of-the-art methods in terms of convergence and accuracy in a number of experiments.

---


### 132. [Robust Dempster-Shafer Evidence Fusion with Chaos-Conflict Measurement and Historical-Experience Weighting](https://arxiv.org/abs/2608.13108)

**<font color=#1a73e8>作者：</font>** Huiyu Li, Weibo Liu, Xinru Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-source evidence fusion under Dempster-Shafer theory faces two persistent challenges: existing conflict measures assess inter-evidence inconsistency and intra-evidence uncertainty independently, yielding incomplete evaluations, and current fusion methods evaluate evidence sources exclusively through instantaneous comparisns without exploiting their long-term reliability across diverse decision contexts. This paper proposes a unified evidence reasoning framework that addresses both limitations. Specifically, a chaos-conflict measurement is introduced to jointly quantify cross-evidence conflict and intra-evidence non-specificity, with five formally proven properties ensuring consistent assessment. A historical experience driven weighting scheme partitions the decision space via spectral clustering and applies regret theory to compute context-specific reliability profiles from past fusion outcomes. These mechanisms feed into a hybrid combination rule that adaptively balances uncertainty preservation against weighted consensus, controlled by the global conflict level, followed by a belief-interval decision strategy that enables robust classification without discarding epistemic uncertainty. Experiments on 16 real-world benchmark datasets demonstrate that the proposed framework achieves an average F1 score of 85.78 and a mean AUC of 93.30, outperforming eight DST-based baselines and three gradient boosting methods. Ablation analysis confirms the contribution of each component we proposed. The framework offers an effective approach for adaptive evidence fusion in multi-source decision making.

---


### 133. [Fast Iterative Five point Relative Pose Estimation](https://arxiv.org/abs/2608.13114)

**<font color=#1a73e8>作者：</font>** Johan Hedborg, Michael Felsberg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust estimation of the relative pose between two cameras is a fundamental part of Structure and Motion methods. For calibrated cameras, the five point method together with a robust estimator such as RANSAC gives the best result in most cases. The current state-of-the-art method for solving the relative pose problem from five points is due to Nister [9], because it is faster than other methods and in the RANSAC scheme one can improve precision by increasing the number of iterations. In this paper, we propose a new iterative method, which is based on Powell's Dog Leg algorithm. The new method has the same precision and is approximately twice as fast as Nister's algorithm. The proposed method is easily extended to more than five points while retaining a efficient error metrics. This makes it also very suitable as an refinement step. The proposed algorithm is systematically evaluated on three types of datasets with known ground truth.

---


### 134. [Branch and Bound for Relational Verification of Neural Networks](https://arxiv.org/abs/2608.13118)

**<font color=#1a73e8>作者：</font>** Kota Fukuda, Zhenya Zhang, Guanqin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Verification of neural networks against relational specifications, such as global robustness, is crucial for safety-critical applications of cyber-physical systems (CPS), given their increasing adoption of AI components. Compared to simple trace properties (e.g., local robustness), verifying relational specifications requires reasoning about the relationship between multiple network inferences, which brings significant technical challenges. Existing research has explored abstraction techniques based on sound and convex over-approximation of neural network outputs; however, since these approaches are inherently incomplete and may raise false alarms, they further underscore the need of effective abstraction refinement.
In this paper, we propose a branch-and-bound (BaB) framework to mitigate the issue, which iteratively splits the problem until all sub-problems are verified. Specifically, our BaB framework features splitting of relational neurons rather than individual neurons as prior works do, and as the core of our technique, we devise a relational neuron selection strategy based on the dual formulation of the verification problem, which allows us to efficiently select the (most likely) optimal relational neuron that maximizes the refinement brought by problem splitting. We evaluate SaBRe on 817 verification problems across ACAS Xu, MNIST-F, MNIST-C, CIFAR and GTSRB. The results show that SaBRe outperforms different baseline approaches, in terms of the number of solved instances and verification efficiency, which demonstrates the effectiveness of our proposed techniques.

---


### 135. [Predicting Signed Distance Functions for Visual Instance Segmentation](https://arxiv.org/abs/2608.13135)

**<font color=#1a73e8>作者：</font>** Emil Brissman, Joakim Johnander, Michael Felsberg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual instance segmentation is a challenging problem and becomes even more difficult if objects of interest varies unconstrained in shape. Some objects are well described by a rectangle, however, this is hardly always the case. Consider for instance long, slender objects such as ropes. Anchor-based approaches classify predefined bounding boxes as either negative or positive and thus provide a limited set of shapes that can be handled. Defining anchor-boxes that fit well to all possible shapes leads to an infeasible number of prior boxes. We explore a different approach and propose to train a neural network to compute distance maps along different directions. The network is trained at each pixel to predict the distance to the closest object contour in a given direction. By pooling the distance maps we obtain an approximation to the signed distance function (SDF). The SDF may then be thresholded in order to obtain a foreground-background segmentation. We compare this segmentation to foreground segmentations obtained from the state-of-the-art instance segmentation method YOLACT. On the COCO dataset, our segmentation yields a higher performance in terms of foreground intersection over union (IoU). However, while the distance maps contain information on the individual instances, it is not straightforward to map them to the full instance segmentation. We still believe that this idea is a promising research direction for instance segmentation, as it better captures the different shapes found in the real world.

---


### 136. [A Commitment-Based Hybrid Post-Quantum Cryptographic Model for Multi-File Cloud Storage](https://arxiv.org/abs/2608.13138)

**<font color=#1a73e8>作者：</font>** Lemdi Frank Prikutse, Regina Esi Turkson, Alimatu-Saadia Yussiff 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud storage clients increasingly require authentication that remains secure against future quantum-capable adversaries, motivating hybrid constructions that combine classical primitives with standardized post-quantum alternatives. Extended naively to multi-file upload, such constructions incur a per-file lattice signing cost that dominates authentication time and becomes prohibitive at realistic batch sizes. This paper presents a commitment-based hybrid post-quantum model that addresses this bottleneck. It comprises AES-256-GCM bulk encryption, a hybrid X25519 with ML-KEM-768 key encapsulation mechanism, and a hybrid Ed25519 with ML-DSA-65 dual signature, computed over a SHA3-256 batch commitment. The commitment binds all ciphertexts in a batch to a single fixed-size digest that is signed once, reducing the number of post-quantum signature invocations per batch from n to one, independent of batch size; the remaining encryption and hashing is bounded by fast symmetric throughput. On a commodity client platform, averaged over 20 repetitions, this holds signing-phase time near-constant as the batch grows while the per-file baseline scales linearly. At n = 1000, the model reduces signing-phase time by factors of 629, 606, and 725 for 100 KB, 1 MB, and 10 MB files respectively, against a per-file dual-signing baseline sharing every other primitive.

---


### 137. [MergeOver: Post-Training Token Merging for Recursive Vision Transformers](https://arxiv.org/abs/2608.13141)

**<font color=#1a73e8>作者：</font>** Junseo Kim, Uraz Odyurt, Amirreza Yousefzadeh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) demonstrate exceptional performance in computer vision but suffer from large parameter counts and quadratic computational complexity, severely limiting their deployment on resource-constrained edge hardware. While recursive weight-sharing reduces parameter counts and token merging mitigates computational and memory bottlenecks, integrating these two paradigms without costly retraining is non-trivial, leaving this intersection largely unexplored. We propose MergeOver, a post-training approach that integrates Token Merging (ToMe) into the recursively weight-shared Sliced Recursive Transformer (SReT). Through an Unmerge tracking stack, constraint-safe merge-rate adjustment, and synchronised token-mass tracking across spatial permutations, MergeOver resolves the spatial and merging constraints of this integration. We further employ a stage-wise single-shot schedule that performs token reduction at the first block of each stage and maintains a fixed sequence length throughout its subsequent recursive iterations. Benchmarked on ImageNet-1K, our selected configuration reduces top-1 accuracy by 1.47 percentage points. On the GPU, it reduces peak activation memory by 37.3% and 38.4% at batch sizes 1 and 16, while throughput decreases by 21.7% at batch size 1 but increases by 21.7% at batch size 16. On a Raspberry Pi 5 (ARM CPU), it reduces latency by 2.4% and 17.6% at batch sizes 1 and 16. These results show that MergeOver can recover a meaningful part of the throughput and memory cost that recursive weight-sharing introduces, without retraining, and provides a baseline for combining token merging with hierarchical recursive transformers.

---


### 138. [Geometry-Grounded Unified 3D Perception for Autonomous Driving](https://arxiv.org/abs/2608.13147)

**<font color=#1a73e8>作者：</font>** Longfei Xu, Xiaohui Wang, Zehao Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based autonomous driving perception requires a shared representation that preserves metric 3D structure across synchronized multi-camera streams. However, existing image-based frameworks often rely on backbones pretrained for semantic recognition, and introduce 3D geometry through downstream task-specific modules. As a result, their shared representations may fail to preserve explicit metric geometry and consistent 3D scene structure. In this paper, we present a Geometry-grounded Unified 3D Perception (GeoUP) framework that adapts the reconstruction-oriented latent of VGGT to calibrated, streaming multi-camera driving scenes. GeoUP factorizes cross-image interaction into self, temporal, and view attention to capture structurally distinct temporal and cross-view correspondences. It further injects calibration-aware raymap encodings to provide metric scale and camera geometry. The resulting geometry-grounded latent is decoded for metric depth estimation, 3D object detection, and semantic occupancy prediction, corresponding to surface-, instance-, and volume-level readouts of the same 3D scene. Through joint multi-task and multi-dataset training, GeoUP effectively leverages heterogeneous annotations and generalizes across diverse sensor configurations and perception ranges. Extensive experiments on nuScenes, Argoverse 2, Waymo, KITTI, and DDAD demonstrate that GeoUP achieves SOTA performance across detection, occupancy, and depth estimation. These results validate the effectiveness of geometry-grounded representations for unified 3D driving perception.

---


### 139. [Splat-based Metal Artifact Reduction in Cone-Beam CT via Polychromatic Modeling](https://arxiv.org/abs/2608.13159)

**<font color=#1a73e8>作者：</font>** Kiseok Choi, Inchul Kim, Jaemin Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cone-beam computed tomography (CBCT) enables volumetric reconstruction from X-ray projections, but suffers from severe artifacts--especially beam hardening--when imaging materials with high attenuation such as metals. These artifacts arise from the polychromatic nature of X-rays and are not properly addressed by conventional monochromatic reconstruction algorithms. While recent neural representation-based methods offer improved reconstruction quality, they are computationally expensive and often impractical for deployment. We propose a novel physics-inspired, self-calibrating metal artifact reduction method that efficiently reconstructs 3D CBCT volumes while correcting beam hardening artifacts. Our method integrates a polychromatic X-ray projection model, material-dependent attenuation profiles, and system response modeling into a Gaussian Splatting framework. Unlike prior work, we eliminate the need for manual metal masks or strong prior assumptions, and we optimize both reconstruction parameters and X-ray spectral characteristics jointly during training. We further introduce a high-fidelity synthetic CBCT dataset generation pipeline validated on Monte-Carlo x-ray simulation toolbox and release new datasets with severe metal-induced artifacts to support the community. This is the first splat-based method for reducing beam hardening in CBCT. Extensive experiments on both synthetic and real-world datasets demonstrate that our method outperforms state-of-the-art approaches in artifact suppression and reconstruction accuracy.

---


### 140. [A Controlled Study of Self-Supervised Image and Video Pretraining under Limited Resources](https://arxiv.org/abs/2608.13183)

**<font color=#1a73e8>作者：</font>** Brunó B. Englert, Gijs Dubbelman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual foundation models are a cornerstone of image and video understanding but typically require large amounts of data and computation. The current scale required for pretraining visual foundation models may be unsustainable or unnecessary, and significant benefits arise when effective models can be obtained with fewer resources. To better understand how self-supervised learning (SSL) objectives behave under resource constraints, we conduct a controlled study of image and video SSL objectives under matched data, architecture, and compute budgets. We compare contrastive, reconstruction, feature-prediction, and diffusion objectives and evaluate both standalone and jointly trained image-video SSL formulations across a diverse set of image and video understanding tasks. Our results show that DINOv2-style pretraining consistently provides the strongest overall performance under limited resources. Furthermore, combining DINOv2 with video SSL objectives such as VideoMAE substantially improves image classification and segmentation performance, but degrades video tracking and camera-pose estimation performance, revealing an important tradeoff between semantic and geometric representation learning. These findings suggest that combining image and video SSL objectives can be beneficial in resource-limited settings, while highlighting the need for improved methods that better balance semantic, temporal, and geometric supervision.

---


### 141. [SketchSense: Learning to Interpret Imperfect Sketch Guidance for Image Inpainting](https://arxiv.org/abs/2608.13186)

**<font color=#1a73e8>作者：</font>** Zian Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sketch-guided image inpainting provides intuitive structural control, yet real sketches often mix reliable global intent with locally crowded, displaced, incomplete, or deliberately unconventional strokes. Existing approaches typically either retain the input sketch as a fixed condition throughout denoising or refine it into a clean structure before RGB synthesis. The former assumes uniformly reliable strokes and can propagate local errors throughout generation; the latter must resolve ambiguous structure before emerging appearance and semantic context become available. We propose SketchSense, a framework that interprets imperfect sketch guidance by synchronously denoising interacting RGB and structure streams. Bidirectional Attention Fusion couples appearance generation with structural recovery, producing a refined structure that exposes the model's evolving sketch interpretation. A phrase-level objective aligns the semantic grounding of the two streams. Sketch-Aware Spatial Regulation further adapts sketch use to local generation states by modulating attention and the fusion process, while an optional signed prior injects preserve-versus-correct intent into feature representations and attention behavior. Experiments on natural and structurally complex imagery show substantial gains over existing methods in both restoration quality and structural fidelity.

---


### 142. [ProME: Prototype-Margin Environments with Repair-Aware Selection for Group-Robust Learning](https://arxiv.org/abs/2608.13190)

**<font color=#1a73e8>作者：</font>** Qianqian Wang, Yunshan Li, Dawei Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-robust learning is crucial for maintaining accuracy on rare subpopulations when training-group labels are unavailable. However, existing methods often infer environments from a separate reference model and select representations before fitting the classifier used at deployment, leaving both decisions misaligned with the deployed predictor. In this work, we formulate group robustness without training-group labels as the endogenous environments with repair-aware selection (ERAS) problem, and propose ProME (Prototype-Margin Environments) to align both decisions with the deployed predictor. ProME splits prototype margins at their median to construct approximately balanced environments along the training trajectory, and fits a group-balanced linear head on group-annotated validation data to rank the resulting predictors by validation worst-group accuracy. We theoretically bound the worst risk across the inferred environments for a fixed predictor and partition, showing that this bound transfers to the oracle groups under an explicit alignment condition. Extensive experiments show that prototype margins enrich shortcut-conflicting examples, classifier repair reshapes candidate evaluation, and ProME achieves the highest average worst-group accuracy among the compared methods with the same group-label access.

---


### 143. [Smart Contract Invariants Protect Against Cybercriminals](https://arxiv.org/abs/2608.13191)

**<font color=#1a73e8>作者：</font>** Sofia Bobadilla, Humaira Afrin, Angela Novelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchains are among the most adversarial environments in computing. Billions are stolen by cybercriminals who exploit vulnerabilities. This is an open problem and no concept or technique has proven to really make a difference. In this paper, we claim that the classical notion of program invariant is perhaps the most powerful solution to the problem. We devise anoriginal experimental protocol to 1) study how invariants would have protected against past real-world attacks and 2) whether state-of-the-art automated tools can find them. The experimental toolchain is sophisticated. It is based on INVARIANTEVAL, a benchmark of 28 real Ethereum exploits, each paired with a human-authored invariant that blocks the attack. We validate every invariant with PONDEREPLAY, a replay framework that re-executes transactions in order to prove the correctness and soundness of smart contract invariants. We demonstrate that smart contract invariants block all the cybercriminal attacks in INVARIANTEVAL, fully validated by replaying 108,637 historical transactions. Our large-scale experiments clearly demonstrate that smart contract invariants protect against cybercriminals.

---


### 144. [Fidelity-Constrained Anchoring for Black-Box Denoisers](https://arxiv.org/abs/2608.13194)

**<font color=#1a73e8>作者：</font>** Masaki Satoh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a fidelity-constrained framework that anchors the output of a black-box denoiser to its input without retraining and with little additional computation. The method linearly blends the denoised image with the input and selects the maximum blending factor that satisfies a prescribed local fidelity constraint using Peak Signal-to-Noise Ratio (PSNR) or Structural Similarity Index (SSIM). For PSNR control, a closed-form solution is obtained under a local constant-blending assumption. For SSIM control, we derive a tractable formulation based on inverse SSIM under the same assumption and solve it efficiently using iterative root finding. Experiments on DIV2K images with synthetic Gaussian noise and outputs from Real-ESRGAN and a non-local means denoiser show that the proposed anchoring strategy provides effective fidelity control while balancing denoising performance and statistical naturalness, as measured by the excess kurtosis of residual noise. In particular, SSIM-based anchoring yields more consistent behavior across noise levels than PSNR-based anchoring.

---


### 145. [Beyond Simulated Benchmarks: Evaluating Motion Representations for Fall Detection Under Real-World Data Scarcity](https://arxiv.org/abs/2608.13197)

**<font color=#1a73e8>作者：</font>** Timilehin B. Aderinola, Ilaria D'Ascanio, Luca Palmerini 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Falls are a major health concern for older adults, and wearable sensors have been widely explored for detecting falls and enabling timely intervention. However, real-world falls are extremely rare: collecting 100 of them requires an estimated 100,000 days of monitoring, resulting in severely limited labelled data for training machine learning models. Consequently, many approaches rely on simulated datasets, often reporting high laboratory performance but limited real-world generalisation. We present a systematic evaluation of motion representations for wearable fall detection under real-world data scarcity. Using accelerometer signals, we compare interval-based, kernel-based, symbolic, and foundation model representations. As an interpretable baseline, we additionally investigate a lightweight symbolic representation that converts short motion segments into symbolic sentences augmented with physically-grounded impact descriptors. Experiments use FallAllD, a simulated falls dataset, and FARSEEING, a clinically verified real-world falls dataset. Through cross-validation, controlled data scarcity, and cross-dataset transfer, we examine how representation choices affect robustness under realistic deployment. Our results reveal that highly parameterised kernel and foundation models excel on simulated data but degrade severely under both data scarcity and domain shift. Although the interval-based representation achieves the strongest absolute real-world performance, augmenting a symbolic representation with physically-grounded impact descriptors yields the smallest degradation under domain shift and retains detection sensitivity under extreme scarcity, albeit at lower precision. These findings highlight the importance of evaluating beyond simulated benchmarks and show that representation choice is critical for deployable fall detection given the scarcity of real-world data.

---


### 146. [TANGCO: Learning Topology-Aware Capacity Allocation for Overload-driven Cascading Failures](https://arxiv.org/abs/2608.13212)

**<font color=#1a73e8>作者：</font>** Orkun Irsoy, Leman Akoglu, Osman Yagan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Networked systems, from power grids to traffic networks and cloud clusters, carry loads across nodes with limited capacity. A node whose load exceeds its capacity fails and sheds its load onto its neighbors, which can trigger a system-wide cascade. We study how to allocate a fixed capacity budget across nodes to resist these cascades under local load redistribution. The problem is difficult because no optimal allocation is known, and the fail-or-survive objective is non-differentiable and piecewise constant, so exact and gradient-based optimization methods do not directly apply. We introduce TANGCO (Topology-Aware Neural Graph-Guided Capacity Optimization), which uses a graph neural network policy trained through the cascade simulator with policy-gradient learning and a heuristic anchor. We evaluate TANGCO on five synthetic graph families and five real networks spanning power, road, air, and Internet topologies. The learned policy improves on the best of four hand-designed heuristics in all 450 synthetic instances and in 40 of 45 real-network conditions, with robustness gains ranging from 1.6% to 246%. The learned policies transfer to unseen graphs within a family and partially across related topologies, and TANGCO$^{pre}$, pre-trained on synthetic graphs, matches per-network training on unseen real networks. Training scales near-linearly with graph size, and TANGCO$^{pre}$ allocates on a new network with no per-target training, matching the deployment cost of a hand-designed heuristic. Free-vector variants without the GNN, stay close to the heuristics, so the graph representation carries the gain beyond numerical search. Finally, analysis of the learned allocations identifies when local risk is sufficient, leads to an improved closed-form heuristic, and reveals the regimes where a topology-aware learned policy remains necessary.

---


### 147. [History-informed Lagrangian Neural Networks](https://arxiv.org/abs/2608.13215)

**<font color=#1a73e8>作者：</font>** Tianshuo Zhang, Xianglei Xing, Wenzhe Zhai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting the long-horizon evolution of mechanical systems from position-only observations is a pivotal yet difficult task, as hidden velocities and trajectory-specific physical properties must be inferred simultaneously. Although physics-guided neural networks like Lagrangian Neural Networks (LNNs) guarantee physical plausibility, they generally require complete state inputs and lack adaptability to changing system parameters. To break these limitations, we introduce History-informed Lagrangian Neural Networks (HiLNN). Grounded in the insight that temporal position sequences implicitly encode underlying dynamics, HiLNN employs a recurrent encoder to extract a latent context from history. This context not only reconstructs the unobserved initial velocity but also adaptively modulates the mass matrix, potential energy, and damping coefficients of a structured Lagrangian system. By leveraging a differentiable RK4 rollout scheme, the entire pipeline is optimized end-to-end under multi-step trajectory supervision and energy-consistency regularization. Empirical evaluations across conservative, dissipative, and heterogeneous variable-parameter systems show that HiLNN delivers superior long-term prediction accuracy and maintains precise energy profiles compared to state-of-the-art baselines. The source code is publicly available at this https URL.

---


### 148. [UniCon-Former: Unified Convolution Transformer is All You Need for Hand Gesture Recognition](https://arxiv.org/abs/2608.13217)

**<font color=#1a73e8>作者：</font>** Mallika Garg, Debashis Ghosh, Pyari Mohan Pradhan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional Neural Networks (CNNs) capture local features efficiently but struggle with global context due to their limited receptive field. On the other hand, transformers effectively capture global dependencies through self-attention but suffer from high redundancy and computational costs. Thus, to leverage the advantages of both CNNs and transformers, we propose a unified model (UniCon-Former) that aims to provide robust and efficient performance on dynamic hand gesture recognition. The unified approach helps the model to learn both local and global features. At the beginning of each transformer stage, the convolution projections help in decreasing the dimension of the input vectors of the transformer block. This creates a pyramidal structure at each transformer stage. These features enable the UniCon-Former to reduce resource usage than vanilla transformers, making it flexible for learning multi-scale and high-resolution features, which is required in hand gesture recognition. We have performed experiments with NVGesture and Briareo datasets and achieved state-of-the-art results with fewer parameters and MACs.

---


### 149. [Reliability analysis for BraTS-GoAT segmentation: a controlled robustness study of deep-ensemble uncertainty](https://arxiv.org/abs/2608.13223)

**<font color=#1a73e8>作者：</font>** Riya Deepak Shet, Le Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep networks segment brain tumours accurately in-distribution, but can fail silently when the input differs from their training data. That risk is central to clinical deployment and is the premise of the BraTS-GoAT generalizability task. We ask not only how well a model segments, but whether its uncertainty knows when it is wrong. On BraTS-GoAT (Task 3) we train a 5-fold cross-validated nnU-Net baseline (one held-out prediction per case) and a 3-seed deep ensemble. Both are evaluated for calibration and error detection on a per-region relevant mask, aggregated per case. In-distribution the 3-seed ensemble improves modestly over the already strong single model on the same held-out split, with the clearest gain in calibration. The separation appears under shift. In a controlled robustness study using graded synthetic corruptions as a proxy for acquisition shift, the single model's confidence stays flat while its accuracy and calibration degrade. Inter-member disagreement instead rises steeply, about a quarter to a third above the clean condition, several times the single model's response. On the official validation leaderboard the 5-fold ensemble of those folds attains whole-tumour Dice 0.87. The generalization gap is concentrated on the harder regions, with a characteristic failure of missing small, satellite lesions on unseen cohorts. In the synthetic study, disagreement among the 3-seed members is a more sensitive case-level indicator of acquisition shift than single-model confidence. Its per-voxel error localisation weakens as severity grows. The contribution is a rigorous, honest reliability comparison rather than a claim that any one uncertainty method dominates.

---


### 150. [Knowledge-guided Pattern Discovery via Coupled Tensor Factorizations](https://arxiv.org/abs/2608.13234)

**<font color=#1a73e8>作者：</font>** Gaute Johannessen, Geert Roelof van der Ploeg, Evrim Acar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In order to understand complex systems such as the human metabolome or human brain, different sensing technologies are used, generating complex data. These datasets are often multiway, i.e., with more than two axes of variation such as a subjects by metabolites by time array. While tensor factorizations have successfully revealed interpretable patterns from such complex data, they have so far been mainly data-driven. On the other hand, there is more to data -- there are computational models (of these systems), which are rich sources of prior information. In this paper, we introduce a knowledge-guided approach that brings together data and computational models by jointly analyzing real data and simulated data (generated using a computational model) using coupled tensor factorizations with linear coupling. Our experiments on real metabolomics measurements demonstrate that guiding the analysis of such noisy data with simulated data improves the pattern discovery performance while also revealing potential discrepancies between data and computational models.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-199](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
