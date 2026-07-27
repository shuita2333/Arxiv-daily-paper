# 📦 其他研究 | 2026年07月28日

> 本类共 **169** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-169**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-169**

---

### 151. [Local-Global Geometric Insights for Graph Neural Networks via Entropic Curvature](https://arxiv.org/abs/2607.22381)

**<font color=#1a73e8>作者：</font>** Rachid Caich, Yassine Abbahaddou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Curvature notions on graphs, particularly Ollivier-Ricci and Forman, have emerged as powerful tools for addressing fundamental issues in Graph Neural Networks (GNNs) such as oversmoothing and oversquashing, but rely almost exclusively on local edge-level comparisons and therefore fail to certify how information actually propagates over long distances. We introduce Entropic Curvature, a global, transport-based curvature obtained by extending the Lott-Sturm-Villani framework to graphs through the displacement convexity of entropy along Wasserstein geodesics. We define a tractable Weak Entropic Curvature proxy that lower-bounds the global entropic curvature, and from it derive (i) a Poincare-type inequality controlling oversmoothing, (ii) a transport-entropy generalization bound, and (iii) an expansion paradox proving that sparsity, strong spectral expansion, and positive entropic curvature cannot coexist in large graphs, unifying oversmoothing and oversquashing as opposite ends of a single curvature spectrum. We translate the theory into three practical mechanisms, the E-Gate aggregator, the ENT structural encoding, and Midpoint-Completion Rewiring (MCR), and benchmark them against SDRF, FoSR, BORF, LCP, and Graph Ricci Flow on six node-classification benchmarks, and graph-classification.

---


### 152. [Correlation-Aware and Gaussianity-Preserving Robust Latent Angular Watermarking for Diffusion Models](https://arxiv.org/abs/2607.22386)

**<font color=#1a73e8>作者：</font>** Yebin Zheng, Haonan An, Guang Hua 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent domain watermarking for diffusion models embeds watermarks directly into the latent prior, enjoying non-intrusiveness to model parameters and seamless integration with the generation process. However, due to the violation of latent Gaussianity or sensitivity to normal and malicious perturbations during latent inversion, existing methods are prone to watermark detection or removal attacks. A further overlooked problem is the violation of the i.i.d. latent condition after watermarking, which leads to latent correlation degradation and generation fidelity loss. Although this has been externally measured by FID, the internal correlation structure has yet to be rigorously characterized. To address the above issues, and motivated by the rotation-invariant property of isotropic Gaussian, we propose \textit{Latent Angular Watermarking (LAW)}, which encodes watermark bits as antipodal angles ($\pm\pi/2$ relative to a reference pair) between disjoint pairs of latent elements while preserving the Gaussianity. The antipodal ($\pi$-separation) encoding maximizes geometric separation between bit values, and we prove that the decoding angular-error variance is proportional to the norm of the latent pair, i.e., $\operatorname{var}(\Delta\phi) \propto 1/\rho^2$. We further propose a magnitude-driven variant, LAW-M, which anchors watermark bits in the most geometrically stable latent dimensions, yielding additional robustness gains. Theoretically, we provide a rigorous characterization of the induced correlation degradation, deriving in closed form the autocorrelation structure of the watermarked latent and proving that correlations are confined to a sparse, structured set of off-diagonal elements with fixed $\pm\pi/4$ values.

---


### 153. [SceneActBench: Can Agents Act on the 3D Scenes They See?](https://arxiv.org/abs/2607.22393)

**<font color=#1a73e8>作者：</font>** Yifei Zhao, Xiangxin Zhou, Wenhao Yang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language model (VLM) agents increasingly use tools to act on 3D scenes rather than only describe them. Existing 3D benchmarks score textual responses or single-object operations, leaving agent action on complete multi-object 3D scenes under evaluated. We present SceneActBench, a benchmark for visually conditioned action across five 3D tasks under a unified agent-environment loop. Given PNG images or sampled video frames and, where applicable, supplied 3D assets, an agent acts on a 3D environment. We evaluate each final output against hidden ground truth with task-specific geometric metrics. SceneActBench comprises five tasks built from 210 source instances, yielding 520 task cases including paired input conditions. Every task runs through one fixed agent loop to keep the comparison fair. Across eleven proprietary VLM configurations, Overall scores span 38.6-50.2, and none performs consistently well across tasks. We further analyse where and how failures manifest.

---


### 154. [Unboxing Diffusion Models for the Arts: Interactive Model Bending and Practice-Based Explainability](https://arxiv.org/abs/2607.22428)

**<font color=#1a73e8>作者：</font>** Ahmed M. Abuzuraiq, Philippe Pasquier  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) in creative practice can be less about technocentric explanation and more about enabling artists to inspect modify and debug models as part of making Yet largescale texttoimage diffusion systems are typically presented as opaque endtoend tools limiting this kind of material engagement We argue that even large models can function as creative materials when their internal structure is made visible and manipulable To support this we propose a handson approach to explainability centred on experimentation and intervention We instantiate this approach with a model bending and an interactive (inspection) interface integrated into ComfyUIs nodebased workflow including interactive layer selection and intervention controls Through qualitative and quantitative analysis of bending interventions in Stable Diffusion 15 we show how manipulating specific components of a diffusion pipeline produces relatively consistent families of visual effects allowing artists to build practical layerlevel intuition about how different parts of the model shape generated images

---


### 155. [Hyperball May Not Be a Free Lunch](https://arxiv.org/abs/2607.22444)

**<font color=#1a73e8>作者：</font>** Yihao Xiao, Jialong Sun, Zitian Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For scale-invariant deep networks, Hyperball-style optimizers have shown strong performance in large-scale training by fixing the norms of matrix-valued parameters and normalizing updates. However, the source of their advantage remains unclear. Starting from the angular displacement between consecutive parameter states, we derive an angular effective learning rate that accounts for the parameter-update angle, parameter norm, and update norm. We also show that the conventional norm-based measure is a special case under parameter-update orthogonality. We then decompose optimizer updates into radial and tangential components and analyze how radial updates affect one-step angular displacement. Under the training configurations considered, numerical results show that the radial component has only a limited direct effect on the angular effective learning rate. It therefore cannot explain why MuonH converges more slowly than MuonWD early in training but overtakes it later. To further isolate the underlying mechanism, we devise a heuristic experiment that modifies only the learning-rate schedule so that the dynamics of each optimizer reproduce those of the other. The results suggest that their main difference stems from the evolution of the effective step size rather than an intrinsically superior update direction induced by Hyperball. Our pretraining experiments further show that more aggressive learning-rate decay can accelerate MuonH early in training but may impair its later performance. Thus, maintaining a constant angular velocity does not eliminate the learning-rate-scheduling problem; careful scheduling remains essential to realizing the potential of Hyperball-style optimizers. Our code is publicly available at this https URL.

---


### 156. [Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture](https://arxiv.org/abs/2607.22445)

**<font color=#1a73e8>作者：</font>** Halil Burak Noyan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise AI agents are typically granted static credential sets at configuration time, holding every tool the role might need for every task they perform. This persistent over-privilege expands the attack surface. We argue that capability scoping must follow a dynamic least-privilege principle and be treated as a prevention mechanism before a detection one. A credential that does not exist in an agent's context cannot be misused regardless of the agent's reasoning or evasion sophistication. We outline a three-source architecture instantiating this principle: role-based ceilings, a task-context classifier, and policy-derived combination prohibitions creating a layered proactive defense against LLM agent misalignment and misuse cases. The architecture supports both enforcing and observe-only deployment; the latter records agent permission requests inconsistent with task context, producing a behavioral signal usable in misalignment research.
As a first step toward evaluating this architecture, we contribute a synthetic dataset of 600 enterprise task prompts grounded in a multi-department company policy, labeled with minimum required permissions across a 15-permission tool-based taxonomy that maps directly to deployable credentials or enforceable guardrails. The dataset is constructed via a two-pass pipeline that separates prompt generation from permission labeling to avoid circularity, and is validated against a 60-record/688 decisions human-reviewed sample (Cohen's $\kappa = 0.917$ pre-review and $\kappa = 0.967$ post-review). Iterating between dataset and policy reduced ceiling violations from 46 to 3, a 93% reduction. This shows that synthetic prompt generation can drive policy refinement when the two are developed together. The dataset, environment specification, and generation pipeline are released to support evaluation of dynamic scoping mechanisms.

---


### 157. [Deformable Triangle Splatting: Flexible Primitives for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2607.22446)

**<font color=#1a73e8>作者：</font>** Oriol Jiménez-Ayguadé, Antonio Agudo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent radiance field methods represent scenes with 2D primitives that offer surface alignment and efficient rasterization, from Gaussian disks to triangles, yet all rely on convex boundaries: curved and concave structures demand excessive primitives. We introduce Deformable Triangle Splatting, which augments each triangle with $K$ control points per edge, each parameterized by a single learnable scalar displacement that shifts the boundary inward or outward, enabling non-convex shape representation while preserving the three base vertices that define the 3D plane. To render these non-convex primitives differentiably, we design a rasterization pipeline in the triangle's barycentric coordinate space, ensuring view-consistent rendering. A winding number test determines whether each pixel lies inside the deformed primitive, and a window function controlled by two learnable parameters, sharpness and corner smoothness, together with a per-primitive scalar opacity, produces the smooth opacity transition from interior to boundary. Validation is done in a variety of real-world scenes, outperforming recent works based on non-volumetric primitives in terms of visual quality and versatility while still achieving competitive rendering efficiency.

---


### 158. [A Maximum Entropy Implementation of Differential Privacy Under Linear Invariants](https://arxiv.org/abs/2607.22450)

**<font color=#1a73e8>作者：</font>** Ryan Lafferty, Anindya Roy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differential privacy is the standard for ensuring data privacy and is widely used in major data publications, including reporting results from the U.S. decennial census. Common implementation of differential privacy uses independent Gaussian or Laplace noise addition to the database. However, there could be aggregate (linear) queries to the database that are excluded from the privacy budget, for example, state totals that can not be perturbed due to constitutional mandates. Any implementation of a differential privacy is required to honor these constraints, also referred to as invariants. Under aggregation constraints, the noise vector is no longer independent and the traditional differential privacy guarantees have to be re-evaluated. We propose a high entropy differential privacy implementation that maintains the aggregation invariants with probability one or exponentially close to one and derive the privacy guarantees for the implementation under the invariants. The theoretical proof covers a partial solution to an open question about the null space of correlation matrices. Moreover, the methodology has general use in the context of sampling from normal mixture models under linear equality constraints.

---


### 159. [grapheme-kit: Grapheme-Level Metrics and Text Processing for Multilingual NLP](https://arxiv.org/abs/2607.22456)

**<font color=#1a73e8>作者：</font>** Izzath Nisfer, Ashini Kavindya, Ovindu Atukorala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing lexical distance, similarity, and evaluation metrics operate on Unicode code points, which can misrepresent errors in writing systems where a single grapheme is represented by multiple Unicode code points. We introduce grapheme-kit, an open-source Python library that extends these metrics to operate on grapheme clusters instead. The library also provides improved grapheme processing for Tamil and Sinhala, including accurate grapheme cluster identification and grapheme composition/decomposition utilities. Through an OCR case study, we demonstrate that grapheme-level metrics provide a more faithful evaluation of complex scripts.

---


### 160. [Complexity Bounds and Approaches to Learning Projected Gradient Descent Solver Iterates](https://arxiv.org/abs/2607.22467)

**<font color=#1a73e8>作者：</font>** Anjian Li, Ryne Beeson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data scarcity poses a fundamental challenge in training generative models to produce initial guesses for parametric optimization problems that are otherwise numerically expensive to solve. We therefore study a $k$-neighborhood data collection strategy that augments datasets of converged solutions with intermediate solver iterates, increasing the amount of training data without additional solver runs. To understand the benefits of this approach, we derive a generalization bound based on Rademacher complexity that reveals the role of the $k$-neighborhoods and related parameters. To achieve this result, we focus on one-sided box-constrained quadratic programs solved by projected gradient descent. We illustrate the behavior of this solver on two examples. The approach proposed in this paper enables a more capable DDDAS paradigm by improving the efficiency of the data-model-optimization loop. We finish by discussing two views of learning solver-iterate data and connect our analysis with GLENS, a new data-efficient global search method.

---


### 161. [Beyond Negative-Ridge Endpoints: Mixed-Sign Spectral Regularization via Negative-Shifted Gradient Descent](https://arxiv.org/abs/2607.22474)

**<font color=#1a73e8>作者：</font>** Peng Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In overparameterized linear regression, many weak spectral directions act like a ridge penalty on the signal-bearing spectrum; negative ridge is the natural correction, pushing filters above one. The stable negative-ridge endpoint, however, is structurally limited: its pole must stay below the smallest nonzero empirical eigenvalue, and it anti-shrinks smaller eigenvalues more than larger ones. Early-stopped negative-shifted gradient descent escapes this constraint. Its filter is smooth at the would-be pole and mixed-sign-capable: above-ridgeless directions form a leading prefix, with lower directions shrunk or exposure-controlled while stopping sets the crossover. In a Gaussian spike-plus-flat model we discover a Marchenko-Pastur barrier: the shift that cancels the implicit penalty lies a bulk width above the smallest empirical eigenvalue, and the stopped path improves on every admissible endpoint by a polynomial factor in risk under explicit conditions. Our main theorem permits a general high-effective-rank tail: its trace sets the implicit floor, its squared spectrum controls exposure, and the floor-critical path recovers all head scales at once, beyond positive shrinkage and, once scales separate, every uniform rescaling of ridgeless. Handling the noncontractive shifted dynamics is the central technical challenge; localized Duhamel integrals control them. A finite-grid hold-out inequality transfers the separations to the validation-selected algorithm.

---


### 162. [\k{appa}-LoRA: Condition Numbers Reveal Which LoRA Matrices Worth Updating](https://arxiv.org/abs/2607.22489)

**<font color=#1a73e8>作者：</font>** Jianghui Wang, Silong Yong, Francesco Orabona 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) has become a widely adopted technique for efficient neural network fine-tuning, decomposing model updates into low-rank matrices. However, LoRA remains computationally costly because it updates all matrices uniformly, regardless of their actual contribution to adaptation. This cost is especially prohibitive for large-scale models with billions of parameters and for resource-constrained settings such as edge deployment and on-device fine-tuning. We show for the first time that not all LoRA matrices are equally worth tuning: matrices with smaller condition numbers (the ratio of largest to smallest singular value) are already well-balanced across directions and contribute only marginally to adaptation, whereas matrices with larger condition numbers contain underdeveloped directions that span richer subspaces and drive most of the performance gains. This observation itself is a key contribution of our work, and it motivates a more selective approach to fine-tuning. Building on this insight, we propose \k{appa}-LoRA, a method that optimizes LoRA by focusing updates on the matrices with the largest condition numbers, which capture the most informative directions of change. By restricting LoRA updates to the top 50% of weight matrices ranked by condition number, \k{appa}-LoRA halves the trainable parameter count and correspondingly reduces compute and memory cost. Extensive experiments across multiple benchmarks show that this design cuts fine-tuning time by 16.2% on average while matching the accuracy of standard LoRA and reducing memory cost by 4.5%. Further analysis reveals that the condition numbers of the selected matrices consistently decrease over training, suggesting that \k{appa}-LoRA's effectiveness stems from targeted spectral rebalancing rather than parameter selection alone.

---


### 163. [Susceptible Reservoir Architectures for Regime-Conditional Volatility Forecasting](https://arxiv.org/abs/2607.22491)

**<font color=#1a73e8>作者：</font>** Aliaksei Kaliutau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Volatility forecasting is dominated by persistence and measurement noise, leaving limited residual structure for nonlinear models to exploit. We introduce Susceptible Architectures (SUSA), a reservoir-design principle for volatility forecasting, and its two concrete implementations, based on complex-valued open-chain and periodic reservoirs and regime-conditioned experts to interpret reservoir features across calm, onset, recovery, and persistent-stress states. We also implement open-system $q$-qubit counterparts in Qiskit while retaining a common AR-Ridge anchor and a bounded residual correction trained under QLIKE. We evaluate models on 16 U.S. equity and exchange-traded-fund series using three disjoint chronological training, validation, and test folds, a 12-observation input window, and a five-observation forecast horizon. The proposed models perform competitively with GARCH, achieving statistically significant QLIKE improvements for specific assets (IWM, XLP). Also models' forecasts complement HARQ-style predictions: a stacked ensemble improves mean QLIKE by 0.0116 over its strongest constituent and wins in 75% of test scenarios.

---


### 164. [Interpretable EEG biomarkers with bag-of-waves: Spatial and temporal waveform dictionaries for low-data regimes](https://arxiv.org/abs/2607.22508)

**<font color=#1a73e8>作者：</font>** Athanasios Papastathopoulos-Katsaros, Steven T. Lee, Lin Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is widely used to diagnose neurological conditions, but its analysis usually relies on either predefined spectral features or deep neural networks. Predefined features carry a strong bias, since they fix in advance what counts as informative, while deep neural networks and foundation models are hard to interpret and need large amounts of data and compute. We present bag-of-waves, an interpretable framework that learns a small dictionary of recurring EEG waveform templates, called atoms, using shift-invariant k-means without labels. The continuous EEG is then turned into a sequence of atom tokens, whose counts feed a simple downstream classifier or clustering step. We extend this representation in two ways: we add atom-to-atom transitions, which we call n- grams, to capture temporal structure, and we move from single-channel atoms to regional and cross-channel spatial atoms for the multichannel case. We test the method on three complementary datasets, each probing a different aspect: single-channel mouse genotype clustering with only sixteen animals (the low-data and temporal case), resting-state dementia classification (the spatial case), and the TUEV benchmark, a six-way classification of clinical EEG events (a high-data comparison against strong deep and foundation baselines). Across all three datasets, bag-of-waves achieves performance competitive with state-of-the-art deep and foundation models. Yet, it operates with a fraction of the parameter count and provides full interpretability: because every atom corresponds to an inspectable waveform, the method explicitly recovers known clinical morphologies that a neurophysiologist can directly validate. Its main advantage is that it works in the low-data regime where heavier models are a poor fit.

---


### 165. [Dysphagia Risk Stratification in Head and Neck Cancer via Two-Stage PRO-Clinical Stacking](https://arxiv.org/abs/2607.22514)

**<font color=#1a73e8>作者：</font>** Siyuan Zhao, Eric Ababio Anyimadu, Zachary G. Brumm 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dysphagia is a debilitating late effect of head and neck cancer (HNC) treatment, yet timely identification of at-risk patients remains challenging in survivorship care. Definitive assessment relies on videofluoroscopic imaging, as captured by the Dynamic Imaging Grade of Swallowing Toxicity (CTCAE-DIGEST), which, while validated, requires specialized equipment, trained personnel, and significant patient burden, limiting its routine use in surveillance. Patient-reported outcomes (PROs), by contrast, are low-cost, scalable, and easily collected at any clinical encounter, making them an attractive alternative signal for identifying patients who may warrant further evaluation. However, a clear clinical framework for translating PRO responses into actionable interventions is still evolving. In particular, uncertainty remains regarding when a patient's self-reported symptom burden should prompt escalation of care.
This study addresses this gap by formulating a single-visit PRO-clinical prediction framework and introducing a clinically interpretable two-stage stacking model to predict swallowing impairment risk using PRO responses and structured clinical variables, without requiring videofluoroscopic imaging. The proposed framework quantifies the independent contributions of patient-reported symptoms and clinical factors within a unified and interpretable risk assessment model. Our findings demonstrate that individual MDADI responses contain predictive information beyond that captured by composite or global summary scores, while interpretability analyses reveal symptom patterns and clinical risk factors associated with swallowing impairment. Together, these results support the use of structured PRO-clinical integration as a practical, imaging-free approach for dysphagia risk stratification in HNC survivorship.

---


### 166. [Gridnberg: A Topography-Aware Pedestrian Routing Dataset for New York City](https://arxiv.org/abs/2607.22523)

**<font color=#1a73e8>作者：</font>** Ariel Noyman  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cities are rarely flat, yet urban network analysis usually represents streets as planar graphs. This simplification affects modeled impedance, route choice, and the interpretation of accessibility, particularly where alternative paths differ in grade. This paper introduces Gridnberg ('grid-n-berg', grid and mountain), a topography-aware pedestrian routing dataset for New York City. The dataset enriches the NYCWalks network with vertex-level elevations derived from the New York City Planimetric Database. For each pedestrian-network geometry vertex, the workflow averages selected elevation observations within a 50 m radius, retains segments with complete vertex support, and uses direction-specific cumulative ascent and descent to calculate three routing costs: horizontal distance, a comfort-oriented slope score, and an accessibility-sensitive slope score. The release retains 313184 of 315577 source segments (99.24%). Gridnberg supports reproducible terrain-aware analysis, transparent scenario comparison, and improved pedestrian-network representations in New York and other cities.

---


### 167. [Explainable Reinforcement Learning for assisting Air Traffic Controllers](https://arxiv.org/abs/2607.22525)

**<font color=#1a73e8>作者：</font>** Anduel Mehmeti, Gabriella Gigante, Salvatore Venticinque  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To effectively integrate AI into high-stakes, critical environments such as healthcare, autonomous driving, and aviation--and to advance toward higher levels of automation and seamless human-AI collaboration--building trust in AI-driven solutions is essential. Trust, in turn, is closely linked to the explainability of AI systems. The rapid advancements in AI across various domains have underscored the challenges of establishing trust, raising increasing interest in AI explainability even more when applied to deep learning. In this context, the present work aims to explore the application of explainability techniques to Reinforcement Learning (RL) algorithms, specifically within the safety-critical domain of Air Traffic Control (ATC). Using a simplified ATC environment as an initial testbed, an intelligent agent is trained with a reinforcement learning algorithm to make decisions on alternative flight routes that avoid no-fly zones. As a preliminary explainability approach, a saliency map is employed, providing insights into the input features that most significantly influence the agent's decision-making process.

---


### 168. [Twins: Learn to Predict Unified Representations with Focal Loss](https://arxiv.org/abs/2607.22531)

**<font color=#1a73e8>作者：</font>** Kaixiong Gong, Xin Cai, Bin Lin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models seek a shared visual token space that supports both multimodal understanding and image generation. Discrete methods unify the interface via a shared codebook, whereas continuous pipelines often rely on two disparate representations -- semantic features (e.g., ViT) for understanding and low-level latents (e.g., VAE) for synthesis -- resulting in mismatched latent spaces. We propose Twins, a unified continuous token space formed by channel-wise concatenating ViT and VAE features on the same token grid, so the sequence length is unchanged and attention cost does not increase. However, jointly modeling Twins in a Diffusion Transformer exposes a severe optimization imbalance: the model fits the ViT component well but struggles to match the VAE latent distribution. We trace this imbalance to three sources of heterogeneity: frequency bias, intrinsic dimensionality, and condition-aligned vs condition-independent uncertainty. To address it, we adapt a focal regression objective for flow matching that upweights large-error VAE dimensions, better balancing optimization across the ViT and VAE components. On ImageNet, this yields up to 10.57 gFID gain over naive MSE loss without classifier-free guidance. Twins also performs competitively on multimodal understanding benchmarks and improves reconstruction fidelity, narrowing the gap between understanding- and generation-oriented representations.

---


### 169. [SM4RT: Learning Structured Motion Geometry for 4D Reconstruction](https://arxiv.org/abs/2607.22534)

**<font color=#1a73e8>作者：</font>** Shing Ho J. Lin, Wenzhao Zheng, Dong Zhuo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometry Foundation Models (GFMs) have substantially advanced monocular 3D reconstruction, yet extending this capability to 4D dynamic understanding remains a fundamental challenge. Most existing motion perception methods (e.g., sparse tracking, dense point-wise flow) treat motion as independent point-wise displacements, ignoring the structured nature of physical motion. However, real-world objects usually obey rigid-body kinematics, and points thus usually move collectively, not in isolation. Motion itself possesses geometric structure: physical objects undergo a set of rigid-body transformations governed by SE(3), rather than unstructured point-wise displacements. Building on this insight, we propose SM4RT, a Structured Motion 4D Reconstruction Transformer for end-to-end 3D reconstruction and structured motion perception. SM4RT introduces Structure-of-Motion to represent scene dynamics, where scene motion is decomposed into a compact set of motion bases, each represented as a temporal sequence of 6D twists in SE(3). Dense scene motion is then recovered by sparse, time-shared per-pixel assignment weights over these bases, ensuring points on the same object share a common rigid-body motion trajectory. SM4RT introduces a parallel motion geometry encoder and decoder that jointly infer 3D geometry, world-coordinate motion, and scene kinematic structure in a single forward pass from monocular RGB video. SM4RT achieves strong motion reconstruction performance while preserving the geometric structure of scene motion.

---


> [!TIP]
> 当前位于：**151-169**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-169**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
