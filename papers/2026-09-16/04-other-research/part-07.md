# 📦 其他研究 | 2026年09月16日

> 本类共 **416** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-416](./part-09.md)

---

### 301. [Sensory Precision Inference for Multimodal Arbitration under Uncertainty](https://arxiv.org/abs/2609.15065)

**<font color=#1a73e8>作者：</font>** Tin Mišić, Takato Horii  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous agents operating on multisensory data cannot assume that all sensory modalities remain consistently informative. In real environments, sensory streams are frequently corrupted by noise, missing data, or inter-modal incongruence, requiring adaptive arbitration between competing sensory hypotheses. While active inference provides a principled framework for uncertainty-guided inference, the role of dynamically inferred sensory precision in generative multimodal arbitration under sensory conflict remains comparatively underexplored. We propose a multimodal perceptual inference model in which latent beliefs and modality-specific sensory precisions are jointly updated through iterative free-energy minimization. In our proposed model, sensory precision dynamics not only reflect sensory uncertainty but actively shape the evolution of latent beliefs during multimodal conflict. In addition, we introduce a learned prior over sensory precisions that induces structured, class-dependent precision patterns and influences cross-modal inference dynamics. We evaluate the model using a synthetic multimodal MNIST dataset combining visual, auditory, and tactile representations of digit classes under controlled sensory noise and inter-modal incongruence. Results show that dynamic precision inference improves reconstruction robustness under corrupted sensory evidence, supports coherent latent inference from reduced sensory evidence, and enables stable arbitration between conflicting modalities. Furthermore, learned precision priors generate interpretable precision structures that shape inference dynamics and cross-modal latent structure. These findings support sensory precision inference as a mechanistic control process for adaptive multimodal belief formation under uncertainty, highlighting precision dynamics as a computational mechanism for robust and interpretable multisensory integration.

---


### 302. [Branched Optimal Transport Amortization](https://arxiv.org/abs/2609.15072)

**<font color=#1a73e8>作者：</font>** Semyon Semenov, Viktor Kovalchuk, Meir Roketlishvili 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Methods of Branched Optimal Transport (BOT) mimic the economy and efficiency of natural tree-like structures, such as those found in rivers and biological systems. These methods are widely applicable for designing efficient networks in society, from river basins and blood vessels to mail and gas distribution systems. However, they remain understudied in the context of designing deep generative models, particularly at a large scale. Standard continuous-time generative models, such as the flow matching approach, fail to capture the inherent hierarchical and branching patterns present in real-world data. Current models provide no mechanism for flows to merge or share pathways to minimize total transport cost. Inspired by the "economy of scale" principle in BOT, we introduce a novel, scalable branched flow-matching algorithm designed to solve the branched optimal transport problem in high dimensions. Our method adapts the Benamou-Brenier continuous-time optimal transport formulation to learn branched generative flows. These flows allow probability mass to aggregate along common pathways before branching out to diverse targets. Parametrized by neural networks, our method effectively learns complex branched generative processes. We demonstrate its effectiveness on challenging high-dimensional tasks in biology and image generation.

---


### 303. [Ensemble-Conditioned Molecular Design](https://arxiv.org/abs/2609.15077)

**<font color=#1a73e8>作者：</font>** Ross Irwin, Alessandro Tibo, Jon Paul Janet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular design is typically approached as a problem of finding molecules which can adopt a single bioactive conformation. In reality, molecules occupy a distribution over conformations, and many of the properties which determine whether a candidate is viable depend on that distribution rather than on any single conformer. We reframe molecular design as an optimisation of both the modes and properties of molecules' conformational ensembles, where modes can be represented as shapes, pharmacophore profiles or protein pockets, and properties are aggregate scalars computed over the whole distribution. To realise this we introduce ensemble-conditioned guidance, a framework which conditions 3D molecular generative models on both axes simultaneously. Mode conditions are composed adaptively at inference by combining the vector fields produced under each condition. Conditions may be targeted or avoided, mixed across modalities and combined in arbitrary numbers, allowing a wide range of design tasks to be expressed with a single trained model. We introduce adaptive symmetry learning to allow conditions from different reference frames to be composed, and extend our generative framework to enable flexible-size generation. We evaluate on new benchmarks for multi-mode conditioning and ensemble property optimisation, and apply the framework to two practical drug discovery tasks, dual-target binder design and active-state-selective agonist design, where in both cases conditioning on the additional state improves the desired outcome over single-state conditioning.

---


### 304. [$\mathbb{SL}(n)$ Representation Learning: An Intrinsic Mixed-Curvature Space with Higher Curvature Capacities and Deeper Order-Aware Composition](https://arxiv.org/abs/2609.15083)

**<font color=#1a73e8>作者：</font>** Xingrun Li, Yusuke Mukuta, Xin Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-curvature representation learning seeks to capture rich geometric structures that cannot be adequately modeled by a single curvature regime. Existing approaches largely rely on product manifolds, which require manually specifying how different curvature spaces are combined and separate their curvature contributions across factors. We introduce the $\mathbb{SL}(n)$ space, a representation geometry defined by the simple $\det(A)=1$ constraint and a left invariant Schatten-$p$ Finsler structure. Despite this minimal construction, $\mathbb{SL}(n)$ exhibits pointwise negative, zero, and positive flag curvature around a common flagpole, while its mixed-curvature and curvature-coupling capacities are asymptotically maximal relative to the intrinsic geometric upper bound. Beyond geometry, its noncommutative group structure provides inherent order sensitivity, and its non-nilpotent Lie algebra admits nonzero nested Lie brackets at arbitrary depth, enabling deep order-aware composition. Empirically, $\mathbb{SL}(n)$ consistently outperforms a broad range of representation manifold baselines across graph benchmarks at different scales. It reduces average distortion over the strongest baselines by $44.3\%$ on KEGG and $40.5\%$ on HumanCyc, and improves Hits@20 by $42.8\%$ on OGBL-PPA. Experiments on Flickr30k-Order further support its ability to capture higher order dependencies from ordered composition. Together, these results show how a seemingly simple structural constraint can yield unexpectedly rich geometry, capacity, and composition within a unified representation space.

---


### 305. [OpenAI4S: Code as Action, Science as Sessions](https://arxiv.org/abs/2609.15096)

**<font color=#1a73e8>作者：</font>** Gongbo Zhang, Hao Li, Yu Wang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI co-scientists could accelerate computational research, but over a long-running study the workflow also has to stay inspectable, resumable and reproducible, which requires persistent computational state and provenance. Here we present OpenAI4S, an open-source scientific research agent built around the principle of \emph{Code as Action, Science as Sessions}. OpenAI4S combines a persistent computing runtime with research-session management: orchestration is handled through structured tool calls, while scientific actions are represented as complete code cells executed in persistent Python and R kernels. An append-only Action Ledger, per-cell execution records, versioned artifacts, environment records, and workspace checkpoints preserve how results were produced and support session recovery, branching, and extension. Configurable sandboxing, permission controls, and code and trajectory screening provide complementary safeguards. We evaluate OpenAI4S on 36 research scenarios spanning retrosynthesis, molecular dynamics, protein binder design, protein mutation, catalyst screening, and mineral spectroscopy, measuring scientific task accuracy, workflow completeness, and reproducibility of the resulting repositories. OpenAI4S achieves an overall score of 7.83, compared with 5.7--6.4 for a general-purpose coding harness evaluated with three frontier models, with the largest gains on long-horizon and computation-intensive workflows. These results suggest that integrating persistent execution with session-level provenance can improve the reliability of AI-assisted scientific workflows. Environment specification and full rerunnability remain weak for every evaluated system, ours included, so reproducibility is still an open problem for scientific agents. The system is available under the MIT license at \href{this https URL}{this http URL}.

---


### 306. [LG-VLN: A Zero-Shot Vision-and-Language Navigation Framework with LangGraph State Orchestration](https://arxiv.org/abs/2609.15098)

**<font color=#1a73e8>作者：</font>** Jianhe Zhao, Yanhua Qiu, Zhiyu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous-environment vision-and-language navigation (VLN-CE) requires interpreting natural-language instructions in unseen 3D environments and executing continuous low-level actions. Existing methods often depend on LiDAR, panoramic cameras, or extra sensors; separate geometric-mapping and semantic-navigation visual representations can cause long-trajectory spatial-semantic inconsistencies. We propose LG-VLN, a monocular zero-shot framework with shared visual features and LangGraph-based state orchestration. An online feed-forward 3D reconstruction network predicts depth, camera poses, and dense point clouds for agent-pose estimation and global map fusion. Geometry and navigation share dense CleanDIFT features: semantic consistency rejects incorrect inter-frame correspondences, while target-instance constraints define visual references whose similarity combines with local BLIP-2 image-text relevance to form a semantic value map. LangGraph represents instruction parsing, geometric perception, semantic value updates, path planning, action execution, and failure recovery as a directed state graph with conditional transitions, persistent state, and modular recovery mechanisms. On a fixed 550-episode subset of the R2R-CE val-unseen split, LG-VLN achieves 21.3% success and 12.1% success weighted by path length. Ablations show shared semantic features improve navigation, further boosted by combining visual similarity and image-text relevance. Results establish shared visual representations and explicit state orchestration as effective for zero-shot VLN-CE using monocular RGB alone. Code will be publicly released for reproducibility.

---


### 307. [DNF-SR: Dual-Input and Negative-Aware Feature Fine-Tuning for Real-World Image Super-Resolution](https://arxiv.org/abs/2609.15120)

**<font color=#1a73e8>作者：</font>** Shuhao Han, Wenjie Liao, Hayden Vance 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benefiting from the powerful generative priors of diffusion models, diffusion-based real-world image super-resolution (Real-ISR) methods have demonstrated impressive this http URL achieve efficient Real-ISR, several recent works have designed one-step diffusion-based this http URL, unmediatedly feeding LR into a diffusion model creates a distributional gap with the model's original input.A straightforward approach to reduce the distribution gap is to introduce noise to the LR latents. However, directly adding noise inevitably corrupts the content of the LR this http URL this study, we propose DNF-SR, a Dual-input and Negative-aware Feature fine-tuning method for this http URL, we use a dual-input strategy that concatenates the original LR image with the noisy LR input and feeds them into a diffusion-based image editing model, ensuring both high-fidelity one-step super-resolution and improved perceptual and content this http URL, the noise present in the noisy LR input introduces randomness and diversity into the outputs. We exploit this property and propose a post-training optimization method, Negative-aware Feature Fine-Tuning (NF2T), which guides the model toward producing higher-quality this http URL^2T classifies multiple outputs into positive and negative subsets and then defines implicit policy improvement directions in both the image and feature spaces, thereby further enhancing the stability of the this http URL experiments show that DNF-SR outperforms other this http URL will be released.

---


### 308. [Refinement-based Flow Policy Optimization](https://arxiv.org/abs/2609.15123)

**<font color=#1a73e8>作者：</font>** Bumgeun Park, Hyukjun Yang, Donghwan Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-based policies offer an expressive representation for online reinforcement learning, but conventional flow matching requires samples drawn from the distribution to be modeled. This poses a challenge when the desired action distribution is defined only implicitly by a Q-function, since directly sampling actions from the resulting distribution is generally intractable. We propose Refinement-Based Flow Policy Optimization (RFPO), a novel framework for training a flow policy in online reinforcement learning by alternating between Q-guided sample refinement and self-target flow matching. RFPO first generates actions from Gaussian noise using the current flow policy and then uses a finite-step stochastic refinement procedure to move them toward an energy-based distribution induced by the Q-function. Each refined action is then paired with its corresponding initial noise sample and used as a fixed target for flow-matching training. By repeatedly refining its own outputs and learning from the resulting targets, RFPO incorporates Q-guidance into the policy without requiring direct samples from the target distribution, while retaining the capacity to represent multiple action modes. We further provide a theoretical analysis of the distributional dynamics induced by RFPO. Across six continuous-control tasks, RFPO matches or outperforms a standard Gaussian-policy baseline on almost every task. Experiments on six synthetic two-dimensional target distributions with diverse geometries demonstrate that RFPO captures complex multimodal structure without mode collapse.

---


### 309. [SparseTalk - Sparsifying 3D Gaussian Language Fields for Efficient 3D Visual Question Answering](https://arxiv.org/abs/2609.15137)

**<font color=#1a73e8>作者：</font>** Davit Soselia, Joseph JaJa, Amitabh Varshney  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian language fields provide an explicit, spatially grounded representation for 3D visual question answering (VQA), but their dense semantic features can require tens of thousands of embeddings per scene, resulting in substantial storage, memory, and inference costs. We investigate how much of this representation is actually necessary for downstream reasoning. Starting from a full embedding representation, we systematically sparsify its semantic embeddings, including the previously underexplored regime below a single image-equivalent block down to 8 visual tokens. We compare random, geometric, semantic, and joint spatial-semantic selection strategies and introduce an object-based sparsification method that distributes the token budget across detected object instances while retaining background context. Experiments on ScanQA and MV-ScanQA reveal substantial redundancy in dense Gaussian language fields. Strong VQA performance is retained with only a few hundred semantic embeddings, corresponding to less than 1% of the original representation. Object-based selection performs well relative to others, with only modest observed changes down to 256 tokens. At this budget, SparseTalk retains 0.80% of SplatTalk's 32,076-token inference input and 0.332% of the mean 77,207-Gaussian dense field, increasing inference throughput while reducing decoded-feature memory 125-fold.

---


### 310. [Automated Perceptually-Motivated Assessment of Photographic Consistency in Paired Clinical Photographs: Pipeline Development and Internal Evaluation](https://arxiv.org/abs/2609.15144)

**<font color=#1a73e8>作者：</font>** Derrick Lin, Samantha Rabinovich, Joclin Rabinovich 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Paired pre- and post-operative photographs are the standard unit of evidence for plastic surgical outcomes, yet no objective metric verifies whether two images of the same patient were captured under conditions consistent for comparison.
Approach: We developed a perceptually motivated pipeline that analyzes pre/post pairs across thirteen calibrated sub-metrics, partitioned by unsupervised correlation-structure analysis into five data-driven clusters (photometric, texture / sharpness, pose, illumination direction, and pitch), averaged within each cluster and combined across clusters by a weighted sum into a single consistency score. Each sub-metric is calibrated so that its median difference across published within-patient pairs scores 0.5, which is a reference point and carries no pass/fail meaning. The pipeline was calibrated on 134 matched within-patient published pre/post pairs and evaluated against identical-image pairs, synthetic-perturbation pairs, and 134 mismatched cross-publication pairs.
Results: The master consistency score S separated matched from mismatched pairs (sensitivity index d' = 2.15, 95% confidence interval (CI) [1.83, 2.55]; area under the receiver operating characteristic curve AUC = 0.928, 95% CI [0.896, 0.959]), closely matching Gaussian-equal-variance predictions. The three head-pose angles did not fall in one cluster: yaw and roll grouped together while pitch separated. Identical pairs scored at ceiling (S = 0.99) and the master score fell monotonically with perturbation magnitude on all five perturbation axes.
Conclusions: The score quantifies photographic comparability, not aesthetic or surgical quality, and provides a freely available web tool for auditing the photographic comparability of pre/post pairs, pending validation against expert judgment.

---


### 311. [Multi-source Transfer Learning of Time Series with a Shapelet-based Distance Measure](https://arxiv.org/abs/2609.15148)

**<font color=#1a73e8>作者：</font>** Jiseok Lee, Brian Kenji Iwana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transfer learning is an effective technique for addressing data scarcity in deep learning for time series classification, but its success depends on the selection of source datasets. Conventional transferability estimation methods are often computationally expensive, as they require fully pre-training a model on each potential source dataset to assess its suitability. This paper introduces a novel, training-free source selection method named Shapelet Matching. Our approach first identifies discriminative shapelets from the target and potential source datasets. Then, Shapelet Matching quantifies dataset similarity by comparing the extracted sets of shapelets. To mitigate the risk of negative transfer from selecting an unsuitable single source, we introduce a multi-source transfer learning method. We select several source datasets based on their shapelet-based similarity scores, combine them into a single multi-source dataset, and use this aggregated dataset for pre-training. The model is then fine-tuned on the target task. We evaluated our method on 128 datasets from the UCR Archive using both temporal CNN and Transformer architectures. The empirical results demonstrate that our multi-source pre-training reduces the risk of negative transfer on average. Shapelet Matching achieves the strongest performance for the CNN backbone and remains competitive for patch-based Transformer architectures, while avoiding the cost of pre-training a separate model for every candidate source.

---


### 312. [Weakly Supervised Spatial Grounding for Discriminative Attention-Based Ultrasound-Histopathology Alignment in Prostate Cancer Grading](https://arxiv.org/abs/2609.15150)

**<font color=#1a73e8>作者：</font>** Obed Korshie Dzikunu, Emma Willis, Mohammad Mahdi Abootorabi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unpaired cross-modal distillation transfers grade structure from histopathology into a micro-ultrasound (micro-US) encoder by aligning a pooled needle-region embedding to a frozen histopathology teacher under grade-group correspondence alone. A single objective is thereby required to serve two distinct functions: rendering patch features discriminative of tissue state, and selecting which patches enter the pooled representation. We decouple them. Weak spatial supervision derived from percentage involvement, recorded routinely at biopsy, constrains the predicted proportion of malignant tissue within each core, acting on the encoder features independently of the alignment objective. The alignment loss then operates on features that differ across a core, and attention concentrates on a subset of patches rather than remaining near-uniform. On 7,166 biopsy cores from 811 patients across seven centers under patient-level 5-fold cross-validation, the method reaches 67.1 macro AUC and 68.5 csPCa AUC, against 61.2 and 52.8 for the existing unpaired alignment method and 63.1 and 62.6 for the strongest unimodal baselines. Ablation against existing attention regularizers designed to prevent attention-uniformity collapse shows that such regularizers do not substitute for label-derived supervision: they constrain the attention distribution, whereas the signal required acts on the features that attention reads.

---


### 313. [PACE: Progressive Angular-to-Norm Contrastive Embedding](https://arxiv.org/abs/2609.15152)

**<font color=#1a73e8>作者：</font>** Yanping Li, Wei Zhou, Yawen Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal embedding models encode heterogeneous inputs into a shared embedding space, enabling efficient similarity computation across modalities and tasks. Most existing methods optimize cosine-based contrastive objectives, which promote stable training but restrict semantic compatibility to angular geometry, precluding embedding norms from serving as an additional semantic signal. However, directly optimizing the more expressive dot-product similarity, which leverages both angular and norm information, underperforms cosine-based training and exhibits unstable training dynamics. We attribute this discrepancy to premature optimization-space expansion, manifested as angular--norm entanglement and directional anisotropy in the representation space and further compounded by full-parameter fine-tuning. In this paper, we propose PACE, a two-stage framework that progressively expands both the representation and trainable parameter spaces. Stage I combines cosine-based objective with low-rank adaptation to establish a reliable angular geometry within constrained optimization spaces. Stage II switches to dot-product similarity and full-parameter fine-tuning, enabling embedding directions and norms to jointly encode semantic information. We further introduce Focal Embedding Loss, a confidence-adaptive objective that downweights queries with high positive retrieval confidence while emphasizing ambiguous queries with competitive negatives. Experiments across multiple backbone scales and diverse multimodal embedding tasks consistently validate the effectiveness of PACE.

---


### 314. [CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search](https://arxiv.org/abs/2609.15164)

**<font color=#1a73e8>作者：</font>** Sriram Selvam, Anneswa Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When several retrieved sources support the same claim, an answer engine cites some but not others. We call this decision citation allocation and introduce CITECHOICE, a causal audit of authentic multi-turn agentic search. From 129 everyday-query transcripts, CITECHOICE selects 113 same-call document pairs with independently verified support for the same pre-specified fact, without observing ranks or answer outcomes; blinded human review confirms 103. It runs a hash-verified 2-by-2 replay crossing pair order with jointly generated, fidelity-checked structured and prose renderings of one target while the rest of the transcript remains fixed.
Three results emerge. First, and most importantly, structured rendering concentrates citation credit rather than clearly increasing source admission. It raises target citation count by +0.50 citations per answer (95 percent CI [+0.20, +0.84]; Holm-adjusted p=.033), without increasing total citations or reducing competitor credit. The pre-specified incidence effect (whether the target is cited at all) is +4.5 percentage points and inconclusive (95 percent CI [-1.4, +10.4]; p=.168). Second, observational position differences exceed controlled reordering effects: the citation-rate gap between rank 1 and rank 5 is 42.3 percentage points, compared with +7.9 percentage points in the main replay and 0.0 percentage points held out. Third, citation evaluation has a measurable noise floor. Although the aggregate count effect repeats under fresh decoding of 30 frozen families, 15 percent of binary decisions change and decoding accounts for an estimated 45 percent of single-generation family-effect variance. Together, these findings isolate what survives control: presentation can causally redistribute visible citation credit within frozen transcripts. They do not establish reliable source admission, a pure formatting mechanism, or a general rank advantage.

---


### 315. [Nearly Minimax-Optimal Regret for Linear Contextual Bandits with Arbitrary Adaptive Action Sets](https://arxiv.org/abs/2609.15170)

**<font color=#1a73e8>作者：</font>** Tianyuan Jin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study stochastic linear contextual bandits with arbitrary action menus that may depend on the fixed parameter and the interaction history. We establish matching upper and lower bounds, up to logarithmic factors. Let $d$ be the dimension, $K$ be the menu size, and $T$ the time horizon. For $2\le K\le d$, we prove an upper bound $\widetilde O(K^{1/4}\sqrt{dT})$. When $T\ge d^2$, we further prove a lower bound $\Omega(K^{1/4}\sqrt{dT})$. Thus, for $T\ge d^2$ and $2\le K\le d$, the upper and lower bounds match up to logarithmic factors, and the polynomial dependence on $K$ is optimal. Compared with the previous $\widetilde O(\sqrt{dKT})$ bound, our upper bound improves the dependence on $K$ by a factor of $K^{1/4}$.
For $K\ge d$, we prove an upper bound $\widetilde O_{d,T}\left(\sqrt{dT}\min\{\sqrt d,(d\log K)^{1/4}\}\right)$ and a lower bound $\Omega\left(\sqrt{dT}\min\left\{\sqrt d,\left(\frac{d\log K}{\log(2d)}\right)^{1/4}\right\}\right)$. Here, $\widetilde O_{d,T}$ omits logarithmic factors only in $d$ and $T$. In particular, for polynomially large $K\ge d$, the upper and lower bounds both scale as $d^{3/4}\sqrt T$ up to logarithmic factors, improving the standard $\widetilde O(d\sqrt T)$ rate by a factor of $d^{1/4}$. As $K$ grows further, the regret smoothly recovers the $d\sqrt T$ scale once $\log K$ reaches order $d$.

---


### 316. [EECTracker: Swarm Motion Prior-Guided Feature Compensation for Airborne Optical UAV Swarm Tracking](https://arxiv.org/abs/2609.15171)

**<font color=#1a73e8>作者：</font>** Zhaochen Chu, Tao Song, Ren Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Airborne optical tracking of uncrewed aerial vehicle (UAV) swarms is challenging due to extremely small target scales, rapid viewpoint changes, and cluttered backgrounds, which can weaken target feature responses and lead to intermittent or temporarily missing detector responses. Existing multi-object tracking methods generally depend on reliable target-specific detector responses to maintain target states and identities across frames. When such responses become unreliable, target states cannot be reliably updated and cross-frame association cues become ambiguous, resulting in fragmented trajectories and identity switches. To address this problem, we propose EECTracker, a swarm-motion-prior-guided joint detection-and-tracking framework for airborne optical UAV swarm tracking. EECTracker constructs a probabilistic swarm motion prior from reliable historical tracklets to capture the shared short-term image-plane motion tendency of the swarm and its uncertainty, providing spatial guidance for cross-frame feature compensation. Building on this prior, we introduce Energy--Entropy Consistency Activation (EEC Activation) to evaluate motion-prior-conditioned feature consistency using feature residual energy and local residual entropy. The resulting Local EEC score guides pixel-level feature compensation by enhancing motion-prior-consistent feature responses in potential target regions while suppressing inconsistent background responses. Experiments on AIRMOT and UAVSwarm show that EECTracker achieves superior overall tracking performance compared with state-of-the-art methods. Compared with the strongest competing method SCT-MOT, EECTracker improves MOTA/IDF1 by 3.89/1.79 percentage points on AIRMOT and by 2.81/1.74 percentage points on UAVSwarm, while maintaining online inference speed.

---


### 317. [Does Attention-Guided Masking Really Help Object Discovery in Object-Centric Learning?](https://arxiv.org/abs/2609.15187)

**<font color=#1a73e8>作者：</font>** Youliang Tao, Yanhua Han, Bin Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-Centric Learning (OCL) aims to decompose images into objects without human annotations. A major family of mainstream methods uses Slot Attention to aggregate image features into object-level representations and then from them reconstructs masked image content, i.e., Random Masking (RM), to provide self-supervision. The recent method DIAS simply masks image patches at uniform randomness yet achieves competitive object discovery accuracy. Since attention during aggregation already possesses object discovery ability, we explore using it to develop a better image patch masking strategy, i.e., Attention Guided Masking (AGM), thereby providing better self-supervision. Results on six recognized datasets show that AGM does not always outperform RM. Under unconditional slot initialization, AGM substantially improves background segmentation on datasets with realistic textures (COCO and VOC); Regardless of conditional or unconditional slot initialization and across datasets, foreground object discovery remains comparable or decreases. We suggest peer researchers in the OCL community that attempts to exploit internal attention semantics to improve OCL with masked decoding are risky. Our source code, model checkpoints and evaluation logs will be released upon acceptance.

---


### 318. [Reconstructing Is Not Acting: Action-Centric Latent Dynamics Modeling](https://arxiv.org/abs/2609.15189)

**<font color=#1a73e8>作者：</font>** Dingjie Fu, Dianxing Shi, Yangyang Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent action models (LAMs) learn action representations from unlabeled videos by inferring latent actions from visual transitions and reconstructing future states. However, we identify a fundamental $\textbf{reconstruction-action mismatch}$: lower reconstruction error does not necessarily yield better latent dynamics or downstream performance. We attribute this mismatch to two underconstrained aspects of reconstruction-based latent dynamics modeling: (i) the inverse dynamics model (IDM) is not explicitly encouraged to distinguish action-related transitions from nuisance appearance, and (ii) the forward dynamics model (FDM) can underutilize the inferred latent action by exploiting predictive shortcuts from the current state. To address both limitations, we propose $\textbf{ACT-LAM}$, a lightweight action-centric framework that strengthens both action extraction and action utilization. Specifically, its Action Query IDM (AQ-IDM) employs learnable action queries and gated aggregation to selectively extract rich action-related transition cues without strong information bottlenecks. And its Action Token FDM (AT-FDM) projects latent actions into action tokens that progressively interact with evolving state representations, enabling continuous state-aware action conditioning. ACT-LAM further streamlines feature processing to concentrate model capacity on latent dynamics modeling. Extensive experiments on several robotic datasets and the VP$^2$ benchmark demonstrate stronger latent action consistency, forward dynamics, and downstream visual planning performance with fewer trainable parameters and lower computational overhead. In particular, ACT-LAM surpasses the previous state of the art by $\textbf{7.6%}$ on the aggregated VP$^2$ success rate. Codes at $\href{this https URL}{url}$.

---


### 319. [What Limits Us? Analyzing Self-Reported Limitations in NLP Research](https://arxiv.org/abs/2609.15191)

**<font color=#1a73e8>作者：</font>** Tawan Thaepprasit, Peeranuth Kehasukcharoen, Ding Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Since late 2022, a Limitations section has become mandatory at many top-tier NLP conferences. The growing number of accepted papers at these venues has resulted in a vast corpus of self-reported limitations that cannot all be manually reviewed, yet remains systematically unanalyzed. Therefore, in this paper, we conduct a large-scale analysis of the Limitations sections from ACL and EMNLP papers published between 2020 and 2025 to understand what researchers disclose about their own work. To do so, we implement a novel human-AI framework for iterative hybrid qualitative coding. This framework enables us to investigate trends in self-reported limitations over time, their correlations with specific paper attributes, and the writing patterns that recur around these disclosures. Our findings offer a critical reflection on the diverse reported challenges as well as the self-reporting practices of researchers in the NLP community.

---


### 320. [Sociotechnical Aspects of Tor Relay Rejection](https://arxiv.org/abs/2609.15192)

**<font color=#1a73e8>作者：</font>** Jules Dejaeghere, Lionel Goffaux, Pierre Luycx 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In 2019, the Tor Project enforced an end-of-life (EoL) policy for Tor versions, leading to the rejection of outdated relays, amounting to a notable fraction of consensus weight. While this policy aids network maintenance, reduces backporting efforts, and shortens vulnerability exposure, its sociotechnical implications remain unstudied.
A user study ($N=26$) reveals that relay operators, though not universally aware of the EoL policy, generally view it favorably. Operational practices vary, occasionally excluding newly installed relays from the network.
Network simulations, grounded in historical data, assess the policy's immediate impact on Tor clients against common adversaries. Results indicate a marginal adversarial advantage, with network churn (i.e., relays entering and exiting) exerting a more pronounced effect on user anonymity. Security metrics are introduced to evaluate relay contributions against two adversary models, enabling ranking by individual utility and security. Analysis of four exclusion rounds shows that a minority of rejected relays typically account for over 50% of the security provided by all excluded relays.
Recommendations for EoL policy implementation are proposed to mitigate potential drawbacks.

---


### 321. [Deep Learning-based Intelligent Diagnosis of Congenital Uterine Anomalies in 3D Ultrasound](https://arxiv.org/abs/2609.15225)

**<font color=#1a73e8>作者：</font>** Yueyue Xu, Yuhao Huang, Jiaxiao Deng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective: To develop an intelligent framework, termed CUA-Net, for the automated classification of congenital uterine anomalies (CUA) without requiring coronal plane reconstruction, and to evaluate its clinical applicability.
Methods: CUA-Net was built on 3D ResNet-18, equipped with a dynamic data resampling strategy to mitigate the data imbalance issue and a hard sample mining technique to fully learn from the difficult cases by loss adjustment. We further proposed the self-supervised reconstruction to comprehensively explore the volumes and the online data augmentation to refine the wrong predictions and enhance the model's generalization. We compared the CUA-Net with different deep-learning methods and junior/senior sonographers in the testing set. The evaluation metrics included accuracy, precision, recall, F1-score, micro-AUC, and macro-AUC.
Results: The proposed CUA-Net exhibited satisfactory performance in both internal and external test sets. In the internal cohort, the model achieved accuracy of 93.88%, precision of 87.01%, recall of 95.92%, F1-score of 88.09%, and micro-AUC of 0.9982 and macro-AUC of 0.9997. In the external set, it maintained good performance with accuracy of 91.52%, precision of 83.27%, recall of 88.63%, F1-score of 81.49%, micro-AUC of 0.9945 and macro-AUC of 0.9990. Our CUA-Net outperformed the junior sonographers across all performance indicators and achieved performance comparable to that of the senior sonographers across most metrics.
Conclusion: The CUA-Net demonstrates favorable accuracy and generalizability in classifying common CUA categories, while showing preliminary potential for recognizing less prevalent anomalies. These capabilities may help optimize clinical workflows and support more standardized diagnosis.

---


### 322. [Closed-form Bayesian homography estimation from noisy point correspondences](https://arxiv.org/abs/2609.15227)

**<font color=#1a73e8>作者：</font>** Hanne Beuter, Sebastian Dorn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While homographies are fundamental to many computer vision tasks, the majority of conventional estimation techniques provide only point estimates without directly quantifying uncertainty introduced by noisy observations. Uncertainty, though, propagates to subsequent processing steps such as camera calibration and 3D reconstruction and is particularly relevant in safety-critical and socially relevant fields including medical imaging, autonomous driving, and defense. We present a fast Bayesian formulation for homography estimation from point correspondences that explicitly incorporates measurement uncertainty and prior knowledge while providing a posterior distribution over the homography parameters. A closed-form solution of the posterior mean of the homography is derived in homogeneous coordinates and supplemented by an iterative Bayesian approach to handle non-linearities. Synthetic experiments demonstrate the applicability to projective transformations and show improved estimation accuracy over DLT under varying noise conditions. Image stitching experiments further demonstrate applicability to real image correspondences while additionally providing uncertainty information.

---


### 323. [Unsupervised Point Cloud Registration via Training-Time Semantic Guidance](https://arxiv.org/abs/2609.15228)

**<font color=#1a73e8>作者：</font>** Kezheng Xiong, Shiyun Xu, Sheng Ao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised registration of large-scale LiDAR point clouds remains challenging due to the geometric ambiguity inherent in outdoor scenes, which degrades pseudo-label quality and leads to suboptimal convergence, particularly for sparse, low-resolution scans such as those from nuScenes. We reveal that registration models intrinsically encode semantic awareness that strongly correlates with registration accuracy, albeit without explicit semantic supervision. However, this native awareness is fragile: noisy supervision arising from geometric ambiguity in unsupervised settings rapidly erodes the learned semantic structure, causing performance collapse. To this end, we propose CAESAR, a teacher-student framework guided by an off-the-shelf 3D segmentation model exclusively during training. We observe that potential inlier matches are often buried just beneath a few spurious neighbors in the noisy feature space, motivating Dual-Cue Guided Re-Matching to recover them through reselection rather than simply rejecting. Building on this, a train-only Semantic-Geometric Label Mining performs lightweight, batch-specific teacher refinement and mines reliable pseudo-labels under semantic guidance. We further introduce Semantic Predictive Distillation to consolidate the student's semantic awareness in the feature space. Extensive experiments on KITTI and nuScenes demonstrate state-of-the-art performance, with pronounced gains on the challenging nuScenes benchmark. Crucially, CAESAR incurs zero inference overhead and requires no semantic annotations on the registration data. Code will be released.

---


### 324. [ProtoGuide: Prototype-Driven Guidance for Class-Conditional Graph Generation](https://arxiv.org/abs/2609.15239)

**<font color=#1a73e8>作者：</font>** Salvatore Romano, Marco Grassia, Pietro Liò 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models are a prominent family for graph generation, but standard class-conditional mechanisms embed the class signal in the denoiser during training, tying the conditioning mechanism to the trained model. Classifier guidance avoids this coupling in continuous domains by steering a frozen model with a classifier's gradient, but discrete graph diffusion samples discrete edge states, so gradients cannot propagate through the sampled graph. We introduce ProtoGuide, a post-hoc, backbone-agnostic framework that recovers an analogous mechanism. At each reverse step the denoiser's per-edge output is relaxed into a differentiable soft adjacency, embedded by a frozen Siamese graph neural network, and scored against a target-class prototype and its nearest competitor; the resulting per-edge gradient, damped by a cosine schedule, is injected back into the denoiser output. All components stay frozen, so guidance is retargeted by supplying a different prototype. On five classes of real-world networks and two architecturally different backbones, EDGE and DiGress, ProtoGuide raises macro classification accuracy from 50.7% to 73.5% and from 73.6% to 83.8%, and outperforms DiGress's built-in conditional training under our configuration. Gains are largest where the unguided models are weakest, and are not uniform across classes. Per-graph coverage remains high in most settings, while distributional effects are class-dependent. A Best-of-N selection baseline matches this accuracy given enough oversampling, but at a substantial cost in graph diversity. An independently initialized classifier, a directionality test, and a few-shot analysis support target-directed steering and robustness to very small support sets.

---


### 325. [A 25-$μ$s/inf Event-driven Graph Neural Network Processor with Spatiotemporal Caching and Spline Convolution for Ultra-low-latency AI at the Edge](https://arxiv.org/abs/2609.15241)

**<font color=#1a73e8>作者：</font>** Adrian Kneip, Martin Lefebvre, Daniel Gehrig 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic-vision-sensor (DVS) cameras generate events on a per-pixel basis with a $\mu$s-level temporal resolution, calling for new algorithm-hardware co-design approaches compared to standard frame-based vision. While event-driven graph neural networks (EV-GNNs) emerge as a promising algorithmic solution, they raise new HW challenges by mixing dense-regular compute operations and sparse-irregular memory accesses. We present ETHEREAL, the first EV-GNN accelerator that scales to 640$\times$480 resolutions, thanks to a neighbor-parallel spline convolution engine and a 2D/3D-split memory hierarchy with a novel region-of-interest spatiotemporal caching mechanism. Measurement results demonstrate end-to-end inference with 25.6$\mu$s latency and 1.7$\mu$J energy per event on state-of-the-art workloads

---


### 326. [Bandits with Probing: Optimal Regret and the Limits of Winner Feedback](https://arxiv.org/abs/2609.15248)

**<font color=#1a73e8>作者：</font>** Yongjie Guan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A learner probes at most $k$ of $n$ arms each round, receives the maximum of their rewards in $[0,1]$, and competes with the best fixed arm. When does the probing advantage pay for learning? We determine two minimax laws. Under independent stochastic rewards with winner feedback (the maximum and a winning label), or on arbitrary fixed sequences given a single signed contrast between block maxima, the minimax regret has order $\Phi_{n,k}(T)=\min\{\frac{n-k}{n}T,\frac{n-k}{k}\}$, $2\le k<n$. Under winner feedback, both arbitrary joint i.i.d. rewards and fixed sequences have minimax regret of order $R_{n,k}(T)=\frac{n-k}{n}\min\{T,\frac{n+T}{k},\sqrt{\frac{nT}{k}}\}$. Both laws have universal constants and anytime upper bounds. The first reduces regret to a pure coverage cost: same-round contrasts absorb the stability cost, and independence permits exact resampling whose gains fund sample advancement. The second adds a learning cost that becomes comparable to coverage at horizon $n$; beyond $nk$, numerical maxima improve over labels alone. The lower bound allows every adaptive action size.

---


### 327. [BioDCASE: Active Learning for Bioacoustics](https://arxiv.org/abs/2609.15255)

**<font color=#1a73e8>作者：</font>** Ben McEwen, Rupa Kurinchi-Vendhan, Shiqi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ecological monitoring increasingly relies on machine learning models, whose performance depends on the quality and quantity of labelled data. However, obtaining these labels is costly, particularly in passive acoustic monitoring, where vast amounts of data are collected but only a small proportion can feasibly be annotated. Active learning addresses this bottleneck by prioritizing which samples should be labelled. However, progress is difficult to measure, because published methods are evaluated under different models, budgets, evaluation metrics and datasets. To address this challenge, we present the 2026 Active Learning for Bioacoustics BioDCASE challenge: a systematic evaluation of sampling methods designed to identify effective AL strategies. Participant methods were evaluated across four subsets composed of terrestrial and marine data. Across ten proposed sampling methods from seven teams, the top-ranked method achieved an area under the learning curve 26.4 % higher than random sampling at the same annotation budget, averaged over four data subsets. Significant variation in performance was observed across subsets, with the top-performing submission achieving a 67.1 % gain for the HSN subset over random sampling and a gain of 8 % for the ATBFL subset. Top-ranking submissions combined multiple acquisition signals, and diversity-based selection outperformed pure uncertainty sampling. Furthermore, there is evidence that transitioning from diversity-based to uncertainty-based selection and explicitly reducing redundancy within acquisition batches improve model training. There is also initial evidence that larger acquisition batch sizes may be increasingly beneficial later in the labelling process.

---


### 328. [Learning CNF Formulas from Uniform Random Solutions: Near-Tight Sample Complexity for Valiant's Algorithm](https://arxiv.org/abs/2609.15268)

**<font color=#1a73e8>作者：</font>** Weiming Feng, Yixiao Yu, Yiyao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We revisit Valiant's algorithm (Commun. ACM'84) for learning $n$-variable CNF formulas with clause size $k$ and variable degree $d$ from i.i.d. uniform random solutions in the local lemma regime. For fixed $t\geq1$, under $k\gtrsim(1+1/t)\log d$, Valiant's algorithm achieves total variation error $\varepsilon$ with $\widetilde{O}(n^{\lceil t \rceil}/\varepsilon)$ sample complexity. For $t>1$, we prove a matching lower bound for Valiant's algorithm. At $t=1$ (covering $0<t<1$), we show Valiant's algorithm has optimal sample complexity up to logarithmic factors by an information-theoretic lower bound $\widetilde\Omega(n/\varepsilon)$.

---


### 329. [Draining Fictitious Knots: Restoring Distance-Awareness Guarantees for High-Dimensional Spline Networks](https://arxiv.org/abs/2609.15274)

**<font color=#1a73e8>作者：</font>** Masoud Ataei, Mohammad Javad Khojasteh, Vikas Dhiman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold Networks (KANs) with spline activations have recently shown promise for interpretable function approximation. Distance-Aware Error for Kolmogorov Networks (DAREK) introduces a computationally efficient bottom-up approach to uncertainty quantification by equipping KANs with distance-aware error bounds; yet, in high-dimensional settings, the theoretical guarantees can be weakened by the emergence of fictitious knots. Inspired by the Kolmogorov-Arnold representation theorem, DAREK adopts a componentwise formulation in which each input dimension is treated separately; as a result, induced knot locations may appear in the combined input space without corresponding to actual training data. These fictitious knots mislead the DAREK uncertainty estimator into reporting low uncertainty far from any real observation, violating the distance-awareness guarantee. We identify this failure mode precisely, characterize its geometric structure, and propose a drainage uncertainty mechanism that restores distance-awareness by constructing a monotonically decreasing uncertainty path from any fictitious knot region toward the nearest real knot. The proposed drainage method provides a practical heuristic correction that mitigates the fictitious-knot failure mode while restoring theoretical distance-awareness in high-dimensional settings. Experiments on a 2D synthetic benchmark and a 100-dimensional face dataset show that drainage raises sampled distance-awareness (SDA) from 85% to 98-99%, matching Gaussian processes at lower computational cost.

---


### 330. [Impute-EM: Native Mixed-State Diffusion Models for Heterogeneous Data Imputation](https://arxiv.org/abs/2609.15284)

**<font color=#1a73e8>作者：</font>** Sergei Kholkin, Kirill Sokolov, Dmitry Baranchuk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Missing values are ubiquitous in heterogeneous data mining, where numerical, categorical, and binary variables often coexist. Many imputation methods, especially diffusion-based ones, treat discrete variables through continuous surrogates such as one-hot relaxations rather than modeling them natively. This creates a mismatch between the model state space and the mixed discrete and continuous structure of the data. We propose Impute-EM, an Expectation Maximization style framework that alternates between imputing missing entries with the current model and refitting a diffusion backbone on completed data. We instantiate Impute-EM with native mixed-state diffusion backbones for heterogeneous data, combining Gaussian and masked categorical components without one-hot relaxations. In exact settings, we characterize the update and show that the observed mask-indexed marginals match the targets at the limit, while making explicit that the full data distribution is generally non-identifiable from incomplete observations alone. Empirically, Impute-EM delivers the best distributional fidelity on mixed-type tabular imputation, on which downstream modeling relies, with text imputation serving as a controlled validation of the native discrete backbone.

---


### 331. [AlignUS: MRI-Guided Ultrasound Representation Learning for ALS Classification from Tongue Images](https://arxiv.org/abs/2609.15285)

**<font color=#1a73e8>作者：</font>** Kadija Abdel Ghader, Emani Babe, Lorenzo Pettinari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Amyotrophic lateral sclerosis (ALS) is a progressive neurodegenerative disease in which early assessment remains challenging, particularly in low-resource settings where MRI is often unavailable. High-resolution ultrasound (HRUS) of the tongue offers a portable and low-cost alternative for evaluating bulbar involvement, but learning reliable diagnostic models is limited by small datasets and the difficulty of extracting robust representations from ultrasound alone. We propose AlignUS, a cross-modal knowledge distillation framework that transfers anatomical knowledge from MRI to a HRUS-based classifier while requiring only HRUS at inference time. The model combines classification loss, supervised contrastive learning, and feature-level distillation to align HRUS representations with MRI embeddings. AlignUS achieves a patient-level balanced accuracy of 0.958, macro-F1 of 0.963, and ROC-AUC of 0.990, aggregated across four patient-level cross-validation folds, with consistent improvements over HRUS baselines and cross-modal alternatives. These results demonstrate that MRI-derived supervision can substantially improve ultrasound-based ALS assessment while preserving low-cost, inference-time independence from MRI.

---


### 332. [ProIQA: A Process-Based Framework for Fine-Grained Math Item Quality Assessment](https://arxiv.org/abs/2609.15292)

**<font color=#1a73e8>作者：</font>** Junkai Tong, Mingjia Li, Haoran Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic Item Generation (AIG) is pivotal for personalized education, yet guaranteeing the pedagogical value of generated items remains a bottleneck. Existing Item Quality Assessment (IQA) methods typically rely on unscalable manual reviews or shallow stem-based metrics, failing to capture the reasoning process required for mathematical problem-solving. To bridge this gap, this paper proposes Process-based Item Quality Assessment (ProIQA), a process-aware framework for fine-grained quality assessment of math items. We first formulate IQA across three heterogeneous dimensions, including knowledge concepts, difficulty, and disciplinary competencies, under a unified process-aware perspective. Based on this formulation, we construct a process-enhanced IQA resource by augmenting original item data with structured reasoning trees derived from raw solutions. Technically, ProIQA leverages Large Language Modelsto construct hierarchical reasoning trees and employs Graph Neural Networks (GNN) to encode their topological dependencies and procedural semantics. The resulting solving representation is fused with stem semantics through a dual-view (``Stem + Solving'') architecture, enabling comprehensive assessment across learning objectives. Extensive experiments on K12 mathematical datasets show that ProIQA effectively captures process-oriented features, offering a scalable data-driven solution for evaluating AIG outputs in intelligent education systems.

---


### 333. [Admissable: Training Reinforcement Learning Agents against Adversarial Missingness](https://arxiv.org/abs/2609.15297)

**<font color=#1a73e8>作者：</font>** Paul Stahlhofen, Luca Hermes, Tim Kochs 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In order to make Reinforcement Learning algorithms applicable in real world scenarios, safety must be ensured even under adverse operating conditions. In this work, we consider the challenge of adversarial feature missingness: a scenario in which an adversary occludes features from the agent's observation in order to reduce performance as much as possible. We formally define adversarial missingness for Reinforcement Learning and compare it to the related concepts of $\ell_\infty$-norm bounded adversarial perturbations and learning with missing data. We develop an adversarial training algorithm and show its effectiveness in increasing robustness against adversarial missingness on three MuJoCo benchmark environments. Compared to a baseline trained with random uniform missingness, our method achieves better robustness on all three tasks.

---


### 334. [When Correlations Mislead: Confounder-Aware Multi-View Urban Region Representation Learning](https://arxiv.org/abs/2609.15305)

**<font color=#1a73e8>作者：</font>** Sean Bin Yang, Ying Sun, Zongyi Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban region representation learning commonly combines heterogeneous data sources, such as mobility flows, points of interest, and land-use information, to support tasks including mobility analysis, public safety forecasting, and service demand estimation. Existing multi-view methods typically improve region embeddings by strengthening interactions across views. However, such methods often overlook view-specific regional structures and may propagate correlations induced by shared latent factors, which can reduce the stability of downstream predictions. To overcome this major limitation, we propose CURE, a confounder-aware framework for multi-view urban region representation learning. CURE first encodes each view with its regional graph structure, estimates a shared latent component, and then reduces its projected influence before cross-view interaction. A hierarchical graph-aware fusion module subsequently aggregates the residual view representations using local and global regional contexts Experiments on three real-world cities show that CURE improves predictive performance, remains robust under missing and noisy input views, and provides reliable cross-view integration through shared component separation and context-dependent view weighting.

---


### 335. [Learning from Reliable Negatives: Confidence-Anchored Test-Time Adaptation for GUI Grounding](https://arxiv.org/abs/2609.15307)

**<font color=#1a73e8>作者：</font>** Yizhou Liu, Fei Tang, Yuchen Yan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) grounding is essential for autonomous agents to map natural language instructions to precise screen coordinates. However, existing supervised fine-tuning and reinforcement learning methods are constrained by the high cost of annotation, creating a scalability bottleneck. In this paper, we introduce a label-free test-time training paradigm driven by two key insights: (1) confidence patterns in coordinate tokens are a better indicator than full-sequence confidence, and (2) in sparse GUI coordinate spaces, negative samples offer more reliable learning signals than potentially noisy positive ones. We first propose Confidence-Anchored Learning (CAL), which utilizes coordinate-token confidence to filter pseudo-labels and assign distance-based binary rewards. Building on this, we develop Confidence-Anchored Negative Learning (CANL), which exclusively optimizes the model using negative samples to bypass the risks of incorrect positive samples. Experimental results demonstrate that CANL-7B achieves 92.1% on ScreenSpot-V2. On more challenging ScreenSpot-Pro, CANL-7B reaches 33.8%, an 8.9% absolute improvement over the base model. Our findings establish coordinate-token confidence as a powerful alternative to manual annotations for scalable GUI agent development.

---


### 336. [Large Universe Subset Predicate Encryption with IND-CCA Security (with Constant-size Ciphertext and Keys)](https://arxiv.org/abs/2609.15312)

**<font color=#1a73e8>作者：</font>** Sayantan Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Katz et al. (CANS'17) introduced Subset Predicate Encryption (SPE).
This scheme is a generalization of broadcast encryption as it emulates the \emph{subset containment} predicate in the encrypted domain.
They proposed two selectively IND-CPA secure SPE constructions in the small universe setting.
They also showed some black-box transformations of SPE to well-known primitives like WIBE and ABE to establish the richness of the SPE structure.
Chatterjee and Mukherjee (RSA'19) proposed two SPE constructions in the large-universe setting.
Their first construction achieved constant-size ciphertexts and secret keys, but it is proven secure in a restricted version of selective security.
Although the second construction achieves adaptive security, the ciphertext size depends on the size of the data-attribute set.
Furthermore, neither of these two constructions achieves CCA security.
In this work, we propose the first large-universe CCA-secure subset predicate encryption with constant-size ciphertext and secret keys.
We prove this construction achieves standard selective security under the standard subgroup decision problems.
Finally, we transform our extremely efficient SPE into the first CCA-secure WIBE, WKD-IBE, etc., with constant-size ciphertexts and secret keys via black-box transformations.

---


### 337. [Evaluation Metrics for Safe Reinforcement Learning](https://arxiv.org/abs/2609.15315)

**<font color=#1a73e8>作者：</font>** Lindsay Spoor, Aske Plaat, Thomas Moerland  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safe reinforcement learning (RL) is commonly formalized as a Constrained Markov Decision Process (CMDP), in which an agent maximizes expected reward while keeping its expected cumulative cost below a specified safety bound. Existing safe RL benchmarks predominantly report whether an algorithm is safe on average, following this expectation-based guarantee. We argue that this convention is insufficient to reliably characterize an algorithm's true safety: it fails to capture how often and how severely the safety bound is violated, whether this holds consistently across tasks and safety bounds, and whether training-time behavior is representative of behavior of the final converged policy. Therefore, we introduce (i) evaluation metrics for safe RL that address each of these concerns and in addition allow for aggregation across tasks and safety bounds. We furthermore define (ii) a safety tier system to systematically categorize and compare algorithms in terms of safety and reliability at both training and for a final policy. Using this framework, we provide (iii) an empirical safety evaluation across multiple safety navigation tasks. Our results show that aggregate metrics, distributional reporting, and task- and safety bound-specific results each reveal information the other metrics cannot. We therefore recommend reporting all three jointly, rather than compressing this information into a single value, as is common practice. We provide SafeRLEval, an open-source evaluation suite to support the reliable characterization of safety in future safe RL research.

---


### 338. [Hypergraph-Regularized Gramian Volumes for Multimodal Retrieval](https://arxiv.org/abs/2609.15320)

**<font color=#1a73e8>作者：</font>** Anindya Nag, Ambuj Mehrish, Sebastiano Vascon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Volume-based multimodal retrieval jointly scores a text query with a candidate's video, audio, and subtitle embeddings. While this approach captures higher-order within-candidate alignment, the score remains candidate-local, and semantically related training samples primarily serve as contrastive negatives. This work introduces Hypergraph-Regularized Gramian Volumes (HyVol), a training-time module that incorporates these semantic relations prior to evaluating the original volume loss. Document hyperedges connect the observed modalities of each candidate, whereas semantic hyperedges link candidates whose detached captions are mutual top-k neighbors. A shallow gated hyper-graph network applies residual corrections to the modality embeddings. Presence masks exclude unavailable streams from message passing, and identity padding preserves the determinant of the observed Gram submatrix without feature imputation. As refinement operates on embeddings rather than scores, the same construction applies to both Gram and HyperGram. We remove the hypergraph after training, leaving the backbone-only architecture, original scoring function, and retrieval cost unchanged. We train both backbones on a 150K-clip subset of VAST-27M and evaluate zero-shot performance on six benchmarks. Under the paired protocol, HyVol improves R@1 across all five retrieval benchmarks, with video-to-text gains reaching +8.3 on MSR-VTT and +7.6 on VATEX. Under missing-modality masking, the V2T margin remains positive in all experimental settings, although the T2V margin becomes slightly negative in four.

---


### 339. [Query-Conditioned Spherical Centroid Aggregation for Multimodal Retrieval](https://arxiv.org/abs/2609.15335)

**<font color=#1a73e8>作者：</font>** Ambuj Mehrish, Anindya Nag, Sebastiano Vascon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal retrieval integrates video, audio, subtitles, and text; however, recent geometric aggregators, such as Gramian volumes, hyperbolic volumes, and spectral objectives, treat all modalities symmetrically. Under a unified evaluation protocol, their joint scores frequently lag behind the strongest single-modality pathway by 1.9 to 27.6 R@1. Controlled analyses attribute this outcome to uniform modality influence. This work introduces Spherical Centroid Aggregation with Learned Adaptive Relevance (SCALAR), a query-conditioned aggregator that assigns relevance-based weights to each available modality before computing a spherical centroid. SCALAR accommodates arbitrary modality subsets and is trained on masked, reduced-arity views using rank-8 LoRA adapters. Across five benchmarks, SCALAR achieves positive aggregation gain on four, reaching +4.0 R@1, while none of the evaluated prior aggregators is positive on more than one. A uniform-weight ablation reproduces the degradation observed with symmetric aggregation. With only 4.8 million trainable parameters, SCALAR attains the highest text-to-video R@1 on three and performs within seed variation of the best result on a fourth. Under test-time modality dropout, SCALAR's representation-stage score surpasses the released GRAM checkpoint at every evaluated masking rate and benchmark by 3.2 to 10.9 R@1. Finally, as modalities are removed, rerankers trained exclusively on complete modality sets increasingly converge toward their video-only pathways, diminishing these representation-level gains and underscoring a limitation of standard two-stage retrieval pipelines.

---


### 340. [Robust Multi-Model Fitting through Learning Neighbor Regions](https://arxiv.org/abs/2609.15348)

**<font color=#1a73e8>作者：</font>** Chang Nie, Guangming Wang, Zhe Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-model fitting involves fitting multiple models accurately in a noisy environment. It is the basis for computer vision tasks such as scene reconstruction and mixed reality. However, its performance is often limited by insufficient feature utilization, inefficient optimization, model overlap, and the non-differentiable pipelines. To overcome these limitations, we introduce a robust coarse-to-fine framework called Learning Neighbor Regions (LNR). Recognizing that substantial computational resources are wasted on numerous bad minimum sets, we propose the coarse-level module. This module utilizes a neural network to extract and analyze geometric feature of both local point-wise relationships and global contextual information in minimum sets, outputting confidence to pre-select a small number of good minimum sets, thereby enhancing overall efficiency before solving hypotheses. To address model overlap, LNR encodes neighbor region features for each hypothesis in its fine-level module. These region features consist of geometric features of neighboring data points, which can be used by multiple regions simultaneously. This design allows the neural network to individually refine and score each hypothesis. Importantly, LNR is trained to learn directly from data point features rather than from the hypothesis parameters, thus avoiding differentiating the sampling process and the model solvers. Extensive experiments on four classic multi-model fitting tasks demonstrate that LNR achieves state-of-the-art performance. The analysis suggests that LNR can be easily adapted to various robust multi-model fitting tasks.

---


### 341. [End-to-End Cell Detection via Instance-aware Graph Modeling](https://arxiv.org/abs/2609.15354)

**<font color=#1a73e8>作者：</font>** Ruochen Liu, Yalin Zheng, Jingxin Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate cell detection and classification are crucial for pathological analysis, directly affecting diagnostic accuracy and treatment planning. To capture complex cellular interactions beyond visual appearance within the tumor microenvironment, several approaches have employed graph neural networks to model spatial and relational patterns among cell nuclei, yielding promising results. However, these methods typically adopt a two-stage paradigm of visual extraction followed by relational modeling, which necessitates separate tuning for each stage, thereby increasing pipeline complexity and hindering end-to-end joint optimization. In this paper, we propose an end-to-end framework for cell detection and classification that jointly models patch-level visual representations and instance-level interactions, which incorporates a dynamic graph construction module and an instance-aware graph network. Specifically, the graph construction module dynamically builds the graph structure using learnable queries derived from patch-level features as cell instance representations, with adjacency defined by integrating feature similarity and spatial distances. The instance-aware graph network performs adaptive instance filtering and feature reorganization, aggregating them over the cell graph into a topological latent state for a selective state-space transition driven by visual cues, fusing appearance and relational evidence. When evaluated on multiple datasets with different staining protocols for cell and nucleus detection, our method significantly outperforms existing approaches in both detection and classification performance. The code will be released at this https URL.

---


### 342. [Diffusion Trajectory Modeling for Semantic Correspondence](https://arxiv.org/abs/2609.15357)

**<font color=#1a73e8>作者：</font>** Yusung Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models generate images through an iterative diffusion process, and recent studies have demonstrated that the intermediate feature maps produced during this process contain rich visual representations, leading to their adoption across a variety of downstream tasks. However, most existing approaches are limited to either using a single feature map at a specific timestep or aggregating feature maps across multiple timesteps. We observe that intermediate representations in the diffusion process form meaningful trajectories along the time axis. In particular, the representation of each spatial patch evolves progressively throughout the generative process, encoding semantics that are difficult to capture from static snapshots alone. This observation motivates the need to treat diffusion representations as temporally structured trajectories rather than static snapshots. To this end, we propose Diffusion Trajectory Modeling (DTM), a framework that interprets the temporal evolution of each spatial patch as a trajectory and leverages it for semantic correspondence. By effectively modeling patch-wise trajectories generated across multiple timesteps, DTM captures correspondence cues that prior methods are not designed to capture. We further demonstrate empirically that spatially corresponding patches form similar trajectory patterns throughout the diffusion process, suggesting that the temporal axis of diffusion carries semantic information. Experiments on SPair-71k, SPair-U and AP-10K show that DTM achieves strong performance, presenting a new perspective for exploiting diffusion representations from a trajectory-centric viewpoint.

---


### 343. [Robust and Efficient Communication for Multi-Agent Learning](https://arxiv.org/abs/2609.15361)

**<font color=#1a73e8>作者：</font>** Rafael Pina, Varuna De Silva, Corentin Artaud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective communication is a cornerstone of distributed intelligence in Multi-Agent Reinforcement Learning (MARL), yet ensuring that generated messages are both informative and robust to physical constraints remains a significant challenge. This paper introduces Multi-Agent Regularized Communication (MARC), a novel framework inspired by information-theoretic principles of conditional mutual information. MARC employs an attention-based architecture coupled with a unique message regularization mechanism designed to minimize uncertainty regarding future system states, thereby inducing the learning of highly representative communication protocols. Crucially, we evaluate MARC under stringent communication bottlenecks and lossy channels, simulating the real-world constraints of autonomous robotic networks and decentralized systems. Our results demonstrate that MARC significantly outperforms state-of-the-art methods in complex cooperative domains. Furthermore, we provide a deep analysis of message characteristics, proving that MARC maintains high operational performance even under significant data compression, offering a scalable path for deploying intelligent agents in resource-constrained environments.

---


### 344. [CapsuleMotion: A Lightweight Real-Time Visual Motion Predictor for Capsule Endoscopy](https://arxiv.org/abs/2609.15367)

**<font color=#1a73e8>作者：</font>** Oliver Bause, Julia Werner, Oliver Bringmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Capsule Endoscopy (VCE) is a non-invasive medical examination that allows for the observation of the small intestine, which is otherwise difficult to access. A fundamental challenge persists in the form of their limited size in order to still be swallowable. The resulting restricted battery capacity, however, contradicts with the power-intensive nature of image capture and transmission. Therefore, we propose CapsuleMotion, a patient-specific dynamic capsule behavior that utilizes the available energy in a goal-oriented manner to increase the likelihood of a complete screening of the gastrointestinal tract. By investigating and combining metrics from the on-device image compression, CapsuleMotion predicts the motion between two successive frames. The camera's frame rate will be modified in accordance with the predicted magnitude of motion. Furthermore, prior to entering the small intestine, the capsule operates in a low power mode with a significantly reduced frame rate. In this mode, the LocalizationNet is employed to determine the current organ, provided that motion was predicted. The proposed framework is evaluated on the Rhode Island VCE dataset and deployed on an ultra-low power single-core RISC-V demonstrator with an integrated hardware accelerator. CapsuleMotion demonstrated the capability to reduce electric energy consumption by up to 20.66% in comparison with conventional capsules that lack a dynamic frame rate. Additionally, the accuracy of detecting the entry point of the small intestine has been improved.

---


### 345. [Representing Clinical Conditions on Vital Signs from Healthy Individuals using Latent Modeling](https://arxiv.org/abs/2609.15379)

**<font color=#1a73e8>作者：</font>** Rafael Pina, Varuna De Silva, Mindula Illeperuma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning can be crucial to help scale complex signal processing applications in scenarios such as healthcare. However, these machine learning models need rich datasets to be trained and there are often cases where it is not possible to access representative datasets. In this paper, we propose a deep generative model based on conditional variational autoencoders with the objective of augmenting the vital signs of healthy individuals in a way that mimics the patterns of a certain clinical condition. More specifically, we use a publicly available ICU (Intensive Care Unit) dataset to train our model and then evaluate it using the vital data that we have collected from healthy individuals. Our results demonstrate that the proposed model can not only learn the underlying dynamics of the ICU data but, more importantly, can reshape our collected data from healthy individuals in a way that is aligned with the vital signs of a certain clinical condition. We propose a distance metric that shows how our model can generate samples that are more aligned with the intended clinical labels when compared to the tested baselines.

---


### 346. [When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent-Tool Boundary](https://arxiv.org/abs/2609.15397)

**<font color=#1a73e8>作者：</font>** Artem Trofimov, Boris Novikov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly execute long-running workflows that externalize effects through independently supplied tools. Under retries, speculative execution, concurrency, and partial failures, the resulting external state may be inconsistent with the workflow's intended resolution: required effects may be missing or duplicated, aborted effects may survive, and committed effects may depend on provisional state that is later withdrawn. Advanced transaction models address related failures, but assume that lower-level operations expose the semantics they depend on: whether an effect occurred, whether it can be compensated, staged, or safely reordered. Shared agent-tool interfaces usually do not.
We contribute an effect-history model that separates events in the external world from the runtime's observations of them, and a catalog of eight recurring external-effect anomalies. From the catalog we derive the boundary capabilities required to exclude each anomaly in general, and four points where black-box tool invocation alone cannot provide a general guarantee. We then ask how much of this is expressible in a widely used shared tool interface, measuring the use of the standard annotation vocabulary across 98,291 tools exposed by registered Model Context Protocol (MCP) servers. The fields are widely emitted but provide only coarse call-level hints, and none of the required capabilities is fully expressible. These results motivate reusable transactional contracts at the tool boundary.

---


### 347. [BSC-Net: A Small-Branch-Sensitive Structural Continuity Network for Coronary Vessel Segmentation and Quantitative Angiographic Analysis](https://arxiv.org/abs/2609.15400)

**<font color=#1a73e8>作者：</font>** Wanxian Li, Jiaqian Qin, Qingyi Xian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vessel segmentation in X-ray coronary angiography (XCA) is a fundamental step for quantitative coronary analysis and subsequent assessment of coronary artery disease. However, accurate vessel segmentation remains challenging because of imaging noise, complex bifurcations, and the overlap of vessels and background structures, which can lead to disrupted vascular connectivity and missed small branches. In this work, we propose BSC-Net, a ResNet-U-Net-based framework tailored to improve small-vessel representation and repair vascular structural continuity. BSC-Net enhances small-vessel representation through targeted sampling and improves vascular structural continuity by integrating long-range contextual modeling and Edge-Informed Loss (EIL). BSC-Net was validated on two public XCA datasets, demonstrating state-of-the-art (SOTA) performance in coronary vessel segmentation with Dice and IoU scores of 77.8%/90.6% and 64.5%/83.0%, respectively. Furthermore, based on the obtained vessel segmentation, we performed automated quantitative coronary analysis and derived clinically relevant morphological and hemodynamic parameters, including stenosis ratio, time-to-peak, and relative propagation velocity. These results demonstrate that BSC-Net produces accurate vessel segmentation results with preserved vascular continuity for quantitative coronary assessment, enabling reliable downstream analysis and clinical evaluation of coronary artery disease.

---


### 348. [Can AI systems have free will?](https://arxiv.org/abs/2609.15407)

**<font color=#1a73e8>作者：</font>** Christian List  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While there has been much discussion of whether AI systems could function as moral agents or acquire sentience, there has been very little discussion of whether AI systems could have free will. I sketch a framework for thinking about this question, inspired by Daniel Dennett's work. I argue that, to determine whether an AI system has free will, we should not look for some mysterious property, expect its underlying algorithms to be indeterministic, or ask whether the system is unpredictable. Rather, we should simply ask whether we have good explanatory reasons to view the system as an intentional agent, with the capacity for choice between alternative possibilities and control over the resulting actions. If the answer is "yes", then the system counts as having free will in a pragmatic and diagnostically useful sense.

---


### 349. [ViCo-SAM3: Vision-Conditioned Alignment for Open-Vocabulary Camouflaged Object Segmentation](https://arxiv.org/abs/2609.15418)

**<font color=#1a73e8>作者：</font>** Qiangqiang Zhou, Wenjun Tang, Yong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary camouflaged object segmentation (OVCOS) aims to segment unseen camouflaged objects under text guidance. We observe that SAM3 still suffers from a pronounced semantic gap between global textual semantics and fine-grained pixel-level visual cues in OVCOS. Meanwhile, fully fine-tuning the text encoder introduces heavy parameter overhead and risks overfitting to training categories, which compromises open-vocabulary representation flexibility. To address these issues, we propose ViCo-SAM3, a Vision-Conditioned alignment framework designed for OVCOS. Specifically, we introduce vision-conditioned (ViCo) module, which dynamically modulates text embeddings with global visual context, enabling textual representations to adapt to the current image content and thereby effectively bridging the semantic gap between vision and text. Building on this, we further design a vision-conditioned cross-modal binding (ViCoBind) module to enhance cross-modal interaction and semantic alignment between visual and textual representations. Without bells and whistles, ViCo-SAM3 achieves state-of-the-art performance on the OVCamo benchmark and demonstrates strong generalization.

---


### 350. [An Empirical Security Analysis of Open-Source Software Used in Onboard Satellite Systems](https://arxiv.org/abs/2609.15425)

**<font color=#1a73e8>作者：</font>** Roee Idan, Tomer Cohen Galor, Asaf Shabtai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The use of open-source software (OSS) in satellite flight systems is increasing as missions adopt reusable frameworks, shared libraries, and community-maintained components. While this accelerates development, it also introduces software-security risks into systems where patching is costly and failures may affect mission operations. This paper presents an empirical security study of OSS used in onboard satellite systems. We analyze 126 public repositories using a pipeline that combines software bill of materials generation, software composition analysis, static application security testing, infrastructure-as-code analysis, and secret scanning. After rule-based cleaning, onboard-scope filtering, and fingerprint-based deduplication, the pipeline produced a final dataset of 2,827 findings.
The results show that security findings are widespread but unevenly distributed. Medium-severity findings account for 49% of the dataset, and 72% are classified as medium severity or higher. A Common Weakness Enumeration (CWE)-based taxonomy assigns all findings to eight weakness families. Memory Safety and Code Quality dominate the dataset, followed by Input Validation and Injection. Most findings occur in project-developed code, accounting for 81.4% of the dataset, while external dependency code remains a relevant source of findings. While these findings do not establish mission-specific exploitability, they provide an empirical characterization of recurring security patterns across the open-source onboard satellite software ecosystem, helping quantify their prevalence and prioritize areas that warrant the greatest security attention.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-416](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
