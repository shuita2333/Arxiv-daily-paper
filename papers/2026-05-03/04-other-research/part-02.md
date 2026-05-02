# 📦 其他研究 | 2026年05月03日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

---

### 51. [Learning Rate Engineering: From Coarse Single Parameter to Layered Evolution](https://arxiv.org/abs/2604.27295)

**<font color=#1a73e8>作者：</font>** Ming-Hong Yao, Di Wang, Jian Cui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning rate scheduling has evolved from the single global fixed rate of early SGD to sophisticated layer-wise adaptive strategies. We systematize this evolution into five generations: (Gen1) global fixed learning rates, (Gen2) global scheduling, (Gen3) parameter-level adaptation, (Gen4) layer-level differentiation, and (Gen5) joint layer-time scheduling. We trace the fundamental motivation behind each transition, showing how the shift from one-size-fits-all to tailoring by layer and time addresses the impossible trinity of transfer learning: lower layers require small updates to preserve general knowledge while higher layers need large updates to adapt to new tasks. Building on this taxonomy, we propose Discriminative Adaptive Layer Scaling (DALS), a unified framework that integrates phase-adaptive cosine scheduling, depth-aware Grokfast gradient filtering, and LARS-style trust ratios into a single coherent optimizer. We benchmark 18 strategies including three DALS variants across all five generations on five datasets: synthetic, CIFAR-10 (from scratch), RTE, TREC-6, and IMDb (fine-tuning). On synthetic, DALS achieves the best accuracy at 98.0%, while DALS-Fast reaches 90% in just 3 epochs. The cross-dataset analysis reveals striking regime-dependent patterns -- no single strategy wins across all regimes. Critically, STLR+Discriminative, the ULMFiT champion, catastrophically fails on from-scratch tasks (43.6% on TREC-6 from scratch vs. 96.8% with RAdam), confirming that directional decay biases are harmful without pretrained features. DALS avoids either extreme, achieving the best synthetic result while maintaining competitive fine-tuning performance.

---


### 52. [Machine Collective Intelligence for Explainable Scientific Discovery](https://arxiv.org/abs/2604.27297)

**<font color=#1a73e8>作者：</font>** Gyoung S. Na, Chanyoung Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deriving governing equations from empirical observations is a longstanding challenge in science. Although artificial intelligence (AI) has demonstrated substantial capabilities in function approximation, the discovery of explainable and extrapolatable equations remains a fundamental limitation of modern AI, posing a central bottleneck for AI-driven scientific discovery. Here, we present machine collective intelligence, a unified paradigm that integrates two fundamental yet distinct traditions in computational intelligence--symbolism and metaheuristics--to enable autonomous and evolutionary discovery of governing equations. It orchestrates multiple reasoning agents to evolve their symbolic hypotheses through coordinated generation, evaluation, critique, and consolidation, enabling scientific discovery beyond single-agent inference. Across scientific systems governed by deterministic, stochastic, or previously uncharacterized dynamics, machine collective intelligence autonomously recovered the underlying governing equations without relying on hand-crafted domain knowledge. Furthermore, the resulting equations reduced extrapolation error by up to six orders of magnitude relative to deep neural networks, while condensing 0.5-1 million model parameters into just 5-40 interpretable parameters. This study marks an important shift in AI toward the autonomous discovery of principled scientific equations.

---


### 53. [Static Attribution of Android Residential Proxy Malware Using Graph Kernels](https://arxiv.org/abs/2604.27302)

**<font color=#1a73e8>作者：</font>** Peter Clark, Yong Guan, Zhonghao Liao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Android residential proxy applications represent a growing class of potentially-unwanted programs (PUPs) that covertly route third-party traffic through end-user devices, enabling ad fraud, credential abuse, and evasion of geolocation controls by sophisticated threat actors. Attributing an unknown APK to a specific proxy network remains challenging due to code reuse, SDK embedding, and obfuscation across proxy families.
We present a static-analysis pipeline for automated proxyware family attribution, extracting graph-structured representations (control-flow and function-call graphs) and behavioral signatures from a labeled corpus of 3,365 Android proxy apps spanning four commercial proxy networks. We evaluate Weisfeiler-Lehman graph kernel features alone and fused with binary capability vectors across multiple classifiers. Using 5-fold DEX-grouped cross-validation to prevent data leakage, SGD achieves a macro F1 of 0.985 on the expanded dataset. To support explainability, we map classifier decisions to automatically generated Yara rules, achieving per-family accuracies up to 88.45\% after filtering non-discriminative signatures.
Finally, we discuss these results in the context of the broader ecosystem. We find that from the expanded dataset, the majority of applications (51.4\%) still available through APKPure still contain embedded proxy SDK code. Further analysis of developer accounts reveals that 23 developers are responsible for other applications also containing such functionality, suggesting continuous and ongoing commercial relationships between proxy providers and developers.

---


### 54. [BoostLoRA: Growing Effective Rank by Boosting Adapters](https://arxiv.org/abs/2604.27308)

**<font color=#1a73e8>作者：</font>** Raviteja Anantha, Nick Levato, Layne C. Price  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) methods face a tradeoff between adapter size and expressivity: ultra-low-parameter adapters are confined to fixed low-rank subspaces, capping performance even with extended training. We propose BoostLoRA, a gradient-boosting framework that overcomes this limit by iteratively training and merging minimal adapters on the examples the current model gets wrong. A ROTATE SVD basis strategy assigns each round to an orthogonal subspace, so cumulative effective rank grows linearly with the number of rounds while each adapter remains ultra-low-rank. After merging, adapters are discarded, leaving zero inference overhead. On Qwen2.5-3B, BoostLoRA reaches 89.1% on GSM8K and 68.8% on MATH-500, surpassing both the best single-shot ultra-low parameter adapter (TinyLoRA) and full fine-tuning; on code generation it reaches 57.2% on MBPP and 80.4% on HumanEval while full fine-tuning drops below the zero-shot baseline. We also demonstrate cross-architecture transfer on protein binding classification with ESM2-650M and cross-entropy training. BoostLoRA is, to our knowledge, the first PEFT method whose effective rank grows with training, separating per-round parameter cost from total representational capacity.

---


### 55. [End-to-End Evaluation and Governance of an EHR-Embedded AI Agent for Clinicians](https://arxiv.org/abs/2604.27309)

**<font color=#1a73e8>作者：</font>** Aaryan Shah, Andrew Hines, Alexia Downs 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical AI systems require not just point-in-time evaluation but continuous governance: the ongoing practice of monitoring, evaluating, iterating, and re-evaluating performance throughout deployment. We present an end-to-end framework of governance that integrates rubric validation, live deployment feedback, technical performance monitoring, and cost tracking, with controlled experimentation gating system changes before deployment. Applied to Hyperscribe, an EHR-embedded agent that converts ambient audio into structured chart updates, twenty clinicians authored 1,646 validated rubrics across 823 cases. Seven Hyperscribe versions were evaluated through controlled experiments, with median scores improving from 84% to 95%. Analysis of 107 live feedback entries over three months showed feedback composition shifting from 79% error reports and 14% positive observations to 30% errors and 45% positive observations as engineering interventions resolved failures. Median processing time per audio segment was 8.1 seconds with a 99.6% effective completion rate after retry mechanisms absorbed transient model errors. These results demonstrate that continuous, multi-channel governance of deployed clinical AI is both achievable and effective.

---


### 56. [PINN-Cast: Exploring the Role of Continuous-Depth NODE in Transformers and Physics Informed Loss as Soft Physical Constraints in Short-term Weather Forecasting](https://arxiv.org/abs/2604.27313)

**<font color=#1a73e8>作者：</font>** Hira Saleem, Flora Salim, Cormac Purcell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operational weather prediction has long relied on physics-based numerical weather prediction (NWP), whose accuracy comes at the cost of substantial compute and complex simulation workflows. Recent transformer-based forecasters offer efficient data-driven alternatives, however transformers are physics-agnostic models. Additionally, standard transformer encoders evolve representations through discrete layer updates that may be less suited to modeling smooth latent dynamics. In this work, we propose a continuous-depth transformer encoder for weather forecasting that integrates Neural Ordinary Differential Equation (Neural ODE) dynamics within each encoder block. Specifically, we replace discrete residual updates with ODE-based updates solved using adaptive numerical integration. We also introduce a two-branch attention module that combines conventional patch-wise self-attention with an auxiliary branch that applies a derivative operator to attention logits, providing an additional change-sensitive interaction signal. To further align forecasts with governing principles, we propose a customized physics-informed training objective that enforces physical consistency as a soft constraint. We evaluate the proposed method against a standard discrete transformer baseline and an existing continuous-time Neural ODE forecasting variant, demonstrating the importance of PINN-Cast in short term weather forecasting.

---


### 57. [YOSE: You Only Select Essential Tokens for Efficient DiT-based Video Object Removal](https://arxiv.org/abs/2604.27322)

**<font color=#1a73e8>作者：</font>** Chenyang Wu, Lina Lei, Fan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Diffusion Transformer (DiT)-based video generation technologies have shown impressive results for video object removal. However, these methods still suffer from substantial inference latency. For instance, although MiniMax Remover achieves state-of-the-art visual quality, it operates at only around 10FPS, primarily due to dense computations over the entire spatiotemporal token space, even when only a small masked region actually requires processing. In this paper, we present YOSE, You Only Select Essential Tokens, an efficient fine-tuning framework. YOSE introduces two key components: Batch Variable-length Indexing (BVI) and Diffusion Process Simulator (DiffSim) Module. BVI is a differentiable dynamic indexing operator that adaptively selects essential tokens based on mask information, enabling variable-length token processing across samples. DiffSim provides a diffusion process approximation mechanism for unmasked tokens, which simulates the influence of unmasked regions within DiT self-attention to maintain semantic consistency for masked tokens. With these designs, YOSE achieves mask-aware acceleration, where the inference time scales approximately linearly with the masked regions, in contrast to full-token diffusion methods whose computation remains constant regardless of the mask size. Extensive experiments demonstrate that YOSE achieves up to 2.5X speedup in 70% of cases while maintaining visual quality comparable to the baseline. Code is available at: this https URL.

---


### 58. [A Short Note on Batch-efficient Divide-and-Conquer Algorithm for EigenDecomposition](https://arxiv.org/abs/2604.27325)

**<font color=#1a73e8>作者：</font>** Yue Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EigenDecomposition (ED) is at the heart of many computer vision algorithms and applications. One crucial bottleneck limiting its usage is the expensive computation cost, particularly for a mini-batch of matrices in deep neural networks. Our previous work proposed a dedicated QR-based ED algorithm for batched small matrices (dim${<}32$). This short paper targets the limitation and proposes a batch-efficient Divide-and-Conquer based ED algorithm for larger matrices. The numerical test shows that for a mini-batch of matrices whose dimensions are smaller than $64$, our method can be much faster than the Pytorch SVD function.

---


### 59. [Gait Recognition via Deep Residual Networks and Multi-Branch Feature Fusion](https://arxiv.org/abs/2604.27353)

**<font color=#1a73e8>作者：</font>** Yabo Luo, Xiaoyun Wang, Cunrong Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait recognition has emerged as a compelling biometric modality for surveillance and security applications, offering inherent advantages such as non-intrusiveness, resistance to disguise, and long-range identification capability. However, prevailing approaches struggle to comprehensively capture and exploit the rich biometric cues embedded in human locomotion, particularly under covariate interference including viewpoint variation, clothing change, and carrying conditions. In this paper, we present a high-precision gait recognition framework that deeply extracts and synergistically fuses gait dynamics with body shape characteristics through a multi-branch architecture grounded in deep residual learning. Specifically, we first employ the High-Resolution Network (HRNet) to perform robust skeletal keypoint estimation, preserving fine-grained spatial information even under low-resolution inputs. We then construct three complementary feature branches -- body proportion, gait velocity, and skeletal motion -- from the extracted pose sequences. A 50-layer Residual Network (ResNet-50) backbone is leveraged within a deep feature extraction module to capture hierarchically rich and discriminative representations. To effectively integrate heterogeneous feature streams, we design a Multi-Branch Feature Fusion (MFF) module inspired by channel-wise attention mechanisms, which dynamically allocates contribution weights across branches through learned activation parameters. Extensive experiments on the cross-view multi-condition CASIA-B benchmark demonstrate that our method achieves a Rank-1 accuracy of 94.52\% under normal walking, with the best recognition performance among skeleton-based methods for the coat-wearing condition.

---


### 60. [CoAX: Cognitive-Oriented Attribution eXplanation User Model of Human Understanding of AI Explanations](https://arxiv.org/abs/2604.27354)

**<font color=#1a73e8>作者：</font>** Louth Bin Rawshan, Zhuoyu Wang, Brian Y. Lim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) aims to improve user understanding and decisions when using AI models. However, despite innovations in XAI, recent user evaluations reveal that this goal remains elusive. Understanding human cognition can help explain why users struggle to effectively use AI explanations. Focusing on reasoning on structured (tabular) data, we examined various reasoning strategies for different XAI methods (none, feature importance, feature attribution) in the decision task of anticipating AI decisions (i.e., forward simulation). We i) elicited reasoning strategies from a formative user study, and ii) collected decisions from a summative user study. Using cognitive modeling, we implemented the processes underlying each reasoning strategy and evaluated their alignment with human decision-making. We found that our models better fit human decisions than baseline machine learning proxies, providing insights into which reasoning strategies are (in)effective. We then demonstrate how the fitted model can be used to form hypotheses and investigate research questions that are costly to study with real human participants. This work contributes to debugging human understanding of XAI, informing the future development of more usable and interpretable AI explanations.

---


### 61. [TypeBandit: Type-Level Context Allocation and Reweighting for Effective Attribute Completion in Heterogeneous Graph Neural Networks](https://arxiv.org/abs/2604.27356)

**<font color=#1a73e8>作者：</font>** Ta-Yang Wang, Rajgopal Kannan, Viktor Prasanna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous graphs are widely used to model multi-relational systems, but missing node attributes remain a major bottleneck for downstream learning. In this paper, we identify and formalize type-dependent information asymmetry: the phenomenon that different node types provide substantially different levels of useful signal for attribute completion. Motivated by this observation, we propose TypeBandit, a lightweight, model-agnostic methodology for heterogeneous attribute completion. TypeBandit combines topology-aware initialization, type-level bandit sampling, and joint representation learning. It allocates a finite global sampling budget across node types, samples representative nodes within each type, and uses the resulting sampled type summaries as shared contextual signals during representation construction. By operating at the type level rather than over each target node's local neighborhood, TypeBandit keeps the adaptive state compact and practical for large heterogeneous graphs.
A key advantage of TypeBandit is architectural flexibility. Rather than requiring a new heterogeneous graph neural network architecture, TypeBandit acts as a type-aware front end for representative heterogeneous GNN backbones, including R-GCN, HetGNN, HGT, and SimpleHGN. We further introduce a hybrid pretraining scheme that combines structural degree priors with feature propagation, yielding a more reliable initializer than degree-only pretraining. Under a fixed-split protocol on DBLP, IMDB, and ACM, TypeBandit provides dataset-dependent but practically meaningful gains. Additional ablation, stability, efficiency, semantic-propagation, and sampled OGBN-MAG experiments support TypeBandit as a practical strategy for heterogeneous attribute completion when type-specific information is unevenly distributed and sampling resources are limited.

---


### 62. [AG-TAL: Anatomically-Guided Topology-Aware Loss for Multiclass Segmentation of the Circle of Willis Using Large-Scale Multi-Center Datasets](https://arxiv.org/abs/2604.27357)

**<font color=#1a73e8>作者：</font>** Jialu Liu, Yue Cui, Shan Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate multiclass segmentation of the Circle of Willis (CoW) is essential for neurovascular disease management but remains challenging due to complex vascular topology and variable morphology. Existing deep learning methods often suffer from vascular discontinuities and inter-class misclassification, while current topological loss functions incur prohibitive computational costs in 3D multiclass settings. To address these limitations, we propose an Anatomically-Guided Topology-Aware Loss (AG-TAL) and introduce a large-scale, multi-center CoW dataset with unified annotations to facilitate robust model training. AG-TAL specifically integrates a radius-aware Dice loss to address class imbalance in small vessels, a breakage-aware clDice loss that utilizes group convolutions to efficiently preserve local connectivity, and an adjacency-aware co-occurrence loss that leverages anatomical priors to enforce distinct boundaries between neighboring arteries. Evaluated using 5-fold cross-validation, AG-TAL achieved an average Dice score of 80.85% for all CoW arteries, with small arteries notably higher by 1.05-3.09% compared to state-of-the-art methods. Across six independent datasets, the performance of AG-TAL achieved Dice scores ranging from 74.46% to 81.17% for all CoW arteries, with improvements of 2.20% to 9.98% for small arteries compared to other methods. This study demonstrates the superiority of AG-TAL in identifying multiclass CoW arteries and its ability to generalize well to multiple independent datasets. Furthermore, reliability analyses and clinical applications in an Alzheimer's disease cohort validate the AG-TAL's robustness and its potential for discovering imaging-based morphological biomarkers.

---


### 63. [Safe Bilevel Delegation (SBD): A Formal Framework for Runtime Delegation Safety in Multi-Agent Systems](https://arxiv.org/abs/2604.27358)

**<font color=#1a73e8>作者：</font>** Yuan Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM) agents are deployed in high-stakes environments, the question of how safely to delegate subtasks to specialized sub-agents becomes critical. Existing work addresses multi-agent architecture selection at design time or provides broad empirical guidelines, but neither provides a runtime mechanism that dynamically adjusts the safety-efficiency trade-off as task context changes during execution.
We propose Safe Bilevel Delegation (SBD), a formal framework for runtime delegation safety in hierarchical multi-agent systems. SBD formulates task delegation as a bilevel optimization problem: an outer meta-weight network phi learns context-dependent safety-efficiency weights lambda(s) in [0,1]; an inner loop optimizes the delegation policy pi subject to a probabilistic safety constraint P(safe) >= 1-delta. The continuous delegation degree alpha in [0, 1] controls how much decision authority is transferred to each sub-agent, interpolating smoothly between full human override (alpha=0) and fully autonomous execution (alpha=1).
We establish three theoretical results: (1) Safety Monotonicity--higher outer safety weight produces a weakly safer inner policy; (2) Inner Policy Convergence--projected gradient descent on the inner problem converges linearly under standard smoothness assumptions; (3) an Accountability Propagation bound that distributes responsibility across multi-hop delegation chains with a provable per-agent ceiling. We instantiate SBD in three high-stakes domains--medical AI (MIMIC-III), financial risk control (S and P 500), and educational agent supervision (ASSISTments)--specifying datasets, safety constraint sets, baselines, and evaluation protocols. This manuscript presents the formal framework and theoretical results in full; empirical validation following the protocols described herein is planned and will be reported in a forthcoming revision.

---


### 64. [TIO-SHACL: Comprehensive SHACL validation for TMF Intent Ontologies](https://arxiv.org/abs/2604.27359)

**<font color=#1a73e8>作者：</font>** Jean Martins, Leonid Mokrushin, Marin Orlic  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intent-based networking promises to revolutionize telecommunications network management by enabling operators to specify high-level goals rather than low-level configurations. The TM Forum Intent Ontology (tio) provides a standardized vocabulary for expressing network intents, yet lacks formal validation mechanisms to ensure intent correctness before its admission. We present tio-shacl, the first comprehensive SHACL (Shapes Constraint Language) validation framework for the TMF Intent Ontology. Our contribution includes 56 node shapes and 69 property shapes across all 15 tio v3.6.0 ontology modules, a reusable constraint library with 25 parameterized SPARQL-based constraint components, and novel validation patterns for recursive logical operators, quantity-based constraints, and cross-expectation relationships. We pursued 100% vocabulary coverage (87 classes, 109 properties, 72 functions), cross-implementation compatibility across three major SHACL engines, and validation accuracy on a corpus of 133 test cases. tio-shacl is publicly available under MIT license at this https URL and enables automated syntactic and semantic validation of network intents, addressing a critical gap in the field.

---


### 65. [CasLayout: Cascaded 3D Layout Diffusion for Indoor Scene Synthesis with Implicit Relation Modeling](https://arxiv.org/abs/2604.27361)

**<font color=#1a73e8>作者：</font>** Yingrui Wu, Youkang Kong, Mingyang Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing realistic 3D indoor scenes remains challenging due to data scarcity and the difficulty of simultaneously enforcing global architectural constraints and local semantic consistency. Existing approaches often overlook structural boundaries or rely on fully connected relation graphs that introduce redundant generation errors. Inspired by human design cognition, we present CasLayout, a cascaded diffusion framework that decomposes the joint scene generation task into four conditional sub-stages with explicit physical and semantic roles: (1) predicting furniture quantity and categories, (2) refining object sizes and feature embeddings, (3) modeling spatial relationships in a latent space, and (4) generating Oriented Bounding Boxes (OBBs). This decoupled architecture reduces data requirements and enables flexible integration of Large Language Models (LLMs) and Vision Language Models (VLMs) for zero-shot tasks such as image-to-scene generation. To maintain physical validity within complex floor plans, we explicitly model building elements (e.g., walls, doors, and windows) as conditional constraints. Furthermore, to address the high entropy of dense relation graphs, we introduce a sparse relation graph formulation aligned with human spatial descriptions. By encoding these sparse graphs into a compact latent space using a bidirectional Variational Autoencoder (VAE), the proposed framework provides enhanced relational controllability, allowing generated layouts to better respect functional organization. Experiments demonstrate that CasLayout achieves state-of-the-art performance in fidelity and diversity while enabling improved controllability in practical applications.

---


### 66. [Hyperspectral Image Classification via Efficient Global Spectral Supertoken Clustering](https://arxiv.org/abs/2604.27364)

**<font color=#1a73e8>作者：</font>** Peifu Liu, Tingfa Xu, Jie Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral image classification demands spatially coherent predictions and precise boundary delineation. Yet prevailing superpixel-based methods face an inherent contradiction: clustering aggregates similar pixels into regions, but the subsequent classifier operates pixel-wise, undermining regional consistency. Consequently, existing approaches do not guarantee region-level, boundary-aligned classification. To address this limitation, we propose the Dual-stage Spectrum-Constrained Clustering-based Classifier (DSCC), an end-to-end framework that explicitly decouples clustering from classification by first grouping spectral similar and spatially proximate pixels into spectral supertokens and then performing token-level prediction. At its core, DSCC computes an image-level multi-criteria feature distance between pixels and centers, followed by a locality-aware assignment regularization, enabling the generation of boundary-preserving spectral supertokens. A density-isolation based center selection further yields representative, well-separated centers, reducing redundancy and improving robustness to scale variation. To accommodate mixed land-cover compositions within each token, we introduce a soft-label scheme that encodes class proportions and improves robustness for mixed-class tokens. DSCC attains a CF1 of 0.728 at 197.75 FPS on the WHU-OHS dataset, offering a superior accuracy-efficiency trade-off compared with state-of-the-art methods. Extensive experiments further validate the effectiveness and generality of the proposed dual-stage paradigm for hyperspectral image classification. The source code is available at this https URL.

---


### 67. [Judge, Then Drive: A Critic-Centric Vision Language Action Framework for Autonomous Driving](https://arxiv.org/abs/2604.27366)

**<font color=#1a73e8>作者：</font>** Lijin Yang, Jianing Huang, Zhongzhan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision language action (VLA) models have shown remarkable potential for autonomous driving by directly mapping multimodal inputs to control signals. However, previous VLA-based methods have not explicitly exploited the critic capability of VLAs to refine driving decisions, even though such capability has been well demonstrated in other LLM-based domains, thereby limiting their performance in complex closed-loop scenarios. In this work, we present a theoretically inspired two-stage framework, CriticVLA, which extends the role of VLAs from acting to judging. CriticVLA first generates a rough trajectory and then refines it through multimodal evaluation and single-step optimization guided by a VLA-based critic, yielding higher-quality driving behaviors. To support this process, we construct a large-scale synthetic dataset of 12.9 million annotated trajectories covering diverse driving scenarios, which enhances the critic's reasoning and refinement abilities. Extensive closed-loop experiments on the Bench2Drive benchmark show that CriticVLA significantly surpasses state-of-the-art baselines, achieving a 73.33% total success rate and delivering about 30% improvement in challenging scenarios.

---


### 68. [Stable but Wrong: An Inference Limit in Galactic Archaeology](https://arxiv.org/abs/2604.27368)

**<font color=#1a73e8>作者：</font>** Zhipeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Statistical inference in observational science typically relies on a fundamental assumption: as sample size increases and uncertainties decrease, the inferred results should converge to the true physical quantities. This assumption underpins the notion that big data lead to more reliable conclusions. In Galactic archaeology, stellar ages inferred from spectroscopic surveys are widely used to reconstruct the formation history of the Milky Way disk. The age metallicity relation (AMR) and its derived formation timescale are often regarded as key physical diagnostics of early disk evolution. This interpretation carries an implicit premise: that observational quality does not introduce systematic bias into age inference. Here we show that this premise may fail. Using a large sample of subgiant stars, we identify a region in the observational quality parameter space (signal-to-noise ratio and parallax precision) where the inferred formation timescale exhibits a systematic offset of 0.5-1 Gyr relative to an independent asteroseismic reference, while the statistical uncertainties remain small, thus producing a stable-but-wrong inference state.

---


### 69. [Emotion-Aware Clickbait Attack in Social Media](https://arxiv.org/abs/2604.27369)

**<font color=#1a73e8>作者：</font>** Syed Mhamudul Hasan, Mohd. Farhan Israk Soumik, Abdur R. Shahid  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clickbait is characterized by disproportionately high emotional intensity relative to informational content, often reinforced by specific structural patterns. However, current research considers clickbait as a static textual phenomenon characterized by linguistic patterns and structural cues. Additionally, existing detection systems primarily rely on surface-level features of clickbait. This paper introduces an emotion-aware clickbait generation attack, where stylistic transformations are used to optimize emotional impact. We propose an emotion-aware framework based on the Valence-Arousal-Dominance (VAD) space to model the emotional dynamics underlying clickbait generation for optimal user engagement. To simulate realistic attack scenarios, we align clickbait headlines with semantically similar social media posts using Sentence-BERT and generate multiple stylistic rewrites via Large Language Models (LLMs). Building on this, we define a Curiosity Gap (CG) function that computes clickbait's headline variation to the current post to quantify how emotional activation will contribute to user curiosity and evade the existing system found on social media. Experimental results demonstrate that emotion-aware stylization significantly degrades the performance of state-of-the-art classifiers, leading to misclassification rates of up to 2.58% to 30.63% on the base system.

---


### 70. [Measurement Risk in Supervised Financial NLP: Rubric and Metric Sensitivity on JF-ICR](https://arxiv.org/abs/2604.27374)

**<font color=#1a73e8>作者：</font>** Sidi Chang, Peiying Zhu, Yuxiao Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLMs become credible readers of earnings calls, investor-relations Q\&A, guidance, and disclosure language, supervised financial NLP benchmarks increasingly function as decision evidence for model selection and deployment. A hidden assumption is that gold labels make such evidence objective. This assumption breaks down when the benchmark ruler itself is sensitive to rubric wording, metric choice, or aggregation policy. We study this measurement risk on Japanese Financial Implicit-Commitment Recognition (JF-ICR; a pinned 253-item test split x 4 frontier LLMs x 5 rubrics x 3 temperatures x 5 ordinal metrics). Three findings follow. First, rubric wording materially changes model-assigned labels: R2--R3 agreement ranges from 70.0% to 83.4%, with the dominant movement near the +1 / 0 implicit-commitment boundary. This pattern is consistent with a pragmatic-boundary interpretation, but is not a validated linguistic-causality claim because the present rubric variants confound semantics, examples, and verbosity. Second, not every metric remains informative under the JF-ICR class distribution. Within-one accuracy is too easy because near misses receive credit and the majority class dominates; worst-class accuracy is too noisy because the rarest class has only two examples. Exact accuracy, macro-F1, and weighted \k{appa} are therefore the identifiable metrics under our operational rule. Third, ranking claims become more defensible only after this metric-identifiability audit: Bradley--Terry, Borda, and Ranked Pairs agree on the identifiable metric subset, while the full five-metric sweep produces disagreement on the closest pair. The contribution is not a new leaderboard, but a reporting discipline for supervised financial benchmarks whose gold labels exist and whose evaluation ruler still requires governance.

---


### 71. [VeraRetouch: A Lightweight Fully Differentiable Framework for Multi-Task Reasoning Photo Retouching](https://arxiv.org/abs/2604.27375)

**<font color=#1a73e8>作者：</font>** Yihong Guo, Youwei Lyu, Jiajun Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning photo retouching has gained significant traction, requiring models to analyze image defects, give reasoning processes, and execute precise retouching enhancements. However, existing approaches often rely on non-differentiable external software, creating optimization barriers and suffering from high parameter redundancy and limited generalization. To address these challenges, we propose VeraRetouch, a lightweight and fully differentiable framework for multi-task photo retouching. We employ a 0.5B Vision-Language Model (VLM) as the central intelligence to formulate retouching plans based on instructions and scene semantics. Furthermore, we develop a fully differentiable Retouch Renderer that replaces external tools, enabling direct end-to-end pixel-level training through decoupled control latents for lighting, global color, and specific color adjustments. To overcome data scarcity, we introduce AetherRetouch-1M+, the first million-scale dataset for professional retouching, constructed via a new inverse degradation workflow. Furthermore, we propose DAPO-AE, a reinforcement learning post-training strategy that enhances autonomous aesthetic cognition. Extensive experiments demonstrate that VeraRetouch achieves state-of-the-art performance across multiple benchmarks while maintaining a significantly smaller footprint, enabling mobile deployment. Our code and models are publicly available at this https URL.

---


### 72. [Proactive Dialogue Model with Intent Prediction](https://arxiv.org/abs/2604.27379)

**<font color=#1a73e8>作者：</font>** Yang Luo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialogue models are inherently reactive, responding to the current user turn without anticipating upcoming intents, which leads to redundant interactions in multi-intent settings. We address this limitation by introducing a lightweight intent-transition prior derived from dialogue data and injected into the system prompt at inference time. We instantiate this prior using a Temporal Bayesian Network (T-BN) trained on per-turn intent annotations in MultiWOZ 2.2. The T-BN achieves Recall@5 = 0.787 and MRR = 0.576 on 1,071 held-out USER-turn pairs. In a ground-truth replay over 200 dialogues, BN-guided generation improves Coverage AUC from 0.742 to 0.856 and reduces the number of turns required to reach 75% intent coverage from 3.95 to 2.73. These results show that lightweight intent-transition guidance enables more proactive and efficient dialogue behavior without modifying the underlying language model.

---


### 73. [Robust Learning on Heterogeneous Graphs with Heterophily: A Graph Structure Learning Approach](https://arxiv.org/abs/2604.27387)

**<font color=#1a73e8>作者：</font>** Yihan Zhang, Ercan E. Kuruoglu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Heterogeneous graphs with heterophily have emerged as a powerful abstraction for modeling complex real-world systems, where nodes of different types and labels interact in diverse and often non-homophilous ways. Despite recent advances, robust representation learning for such graphs remains largely unexplored, particularly in the presence of noisy or misleading connectivity. In this work, we investigate this problem and identify structural noise as a critical challenge that significantly degrades model performance. To address this issue, we propose a unified framework, Heterogeneous Graph Unified Learning (HGUL), which jointly handles heterophily and noisy graph structures. The framework consists of three complementary modules: a kNN-based graph construction module that recovers reliable local neighborhoods, a graph structure learning module that adaptively refines the adjacency by filtering noisy edges, and a heterogeneous affinity learning module that captures class-level relationships via an extended affinity matrix derived from a polynomial graph kernel. Extensive experiments on multiple datasets demonstrate that HGUL consistently outperforms existing methods on clean graphs and maintains strong robustness under varying levels of structural noise. The results further underscore the importance of jointly modeling heterophily and noise in heterogeneous graph learning.

---


### 74. [Leading Across the Spectrum of Human-AI Relationships: A Conceptual Framework for Increasingly Heterogeneous Teams](https://arxiv.org/abs/2604.27392)

**<font color=#1a73e8>作者：</font>** Alejandro R. Jadad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What shapes a consequential decision when human and artificial intelligence work on it together? The answer is becoming harder to see. A decision may look human-led after AI has set the frame, or appear automated while human judgment still carries decisive force. This paper offers a leadership-facing spectrum to see those relationships within a bounded mandate: Pure Human, Centaur (human-dominant, with AI in the loop), Co-equal, Minotaur (AI-dominant, with humans in the loop), and Pure AI.
The spectrum asks where leadership work occurs: who frames the problem, who redirects the work, and who can answer for what follows. The five positions are landmarks that help leaders recognize configurations as they layer, drift, or change in a single decision. The central risk is misrecognition: leaders may keep a human-centered story in place after decision-shaping authority has shifted elsewhere. They may believe oversight remains meaningful when it has become ceremonial, or keep humans in the loop when their involvement could make the decision worse. The framework introduces co-adaptability, the capacity of a configuration to improve as human and non-human participants adjust together, and places it within heterogeneous teaming, where participants may vary by number, substrate, model architecture, capability, speed, memory, and form of participation.
The aim is practical: to help strategic leaders and those designing or deploying AI systems recognize the configuration at work, notice when it shifts, and judge whether it fits the decision before them. These configurations will shape how power, responsibility, and trust are distributed in organizational life. Whether the futures they help create remain governable and worth inhabiting will depend on leaders who can see, early enough, where and how consequential decisions are actually being shaped.

---


### 75. [Why Mean Pooling Works: Quantifying Second-Order Collapse in Text Embeddings](https://arxiv.org/abs/2604.27398)

**<font color=#1a73e8>作者：</font>** Tomomasa Hara, Hiroto Kurita, Masaaki Imaizumi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For constructing text embeddings, mean pooling, which averages token embeddings, is the standard approach. This paper examines whether mean pooling actually works well in real models. First, we note that mean pooling can collapse information beyond the first-order statistics of the token embeddings, such as second-order statistics that capture their spatial structure, potentially mapping distinct token embedding distributions to similar text embeddings. Motivated by this concern, we propose a simple metric to quantify such a collapse induced by mean pooling. Then, using this metric, we empirically measure how often this collapse occurs in actual models and texts, and find that modern text encoders are robust to this collapse. In particular, contrastive fine-tuned text encoders tend to be less prone to the collapse than their pretrained backbone models. We also find that the robustness of these text encoders lies in the concentration of token embeddings within each text. In addition, we find that robustness to the collapse, as quantified by our proposed metric, correlates with downstream task performance. Overall, our findings offer a new perspective on why modern text encoders remain effective despite relying on seemingly coarse mean pooling.

---


### 76. [Detecting is Easy, Adapting is Hard: Local Expert Growth for Visual Model-Based Reinforcement Learning under Distribution Shift](https://arxiv.org/abs/2604.27411)

**<font color=#1a73e8>作者：</font>** Haiyang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual model-based reinforcement learning (MBRL) agents can perform well on the training distribution, but often break down once the test environment shifts. In visual MBRL, recognizing that a shift has occurred is often the easier part; the harder part is turning that recognition into useful action-level correction. We study several ways of responding to shift, including planning penalties, direct fine-tuning, global residual correction, and coarse gating. In our experiments, these approaches either do not improve closed-loop control or hurt in-distribution (ID) performance. Based on these negative results, we propose JEPA-Indexed Local Expert Growth. The method uses a frozen JEPA representation only for problem indexing, while cluster-specific residual experts add local action corrections on top of the original controller. The baseline controller itself is not modified. Using paired-bootstrap evaluation, we find that the original naive-preference variant is not stable under stricter testing. In contrast, the harder-pair variant produces statistically significant OOD improvements on all four evaluated shift conditions while preserving ID performance. The learned experts also remain useful when the same shift is encountered again, which supports the view of adaptation as incremental knowledge growth rather than repeated full retraining. We further show that automatic ID rejection can be achieved with simple density models, whereas fine-grained discrimination among OOD sub-families is limited by the representation. Overall, the results indicate that, for visual MBRL under distribution shift, the main challenge is not simply noticing that the environment has changed, but applying the right local action correction after the change has been recognized.

---


### 77. [Sparse-View 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2604.27422)

**<font color=#1a73e8>作者：</font>** Wongi Park, Jordan A. James, Myeongseok Nam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a 3D novel sparse-view synthesis framework for unconstrained real-world scenarios that contain distractors. Unlike existing methods that primarily perform novel-view synthesis from a sparse set of constrained images without transient elements or leverage unconstrained dense image collections to enhance 3D representation in real-world scenarios, our method not only effectively tackles sparse unconstrained image collections, but also shows high-quality 3D rendering results. To do this, we introduce reference-guided view refinement with a diffusion model using a transient mask and a reference image to enhance the 3D representation and mitigate artifacts in rendered views. Furthermore, we address sparse regions in the Gaussian field via pseudo-view generation along with a sparsity-aware Gaussian replication strategy to amplify Gaussians in the sparse regions. Extensive experiments on publicly available datasets demonstrate that our methodology consistently outperforms existing methods (e.g., PSNR - 17.2%, SSIM - 10.8%, LPIPS - 4.0%) and provides high-fidelity 3D rendering results. This advancement paves the way for realizing unconstrained real-world scenarios without labor-intensive data acquisition. Our project page is available at $\href{this https URL}{here}$

---


### 78. [AdaBFL: Multi-Layer Defensive Adaptive Aggregation for Bzantine-Robust Federated Learning](https://arxiv.org/abs/2604.27434)

**<font color=#1a73e8>作者：</font>** Zehui Tang, Yuchen Liu, Feihu Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a popular distributed learning paradigm in machine learning, which enables multiple clients to collaboratively train models under the guidance of a server without exposing private client data. However, FL's decentralized nature makes it vulnerable to poisoning attacks, where malicious clients can submit corrupted models to manipulate the system. To counter such attacks, although various Byzantine-robust methods have been proposed, these methods struggle to provide balanced defense against multiple types of attacks or rely on possessing the dataset in the server. To deal with these drawbacks, thus, we propose an effective multi-layer defensive adaptive aggregation for Bzantine-robust federated learning (AdaBFL) based on a novel three-layer defensive mechanism, which can adaptively adjust the weights of defense algorithms to counter complex attacks. Moreover, we provide convergence properties of our AdaBFL method under the non-convex setting on non-iid data. Comprehensive experiments across multiple datasets validate the superiority of our AdaBFL over the comparable algorithms.

---


### 79. [Softmax-GS: Generalized Gaussians Learning When to Blend or Bound](https://arxiv.org/abs/2604.27437)

**<font color=#1a73e8>作者：</font>** Chen Ziwen, Peng Wang, Hao Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3D GS) is widely adopted for novel view synthesis due to its high training and rendering efficiency. However, its efficiency relies on the key assumption that Gaussians do not overlap in the 3D space, which leads to noticeable artifacts and view inconsistencies. In addition, the inherently diffuse boundaries of Gaussians hinder accurate reconstruction of sharp object edges. We propose Softmax-GS, a unified solution that addresses both the view-inconsistency and the diffuse-boundary problem by enforcing a softmax-based competition in overlapping regions between two Gaussians. With learnable parameters controlling the strength of the competition, it enables a continuous spectrum from smooth color blending to crisp, well-defined boundaries. Our formulation explicitly preserves order invariance for any two overlapping Gaussians and ensures that the output transmittance remains unchanged irrespective of the extent of overlapping, preventing undesirable discontinuities in the rendered output. Ablation experiments on simple geometries demonstrate the effectiveness of each component of Softmax-GS, and evaluations on real-world benchmarks show that it achieves state-of-the-art performance, improving both reconstruction quality and parameter efficiency.

---


### 80. [Tracking Conversations: Measuring Content and Identity Exposure on AI Chatbots](https://arxiv.org/abs/2604.27438)

**<font color=#1a73e8>作者：</font>** Muhammad Jazlan, Ethan Wang, Yash Vekaria 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI chatbots are becoming a primary interface for seeking information. As their popularity grows, chatbot providers are starting to deploy advertising and analytics. Despite this, tracking on AI chatbots has not been systematically studied. We present a systematic measurement of web tracking on 20 popular AI chatbots. Under controlled settings using a sensitive prompt, we capture and compare network traffic in normal chats and, where supported, private chats. We search for exposure of two categories of information: content, including prompts, prompt-derived titles, chat URLs, and chat identifiers; and identity, including names, emails, account identifiers, first-party cookies, and explicit IP/User-Agent fields in payloads. We find that 17 of 20 chatbots share information with at least one third party. Three chatbots share plaintext conversation text, including both prompt and response snippets, with Microsoft Clarity through session replay. Fifteen chatbots share conversation URLs or chat identifiers with third-party advertising, analytics, or social endpoints. Several chatbots expose user identity through support widgets, analytics, advertising, and session replay tags; in some cases, hashed emails are shared.

---


### 81. [Sentiment Analysis of AI Adoption in Indonesian Higher Education Using Machine Learning and Transformer-Based Models](https://arxiv.org/abs/2604.27439)

**<font color=#1a73e8>作者：</font>** Happy Syahrul Ramadhan, Ahmad Sahidin Akbar, Karin Yehezkiel Sinaga 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study analyzes Indonesian student opinions on the adoption of artificial intelligence in higher education using two approaches: TF-IDF-based machine learning and Transformer-based deep learning. The dataset consists of 2,295 labeled samples, combining 1,154 student opinions with additional lexical sentiment data. LightGBM, Random Forest, and Support Vector Machine (SVM) are evaluated as machine learning models, while DistilBERT is fine-tuned for binary sentiment classification. The results show that SVM achieves the best performance among the machine learning models with 82.14% test accuracy and F1-score, while DistilBERT performs best overall with 84.78% accuracy and 84.75% F1-score. These findings indicate that Transformer-based models better capture contextual information, although SVM remains a competitive and efficient alternative for sentiment classification.

---


### 82. [ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space](https://arxiv.org/abs/2604.27443)

**<font color=#1a73e8>作者：</font>** Gabe Guo, Thanawat Sornwanee, Lutong Hao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating continuous-time, continuous-space stochastic processes (e.g., videos, weather forecasts) conditioned on partial observations (e.g., first and last frames) is a fundamental challenge. Existing approaches, (e.g., diffusion models), suffer from key limitations: (1) noise-to-data evolution fails to capture structural similarity between states close in physical time and has unstable integration in low-step regimes; (2) random noise injected is insensitive to the physical process's time elapsed, resulting in incorrect dynamics; (3) they overlook conditioning on arbitrary subsets of states (e.g., irregularly sampled timesteps, future observations). We propose ABC: Any-Subset Autoregressive Models via Non-Markovian Diffusion Bridges in Continuous Time and Space. Crucially, we model the process with one continual SDE whose time variable and intermediate states track the real time and process states. This has provable advantages: (1) the starting point for generating future states is the already-close previous state, rather than uninformative noise; (2) random noise injection scales with physical time elapsed, encouraging physically plausible dynamics with similar time-adjacent states. We derive SDE dynamics via changes-of-measure on path space, yielding another advantage: (3) path-dependent conditioning on arbitrary subsets of the state history and/or future. To learn these dynamics, we derive a path- and time-dependent extension of denoising score matching. Our experiments show ABC's superiority to competing methods on multiple domains, including video generation and weather forecasting.

---


### 83. [Context as Prior: Bayesian-Inspired Intent Inference for Non-Speaking Agents with a Household Cat Testbed](https://arxiv.org/abs/2604.27445)

**<font color=#1a73e8>作者：</font>** Wenqian Zhang, Zehao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many agents in real-world environments cannot reliably communicate their goals through language, including household pets, pre-verbal infants, and other non-speaking embodied agents. In such settings, intent must be inferred from incomplete behavioral observations in context-rich environments. This creates a core ambiguity: observable behavior is often noisy or underspecified, while context provides strong prior information but can also induce brittle shortcut predictions if used naively.
We present CatSignal, a Bayesian-inspired probabilistic framework for multimodal intent inference that models spatial context as a prior-like constraint and behavioral observations as evidence. Rather than treating context as an ordinary input feature, our method uses a context-gated Product-of-Experts formulation to compute posterior-like intent distributions from context, pose dynamics, and acoustic cues. We instantiate this formulation in a household cat setting as a focused proof-of-concept for intent inference in non-speaking agents.
Under Leave-One-Video-Out evaluation on a multimodal domestic cat dataset, the proposed prior-guided fusion achieves the best overall accuracy of 77.72%, outperforming feature concatenation (71.83%) and stronger late-fusion baselines. More importantly, it substantially reduces context-driven shortcut failures in ambiguous cases. While simpler fusion strategies remain competitive in Macro-F1 and selective prediction, the proposed model provides the strongest overall accuracy and the best suppression of context-based shortcut collapse.

---


### 84. [LA-Pose: Latent Action Pretraining Meets Pose Estimation](https://arxiv.org/abs/2604.27448)

**<font color=#1a73e8>作者：</font>** Zhengqing Wang, Saurabh Nair, Prajwal Chidananda 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper revisits camera pose estimation through the lens of self-supervised pretraining, focusing on inverse-dynamics pretraining as a scalable alternative to the current trend of fully supervised training with 3D annotations. Concretely, we employ inverse- and forward-dynamics models to learn latent action representations, similar to Genie from large-scale driving videos. Our idea is simple yet effective. Existing methods use latent actions in their original capacity, that is, as action conditioning of world-models or as proxies of robot action parameters in policy networks. Our method, dubbed LA-Pose, repurposes the latent action features as inputs to a camera pose estimator, finetuned on a limited set of high-quality 3D annotations. This formulation enables accurate and generalizable pose prediction while maintaining feed-forward efficiency. Extensive experiments on driving benchmarks show that LA-Pose achieves competitive and even superior performance to state-of-the-art methods while using orders of magnitude less labeled data. Concretely, on the Waymo and PandaSet benchmarks, LA-Pose achieves over 10% higher pose accuracy than recent feed-forward methods. To our knowledge, this work is the first to demonstrate the power of inverse-dynamics self-supervised learning for pose estimation.

---


### 85. [From Coarse to Fine: Benchmarking and Reward Modeling for Writing-Centric Generation Tasks](https://arxiv.org/abs/2604.27453)

**<font color=#1a73e8>作者：</font>** Qingyu Ren, Tianjun Pan, Xingzhou Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have achieved remarkable progress in text generation but still struggle with generative writing tasks. In terms of evaluation, existing benchmarks evaluate writing reward models coarsely and fail to measure performance from the perspective of specific requirements. In terms of training, existing training methods either use LLM-as-a-judge approaches or train coarse-grained reward models, lacking fine-grained requirement-adherence reward modeling. To address these issues, we propose a fine-grained evaluation pipeline WEval for writing reward models and a fine-grained reinforcement learning training framework WRL. The evaluation data of WEval covers multiple task categories and requirement types, enabling systematic evaluation of writing reward models by measuring the correlation between the rankings of the reward model and gold rankings. WRL constructs positive and negative samples by selectively dropping instruction requirements, allowing for more precise reward model training. Experiments show that our models achieve substantial improvements across various writing benchmarks and exhibit strong generalization. The code and data are publicly available at \href{this https URL}{this https URL\_Coarse\_to\_Fine}.

---


### 86. [Secure Cross-Silo Synthetic Genomic Data Generation](https://arxiv.org/abs/2604.27456)

**<font color=#1a73e8>作者：</font>** Daniil Filienko, Martine De Cock, Sikha Pentyala  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Access to genomic data is highly regulated due to its sensitive nature. While safeguards are essential, cumbersome data access processes pose a significant barrier to the development of AI methods for genomics. Synthetic data generation can mitigate this tension by enabling broader data sharing without exposing sensitive information. Synthetic genomic data are produced by training generative models on real data and subsequently sampling artificial data that preserves relevant statistics while limiting disclosures about the underlying individuals. In some settings, a single data holder may have sufficient data to train such generative models; however, in many applications data must be combined across multiple sites to achieve adequate scale. This need arises, e.g., in rare disease studies, where individual hospitals typically hold data for only a small number of patients. The solution we present in this paper enables multiple data holders to jointly train a synthetic data generator without revealing their raw data. Our approach combines secure multiparty computation (MPC) to ensure input privacy, so that no party ever discloses its data in unencrypted form, with differential privacy (DP) to provide output privacy by mitigating information leakage from the released synthetic data. We empirically demonstrate the effectiveness of the proposed method by generating high-utility synthetic datasets from multiple real RNA-seq cohorts in federated settings, showing that our approach enables privacy-preserving data synthesis even when data are distributed across institutions.

---


### 87. [Improving Graph Few-shot Learning with Hyperbolic Space and Denoising Diffusion](https://arxiv.org/abs/2604.27462)

**<font color=#1a73e8>作者：</font>** Yonghao Liu, Jialu Sun, Wei Pang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph few-shot learning, which focuses on effectively learning from only a small number of labeled nodes to quickly adapt to new tasks, has garnered significant research attention. Despite recent advances in graph few-shot learning that have demonstrated promising performance, existing methods still suffer from several key limitations. First, during the meta-training phase, these methods typically perform node representation learning in Euclidean space, which often fails to capture the inherently hierarchical structure existing in real-world graph data. Second, during the meta-testing phase, they usually fit an empirical target distribution derived from only a few support samples, even when this distribution significantly deviates from the true underlying distribution. To address these issues, we propose IMPRESS, a novel framework that IMproves graPh few-shot learning with hypeRbolic spacE and denoiSing diffuSion. Specifically, our model learns node representations in a hyperbolic space and enriches the support distribution through denoising diffusion mechanisms. Theoretically, IMPRESS achieves a tighter generalization bound. Empirically, IMPRESS consistently outperforms competitive baselines across multiple benchmark datasets.

---


### 88. [Security Attack and Defense Strategies for Autonomous Agent Frameworks: A Layered Review with OpenClaw as a Case Study](https://arxiv.org/abs/2604.27464)

**<font color=#1a73e8>作者：</font>** Luyao Xu, Xiang Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous agent frameworks built upon large language models (LLMs) are evolving into complex, tool-integrated, and continuously operating systems, introducing security risks beyond traditional prompt-level vulnerabilities. As this paradigm is still at an early stage of development, a timely and systematic understanding of its security implications is increasingly important. Although a growing body of work has examined different attack surfaces and defense problems in agent systems, existing studies remain scattered across individual aspects of agent security, and there is still a lack of a layered review on this topic. To address this gap, this survey presents a layered review of security risks and defense strategies in autonomous agent frameworks, with OpenClaw as a case study. We organize the analysis into four security-relevant layers: the context and instruction layer, the tool and action layer, the state and persistence layer, and the ecosystem and automation layer. For each layer, we summarize its functional role, representative security risks, and corresponding defense strategies. Based on this layered analysis, we further identify that threats in autonomous agent frameworks may propagate across layers, from manipulated inputs to unsafe actions, persistent state contamination, and broader ecosystem-level impact. Finally, we highlight potential key challenges, including research imbalance across layers, the lack of long-horizon evaluation, and weak ecosystem trust models, and outline future directions toward more systematic and integrated defenses.

---


### 89. [Syntactically-guided Information Maintenance in Sentence Comprehension](https://arxiv.org/abs/2604.27468)

**<font color=#1a73e8>作者：</font>** Shinnosuke Isono, Kohei Kajikawa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Maintaining information in context is essential in successful real-time language comprehension, but maintenance is cognitively costly and can slow processing. We hypothesize that rational language users selectively maintain information that is crucial for future prediction, guided by syntactic structure. Under this view, two factors affect maintenance cost: the number of predicted heads and the number of incomplete dependencies. Although these factors have been treated as competing hypotheses in the literature, our account predicts that they are not reducible to one another. We show this is the case, using a naturalistic reading time dataset in Japanese, a language in which the two factors contrast particularly clearly. We further show that there is a tradeoff such that readers that slow down for maintenance tend to benefit more from predictability, providing additional support for the proposed account.

---


### 90. [PRTS: A Primitive Reasoning and Tasking System via Contrastive Representations](https://arxiv.org/abs/2604.27472)

**<font color=#1a73e8>作者：</font>** Yang Zhang, Jiangyuan Zhao, Chenyou Fan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models advance robotic control via strong visual-linguistic priors. However, existing VLAs predominantly frame pretraining as supervised behavior cloning, overlooking the fundamental nature of robot learning as a goal-reaching process that requires understanding temporal task progress. We present \textbf{PRTS} (\textbf{P}rimitive \textbf{R}easoning and \textbf{T}asking \textbf{S}ystem), a VLA foundation model that reformulates pretraining through Goal-Conditioned Reinforcement Learning. By treating language instructions as goals and employing contrastive reinforcement learning, PRTS learns a unified embedding space where the inner product of state-action and goal embeddings approximates the log-discounted goal occupancy, the probability of reaching the language-specified goal from the current state-action, quantitatively assessing physical feasibility beyond static semantic matching. PRTS draws this dense goal-reachability supervision directly from offline trajectories without reward annotations, and folds it into the VLM backbone via a role-aware causal mask, incurring negligible overhead over vanilla behavior cloning. This paradigm endows the high-level reasoning system with intrinsic goal reachability awareness, bridging semantic reasoning and temporal task progress, and further benefits goal-conditioned action prediction. Pretrained on 167B tokens of diverse manipulation and embodied-reasoning data, PRTS reaches state-of-the-art performance on LIBERO, LIBERO-Pro, LIBERO-Plus, SimplerEnv, and a real-world suite of 14 complex tasks, with particularly substantial gains on long-horizon, contact-rich, and zero-shot novel-instruction settings, confirming that injecting goal-reachability awareness significantly improves both execution success and long-horizon planning of general-purpose robotic foundation policies.

---


### 91. [Toward Scalable SDN for LEO Mega-Constellations: A Graph Learning Approach](https://arxiv.org/abs/2604.27478)

**<font color=#1a73e8>作者：</font>** Sivaram Krishnan, Bassel Al Homssi, Zhouyou Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Terrestrial network limitations drive the integration of non-terrestrial networks (NTNs), notably mega-constellations comprising thousands of low Earth orbit (LEO) satellites. While these satellites act as interconnected network switches via inter-satellite links (ISLs), their massive scale creates severe bottlenecks for network management. To address this, we propose a scalable, hierarchical software-defined networking (SDN) framework. Our architecture leverages graph neural networks (GNNs) to compactly represent the constellation topology, and Koopman theory to linearize nonlinear dynamics. Specifically, a Graph Koopman Autoencoder (GKAE) forecasts spatio-temporal behavior within a linear subspace for each orbital shell. A central SDN controller then aggregates these shell-level predictions for globally coordinated control. Simulations on the Starlink constellation demonstrate that our approach achieves at least a 42.8\% improvement in spatial compression and a 10.81\% improvement in temporal forecasting compared to established baselines, all while utilizing a significantly smaller model footprint.

---


### 92. [Why Learners Drift In and Out: Examining Intermittent Discontinuance in AI-Mediated Informal Digital English Learning (AI-IDLE) Using SEM and fsQCA](https://arxiv.org/abs/2604.27493)

**<font color=#1a73e8>作者：</font>** Yiran Du, Huimin He  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examined intermittent discontinuance in AI-mediated informal digital learning of English (AI-IDLE) through the cognition-affect-conation framework. Survey data were collected from 632 Chinese university EFL learners with prior AI-IDLE experience and analysed using structural equation modelling and fuzzy-set qualitative comparative analysis. The SEM results showed that perceived intelligence, perceived interactivity, and perceived personalisation reduced AI-IDLE intermittent discontinuance indirectly through enjoyment, whereas perceived ineffectiveness, perceived uncontrollability, and perceived complexity increased discontinuance indirectly through boredom. The fsQCA results further identified four configurational pathways leading to intermittent discontinuance, indicating that learners' temporary withdrawal from AI-IDLE can result from different combinations of cognitive barriers and affective disengagement. These findings extend AI-IDLE research from adoption and continuance to post-adoption discontinuance and highlight the need to design AI-supported English learning experiences that are enjoyable, personalised, controllable, and cognitively manageable.

---


### 93. [SST-Guard: Detecting and Characterizing Server-Side Google Analytics in the Wild](https://arxiv.org/abs/2604.27497)

**<font color=#1a73e8>作者：</font>** Muhammad Jazlan, Alexander Gamero-Garrido, Zubair Shafiq 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As web browsers increasingly restrict client-side tracking, the web tracking ecosystem is shifting from client-side to server-side tracking (SST). In SST, the browser sends tracking requests to an intermediate endpoint, which then forwards them to the tracker's endpoint, eliminating direct client-to-tracker requests. As a result, existing tracking protections that block requests to known tracker endpoints are rendered ineffective.
In this paper, we investigate server-side implementation of Google Analytics, the most widely deployed third-party tracking service on the web today. We also present SST-Guard, a multi-modal, browser-based system for detecting and blocking server-side Google Analytics (sGA). Our key insight is that even when the tracker's endpoints change, sGA must necessarily still collect and share the same semantic information as client-side Google Analytics (e.g., identifiers, event metadata). Therefore, rather than detecting requests to known Google Analytics endpoints, SST-Guard aims to detect underlying artifacts of collection and sharing of these semantic values to any arbitrary endpoint. Operationalizing this insight is challenging because real-world sGA deployments commonly customize endpoints and obfuscate URLs/payloads. SST-Guard addresses this challenge using a value-template approach that employs regular expressions to match semantic value patterns across multiple modalities: network requests, cookies, and the window object.
We validate SST-Guard on Tranco top-10k websites, detecting 4.02\% (403) sGA domains with over 93\% accuracy across three modalities, with network request classifier demonstrating the highest accuracy (99.8\%). By deploying SST-Guard in the wild, we find 4.21\% (6,314) of Tranco top-150k websites using sGA.

---


### 94. [Towards All-Day Perception for Off-Road Driving: A Large-Scale Multispectral Dataset and Comprehensive Benchmark](https://arxiv.org/abs/2604.27499)

**<font color=#1a73e8>作者：</font>** Shuo Wang, Jilin Mei, Wenfei Guan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Off-road nighttime autonomous driving suffers from unreliable visible-light perception, making infrared modality crucial for accurate freespace detection. However, progress remains limited due to the scarcity of annotated infrared off-road datasets and the inter-frame inconsistencies inherent to current single-frame methods. To address these gaps, we present the IRON dataset, which, to our knowledge, is the first large-scale infrared dataset for off-road temporal freespace detection under all-day conditions, with strong support for nighttime perception. The dataset comprises 24,314 densely annotated infrared images with synchronized RGB images in diverse scenes and different light conditions. Building upon this dataset, we propose IRONet, a novel flow-free framework for temporal freespace detection that addresses inter-frame inconsistencies by aggregating historical context via a memory-attention mechanism and a carefully designed mask decoder. On our IRON dataset, IRONet achieves state-of-the-art performance, reaching 82.93%(+1.19%) IoU and 90.66%(+0.71%) F1 score at real-time inference. Remarkably, IRONet also exhibits robust generalization to RGB modalities on ORFD and Rellis datasets. Overall, our work establishes a foundation for reliable all-day off-road autonomous driving and future research in infrared temporal perception. The code and IRON dataset are available at this https URL.

---


### 95. [From Elastic to Viscoelastic: An EEMD-Enhanced Pulse Transit Time Model for Robust Blood Pressure Estimation](https://arxiv.org/abs/2604.27500)

**<font color=#1a73e8>作者：</font>** Boyuan Gu, Yijin Yang, Shuaiqi Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cuffless blood pressure (BP) estimation based on Pulse Transit Time (PTT) has emerged as a promising solution for continuous health monitoring. However, conventional models relying on the Moens-Korteweg equation often fail during rapid hemodynamic fluctuations, as they assume arterial walls are purely elastic and neglect inherent viscoelasticity. To address this limitation, we propose a physics-informed framework introducing a viscoelastic compensation mechanism. First, raw photoplethysmogram (PPG) signals undergo high-fidelity reconstruction using Modified Akima (Makima) interpolation. Second, a robust Intersecting Tangent Method is applied for precise pulse foot localization. Crucially, we utilize Ensemble Empirical Mode Decomposition (EEMD) to isolate high-frequency Intrinsic Mode Functions (IMFs), defining a ``Viscoelastic Velocity Metric'' to quantify the vascular damping effect ($\eta \cdot \dot{\epsilon}$) typically ignored by elastic models. The framework was rigorously validated on a challenging subset of the MIMIC-II database (364 subjects, 28,525 cardiac cycles) characterized by a high prevalence of hypertension (23.4\%). Experimental results demonstrate medical-grade accuracy, yielding a Root Mean Square Error (RMSE) of 5.22 mmHg for Systolic and 3.65 mmHg for Diastolic BP, with Pearson correlation coefficients ($R > 0.97$). These findings confirm that incorporating viscoelastic features significantly enhances robustness against vascular hysteresis.

---


### 96. [REVIVE 3D: Refinement via Encoded Voluminous Inflated prior for Volume Enhancement](https://arxiv.org/abs/2604.27504)

**<font color=#1a73e8>作者：</font>** Hankyeol Lee, Wooyeol Baek, Seongdo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent generative models have shown strong performance in generating diverse 3D assets from 2D images, a fundamental research topic in computer vision and graphics. However, these models still struggle to generate voluminous 3D assets when the input is a flat image that provides limited 3D cues. We introduce REVIVE 3D, a two-stage, plug-and-play pipeline for generating voluminous 3D assets from flat images. In Stage 1, we construct an Inflated Prior by inflating the foreground silhouette to recover global volume and superimposing part-aware details to capture local structure. In Stage 2, 3D Latent Refinement injects Gaussian noise into the Inflated Prior's latent and then denoises it, using the prior's geometric cues to leverage the backbone's pretrained 3D knowledge. Furthermore, our framework supports image-conditioned 3D editing. To quantify volume and surface flatness, we propose Compactness and Normal Anisotropy. We validate Compactness and Normal Anisotropy through a user study, showing that these metrics align with human perception of volume and quality. We show that REVIVE 3D achieves state-of-the-art performance on a challenging flat image dataset, based on extensive qualitative and quantitative evaluations.

---


### 97. [Examining discontinuance of AI-mediated informal digital learning of English (AI-IDLE) among university students: Evidence from SEM and fsQCA](https://arxiv.org/abs/2604.27506)

**<font color=#1a73e8>作者：</font>** Yiran Du, Huimin He  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examined university students' discontinuance intention towards AI-mediated informal digital learning of English (AI-IDLE). Drawing on the cognition-affect-conation framework, the study investigated how three cognitive factors, namely disconfirmation, perceived complexity, and perceived risk, influence two affective responses, namely dissatisfaction and frustration, and how these affective responses predict discontinuance intention. A cross-sectional survey was conducted with 746 Chinese university students who had experience using AI tools for informal English learning. Data were analysed using structural equation modelling (SEM) and fuzzy-set qualitative comparative analysis (fsQCA). The SEM results showed that dissatisfaction and frustration positively predicted discontinuance intention, with frustration showing the stronger effect. Disconfirmation, perceived complexity, and perceived risk also positively influenced dissatisfaction and frustration. The fsQCA results further identified multiple sufficient configurations leading to high AI-IDLE discontinuance intention, indicating that discontinuance is shaped by causal complexity and equifinality rather than by a single necessary condition. These findings extend AI-IDLE research from adoption and engagement to post-adoption disengagement and provide implications for reducing learners' dissatisfaction, frustration, perceived complexity, and risk in AI-supported informal English learning.

---


### 98. [I'm Fine, But My Voice Isn't: Cross-Modal Affective Dissonance Detection for Reflective Journaling](https://arxiv.org/abs/2604.27517)

**<font color=#1a73e8>作者：</font>** Sumin Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital journaling creates an authenticity gap: users consciously translate raw emotions into text, often sanitizing narratives even in private writing. We formalize this as Cross-Modal Affective Dissonance Detection (CADD), a directional three-way classification distinguishing Masking (positive text, negative acoustics), Coping (negative text, positive acoustics), and Congruent utterances, grounded in Gross's process model of emotion regulation. We present three further contributions: (i) CADD-Journal, a 1,800-sample TTS dataset with a shared-sentence-pool design that provably isolates acoustic signal from textual content; (ii) DACM, a dual-encoder model with asymmetric cross-modal attention that re-solves a gradient degeneracy in pooled fusion, achieving macro-F1 0.711 - with a four-step ablation demonstrating that asymmetric attention is the dominant driver (+ 0.242) while the DIM is effective only on cross-modal features (+0.033); and (iii) a domain gap quantification: zero-shot evaluation across three naturalistic corpora reveals a substantial gap between TTS-trained models and real speech, and we identify two concrete requirements for future in-the-wild corpus construction. ReflectJournal, a proof-of-concept iOS application, operationalizes the framework and provides a deployment platform for naturalistic data collection.

---


### 99. [lpviz: Interactive Linear Programming Visualization](https://arxiv.org/abs/2604.27518)

**<font color=#1a73e8>作者：</font>** Evan Grand, Michael Klamkin  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents lpviz, a browser-based visualization tool for linear programming. lpviz is deeply interactive, offering an intuitive interface where users can directly draw and edit the feasible region and objective vector, without requiring cumbersome manipulation of raw numerical coefficients. lpviz lets users compare the behavior of several classes of linear programming algorithms, namely Simplex, Interior-Point, Primal-Dual Hybrid Gradient, and Central Path. In the 3D mode, lpviz places iterates at heights corresponding to important solver metadata such as complementarity gap or KKT residual, helping users gain further insight into algorithm behavior beyond the primal iterates alone. lpviz has been used in both research and classroom settings, to help develop intuition for the strengths and weaknesses of different solvers and the impact of solver settings on convergence behavior. lpviz is open-source, permissively licensed, and freely available on any device with a web browser at this https URL .

---


### 100. [Adjoint Inversion Reveals Holographic Superposition and Destructive Interference in CNN Classifiers](https://arxiv.org/abs/2604.27529)

**<font color=#1a73e8>作者：</font>** Kaixiang Shu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A foundational assumption in CNN interpretability -- that deep encoders suppress background pixels while classifiers merely select from a cleaned feature pool (the Spatial Funnel Hypothesis) -- remains untested due to spatial hallucinations in existing visualization tools. We address this by introducing a hallucination-free inversion framework built on magnitude-phase decoupling and Local Adjoint Correctors. Our method mathematically guarantees that the spatial gradient support of every reconstruction stems strictly from genuinely active channels.
Using this framework as a geometric probe, we uncover the first pixel-level evidence of strong superposition in vision encoders. We show that per-channel inversions are uniformly holographic: positive and negative weight reconstructions are visually and energetically indistinguishable. However, their algebraic sum sharply concentrates on the foreground. This proves classification operates via destructive interference -- classifier weights cancel a shared background direction in pixel space and constructively assemble class-discriminative residuals, directly falsifying the Spatial Funnel Hypothesis.
This interference model identifies the volume of the admissible interference subspace as the geometric quantity governing channel requirements. We prove this volume is dual to the GAP covariance determinant, yielding a covariance-volume channel selection algorithm with a $(1-1/e)$ approximation guarantee. This algorithm mathematically reveals out-of-distribution (OOD) failure as a measurable collapse of the covariance volume essential for interference-based classification. Our framework extends seamlessly to attention-based heads without retraining.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
