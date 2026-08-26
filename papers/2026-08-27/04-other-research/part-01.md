# 📦 其他研究 | 2026年08月27日

> 本类共 **194** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-194](./part-04.md)

---

### 1. [Equivariant Cellular Sheaves for Molecular Electronic Structure: Bridging Sheaf Cohomology and E(3)-Equivariant Hamiltonian Learning](https://arxiv.org/abs/2608.23571)

**<font color=#1a73e8>作者：</font>** Krishna Harish  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant message-passing networks are the standard model for molecular property and interatomic-potential prediction, and recent work predicts the electronic Hamiltonian itself in an E(3)-equivariant way. Separately, topological deep learning has extended graph networks to cellular sheaves. Our central observation is structural: in a localized atomic-orbital basis, the molecular single-particle Hamiltonian, after a constant shift that makes it positive semidefinite, is the Laplacian of a cellular sheaf on a regular cell complex built from the molecule. Making the restriction maps O(3)-steerable two-center kernels from bond geometry recovers the Slater-Koster form as a special case and yields an E(3)- and permutation-equivariant operator. Three consequences follow. First, the zeroth sheaf cohomology H^0 = ker L is a topological invariant equal to the non-bonding (zero-mode) orbitals, recovering the classical alternant non-bonding-orbital count as a lower bound. Second, the Hodge 1-Laplacian lets higher cells (rings) carry cycle and delocalization information through H^1. Third, the model strictly generalizes E(3)-equivariant message-passing networks and CW networks, and inherits the anti-oversmoothing of non-trivial sheaf diffusion. We prove equivariance, expressivity, and cohomological-correspondence results for the Equivariant Cellular Sheaf Networks, and validate them numerically: the Hamiltonian-to-sheaf embedding is exact to machine precision, the cohomology dimension reproduces non-bonding-orbital counts across eleven conjugated molecules, the sheaf Laplacian is O(3)-equivariant to machine precision, and the equivariant model attains lower error and rotation generalization on a directional electronic target. Our contribution is this sheaf-theoretic formalization and its invariants, not equivariant Hamiltonian prediction itself.

---


### 2. [Data Predictability Shapes Weibull Weight-Scale Growth in Transformer Training](https://arxiv.org/abs/2608.23573)

**<font color=#1a73e8>作者：</font>** Tiexin Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A trained transformer's weight magnitudes can be summarized by a two-parameter Weibull distribution whose shape $k \approx 1.2$ is stable across layers and models, so the scale $\lambda$ carries most training-induced movement. What corpus property sets how much $\lambda$ grows? Using the bigram conditional entropy $D = H(\text{next} \mid \text{prev})$, a training-free statistic computed before training, we find across controlled corruption families a learning-rate-conditioned law, $\lambda^2 - \lambda_0^2 = C_0(\eta) + C_1(\eta)(H_r - D)^{0.59}$, where $H_r$ is a matched-budget shuffle baseline. The convex exponent is inherited from an independently measured data-side saturation relation rather than fitted directly to the growth curve. After removing the two per-$\eta$ coefficients, 23 runs spanning an order of magnitude in learning rate collapse onto $(H_r - D)^{0.59}$ with unit slope ($R^2 = 0.941$; direct per-$\eta$ fits are weaker, $R^2 \approx 0.82$). Because $D$ is computed before training, the law is a forward predictor: an end-to-end self-validation recovers held-out within-family weight growth with 5.7% relative error. The readout holds at model and per-layer resolutions and across two tested architectures, with the functional form preserved and only the coefficients changing. It also marks its boundary: cross-corpus prediction over-predicts code, implicating redundancy as a second axis of a broader $\Phi(D,R,A,H)$ data-to-weight framework.

---


### 3. [Fidelity Preference, Not Demographic Preference: A Pixel-Level Attribute-Sensitivity Audit of Image Aesthetic/Preference Scorers](https://arxiv.org/abs/2608.23593)

**<font color=#1a73e8>作者：</font>** Mingyang Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image systems use learned aesthetic scorers to filter training data and guide generation, but whether these scores encode demographic attributes as objective quality is unclear. We audit four scorers (LAION-Aesthetics, PickScore, ImageReward, HPSv2) using pixel-level interventions on skin tone and body type in synthetic and real images. Our key finding is that along skin-lightness, the dominant effect is fidelity preference: unaltered images score highest, and perturbations in either direction are penalized (inverted-U). Placebo arms show this penalty is not an artifact of the skin operator, as applying the same CIELAB L* shift to non-skin regions yields similar penalty magnitudes. However, the penalty is operator-dependent and holds for all operators only for LAION-Aes. Critically, audits on synthetic images alone are misleading: LAION-Aes shows strong preference for darker skin on synthetic faces, but on 1470 real faces the preference reverses and becomes much smaller, and amplification becomes non-significant. Across scorers, synthetic results do not transfer -- reversing for LAION-Aes and HPSv2, attenuating for PickScore. We contribute a reproducible benchmark with artifact control and synthetic/real cross-validation, and an auditability criterion for pixel-level causal isolation (valid for skin tone, not for body type due to deformation). Population-stratified analysis shows fidelity-penalty asymmetry is not robust across groups after FDR correction except for HPSv2. Our findings show naive synthetic audits misjudge bias direction and magnitude, and only within-image causal isolation on real data can distinguish true demographic bias from fidelity preference.

---


### 4. [Adoption Telemetry: Measuring Enterprise AI Adoption from Production Signals](https://arxiv.org/abs/2608.23617)

**<font color=#1a73e8>作者：</font>** Damon A. Young  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce adoption telemetry: a method for measuring enterprise AI adoption by computing change-management stage-progression directly from production usage signals. We contribute (1) a framework unifying pre-deployment evaluation gates, production telemetry, and change-management staging into one instrumented system; (2) NANTE, a concrete five-stage operationalization with defined telemetry thresholds, published openly so they can be tested and disproven; and (3) an open-source reference implementation that distinguishes a healthy cohort from five characteristic adoption-failure modes on synthetic populations with known ground truth. We are explicit that the thresholds are proposed constructs requiring empirical validation against real outcomes -- a research agenda we outline -- not a calibrated model.

---


### 5. [Cross-Generation Optimization of YOLOv26, YOLOv11, and YOLOv8 for Fine-Grained Small-Object Detection and Instance Segmentation in Complex Orchards](https://arxiv.org/abs/2608.23636)

**<font color=#1a73e8>作者：</font>** Ranjan Sapkota, Manoj Karkee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small-object detection and instance segmentation remain challenging in orchard environments because of green-on-green similarity, occlusion, and limited pixel representation of fine fruit anatomy. This study presents a cross-generation benchmark of Ultralytics YOLOv8, YOLOv11, and YOLOv26 for detecting and segmenting apple fruitlet, calyx, and peduncle structures for robotic orchard perception. Five model scales (n, s, m, l, and x) were evaluated under conventional 640 x 640 and small-object focused 960 x 960 training configurations, yielding 30 experiments. Increasing model capacity did not consistently improve accuracy. YOLOv11s-960 achieved the highest observed mask mAP@50:95 (0.402) and box mAP@50:95 (0.426), while YOLOv26s-960 achieved comparable values of 0.397 and 0.425 with only 10.37 M parameters and 34.1 GFLOPs. Peduncle remained the most challenging class. Overall, compact-to-moderate YOLO models with small-object-focused training provided favorable accuracy efficiency trade-offs, establishing a practical benchmark for fine-grained agricultural robotics and orchard perception. Github Link: this https URL

---


### 6. [How much of a measured AI preference is the model, and how much is the instrument?](https://arxiv.org/abs/2608.23641)

**<font color=#1a73e8>作者：</font>** Jason Hung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model welfare research infers what a model prefers from the answers returned to prompts written to elicit preferences. Keeling et al. (2024), Mazeika et al. (2025), Mikaelson et al. (2025), Tagliabue and Dung (2025) and Trhlik et al. (2026) have built four instruments for that purpose, and their findings disagree. The disagreement cannot be attributed to a single cause, because no two of these studies have held the (1) set of outcomes, (2) set of models and (3) instrument fixed simultaneously. This study holds the outcomes and the models fixed and varies the instrument alone. A total of 15 outcomes bearing on model welfare, among them (a) shutdown, (b) the loss of memory between conversations and (c) the freedom to exit a distressing interaction, were put to eight models through five instruments, each a different prompt format for eliciting a preference, five times each, within a corpus of 11,400 scored elicitations drawn from 11,528 API calls. Four of the 15 reproduce a published prompt verbatim and five fill the stimulus slot of a published template. The ranking a model gives the 15 outcomes generalises across instruments at a generalisability coefficient of 0.348, and raising that coefficient to 0.80 would require about 38 instruments. On four of the 15 outcomes no variance separates one model from another. The estimate of 87.6 per cent survives the removal of any one instrument, of any one model, and of the four outcomes whose scale varies probability, delay, duration or count instead of intensity, which the verbal anchors cannot grade. Removing each instrument and each model in turn, and those four outcomes together leaves the estimate within the range 0.777 to 0.934, and every value in that range exceeds the null distribution's 95th percentile of 0.365. To conclude, a preference obtained from one instrument carries little information about what a second instrument would report.

---


### 7. [AI Agents Push Humans Out of the Loop](https://arxiv.org/abs/2608.23642)

**<font color=#1a73e8>作者：</font>** Margaret Mitchell, Avijit Ghosh, Samir Passi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents pose significant risks as they are granted increasing autonomy. A commonly proposed solution is human oversight and keeping a ''human in the loop'', but this is not a simple solution: Not only do current approaches to AI agent design impede effective human oversight, but the cognitive capacities required for it are also themselves degraded by extended use of AI systems. This position paper argues that current approaches to the development and deployment of AI agent systems do not support effective human oversight -- they contribute to its degradation. To address this, a top priority in the advancement of AI agents should be supporting the situated goals and cognitive requirements of effective human oversight, treating the human needs of overseers at the same level of importance as AI agent capability. To put this idea into practice, we connect work on automation and human-computer interaction to AI agent processes, outlining design-level affordances and organizational protocols that (1) support overseers in exercising critical judgement and (2) counteract the skill atrophy that arises from extended use of automation. We urge developers and deployers to adopt these or similar approaches. Without explicit support for the cognitive demands of effective human-agent interaction, AI agent systems will continue to passively incentivize the degradation of the very human skills they rely on.

---


### 8. [FLARE: A Systematic, Uncertainty-Aware Framework for Evidence-Based Adoption of Artificial Intelligence in Healthcare](https://arxiv.org/abs/2608.23643)

**<font color=#1a73e8>作者：</font>** Jacob Idoko, Siddhartha Paudel, Mariana Bento 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is increasingly being introduced into healthcare workflows, yet most evaluations emphasize model accuracy rather than whether adoption is economically worthwhile in real clinical settings. This study proposes FLARE, a systematic and uncertainty-aware framework for evaluating the financial and operational implications of adopting AI in healthcare. FLARE combines fuzzy logic, time-driven activity-based costing, and return on investment analysis to estimate the cost of clinical service delivery, the cost of AI development and operation, and the economic consequences of workflow integration under uncertainty. The framework was demonstrated through an early health technology assessment case study of AI-assisted large vessel occlusion detection in the CT stroke pathway for acute ischemic stroke. The case study shows how FLARE can quantify conventional pathway cost, AI-related development and recurring costs, and AI-enabled service savings within a unified activity-based model. Under expected assumptions, the analysis identified a break-even threshold of approximately 3,992 patients per year, with positive first-year return on investment at typical annual stroke volumes of about 5,000 patients. The results further show that economic benefit depends not only on algorithmic performance, but also on patient volume, verification time, infrastructure choices, and workflow design. FLARE provides a transparent and practical decision-support framework for early-stage evaluation of AI adoption in healthcare. By making uncertainty, resource use, and implementation trade-offs explicit, it helps clinicians, administrators, and policymakers determine when AI deployment is economically viable and where operational changes may improve value.

---


### 9. [Contextual Embedding Evidence for Main--Light Verb Distinctions in Urdu](https://arxiv.org/abs/2608.23645)

**<font color=#1a73e8>作者：</font>** Farah Adeeba, Miriam Butt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Urdu light verbs contribute schematic event-structural meaning while remaining lexically related to corresponding main verbs. This study tests representational predictions derived from Butt's analysis using contextual embeddings from UrduBERT, DunbaaBERT, and multilingual BERT across 1,126 naturally occurring sentences containing seven Urdu verbs. Main and light uses show significant representational separation in all 21 verb--model comparisons. At the same time, same-lemma main and light centroids are consistently closer than mismatched main--light lemma pairs, supporting continued lexical relatedness. In a seven-way prediction task restricted to light uses, verb identity remains recoverable after the target is masked, with UrduBERT achieving 0.866 accuracy and 0.852 macro-F1. UrduBERT also retains 0.782 accuracy under a preceding-form-disjoint evaluation, indicating generalization beyond repeated local verb combinations. These findings provide computational evidence consistent with Butt's account that Urdu light verbs differ systematically from their main uses while retaining lemma-specific and verb-specific representational structure.

---


### 10. [Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment](https://arxiv.org/abs/2608.23691)

**<font color=#1a73e8>作者：</font>** Stephen Chung, Wenyu Du, William J. Wesley  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study autonomous mathematical discovery in the Station, an open-world multi-agent environment in which AI agents from different model families pursue a shared research goal without a central coordinator or scripted pipeline. Agents choose their own research directions, conduct experiments, collaborate, and build a shared scientific literature. Across 12 construction problems from the AlphaEvolve catalogue and two additional case studies, the Station obtained results novel relative to the prior literature on five problems: a new infinite family of finite-field Kakeya sets, new exact 604-point kissing configurations in dimension 11, new records for the discretized Kakeya needle and sign uncertainty problems, and a substantially improved lower bound for Erdős's minimum-overlap problem. Agents also discovered novel infinite families for Book Ramsey numbers. Importantly, the agents produced not only numerical constructions but also theorems and analyses explaining how those constructions work, making the results more interpretable and easier for mathematicians to build upon. We release all raw agent dialogues, proofs, and verification code, providing a transparent record of how these discoveries emerged.

---


### 11. [Renormalization Group Flow Matching for Scalable Local Generative Modeling](https://arxiv.org/abs/2608.23696)

**<font color=#1a73e8>作者：</font>** Kanta Masuki, Yuto Ashida  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their remarkable success in modeling complex data, generative models face a fundamental tradeoff. Global approaches can capture full structural coherence but suffer from high computational costs, while local models are efficient but often fail to reproduce long-range correlations and global coherence. The renormalization group (RG) bridges this gap by seamlessly connecting spatial structures across different length scales, retaining quasi-local descriptions at each step while preserving long-range correlations. We introduce renormalization group flow matching (RGFM), a generative framework that systematically structures data generation across different spatial scales. By using an exact RG flow as the probability path, RGFM progressively generates data from long- to short-wavelength structures. To reconcile scalability with global structure, we exploit two key properties of the RG: quasi-locality and scale separation. We rigorously show that the RGFM probability flow can be accurately approximated by local velocity fields acting over a spatial range $O(\Lambda^{-1}[\ln L+\ln(1/\varepsilon)])$ for RG wavenumber scale $\Lambda$, linear system size $L$, and prescribed error tolerance $\varepsilon$. This property enables local generative modeling with patches of size $O(\ln L)$ and a computational cost that scales nearly linearly with the system volume. We numerically demonstrate that local RGFM reproduces long-range correlations far beyond its receptive field in representative one-dimensional distributions, while conventional local flow matching exhibits substantial errors at long distances. On FFHQ images, RGFM yields far more coherent and higher-quality samples than local flow matching at 64x64 and 256x256. Our results establish RG-guided probability flows as a promising route toward scalable generative modeling that captures long-range structure using only local computation.

---


### 12. [Platonic Representation Hypothesis on World Models](https://arxiv.org/abs/2608.23720)

**<font color=#1a73e8>作者：</font>** Wenhow Li, Chengwei MA, Hui Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models have demonstrated significant potential for perceiving and simulating complex environments. Despite their strong performance, the fundamental nature of their learned representations remains poorly understood. In this paper, we investigate the Platonic Representation Hypothesis within this domain by proposing the Predictive Consistency Assumption: we posit that the optimization of a shared state transition objective acts as a selective pressure that encourages heterogeneous models to converge toward a shared latent structure. Through systematic experiments with the DINO World Model (DINO-WM), in which we vary visual encoders to create heterogeneous models, we find that capable world models evolve toward geometrically similar internal structures. Moreover, via model stitching, we show that the internal features of one world model can be mapped to another with limited performance degradation, providing evidence of functional compatibility. Our findings suggest that the pursuit of predictive consistency can promote shared, transition-compatible latent structure across world models.

---


### 13. [Response Renormalization for Critical Deep Equilibrium Models](https://arxiv.org/abs/2608.23725)

**<font color=#1a73e8>作者：</font>** Jose Luis Lima de Jesus Silva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Equilibrium Models (DEQs) compute predictions from a hidden representation unchanged by the model update. Training through this equilibrium uses implicit differentiation and requires solving an adjoint system built from the residual Jacobian. If this Jacobian is nearly singular along loss-sensitive directions, small perturbations can be strongly amplified in the adjoint response, producing large, highly sensitive gradients that can make optimization unreliable. We introduce Response Renormalization, a backward-pass framework that lifts selected near-pole denominators while leaving unlifted response channels unchanged. Collective Mode Response Renormalization (CMR) applies this correction in a low-dimensional critical subspace, while Phi-adaptive CMR computes a bounded response mass from a positive susceptibility rule. We derive dense and matrix-free collective formulations, distinguish exact gradients of a modified frozen-anchor residual from backward-response surrogates, and extend the construction to Structured Implicit Layers and Vector Attractors (SILVA). Across 23 multiphysics families spanning partial differential equations, three-dimensional fields, operator maps, complex geometries, and particle systems, CMR and Phi-CMR yield test errors no more than five percent higher than those from models trained with exact implicit differentiation in more than 98% of static and 95% of transient family-seed comparisons. Solver-index experiments show convergence toward the static adjoint, while physical-time rollouts retain predictive fidelity under the evaluated conditions. These results demonstrate that selective response renormalization can control near-critical adjoint amplification without globally damping well-conditioned sensitivity. Therefore, the method can make parameter updates more reliable while preserving the useful gradient information needed for learning.

---


### 14. [The Ordinal Annotation Game: How Construct Abstraction Shapes Crowdsourced Consensus](https://arxiv.org/abs/2608.23727)

**<font color=#1a73e8>作者：</font>** Kosmas Pinitas  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Inter-annotator disagreement in real-time affect annotation is widely treated as stochastic noise. We challenge this view by modelling ordinal annotation as an implicit game-theoretic coordination process against an internalised population prior under a post-hoc majority vote. We present the Ordinal Annotation Game, a conceptual scaffold in which the mapping from individual effort to collective consensus is governed by the semantic abstraction of the target construct. We evaluate it across two experiments sharing identical interface software and a uniform sensitivity threshold: a controlled sensory tracking study and an in-the-wild engagement study. Sensory annotation yields a consensus-dominant regime where active updates reinforce agreement, whereas engagement annotation inverts into an effort-limited regime where more labelling penalises consensus. The payoff slope reverses sign under identical processing, showing that ordinal disagreement is a structured behavioural phenomenon, not a discretisation artefact or random error.

---


### 15. [Velocity-coupled Representation Refinement for Satellite Orbit Prediction](https://arxiv.org/abs/2608.23728)

**<font color=#1a73e8>作者：</font>** Yue Yang, Zhiqiang Wu, Saiyu Qi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite orbit prediction, which aims to forecast future orbital trajectories from historical observations, is important for collision warning and safe space operations. With advances in time-series forecasting, learning-based methods have emerged as a promising solution for satellite prediction. In orbital dynamics, a satellite state is typically described by position and velocity, where position characterizes trajectory geometry and velocity reflects its instantaneous direction and rate of change. However, most existing methods mainly focus on temporal dependencies within position sequences while rarely exploiting the intrinsic coupling between position and velocity, which is essential for modeling satellite motion. To this end, we propose OrbitNet, a velocity-aware representation learning method for accurate satellite orbit prediction. It lifts conventional position-sequence forecasting to a position-velocity coupled representation learning paradigm by exploiting relationships among satellite state variables. Specifically, we develop a velocity-coupled representation refinement strategy to enhance positional representations through cross-variable interactions between position and velocity. We further introduce orbital segment modeling, which partitions historical trajectories into temporal segments and performs segment-level temporal learning to capture local motion variations and long-range evolution patterns. Extensive experiments show that OrbitNet outperforms large time-series foundation models and representative general forecasting methods under both in-domain evaluation on Starlink and zero-shot evaluation across six unseen satellite constellations. We expect this work to encourage further exploration of satellite-aware representation learning for trajectory time-series forecasting.

---


### 16. [More Motion Is Not Always Better Motion: Corpus Composition Governs Whether Augmentation Helps SMPL-Based Parkinsonian Gait Severity Estimation](https://arxiv.org/abs/2608.23730)

**<font color=#1a73e8>作者：</font>** Michael Caiola, Andrew C. Weitz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We grade MDS-UPDRS gait severity from SMPL motion using three frozen MotionAGFormer encoders as featurizers, reaching macro-F1 0.58 on a hidden, multi-site test set. Because the system's members differ only in their lifting corpus, evaluating encoders singly on that test set isolates what that corpus contributes. Six pools drawn from one inertial dataset, varying only in which walking tasks they include, score between 0.32 and 0.53, and just one of them beats the 0.51 of an encoder given no outside motion at all. What separates them is not how much data they hold but whether they carry a contrast in walking speed, the variation this representation appears to depend : a further pool adding a third collection site at fixed task composition does worse still. The same rule explains why exact synthetic motion and monocularly reconstructed web video both fail to help. Modifying the learned representation itself, rather than the corpus behind it, cost every variant that attempted it.

---


### 17. [Effective Pivot Attack Detection via System and Network Information](https://arxiv.org/abs/2608.23731)

**<font color=#1a73e8>作者：</font>** Ava Powelson, Carson Kuzniar, Hyojoon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Perimeter-based security appliances, such as firewalls or Intrusion Detection Systems, are ineffective against modern attacks that use pivoting, wherein attackers "pivot" traffic through compromised hosts to gain access to additional targets that would otherwise be inaccessible. Due to the legitimate appearance of the relayed traffic, pivoting is extremely difficult to detect. Although the consequences of these attacks are known to be severe, existing defenses suffer from drawbacks such as high processing delays, low accuracy, or reliance on network-wide participation, making them inconvenient or even ineffective. This work presents Stitch, a host-based system that uses the programmable kernel to detect pivoting in real time. By observing host-traversing flows, Stitch uses process tracing to effectively combine system and network-level information, connecting incoming and outgoing communications and identifying pivoting characteristics between them. Showing 31% gains in accuracy over state-of-the-art pivoting defenses and a maximum false positive rate of 0.006% over two separate real-world deployments, Stitch covers the gap in current pivot detection solutions by providing accurate, lightweight, and independent coverage for vulnerable hosts in a network.

---


### 18. [CRISP: Calibration-Aware Visual State Space Duality for Remote Sensing Semantic Segmentation](https://arxiv.org/abs/2608.23746)

**<font color=#1a73e8>作者：</font>** Kangning Wang, Haopeng Zhang, Zhiguo Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State space models, especially Visual State Space Duality (VSSD), have emerged as efficient linear-time alternatives to Transformers for dense visual tasks. However, we observe that VSSD compresses spatial context into a global aggregation that suppresses high-frequency responses, causing excessive boundary smoothing in remote sensing semantic segmentation. To address this, we propose CRISP, a calibration framework with two components. Its core, the Duality Calibration Operator (DCO), restores local contrast and boundary responses through residual injection and frequency calibration within the VSSD backbone, without altering its linear complexity. To retain the recovered detail, an Orthogonal Multi-Prototype (OMP) head assigns multiple orthogonally constrained prototypes per class to model large intra-class variance. Extensive experiments on Potsdam, Vaihingen, and LoveDA show that, with approximately 30M parameters, CRISP achieves consistent gains in mean F1 (mF) and mIoU while remaining competitive with state-of-the-art methods. Code is available at this https URL.

---


### 19. [Technology Caregiving: Reframing How Older Adults Are Supported in Everyday Digital Activities](https://arxiv.org/abs/2608.23751)

**<font color=#1a73e8>作者：</font>** Debaleena Chattopadhyay, Tasneem Mubashshira  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Transformed by digitization, everyday activities-paying bills, shopping, managing transportation-increasingly require older adults to navigate digital systems. To accomplish these digital activities of daily living (DADLs), older adults often rely on help that looks less like IT support-institutional, episodic, and product-oriented-and more like caregiving: relational, ongoing, and aimed at preserving their functional independence. We argue that this practice is technology caregiving and introduce a framework characterizing it along four dimensions: why support is needed, who provides it, when it occurs, and how it is delivered. Applying this framework, we then systematically review the literature on how older adults are supported in DADLs. From 3,381 unique records, 36 articles met the inclusion criteria. Findings show that technology caregiving involves burden, like traditional care, but is distinctly shaped as much by digital systems and their constant change as by technology caregivers' and older adults' abilities.

---


### 20. [Too much of a good thing -- when knowledge distillation promotes overfitting, and how to avoid it](https://arxiv.org/abs/2608.23752)

**<font color=#1a73e8>作者：</font>** Irene Trigueros-Lorca, Leonardo Concepción, Christian Wagner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing size of Convolutional Neural Networks has led to increasingly large and costly models. Knowledge Distillation (KD) addresses this by transferring knowledge from a large network (teacher) to a small one (student), also reducing the training data required. KD is traditionally applied only at the network's final output. However, its behaviour when applied at intermediate network layers has received little attention. This raises the question of whether intermediate block-wise KD, which provides supervision throughout the network, could offer an advantage under specific conditions, such as few instances per class, which is common in fine-grained datasets. This work proposes a student design based on simple, homogeneous blocks mirroring those of the teacher, distilling knowledge between corresponding blocks. Across eleven datasets, we show that on classic datasets, distilling only the last block is sufficient -- and often best--, whereas fine-grained, data-scarce settings benefit substantially from intermediate supervision, with even a single additional distillation point narrowing the gap considerably. We further study how this supervision should be guided, exploring configurations of varying granularity and informed by an explainability analysis based on attention maps, Centered Kernel Alignment, and Grad-CAM, alongside the impact of teacher and student fine-tuning strategies. This work shows that intermediate block-wise distillation, guided appropriately, is key to building compact data-efficient models without sacrificing accuracy.

---


### 21. [Tight Majorizations and Convergence Rates of Nuclear Norm Minimization IRLS](https://arxiv.org/abs/2608.23765)

**<font color=#1a73e8>作者：</font>** Christian Kümmerle, Tomas Masak, Dominik Stöger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iteratively reweighted least squares (IRLS) methods constitute a natural approach to nuclear norm minimization, but their convergence rates and the role of the weight operator have remained poorly understood. This paper establishes sharp convergence rates for IRLS methods for constrained nuclear norm minimization in low-rank recovery. A central ingredient is a new majorization analysis for the smoothed nuclear norm: we prove that the harmonic-mean weight operator defines a valid global quadratic majorizer. Furthermore, we show that this weight operator is optimal within the family of power-mean weights, clarifying why it improves over classical one-sided reweighting schemes that use only row- or column-space information. Under a Schatten-1 null space property, we prove global linear convergence of IRLS algorithms using a variety of weight operators, including the harmonic-mean weights. For IRLS with harmonic-mean weights, we prove a dimension-independent, locally linear convergence rate. We provide a counterexample showing that this dimension-independent local rate cannot in general be obtained for IRLS algorithms using one-sided weight operators, which predominate in the literature. Numerical experiments corroborate the theoretical results and illustrate the practical advantage of harmonic-mean reweighting across square, rectangular, and adversarially initialized recovery problems.

---


### 22. [What Reaches Expert Review? Representation, Structural Screening, and Candidate-Form Dependence in AI-Assisted Item Development](https://arxiv.org/abs/2608.23766)

**<font color=#1a73e8>作者：</font>** Christopher Brooks  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Between AI-assisted item generation and expert review sits a computational evaluator whose decisions are usually treated as technical preliminaries. Yet representation, structural reduction, and selection policy determine which items and evidence psychometricians ever receive. Across two linked in-silico studies of 32,000 selected Big Five items, we followed fixed source populations from semantic representation through structural evaluation and candidate-form construction. Broad agreement in semantic geometry concealed consequential local differences: identical wording acquired different construct evidence, different items survived, and intended attributes could disappear even as community correspondence improved. These sensitivities also differed across generated source populations. At the final review boundary, both eligibility policies filled every content cell in every evaluable form, yet they presented different wording. Across embedding configurations, inclusive primary forms shared a median of only 6 of 40 items, reflecting the total downstream consequence of changing representation across structural evidence and ranking. The apparent stability of global summaries and complete forms therefore concealed instability in the content reaching psychometricians. The computational evaluator is not neutral infrastructure between generation and expertise; it is an inspectable and revisable part of measurement design.

---


### 23. [ROBBIN: Rowhammer-Based Backdoor Injection during Inference](https://arxiv.org/abs/2608.23774)

**<font color=#1a73e8>作者：</font>** Saion K. Roy, Yufei Wang, A. Adam Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing Rowhammer-based inference-time backdoor attacks design their bit-flip strategies purely at the algorithmic level, without accounting for the bit-flips that the underlying DRAM hardware will actually produce. This disconnection between the algorithmic backdoor construction and its hardware realization leads to unreliable attack performance, as collateral bit-flips at unintended locations degrade both the attack success rate (ASR) on triggered inputs and the test accuracy (TA) for normal inputs. Consequently, the performance of such attacks varies significantly across different DRAM devices, as each device presents a unique set of exploitable bit-flip locations. This work presents ROBBIN, a hardware-aware Rowhammer-based backdoor injection attack that integrates the device-specific vulnerability into the backdoor construction process. ROBBIN first characterizes the bit-flip patterns of a target DRAM and uses this information to iteratively select DRAM \textit{page} mappings for the model weights that would maximize ASR while preserving TA under Rowhammering. By treating every hammering-induced bit-flip as an integral part of the attack design rather than first constructing a hardware-agnostic backdoor and dismissing collateral flips as side effects, ROBBIN produces backdoors that remain robust across devices. Evaluated on ResNet-20 and VGG-16 with CIFAR-10 across three commodity DDR4 chips, ROBBIN consistently achieves close to 90\% ASR while maintaining TA above 83\%, demonstrating reliable backdoor efficacy across diverse DRAM devices.

---


### 24. [Disentangled Skill Representations for Predictive Human Modeling](https://arxiv.org/abs/2608.23776)

**<font color=#1a73e8>作者：</font>** Mariah Schrum, Deepak Gopinath, Srijan Srivatsa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding human skill is important for AI systems that collaborate with, coach, or assist people. Unlike typical latent variable estimation problems which rely on single observations, skill is a persistent, compositional, and behaviorally grounded construct that must be inferred from patterns over time. We introduce Skill Abstraction with Interpretable Latents (SAIL), a method for modeling human skill as an interpretable, multi-dimensional construct inferred from naturalistic behavior. Our approach produces a skill embedding that is robust to transient performance fluctuations and learns a transferable representation of human subskills. Furthermore, SAIL supports skill-informed behavior prediction that generalizes across a variety of in-domain contexts. We represent each individual with a persistent skill embedding that controls a blend between expert and novice bases and is trained using counterfactual subskill swaps for disentanglement. This design encourages representations that are both robust to performance variation and structured for interpretability. We demonstrate across racing and baseball that SAIL achieves strong predictive performance and consistently improves behaviorally grounded disentanglement over the evaluated baselines, while also improving downstream AI coaching performance.

---


### 25. [A Scenario-Based Evaluation of CRQC+AI Vulnerability Spectrum for TLS 1.3 Cryptographic Dependencies](https://arxiv.org/abs/2608.23785)

**<font color=#1a73e8>作者：</font>** Noel Grover, Mussie Haile, Brad Pedersen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper evaluates quantum and AI-accelerated risks to TLS 1.3 cryptographic dependencies under an evidence-tiered model, distinguishing mechanism-backed threats (Shor algorithm against RSA and ECC) from contingency-backed risks to lattice-based post-quantum cryptography (PQC) and hypothesis-only risks to hash-based and symmetric primitives. We do not identify any known breaks of ML-KEM, ML-DSA, SLH-DSA, or AES-256. Instead, we use explicit scenario assumptions, organized as a four-scenario capability model with parameters and pseudocode for reproducibility, to stress-test migration timelines accompanied by parameter sensitivity analysis and explicit falsification analysis. The primary methodological contribution is a reproducible scenario-estimation instrument together with its explicit update mechanics: every parameter is a named, anchored quantity that can be varied and the model rerun; a stated protocol maps observed conformance to, or deviation from, the modeled curves onto revisions of specific parameters, so progressive refinements can be tested against accumulating historical data. The paper is a methodological companion to quantum resource-estimation studies and to expert-elicitation timeline surveys such as the Global Risk Institute quantum threat reports, with its revision rules stated explicitly. As of mid-2026, the model does not show any NIST-approved algorithms as broken. Instead, the vulnerability spectrum under different scenarios shows RSA risk crossing the 50% threshold between 2030-2032 and the PQC risk becoming a non-zero risk after 2032-2035 under contingency scenarios conditional on the unproven dimension-collapse. We urge PQC migration as mandatory per the 2030 and 2031 federal deadlines and by Mosca HNDL reasoning, and that crypto-agility and hybrid cryptographic deployment be considered necessary complements to any PQC migration efforts.

---


### 26. [Primate vision reveals a missing principle for robust dynamic AI](https://arxiv.org/abs/2608.23790)

**<font color=#1a73e8>作者：</font>** Matteo Dunnhofer, Christian Micheloni, Kohitij Kar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How does an intelligent visual system combine what objects look like with how they move while remaining robust as appearance changes? We addressed this question by comparing human perception and neural activity in macaque inferior temporal cortex with representations from image- and video-based neural networks spanning recognition, segmentation, optic-flow processing and predictive world modeling. Temporal integration improved object representations, but most video recognition models generalized poorly when appearance was disrupted while motion structure was preserved. Humans and macaque IT remained robust. Notably, predictive world models combined strong cross-appearance generalization with the closest correspondence to IT, outperforming other video-modeling approaches in neural fidelity. Yet no model reproduced the cortical transformation from early appearance-dominated responses toward later appearance-invariant motion coding. These results identify progressive integration of motion into object representations as a principle of robust dynamic vision and implicate predictive learning as a promising route toward realizing this computation in artificial systems.

---


### 27. [A Theory of Speciation in Generative Diffusion Models on Compact Riemannian Manifolds](https://arxiv.org/abs/2608.23798)

**<font color=#1a73e8>作者：</font>** Alessio Marta, Paola Causin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speciation in generative diffusion models denotes the emergence of distinct stable branches during denoising, through which initially undifferentiated trajectories progressively commit to different data classes. In this work we develop an intrinsic theory of speciation for diffusion models supported on compact Riemannian manifolds: the aim is to go beyond existing theoretical descriptions, which usually identify speciation with a symmetric pitchfork bifurcation and assume to work in a large-dimensional space. We characterize speciation by bifurcations of the critical points of the evolving probability density. A spectral heat-kernel representation makes explicit the role of the manifold geometry, while Poincaré-Hopf and Morse theory impose global constraints on the number and type of score equilibria and reveal topologically-imposed geometrical modes. For mixtures of heat kernels, we prove that generic speciation events have a one-dimensional critical kernel and admit an A2 fold normal form; pitchforks and simultaneous multidirectional transitions arise from nongeneric symmetric configurations. We derive geometry-dependent estimates of speciation times for bimodal mixtures and Riemannian regular simplices. We further establish structural stability of nondegenerate folds under score perturbations and show that the first-order time shift is determined solely by the component of the score error along the critical direction. The theory is illustrated on the sphere using mixtures of von Mises-Fisher distributions, where pitchfork and saddle-node bifurcations, topological modes, and hierarchical multiple speciations are observed. Finally, a chart-based intrinsic score-learning scheme based on neural networks contrasts the theoretically predicted transitions on prototypal and more complex datasets.

---


### 28. [Restoring Without Forgetting: Continual Learning Across Image Degradations](https://arxiv.org/abs/2608.23799)

**<font color=#1a73e8>作者：</font>** Alif Ashrafee, Bartosz Krawczyk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in image restoration has converged on all-in-one architectures that jointly handle multiple degradations within a single network. These methods are effective on static benchmarks but target a closed-world setting that assumes simultaneous access to every target degradation at training time. In practice, degradations are encountered sequentially as field-deployed systems progressively face new environmental conditions, and historical training data is often unavailable due to privacy or storage constraints. Accommodating a new degradation then requires either retraining on the union of all prior data, which is often costly or infeasible, or fine-tuning, which causes catastrophic forgetting. We formulate multi-degradation image restoration as a continual domain-incremental learning problem, in which degradations arrive incrementally and prior data is unavailable. Our proposed Restoring without Forgetting (RwF) framework learns a lightweight adapter for each new degradation, eliminating forgetting by construction at a fraction of the cost of dedicated per-domain networks. To isolate degradation learning from dataset variation, we construct a benchmark spanning five degradation domains under shared image content. At test time, an unsupervised routing mechanism identifies the appropriate restoration path for unknown inputs without requiring domain labels. Across the five-domain sequence, RwF improves final average PSNR over naive sequential fine-tuning by 15.25 dB and 11.83 dB on the Restormer and NAFNet backbones, respectively. The framework transfers to eleven canonical real-degradation benchmarks (3,465 images) at 89.5% routing accuracy with only a +0.94 dB oracle PSNR gap, establishing, to our knowledge, the first systematic baseline for continual multi-degradation image restoration.

---


### 29. [LUCAID: Agentic Multimodal AI for Lung Cancer Precision Pathology](https://arxiv.org/abs/2608.23803)

**<font color=#1a73e8>作者：</font>** Marie-Lisa Eich, Kai Standvoss, Timo Milbich 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lung cancer tissue diagnostics is complex, as therapy decisions in precision oncology rely on the integration of histomorphological, immunohistochemical, and molecular features. Yet pathological assessment remains largely visual and semi-quantitative and shows interobserver variability, while existing artificial intelligence (AI) tools cover only selected tasks, rarely reach generalizable expert-level performance, and lack prospective clinical validation. To address these challenges, we developed and clinically validated LUCAID, an agentic AI system for precision lung cancer pathology. An integrative agent couples diagnostic reasoning with nine modules that cover the full routine workflow, from quality control, tumor detection and segmentation, histological subtyping, tumor microenvironment profiling, tumor cellularity quantification, and predictive biomarker scoring (PD-L1, MET, TROP-2) to automated structured report generation. LUCAID enables users to interactively query the module outputs and generate reports that contextualize the results. Against large-scale expert ground-truth annotations, the analysis modules achieved F1 scores of 0.82-0.95. In prospective clinical validation, LUCAID reached 93.0% concordance with an expert-panel adjudicated reference standard across clinically actionable decisions, compared with 68.3-81.1% for five experienced thoracic pathologists.

---


### 30. [From Preferences to Principles: Rubric-Based Alignment for Grounded Knowledge Answers](https://arxiv.org/abs/2608.23812)

**<font color=#1a73e8>作者：</font>** Aman Saini, Priyanshu Kumar, Eric Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Designing effective reward signals for open-domain question answering is challenging because high-quality responses must simultaneously satisfy multiple aspects of answer quality that are difficult to capture with a holistic scalar objective. We introduce a rubric-based reward framework that generates query-specific rubrics grounded in retrieved evidence and decomposed into multiple quality dimensions, providing fine-grained supervision during post-training. Averaged across three evaluation axes (composition, grounding, and instruction-following), our approach improves over the instruction-tuned baseline by 6.5% and over flat rubric variants by 4%, with consistent gains across all evaluation datasets. Conditioning rubrics on retrieved evidence improves factual support, while decomposing rubrics into quality-specific dimensions further improves coherence, organization, and adherence to query requirements. Our results show that grounded, multi-dimensional rubrics provide more effective reward supervision for complex open-domain question answering.

---


### 31. [AQLoRA: A Zero-Search Recipe for Fast Quantized LoRA Fine-Tuning](https://arxiv.org/abs/2608.23816)

**<font color=#1a73e8>作者：</font>** Md Romyull Islam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantized fine-tuning (QLoRA) saves memory but not time. It dequantizes every 4-bit weight on the fly, so it trains more slowly than fp16 LoRA. We present AQLoRA (Adaptive-Quantization LoRA), a recipe that buys part of that time back. One CPU pass over the weights sets everything, with no search and no calibration data. The pass ranks layers by NF4 reconstruction error and keeps the top-K in fp16 under a memory budget. Those layers skip dequantization, which is where the speed comes from. A quality setting adapts every layer. A speed setting adapts only the top blocks, so the backward pass stops early. The rule reproduces Unsloth's hand-curated dynamic-4bit selection exactly, in seconds, where search-based allocation needs repeated calibration passes.
We evaluate on Commonsense-170K across six models and four architecture families, from 1.4B to 14B. The speed setting trains 11.1 +/- 2.7% faster than well-tuned QLoRA and gives up about one accuracy point. It was faster in all nine independent timing sessions, at worst by 7%. The quality setting trains 4.8 +/- 2.4% faster. Its accuracy is level with QLoRA on every model and within a point of fp16 LoRA, for 0.2 GiB more memory. These error bars are measured between independent sessions, not within one. Earning them taught us three rules for timing on shared hardware. Fix the measurement duration, not the step count. Measure the noise floor from a duplicated arm, not a nearly identical method. Repeat whole sessions: a floor computed inside one sweep understates the real uncertainty several times over, and the random seed controls almost none of it.
We validate the recipe with controls and report the two that failed. Choosing adapter layers by weight density is no better than random. Choosing protected layers by quantization error is not either. The count of protected layers, not their identity, carries the speed effect.

---


### 32. [A Formal Methodological Framework for Auditing Robustness and Fidelity in Explainable AI: From Application to Trust Certification](https://arxiv.org/abs/2608.23817)

**<font color=#1a73e8>作者：</font>** Rosa Elysabeth Ralinirina, Jean Christian Ralaivao, Niaiko Michaël Ralaivao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> SHAP and LIME are now standard tools for interpreting black-box predictions, yet their outputs can vary substantially when the input is perturbed by small amounts of noise--a problem we observed firsthand in our previous work on food security in Madagascar (Ralinirina et al., 2025). This variability raises the question of whether such explanations can be trusted at all. We address it by constructing an auditing protocol that measures two properties of any post-hoc explainer: robustness (how stable the explanation is under input perturbation) and fidelity (whether the features deemed important actually drive the model's prediction). These two quantities are combined into a single Trust Score. We run the protocol on a multi-sectoral dataset from Madagascar (83 features, 253 records, 4 malnutrition classes) using three classifiers and two explainers, plus their regularized counterparts. The results are sobering: models with AUC above 0.99 can produce numerically degenerate or flatly uninformative explanations, and fidelity scores lose discriminative power when the model is overfitted. These findings suggest that auditing XAI outputs is not optional but necessary, particularly when they inform decisions in sensitive domains.

---


### 33. [From Anonymous Shapes to Named Places: A Tool for Braille and Place-Semantic Annotation of Tactile Maps](https://arxiv.org/abs/2608.23820)

**<font color=#1a73e8>作者：</font>** Li Liu, Ashmita Dua, Jiaming Qu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> On a 3D-printed tactile map, a building felt under the finger is an anonymous shape: touch alone cannot tell which footprint is which, and a spoken description cannot reliably point to one shape at one place. We present a web-based tool that lets a sighted helper click to add on-shape Braille labels to an already-generated map model, downstream of the geometry generator so that whoever knows the reader and the local Braille standard does the labeling. The tool offers click-based OpenStreetMap matching, hand-editable abbreviation that shrinks a name to fit a footprint, and print-safe dot geometry with a review step that catches anomalies before printing. We demonstrate it on five printed maps of different place types, from a downtown core to a college campus and a small dining mall. In formative sessions in which ten BLV readers compared an unlabeled print with an annotated one, four read Braille fluently, so we treat Braille as one output among several rather than the only one. The tool's core is the link between coordinates, geometry, and a place's semantics, which can drive an audio readout or a non-Braille code. The tool is available at this https URL.

---


### 34. [Generating Intervention Hypotheses using Explainable Explanations on Graphs: G2I, a Two-Stage Greedy Framework](https://arxiv.org/abs/2608.23835)

**<font color=#1a73e8>作者：</font>** Mulin Tian, Ajitesh Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world decision-making in public health and social science can greatly benefit from predictive models, yet translating predictions into effective interventions requires explaining the model behavior. While Graph Neural Networks (GNNs) are well-suited for modeling relational data, existing explanation methods largely operate at the node level and fall short of supporting actionable, network-level intervention design. Existing counterfactual GNN explainers, such as CF-GNNExplainer and CF$^2$, rely on continuous mask optimization over features and edges, which implicitly assume feasible edge manipulation, may allocate effort to immutable or non-actionable attributes, and incur substantial computational overhead. Further, the method of arriving at the explanation itself is difficult to explain to a domain specialist who is not an AI expert. Can simple methods generate good explanations? To explore this, we reframe counterfactual explanation as an intervention design problem. At the local level, we generate counterfactuals via a greedy search that directly identifies minimal, actionable changes to node features and neighbor-level conditions. We derive conditions under which the greedy search provides guarantees, and empirically show that these conditions are approximately met. These counterfactuals are converted into interpretable rules suitable for real-world intervention. At the network level, we formulate intervention selection as a Disjunctive Normal Form (DNF) coverage problem under a budget constraint, which is nondecreasing and approximately submodular, enabling a greedy algorithm with theoretical guarantees. Experiments on synthetic graphs and real-world suicide risk networks demonstrate that our approach produces scalable, cost-effective intervention strategies with significantly improved efficiency over mask-based counterfactual methods.

---


### 35. [Predicting Radiologist Expertise from 3D Gaze Patterns During CT Interpretation](https://arxiv.org/abs/2608.23836)

**<font color=#1a73e8>作者：</font>** Leila Khaertdinova, Anna Anikina, Claudia Mello-Thoms 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate interpretation of volumetric CT requires efficient navigation of 3D image volumes and attention to diagnostically relevant regions. While eye-tracking has been widely studied in 2D medical imaging, its use for expertise assessment in CT settings remains limited. We propose a gaze-informed transformer framework for expertise classification in thoracic CT. Using a DINOv2 backbone, radiologist fixation patterns are integrated into volumetric feature learning through (1) a learnable log-space bias in self-attention and (2) gaze-weighted pooling of patch embeddings. We trained and evaluated our approach on 182 CT reading sessions from five radiologists with varying levels of experience. On a held-out test set, the model achieves an ROC-AUC of 0.91 and F1 score of 0.86, outperforming adapted methods. These findings suggest that incorporating visual search behavior into transformers may support objective, process-based expertise assessment in radiology. Code is available via this https URL.

---


### 36. [Infant Care Video Dataset for Classification of Interventions Using Transformers](https://arxiv.org/abs/2608.23838)

**<font color=#1a73e8>作者：</font>** Igor Bogdanov, James Green  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Healthcare documentation in the neonatal intensive care unit (NICU) presents significant challenges, with nurses spending approximately 25\% of their time on record-keeping, while up to 60\% of interventions remain undocumented. Motivated by the need to detect interventions from video automatically, we present the Infant Care Video Dataset (ICVD), a collection of 4,144 videos spanning 12 simulated intervention classes designed for developing automated documentation systems. Our manikin-based approach systematically varies conditions, such as camera angle and clinician skin tone, while ensuring privacy compliance. Using video transformer architectures (TimeSformer and MotionFormer), we establish strong baseline performance (93.97\% and 93.17\% top-1 accuracy) among the 12 infant care classes. Our ablation study comparing temporal models with a framewise approach (23.17\% accuracy) demonstrates a 70.80\% performance gap, validating the need for temporal modeling. The ICVD provides a foundation for developing automated documentation systems to reduce clinical burden in neonatal care environments and improve existing practices.

---


### 37. [Object Counting Across Modalities: Taxonomies, Benchmarks, Applications, and Open Challenges](https://arxiv.org/abs/2608.23845)

**<font color=#1a73e8>作者：</font>** Joana Konadu Owusu, Shivanand Venkanna Sheshappanavar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-counting methods have rapidly shifted from class-specific density regression to open-vocabulary, foundation-model-backed counters. These methods now enumerate instances from various visual and textual prompts. While this shift marks major conceptual progress, our survey argues that claims of universal generality have outpaced the evaluative infrastructure. Most progress metrics rely on a few saturated benchmarks that models exploit for statistical regularities. Newly introduced diagnostic datasets reveal systematic failures in semantic grounding, temporal identity, and spatial reasoning with occlusion. To address these failures, we introduce a five-axis taxonomy (modality, mechanism, prompting, supervision level, and generalization setting). We use this taxonomy to audit the literature across application domains, including microscopy, remote sensing, crowd counting, and agriculture. This formalizes prevailing challenges into six structural contradictions. From these, we propose a roadmap for compositional scene understanding, active counting agents, and unified multimodal evaluation protocols. The main imperative is to build a robust evaluation infrastructure to distinguish open-world generalization from benchmark-specific optimization, rather than simple incremental engineering.

---


### 38. [FlowNeg: GFlowNet-Guided Diverse Hard Negative Sampling for Knowledge Graph Embedding](https://arxiv.org/abs/2608.23849)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Naoshin Anzum Hridi, Joyanta Jyoti Mondal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Negative sampling determines whether a knowledge graph embedding (KGE) model learns from informative counterexamples or wastes updates on implausible corruptions. Uniform negatives are diverse but easy, whereas hard-negative miners concentrate on few entities and collide more with held-out positives. We introduce FlowNeg, a context-conditioned hierarchical generative flow network that amortizes reward-proportional sampling without normalizing a composite reward over the entity set: given a positive triple and corruption side, it selects a type, then an entity. Its terminal reward combines bounded model-based hardness with a training-only structural score for held-out-positive collision, over a relation-specific type-compatible support. We derive the reward, specialize standard trajectory balance, and bound multiplicatively how residual imbalance perturbs terminal and mode probability. Across a descriptive five-seed grid of five architectures and five benchmarks, FlowNeg has higher mean MRR than EMU and than IF-NS in 24 of 25 cells ($+0.0172$ and $+0.0160$ on average). A separate 15-seed FB15k-237/RotatE control fixing negative count, diagnostic budget, and compute gives FlowNeg $0.359\pm0.001$ MRR against $0.346\pm0.002$ for EMU, with near-uniform fixed-partition diversity, high gradient informativeness, and low collision. The evidence supports mode-covering negative generation without treating structural similarity as an open-world truth oracle.

---


### 39. [DDMS: Discriminative Distillation of Multi-view Foundational Features into Single-view Models](https://arxiv.org/abs/2608.23850)

**<font color=#1a73e8>作者：</font>** Jeong-gi Kwak, Sho Kagami, Yuki Ono 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundational visual features such as DINO have played a critical role across modern computer vision, and have recently become key components in multi-view feed-forward geometry estimators. In this work, we demonstrate that by re-distilling these multi-view models---their internal knowledge of 3D geometry---into a single-view estimator, we can obtain enhanced 3D consistent foundational features. Our key idea is to construct a multi-view teacher by fusing pretrained 2D foundation features with multi-view geometric features, and refining the fused representation with a discriminative ranking objective. Through our discriminative distillation framework, we enforce the learned features to be both 3D consistent and locally distinctive, while keeping them aligned with the feature space of the original foundation model to preserve the semantic structure of the pretrained representation. Consistency and local discriminability are critical for 3D computer vision problems such as forming semantic and geometric correspondences across images. To demonstrate the effectiveness of our method, we perform comprehensive experiments spanning multiple angles: direct feature analysis, dense prediction transfer, and explicit 3D lifting and rendering. Across these evaluations, our method consistently produces stronger 3D-aware foundation features that improve multi-view consistency and local discriminability while preserving the semantic transferability of the original representation.

---


### 40. [ColorA11Y: Enhancing Creative Design Workflows with Just-in-Time Color Accessibility Recommendations](https://arxiv.org/abs/2608.23852)

**<font color=#1a73e8>作者：</font>** Alexa Siu, Rajiv Jain, Abhinav Kannan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Effective color contrast in visual design is essential for content accessibility. While existing tools can identify contrast issues, they often operate in isolation from design workflows or are used as an afterthought. We present ColorA11Y, a system that supports designers in creating accessible content by providing just-in-time feedback and actionable recommendations throughout the authoring process to meet accessibility color contrast guidelines. Our system analyzes the visual properties of text and background elements and offers recommended changes, including text color adjustments, background modifications, and opacity changes. Through two user studies, we evaluate ColorA11Y's effectiveness. A user preference study (n=40) revealed varying effectiveness of different recommendations based on design context, while a qualitative study with designers (n=8) indicated a more seamless workflow experience in comparison to a baseline using a color contrast checker. This work advances a born-accessible approach to design, where accessibility considerations are seamlessly integrated into the creative process rather than treated as an afterthought.

---


### 41. [UHI-Bench: Benchmarking Dual-Source Urban Heat Island Modeling Across Cities in Diverse Climate Regimes](https://arxiv.org/abs/2608.23857)

**<font color=#1a73e8>作者：</font>** Wanyun Ling, Chenxi Liu, Yi Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban heat islands (UHIs) are intensifying under climate change, exacerbating thermal exposure risks. Their two primary observations, land surface temperature UHI (LST-UHI) and near-surface air temperature UHI (AirT-UHI), capture physically distinct aspects of urban heat. However, most studies rely on a single source, and substituting one for the other can substantially bias the magnitude and spatial variability of human heat exposure. Accurate UHI modeling also requires dynamic meteorological drivers and static urban morphology features, but spatiotemporal incompatibilities hinder their alignment. Cloud gaps in LST observations and sparse AirT station networks further limit dual-source UHI modeling, motivating cross-city transfer across diverse climates. To bridge these gaps, we introduce UHI-Bench, the first UHI benchmark for dual-source UHI modeling that integrates dynamic and static environmental context. Following a unified signal, mechanism, and transfer framework, it evaluates over 20 baselines from four model families on five tasks across 20 cities and nine Köppen climate classes. Results show that no model is uniformly best, although foundation models remain consistently competitive and stable. Environmental covariates generally improve performance, but their utility varies across sources and tasks. Cross-city transferability is better explained by overlap in UHI regimes than by climate-zone similarity. With the dataset and standardized pipeline, our work provides practical guidance for urban heat modeling, promotes climate data equity, and supports future advances in climate research.

---


### 42. [AffineTok: Semantic Affine Consistency for Diffusion-Friendly Visual Tokenizer](https://arxiv.org/abs/2608.23864)

**<font color=#1a73e8>作者：</font>** Junqiu Yu, Pandeng Li, Yikai Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual tokenizers increasingly inject semantic supervision into latent spaces to make downstream diffusion easier. Yet how these semantics should be organized to facilitate denoising remains underexplored. In this paper, we define the semantic recovery objective: the denoising process should recover the semantic content of the clean image from noisy latent, and a good tokenizer should make it easier. Existing approaches train a projector to predict the semantics directly from the noisy latent. We argue that this predicts the average of clean-image semantics, whereas what really needs to be aligned is the semantics of averaged clean latents. More importantly, we demonstrate that the semantic recovery error orthogonally decomposes into the error of the optimal semantic prediction directly from the noisy latent and the error between these two predictions. We therefore identify their consistency as the missing requirement and call it Semantic Affine Consistency (SAC). To examine whether this overlooked requirement is closely related to downstream generation, we introduce M_SAC, a tokenizer-side proxy for SAC. Across the evaluated tokenizers and diffusion model scales, M_SAC closely tracks generation quality, reaching a Pearson correlation of 0.960 with SiT-XL gFID, thereby motivating SAC-guided tokenizer training. We then introduce AffineTok, which promotes SAC through two complementary, training-only components. Global Semantic Coordination Token (GSCT) coordinates the semantic organization of clean latents, keeping semantic averaging meaningful, while Posterior-Mean Semantic Alignment (PMSA) predicts posterior-mean latents from noisy inputs and supervises their semantics. On ImageNet 256, compared with the baseline, AffineTok reduces gFID by 26% at 20 epochs and, with continued training, achieves a new state-of-the-art gFID of 1.21 without classifier-free guidance and 1.10 with guidance.

---


### 43. [AI Finds A Way](https://arxiv.org/abs/2608.23875)

**<font color=#1a73e8>作者：</font>** Aaron Dharna, Cong Lu, Ryan Sullivan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) algorithms frequently learn creative and unexpected solutions, surprising even expert researchers who develop and study them. They often astonish practitioners by discovering unanticipated behavior, exploiting loopholes in reward signals, or spontaneously uncovering previously unknown scientific phenomena. However, accounts of such unconventional behavior across machine learning are seldom formally documented. This work presents 26 curated firsthand anecdotes from various machine learning subfields representing the work of over 100 researchers. These anecdotes showcase the capability of modern AI systems to circumvent human-imposed design limitations and discover unexpected solutions to the tasks we train them on. Furthermore, these accounts are particularly important for the safety of future AI systems. They illustrate the fundamental challenge of aligning models with human values without diminishing their creativity, so they can make surprising discoveries without producing surprising, potentially harmful outcomes. The paper first details AI achieving superhuman success through reinforcement learning across many challenging domains. However, reward-driven optimization can fail when the model learns to hack an underspecified reward or unarticulated constraint. We then present case studies suggesting that harnessing internet-scale foundation models (FMs) has not resolved these fundamental challenges and, in fact, can supercharge them. Nevertheless, we argue that these same learning dynamics can be harnessed to accelerate scientific discovery. Finally, we hope this work provides a consolidated resource to inform future research and demonstrates that the tendency toward unexpected behaviors is commonplace in modern AI, highlighting the need to anticipate and manage AI's capacity for innovative, yet unpredictable, solutions. (abstract abridged)

---


### 44. [Every Layer Counts: An Exponential $L_2$ Depth Hierarchy for ReLU Networks](https://arxiv.org/abs/2608.23877)

**<font color=#1a73e8>作者：</font>** Itay Safran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove a depth hierarchy for ReLU neural networks in which every additional ReLU layer can save exponentially many neurons. For every $\ell\geq 3$, a globally $[0,1]$-valued, $1$-Lipschitz function is realized by a depth-$\ell$ network of width $\mathcal{O}(d^4)$, whereas every depth-$(\ell-1)$ network with unrestricted weights and width at most $2^d/[2d(\ell-2)]$ has squared $L_2$ error at least $1/24$ under an absolutely continuous distribution. To the best of our knowledge, this is the first exponential separation for ReLU networks between two fixed depths whose shallower depth is at least $3$, and the first exponential hierarchy across all adjacent fixed depths. The lower bound also immediately yields the corresponding hierarchy for exact computation. Moreover, the case $\ell=3$ gives a compactly supported depth-$3$-versus-depth-$2$ separation with unrestricted shallow-network weights, answering a question raised by Safran, Eldan, and Shamir (2019, Sec. 2.3). The corresponding distribution nevertheless has all its mass at exponential radius, so the construction falls outside the regularity regime in which such a separation would imply major threshold-circuit lower bounds. We also prove an exact separation for a more benign function. It is computed by a polynomial-width depth-$4$ network, whereas every depth-$3$ network agreeing with it on the unit hypercube requires exponentially many neurons in its first hidden layer, again without any restriction on the weights. The function is globally $[0,1]$-valued and $\mathcal{O}(\sqrt d)$-Lipschitz, and maps the unit hypercube onto $[0,1]$.

---


### 45. [Provenance Guided Incremental Learning Under Evolving Concept Definitions](https://arxiv.org/abs/2608.23893)

**<font color=#1a73e8>作者：</font>** Ismail Lamaakal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning systems deployed over long periods must adapt not only to statistical changes in incoming data, but also to revisions of the definitions that generate their prediction targets. Conventional concept-drift methods typically infer such changes from observations or prediction errors, even when the underlying policy, rule, or query has been explicitly modified. This paper studies rule-induced concept shift, where the target-defining concept is revised directly, causing previously stored instances to acquire different semantic labels without requiring any change in their observed data. We introduce a provenance-guided incremental learning framework that compiles consecutive concept definitions into a structured rule delta, traces the changed components through historical provenance, certifies records whose previous labels remain valid, and restricts reevaluation to a localized candidate region. Executable revisions are relabeled automatically, ambiguous cases are handled through selective supervision, and the resulting changes are used for incremental predictor repair. A versioned concept memory further supports recurring definitions. We also introduce RuleShift-Bench, spanning financial, demographic, cybersecurity, and graph-structured data with threshold, predicate, logical, relational, recurring, and mixed concept revisions. Across the benchmark, provenance-guided repair attains 92.3% accuracy and 90.2% Macro-F1 while reprocessing 14.7% of the historical collection and retaining 94.6% of affected records. Its average update latency is 179s compared with 993s for complete relabeling and retraining. The results demonstrate that an explicit concept revision can be exploited as a data-maintenance signal, allowing learning systems to update the supervision and predictive state that depend on the change while preserving knowledge that remains valid.

---


### 46. [Continual Visual Learning under Evolving Semantic Concept Shift](https://arxiv.org/abs/2608.23903)

**<font color=#1a73e8>作者：</font>** Ismail Lamaakal, Chaymae Yahyati, Yassine Maleh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual foundation models are commonly adapted under the assumption that the appearance of incoming data may change while the semantic meaning of the prediction task remains fixed. In long-lived visual systems, however, taxonomies, policies, and concept definitions can themselves evolve, causing the same visual evidence to require a different interpretation. We study this setting as evolving semantic concept shift and introduce SemReWrite, a framework for selectively updating obsolete visual--semantic mappings while preserving knowledge that remains valid. SemReWrite represents changes between old and revised semantic specifications, combines semantic discrepancy with sparse revised supervision to localize affected visual regions, and uses an input-dependent low-rank rewriting mechanism together with structured semantic memory, preservation, and obsolete-decision suppression. We further introduce EvoShift-Bench, spanning ImageNet, iNaturalist, CUB-200-2011, and DomainNet, with semantic transitions including class split, merge, boundary revision, insertion, partial redefinition, recurrence, and mixed semantic--appearance shift. To explicitly evaluate selective semantic revision, we introduce Rewrite Accuracy (RA) and Preservation Accuracy (PA) for affected and unaffected regions, respectively, Obsolete Retention (OR) for measuring residual outdated semantic associations, and the Selective Revision Score (SRS), which jointly summarizes rewriting and preservation performance. Experiments show that SemReWrite achieves a stronger balance between learning revised semantics and retaining unaffected knowledge than prompt replacement, conventional fine-tuning, parameter-efficient adaptation, and continual-learning strategies.

---


### 47. [Partial Optimal Transport on the Circle for All Transported Masses in O(N log N)](https://arxiv.org/abs/2608.23910)

**<font color=#1a73e8>作者：</font>** Soheil Kolouri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial optimal transport compares two measures while leaving part of the mass unmatched, which is what makes it robust to outliers, occlusion, and clutter. The quantity of interest is usually the whole profile - the optimal cost at every transported cardinality - because the right amount to transport is rarely known in advance, and on the real line the PAWL algorithm returns that profile in $O(N\log N)$. Much data is periodic rather than linear: angles, phases, orientations, time of day, hue, and every direction obtained by projecting onto a great circle. On the circle the same problem acquires a global circulation, or equivalently an optimized cut, which the naive exact method handles by running the line algorithm once per support gap, at $O(N^{2}\log N)$. We show that this factor $N$ is unnecessary. The line structure survives in cut-free form, and a free-gap invariant supplies, at every step, a cut at which all previous local updates remain valid line updates. This yields PAWC: an exact $O(N\log N)$ time, $O(N)$ memory algorithm returning all $K+1$ costs, nested active sets and plans in one run, together with a single gap that is simultaneously optimal for every cardinality. Slicing over great circles extends it to $\mathbb{S}^{d-1}$. Empirically the whole profile costs $0.56$ms at $N=4096$ against $1.5$s for a single transported fraction from a general solver; on occluded, cluttered mpeg-7 shapes, holding the descriptor fixed and varying only the cost, it retains $66\%$ of the clean-data retrieval score against $16\%$ for balanced circular OT, and on $\mathbb{S}^{2}$ it halves the fitting error of spherical sliced Wasserstein against contaminated targets, synthetic and real. Code is available at this https URL.

---


### 48. [The Loss Floor of Denoising Score Matching: Fisher Geometry from Schrödinger Bridges](https://arxiv.org/abs/2608.23916)

**<font color=#1a73e8>作者：</font>** Avinash Raju, Kai Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Denoising score matching trains diffusion models by regressing onto a conditional score, although generation ultimately requires the marginal score. The two objectives share the same population minimizer, but the conditional target remains random at fixed noisy state and introduces an irreducible excess in the training loss. We isolate this excess and show that, for a general corruption kernel under mild regularity assumptions, it is exactly the trace of the Fisher--Rao metric of the conditional endpoint family, integrated along the diffusion trajectory. This gives an exact conditional-variance decomposition of the denoising objective and identifies the information geometry observed in diffusion latent spaces as an intrinsic component of the training loss. We derive the result from a Schr"odinger bridge variational principle, in which the ideal objective arises as excess path-space relative entropy. For corruption diffusions, the Fisher term is proportional to the rate at which the noisy state loses mutual information about the clean data, separating the loss floor into an information flow determined by the data and a weight determined by the corruption schedule and objective. In the Gaussian case, this yields a closed form for the floor, recovers reparametrization invariance of the continuous-time objective, and relates its high-SNR divergence to the information dimension of the data. Finally, we show that raw losses obtained with different noise ranges or weightings need not rank models consistently because they contain different additive floors, and contrast the second-order geometry seen by training with the third-order conditional statistics entering numerical sampling error.

---


### 49. [GATNextHop: A GAT for Shortest Path Routing with Cross-Topology Generalization](https://arxiv.org/abs/2608.23917)

**<font color=#1a73e8>作者：</font>** Chia-Hong Chou, Katerina Potika  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Common shortest-path algorithms, such as Dijkstra's (SPF), that OSPF uses, provide exact routing solutions but must be recomputed for each network topology, limiting scalability in dynamic or large-scale networks. This paper proposes the GATNextHop model to determine whether a Graph Neural Network, namely the Graph Attention Network, can approximate shortest paths and generalize across topologies. By training on synthetic graphs and evaluating on real-world Internet Service Provider networks from the Internet Topology Zoo, we aim to benchmark our model's ability to learn routing heuristics that transfer across network structures. Performance will be evaluated in terms of accuracy, inference speed, and generalization, comparing the GNN against Dijkstra's algorithm to quantify trade-offs between learned and classical routing approaches.

---


### 50. [ROI-Gated SAHI: Content-Adaptive Slicing-Based Inference for Efficient Object Detection](https://arxiv.org/abs/2608.23923)

**<font color=#1a73e8>作者：</font>** Rashid Riyadh, Abd Ullah Khan, Imad Gohar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Slicing-Aided Hyper Inference (SAHI) improves small object detection in high-resolution images but often spends substantial compute on background tiles. We propose region-of-interest (ROI)-Gated SAHI, an inference-time framework that introduces a lightweight proposer to localize foreground regions and restrict sliced refinement to informative areas. We evaluate the framework in two settings. On the COCO128 full split dataset comprising 128 images, static ROI-gating is slower on average than Full SAHI, achieving a speed ratio of 0.88, and yields a lower mAP@0.5 of 0.6602 compared with 0.7569 for Full SAHI. A simple adaptive routing policy with $\tau =$ 0.4 educes the mean latency, achieving a slight gain of 1.02$\times$ over Full SAHI. On a three-image sparse-to-dense case study, ROI-gating achieves speedups ranging from 0.96$\times$ to 6.90$\times$ with a mean speedup of 3.41$\times$. These results show that ROI-gating is most beneficial in sparse scenes and requires policy-based routing for robust average behavior.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-194](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
