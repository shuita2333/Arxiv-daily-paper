# 📦 其他研究 | 2026年11月11日

> 本类共 **520** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

---

### 101. [A Topological Encoder Decoder Framework for Temporal Graph Learning](https://arxiv.org/abs/2611.10385)

**<font color=#1a73e8>作者：</font>** Ronan Buck, Kiarash Shamsi, Tran Gia Bao Ngo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most temporal graph learning methods reduce future prediction to discriminative inference over past interactions, focusing on edges or node labels for a largely persistent set of nodes. This view breaks down when new nodes and edges appear, since the future graph becomes a new object with changing size, composition, and structure. We address this gap by framing temporal graph prediction as an inverse topology problem. Instead of predicting edges directly, we first predict a multiscale topological descriptor of the future graph and then reconstruct a plausible future snapshot that realizes this descriptor under inductive constraints. This approach makes global structure and node churn explicit prediction targets and produces forecasted graphs that downstream tasks can evaluate without retraining. Across 14 temporal graph datasets, we evaluate our method, TOPOGED, on node, link, and graph property prediction and compare it against state-of-the-art temporal graph models. TOPOGED significantly improves node-level forecasting accuracy over the strongest baseline, with a macro average of 0.49 versus 0.05. It also outperforms baselines in 60% of graph-structure metric evaluations and substantially increases macro-average edge prediction metrics, from near-zero to 0.12. Our results show that topology-guided graph forecasting can predict inductive future snapshots whose structure supports multiple downstream evaluations.

---


### 102. [Tiresias: Towards Language-Conditioned World Models](https://arxiv.org/abs/2611.10392)

**<font color=#1a73e8>作者：</font>** Fengyi Wu, Yifei Dong, Yetong Sha 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models enable planning through internal simulation, while natural language provides intuitive task specification. Yet, language-conditioned world modeling remains fragmented across domains with disparate action spaces, datasets, and evaluation protocols. We introduce LCWM, a shared task that maps an initial agent-view observation and a language instruction to an action sequence that fulfills the instruction. Its accompanying benchmark, LCWM-Bench, integrates 15 datasets across navigation, robotics, 3D gaming, and driving under a shared action interface and evaluation protocol, pairing 142,987 episodes with 428,961 instructions in three styles. We further propose Tiresias, an agent that plans via selective imagination: a language-conditioned diffusion policy generates candidate trajectories, a trajectory ranker shortlists them, and a video-pretrained world model imagines their visual consequences. A visual ranker evaluates these rollouts, complementing trajectory scores to select the final plan. Tiresias achieves competitive planning and imagination performance on LCWM-Bench. Ablations demonstrate the complementary benefits of trajectory ranking and visual verification, while experiments with alternative proposal methods show that the trained rankers remain effective beyond our diffusion policy. Together, LCWM-Bench and Tiresias provide a unified evaluation setting and an effective starting point for studying language-guided planning through world models.

---


### 103. [Finite Time Analysis of Risk-Sensitive RL via Noisy Power Iteration](https://arxiv.org/abs/2611.10393)

**<font color=#1a73e8>作者：</font>** Waqar Mirza, Yashaswini Murthy, Laixi Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating the principal eigenpair of a positive operator from stochastic evaluations gives rise to a noisy form of normalized power iteration: each step applies a sampled operator estimate and then renormalizes. We establish finite-time stochastic-approximation guarantees for this procedure, working in Hilbert's projective metric, which is well-suited to the multiplicative geometry of Perron--Frobenius eigenproblems. Our main application is risk-sensitive average-cost reinforcement learning (RL) with exponential utility. In this setting the Bellman equations are multiplicative, and value functions are characterized by nonlinear eigenvalue problems rather than additive fixed points. We cast both policy evaluation and control in this framework, obtaining risk-sensitive TD- and Q-learning algorithms that learn from a single Markovian trajectory. Under explicit positivity, mixing, and linear function approximation assumptions, we prove finite-time bounds on the recovered eigenvector and eigenvalue with $\tilde{O}(\epsilon^{-2})$ sample complexity up to problem-dependent constants. The results cover both tabular and linear function approximation regimes, and through the duality between exponential utility and KL-robust control yield finite-time guarantees for KL-robust average-cost RL as well.

---


### 104. [The Limits of Information-Flow Control Enforcement for Agentic Systems](https://arxiv.org/abs/2611.10395)

**<font color=#1a73e8>作者：</font>** Jonathan Gregory, Kyle Domico, Kunyang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Information-flow control (IFC) is a promising approach to enforce policy in agentic AI systems. However, IFC suffers from label creep, a phenomenon where monotonically increasing security labels propagate through a system and progressively limit its utility. Label creep in agentic AI systems can be mitigated using two major strategies: (1) improved system design and (2) label declassification. In this paper, we characterize how far system design alone can mitigate label creep in agentic systems. Specifically, we measure how system topology, scale, and agent composition affect utility loss and security enforcement cost proxies for conservative IFC enforcement in a stateful agentic system simulator. We develop a pipeline to systematically vary these features and measure their impacts on label propagation. Our results demonstrate strong associations between structural graph features and our IFC utility loss metric (up to a Spearman correlation $|\rho|$ of $0.96$) and show that system size and tool allocation substantially affect how labels propagate. These findings identify design choices to reduce IFC utility loss, but they also demonstrate that system design alone cannot fully prevent utility loss due to monotonic label propagation. This motivates the development of label declassification mechanisms that aid these design choices and diminish IFC utility cost.

---


### 105. [Regularization Amplifies Subliminal Learning](https://arxiv.org/abs/2611.10397)

**<font color=#1a73e8>作者：</font>** Lawrence Feng, Jacob Mitchell Springer, Gaurav R. Ghosal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that hidden biases can be transferred through data with no apparent semantic relationship to those biases. Can regularization limit this covert influence? By constraining adaptation, regularization might be expected to suppress behavioral changes on seemingly unrelated inputs. We systematically study this hypothesis in subliminal learning, as well as in related settings of covert influence, including phantom transfer and logit-linear selection. We find the opposite: regularization amplifies the transfer of hidden biases. In particular, subliminal learning is typically absent under full fine-tuning, but low-rank adaptation or explicit penalties can induce strong transfer. Phantom transfer and logit-linear selection show similar trends. Adding more data, an implicit form of regularization, also strengthens covert influence. Together, these findings suggest that the simplicity biases induced by regularization may facilitate covert influence. We further hypothesize that the level of regularization that maximizes covert transfer depends on task complexity.

---


### 106. [Too Big to Inspect? Ethically Auditing Large Datasets Through Small Samples](https://arxiv.org/abs/2611.10399)

**<font color=#1a73e8>作者：</font>** Giovana Marchetti, Jhessica Silva, Tiago Torrent 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Big techs and researchers increasingly claim that their training datasets are too large to inspect for bias and ethical problems. However, in the race to build ever-large models, they have relied on automated web scraping and no human curation. Datasets built this way absorb the stereotypes, exclusionary norms, and historical prejudices of their sources, and the models trained on them can reproduce and amplify those patterns. Because manually auditing billions of samples is humanly impossible, we need practical, effective methods to identify biases in these datasets. This paper studies the feasibility of ethically auditing large datasets through small samples and proposes a practical method for identifying structural biases by applying AI Ethics Tools (AIETs) to random samples. We applied Datasheets for Datasets, Data Statements, Data Nutrition Labels, and Data Cards to a 1% sample of Framed Multi30K, and Datasheets for Datasets to two 0.00006% samples of relaion2B-en-research-safe. Our results show that evaluating small samples with AIETs can reveal ethical problems, structural biases, and technical inconsistencies. Although industry practice assumes that identifying problems requires analyzing the entire dataset, we show that a random subset supports a viable qualitative analysis without overwhelming computational or human resources. Demonstrating that a dataset is biased does not require examining every instance: if a bias appears in a random sample, it is a flaw of the creation process. The AIETs' questions acted as provocateurs, evoking different perspectives and analysis methods for the same dataset, but the analysis and its results depended fundamentally on the human factor. We hope these findings contribute to urgent public discussions about ethics, transparency, accountability, and AI regulation by offering a practical pathway for responsibly auditing massive datasets.

---


### 107. [QUASI: Post-Quantum Quorum Attestation of Pre-Validated Statements](https://arxiv.org/abs/2611.10403)

**<font color=#1a73e8>作者：</font>** Maksym Ioffe, Dahlia Malkhi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present QUASI, a newly conceived class of protocols that enable a group of parties to produce a publicly verifiable attestation about a pre-validated statement. Designed for quorum-based systems, QUASI enables parties to attest to external entities that the statement is valid. Surprisingly, each party need not sign the entire statement: authenticating only a small subset of symbols suffices for the quorum to attest to the whole. A simple deterministic construction illustrates this possibility. Built purely from hashing and error correction, QUASI achieves small per-party contributions and low attestation generation and verification costs, without relying on SNARKs for aggregation.
Our main contribution is a randomized construction achieving reductions of more than $10\times$ in per-party contribution size and hash computations for generation and verification, compared with full hash-based signatures.
QUASI is a generic primitive supporting diverse applications. Two principal use cases are external attestation for signature-free consensus, enabling clients to verify statements about committed state; and preprocessing for SNARK-based aggregation, compounding QUASI's savings with succinct-proof compression.

---


### 108. [Early Signals of Problematic AI Use: The Longitudinal Roles of Motivation and Emotional Engagement](https://arxiv.org/abs/2611.10406)

**<font color=#1a73e8>作者：</font>** Jina Suh, Constance Hadley, Koustuv Saha  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Longitudinal evidence about the psychological impact of conversational AI use remains scarce. We report a survey study of 114 adults who reported their level of problematic AI use one year after reporting their motivations (for escape, social, entertainment, and instrumental reasons) for engaging with AI. We found high levels of AI motivation of all types predicted later problematic AI use, especially when participants turned to AI for managing their feelings and overcoming difficulties. Our findings imply that AI motivation could be used as an early warning signal of potential problematic use, especially if individuals engage with AI for emotional purposes over time.

---


### 109. [Sharp Logarithmic-Product Bounds for List Replicability of Sign Matrices](https://arxiv.org/abs/2611.10408)

**<font color=#1a73e8>作者：</font>** Guangjian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> List replicability measures how many accurate hypotheses suffice to contain the output of a learning rule with arbitrarily high confidence. We prove that every nonempty class of $m$ binary concepts on $n$ domain points has list replicability at most $805\ln(2m)\ln(2n)$. This resolves the logarithmic-product conjecture of Blondal, Hatami, Hatami, Lalov, and Tretiak. Hanner matrices give lower bounds of the same order, for square matrices and for explicit families with unequal logarithmic aspect ratios. The upper bound is obtained by constructing nested acyclic sets in the faces of a cube. A critical-point estimate supplies highly connected regions, weighted cell attachments keep the sets compatible across faces, and a cubical carrier theorem converts them into accurate finite covers and learning rules. Appending one constant coordinate turns list replicability into an exact geometric quantity, the face width, and graph-orientation classes satisfy exact product formulas. In particular, there are explicit classes with list replicability $4k+1$ and equivariant index $3k$, so the additive gap between the two is unbounded. We also develop entropy-tilting and two-sided Gibbs constructions, give combinatorial upper bounds adapted to structured matrices, compute exact values on classical families, and study the index of Paley matrices.

---


### 110. [Frequency-Structure Complementary Modeling for Hyperspectral Image Fusion](https://arxiv.org/abs/2611.10413)

**<font color=#1a73e8>作者：</font>** Song Qiya, Tian Siyu, Li Shutao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing methods mainly rely on convolutional aggregation or attention-based spatial-spectral interaction. However, conventional feature-domain attention does not explicitly characterize variation patterns along spatial-token and learned latent-channel coordinates, while spatially shared local operators lack the flexibility to adapt neighborhood aggregation to heterogeneous structures. To address these limitations, we propose a Frequency-Structure Complementary Modeling Network (FSCM-Net), which couples frequency-aware dependency learning with structure-adaptive local refinement. Specifically, a Spatial-Spectral Frequency Calibration Attention (SSFCA) module constructs spatial-token affinities from Fourier-interacted query-key representations and builds latent-channel affinities after input-conditioned frequency filtering along learned channel coordinates. The latent-channel response is then calibrated by a learned shared gain and combined with the spatial-token response. Complementarily, a Structure-Coherent Dynamic Feature Fusion (SC-DFF) module combines regularized structure-tensor cues from MSI features with context-modulated HSI detail representations to generate channel- and position-dependent aggregation kernels. This design makes local HSI refinement responsive to smooth regions, edges, and textures while maintaining spectral fidelity. The two modules are progressively integrated within a multiscale encoder-decoder to coordinate representation-level interaction and structure-adaptive reconstruction. Experiments on two simulated benchmarks and one real remote-sensing dataset demonstrate favorable performance against representative fusion methods in spatial detail reconstruction and spectral preservation.

---


### 111. [S2HAND: Accuracy-Preservation Trade-Offs for Hand Specialization in Whole-Body Pose Models](https://arxiv.org/abs/2611.10416)

**<font color=#1a73e8>作者：</font>** Singyu Muk, Xuanren Song, Kalin Stefanov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified whole-body pose estimators jointly predict body, face, and hand landmarks, but often degrade on small, blurred, or occluded hands. Attaching a standalone hand specialist introduces extra detection overhead, coordinate alignment, and wrist-stitching artifacts. We introduce S2HAND, a hand-specialized Sapiens2-5B framework that preserves the native 308-keypoint output interface. Specifically, S2HAND-MT adapts a lightweight 0.87M-parameter pose branch to route 40 finger heatmaps while strictly preserving the shared Transformer, auxiliary task heads, and the other 268 body, foot, and face heatmaps. S2HAND-Pose further fine-tunes three Fisher-selected Transformer blocks (267.13M parameters), trading exact preservation for stronger hand recovery: it lifts macro AUC from 57.83% to 65.73% across HInt TEST, COCO WholeBody VAL, and FreiHAND EVAL, and surpasses HInt-adapted Hand5/HRNet and stitched Hand5 systems on all five Native Pipeline benchmarks. On COCO, S2HAND-Pose improves hand AP by 12.89 points and body-plus-foot AP by 0.19 points. Across a 512-image multi-task audit, it maintains 99.60% foreground segmentation agreement with the public checkpoint, with quantified normal and pointmap drift. Its 2D coordinates also lower 3D mesh error in frozen Pose2Mesh transfer, while our optional TailGuard re-cropping module cuts S2HAND-MT's severe failure rate on NewDays from 13.45% to 10.43%. S2HAND thus resolves the whole-body hand bottleneck with either exact non-hand preservation (MT) or empirically audited trade-offs (Pose).

---


### 112. [Applied bifidelity material response model construction and uncertainty quantification with a sampling hypernetwork](https://arxiv.org/abs/2611.10429)

**<font color=#1a73e8>作者：</font>** Reese E. Jones, Cosmin Safta, Dan Bolintineau 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multifidelity modeling offers a practical route to accurate prediction and uncertainty quantification when high-fidelity data are scarce but lower-fidelity data are comparatively abundant. This work develops a bifidelity Langevin sampling hypernetwork framework that constructs probabilistic neu- ral response models by learning a posterior distribution over model parameters rather than a single deterministic fit. The method combines a flexible shared-latent data representation for low- and high-fidelity responses, enabling parameter sharing and transfer learning between the fidelities. We introduce several methodological enhancements to improve the robustness and efficiency of this ap- proach, including stability-promoting drift models, staged and conditional training strategies, adap- tive initialization of Langevin trajectories, and training procedures designed to better exploit corre- lations between fidelity levels. These additions improve convergence behavior, reduce the sampling effort required to obtain representative posterior ensembles, and provide more reliable predictive uncertainty in data-limited regimes. The resulting framework makes more effective use of available multifidelity data while preserving interpretability through the learned posterior structure, yielding improved predictive performance, better uncertainty characterization, and a more stable workflow for constructing uncertainty-aware surrogate models. The method is demonstrated on experimental, high-fidelity simulation and illustrative synthetic data.

---


### 113. [Split and Bridge: Multimodal Generation via Diffusion Bridging](https://arxiv.org/abs/2611.10441)

**<font color=#1a73e8>作者：</font>** Ahmad Arrabi, Xiaohan Zhang, Xingyu Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual data are often expressed through multiple complementary modalities (e.g., images and segmentation masks), each capturing different aspects of the same underlying structure. Most existing multimodal methods adopt a top-down paradigm, learning a shared latent variable through joint training from scratch, which limits scalability. We propose Split and Bridge (SnB), a bottom-up framework for multimodal generation that couples pretrained unimodal diffusion models at sampling time. Rather than learning a unified latent space, SnB generates coherent multimodal samples by following a shared diffusion trajectory up to a split point and then branching into modality-specific trajectories guided by a bridge module. This design enables plug-and-play reuse of powerful pretrained models without joint training, making it scalable and easily adaptable. Across standard benchmarks (PolyMNIST, CelebAMask-HQ) and more complex settings (PIE-Bench++, ROCO), SnB achieves a strong balance between sample quality and coherence. We show that SnB naturally extends to downstream zero-shot tasks such as interleaved co-generation, image editing, and style coupling/decoupling. Our results demonstrate that bottom-up generation provides a practical framework that complements existing top-down multimodal approaches. Code is available at this https URL

---


### 114. [ESTRA: Enabling Extreme Attention Sparsity for Training-Free Video Diffusion Acceleration](https://arxiv.org/abs/2611.10448)

**<font color=#1a73e8>作者：</font>** Enhuai Liu, Yunke Wang, Yutong Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers generate high-quality videos, but attention over long spatiotemporal sequences makes inference computationally expensive. Sparse attention reduces this cost by computing only a subset of query-key interactions exactly, and recent training-free methods further approximate the remaining interactions. These methods, however, degrade quickly at high sparsity, which limits the achievable speedup. We present ESTRA (Extreme Sparsity Through Refined Attention), a training-free acceleration method that preserves generation quality even at extreme sparsity. ESTRA concentrates exact attention computation on a small set of important key-value tokens and approximates the remaining contributions with cluster representatives. To identify these tokens efficiently, it groups similar queries and uses their representatives to score individual keys. A variance-based correction further refines the attention weights of the cluster representatives, improving the accuracy of the approximation. Experiments on Wan2.1-14B and HunyuanVideo-13B show that ESTRA establishes a new quality-efficiency frontier for training-free sparse attention, achieving $3.26\times$ and $4.71\times$ end-to-end speedups at 5% attention density while surpassing Sol-Attn and SVG-EAR in fidelity to dense generation and on most VBench dimensions. Even at 1% density, ESTRA remains more faithful to dense generation than Sol-Attn at 12.5%, while reaching up to $5.39\times$ speedup.

---


### 115. [Decentralised Drone Swarm Formation under Silent Failures with ACO Pheromone Claims and PSO Tuning](https://arxiv.org/abs/2611.10454)

**<font color=#1a73e8>作者：</font>** Md. Abu Horaira  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study decentralised drone formation, without a central planner, under the conditions that make it hard: nobody knows how many drones are alive, failures are silent, radio is short-ranged and lossy, and actuation is noisy. In our controller, ant colony optimisation (ACO) allocates drones to picture positions through claims that behave as reinforced, evaporating pheromone and are gossiped between neighbours, so evaporation doubles as failure detection. A particle swarm optimisation (PSO) law flies the drones, a noise-buffered Voronoi filter keeps them apart, and PSO also tunes the controller offline. We prove that claims of destroyed drones vanish within bounded time, that conflicts between drones that exchange tables are resolved consistently, that survivors cover the picture to within a factor of two, and that drones cannot collide while their safety cells are feasible. On held-out seeds and with two tuned configurations, the controller formed the picture in 95-99% of runs in the hardest regime, restored it after a silent loss of half the swarm in 96-100% of runs at normal difficulty, transferred unchanged to eight unseen shapes and to 300 drones, and overlapped in 5 of 21,088 runs. A CBBA-style baseline that shares the evaporating claims but uses argmax without swaps was at least as reliable as ours once tuned with the same budget, and repaired faster, whereas ours generalised better to unseen shapes. The benefit thus comes from the pheromone dynamics and from tuning, not from ACO's stochastic construction or PSO's social terms. A centralised oracle is faster.

---


### 116. [The Fast Tree Transform](https://arxiv.org/abs/2611.10466)

**<font color=#1a73e8>作者：</font>** Paul Burchard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Fast Tree Transform is a locally-aggregated transform defined for arbitrary graph geometries that generalizes both the Hadamard frequency transform and the Haar wavelet transform on the circle. The pure frequency part of the transform approximately diagonalizes the graph Laplacian; this fact makes it useful as a preconditioner in geometric optimization problems. The full transform provides an only slightly-redundant representation of signals on the graph that allows sparse representation of signals that include both edges and textures.

---


### 117. [Dynamic State Estimation from Sparse PMUs via Physics-Informed Graph Neural Operators](https://arxiv.org/abs/2611.10468)

**<font color=#1a73e8>作者：</font>** Huy Hoang Le, Haoguang Wang, Christian Moya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a physics-informed graph neural operator for power system dynamic state estimation. From a sparse, intermittent measurement window at a few generator buses, the operator estimates the rotor-angle and speed trajectories of all machines, unmeasured ones included, in one forward pass. A graph-attention encoder processes the measurements, and the swing equations are imposed as a hard constraint or as a soft one with a learned correction that absorbs model errors. It is trained on simulated measurements, without state labels. With several phasor measurement units, masked training hides one from the input but keeps it in the loss. On four transmission systems, simulations show that the operator is the most accurate estimator that neither optimizes per scenario nor uses state labels, except on the smallest system at large model errors, where tuned Kalman smoothers are better. Networks trained on simulated states are more accurate on the two smallest systems but not on the 118-bus system, where the operator is faster and more accurate than hard-constrained moving-horizon estimation. Under model errors, it matches or outperforms an optimization-based benchmark at a fraction of its cost. The results hold for a detailed machine model with exact parameters seen only through voltage phasors.

---


### 118. [WordEval: Evaluating Word-Native Operation Fidelity in Document Editing](https://arxiv.org/abs/2611.10475)

**<font color=#1a73e8>作者：</font>** Jinyoung Park, Yupan Huang, Shimin Zhang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Microsoft Word is a central environment for office automation, and the faithful execution of its editing operations is an important capability for document agents. Unlike plain-text editing, editing in Word modifies a structured object model, where the requested effect is realized in object properties. Existing benchmarks, however, evaluate office workflows or desktop automation, treating word-processor documents as one task domain among many and verifying outcomes with keyword matching, per-task property checks, or screenshot comparison. We introduce WordEval, an operation-fidelity benchmark that instead centers evaluation on Word editing operations, testing whether each requested edit is realized as intended changes to Word objects and properties. It contains 642 cases across 15 Word feature areas, ranging from text and lists to charts, shape geometry, and SmartArt. 546 atomic cases cover 231 commands, 96 compositional cases combine multiple edits in a single document, and a Word-native oracle checks task-specific object properties and preservation conditions. Cases are constructed from editing-unit specifications, yielding controlled input documents, reference documents, and aligned oracle checks. Each compositional case is linked to corresponding atomic cases, supporting fine-grained diagnosis of editing failures. We evaluate eight agent systems and find that many struggle on the Atomic track, with performance varying across feature areas. Moreover, every system scores lower on Compositional than on Atomic, with gaps that vary substantially by system. Exact atomic-intent links and recorded failure diagnoses provide complementary views of this variation.

---


### 119. [Decoupling Direction and Magnitude: Language-Steered Flow Matching for Super-Resolution in the Dark](https://arxiv.org/abs/2611.10485)

**<font color=#1a73e8>作者：</font>** Jiaxin Gao, Ziyu Yue, Yaohua Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image super-resolution in the dark is fundamentally challenged by extreme spatial heterogeneity: severely underexposed and noisy regions demand aggressive generative enhancement to reconstruct missing details, while relatively well-exposed areas require conservative updates to prevent hallucinated textures. Standard diffusion and flow-matching models, however, rely on globally uniform integration trajectories, making them sub-optimal for such spatially varying degradations. In this paper, we propose DeLang-SR (Degradation-Language steered Super-Resolution), a one-step flow-matching framework that explicitly decouples the restoration direction and magnitude. Rather than treating low-light corruption as arbitrary latent features, DeLang-SR translates measurable physical statistics into structured degradation language, harnessing the semantic prior of pretrained text-to-image models. The degradation-language intent, complemented by image-specific visual tokens, steers the velocity field (direction) toward restoration-relevant manifolds. Simultaneously, a continuous spatial update-strength field acts as a locally varying Euler step-size field (magnitude), applying stronger integration steps in heavily degraded shadows while enforcing conservative updates in reliable regions. Experiments on paired and real dark images, together with ablations and diagnostic analyses, show that DeLang-SR provides an effective and interpretable one-step route to super-resolution in the dark. Code and pretrained models are available at this https URL.

---


### 120. [Disentangling Channel Semantics in Vision Transformers via Token Decorrelation and Composition-Aware Modulation](https://arxiv.org/abs/2611.10497)

**<font color=#1a73e8>作者：</font>** Daeun Kim, Hyesong Choi, Hyejin Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-channel images encode heterogeneous channel semantics aligned over a shared spatial structure, which requires models to jointly capture globally shared structure and channel-specific variations. Recent multi-channel Vision Transformers attempt to address this challenge by augmenting the [CLS] token with memory tokens to organize multi-channel representations under varying channel compositions. However, we find that these context tokens collapse onto a few dominant channels under high inter-channel redundancy, producing redundant representations and a biased global summary that fails to reliably support composition-aware channel interpretation. We propose MuCa-ViT (Multi-Channel Composition-Aware Vision Transformer), a unified framework that addresses these limitations through two coupled mechanisms. Factorial Token Learning (FTL) enforces token-level decorrelation among context tokens, encouraging the [CLS] token to capture globally shared semantics while memory tokens preserve complementary channel-specific cues. Channel Composition-Aware Modulation (CAM) uses the FTL-refined [CLS] as a semantic anchor to generate sample-wise modulation signals, which enable composition-aware interpretation of channels within a unified backbone rather than relying on static channel embeddings. Experiments on JUMP-CP, CHAMMI, and So2Sat show that MuCa-ViT outperforms prior multi-channel ViTs across all three benchmarks, and the magnitude of improvement aligns with the inter-channel redundancy of each dataset ($\rho \in [0.19, 0.77]$), validating the diagnostic analysis that motivates our design. Our code is available at this https URL .

---


### 121. [Learning a Unified Cross-Model Semantic Dictionary via Gated Bottleneck Sparse Autoencoders](https://arxiv.org/abs/2611.10503)

**<font color=#1a73e8>作者：</font>** Jinchi Zhu, Tie Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models pretrained on similar data distributions tend to learn overlapping semantic structure, but their representations are distinct due to different model architecture, pretraining objectives and protocols. This prevents unified interpretability and cross-model feature reuse. Existing approaches extract interpretable concepts from individual models and align these concepts in a shared coordinate system using cross-reconstruction objectives, but the alignment only applies to latent coordinates while the concepts themselves remain model-specific and cannot be shared or reused. This paper introduces the Gated Bottleneck Sparse Autoencoder (GB-SAE), which casts unified cross-model interpretability as a representation factorization problem and solves it by simultaneously learning a unified shared dictionary and multiple private model-specific dictionaries via a gated bottleneck sparse autoencoder framework. The shared dictionary encodes the cross-model common semantic structure in unified concepts that are reusable across all participating models (and beyond), while each private dictionary comprises residual concepts that capture model-specific biases. We evaluate GB-SAE with distinct foundation models including ViT, SigLIP, DINOv2, and ConvNeXt. GB-SAE demonstrates superior reconstruction capability, unified and faithful interpretability, strong reusability and generalization to unseen models and downstream tasks. The code is available at this https URL.

---


### 122. [SRA: Spatial Reasoning Adapter via Evolving Social Interaction Graphs for Trajectory Prediction](https://arxiv.org/abs/2611.10506)

**<font color=#1a73e8>作者：</font>** Jaewoo Jeong, Seonkyu Song, Hyeonwoo Park 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting where multiple agents will move next is fundamental to autonomous driving, robotics, and any system that must share space with people safely. Modern stochastic predictors read off inter-agent interactions once from the observed past and keep that view fixed throughout the generative rollout, so the reciprocal geometric constraints that emerge as the joint future sharpens are not re-examined. We address this gap with SRA (Spatial Reasoning Adapter), a modular graph denoiser that is integrated into existing diffusion and flow-matching predictors without redesigning their generative cores. At every reverse step, SRA reads the host's current future estimate, builds a sparse Euclidean interaction graph on the predicted trajectories, and returns a residual correction to the host's decoding path. Our adapter consists of three core components: a sparse neighborhood retrieved with a learned query-key score and a geometric bias, a future-conditioned relational feature recomputed on the evolving prediction, and uncertainty-weighted message passing where confident agents act as anchors for uncertain ones. We instantiate SRA on three structurally different hosts (LED, MID, and MoFlow) across four multi-agent benchmarks: SDD, NBA, Soccer, and Football. SRA improves ADE for every host on every dataset, with average gains of 5.8% in ADE and 7.0% in FDE. A cumulative ablation shows that the three components act as one mechanism: only together do they improve every host on every sports dataset, indicating that spatial reasoning over the model's own evolving future, weighted by how far that future can be trusted, is broadly useful across denoising architectures. Code is available at this https URL.

---


### 123. [Scaling Optimization-Oriented Hypernetworks for Implicit Neural Representations](https://arxiv.org/abs/2611.10509)

**<font color=#1a73e8>作者：</font>** Lulu Cai, Hanxiang Ren, Siyan Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a hypernetwork that generates the parameters of an implicit neural representation (INR) for a given signal in a single forward pass, without test-time optimization. Existing hypernetworks for this problem either ignore the chain-rule structure of the test-time optimization that produces an INR or, when they preserve it, instantiate the structure with MLPs whose parameter count grows quartically in target-network width. Our central contribution is to show that this parameter-count cost is structural to the MLP instantiation, not to the optimization-oriented principle of preserving chain-rule structure, and to resolve it by replacing the MLP body with attention. The resulting hypernetwork combines three design choices: an output-neuron-centric tokenization that aligns the token axis with each layer's output-neuron axis; an information-flow consistency rule that fixes the role of every cross-attention module from the representation its output should occupy; and a token-space iterative rollout that realizes the five quantities one optimization step on the target INR computes as five cross-attention modules with parameter count independent of target-network width. Across five 2D and 3D INR generation benchmarks, our method outperforms the state-of-the-art single-pass and optimization-oriented baselines; scales to target-network widths at which the MLP-based optimization-oriented paradigm exhausts GPU memory; and produces the highest result on NeRF generation without ground-truth INR weights supervision.

---


### 124. [FADE: Fractional Anomalous Dynamics Extrapolation for Training-Free Diffusion Transformers Acceleration](https://arxiv.org/abs/2611.10514)

**<font color=#1a73e8>作者：</font>** Jinlong Yang, Lizilin, Jinke Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have established themselves as the preeminent paradigm for high-fidelity generative modeling across various modalities, yet their practical deployment is hindered by the severe computational overhead of iterative sampling. While recent feature-caching methods mitigate this latency through feature reuse or forecasting based on integer-order operators, they remain limited in adapting to the non-stationary and highly curved dynamics of DiT latent trajectories. In this work, we reveal that DiT feature evolution exhibits anomalous diffusion characteristics and a certain degree of spatiotemporal heterogeneity, rendering static, integer-order forecasting operators inadequate and prone to error accumulation. To address this, we propose Fractional Anomalous Dynamics Extrapolation (FADE), a unified framework for training-free diffusion transformers acceleration. FADE models DiT feature evolution via anomalous diffusion and employs a Mittag--Leffler fractional operator to better adapt to high-curvature and non-linear latent trajectories of DiTs. Leveraging the empirical observation that these complex dynamics maintain cross-sample stability, we further construct a Look-Up Table with multiple dimensions through offline profiling. This enables negligible LUT-retrieval overhead, spatiotemporally adaptive parameter retrieval during online inference. Extensive evaluations across diverse architectures and modalities demonstrate that FADE achieves state-of-the-art acceleration, preserving exceptional generation fidelity under aggressive skip intervals with negligible latency overhead. Our project page is available at this https URL.

---


### 125. [Beyond Row Alignment: Virtual-Camera-Aware Online Stereo Rectification](https://arxiv.org/abs/2611.10518)

**<font color=#1a73e8>作者：</font>** Yizhao Peng, Rui Gong, Zaiwang Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereo matchers estimate depth by comparing the left and right images from a stereo camera pair, but they assume that the two cameras are accurately calibrated and rectified. In real deployments, small physical shifts after calibration, caused by camera motion, mechanical drift, vibration, or installation changes, can break this assumption and degrade depth estimation. Online stereo rectification is therefore needed to correct the image pair during operation and recover a stereo geometry where standard stereo matching can work reliably. Recent online rectification methods mainly optimize row alignment, making the left and right views of the same scene point fall on the same image row. We show that this target, while necessary, is insufficient for deployable stereo depth estimation. A rectifier may make a small set of matched points look well row-aligned, but still distort the full images in ways that hurt stereo matching: useful image regions may be cut off, large blank areas may appear, objects may be stretched or squeezed, or image scale may change unevenly across the view. We propose VirtualRect, an online stereo rectification method designed for reliable real-world deployment. Rather than treating rectification as simply making the left and right image rows line up, this method estimates a rectified virtual stereo camera and combines image-wide supervision of image warp behavior. This makes the rectified images and the camera parameters come from the same geometry, so the images used for matching and the model used for depth computation remain consistent. Experiments on multiple datasets show that, compared with the prior state-of-the-art online rectifier, VirtualRect reduces vertical flow error by 17% on Carla-Flowguided and 7% on Semi-Truck Highway, and lowers depth MAE by 30-41% on Carla-Flowguided across three downstream stereo matchers.

---


### 126. [Action Transfer Across Character Body Plans in Latent-Action World Models: An Empirical Study of Animated Characters](https://arxiv.org/abs/2611.10523)

**<font color=#1a73e8>作者：</font>** Amarnath R  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent-action world models learn actions from video without labels, and recent methods aim to share these actions across bodies. Transfer between 2D characters with different body structures remains underexplored. In this paper, we study whether an action learned from one character can make a character with a different body perform the same action. A cat, a blob and a human can all jump, but each moves its body in its own way. The usual transfer gain mixes body motion with screen movement and can assign a perfect score to a model that ignores its action. To address this, we introduce a transfer score that compares the correct action with wrong ones from the same source. We test five training objectives on a new synthetic benchmark of 2D cartoon characters with six body plans, the standard Sprites benchmark, and 431 selected animal and human animations from DeformingThings4D. With a fixed camera, a baseline that only copies the source's screen movement scores 0.71, as high as most learned models. In contrast, with a camera that follows the body, the best model reaches only 0.46 for an unseen animal family and 0.20 for humans. With this camera, a linear probe identifies the action class of unseen animal families with 66% to 86% balanced accuracy (chance 17%). The learned actions therefore retain information about which action is performed, but the correct action closes only part of the prediction error gap for a new character.

---


### 127. [Intra-Option Fitted Q-Evaluation: Evaluating Hierarchical Policies from Non-Hierarchical Data](https://arxiv.org/abs/2611.10543)

**<font color=#1a73e8>作者：</font>** Yunfu Deng, Josiah P. Hanna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy evaluation (OPE) estimates the expected return of a target policy from previously collected data without additional environment interaction. While OPE methods for flat Markovian policies are well studied, little work has addressed evaluating hierarchical policies in which a high-level policy selects temporally extended options that generate primitive actions until a termination condition is met. The primary existing approach applies per-decision importance sampling at the option level, but requires option-annotated trajectories and exhibits variance that still grows with the horizon. For non-hierarchical policies, fitted Q-evaluation (FQE) typically achieves lower error than importance sampling by leveraging the classic Bellman equation for policy evaluation; however, a naive extension of FQE to hierarchical policies results in a biased policy value estimate. In this paper, we introduce Intra-Option Fitted Q-Evaluation (IO-FQE), which estimates a value function in the augmented state-option space; this approach enables OPE of hierarchical policies even when we lack annotations of what option was run in the data. We develop two continuous-action instantiations of IO-FQE and show on long-horizon hierarchical continuous control tasks (AntMaze navigation and OGBench Puzzle manipulation) that IO-FQE eliminates the bias incurred by a naive application of FQE to hierarchical policies and substantially lowers mean squared-error compared to option-level importance sampling.

---


### 128. [Dual-Granularity Learning for Regression with Continuous Noisy Labels](https://arxiv.org/abs/2611.10550)

**<font color=#1a73e8>作者：</font>** Hui Guo, Boyu Wang, Grace Y. Yi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning with noisy labels has been extensively studied for classification, yet its regression counterpart remains relatively underexplored. Unlike classification, regression involves continuous-valued targets where label noise exhibits heterogeneous magnitudes across instances, which poses conflicting requirements on the model: correcting small-to-moderate deviations requires sensitivity to label values for instance-level refinement, whereas large deviations caused by corrupted or outlying annotations render exact label values unreliable, necessitating reduced reliance on exact labels and instead leveraging ordinal structure among samples. These requirements call for methods that capture both global structure and sample-specific deviations in a unified manner. To this end, we propose GRAIN, a dual-granularity framework for robust noisy regression. At the fine-grained level, we derive an explicit residual learning mechanism from a robust loss formulation, introducing instance-specific auxiliary variables to decouple label noise from predictive signals. At the coarse-grained level, we introduce a binning-based contrastive regularization that enforces an order-preserving feature structure aligned with label proximity, addressing noise beyond the capacity of local residual refinement. The two levels are coupled via a histogram-based bridging mechanism that enables bidirectional information flow: coarse-grained structural guidance establishes a well-ordered feature space that anchors residual learning, while fine-grained residual refinement corrects instance-level deviations that structural regularization alone cannot resolve. Experimental results show that GRAIN consistently improves robustness and generalization under diverse noise conditions.

---


### 129. [Meta-Reinforcement Learning with Zero-Shot Reinforcement Learning](https://arxiv.org/abs/2611.10553)

**<font color=#1a73e8>作者：</font>** Jake Grigsby, Siddhant Agarwal, Yu Lei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Meta-reinforcement learning (meta-RL) trains agents to adapt to novel tasks from test-time experience, but requires diverse training environments and reward functions. While environments are becoming cheaper to generate, it remains difficult to anticipate every objective an agent may be asked to pursue at test time. Behavior Foundation Models (BFMs) learn policies from reward-free data and support zero-shot RL (ZSRL): adaptation to new objectives at test time using a large reward-labeled dataset. Recent work has shown that BFM task inference can instead be performed online without prior task-specific data. We note that this capability positions BFMs and meta-RL as alternative approaches for online adaptation to new reward functions in a fixed environment. We then ask whether we can extend BFMs to compete with meta-RL more broadly, including in novel environments, and identify four challenges: environment identification, online data collection, test-time exploration, and learning from mixed reward supervision. We study each individually, then propose MetaBFM, a hybrid method that addresses all four. During training, it combines supervised reward-following with unsupervised learning; at test time, it can interpolate between exploration, exploitation, and ZSRL-style reward inference. We demonstrate that MetaBFM can recover the in-distribution performance of supervised meta-RL while generalizing to reward functions outside the training set. Our work suggests that BFMs and meta-RL are complementary research directions whose combined strengths allow adaptive agents to learn more diverse behaviors from a fixed set of supervised objectives.

---


### 130. [ZARA: Zero-shot Animatable and Relightable 3D Avatar reconstruction from a single image](https://arxiv.org/abs/2611.10562)

**<font color=#1a73e8>作者：</font>** Yixiao Chen, Dongdong Weng, Chengfeng Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent large human reconstruction models create remarkable animatable 3D avatars from a single image, but their appearance remains entangled with the illumination and cannot be relighted. In contrast, existing 3D relightable-avatar reconstruction methods typically require person-specific optimization. We present ZARA, a zero-shot feed-forward framework that reconstructs an animatable 3D Gaussian avatar together with its intrinsic attributes from a single image. ZARA couples a pretrained large-scale human reconstruction model with a Material Transformer to inherit geometry priors while learning material-aware Gaussian representations. To preserve localized details, we introduce Gaussian-aligned material feature fusion strategy, which injects multi-scale material features onto individual Gaussians and combines them with geometry tokens. As most human-avatar datasets lack ground-truth material maps, we use pseudo-material labels as conditioning inputs and supervision targets during training. We further introduce MatFace regularization to preserve facial structure and color in albedo prediction under unreliable facial pseudo-material supervision. Extensive experiments demonstrate that ZARA reconstructs animatable and relightable humans within tens of seconds without person-specific optimization or post-processing, outperforming existing baselines in both relighting quality and materials generalization ability. As the ability of recovering the physically-based-rendering attributes of the human, ZARA also enables direct material editing of the avatar's appearance.

---


### 131. [Confronting Uncertainty in Mechanism-AI Coupled Dynamical Systems via Optimal Transport and Information Geometry: Part I. Distribution Learning](https://arxiv.org/abs/2611.10563)

**<font color=#1a73e8>作者：</font>** Pengfei Song, Yanni Xiao, Shuangshuang Yin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanism-AI coupled dynamical systems are increasingly used to study complex biological systems. However, uncertainty associated with noisy, sparse, and partially observed data limits their reliability. This paper presents a systematic mathematical formulation for treating these uncertainties from the perspective of optimal transport and information geometry. We formulate the uncertainty quantification problem as the minimization of an energy functional on a probability density space equipped with a Riemannian metric, with the loss evaluated through a differential equation, and give a unified description of the gradient flows of the energy functional under specific metrics, such as the Wasserstein and Fisher-Rao metrics. Furthermore, we present corresponding numerical methods for solving these gradient flows using abstract adjoint sensitivity analysis. The formulation connects a range of Bayesian inference methods for dynamical systems; numerical experiments compare posterior approximation and predictive uncertainty under a common computational budget. Moreover, it also provides a geometric perspective on dynamical modeling and the study of heterogeneity evolution.

---


### 132. [Understanding the Effect of Visual Attention in CNNs: A Decision-Space Alignment Perspective](https://arxiv.org/abs/2611.10571)

**<font color=#1a73e8>作者：</font>** Niladri B. Puhan, K. Kamala Priya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Attention enhances convolutional neural networks (CNNs) by modulating intermediate features, yet their effects on downstream decisions remain less understood. We present a decision-space framework that models multiplicative attention as an intermediate feature perturbation and derives a first-order prediction of its effect on the target-versus-competitor classification margin. We further introduce the Decision Alignment Score (DAS) to quantify the directional alignment between the perturbation and the local margin gradient. We evaluate the framework on CIFAR-100 using SimAM and CBAM across five popular CNN backbones, ResNet-18, ResNet-20, ResNet-50, ResNet-56, and MobileNetV2. The analysis examines prediction agreement, DAS margin correlations, and downstream activation-state changes. Across most final-attention configurations, predicted and actual margin changes show good agreement, while DAS exhibits positive correlations with actual margin changes. Single-attention experiments further show that prediction agreement and DAS margin correlations depend on attention placement, with stronger associations at later stages.

---


### 133. [Predictive Modelling of Solid Waste Generation through Time Series Analysis](https://arxiv.org/abs/2611.10579)

**<font color=#1a73e8>作者：</font>** Mitra Tithi Dey, Punyasha Chatterjee, Amlan Chakrabarti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable forecasting of Municipal Solid Waste (MSW) production is pivotal for sustainable urban management, as it enables efficient resource planning, optimized collection schedules, and reduced environmental impacts. Existing works on MSW forecasting have some limitations, such as unavailability of granular data from lower administrative units, small datasets, limited or sometimes no consideration of important factors that can affect MSW generation, including holidays, weekends, seasonality, changes in temperature or humidity.
This work presents a comprehensive comparative analysis of four popularly used time series forecasting models, namely Seasonal Autoregressive Integrated Moving Average with Exogenous Regressors (SARIMAX), Prophet, Long Short Term Memory (LSTM) and Gated Recurrent Unit (GRU), using a real-world MSW dataset from Sri Lanka spanning 2012-2018. A detailed factor-wise analysis is conducted to examine waste generation behaviour considering holidays, weekday-weekend variations, seasonal patterns, temperature and humidity. The results show lower waste generation during holidays and weekends, higher generation during Summer and Winter, and comparatively lower generation during Monsoon and Post-Monsoon. Temperature and humidity do not exhibit a direct linear relationship with waste generation, although their seasonal variations are associated with the changes in waste generation across different seasons. All model performances are evaluated using Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), Root Mean Squared Error (RMSE), and the coefficient of determination (R2). Among the evaluated models, LSTM and SARIMAX achieve the best overall forecasting performance.

---


### 134. [Receiver-Resolution APS-PDP Maps for Wireless Channels: Benchmarking and Coarse-to-Fine Modeling](https://arxiv.org/abs/2611.10581)

**<font color=#1a73e8>作者：</font>** Peilin Zheng, Haozhe Jia, Xiucheng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Angle Power Spectrum (APS) and Power Delay Profile (PDP) are receiver-facing spectra that govern beam selection and wideband equalization. Most ray-tracing benchmarks provide supervision as variable-size multipath component lists. This format does not match practical receivers, whose angular and delay resolutions are limited by array aperture and system bandwidth. As a result, learning targets are ambiguous and evaluations can change with reconstruction conventions. We introduce UrbanADPSMap, a benchmark that converts ray-traced supervision into fixed-grid APS and PDP targets by explicitly modeling bandwidth-limited and aperture-limited response kernels. By fixing the receiver-domain kernels, discretization, and validity mask, UrbanADPSMap removes reconstruction-induced target ambiguity and stabilizes downstream evaluation across methods. Built on this benchmark, we propose SpecFlowAR, a coarse-to-fine generator based on multi-scale autoregressive flow matching. The model first captures coarse dispersion structure and then refines beam-relevant peaks and low-power tails. The number of function evaluations controls the sampling budget, enabling latency and quality to be adjusted for dense spectrum queries. Experiments on the test set show that SpecFlowAR reduces BPL@5 to 2.03 dB under a unified NFE=80 budget, while improving beam utility and reducing errors of 3GPP dispersion statistics.

---


### 135. [Design and Evaluation of Secure Distributed Chaotic Image Encryption on ESP32-S3](https://arxiv.org/abs/2611.10595)

**<font color=#1a73e8>作者：</font>** Mohammed Almozaini, Fazal Noor, Sohail Alhazimi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The limited computational resources of Internet of Things (IoT) devices present challenges for secure image processing. This paper presents a distributed chaotic image encryption system using independent Wi-Fi-connected ESP32-S3 microcontrollers. A master-worker architecture distributes image blocks through master-coordinated chaotic sequence management, maintaining one logically continuous chaotic sequence by assigning block-specific starting states independently of worker assignments. The implemented system uses reversible chaotic substitution (SUBSTITUTE), while Elliptic Curve Digital Signature Algorithm (ECDSA)-signed discovery messages and Transport Layer Security (TLS) 1.3 with mutual authentication secure device communication. Experimental evaluation using one, two, and four workers demonstrates a reduction in execution time from 43.215 to 15.878 seconds, achieving a speed-up of 2.72 times. The encrypted image achieves a Shannon entropy of 7.999940 bits/byte and near-zero adjacent-pixel correlation. Exact image recovery is verified through matching Secure Hash Algorithm 256-bit (SHA-256) hashes and a Structural Similarity Index (SSIM) value of 1.0. Additional experiments demonstrate successful encryption and decryption using different worker counts and block sizes, automatic task reassignment following worker failure, and rejection of a mismatched private key during TLS authentication. These findings demonstrate the feasibility of secure, flexible, and distributed chaotic image processing across independent resource-constrained IoT devices.

---


### 136. [Agentic discrete-event simulation for manufacturing system design: an open 3D simulator, a benchmark and an industrial case](https://arxiv.org/abs/2611.10602)

**<font color=#1a73e8>作者：</font>** Javier Pernas-Álvarez, Diego Crespo-Pereira  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The design of manufacturing systems relies on discrete-event simulation (DES) models that experts still build in tool-specific interfaces. AI agents can now write simulation code, but every model they write from scratch is new, unverified software. We present SimuLean, an open-source 3D DES simulator on the Unity engine designed to be programmed by AI agents: its modelling semantics are verified once, in the platform, and the agent builds and studies one model through domain-level commands, in the 3D scene or headless; physically simulated durations are calibrated for fast headless studies. We evaluated it on 18 manufacturing modelling tasks, from single machines to published production lines. A frontier agent built valid models in 93 of 108 attempts (86%), in about two minutes each; on the benchmark's interface version, two frontier agents built 105 of 108 models through domain commands alone, so that each comes with a record of how it was built. Every residual failure was silent - a model that builds and runs but answers wrongly - and only comparison with reference models revealed them all. In an industrial case, one agent working alone rebuilt, verified and studied a robotised welding workshop from a published study, in SimuLean and in SimPy. Comparing them with the published, expert-built model exposed an error in it; against the corrected model, the agent-built models agree within 1%. One agent can already build complete, realistic and traceable models for the design of manufacturing systems; independent reference models are what make them trustworthy.

---


### 137. [Clinical Evidence-Guided Residual Learning for Medication Recommendation with Dynamic DDI Regularization](https://arxiv.org/abs/2611.10613)

**<font color=#1a73e8>作者：</font>** Zesheng Li, Chengchang Pan, Honggang Qi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medication recommendation must combine patient-specific treatment evidence with the interaction structure of a prescription. The central challenge is to determine which evidence supports each medication and how strongly to regularize interactions while preserving predictive quality. We propose EviDrug, a clinical evidence-guided residual learning framework. Its clinical-memory backbone integrates a self-trained visit-aware encoder, training-case memory and one medication-set interaction block to establish a patient-specific prescription. A gated refinement head combines the backbone states with clinical associations and history-conditioned medication identities through bounded logit corrections. Drug-drug interaction (DDI) feedback adapts regularization strength using training-query predictions. Across MIMIC-IV, NWICU and SICdb, EviDrug leads twelve published-method baselines in AP, F1 and Jaccard, improving AP by 2.26, 2.06 and 1.71 percentage points over the strongest comparator. These gains come at lower parameter and runtime costs than MetaDrug. Matched controls demonstrate DDI reductions with stable predictive quality. Code is available at this https URL.

---


### 138. [CAROUSEL: GPU-Accelerated Private Vector Search via Homomorphic Sketching](https://arxiv.org/abs/2611.10622)

**<font color=#1a73e8>作者：</font>** Sohaib, Divyakant Agrawal, Amr El Abbadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vector search on untrusted infrastructure exposes the \emph{query embedding}, a faithful summary of the user's intent. Fully homomorphic encryption can hide the query, but existing approaches still require a full scan followed by ranking of encrypted scores. Scalable private systems avoid encrypted ranking by either sending scores from a single cluster to the client or moving the search to the client, which must first stream the entire vector index for preprocessing. We present \textsc{Carousel}, which instead scores the full corpus under encryption and compresses the results for client-side ranking. The server scores every vector under encryption, raises the scores to a power that preserves their order by magnitude while suppressing all but a handful, and compresses the resulting sparse vector into a logarithmic number of ciphertexts using homomorphic additions alone. Because every vector is scored, \textsc{Carousel} incurs no recall loss from discarding candidates. Since clients hold no database-dependent state, insertions and deletions take effect immediately at the cost of a single vector write. \textsc{Carousel} searches $1$ billion vectors of BIGANN SIFT1B across multiple GPUs and achieves recall@100 of $0.9715$. At $100$ million SIFT vectors, it achieves recall@100 of $0.9845$ with a query latency of $3.735$ seconds on a single GPU.

---


### 139. [CONSTRAINER: Promptable Graph-Structured Optimization via Constraint Conditioning](https://arxiv.org/abs/2611.10627)

**<font color=#1a73e8>作者：</font>** Zeeshan Memon, Mingke Tian, Xinyuan Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural methods for graph-structured optimization have achieved strong performance within individual problem classes, but are typically trained for fixed formulations, limiting reuse across related problem variants. Recent progress in foundation models has motivated shared neural backbones trained across multiple graph-structured optimization tasks; however, existing approaches primarily share instance-level representations while treating feasibility constraints implicitly. A key source of shared structure across constrained optimization problems is the constraint set itself, which often exhibits substantial overlap across tasks. We propose CONSTRAINER, a constraint-conditioned framework for graph-structured optimization that treats constraints as structured inputs. Constraint specifications are parsed into operator graphs and encoded using a graph neural network to produce invariant constraint embeddings, which condition a shared backbone model for solution prediction. We evaluate our approach on power grid optimization and mixed-integer linear programming problems, where it shows improved solution optimality and enables efficient transfer learning and generalization compared to baseline methods.

---


### 140. [Latent-WAM++: Shaping World and Action Representations for End-to-End Autonomous Driving](https://arxiv.org/abs/2611.10632)

**<font color=#1a73e8>作者：</font>** Yichen Zhang, Yupeng Zheng, Linbo Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Latent-WAM++, a representation-centered World Action Model (WAM) for end-to-end autonomous driving. Existing WAMs are primarily trained to predict future states or final actions, leaving the intermediate world and action representations that connect prediction to planning only indirectly constrained. Latent-WAM++ matches the supervision of each representation to its role in planning. World Representation Construction combines scene-ego future prediction, SIGReg-based distribution stabilization, and frozen geometric priors to learn a temporally predictive, non-degenerate, and geometry-aware world representation without an EMA target encoder. Trajectory MeanFlow Planner directly predicts multimodal trajectory proposals while being optimized with an Improved MeanFlow velocity-space objective, enabling one-step sampling. Visual-Action Representation Alignment further aligns the resulting pre-output action features with a stop-gradient target derived from current visual semantics. Latent-WAM++ achieves state-of-the-art performance on NAVSIM v2 and under zero-shot evaluation on HUGSIM, reaching 90.1 EPDMS on NAVSIM v2 and 47.0 average RC and 30.1 average HD-Score on HUGSIM. Training the planner end to end costs 190 GPU-hours for Latent-WAM++ versus 1,600 for Latent-WAM, a reduction of 88.1%.

---


### 141. [VAComp: View-Aware Full Projector Compensation](https://arxiv.org/abs/2611.10637)

**<font color=#1a73e8>作者：</font>** Kai Zhou, Qingyue Deng, Bingyao Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Full projector compensation adjusts a projector's input image to compensate for both geometric and photometric distortions introduced by the projection surface. Existing methods generally treat the viewing condition as a static camera viewpoint. When applied to a moving viewer, existing methods face two key challenges: (1) view-dependent methods require model retraining or recalibration to compensate for novel viewpoints; and (2) NeRF/GS-based view-agnostic methods use structure from motion (SfM) to calibrate the projector-camera systems (ProCams) with an unknown global scale, while view-aware tracking requires calibrating a camera oriented opposite to the projector, which introduces an additional calibration challenge. To address these challenges, we introduce VAComp, the first view-aware framework for full projector compensation for a moving viewer in a naked-eye setting. Using a projector, VAComp enables the viewer to perceive a virtual object that visually replaces the real object or to observe view-consistent modifications of the real object's appearance and material properties. To resolve the SfM scale ambiguity, we use metric calibration as a reference to recover the global scale; to calibrate the oppositely facing camera, we use two checkerboards, one facing the RGB camera and the other facing the depth camera. To balance compensation quality and runtime efficiency, we develop two non-iterative hybrid methods, VAComp-SD and VAComp-SI. Both combine 2D Gaussian-based view-conditioned geometric correction with learned photometric compensation, predicting each compensation image through a single forward pass without per-frame iterative optimization. Real-world experiments show that both methods achieve competitive compensation quality, with VAComp-SD enabling real-time updates and VAComp-SI operating at interactive rates. Project page: this https URL.

---


### 142. [SLA-Aware Task Offloading in the IoT Edge-Cloud Continuum: Class-Weighted Deep Reinforcement Learning Against an Exact Optimum](https://arxiv.org/abs/2611.10638)

**<font color=#1a73e8>作者：</font>** Shilpa Golla, Tharun Kumar Korine Palli, Urmila Bandaru  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (RL) is often used to decide where Internet of Things (IoT) tasks with different latency limits run in the edge-cloud continuum, yet some methods give every missed task the same penalty and few compare their agents with an optimal policy. This benchmark study builds four offloading systems small enough to solve exactly by dynamic programming and measures reward and learner against the optimum. A bonus for a met limit makes each miss cost its penalty plus the bonus, which shifts the class weights of published per-class rewards. A class-blind penalty stays 65% to 118% above the optimal cost even with a perfect learner, while a corrected per-class penalty comes within 0.13% of the optimum. With a per-class reward, tuned proximal policy optimization (PPO) agents come within 9% to 11% of the optimum in the smallest system, and the corrected one beats a tuned reservation rule in 9 of 10 seeds. In larger systems the agents stay 41% to 76% above the optimum, and a tuned rule beats their mean. Training ten times longer does not close this gap, and a PPO-Lagrangian agent with reachable targets does no better than the per-class reward.

---


### 143. [Agent2BIM: A Systematic Evaluation of Reality-Capture Configurations and Prior Models for As-Built Modeling](https://arxiv.org/abs/2611.10644)

**<font color=#1a73e8>作者：</font>** Boyu Wang, Borja García de Soto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI agents can generate as-built Building Information Models (BIMs) from reality-capture data, but the evidence required for accurate reconstruction remains unclear. This paper presents Agent2BIM, an agent-based Scan-to-BIM framework, and evaluates seven capture configurations in a research laboratory and a mechanical, electrical, and plumbing (MEP) scene. Inputs include 360° panoramas, smartphone video, smartphone LiDAR, terrestrial laser scanning (TLS), TLS with posed panoramas, and imagery supplemented by prior IFC models. Outputs are compared against TLS-verified reference models for component detection, geometric accuracy, and MEP connectivity. In the laboratory, component recall ranged from 84% to 100%, but only 9% of components reconstructed from panoramas were within 20 cm of their reference positions, compared with 86% using smartphone LiDAR. In the MEP scene, scale-free inputs recovered 11 - 43% of components, versus 75 - 93% for metric inputs. Prior IFC models improved MEP reconstruction but could propagate inaccuracies. The results highlight the complementary roles of visual and metric evidence in agent-based Scan-to-BIM.

---


### 144. [SHIN: Scalable Hierarchy for INcremental 3D Gaussian Splatting](https://arxiv.org/abs/2611.10652)

**<font color=#1a73e8>作者：</font>** Reagan Koo, Yeong-Gyu Kim, Eun-Seok Ryu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) provides high-quality real-time novel-view synthesis, but deployment budgets vary across devices and network conditions. Most compact methods target one operating point, so another budget requires a separate representation. SHIN is a scalable 3DGS hierarchy with a reusable Base and additive enhancement layers, so each higher-quality operating point extends rather than replaces the decoded representation. Constructing this hierarchy requires deciding which Gaussians each stage adds and how much spherical-harmonic (SH) appearance each retains, because these choices remain fixed in later prefixes. SHIN derives one shared Gaussian order from multi-scale position-scale sensitivity and divides each stage budget between adding Gaussians and retaining SH bands using calibrated gradient-based scores per byte. Lightweight opacity updates adjust compositing while transmitted geometry and SH coefficients remain unchanged. Across three benchmarks, SHIN progressively improves one cumulative representation and achieves the best PSNR-size efficiency in every overlapping comparison with the multi-rate and progressive baselines.

---


### 145. [FG-DSA: Frequency-Guided Depthwise Separable Attention for Efficient Dense Prediction](https://arxiv.org/abs/2611.10653)

**<font color=#1a73e8>作者：</font>** Yiyao Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense prediction and generative modeling in resource-constrained scenarios remain challenging, as repeated downsampling substantially reduces spatial detail and degrades boundaries. Although recent attention mechanisms have alleviated the problem of semantic ambiguity, they often fail to preserve high-frequency features or do so at the expense of a very high computational cost. In this paper, we propose the Frequency Guided Depthwise Separable Attention for Efficient Dense Prediction (FG-DSA), a novel framework for efficient dense visual understanding and generation. FG-DSA employs a 2D FFT high-pass filtering module to explicitly inject frequency domain priors into the spatial attention mechanism, allowing lightweight networks to recover sharp boundary transitions with linear complexity. A range of experiments show that FG-DSA is effective at recovering fine object boundaries and leads to a consistent performance gain in the task of semantic segmentation. Importantly, we show that FGA-DSA can be used as a module in diffusion-based generative U-Nets, leading to a significant improvement in the detail of the generated images with very little additional parameter and Floating Point Operation (FLOP) cost.

---


### 146. [STABLE: A Continual Learning Optimizer with Adaptive Drift Control](https://arxiv.org/abs/2611.10655)

**<font color=#1a73e8>作者：</font>** Xiaoyan Li, Lanpei Li, Massimo Coppola 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning suffers from catastrophic forgetting, leading to the loss of past knowledge and unstable adaptation across task streams. Existing approaches typically address this issue through replay buffers, architectural changes, or additional regularization terms. We argue that forgetting is a consequence of unstable learning dynamics, which may benefit from an optimizer-level solution. The main challenge is that learning dynamics are time-dependent, as demonstrated by empirical phenomena such as the stability gap. First, we formally prove that, for distance-based classifiers, bounded parameter drift guarantees bounded margin erosion under a local score-stability condition. Based on this insight, we propose STABLE, a primal-dual optimizer with adaptive drift control. STABLE enforces a drift budget by increasing the dual variable when the budget is violated and decreasing it otherwise. This results in high stability without penalizing plasticity. Experiments on long-horizon unimodal streams and CLIP-based multimodal streams show that vanilla PEFT baselines trained with STABLE match or outperform specialized continual learning methods. In the multimodal setting, STABLE further preserves zero-shot transfer, matching or exceeding dedicated multimodal continual learning methods.

---


### 147. [The Delta Gap: Cellular World Models for Perturbation Response Prediction Are Far Harder Than Global Correlation Implies](https://arxiv.org/abs/2611.10658)

**<font color=#1a73e8>作者：</font>** Junhui Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cellular world models aim to predict how cells respond to genetic perturbations, analogous to world models in reinforcement learning. Perturbation response models are evaluated almost exclusively by global Pearson correlation between predicted and observed transcriptomes. We show this metric is dominated by thousands of non-responsive genes and severely inflates apparent performance. On the Replogle K562 screen (509 unseen perturbations, 5000 genes), GEARS achieves global Pearson 0.977, but its delta Pearson is only 0.076. A trivial baseline predicting mean training delta achieves 0.267, which is 3.5x better than GEARS. Our primary contribution is methodological: we identify and quantify this delta gap as a systematic evaluation artifact, and propose delta-space evaluation as the primary benchmark. We provide two post-hoc corrections (RWR on co-expression graphs and kNN matching) and show that 2.8x of the remaining gap lies in perturbation representation geometry, not decoder capacity. We further show the gap is partially addressable end-to-end: delta-aligned training (lambda = 3.0) raises delta Pearson to 0.179 on Replogle (2.35x over GEARS) and surpasses the trivial baseline on direction accuracy (0.680 vs 0.567) and gene recovery (1.52 vs 1.19); combined with kNN it reaches 0.217. An amplitude-calibration variant (eta = 0.3) further raises gene recovery to 2.16 while reaching 0.218. Critically, these representations transfer zero-shot across cell lines: from Replogle K562 to unseen Norman A549, the delta-aligned model reaches 0.328 on 741 shared genes, 4.7x a trivial baseline and 2.1x standard GEARS. This is the first systematic quantification of the delta gap, and the first diagnostic framework localizing the residual gap to perturbation representation geometry via an oracle upper bound.

---


### 148. [Dynamics-Informed Action Learning for Goal-Conditioned Latent Planning](https://arxiv.org/abs/2611.10660)

**<font color=#1a73e8>作者：</font>** Yinuo Jiang, Guangzhi Wang, Yiran Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent world models enable visual control by planning action sequences in compact representation spaces, but a gap remains between how latent dynamics are learned and how they are used for planning. First, teacher-forced training does not expose the dynamics model to the recursively predicted latent states encountered during planning. Second, sampling-based planners typically initialize action search from goal-agnostic proposals, without exploiting the action-conditioned dynamics learned by the world model. We introduce Dynamics-Informed Action Learning (DIAL) to bridge these two gaps. During training, rollout alignment exposes the forward model to its own autoregressive latent predictions, while multi-step inverse supervision trains a lightweight inverse dynamics head to infer actions from latent-state transitions. We further apply the inverse head to model-generated transitions with its parameters held fixed, encouraging predicted rollouts to retain action-relevant information. At test time, DIAL autoregressively couples the inverse and forward dynamics to construct a dynamics-informed action sequence toward the goal, which initializes the mean of the Cross-Entropy Method (CEM) proposal distribution. The subsequent CEM search then refines this initialization using the standard sampling and updating procedure. Experiments across four visual control benchmarks demonstrate that DIAL outperforms existing latent world models and planning baselines in both standard and long-horizon scenarios.

---


### 149. [Physically Guided TeX Generation for Low-Light Visual Tasks](https://arxiv.org/abs/2611.10665)

**<font color=#1a73e8>作者：</font>** Daoheng Li, Jianjun Qian, Mengkai Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light conditions reduce visible contrast and obscure details, while infrared images lack color and texture, motivating the fusion of infrared and visible information for visual tasks. Existing fusion methods primarily optimize image appearance or task-specific features without explicitly disentangling the coupled factors underlying thermal observations, limiting their physical interpretation under thermal degeneracy. Hyperspectral thermal measurements enable physical decomposition, but they require specialized imaging hardware, while pixel-level physical annotations for supervision or evaluation incur additional costs. We propose TeX-Gen, a physically guided framework for TeX generation from paired visible and infrared images in low-light visual tasks. TeX Generation constructs complementary multi-view features and employs independent branch-specific gates to route cues into the Temperature, Emissivity, and Texture maps. TeXMetric integrates radiometric reconstruction, channel structure, and material consistency to assess the generated maps without requiring pixel-level physical labels. TeX Tune improves performance through task-guided adjustments, jointly optimizing the adjustment modules and task network while keeping the generator frozen. Experiments show that TeX-Gen achieves competitive task performance in low-light environments on the FLIR, LLVIP, M3FD, and MSRS datasets. Experiments on HADAR also examine the association between TeXMetric scores and downstream detection performance.

---


### 150. [Causal Heteroscedastic Structure Learning From Incomplete Temporal data](https://arxiv.org/abs/2611.10668)

**<font color=#1a73e8>作者：</font>** Abdellah Rahmani, Pascal Frossard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discovering causal structures in multivariate time series (MTS) is critical in domains such as finance and neuroscience, yet remains challenging in practice due to three distinct obstacles. First, MTS are routinely corrupted by missing values, where naive impute-then-discover pipelines distort the underlying data distribution and yield spurious causal graphs. Second, identifying instantaneous effects is difficult even on complete data, and missingness further entangles imputation with graph recovery. Third, real-world data frequently exhibits heteroscedastic noise with variance driven by both instantaneous and lagged causes, violating the core assumptions of standard discovery methods. Existing approaches fail to address these challenges concurrently, typically presuming complete data, homoscedastic noise, or strictly time-lagged relationships. Crucially, we show through ablation studies that resolving these issues sequentially, rather than jointly, leads to a substantial degradation in performance. To overcome this, we introduce Cheesefill, an optimal transport framework for causal structure learning under missingness and heteroscedastic noise. Cheesefill parameterizes causal mechanisms using conditional normalizing flows and jointly learns a stochastic correction map that refines naive imputations into trajectories consistent with the inferred causal mechanisms. Theoretically, we prove that optimizing over stochastic correction maps is equivalent to a conditional kernel reformulation of the Kantorovich problem, from which our neural parameterization yields a tractable objective. Extensive experiments on synthetic and real-world benchmarks demonstrate that Cheesefill consistently outperforms existing baselines across diverse missingness regimes.

---


> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
