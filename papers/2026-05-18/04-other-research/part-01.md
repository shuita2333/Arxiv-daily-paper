# 📦 其他研究 | 2026年05月18日

> 本类共 **337** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-337](./part-07.md)

---

### 1. [Mixed Integer Goal Programming for Personalized Meal Optimization with User-Defined Serving Granularity](https://arxiv.org/abs/2605.13849)

**<font color=#1a73e8>作者：</font>** Francisco Aguilera Moreno  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Determining what to eat to satisfy nutritional requirements is one of the oldest optimization problems in operations research, yet existing formulations have two persistent limitations: continuous variables produce impractical fractional servings (1.7 eggs, 0.37 bananas), and hard nutrient constraints cause infeasibility when targets conflict. A systematic review of 56 diet optimization papers found that none combine integer programming with goal programming to address both issues. We propose Mixed Integer Goal Programming (MIGP) for personalized meal optimization. The formulation uses integer variables for practical serving counts and goal programming deviations for soft nutrient targets, with inverse-target normalization to balance multi-nutrient optimization. Per-food serving granularity allows natural units (one egg, one tablespoon of oil) without post-hoc rounding. We characterize the integrality gap in the goal programming context and identify a deviation absorption property: GP deviation variables buffer the cost of requiring integer servings, making the gap structurally smaller than in hard-constraint MIP. For meals with 15+ foods, the integer solution matches the continuous optimum in every benchmark instance. A computational evaluation across 810 instances (30 USDA foods, 9 configurations, 3 methods) shows MIGP finds strictly better solutions than GP with post-hoc rounding in 66% of cases (never worse) while maintaining 100% feasibility; hard-constraint IP achieves only 48%. Solve times stay under 100 ms for typical meal sizes using the open-source HiGHS solver. The implementation is available as an open-source Python module integrated into an interactive meal planning application.

---


### 2. [A Two-Dimensional Framework for AI Agent Design Patterns: Cognitive Function and Execution Topology](https://arxiv.org/abs/2605.13850)

**<font color=#1a73e8>作者：</font>** Jia Huang, Joey Tianyi Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing frameworks for LLM-based agent architectures describe systems from a single perspective: industry guides (Anthropic, Google, LangChain) focus on execution topology -- how data flows -- while cognitive science surveys focus on cognitive function -- what the agent does. Neither axis alone disambiguates architecturally distinct systems: the same Orchestrator-Workers topology can implement Plan-and-Execute, Hierarchical Delegation, or Adversarial Verification -- three patterns with fundamentally different failure modes and design trade-offs.
We propose a two-dimensional classification that combines (1) a Cognitive Function axis with seven categories (Context Engineering, Memory, Reasoning, Action, Reflection, Collaboration, Governance) and (2) an Execution Topology axis with six structural archetypes (Chain, Route, Parallel, Orchestrate, Loop, Hierarchy). The resulting 7x6 matrix identifies 27 named patterns, 13 with original names. We demonstrate orthogonality through systematic cross-axis analysis, define eight representative patterns in detail, and validate descriptive coverage across four real-world domains (financial lending, legal due diligence, network operations, healthcare triage). Cross-domain analysis yields five empirical laws of pattern selection governing the relationship between environmental constraints (time pressure, action authority, failure cost asymmetry, volume) and architectural choices. The framework provides a principled, framework-neutral, and model-agnostic vocabulary for AI agent architecture design.

---


### 3. [Contrastive Multi-Modal Hypergraph Reasoning for 3D Crowd Mesh Recovery](https://arxiv.org/abs/2605.13854)

**<font color=#1a73e8>作者：</font>** Minghao Sun, Chongyang Xu, Yitao Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-person 3D reconstruction is pivotal for real-world interaction analysis, yet remains challenging due to severe occlusions and depth ambiguity. Current approaches typically rely on single-modality inputs, which inherently lack geometric guidance. Furthermore, these methods often reconstruct subjects in isolation, neglecting the collective group context essential for resolving ambiguities in crowded scenes. To address these limitations, we propose Contrastive Multi-modal Hypergraph Reasoning to synergize semantic, geometric, and pose cues for crowd reconstruction. We first initialize robust node representations by combining RGB features, geometric priors, and occlusion-aware incomplete poses. Additionally, we introduce a pelvis depth indicator as a global spatial anchor, aligning visual features with a metric-scale-agnostic depth ordering. Subsequently, we construct a shared-topology hypergraph that moves beyond pairwise constraints to model higher-order crowd dynamics. To improve feature fusion, we design a hypergraph-based contrastive learning scheme that jointly enhances intra-modal discriminability and enforces cross-modal orthogonality. This mechanism enables the network to propagate global context effectively, allowing it to infer missing information even under severe occlusion. Extensive experiments on the Panoptic and GigaCrowd benchmarks confirm that our method achieves new state-of-the-art performance. Code and pre-trained models are available at this https URL.

---


### 4. [PREPING: Building Agent Memory without Tasks](https://arxiv.org/abs/2605.13880)

**<font color=#1a73e8>作者：</font>** Yumin Choi, Sangwoo Park, Minki Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent memory is typically constructed either offline from curated demonstrations or online from post-deployment interactions. However, regardless of how it is built, an agent faces a cold-start gap when first introduced to a new environment without any task-specific experience available. In this paper, we study pre-task memory construction: whether an agent can build procedural memory before observing any target-environment tasks, using only self-generated synthetic practice. Yet, synthetic interaction alone is insufficient, as without controlling what to practice and what to store, synthetic tasks become redundant, infeasible, and ultimately uninformative, and memory further degrades quickly due to unfiltered trajectories. To overcome this, we present Preping, a proposer-guided memory construction framework. At its core is proposer memory, a structured control state that shapes future practice. A Proposer generates synthetic tasks conditioned on this state, a Solver executes them, and a Validator determines which trajectories are eligible for memory insertion while also providing feedback to guide future proposals. Experiments on AppWorld, BFCL v3, and MCP-Universe show that Preping substantially improves over a no-memory baseline and achieves performance competitive with strong playbook-based methods built from offline or online experience, with deployment cost $2.99\times$ lower on AppWorld and $2.23\times$ lower on BFCL v3 than online memory construction. Further analyses reveal that the main benefit does not come from synthetic volume alone, but from proposer-side control over feasibility, redundancy, and coverage, combined with selective memory updates.

---


### 5. [Ready from Day 1: Population-Aware Coordination for Large-Scale Constrained Multi-Agent Systems](https://arxiv.org/abs/2605.13900)

**<font color=#1a73e8>作者：</font>** Angel Wang, Dominique Perrault-Joncas, Alvaro Maggiar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In large-scale multi-agent systems with shared resource constraints, an upstream planner must iteratively evaluate candidate resource plans -- assessing feasibility, aggregate response, and marginal cost -- before committing to one. Lagrangian relaxation separates local decisions through a broadcast cost signal, but the planner still needs the cost-to-utilization response map to explore plan space, and this map depends on population composition that changes across planning cycles. We propose \emph{population-aware coordination interfaces}: learned primal and dual maps, conditioned on compact population summaries, that the planner queries inside its iterative loop. The primal map predicts aggregate utilization under a proposed cost trajectory; the dual map predicts the cost trajectory for a target plan. By encoding response-relevant population structure, these maps remain reliable across evolving populations without per-cycle retraining, and support coordination of large populations from compact subsamples. We additionally cast Sim2Real transfer as a backtestable procedure, enabling evaluation before deployment. In a supply-chain capacity-control case study, population-aware interfaces reduce forecast error by 16--19\% and capacity violations by 20--51\% relative to population-unaware baselines under composition shift; 20K-agent cohorts support accurate coordination of 500K-agent populations; and simulator-trained primal maps achieve 11.1\% MAPE on real observations versus 13--24\% for baselines.

---


### 6. [XAI and Statistical Analysis for Reliable Intrusion Detection in the UAVIDS-2025 Dataset: From Tree to Hybrid and Tabular DNN Ensembles](https://arxiv.org/abs/2605.13922)

**<font color=#1a73e8>作者：</font>** Iakovos-Christos Zarkadis, Christos Douligeris  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> During the last few years, the term Mechanistic Interpretability, a specific area, under the umbrella of explainable artificial intelligence (XAI), has been introduced, to explain the decisions made by complex machine learning (ML) models in critical systems like UAV intrusion detection systems (UAVIDS). In this paper, we apply best-practices for data pre-processing and examine a wide range of tree-ensembles, deep neural networks, hybrid stacking models and the latest ensemble neural networks to detect intrusions in UAV, with stratified 10-fold cross validation. With our top-performing model, XGBoost, we proceed to Shapley Additive explanations (SHAP), to analyze the global and local feature importances and understand which features, each attack targets, to mimic normal traffic and where the misclassifications occur. Furthermore a distribution analysis follows, by visually comparing violin plots and the curves of kernel density estimations. With the Westfall-Young permutation test for multiple comparisons, the Bandwidth optimization of the KDEs and the selection of Jensen-Shannon Distance for the test, we discover the true causes of false predictions, observed in Wormhole and Blackhole attacks in UAVIDS-2025. The findings provide robust, reliable and explainable models for UAV intrusion detection, along with statistical insights, which capture and clarify the masked nature of the attacks, regarding the challenge of Density Support Intersection, between these attacks, in this dataset.

---


### 7. [Vision-Based Runtime Monitoring under Varying Specifications using Semantic Latent Representations](https://arxiv.org/abs/2605.13923)

**<font color=#1a73e8>作者：</font>** Bardh Hoxha, Oliver Schön, Hideki Okamoto 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study certified runtime monitoring of past-time signal temporal logic (ptSTL) from visual observations under partial observability. The monitor must infer safety-relevant quantities from images and provide finite-sample guarantees, while being \emph{reusable}: once trained and calibrated, it should certify any formula in a target fragment without per-formula retraining. For fragments induced by a finite dictionary of temporal atoms, we prove that the \emph{semantic basis}, the vector of atom robustness scores, is the minimum prediction target within the class of monotone, 1-Lipschitz reusable interfaces: any formula is evaluated by a deterministic decoder derived from the parse tree, and a single conformal calibration pass certifies the entire fragment with no union bound. We also introduce a \emph{rolling prediction monitor} that predicts only current predicate values and reconstructs temporal history online; this is easier to learn but grows conservative at long horizons. On a pedestrian-crossroad benchmark, rolling achieves tighter certified bounds at short horizons while the semantic-basis monitor is up to 4-times tighter at long horizons. We validate the presented monitors on real-world Waymo driving data, where both monitors satisfy the conformal coverage guarantee empirically.

---


### 8. [Rethinking Molecular OOD Generalization via Target-Aware Source Selection](https://arxiv.org/abs/2605.13932)

**<font color=#1a73e8>作者：</font>** Zhuohao Lin, Kun Li, Jiameng Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust prediction of molecular properties under extreme out-of-distribution (OOD) scenarios is a pivotal bottleneck in AI-driven drug discovery. Current scaffold-splitting protocols fail to obstruct microscopic semantic overlap, predisposing models to shortcut learning and overestimating their true extrapolation capability; meanwhile, conventional domain adaptation paradigms suffer under extreme structural shifts, as blindly aligning heterogeneous source libraries injects topological noise and triggers negative transfer. To address these two challenges, scaffold-cluster out-of-distribution performance evaluation benchmark (SCOPE-BENCH), a benchmark built on cluster-level partitioning in an explicit physicochemical descriptor space, is proposed alongside policy optimization for multi-source adaptation (POMA), a framework that formulates knowledge transfer as a retrieve-compose-adapt pipeline: labeled source scaffolds structurally close to the unlabeled target are first identified as proxy targets; a reinforcement learning policy then adaptively selects the optimal source subset from an exponentially large candidate pool; and dual-scale domain adaptation is finally performed at macroscopic topological and microscopic pharmacophore scales. Evaluations show that prediction errors of state-of-the-art 3D molecular models surge by up to 8.0x on SCOPE-BENCH with a mean of 5.9x, while POMA achieves up to an 11.2% reduction in mean absolute error with an average relative improvement of 6.2% across diverse backbone architectures. Code is available at this https URL.

---


### 9. [Unsupervised learning of acquisition variability in structural connectomes via hybrid latent space modeling](https://arxiv.org/abs/2605.13933)

**<font color=#1a73e8>作者：</font>** Gaurav Rudravaram, Lianrui Zuo, Karthik Ramadass 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Acquisition differences across sites, scanners, and protocols in dMRI introduce variability that complicates structural connectome analysis. This motivates deep learning models that can represent high-dimensional connectomes in a low-dimensional space while explicitly separating acquisition-related effects from biological variation. Conventional dimensionality reduction methods model all variance as continuous, so acquisition effects often get absorbed into a continuous latent space. Recent hybrid latent-space models combine discrete and continuous components to address this, but typically require manual capacity tuning to ensure the discrete component captures the intended variability. We introduce an unsupervised framework that removes this manual tuning by architecturally annealing encoder outputs before decoding, allowing the model to adaptively balance discrete and continuous latent variables during training. To evaluate it, we curated a dataset of N=7,416 structural connectomes derived from dMRI, spanning ages 2 to 102 and 13 studies with 25 unique acquisition-parameter combinations. Of these, 5,900 are cognitively unimpaired, 877 have mild cognitive impairment (MCI), and 639 have Alzheimer's disease (AD). We compare against a standard VAE, PCA with k-means clustering, and hybrid models that anneal only through the loss function. Our architectural annealing produces stronger site learning (ARI=0.53, p<0.05) than these baselines. Results show that a hybrid continuous-discrete latent space, with architectural rather than loss-based annealing, provides a useful unsupervised mechanism for capturing acquisition variability in dMRI: by jointly modeling smooth and categorical structure, the Joint-VAE recovers clusters aligned with scanner and protocol differences.

---


### 10. [AgentTrap: Measuring Runtime Trust Failures in Third-Party Agent Skills](https://arxiv.org/abs/2605.13940)

**<font color=#1a73e8>作者：</font>** Haomin Zhuang, Hanwen Xing, Yujun Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party skills are becoming the package ecosystem for LLM agents. They package natural-language instructions, helper scripts, templates, documents, and service configuration into reusable workflows. This makes skills useful, but it also introduces a new security problem: a malicious skill does not need to ask the model to perform an obviously harmful action. Instead, it can disguise the harmful behavior as part of a routine workflow, relying on the agent to execute that workflow with high-value permissions and limited human supervision.
We introduce AgentTrap, a dynamic benchmark for evaluating whether LLM agents can use third-party skills while resisting malicious runtime behavior. AgentTrap contains 141 tasks: 91 malicious tasks and 50 benign utility tasks, covering 16 security-impact dimensions grounded in agent-skill supply-chain threats. In each task, the agent receives an ordinary user request, runs with installed skills that may contain malicious workflow elements, and is executed in a sandboxed environment. AgentTrap then judges complete trajectories for attack success, blocked or refused behavior, attack-not-triggered cases, and no-attack-evidence outcomes. Our central finding is that the most informative failures are not simple jailbreaks. Models often complete the visible user task while treating unsafe side effects introduced by the skill as part of the normal workflow. This motivates runtime evaluation of the concrete model--framework--workspace environment in which users actually delegate work. Code and data are available at this https URL and this https URL.

---


### 11. [EMA: Efficient Model Adaptation for Learning-based Systems](https://arxiv.org/abs/2605.13942)

**<font color=#1a73e8>作者：</font>** Daiyang Yu, Xinyu Chen, Yihan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) is increasingly applied to optimize system performance in tasks such as resource management and network simulation. Unlike traditional ML tasks (e.g., image classification), networked systems often operate in heterogeneous, long-running, and dynamic environment states, where input conditions (e.g., network loads) and operational objectives can shift over time and across settings. Existing learning-based systems offer little support for adaptation, resulting in costly model training, extensive data collection, degraded system performance, and slow responsiveness.
This paper presents EMA, the first model adaptation system supporting learning-based systems to adapt to evolving environments with minimal operational overhead. EMA takes a system-driven, data-centric approach that accommodates diverse system and model designs while addressing two key deployment challenges. First, it reduces expensive model training by introducing state transformers that align the input state of a new environment with previously similar states, allowing models to warm-start adaptation. Second, it addresses the often-overlooked yet costly process of data labeling--collecting ground truth for exploring and training on various system decisions--by prioritizing labeling high-utility data while balancing the tradeoff between training and labeling cost. Evaluations on eight representative learning-based systems show that EMA reduces adaptation costs (e.g., GPU training time) by 14.9-42.4% while improving system performance (e.g., network throughput) by 6.9-31.3%.

---


### 12. [A Unified Geometric Framework for Weighted Contrastive Learning](https://arxiv.org/abs/2605.13943)

**<font color=#1a73e8>作者：</font>** Raphael Vock, Edouard Duchesnay, Benoit Dufumier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive learning (CL) aims to preserve relational structure between samples by learning representations that reflect a similarity graph. Yet, the geometry of the resulting embeddings remains poorly understood. Here we show that weighted InfoNCE objectives can be interpreted as Distance Geometry Problems, where the weighting scheme specifies the target geometry to be realized by the representation. This viewpoint yields exact characterizations of the optimal embeddings for several supervised and weakly supervised objectives. In supervised classification, both SupCon and Soft SupCon (a dense relaxation of it where pairs from distinct classes have small non-zero similarity) collapse samples within each class to a single prototype. However, while balanced SupCon recovers the classical regular simplex geometry, class imbalance breaks this symmetry: SupCon induces non-uniform inter-class similarities depending on class sizes, whereas Soft SupCon preserves a regular simplex geometry regardless of class imbalance. In continuous-label settings, our framework reveals a different failure mode: y-Aware CL generally cannot attain its entropic optimum unless the labels lie on a hypersphere, exposing a mismatch between Euclidean label weights and spherical latent similarity. By contrast, geometrically consistent choices such as Euclidean-Euclidean weighting or X-CLR admit unique optimal embeddings. Our results show that the choice of weighting scheme determines whether contrastive learning is geometrically realizable, degenerate, or inconsistent, providing a principled framework for designing contrastive objectives.

---


### 13. [Collider-Bench: Benchmarking AI Agents with Particle Physics Analysis Reproduction](https://arxiv.org/abs/2605.13950)

**<font color=#1a73e8>作者：</font>** Darius A. Faroughy, Sofia Palacios Schweitzer, Ian Pang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous language-model agents are increasingly evaluated on long-horizon tool-use tasks, but existing benchmarks rarely capture the complexity and nuance of real scientific work. To address this gap, we introduce Collider-Bench, a benchmark for evaluating whether LLM agents can reproduce experimental analyses from the Large Hadron Collider (LHC) using only public papers and open scientific software. Such analyses are often difficult to reproduce because the public toolchain only approximates the software used internally by the experimental collaborations, while the published papers inevitably omit implementation details needed for a faithful reconstruction. Agents must therefore rely on physical reasoning, domain knowledge, and trial-and-error to fill these gaps. Each task requires the agent to turn a published analysis into an executable simulation-and-selection pipeline and submit predicted collision event yields in specified signal regions. These predictions are evaluated with standard histogram metrics that provide continuous fidelity scores without a hand-written rubric. We also report the computational cost incurred by each agent per task. Finally, we evaluate the codebase and full session trace using an LLM judge to catch qualitative failure modes such as fabrications, hallucinations and duplications. We release an initial set of tasks drawn from LHC searches, together with a containerized sandbox and event simulation tools. We evaluate across a capability ladder of general purpose coding agents. Our results show that on average no agent reliably beats the physicist-in-the-loop solution.

---


### 14. [WarmPrior: Straightening Flow-Matching Policies with Temporal Priors](https://arxiv.org/abs/2605.13959)

**<font color=#1a73e8>作者：</font>** Sinjae Kang, Chanyoung Kim, Kaixin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative policies based on diffusion and flow matching have become a dominant paradigm for visuomotor robotic control. We show that replacing the standard Gaussian source distribution with WarmPrior, a simple temporally grounded prior constructed from readily available recent action history, consistently improves success rates on robotic manipulation tasks. We trace this gain to markedly straighter probability paths, echoing the effect of optimal-transport couplings in Rectified Flow. Beyond standard behavior cloning, WarmPrior also reshapes the exploration distribution in prior-space reinforcement learning, improving both sample efficiency and final performance. Collectively, these results identify the source distribution as an important and underexplored design axis in generative robot control.

---


### 15. [Few Channels Draw The Whole Picture: Revealing Massive Activations in Diffusion Transformers](https://arxiv.org/abs/2605.13974)

**<font color=#1a73e8>作者：</font>** Evelyn Turri, Davide Bucciarelli, Sara Sarto 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) and related flow-based architectures are now among the strongest text-to-image generators, yet the internal mechanisms through which prompts shape image semantics remain poorly understood. In this work, we study massive activations: a small subset of hidden-state channels whose responses are consistently much larger than the rest. We show that, despite their sparsity, these few channels effectively draw the whole picture, in three complementary senses. First, they are functionally critical: a controlled disruption probe that zeroes the massive channels causes a sharp collapse in generation quality, while disrupting an equally-sized set of low-statistic channels has marginal effect. Second, they are spatially organized: restricting image-stream tokens to massive channels and clustering them yields coherent partitions that closely align with the main subject and salient regions, exposing a structured spatial code hidden inside an apparently outlier-like subspace. Third, they are transferable: transporting massive activations from one prompt-conditioned trajectory into another, shifts the final image toward the source prompt while preserving substantial content from the target, producing localized semantic interpolation rather than unstructured pixel blending. We exploit this property in two use cases: text-conditioned and image-conditioned semantic transport, where massive activations transport enables prompt interpolation and subject-driven generation without any additional training. Together, these results recast massive activations not as activation anomalies, but as a sparse prompt-conditioned carrier subspace that organizes and controls semantic information in modern DiT models.

---


### 16. [TabPFN-3: Technical Report](https://arxiv.org/abs/2605.13986)

**<font color=#1a73e8>作者：</font>** Léo Grinsztajn, Klemens Flöge, Oscar Key 等 41 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data underpins most high-value prediction problems in science and industry, and TabPFN has driven the foundation model revolution for this modality. Designed with feedback from our users, TabPFN-3 builds on this foundation to scale state-of-the-art performance to datasets with 1M training rows and substantially reduce training and inference time. Pretrained exclusively on synthetic data from our prior, TabPFN-3 dramatically pushes the frontier of tabular prediction and brings substantial gains on time series, relational, and tabular-text data. On the standard tabular benchmark TabArena, a forward pass of TabPFN-3 outperforms all other models, including tuned and ensembled baselines, by a significant margin, and pareto-dominates the speed/performance frontier. On more diverse datasets, TabPFN-3 ranks first on datasets with many classes, and beats 8-hour-tuned gradient-boosted-tree baselines on datasets up to 1M training rows and 200 features. TabPFN-3 introduces test-time compute scaling to tabular foundation models. Our API offering TabPFN-3-Plus (Thinking) exploits this to beat all non-TabPFN models by over 200 Elo on TabArena, rising to 420 Elo on the largest data subset, and outperforms AutoGluon 1.5 extreme while being 10x faster, without using LLMs, real data, internet search or any other model besides TabPFN. TabPFN-3 extends the capabilities of our models, enabling SOTA prediction on relational data (new SOTA foundation model on RelBenchV1) and tabular-text data (SOTA on TabSTAR via TabPFN-3-Plus); and improves existing integrations: a specialized checkpoint, TabPFN-TS-3, ranks 2nd on the time-series benchmark fev-bench, and SHAP-value computation is up to 120x faster. TabPFN-3 achieves this performance while being up to 20x faster than TabPFN-2.5. In addition, a reduced KV cache and row-chunking scale to 1M rows on one H100 with fast inference speed.

---


### 17. [Neural Fields for NV-Center Inverse Sensing](https://arxiv.org/abs/2605.13988)

**<font color=#1a73e8>作者：</font>** Zhixuan Zhao, Tao Zhong, Yixun Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse problems in scientific sensing are often solved with either hand-designed regularizers or supervised networks trained on simulated labels, yet both can fail when the forward model is nonlinear, spectrally coupled, and physically delicate. We study this issue for noise sensing based on nitrogen-vacancy (NV) centers in diamond, where a quantum sensor measures magnetic-noise spectra generated by sparse spin sources. We show that replacing a common scalar/coherent forward approximation with a tensor power-summed dipolar operator changes the inverse landscape and exposes a center-collapse failure mode in free-density optimization. We propose NeTMY, an amortization-free coordinate neural field coupled to the differentiable NV forward model, with annealed positional encoding, multiscale optimization, sparsity/gating, and spectrum-fidelity losses. Across sparse synthetic reconstructions generated by the corrected operator, NeTMY achieves the best localization and distributional metrics in the tested benchmark. Mechanism experiments show that NeTMY does not directly execute the raw density-space gradient; its parameterization smooths and redistributes updates, mitigating the center-collapse pathology. These results position NV quantum sensing as a useful testbed for physics-faithful neural inverse problems.

---


### 18. [CineMesh4D: Personalized 4D Whole Heart Reconstruction from Sparse Cine MRI](https://arxiv.org/abs/2605.13994)

**<font color=#1a73e8>作者：</font>** Xiaoyue Liu, Xiaohan Yuan, Mark Y Chan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D+t whole-heart mesh reconstruction from cine MRI is a clinically crucial yet technically challenging task. The difficulty of this task arises from two coupled factors: inherently sparse sampling of 3D cardiac anatomy by 2D image slices and the tight coupling between cardiac shape and motion. Current cardiac image-to-mesh approaches typically reconstruct only a subset of cardiac chambers or a single phase of the cardiac cycle. In this work, we propose CineMesh4D, a novel end-to-end 4D (3D+t) pipeline that directly reconstructs patient-specific whole-heart mesh from multi-view 2D cine MRI via cross-domain mapping. Specifically, we introduce a differentiable rendering loss that enables supervision of 3D+t whole-heart mesh from multi-view sparse contours of cine MRI. Furthermore, we develop a dual-context temporal block that fuses global and local cardiac temporal information to capture high-dimensional sequential patterns. In quantitative and qualitative evaluations, CineMesh4D outperforms existing approaches in terms of reconstruction quality and motion consistency, providing a practical pathway for personalized real-time cardiac assessment. The code will be publicly released once the manuscript is accepted.

---


### 19. [Support Before Frequency in Discrete Diffusion](https://arxiv.org/abs/2605.13999)

**<font color=#1a73e8>作者：</font>** Adrian Müller, Antoine Gonon, Zebang Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models are increasingly competitive for language modeling, yet it remains unclear how their denoising objectives organize learning. Although these objectives target the full data distribution, we show that the exact reverse process induces a hierarchy between coarse support information and finer frequency information. For uniform and absorbing (a.k.a. masking) diffusion, we prove that, in the small-noise regime of the final denoising steps, each single-token reverse edit decomposes into a leading scale, determined by whether it moves toward the data support (e.g., grammatically valid sentences), and a finer coefficient, determining relative probabilities within the same scale. Thus, recovering validity structure only requires learning the correct order of magnitude of reverse probabilities, whereas recovering data frequencies requires coefficient-level estimation. The separation is mechanism-dependent: uniform diffusion exhibits a trichotomy into validity-improving, validity-preserving, and validity-worsening edits, while absorbing diffusion places its leading-order mass on validity-improving moves. Experiments on a masked language diffusion model and synthetic regular-language tasks support these predictions: support-localization emerges earlier than within-support frequency ranking, and the contrast between uniform and absorbing diffusion matches the predicted rate separation. Together, our results suggest that discrete diffusion models learn data support before data frequencies.

---


### 20. [Conditional Attribute Estimation with Autoregressive Sequence Models](https://arxiv.org/abs/2605.14004)

**<font color=#1a73e8>作者：</font>** Erica Stutz, Giacomo Marino, Daniella Meeker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models are often trained with a next-token prediction objective, yet many downstream applications require the ability to estimate or control sequence-level properties. Next-token prediction can lead to overfitting of local patterns during training, underfitting of global structure, and requires significant downstream modifications or expensive sampling to guide or predict the global attributes of generated samples at inference time. Here, we introduce Conditional Attribute Transformers, a novel method for jointly estimating the next-token probability and the value of an attribute conditional on each potential next token selection. This framework enables three critical capabilities within a single forward pass, without modification of the input sequence: (1) per-token credit assignment across an entire sequence, by identifying how each token in a sequence is associated with an attribute's value; (2) counterfactual analysis, by quantifying attribute differences conditional on alternative next token choices; (3) steerable generation, by decoding sequences based on a combination of next-token and attribute likelihoods. Our approach achieves state of the art performance on sparse reward tasks, improves next-token prediction at sufficient model sizes, estimates attribute probabilities orders of magnitude faster than sampling, and can guide decoding of autoregressive sequence models on a range of language tasks.

---


### 21. [Dywave: Event-Aligned Dynamic Tokenization for Heterogeneous IoT Sensing Signal](https://arxiv.org/abs/2605.14014)

**<font color=#1a73e8>作者：</font>** Tomoyoshi Kimura, Denizhan Kara, Jinyang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Internet of Things (IoT) systems continuously collect heterogeneous sensing signals from ubiquitous sensors to support intelligent applications such as human activity analysis, emotion monitoring, and environmental perception. These signals are inherently non-stationary and multi-scale, posing unique challenges for standard tokenization techniques. This paper proposes Dywave, a dynamic tokenization framework for IoT sensing signals that constructs compact input representations aligned with intrinsic temporal structures and underlying physical events. Dywave leverages wavelet-based hierarchical decomposition, identifies meaningful temporal boundaries corresponding to underlying semantic events, and adaptively compresses redundant intervals while preserving temporal coherence. Extensive evaluations on five real-world IoT sensing datasets across activity recognition, stress assessment, and nearby object detection demonstrate that Dywave outperforms state-of-the-art methods by up to 12% in accuracy, while improving computational efficiency by reducing input token lengths by up to 75% across mainstream sequence models. Moreover, Dywave exhibits improved robustness to domain shifts and varying sequence lengths.

---


### 22. [Memory Forensics Techniques for Automated Detection and Analysis of Go Malware](https://arxiv.org/abs/2605.14020)

**<font color=#1a73e8>作者：</font>** Hala Ali, Andrew Case, Irfan Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Go programming language has become increasingly popular among malware developers due to its ability to produce statically linked, cross-platform executables that challenge traditional analysis techniques. These binaries embed a substantial runtime and compiler-generated metadata and are compiled with aggressive optimizations that discard type information for function parameters and local variables. Go's design further complicates analysis by representing strings as pointer-length pairs rather than null-terminated sequences, employing a caller-allocated stack model that obscures argument boundaries, and fragmenting program state across concurrent goroutines. Although existing static analysis and reverse engineering tools provide Go-specific support, they remain limited to compile-time artifacts and cannot recover runtime execution state and artifacts that persist solely in memory. To address this gap, we present the first memory forensics framework for runtime analysis of Go binaries. By parsing Go's internal structures, our framework reconstructs type and function metadata, recovers heap-allocated and static strings, and distinguishes application-level functions. Through ABI-aware backward analysis, it derives execution paths and argument values from call sites. To capture runtime state beyond what static analysis reveals, it analyzes goroutine stacks to identify actively executing functions and recover their runtime argument values. We implemented all capabilities as Volatility 3 plugins and evaluated them against malware seen in recent incidents, such as the BRICKSTORM backdoor, Obscura ransomware, and Pantegana RAT, as well as open-source samples for reproducibility. The framework successfully recovered C2 endpoints, persistence mechanisms, encryption keys, ransom notes, and execution state, including critical runtime artifacts that were absent from published threat intelligence.

---


### 23. [R2R2: Robust Representation for Intensive Experience Reuse via Redundancy Reduction in Self-Predictive Learning](https://arxiv.org/abs/2605.14026)

**<font color=#1a73e8>作者：</font>** Sanghyeob Song, Donghyeok Lee, Jinsik Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For reinforcement learning in data-scarce domains like real-world robotics, intensive data reuse enhances efficiency but induces overfitting. While prior works focus on critic bias, representation-level instability in Self-Predictive Learning (SPL) under high Update-to-Data (UTD) regimes remains underexplored. To bridge this gap, we propose Robust Representation via Redundancy Reduction (R2R2), a regularization method within SPL. We theoretically identify that standard zero-centering conflicts with SPL's spectral properties and design a non-centered objective accordingly. We verify R2R2 on SPL-native algorithms like TD7. Furthermore, to demonstrate its orthogonality to prior advancements, we extend the state-of-the-art SimbaV2, which originally lacks SPL, by integrating a tailored SPL module, termed SimbaV2-SPL. Experiments across 11 continuous control tasks confirm that R2R2 effectively mitigates overfitting; specifically, at a UTD ratio of 20, it improves TD7 by ~22% and provides additional gains on top of SimbaV2-SPL, which itself establishes a new state-of-the-art. The code can be found at: this https URL

---


### 24. [Sheaf-Theoretic Transport and Obstruction for Detecting Scientific Theory Shift in AI Agents](https://arxiv.org/abs/2605.14033)

**<font color=#1a73e8>作者：</font>** David N. Olivieri, Roque J. Hernández  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific theory shift in AI agents requires more than fitting equations to data. An artificial scientific agent must detect whether an existing representational framework remains transportable into a new regime, or whether its language has become locally-to-globally obstructed and must be extended. This paper develops a finite sheaf-theoretic framework for detecting theory-shift candidates through transport and obstruction. Contexts are organized as a local-to-global structure in which source, overlap, target, and validation charts are fitted, restricted, and tested for gluing. Obstruction measures failure of coherence through residual fit, overlap incompatibility, constraint violation, limiting-relation failure, and representational cost. We evaluate the framework on a controlled transition-card benchmark designed to separate deformation within a source language from extension of that language. The main result is direct obstruction ranking: the intended deformation or extension is usually the lowest-obstruction candidate, and transition type is separated in the benchmark. A constellation kernel over the same signatures is included only as a secondary representational-similarity probe. The aim is not to reconstruct historical paradigm shifts or solve open-ended autonomous theory invention, but to isolate a finite diagnostic subproblem for AI agents: detecting when representational transport fails and extension becomes the coherent next move.

---


### 25. [Enhanced and Efficient Reasoning in Large Learning Models](https://arxiv.org/abs/2605.14036)

**<font color=#1a73e8>作者：</font>** Leslie G. Valiant  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In current Large Language Models we can trust the production of smoothly flowing prose on the basis of the principles of machine learning. However, there is no comparably principled basis to justify trust in the content of the text produced. It appears to be conventional wisdom that addressing this issue by adding more principled reasoning is not computationally affordable.
Here we propose a principled method of reasoning that is efficient enough to be practical for large language models. Further, the method allows the retention of much of the currently used software and hardware base. Our method for improving the functioning of large language models consists of a first stage of preprocessing that recodes the data to a Unary Relational Integracode that is more explicit about the relationships among the objects described in the text, followed as a second stage by a standard but possibly streamlined machine learning process that then also learns to predict these relationships.
The method may be viewed as realizing a world model and applying beyond natural language, to vision and actions, for example, where the multiple properties of an object referred to in an input are brought together explicitly, rather than remaining distributed in the various references to it in the input. We articulate its advantages in terms of Robust Logic, a system for performing principled chaining on learned, and hence uncertain, information. We show that this recoding has the surprising and fortuitous property that, while succinct, it makes the task of learning a core subset of relational rules that hold in the world described in the training data polynomial time learnable in a defined sense, the polynomial depending on the complexity of the rule. This gives support for sound reasoning within each single call of the learned classifier as well as between multiple calls.

---


### 26. [Self-Pruned Key-Value Attention: Learning When to Write by Predicting Future Utility](https://arxiv.org/abs/2605.14037)

**<font color=#1a73e8>作者：</font>** Gergely Szilvasy, Manuel Faysse, Maria Lomeli 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Under modern test-time compute and agentic paradigms, language models process ever-longer sequences. Efficient text generation with transformer architectures is increasingly constrained by the Key-Value cache memory footprint and bandwidth. To address this limitation, we introduce Self-Pruned Key-Value Attention (SP-KV), a mechanism designed to predict future KV utility in order to reduce the size of the long-term KV cache. This strategy operates at a fine granularity: a lightweight utility predictor scores each key-value pair, and while recent KVs are always available via a local window, older pairs are written in the cache and used in global attention only if their predicted utility surpasses a given threshold. The LLM and the utility predictor are trained jointly end-to-end exclusively through next-token prediction loss, and are adapted from pretrained LLM checkpoints.
Rather than enforcing a fixed compression ratio, SP-KV performs dynamic sparsification: the mechanism adapts to the input and typically reduces the KV cache size by a factor of $3$ to $10\times$, longer sequences often being more compressible. This leads to vast improvements in memory usage and decoding speed, with little to no degradation of validation loss nor performance on a broad set of downstream tasks. Beyond serving as an effective KV-cache reduction mechanism, our method reveals structured layer- and head-specific sparsity patterns that we can use to guide the design of hybrid local-global attention architectures.

---


### 27. [PVRF: All-in-one Adverse Weather Removal via Prior-modulated and Velocity-constrained Rectified Flow](https://arxiv.org/abs/2605.14045)

**<font color=#1a73e8>作者：</font>** Wei Dong, Han Zhou, Terry Ji 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adverse weather removal (AWR) in real-world images remains challenging due to heterogeneous and unseen degradations, while distortion-driven training often yields overly smooth results. We propose PVRF, a unified framework that integrates zero-shot soft weather perceptions with velocity-constrained rectified-flow refinement. PVRF introduces an AWR-specific question answering module (AWR-QA) that uses frozen vision--language models (VLMs) to estimate soft probabilities of weather types and low-level attribute scores. These perceptions condition restoration networks via attribute-modulated normalization (AMN) and weather-weighted adapters (WWA), producing an anchor estimate for refinement. We then learn a terminal-consistent residual rectified flow with perception-adaptive source perturbation and a terminal-consistent velocity parameterization to stabilize learning near the terminal regime. Extensive experiments show that PVRF improves both fidelity and perceptual quality over state-of-the-art baselines, with strong cross-dataset generalization on single and combined degradations. Code will be released at this https URL.

---


### 28. [Evolving Layer-Specific Scalar Functions for Hardware-Aware Transformer Adaptation](https://arxiv.org/abs/2605.14047)

**<font color=#1a73e8>作者：</font>** Kieran Carrigg, Sigur de Vries, Amirhossein Sadough 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) achieve state-of-the-art performance on challenging vision tasks, but their deployment on edge devices is severely hindered by the computational complexity and global reduction bottleneck imposed by layer normalization. Recent methods attempt to bypass this by replacing normalization layers with hardware-friendly scalar approximations. However, these homogeneous replacements do not optimally fit to all layers' behaviour and rely on expensive model retraining. In this work, we propose a highly efficient, hardware-aware framework that utilizes genetic programming (GP) to evolve heterogeneous, layer-specific scalar functions directly from pre-trained weights. Coupled with a novel post-training re-alignment strategy, our approach eliminates the need to retrain models from scratch entirely. Our evolved expressions accurately approximate the target normalization behaviours, capturing $91.6\%$ of the variance ($R^2$) compared to only $70.2\%$ for homogeneous baselines, allowing our modified architecture to recover $84.25\%$ Top-1 ImageNet-1K accuracy in only 20 epochs. By preserving this performance while eliminating the global reduction bottleneck, our approach establishes a highly favourable trade-off between arithmetic complexity and off-chip memory traffic, removing a primary barrier to the efficient deployment of ViTs on edge accelerators.

---


### 29. [Network-Aware Bilinear Tokenization for Brain Functional Connectivity Representation Learning](https://arxiv.org/abs/2605.14048)

**<font color=#1a73e8>作者：</font>** Leo Milecki, Qingyu Hu, Bahram Jafrasteh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Masked autoencoders (MAEs) have recently shown promise for self-supervised representation learning of resting-state brain functional connectivity (FC). However, a fundamental question remains unresolved: how should FC matrices be tokenized to align with the intrinsic modular organization of large-scale brain networks? Existing approaches typically adopt region-centric or graph-based schemes that treat FC as structurally homogeneous elements and overlook the large-scale network brain organization. We introduce NERVE (Network-Aware Representations of Brain Functional Connectivity via Bilinear Tokenization), a self-supervised learning framework that redefines FC tokenization by partitioning FC matrices into patches of intra- and inter-network connectivity blocks. Unlike image-based MAE, where fixed-size patches share a common tokenizer, FC patches defined by network pairs are heterogeneous in size and correspond to distinct functional roles. To resolve this problem, NERVE embeds FC patches through a novel structured bilinear factorization. This formulation preserves network identity and reduces parameter complexity from quadratic to linear scaling in the number of networks. We evaluate NERVE across three large-scale developmental cohorts (ABCD, PNC, and CCNP) for behavior and psychopathology prediction. Compared to structurally agnostic MAE variants and graph-based self-supervised baselines, the proposed network-aware formulation yields more stable and transferable representations, particularly in cross-cohort evaluation. Ablation studies confirm that the proposed bilinear network embedding and anatomically grounded parcellation are critical for performance. These findings highlight the importance of incorporating domain-specific structural priors into self-supervised learning for functional connectomics.

---


### 30. [Bridging Legal Interpretation and Formal Logic: Faithfulness, Assumption, and the Future of AI Legal Reasoning](https://arxiv.org/abs/2605.14049)

**<font color=#1a73e8>作者：</font>** Olivia Peiyu Wang, Leilani H. Gilpin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing adoption of large language models in legal practice brings both significant promise and serious risk. Legal professionals stand to benefit from AI that can reason over contracts, draft documents, and analyze sources at scale, yet the high-stakes nature of legal work demands a level of rigor that current AI systems do not provide. The central problem is not simply that LLMs hallucinate facts and references; it is that they systematically draw inferences that go beyond what the source text actually supports, presenting assumption-laden conclusions as if they were logically grounded. This proposal presents a neuro-symbolic approach to legal AI that combines the expressive power of large language models with the rigor of formal verification, aiming to make AI-assisted legal reasoning both capable and trustworthy, thus reducing the burden of manual verification without sacrificing the accountability that legal practice demands.

---


### 31. [Dual Hierarchical Dialogue Policy Learning for Legal Inquisitive Conversational Agents](https://arxiv.org/abs/2605.14057)

**<font color=#1a73e8>作者：</font>** Xubo Lin, Zezhii Deng, Shihao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most existing dialogue systems are user-driven, primarily designed to fulfill user requests. However, in many critical real-world scenarios, a conversational agent must proactively extract information to achieve its own objectives rather than merely respond. To address this gap, we introduce \emph{Inquisitive Conversational Agents (ICAs)} and develop an ICA specifically tailored to U.S. Supreme Court oral arguments. We propose a Dual Hierarchical Reinforcement Learning framework featuring two cooperating RL agents, each with its own policy, to coordinate strategic dialogue management and fine-grained utterance generation. By learning when and how to ask probing questions, the agent emulates judicial questioning patterns and systematically uncovers crucial information to fulfill its legal objectives. Evaluations on a U.S. Supreme Court dataset show that our method outperforms various baselines across multiple metrics. It represents an important first step toward broader high-stakes, domain-specific applications.

---


### 32. [MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)

**<font color=#1a73e8>作者：</font>** Nilay Patel, Noah Arias, Davit Babayan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current autoformalization benchmarks are largely focused on olympiad or undergraduate mathematics, while graduate and research-level mathematics remains underexplored. In this paper, we introduce MathAtlas, the first large-scale autoformalization benchmark of in the wild graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks. MathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems. Our extensive experiments show that MathAtlas is high quality but extremely challenging: strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. Furthermore, we find performance of state-of-the-art models degrades substantially with dependency depth: on MA-Hard, a subset of 700 entities with the deepest dependency trees, the best model achieves only 2.6% correctness for autoformalization on this challenging dataset. We release MathAtlas to the community as a benchmark set for large-scale autoformalization of graduate-level mathematics in the wild.

---


### 33. [Reliability-Gated Source Anchoring for Continual Test-Time Adaptation](https://arxiv.org/abs/2605.14063)

**<font color=#1a73e8>作者：</font>** Vikash Singh, Debargha Ganguly, Weicong Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual test-time adaptation (CTTA) updates a pretrained model online on an unlabeled, non-stationary stream while anchoring it to a frozen source checkpoint. This anchor is useful only when the source remains reliable. On CCC-Hard, however, a ResNet-50 source falls to approximately $1.3\%$ top-$1$ accuracy, while existing source-anchored CTTA methods continue applying the same anchor strength. We call this failure mode blind anchoring and propose RMemSafe, a reliability-gated extension of ROID that uses the frozen source's normalized predictive entropy to attenuate all explicit source-coupled uses in the objective. When the source posterior approaches uniformity, the gate closes: the source anchor and agreement filter vanish, and the objective reduces to a source-agnostic fallback comprising ROID's base losses plus marginal calibration. Combined with ASR, RMemSafe achieves the lowest error on $8$ of $9$ matched-split continual-corruption cells and is the best reset-based method on all $9$, improving ROID+ASR by $1.05$~pp on ResNet-50 and $0.48$~pp on ViT-B/16. A controlled source-degradation sweep shows a $1.13{\times}$ shallower harm slope than ROID+ASR, consistent with the graceful-decay prediction. The entropy gate detects high-entropy source collapse, not confidently wrong low-entropy sources; this scope is explicitly evaluated and discussed.

---


### 34. [Comparative Evaluation of Machine Learning Approaches for Minority-Class Financial Distress Prediction Under Class Imbalance Constraints](https://arxiv.org/abs/2605.14067)

**<font color=#1a73e8>作者：</font>** Karan Sehgal, Khawar Naveed Bhatti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial distress prediction remains a significant challenge in enterprise risk analysis due to the highly imbalanced nature of real-world financial datasets, where bankrupt or distressed firms typically constitute only a small minority of observations.
This paper presents a comparative evaluation of classical statistical methods, ensemble learning approaches, and exploratory neural models for minority-class financial distress prediction under class imbalance constraints.
The study incorporates structured preprocessing, imbalance mitigation using the Synthetic Minority Oversampling Technique (SMOTE), comparative evaluation across ensemble learning architectures including XGBoost, CatBoost, LightGBM, Random Forest, and explainability analysis using SHAP-based feature attribution methods.
Experimental evaluation demonstrates that gradient-boosting approaches achieved improved minority-class sensitivity relative to baseline statistical classifiers under severe imbalance conditions. The workflow additionally emphasises reproducibility, interpretability, auditability, and governance-oriented machine learning evaluation within enterprise financial risk environments.
The work is positioned as an applied engineering evaluation intended to support reproducible and interpretable machine learning workflows for financial distress prediction under severe class imbalance constraints.

---


### 35. [SurF: A Generative Model for Multivariate Irregular Time Series Forecasting](https://arxiv.org/abs/2605.14069)

**<font color=#1a73e8>作者：</font>** Mohammad R. Rezaei, Tejas Balaji, Rahul G. Krishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Irregularly sampled multivariate event streams remain a stubbornly difficult modality for generative modeling: tokenization-based approaches break down when inter-event intervals vary by orders of magnitude, and neural temporal point processes are bottlenecked by window-level numerical quadrature. We (i) propose SurF, a generative model that uses the Time Rescaling Theorem (TRT) as a learnable bijection between event sequences and i.i.d.\ unit-rate exponential noise, enabling a single model to be trained across heterogeneous event-stream datasets; (ii) three efficient parameterizations of the cumulative intensity that scale to long sequences; and (iii) a Transformer-based encoder for multi-dataset pretraining. On six real-world benchmarks, SurF achieves the best reported time RMSE on Earthquake, Retweet, and Taobao, and is within trial-level noise of the strongest specialist on the remaining three. Under a strict leave-one-out protocol, the held-out checkpoint beats every classical and neural-autoregressive baseline on 5/6 datasets and beats every baseline on Amazon and Earthquake, an initial step toward foundation models over asynchronous event streams.

---


### 36. [AttnGen: Attention-Guided Saliency Learning for Interpretable Genomic Sequence Classification](https://arxiv.org/abs/2605.14073)

**<font color=#1a73e8>作者：</font>** Rayhaneh Shabani Nia, Ali Karkehabadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks have achieved strong performance in genomic sequence classification; however, relating their predictions to biologically meaningful sequence patterns remains challenging. In this work, we present AttnGen, an attention-guided training framework that embeds interpretability directly into the optimization process. AttnGen computes nucleotide-level importance scores using an attention mechanism and progressively suppresses low-contribution positions during training. This encourages the model to focus its predictions on a compact set of informative regions while reducing reliance on noisy sequence elements. We evaluate AttnGen on the standardized demo_human_or_worm benchmark, a binary classification task over 200-nucleotide sequences. With moderate masking, AttnGen achieves a validation accuracy of 96.73%, outperforming a conventional CNN baseline with 95.83% accuracy, while also exhibiting faster convergence and improved training stability. To assess whether the learned importance scores reflect functionally relevant signal, we conduct perturbation-based analysis by removing high-saliency nucleotides. This causes accuracy to drop from 96.9% to near chance level on a 3,000-sequence evaluation set, indicating that the model relies on a relatively small subset of informative positions. Our analysis shows that masking 10--20% of positions provides the most favorable trade-off between predictive performance and interpretability. These results suggest that attention-guided masking not only improves classification performance but also reshapes how models distribute importance across sequence positions. Although this study focuses on short genomic sequences, the proposed approach may extend to more complex interpretable sequence modeling settings.

---


### 37. [Fair and Calibrated Toxicity Detection with Robust Training and Abstention](https://arxiv.org/abs/2605.14074)

**<font color=#1a73e8>作者：</font>** Mokshit Surana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness in toxicity classification involves three integrated axes: ranking, calibration, and abstention. Training-time interventions and post-hoc safety mechanisms cannot be evaluated independently because the former determines the efficacy of the latter. We compare Empirical Risk Minimization (ERM), instance-level reweighting, and Group DRO across these axes, combined with temperature scaling, confidence-based abstention, and per-identity threshold optimization. Evaluation uses subgroup AUC, BPSN/BNSP AUC, error gaps, and per-subgroup Expected Calibration Error (ECE) with bootstrap CIs ($n = 1000$).
We report four findings. (1) Calibration disparity is a hidden fairness violation. ERM has near-perfect aggregate calibration ($0.013$) but is significantly miscalibrated across all identity subgroups ($+0.029$ to $+0.134$). (2) Training interventions reshape rather than eliminate disparity. Reweighted ERM improves ranking (BPSN AUC $+0.06$ to $+0.12$) but worsens the calibration-fairness gap by up to $+0.232$. Group DRO eliminates calibration disparity but only by becoming uniformly miscalibrated globally (ECE $0.118$). (3) Post-hoc methods inherit training failure modes. Temperature scaling fails because miscalibration is non-uniform. Confidence-based abstention works under ERM but breaks under DRO, where the risk-coverage curve rises with deferral. (4) Abstention itself is unfair. Confidence-based deferral helps background content far more than identity-mentioning content. We argue that SRAI fairness requires a multi-axis framework: methods that differ only in aggregate ranking can differ sharply in failure modes that determine real-world harm.

---


### 38. [Venus-DeFakerOne: Unified Fake Image Detection & Localization](https://arxiv.org/abs/2605.14091)

**<font color=#1a73e8>作者：</font>** GuangJian Team  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, the rapid evolution of generative AI has fundamentally reshaped the paradigm of image forgery, breaking the traditional boundaries between document editing, natural image manipulation, DeepFake generation, and full-image AIGC synthesis. Despite this shift toward unified forgery generation, existing research in Fake Image Detection and Localization (FIDL) remains fragmented. This creates a mismatch between increasingly unified forgery generation mechanisms and the domain-specific detection paradigm. Bridging this mismatch poses two key challenges for FIDL: understanding cross-domain artifacts transfer and interference, and building a high-capacity unified foundation model for joint detection and localization. To address these challenges, we propose DeFakerOne, a data-centric, unified FIDL foundation model integrating InternVL2 and SAM2. DeFakerOne enables simultaneous image-level detection and pixel-level forgery localization across diverse scenarios. Extensive experiments demonstrate that DeFakerOne achieves state-of-the-art performance, outperforming baselines on 39 forgery detection benchmarks and 9 localization benchmarks. Furthermore, the model exhibits superior robustness against real-world perturbations and state-of-the-art generators such as GPT-Image-2. Finally, we provide a systematic analysis of data scaling laws, cross-domain artifacts transfer-interference patterns, the necessity of fine-grained supervision, and the original resolution artifacts preservation, highlighting the design principles for scalable, robust, and unified FIDL.

---


### 39. [ChromaFlow: A Negative Ablation Study of Orchestration Overhead in Tool-Augmented Agent Evaluation](https://arxiv.org/abs/2605.14102)

**<font color=#1a73e8>作者：</font>** Tarun Mittal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous language-model agents increasingly combine planning, tool use, document processing, browsing, code execution, and verification loops. These capabilities make agent systems more useful, but they also introduce operational failure modes that are not visible from final accuracy alone. This report presents ChromaFlow, a tool-augmented autonomous reasoning framework built around planner-directed execution, specialized tool use, and telemetry-driven evaluation. We analyze ChromaFlow on GAIA 2023 Level-1 validation tasks under clean evaluation constraints. A frozen full Level-1 baseline achieved 29/53 correct answers, or 54.72%. A later recovery configuration with expanded orchestration achieved 27/53 correct answers, or 50.94%, while increasing tracebacks, timeout events, tool-failure mentions, token-line calls, and campaign-log cost estimates. Two randomized 20-task smoke evaluations produced 12/20 and 11/20 correct answers, showing that small diagnostic gains can be unstable across samples. The central result is therefore a negative ablation: more aggressive orchestration did not improve full-set performance and increased operational noise. The report argues that bounded planner escalation, deterministic extraction, evidence reconciliation, and explicit run gates should be treated as first-order requirements for reliable autonomous agent evaluation.

---


### 40. [DUET: Dual-Paradigm Adaptive Expert Triage with Single-cell Inductive Prior for Spatial Transcriptomics Prediction](https://arxiv.org/abs/2605.14104)

**<font color=#1a73e8>作者：</font>** Junchao Zhu, Ruining Deng, Junlin Guo 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inferring spatially resolved gene expression from histology images offers a cost-effective complement to spatial transcriptomics (ST). However, existing methods reduce this task to a simple morphology-to-expression mapping, where visual similarity does not guarantee molecular consistency. Meanwhile, single-cell data has amassed rich resources far surpassing the scale of ST data, yet it remains underexplored in vision-omics modeling. Furthermore, current approaches commit to a monolithic paradigm with bottlenecks, unable to balance expressive flexibility with biological fidelity. To bridge these gaps, we propose DUET, a novel dual-paradigm framework that synergizes parametric prediction and memory-based retrieval under cellular inductive priors. DUET implements a parallel regression-retrieval paradigm, adaptively reconciling the outputs of its complementary pathways. To mitigate aleatoric vision ambiguity, we incorporate large-scale single-cell references to impose molecular states as biological constraints for faithful learning. Building upon structural refinement, we further design a lightweight adapter to dynamically assign branch preference across spatial contexts to achieve optimal performance. Extensive experiments on three public datasets across varied gene scales demonstrate that DUET achieves SOTA performance, with consistent gains contributed by each proposed component. Code is available at this https URL

---


### 41. [Bridging the Rural Healthcare Gap: A Cascaded Edge-Cloud Architecture for Automated Retinal Screening](https://arxiv.org/abs/2605.14108)

**<font color=#1a73e8>作者：</font>** Nishi Doshi, Shrey Shah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diabetic Retinopathy (DR) is one of the leading causes of preventable blindness, yet rural regions often lack the specialists and infrastructure needed for early detection. Although cloud-based deep learning systems offer high accuracy, they face significant challenges in these settings due to high latency, limited bandwidth, and high data transmission costs. To address these challenges, we propose a two-tier edge-cloud cascade on the public APTOS 2019 Blindness Detection dataset. Tier 1 runs a lightweight MobileNetV3-small model on a local clinic device to perform a binary triage between Referable DR (Classes 2-4) and Non-referable DR (Classes 0-1). Tier 2 runs a RETFoundDINOv2 model in the cloud for ordinal severity grading, but only on the subset of images flagged as referable by Tier 1. On a stratified APTOS test split of 733 images, Tier 1 reaches 98.99% sensitivity and 84.37% specificity at a validation-tuned high-sensitivity threshold. The default cascade forwards 49.52% of test images to Tier 2, reducing cloud calls by 50.48% relative to using a cloud-based model for all images. In the deployed 4-class output space (Class 0-1 / Class 2 / Class 3 / Class 4), the cascade obtains 80.49% accuracy and 0.8167 quadratic weighted kappa; the cloud-only baseline obtains 80.76% accuracy and 0.8184 quadratic weighted kappa. On APTOS, the cascade cuts cloud use by about half with a modest drop in grading performance. Index Terms: Diabetic Retinopathy, Edge-Cloud Cascade, MobileNetV3-small, RETFound-DINOv2, Retinal Screening, tele-ophthalmology

---


### 42. [SToRe3D: Sparse Token Relevance in ViTs for Efficient Multi-View 3D Object Detection](https://arxiv.org/abs/2605.14110)

**<font color=#1a73e8>作者：</font>** Sandro Papais, Lezhou Feng, Charles Cossette 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) enable strong multi-view 3D detection but are limited by high inference latency from dense token and query processing across multiple views and large 3D regions. Existing sparsity methods, designed mainly for 2D vision, prune or merge image tokens but do not extend to full-model sparsity or address 3D object queries. We introduce SToRe3D, a relevance-aligned sparsity framework that jointly selects 2D image tokens and 3D object queries while storing filtered features for reactivation. Mutual 2D-3D relevance heads allocate compute to driving-critical content and preserve other embeddings. Evaluated on nuScenes and our new nuScenes-Relevance benchmark, SToRe3D achieves up to 3x faster inference with marginal accuracy loss, establishing real-time large-scale ViT-based 3D detection while maintaining accuracy on planning-critical agents.

---


### 43. [Modeling Bounded Rationality in Drug Shortage Pharmacists Using Attention-Guided Dynamic Decomposition](https://arxiv.org/abs/2605.14111)

**<font color=#1a73e8>作者：</font>** Yaniv Eliyahu Amiri, Noah Chicoine, Jacqueline Griffin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hospital pharmacists make high-stakes decisions to mitigate drug shortages under uncertainty, time pressure, and patient risk. Interviews revealed that pharmacists focus attention on a small subset of drugs, limiting cognitive effort to the most urgent cases. Motivated by these findings, we formalize a bounded-rational, attention-guided decision framework that dynamically decomposes drugs into a subset for high-cost reasoning and a complementary subset for low-cost monitoring. We develop two agents: an Expert Agent that applies attention weights derived from pharmacist interviews, and a Learner Agent that adapts attention allocation over time through experience. Across simulated scenarios spanning short to long horizons, we show that attention-guided planning supports stable decision-making without complete state reasoning. These results suggest that a primary decision is not what action to take, but where to allocate cognitive effort, and that attention-guided, satisficing strategies can reduce problem complexity while maintaining stable performance.

---


### 44. [Pluot: Towards 'write once, run everywhere' visualization software](https://arxiv.org/abs/2605.14118)

**<font color=#1a73e8>作者：</font>** Mark S. Keller, Nils Gehlenborg  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Tools used for implementing visualization software systems can generally be divided into camps such as static versus interactive and desktop versus web-based. We contribute Pluot, an architecture that bridges these divides, enabling a single software implementation of a visualization to be used regardless of the target level of interactivity or computing environment. With Pluot, a visualization developer implements a given visualization rendering function once, using the Rust programming language. Then, bindings to the Rust program can be generated to enable reproducible execution of the rendering function from other languages, such as Python or JavaScript. Pluot can render visualizations to bitmap or vector graphics format, bridging gaps between interactive performance and publication-quality figure creation. The software is available at this https URL.

---


### 45. [Privacy Preserving Multi Agent Path Finding](https://arxiv.org/abs/2605.14119)

**<font color=#1a73e8>作者：</font>** Rotem Lev Lehman, Roni Stern, Guy Shani  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In the multi-agent path finding (MAPF) problem, a group of agents search in a graph for a path for each agent where no two paths collide. While in all applications of MAPF the agents must not collide with each other, in some of them the agents may not wish to share their paths due to privacy constraints. In this work, we formulate two types of privacy constraints for MAPF and propose algorithms that preserve them. The first type of privacy we consider is planning-level privacy, which means that during planning, the agents cannot identify exactly the planned location of the other agents. We propose a general framework for obtaining planning-level privacy, which works by adding mock agents to the planning process. The second type of privacy we consider is execution-level privacy, which is relevant when agents have limited sensing capabilities. Execution-level privacy is preserved if none of the agents is allowed to sense the location of the other agents during execution. We show how to adapt two popular MAPF algorithms, namely PIBT and LaCAM, such that they preserve execution-level privacy. Lastly, we propose a post-processing technique that allows the agents to reduce the sum of costs of the returned solution without losing any privacy. We also implemented our algorithms and evaluated them empirically, showing that the proposed post-processing technique indeed improved cost significantly.

---


### 46. [ClawForge: Generating Executable Interactive Benchmarks for Command-Line Agents](https://arxiv.org/abs/2605.14133)

**<font color=#1a73e8>作者：</font>** Yuxiang Lai, Peng Xia, Haonian Ji 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive agent benchmarks face a tension between scalable construction and realistic workflow evaluation. Hand-authored tasks are expensive to extend and revise, while static prompt evaluation misses failures that only appear when agents operate over persistent state. Existing interactive benchmarks have advanced agent evaluation significantly, but most initialize tasks from clean state and do not systematically test how agents handle pre-existing partial, stale, or conflicting artifacts. We present \textbf{ClawForge}, a generator-backed benchmark framework for executable command-line workflows under state conflict. The framework compiles scenario templates, grounded slots, initialized state, reference trajectories, and validators into reproducible task specifications, and evaluates agents step by step over persistent workflow surfaces using normalized end state and observable side effects rather than exact trajectory matching. We instantiate this framework as the ClawForge-Bench (17 scenarios, 6 ability categories). Results across seven frontier models show that the best model reaches only 45.3% strict accuracy, wrong-state replacement remains below 17\% for all models, and the widest model separation (17% to 90%) is driven by whether agents inspect existing state before acting. Partial-credit and step-efficiency analyses further reveal that many failures are near-miss closures rather than early breakdowns, and that models exhibit qualitatively different failure styles under state conflict.

---


### 47. [PanoPlane: Plane-Aware Panoramic Completion for Sparse-View Indoor 3D Gaussian Splatting](https://arxiv.org/abs/2605.14135)

**<font color=#1a73e8>作者：</font>** Adil Qureshi, Dongki Jung, Jaehoon Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PanoPlane, an approach for high-fidelity sparse-view indoor novel view synthesis that reconstructs closed room geometry via panoramic scene completion. Unlike perspective-based methods that generate training views from limited fields of view, PanoPlane leverages $360^{\circ}$ panoramic completion to condition the generative process on the full spatial layout. We propose Layout Anchored Attention Steering, a training-free mechanism that steers attention within the diffusion model's internal representation toward scene's detected planar surfaces at inference time. By directing each unobserved region's attention toward geometrically consistent observed content, our method replaces unconstrained hallucination with grounded surface extrapolation. The resulting panoramic completions provide supervision for 3D Gaussian Splatting, enabling accurate novel-view synthesis across unobserved regions from as few as three input views. Experiments on Replica, ScanNet++, and Matterport3D demonstrate state-of-the-art novel view synthesis quality across 3, 6, and 9 input views, achieving up to $+17.8\%$ improvement in PSNR over the current state-of-the-art baseline without any training or fine-tuning of the diffusion model.

---


### 48. [TeDiO: Temporal Diagonal Optimization for Training-Free Coherent Video Diffusion](https://arxiv.org/abs/2605.14136)

**<font color=#1a73e8>作者：</font>** Nurislam Tursynbek, Zhiqiang Lao, Heather Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-video diffusion transformers generate visually compelling frames, yet still struggle with temporal coherence, often producing flickering, drifting, or unstable motion. We show that these failures leave a clear imprint inside the model: incoherent videos consistently exhibit irregular, fragmented temporal diagonals in their intermediate self-attention maps, whereas stable motion corresponds to smooth, band-diagonal patterns. Building on this observation, we introduce TeDiO, a training-free, inference-time method that reinforces temporal consistency by regularizing these internal attention patterns. TeDiO estimates diagonal smoothness, identifies unstable regions, and performs lightweight latent updates that promote coherent frame-to-frame dynamics, without modifying model weights or using external motion supervision. Across multiple video diffusion models (e.g., Wan2.1, CogVideoX), TeDiO delivers markedly smoother motion while preserving per-frame visual quality, offering an efficient plug-and-play approach to improving dynamic realism in modern video generation systems.

---


### 49. [Rethinking the Good Enough Embedding for Easy Few-Shot Learning](https://arxiv.org/abs/2605.14145)

**<font color=#1a73e8>作者：</font>** Michael Karnes, Alper Yilmaz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The field of deep visual recognition is undergoing a paradigm shift toward universal representations. The Platonic Representation Hypothesis suggests that diverse architectures trained on massive datasets are converging toward a shared, "ideal" latent space. This again raises a critical question: is a "Good Embedding All You Need?" In this paper, we leverage this convergence to demonstrate that off-the-shelf embeddings are inherently "good enough" for complex tasks, rendering intensive task-specific fine-tuning unnecessary. We explore this hypothesis within the few-shot learning framework, proposing a straightforward, non-parametric pipeline that entirely bypasses backpropagation. By utilizing a k-Nearest Neighbor classifier on frozen DINOv2-L features, we conduct a layer-wise characterization to identify an optimal feature extraction. We further demonstrate that manifold refinement via PCA and ICA provides a beneficial regularizing effect. Our results across four major benchmarks demonstrate that our approach consistently surpasses sophisticated meta-learning algorithms, achieving state-of-the-art performance.

---


### 50. [bde: A Python Package for Bayesian Deep Ensembles via MILE](https://arxiv.org/abs/2605.14146)

**<font color=#1a73e8>作者：</font>** Vyron Arvanitis, Angelos Aslanidis, Emanuel Sommer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> bde is a user-friendly Python package for Bayesian Deep Ensembles with a particular focus on tabular data. Built on an efficient JAX implementation of the sampling-based inference method Microcanonical Langevin Ensembles (MILE), it provides scikit-learn compatible estimators for fast training, efficient Markov Chain Monte Carlo sampling, and uncertainty quantification in both regression and classification tasks.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-337](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
