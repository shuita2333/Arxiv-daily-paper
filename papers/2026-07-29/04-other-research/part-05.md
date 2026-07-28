# 📦 其他研究 | 2026年07月29日

> 本类共 **442** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-442](./part-09.md)

---

### 201. [ATLAS: Automated Approximation of Transformers for Efficient Homomorphic Inference in One Hour](https://arxiv.org/abs/2607.23478)

**<font color=#1a73e8>作者：</font>** Jianhang Xie, Sicheng Tan, Vishnu Naresh Boddeti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) provides strong cryptographic guarantees for private inference, but deploying transformer models under FHE remains prohibitively expensive. A key bottleneck is that non-linear operations such as softmax, normalization, and activation must be replaced with polynomial approximations compatible with the CKKS scheme, and the multiplicative depth consumed by these approximations dominates inference cost. Recent frameworks have advanced approximation techniques, yet all rely on manually configured approximation hyperparameters (e.g., number of iterations, polynomial degree), applied uniformly across all layers. While convenient, this uniform-configuration approach is overly rigid: different layers can tolerate different levels of approximation error without degrading predictive accuracy, and uniform configurations cannot exploit this variability to reduce latency. Allowing each layer to adopt its own configuration, however, causes the search space to explode with model depth, reaching roughly $10^{84}$ configurations for BERT/ViT (12 layers) and $10^{225}$ for LLaMA3 (32 layers), rendering manual exploration practically impossible. We present ATLAS, an automated framework that configures per-layer approximation settings by formulating the problem as a multi-objective optimization over latency and predictive accuracy. The resulting problem is inherently difficult: 1) competing objectives over a large decision space (120 or 320 variables for BERT/ViT or LLaMA3); 2) expensive evaluation, as each configuration takes 70-1,000 seconds even in cleartext; and 3) sparse optimization signals, as 35-50% of candidate configurations yield numerically invalid solutions. ATLAS addresses these challenges through a two-stage optimization strategy that progressively relaxes layer-wise constraints, combined with surrogate models to accelerate evaluation.

---


### 202. [A Multi-stage Constrained Optimization Framework for Data-driven Problems](https://arxiv.org/abs/2607.23480)

**<font color=#1a73e8>作者：</font>** Ye Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variational autoencoders (VAEs) transform high-dimensional, often noisy data into a compact latent representation, making downstream optimization more tractable. Three challenges persist in VAE-based constrained optimization: (i) sampling effectively within the latent space, (ii) identifying the active decision variables that actually influence the objective and constraints, and (iii) enforcing constraints without destabilizing training. We propose a Multi-stage Constrained Optimization Framework (MCOF). First, an entropy-constrained VAE (EC-VAE) coupled with a feature selector embeds objective and constraint information into a designated subset of latent variables, so that optimization proceeds over a low-dimensional subspace while the remaining coordinates supply solution diversity. Second, a Uniform Transformation (UT) module applies a per-dimension probability integral transform, replacing the irregular aggregate posterior with a uniform distribution over a bounded box and mitigating posterior collapse and Gaussian mixture bias. Third, a constraint-priority filter method (CPFM) solves the resulting surrogate problem by alternating violation-reduction and objective-reduction steps under a filter acceptance test, returning solutions that are feasible for the learned surrogate to a specified tolerance without requiring multiplier estimation. Finally, unselected latent coordinates are resampled to generate diverse decodings of a single optimized solution. We validate MCOF on a synthetic problem, where we ablate each stage and recover the analytic optimum, and on a ZINC250k drug design task, where the generated molecules satisfy the imposed constraints and are entirely novel relative to the training set.

---


### 203. [Charging Phase Health Indicators for Battery State-of-Health Estimation: A Systematic Comparison of CC, CV, and Combined Approaches under Cross-Battery Validation](https://arxiv.org/abs/2607.23482)

**<font color=#1a73e8>作者：</font>** Huy Hoang Le, Kim-Anh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate State-of-Health estimation is essential for safe battery operation and cost-effective maintenance. Although numerous health indicators have been derived from constant-current (CC) and constant-voltage (CV) charging phases, their effectiveness under realistic cross-battery validation remains insufficiently studied. This work addresses this gap through a systematic comparison of CC-only, CV-only, and combined indicator sets using rigorous Leave-One-Battery-Out (LOBO) validation on the NASA battery aging dataset. Four CV-phase indicators and CC phase duration are evaluated individually and in combination. Results show that the combined CC+CV approach achieves the best performance (R2 = 0.874), confirming that CC and CV phases capture complementary degradation information. Moreover, a 119% performance gap is observed between standard 5-fold cross-validation and LOBO validation, indicating that conventional evaluation overestimates practical accuracy. Based on these findings, practical guidelines are provided for indicator selection under data and computational constraints.

---


### 204. [An adaptive multi-fuzzy logic model for diagnosing transformer faults using dynamic weight optimization](https://arxiv.org/abs/2607.23486)

**<font color=#1a73e8>作者：</font>** Kim-Anh Nguyen, Huy Hoang Le, Ba Tu Phung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dissolved gas analysis (DGA) is crucial for diagnosing early power transformer failures. Traditional DGA interpretation methods like Duval Triangle, IEC ratio, Roger ratio, Doernenburg ratio and Key Gas are inconsistent and vary in accuracy, especially for multiple fault conditions. We propose an Adaptive Multi-Fuzzy Logic (AMFL) model integrating multiple DGA methods with fuzzy logic and a dynamic weight adjustment mechanism. Unlike existing approaches with fixed weights, this system iteratively evaluates each method's diagnostic performance, identifies multiple fault types, and adjusts weights based on fault prediction accuracy. A feedback-based optimization recalibrates weights after each cycle to ensure optimal solution convergence. The model, implemented in MATLAB/Simulink, is validated against DGA datasets with known error conditions. Results show the AMFL model significantly improves diagnostic accuracy, especially in complex error scenarios, and enhances adaptability to new datasets. Comparative analysis demonstrates the proposed method outperforms traditional fixed weight multi-fuzzy systems in accuracy, consistency, and reliability of error detection. This work provides a robust, flexible diagnostic tool for transformer condition monitoring and supports more accurate asset management decisions.

---


### 205. [Learning Sampling Parameters for Diffusion Models](https://arxiv.org/abs/2607.23488)

**<font color=#1a73e8>作者：</font>** Arisrei Lim, Yossi Gandelsman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models expose many inference-time sampling parameters, including prompts, negative prompts, classifier-free guidance scales, and noise schedules. These parameters are typically manually chosen once and then held fixed across prompts and denoising timesteps, even though different prompts and stages of generation can benefit from different parameter values. We introduce LeSAMP, a framework for learning prompt-conditioned, timestep-varying sampling parameters. We formulate parameter selection as a reinforcement learning problem: Given a user prompt, a large language model is trained to emit schedules for the chosen sampling parameters. We optimize our model using rewards from human preference models and VLM-as-a-judge. We evaluate our model on Flux.1 [dev] and Stable Diffusion 3.5, and find that compared to baselines, LeSAMP has a win rate of up to 68.12% using human preference scores and 73.37% using VLM-as-a-judge. These gains are validated in a user study where we achieve win rates of up to 59.46% over previous baselines. Our results suggest that learned sampling-parameter policies provide a complementary approach to existing post-training methods for improving diffusion model outputs.

---


### 206. [PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491)

**<font color=#1a73e8>作者：</font>** Pengyu Zeng, Yuqin Dai, Jun Yin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Two structural insights have been overlooked in automated residential floor plan generation. First, design is inherently progressive. Architects begin with rough strokes and refine them over time, whereas existing methods typically require their conditioning representation to be fully specified before generation, a fundamental mismatch with how design actually works. Second, the 2D floor plan is not an optional intermediate but an irreplaceable spatial contract. Once room boundaries, doors, and windows are fixed, furnishing reduces from open-ended spatial reasoning to bounded constraint satisfaction. Bypassing this contract, as existing 3D systems do by delegating layout to language models, yields overlapping rooms and implausible proportions; directly calling general-purpose language models likewise produces geometrically invalid layouts. Guided by these insights, we present PlanCraft. SketchPlan supplies the missing training signal by replaying the architect's drawing process on 80K real floor plans, producing partial sketches at every completeness level. PlanCraft-Diff progressively sharpens an incomplete sketch into a geometrically precise, vectorizable floor plan through a coarse-to-fine strategy. With the spatial contract established, PlanCraft-Agent then furnishes the scene within well-defined room boundaries. Experiments show that PlanCraft achieves a 61.1\% lower FID than the best existing 2D method and surpasses existing 3D systems by 15 points in expert-rated spatial rationality, with a sketch at only 25\% completion already outperforming all fully specified baselines.

---


### 207. [To Erase, or Not to Erase: Robust Training-Free Concept Erasure with Preservation aware Adaptive Ranked Subspace Expansion](https://arxiv.org/abs/2607.23492)

**<font color=#1a73e8>作者：</font>** Shaswati Saha, Rajasekhar Anguluri, Manas Gaur  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure techniques (CETs) edit text-to-image diffusion models to erase undesired targets such as NSFW content or copyrighted styles, while preserving model utility on benign concepts. Current CETs face a trade-off between erasure robustness and utility: stronger edits erase the target more reliably but degrade utility on non-target concepts, and vice versa. This stems from how existing methods define what to erase and what to preserve. Many CETs rely on static concept banks specified manually, generated by LLMs, or selected by CLIP image-text similarity. Such banks do not model how prompts steer the model during denoising, leaving it vulnerable to triggers that reintroduce the target while suppressing nearby benign concepts. We present Preservation-aware Adaptive Ranked Subspace Expansion (PARSE), a training-free framework for robust concept erasure in latent diffusion models. Given a target, PARSE queries the diffusion model with classifier-free guidance to dynamically discover target-inducing erase concepts and nearby retain concepts in the model vocabulary. It then edits the cross-attention value space with a preservation-aware projection that removes target directions while leaving retain directions intact. For triggers beyond this vocabulary-indexed space, PARSE iteratively searches for re-emergence triggers by textual inversion and adaptively expands the erased subspace only when a new trigger direction does not conflict with retain semantics. We also introduce the Balanced Erasure Utility Score (BEUS), which combines robustness (ASR under multiple attacks) and utility preservation (FID) via bounded monotone transforms and harmonic mean aggregation. Experiments on NSFW, artistic style, and object erasure, with a large-scale robustness-utility analysis over many CET baselines, show that PARSE erases multiple concepts robustly without sacrificing post-edit utility.

---


### 208. [Physics-Informed Neural Networks for Discovering Periodic Orbits in the Gravitational Three-Body Problem](https://arxiv.org/abs/2607.23501)

**<font color=#1a73e8>作者：</font>** Nikolaos Kollias, Nikolaos Matzakos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Locating periodic solutions of chaotic dynamical systems normally requires an initial guess close enough to the target orbit for numerical continuation or gradient-based search to converge. We show that Physics-Informed Neural Networks (PINNs) trained on sparse, noisy observations \emph{without} initial conditions recover periodic orbits of the gravitational three-body problem, including orbit families absent from the training data. The method rests on a second-order ODE formulation, fixed-frequency Fourier features, percentile-based adaptive refinement, and a trainable scaling parameter, each validated on forward problems. Across two 100-seed ensembles, $23$--$25\%$ of runs converge to families not present in the training data. We then ask what determines which family emerges. Two $\chi^2$ tests give a consistent answer: changing the training data source significantly shifts the distribution of recovered families ($p < 0.001$, Cramér's $V = 0.339$), whereas switching between the two initialization distributions tested does not ($p = 0.620$, $V = 0.094$). The random seed selects which family a given run recovers; the \emph{distribution} the weights are drawn from does not shift the aggregate frequencies, but the training data does. The evidence is empirical: we do not characterize the loss landscape analytically, and PINNs remain slower than conventional integrators on well-posed initial-value problems. What the experiments establish is that the recovered orbits are verifiable rather than merely plausible: the identified ones refine to genuine periodic solutions, a network trained on Lagrange data recovers the figure-eight choreography (Li--Liao class I.A.1, matched to seven significant digits in $T^*$), and one trained on figure-eight data recovers a Broucke--Hadjidemetriou--Hénon orbit closing to $\delta_T < 10^{-9}$.

---


### 209. [Impute On-Demand: Adaptive Correlated Time Series Imputation for Changing Environments](https://arxiv.org/abs/2607.23503)

**<font color=#1a73e8>作者：</font>** Zhichen Lai, Huan Li, Dalin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Internet of Things (IoT) applications generate vast amounts of Correlated Time Series (CTS) data that often contain missing values and require imputation. Existing methods emphasize accuracy but often lack adaptability to changing IoT environments: they are vulnerable to sensor failures, cannot selectively impute only incomplete sensors, and use static architectures that do not adapt to resource availability. To address these limitations, we propose AdaCTSi, an adaptive CTS imputer for changing environments. AdaCTSi combines a One-shot Temporal Convolutional Network with a Learned Time-Sensor Index Table to extract and decouple complex spatio-temporal features into sensor-wise embeddings, enabling adaptation to varying sensor subsets. Sparse Spatial Attention efficiently extracts dynamic spatial correlations, while Correlation-Weighted Sensor Selection selects informative sensors to provide sufficient spatial context. Experiments with twelve baseline methods, three adaptability scenarios, and five benchmark datasets covering traffic, air quality, and trajectory data show that AdaCTSi reduces MAE by an average of 33.1% relative to the strongest baseline on each dataset. A single trained model supports sensor-subset and resource-adaptive inference, and its modest memory footprint enables deployment on commodity computing devices, including MCUs.

---


### 210. [Topological Data Analysis and Graph-Theoretic Approaches for Tennis Match Prediction](https://arxiv.org/abs/2607.23509)

**<font color=#1a73e8>作者：</font>** Jake Schwaderer, Alexander Bastien, Omid Khormali 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present two approaches for predicting tennis match outcomes using topological data analysis and graph theory on ATP singles matches from 2000-2025. The first method applies lower-star filtration to player competitive networks, extracting topological features through persistent homology using four summary methods (VAB, HNAV, HWNAV, OW-HNPV) combined with Modified Band Depth analysis. Algorithmic optimizations including ego graph approximations and triangle elimination enable analysis of about 66k matches. Our Random Forest model achieves 66.2% accuracy (AUC = 0.719) using topological, graph-theoretic, and ranking features. Feature importance analysis reveals that rankings contribute 36.3%, centralities 25.5%, and TDA features 24.0%, with topological features providing complementary signal. When rankings are unavailable, the topology-only model maintains 63.56% accuracy, demonstrating that network-derived features alone capture meaningful competitive structure. The second method uses a modified Katz similarity index with temporal edge weighting, achieving 62.48% accuracy on held-out test data. This work represents the first application of lower-star filtration to tennis prediction, provides systematic comparison of four topological summary methods in sports analytics, and demonstrates that TDA can achieve above-chance prediction using network topology alone while providing additional value when combined with traditional features.

---


### 211. [MOJITO: Modal Joint Learning for Unified End-to-End Autonomous Driving](https://arxiv.org/abs/2607.23511)

**<font color=#1a73e8>作者：</font>** Zhijing Cheng, Xuancheng Zhang, Donglin Di 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end autonomous driving systems commonly follow a cascaded two-stage pipeline where a perception stage compresses multi-modal sensor inputs into a compact context and a downstream planner predicts trajectories conditioned on this context. We argue that this one-way perception-to-planning interface forces sensor inputs into a compact representation, losing the fine-grained details critical for planning. Moreover, by constraining the planner to this compressed context, it is difficult to leverage the rich representations offered by modern vision foundation models. To address these issues, we propose MOJITO, a unified sensor-to-action framework for end-to-end autonomous driving built on modal joint learning. MOJITO removes the cascaded interface and instead performs block-wise Modal Joint Attention that simultaneously updates action, image, and LiDAR features, allowing the planner to directly access multi-modal features during action generation. MOJITO achieves 88.9 PDMS on the NAVSIM v1 dataset and 88.4 EPDMS on the more challenging NAVSIM v2 dataset, setting a new state-of-the-art. Extensive experiments further demonstrate strong scalability, instruction following, and diverse trajectory generation. Code and models are available at this https URL.

---


### 212. [The Cross-Domain Generalization Cost of Offensive Language Detection](https://arxiv.org/abs/2607.23512)

**<font color=#1a73e8>作者：</font>** Ruixing Ren, Junhui Zhao, Xiaoke Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Offensive language detection models generally suffer performance degradation when deployed across datasets and across languages, yet most existing studies stop at reporting this phenomenon and lack a systematic methodology for decomposing the causes of degradation into attributable components and quantifying the cost of remediation. This paper proposes a diagnosis and optimization framework composed of three coordinated technical components. First, a zero-shot transfer loss decomposition that separates the performance degradation from OLID to MLMA into two independently measurable components, namely dataset effect and language effect. Second, a controlled fine-tuning protocol that quantifies both adaptation efficiency and the hidden damage inflicted on the source task by comparing few shot learning curves under continued fine-tuning and cold-start starting points. Third, three joint training strategies incorpo rating temperature sampling and experience replay, which offer a controllable Pareto trade-off between improving multilingual capability and preserving source-task performance. Experiments built on this framework show that the dataset effect dominates the zero-shot transfer loss and substantially outweighs the language effect. Few-shot adaptation without a replay mechanism, though data-efficient, inflicts source task damage 4 to 9 times greater than that of the joint training strategies, and its damage magnitude is highly unstable. The three joint training strategies trade 3.2 to 4.1 percentage points of source-task performance for 8.1 to 42.6 percentage points of multilingual capability gain, forming a clear and controllable Pareto trade-off.

---


### 213. [Chamaileon: Cross-Context Binder Design with Contextualized Modeling and Mixed Sampling](https://arxiv.org/abs/2607.23518)

**<font color=#1a73e8>作者：</font>** Hengyuan Cao, Shizhuo Cheng, Mingxuan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of generative models has unlocked new potentials in protein binder design, a pivotal task in structural biology, by facilitating end-to-end generation via joint sequence-structure modeling or hallucination. However, existing approaches are predominantly implemented under a single-target, single-state assumption, limiting their ability to model multi-target or multi-state interactions required for advanced function-oriented protein design. Here, we introduce Chamaileon, which unifies multi-target and multi-state binder design by formulating the problem as cross-context binding landscape modeling. The framework is underpinned by a training paradigm termed In-Context Complex Co-Design (I3CD) for context-aware sequence-structure co-modeling. During inference, we employ Mixture-of-Paths Sampling (MoPS), a scalable strategy that optimizes a single sequence across contexts while alleviating the scarcity of high-quality multi-conformational paired data. Extensive evaluation on our newly constructed benchmark, CROSS, demonstrates that Chamaileon effectively generates sequences adaptable to diverse conformational landscapes and multi-target requirements. The code is available on this https URL.

---


### 214. [ATCNet-CIAM for Multi-Session Motor Imagery EEG Signal Classification](https://arxiv.org/abs/2607.23522)

**<font color=#1a73e8>作者：</font>** Le Huu Son Hai, Nguyen Chi Hai, Truong Viet Vu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motor imagery (MI)-based electroencephalography is widely used in non-invasive brain--computer interfaces (BCIs), but robust decoding remains challenging due to inter-subject variability and cross-session non-stationarity. This work proposes ATCNet-CIAM, an enhanced attention temporal convolutional network that integrates a lightweight channel-integrated attention module (CIAM) into the ATCNet framework to improve channel-spatial feature representation for MI decoding. The proposed model is evaluated on BCI Competition IV-2a, BCI Competition IV-2b, and the multi-day WBCIC-MI dataset under standard, within-session, and cross-session protocols. Experimental results show that ATCNet-CIAM achieves 86.32% accuracy on BCI IV-2a and 87.96% on BCI IV-2b under the standard protocol, while reaching 89.46% and 83.64% in the within-session WBCIC-MI on 2C and 3C, respectively. The proposed framework consistently improves classification stability and robustness under session-varying conditions, and ablation study confirms the complementary contribution of the proposed architectural components.

---


### 215. [Delegation Intelligence in Deep Search: A Controllable Framework for Disentangled Capability Diagnosis](https://arxiv.org/abs/2607.23524)

**<font color=#1a73e8>作者：</font>** Xinhao Yao, Yuanzhuo Liu, Changhao Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep search is becoming a core capability of modern agent systems, yet it is typically evaluated solely based on end-to-end answer accuracy. This coupled evaluation paradigm entangles retrieval quality, long-context comprehension, evidence verification, and tool-use decisions, making it difficult to determine whether a model truly knows when and how to delegate information seeking to search. To this end: (1) We formalize this meta-capability as Delegation Intelligence in deep search and decompose it into complementary dimensions-Search Decision-Making (recognizing information insufficiency and deciding whether, when, and how to search) and Information Synthesis and Verification (aggregating evidence from multiple sources, judging source reliability, and synthesizing information under noisy, potentially adversarial conditions). (2) To enable disentangled and reproducible measurement, we develop a controllable synthesis pipeline built on document-grounded reverse engineering. This yields a general recipe for constructing controlled deep-search evaluations rather than a single fixed dataset. (3) As a concrete instantiation, we construct DelegSearchBench, together with a disentangled evaluation protocol that isolates each capability dimension by varying document composition and tool access. (4) Across representative models, we demonstrate that deep-search competence cannot be adequately characterized by final-answer accuracy alone...

---


### 216. [Geometry Meets Semantics: Fractional Gradient Stabilization for Semantic-Driven Bounding Box Optimization in Visual Detection Tasks](https://arxiv.org/abs/2607.23530)

**<font color=#1a73e8>作者：</font>** Qi Ming, Haitian Yang, Xudong Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bounding boxes are fundamental for object localization in visual detection tasks. Among them, oriented bounding boxes are widely used in visual detection tasks, which provide a more precise directional representation. Generally, IoU-based losses are widely adopted to optimize box regression. However, we observed that IoU-driven box optimization suffers from two key issues: (1) it relies solely on geometric properties while ignoring semantic cues; (2) orientation optimization suffers from unstable gradients, causing oscillations in orientation convergence. In this paper, we propose a Fractional Semantic IoU loss to achieve unified semantic-geometric learning with gradient stabilization. First, we design a semantic similarity metric to guide IoU optimization, building a Semantic IoU loss (SIoU loss) with an adaptive gradient gating mechanism. Then, we revisit the gradient instability issue in oriented box optimization and extend the SIoU loss to a fractional-order formulation to build the \textbf{Fr}actional \textbf{S}emantic \textbf{IoU} \textbf{loss} (FrSIoU loss). The FrSIoU loss accumulates historical IoU states to regularize abnormal gradients during bounding box optimization process. Extensive experiments demonstrate that our approach achieves stable performance gains across different bounding box formulations and diverse visual detection tasks. The code will be available on GitHub.

---


### 217. [The JEPA Paradox in Language: The Geometry of Linguistic Alternatives](https://arxiv.org/abs/2607.23531)

**<font color=#1a73e8>作者：</font>** Anh Trac Duc Dinh, Khang Nhat Hoang Vo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) are effective for images, video, and audio, yet deterministic JEPA-style latent prediction has not become a standard objective for text encoders. We argue that this gap reflects a mismatch between squared-error latent prediction and the conditional structure of language. The key requirement is conditional concentration: given a context and target location, the target representation should lie near a single meaningful point. Local image prediction often satisfies this through spatial continuity, whereas masked text can admit multiple valid token or span completions whose representations need not share a coherent center. We formalize this mismatch through three conditions---predictability, non-collapse, and low conditional variance---and show how their failure creates centroid degeneracy and collapse pressure in text. Matched I-JEPA and T-JEPA experiments reveal the predicted sequence: mutual-information saturation and elevated target variance precede train--validation instability, effective-rank degeneration, cosine collapse, and poor downstream transfer. The same pattern appears across five independent data seeds, indicating that it is not a sampling artifact. These results do not rule out predictive learning for language; they show that text-compatible JEPA objectives must preserve multiple plausible completions rather than compress them into a single latent point.

---


### 218. [Collusion-Resistant Image-Agnostic Watermarking for Multi-Screen Shooting](https://arxiv.org/abs/2607.23553)

**<font color=#1a73e8>作者：</font>** Mingyue Chen, Xin Liao, Yufeng Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Screen-shooting poses a significant threat to confidential information protection. While existing screen-shooting watermarking methods enable copyright verification, the copyrighted images carrying the same copyright watermark across different screens often exhibit highly similar and estimable watermark patterns. These shared patterns can be exploited for watermark removal and forgery, a threat we term the multi-screen collusion attack. To mitigate this threat, we propose CoMSMark, a collusion-resistant image-agnostic watermarking framework for multi-screen shooting, which reduces shared residual components across screens to resist multi-screen collusion attacks. Specifically, we incorporate screen ID through a style modulation mechanism, enabling the encoder to generate screen-specific watermark residuals for reliable source attribution. We further introduce a collusion suppression loss that reduces shared residual components and encourages high-entropy predictions for forged samples, improving resistance to collusion attacks. Finally, to enable efficient large-scale distribution, CoMSMark employs an image-agnostic encoding paradigm that generates watermark residuals independently of image content. Extensive experiments demonstrate that CoMSMark effectively resists both collusion-based watermark removal and forgery. It maintains an average watermark accuracy above 90% under removal attacks while keeping forged-watermark accuracy near 50%. Moreover, CoMSMark achieves competitive robustness under diverse screen-shooting conditions, including varying capture distances and angles.

---


### 219. [Neonatal Hypoxic-ischaemic Encephalopathy Classification from the EEG and HRV Signals Using a Conformer based Masked Autoencoder](https://arxiv.org/abs/2607.23554)

**<font color=#1a73e8>作者：</font>** Shuwen Yu, William P Marnane, Geraldine B. Boylan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose the MAEConformer, a novel self-supervised learning framework that combines the Conformer architecture with the Masked Autoencoder (MAE) paradigm for large-scale representation learning from unlabelled electroencephalography (EEG) and heart rate variability (HRV) signals. By integrating convolutional operations with Transformer-based self-attention, MAEConformer effectively captures both local temporal patterns and long-range contextual dependencies in physiological time series. To enhance reconstruction fidelity and representation quality, a multi-resolution short-time Fourier transform (MR-STFT) loss is incorporated alongside the reconstruction objective, enabling the model to jointly learn temporal and spectral characteristics across multiple scales. Modality-specific EEG and HRV MAEConformer models were pretrained on 6,030h and 4,868h of unlabelled recordings, respectively, and subsequently transferred to expert-annotated downstream tasks. Experimental results demonstrate that the learned representations provide strong transferability and data efficiency. In EEG-based hypoxic ischemic encephalopathy (HIE) severity classification, the pretrained MAE-EEG model achieved test AUCs of 97.19% and 96.56% for binary and four-class classification tasks, respectively, outperforming a range of state-of-the-art supervised and self-supervised baselines. On the HRV-based HIE severity classification task, MAE-HRV achieved a test AUC of 82.42%, surpassing both self-supervised Transformer-based and supervised convolutional baselines. These findings demonstrate the effectiveness of MAEConformer for learning robust and transferable representations across multiple physiological modalities.

---


### 220. [Random Forest-Based Prediction of Bone Volume Fraction and Fracture Position from S-Parameters](https://arxiv.org/abs/2607.23563)

**<font color=#1a73e8>作者：</font>** Jianhe Li, Jinsui Meng, Yida Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a method for predicting bone volume fraction (BVF) and fracture position by constructing a random forest model based on multichannel S-parameters. A nine-antenna microwave scanning system is designed and fabricated to acquire the multichannel S-parameter data. Bone-mimicking phantoms are developed, and corresponding experiments are conducted to validate the effectiveness of the proposed approach. Both synthetic and experimental results demonstrate the validity of the method.

---


### 221. [D3O: Dynamic Distribution Distillation for Ordinal Regression](https://arxiv.org/abs/2607.23575)

**<font color=#1a73e8>作者：</font>** Chunlai Dong, Yaojun Hu, Yuyang Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ordinal regression is widely used in scenarios where labels are discrete yet inherently ordered. In practice, however, ordinal labels are often obtained by discretizing underlying continuous semantics through subjective human judgment, resulting in ambiguous boundaries and annotation noise. Such uncertainty challenges existing methods that rely on fixed supervision targets, which may reinforce biased ordering under subjective annotations. To address this limitation, we propose D3O, a dynamic distribution distillation framework that replaces static supervision with training-driven evolution of ordinal label distributions via self-distillation. Specifically, we introduce a contrastive ordinal-aware label enhancement module that leverages vision-language alignment to recover refined label distributions capturing both inter-class ambiguity and instance-level uncertainty. Furthermore, we design a CDF-based cross-layer interaction distillation mechanism to propagate cumulative ordinal structure across network hierarchy, ensuring consistent ordinal geometry in intermediate representations. Extensive experiments on four general ordinal regression tasks demonstrate that our proposed D3O consistently outperforms existing approaches, particularly under severe class imbalance and noisy supervision. These results highlight the effectiveness of dynamic supervision in learning robust ordinal representations beyond fixed targets. The code will be publicly available.

---


### 222. [Neuromorphic Object Detection: An In-Depth Study and Future Directions](https://arxiv.org/abs/2607.23576)

**<font color=#1a73e8>作者：</font>** Jianing Li, Dianze Li, Arren Glover 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional frame-based cameras face significant challenges in detecting objects under high-speed motion blur or in low-light environments. Neuromorphic cameras provide asynchronous visual streams with high temporal resolution and a wide dynamic range, offering a promising solution for object detection under challenging conditions. Despite the development of numerous models and the emergence of various applications in neuromorphic object detection, there is still a lack of deep understanding and standardized benchmarks to assess progress and address key challenges. In this paper, we provide a comprehensive survey and benchmark of existing neuromorphic object detection algorithms. Specifically, we first present a problem description, review the available datasets, and revisit the evaluation metrics. We then explore existing neuromorphic object detection approaches from various perspectives, including event representation, temporal modeling, multimodal fusion, asynchronous processing, low-latency processing, and energy-efficient computing. Furthermore, we evaluate a wide range of representative neuromorphic object detection models and offer detailed analyses of the comparative results. Finally, we discuss unresolved issues in neuromorphic object detection and propose potential future research directions. We hope this survey and benchmark will be a valuable resource for researchers and provide guidance for future advancements in neuromorphic object detection.

---


### 223. [SketchMamba: A Lightweight State-Space Model for Joint Progressive Sketch Classification and Stroke Auto-Completion](https://arxiv.org/abs/2607.23580)

**<font color=#1a73e8>作者：</font>** Kavish Jhaveri, Arya Shah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing vector-sketch models treat recognition and generation as separate tasks, leaving a gap for streaming interfaces that must understand a drawing as it is being made. We present SketchMamba, a single causal sequence model that continuously classifies a sketch from any partial prefix while simultaneously generating its continuation. We achieve this by applying a dense per-step classification loss to a selective state-space backbone. Evaluated on a 58-class subset of the Quick, Draw! dataset, SketchMamba yields 94.93% final-step accuracy and a progressive-accuracy Area Under the Curve (AUC) of 0.706, crossing 90% of its final accuracy by the time 70% of the strokes are drawn. In a matched-budget comparison, the 1.55 million-parameter backbone ties a causal Transformer while outperforming recurrent and convolutional baselines. Ablations confirm that the dense supervision regime, rather than the architecture alone, drives the early-prediction capability. The results demonstrate that a single causal hidden state can unify progressive recognition and autoregressive generation without auxiliary encoders or task-specific branching.

---


### 224. [Are You Still the Agent I Authorized? Earned Authority under a Fixed Ceiling for Evolving Agents](https://arxiv.org/abs/2607.23586)

**<font color=#1a73e8>作者：</font>** Zhaoxi Zhang, Xiaomei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-lived AI agents increasingly evolve after deployment by retaining experience, acquiring skills and tools, revising workflows, delegating work, and moving across task phases. This improves adaptation but creates a distinct authorization problem. Tool-enabled agents can turn model errors and prompt injections into consequential external actions; when evolution occurs under a live grant, the subject exercising that authority or the context in which it acts may no longer match what the user evaluated. Evolution can change both the effects reachable under an old grant and the authority required by the task, which may rise, fall, or become incomparable. Existing tool policies constrain actions but do not determine when a grant survives this change.
We formulate authorization continuity: when does an existing grant remain valid, how may active authority change, and what boundary must never move? Our state-bound model fixes a transition envelope and an immutable effect ceiling at grant time. The envelope determines whether the grant survives a mutation; below the ceiling, authority may contract freely and expand only under specified evidence conditions. We distinguish requested from realized effects and prove that, under complete mediation, sound effect abstraction, attenuating delegation, and monitor integrity, mutation cannot amplify protected effects beyond the user-issued ceiling. Agent-produced evidence may allocate authority below the ceiling but cannot raise it. Finally, we map six mutation classes to their authorization consequences.

---


### 225. [Weakly Supervised Instance-Level Gleason Pattern Estimation Using Primary and Secondary Labels](https://arxiv.org/abs/2607.23594)

**<font color=#1a73e8>作者：</font>** Nao Sugeta, Kaito Shiku, Shinnosuke Matsuo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In prostate cancer histopathology, the Gleason Score is determined by the most frequent (Primary) and second most frequent (Secondary) Gleason patterns within a whole-slide image. Although these slide-level labels are routinely available in clinical practice, instance-level Gleason annotations are rarely provided, making patch-level learning challenging. We propose a Multiple Instance Learning (MIL) framework that estimates instance-level Gleason patterns from slide-level Primary and Secondary labels. The proposed method formulates instance-level learning according to the clinical definition of the Gleason Score by aggregating instance predictions into class counts and explicitly modeling the Primary pattern, Secondary pattern, and their dominance. Experimental results demonstrate that the proposed formulation enables effective instance-level learning and outperforms existing MIL approaches on the SICAP-MIL dataset.

---


### 226. [HiTMS: A High-Throughput Multi-Stream Linguistic Steganography Framework](https://arxiv.org/abs/2607.23597)

**<font color=#1a73e8>作者：</font>** Ruiyi Yan, Yugo Murawaki, Zhongliang Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative linguistic steganography conceals secret bits within the sampling randomness of large language models. Existing schemes are single-stream, conveying an entire secret through a single response to a single prompt. This convention incurs two limitations: it provides no protocol-level support for batched multi-stream inference, and naive co-batching does not conceal slot occupancy or payload completion. We propose HiTMS, which distributes a secret across multiple responses produced jointly over successive rounds of interaction. Each round embeds and extracts several streams within a single batched call, thereby amortizing the cost of model invocation and substantially improving throughput. To ensure recoverability, HiTMS wraps each response in a self-describing frame and employs a key-derived schedule that binds streams to slots and fills unused slots with decoys, guaranteeing exact recovery while concealing the number of active streams. The framework is agnostic to both the language model and the steganographic coder. Across eight dataset-model-coder settings, eight-stream HiTMS achieves up to 4.3 times higher embedding and extraction speeds than single-stream baselines, while reducing the steganalyzer AUROC from 0.681 to 0.601 on average. Additional experiments with 4 to 64 streams demonstrate sustained throughput gains as concurrency increases. GitHub repository for this work is this https URL.

---


### 227. [Markerless Motion Capture in Routine Clinical Upper Limb Assessments: Validity and Insights Beyond Ordinal Scoring](https://arxiv.org/abs/2607.23608)

**<font color=#1a73e8>作者：</font>** Tim Unger, Olivier Lambercy, Roger Gassert 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Action Research Arm Test (ARAT) is a widely-used upper limb outcome measure in neurorehabilitation, but its ordinal scoring is subjective and suffers from limited sensitivity and specificity. We evaluated whether artificial-intelligence (AI)-based markerless motion capture (MMC), embedded into ARAT assessments during clinical routine, accurately reconstructs upper limb movement and yields valid, objective kinematic metrics carrying clinically meaningful information beyond the ordinal score. Across 47 sessions from 20 mixed-neurological patients (1,174 ARAT tasks), biomechanical reconstruction was accurate and robust across impairment levels, and kinematic metrics showed the discrimination pattern expected of a construct-valid measure. In longitudinal case studies, the metrics added the specificity and sensitivity the ordinal score lacks: a domain decomposition exposed patient-specific recovery profiles underlying equal ARAT gains (specificity), and kinematic improvement continued to be detected after the ARAT had saturated (sensitivity). MMC in clinical routine can thus provide valid, objective, sensitive, and specific kinematic measurement complementing ordinal scoring.

---


### 228. [DualityCert: Verifier-Gated Language-Model Repair of Broken Duality Claims in Quantum Field Theory](https://arxiv.org/abs/2607.23614)

**<font color=#1a73e8>作者：</font>** Xingyang Yu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present DualityCert, a symbolic verifier for candidate Seiberg-duality claims in four-dimensional N=1 quiver gauge theories. The verifier evaluates 't Hooft anomaly matching, superpotential R-charge consistency, central-charge matching, and a bounded chiral-ring proxy. A claim that passes receives a consistency certificate, which states that no tested inconsistency was found, not that the duality is proven. We use the verifier as a repair environment for language-model agents, which receive a deliberately broken claim and must edit it until it certifies. On a preregistered benchmark of 145 broken claims, with the analysis fixed before the first confirmatory model call, verifier-gated retry improves final repair success over a single attempt by +8.3 percentage points (pp) on deepseek-chat and +7.1 pp on qwen-plus (Holm-adjusted p<0.002). Under an equal budget of eleven attempts, the stop-first strategy portfolio underperforms independent verifier-filtered resampling by 10.3 percentage points on deepseek-chat but outperforms it by 14.7 points on qwen-plus, reversing the ordering of the two tested verifier-exploitation policies across the two confirmatory models. On qwen-plus, category-level verifier feedback is worth +8.7 pp over content-free retry, and interpretable obligation identities alone are worth +6.4 pp over structurally identical masked feedback. Neither effect is detected on deepseek-chat. Separately, a preregistered MiniMax-M2.5 extension again finds an iteration gain and independent verifier-filtered resampling outperforming the strategy portfolio. Which policy is better thus differs between the two models, while every winning policy uses the same cheap certificate. The verifier, benchmark, protocol, and all per-attempt records are released.

---


### 229. [Restoration Flow Matching-Based Channel Refinement and Equalization Correction for MIMO Semantic Communications](https://arxiv.org/abs/2607.23615)

**<font color=#1a73e8>作者：</font>** Wenkai Liu, Nan Ma, Jianqiao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multiple-input multiple-output (MIMO) semantic communication, imperfect channel state information (CSI) and equalization mismatch can seriously degrade semantic reconstruction quality. To address this issue, we propose a unified restoration flow matching (RFM)-based framework for channel refinement and equalization correction. Specifically, the channel RFM (CRFM) module is developed to refine the coarse channel, thereby improving channel estimation accuracy. Based on the refined channel, the developed semantic RFM (SRFM) module is employed to correct the residual distortions in the post-equalization latent space. The key idea is to formulate the two cascaded inverse problems of channel estimation and equalization as the unified conditional restoration task, in which the learned conditional velocity field guides the perturbed distribution towards the target distribution. To enhance the robustness of these two modules under various distortion conditions, we develop a dual-anchor perturbation training strategy that jointly learns near-manifold refinement and large-error correction, and implement inference through a few-step deterministic ordinary differential equation (ODE) solver. Extensive experiments on MIMO channels and visual semantic transmission tasks demonstrate that the proposed scheme improves key metrics for channel estimation and semantic reconstruction quality. Moreover, compared with representative diffusion-based generative baselines, the proposed method requires fewer sampling steps.

---


### 230. [Optimal Reward Shaping: Autonomous Car Parking Case Study](https://arxiv.org/abs/2607.23617)

**<font color=#1a73e8>作者：</font>** Emre Özkaya, Nicolas R. Gauger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing effective reward functions for model-free reinforcement learning under non-holonomic constraints remains a persistent challenge, often resulting in severe local minima such as policy paralysis or over-conservative hazard avoidance. In this work, we present a parameterized reward shaping framework featuring coverage-gated alignment feedback, drive-direction switch regularization, and an aligned episode termination mechanism evaluated on an autonomous parallel parking task. Crucially, we show that environmental reward parameters and algorithmic hyperparameters are deeply co-dependent, requiring joint meta-optimization to achieve stable convergence. By employing surrogate-based Bayesian optimization, our co-optimized Deep Q-Network (DQN) agent resolves characteristic control failure modes, significantly outperforming uncalibrated baselines across both success rate and trajectory smoothness.

---


### 231. [GEMCo: A Validated, Ethically Releasable Proxy for Inaccessible Counselling Data](https://arxiv.org/abs/2607.23621)

**<font color=#1a73e8>作者：</font>** Philipp Steigerwald, Eric Rudolph, Mara Stieler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents GEMCo, a releasable, human-written proxy for inaccessible counselling data: 86 complete German e-mail counselling conversations (728 messages), expert-authored cases and counsellor sessions with trained role-players. It is validated against a held-out reference of 124 real counselling conversations. The proxy and the real conversations are measured against each other in counsellor strategies and client emotions. The gap is detectable but small. A generative validation supports the analysis. The validation method itself generalises to any domain where real data cannot be shared but a human-made proxy can. Privacy and ethics keep real counselling data closed. GEMCo carries none by design and can be released -- a first step toward language research in this domain.

---


### 232. [Variational-Ising-Attention (VIA):TailoredAttentionMattersfor Science](https://arxiv.org/abs/2607.23634)

**<font color=#1a73e8>作者：</font>** Rui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention enables context modeling via query-key scoring with softmax normalization. Driven by industrial long-context demands, mainstream research has converged toward sparsity and efficiency--yet softmax's independence assumption persists. For scientific tasks unburdened by long-token constraints, however, richer structured coupling may often be essential, making tailored attention both viable and more appropriate. To this end, we propose Variational-Ising-Attention (VIA), which augments softmax normalization with an interacting Ising model; attention patterns emerge from learnable pairwise couplings via variational mean-field inference, redefining attention from a ranking over isolated items to a collective state over interacting entities. We instantiate VIA on retrosynthesis reaction center prediction, a task inherently governed by cooperative bond-breaking constraints. Comprehensive experiments across model variants, coupled with mechanistic analyses, demonstrate that VIA consistently and substantially outperforms standard softmax attention. More broadly, our findings suggest that for scientific problems, the optimal solution is not general-purpose efficiency, but appropriately tailored attention aligned with intrinsic domain structure. This work provides a theoretically grounded and empirically validated instantiation of this paradigm.

---


### 233. [WGDnet: Wishart-guided Geometric-aware Deep Network for PolSAR Image Classification](https://arxiv.org/abs/2607.23638)

**<font color=#1a73e8>作者：</font>** Junfei Shi, Haojia Zhang, Yu Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Polarimetric Synthetic Aperture Radar (PolSAR) classification underpins all-weather Earth observation. Conventional Wishart methods depend on rigid handcrafted operators with limited adaptability, while mainstream deep networks ignore PolSAR native Wishart scattering statistics. Additionally, fixed convolution windows fail to capture multi-scale, multi-directional terrain patterns, harming boundary detection and small-object characterization. To mitigate these drawbacks, we propose WGDNet, a Wishart-guided geometric-aware deep network. It integrates three core designs: (1) learnable Wishart convolutions with directional kernels for multi-scale statistical edge feature extraction; (2) an orientation-prior aggregation module that estimates dominant local directions and confidences to refine directional Wishart outputs adaptively; (3) GAnet, a scale-direction adaptive geometric-aware convolution that dynamically reshapes sampling grids to model anisotropic terrain and retain fine details. Our contributions lie in learnable Wishart statistical modeling, orientation-prior feature aggregation, and geometry-adaptive convolution. Evaluations across four real PolSAR datasets verify WGDNet surpasses existing state-of-the-art approaches in classification accuracy and boundary fidelity.

---


### 234. [EmoTrace: An Emotion Trajectory-Centered Framework for Psychological Support Dialogue Generation](https://arxiv.org/abs/2607.23648)

**<font color=#1a73e8>作者：</font>** Kaitong Weng, Lixin Liu, Zihao Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Using large language models (LLMs) to assist psychological counseling is an important task in the field of natural language processing. The construction of high-quality psychological support dialogue corpora serves as a critical foundation for training counseling-oriented conversational models. However, existing data generation approaches generally suffer from several limitations, including emotionally stable seekers, limited variation in emotional dynamics, and a high degree of compliance with counselors' guidance. These issues result in LLM that lack the capability to effectively respond to emotionally unstable scenarios. In addition, counselor responses are typically driven by problem-solving objectives, thereby overlooking the role of emotion-focused interaction, which are essential in psychological counseling. To address these gaps, we propose EmoTrace, a multi-turn dialogue corpus generation framework centered on modeling seekers' emotional trajectories. we construct seekers' cognitive profile and introduce a seeker module with emotional schemas and an associated activation mechanism, a counselor module, and an emotional trajectory control module, thereby enhancing the layering of the seeker's emotional expression and the counselor's targeted empathic expression. Experimental results demonstrate that the proposed method outperforms existing approaches in terms of emotional richness and empathy quality.

---


### 235. [DP-IVON-Gradsq: Differentially Private Squared-Gradient Improved Variational Online Newton](https://arxiv.org/abs/2607.23649)

**<font color=#1a73e8>作者：</font>** Nour Jamoussi, Ikram Dridi, Giuseppe Serra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differential privacy provides formal privacy guarantees for training neural networks on sensitive data, while Bayesian deep learning offers a principled framework for uncertainty-aware prediction. Combining these two objectives remains challenging, as privacy noise can interact with the stochasticity introduced by Bayesian posterior sampling. In this work, we investigate differentially private variational Bayesian learning through the Improved Variational Online Newton (IVON) optimizer. We introduce DP-IVON-Gradsq, a private variant of IVON. The proposed method constructs its curvature estimate from the privatized gradient using a noise-corrected squared-gradient estimator, reducing the direct interaction between posterior-sampling noise and privacy noise while preserving the Adam-like computational efficiency of IVON. We evaluate DP-IVON-Gradsq on CIFAR-10 against the standard private optimizers DP-SGD and DP-Adam over a range of privacy budgets. The results show that DP-IVON-Gradsq is competitive under weak-to-moderate privacy constraints, i.e., large-to-moderate values of $\varepsilon$, while degrading under strong privacy. Code is available at this https URL.

---


### 236. [GRAPE: Graduated Routing for Articulated Portrait mesh Estimation](https://arxiv.org/abs/2607.23657)

**<font color=#1a73e8>作者：</font>** Yunfei Liu, Lijian Lin, Ye Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Articulated portrait mesh estimation is fundamental to 3D understanding, avatar generation, and immersive interaction. Existing approaches primarily rely on 3D Morphable Models (3DMMs). However, face-centric models suffer from the "floating head" assumption, conflating head pose with global rotation due to the lack of neck kinematics. Conversely, body-centric models lack high-fidelity facial expression capabilities. Furthermore, current methods struggle to disentangle jaw articulation from expression blendshapes, often over-relying on expressions for mouth opening. These limitations make monocular portrait recovery difficult across representation, supervision, and anatomical parameter estimation. To address these limitations, we introduce GRAPE(Graduated Routing for Articulated Portrait mesh Estimation). We build a Portrait Parametric Model (PPM) with an explicit torso-to-head kinematic chain and a canonical injection step to merge FLAME and the SMPL-X torso. We propose a Progressive Anatomical Alignment (PAA) network, which is composed of a pretrained portrait encoder, a Graduated-Mask Router, and coarse-to-fine experts that follow the portrait anatomical prior. We then train this network with multi-source supervision that combines sparse anatomical keypoints, feature distillation, foreground mask constraints, and relative geometry constraints. Experiments show that GRAPE improves portrait mesh recovery quality, pose alignment, and jaw--expression disentanglement over prior methods. We also demonstrate that our method can benefit the downstream tasks of audio-driven talking-head generation and 3D portrait generation.

---


### 237. [XMatchAD: A Cross-Modal Matching Perspective on Reconstruction-based Anomaly Detection](https://arxiv.org/abs/2607.23658)

**<font color=#1a73e8>作者：</font>** Mingxiu Cai, Zhe Zhang, Gaochang Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The remarkable success of reconstruction-based methods in Unsupervised Anomaly Detection (UAD) lies in their ability to identify and localize anomalies by modeling discrepancies between input images and their reconstructed counterparts. However, these approaches often struggle to capture subtle anomalies and tend to produce blurred anomaly boundaries, which significantly limits their effectiveness, particularly in complex multi-class scenarios. To address these issues, we present XMatchAD, a novel UAD framework that reinterprets the task from a pseudo cross-modal matching perspective. Specifically, the input and reconstructed images are treated as two complementary modalities and their matching relationships are precisely exploited for anomaly detection. First, a pre-trained feature extractor is employed to encode discriminative representations. Second, an attention-guided cross-modal matching mechanism is introduced to match local inter-modal anomaly-related patterns while mutually refining the features. This enhances the sensitivity to anomalies with diverse shapes and subtle deviations and significantly improves the precision of anomaly detection and localization. Third, we design an adaptive frequency-aware fusion module that further delineates sharp anomaly boundaries through the coupling of high-frequency components from cross-modal multi-scale representations. Comprehensive evaluations on MVTec-AD, VisA, and MPDD benchmarks demonstrate that our method consistently achieves superior performance, outperforming state-of-the-art methods in multi-class anomaly detection and localization. The code will be released at this https URL.

---


### 238. [RRTrack: Robust and Recoverable Object 6D Pose Tracking for Dynamic Scenes](https://arxiv.org/abs/2607.23669)

**<font color=#1a73e8>作者：</font>** Junyue Li, Ye Zheng, Yifan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust object 6D pose tracking is critical for robotic systems operating in dynamic and occluded scenes. Per-frame estimators are accurate but computationally expensive, while current trackers struggle with fast motion and complete occlusion due to their reliance on continuous visibility. To address these challenges, we present RRTrack, an efficient, recoverable object 6D pose tracker that enables robust tracking through fast motion and target disappearance--reappearance. RRTrack introduces a 2D--6D closed-loop tracking strategy that integrates memory-based video object segmentation (VOS) with 6D pose refinement. The 2D branch maintains target localization, and the 6D branch verifies geometric consistency before memory updates. In addition, a DINOv2-based dual-bank template matching module is developed to recover lost targets by jointly exploiting offline synthetic templates and online observation anchors while maintaining real-time efficiency. We also introduce a synthetic RGB-D benchmark comprising three robotic scenarios with fast motion and full occlusion. Experimental results on the synthetic benchmark demonstrate that RRTrack improves equal-subset mean ADD-S AR by 66.3\% and ADD-S AUC by 65.7\% over FoundationPose while achieving 55.2 FPS. Real-world experiments further validate the robustness of RRTrack under noisy sensing conditions. Project page: this https URL

---


### 239. [Plans Work in Mysterious Ways: Evaluating a Plan Mode for Spreadsheet Agents](https://arxiv.org/abs/2607.23670)

**<font color=#1a73e8>作者：</font>** Aayush Kumar, Avik Dutta, Sumit Gulwani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Plan Modes have become standard features in agentic programming tools, allowing users to gain transparency and control by working with the agent to develop a plan before task execution. However, it remains unclear whether the benefits of this feature translate to end-user programming environments such as spreadsheets. Since spreadsheet programmers tend to work iteratively and care less about technical correctness, upfront planning may not fit into their workflows as easily. In this paper, we build a prototype of a Plan Mode for spreadsheet programming and evaluate it against a non-planning baseline through a within-subjects user study (N=24). We found that despite similar task outcomes with both tools, using Plan Mode led to a reduction in refinement and a better perception of the tool across dimensions of creativity support and human-machine collaboration. We discuss the implications of these results for the future design of Plan Modes, and for the broader role of human-AI planning in end-user programming.

---


### 240. [Contrastive Parameter Disentanglement for Multi-modal Remote Sensing Image Generation](https://arxiv.org/abs/2607.23673)

**<font color=#1a73e8>作者：</font>** Yu Zhang, Wenda Zhao, Haojun Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing remote sensing image generation methods are largely confined to single-modality synthesis and therefore fail to exploit the complementary information inherent in multimodal imagery. To address this limitation, we propose a contrastive parameter disentanglement framework for multimodal remote sensing image generation, which generates semantically consistent and structurally aligned images across multiple modalities, including optical, infrared, and synthetic aperture radar (SAR), from a single text prompt. Specifically, we introduce a contrastive parameter disentanglement module that disentangles shared semantics from modality-specific attributes at the parameter level within an orthogonal core subspace. Based on this module, we develop a disentangled optimization strategy that first constrains the parameter matrix A of the LoRA adapter to capture modality-invariant semantics through a multimodal contrastive objective and then guides multiple parameter matrices B to learn modality-specific attributes under text conditioning. This strategy enables the simultaneous generation of multimodal images with consistent semantic content and distinct modality characteristics. Furthermore, to ensure structural alignment across the generated images, we devise a query-key structure transfer mechanism that jointly models multimodal sampling trajectories during inference by transferring structural correlation priors from an anchor modality to the remaining modalities. Extensive experiments demonstrate that our method outperforms state-of-the-art remote sensing image generation approaches in terms of generation quality, semantic consistency, and structural alignment, while also achieving superior performance in the downstream object classification task.

---


### 241. [An empirical investigation into the properties of standard word embeddings](https://arxiv.org/abs/2607.23675)

**<font color=#1a73e8>作者：</font>** Salomon Kabongo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The embedding of word sequences into continuous vector spaces has been one of the most important developments in Natural Language Processing in the recent past. Such embeddings have found application in areas such as Automatic Speech Recognition, Machine Translation, Sentiment Analysis and many more. This essay reviews the various mechanisms that have been proposed for the calculation of word embeddings, investigates popular toolkits and embedding matrices that are available in the public domain, and experiments with one or more selected implementations to better understand their characteristics.
La représentation vectorielle continue de mots a été l'un des développements les plus importants dans le domaine du traitement automatique du langage naturel au cours des dernières années. Ces représentations ont trouvé application dans des domaines tels que la reconnaissance vocale, la traduction automatique, l'analyse des sentiments, etc. Ce travail passe en revue les différents mécanismes proposés pour le calcul de ces vecteurs de mots, étudie les kits d'outils populaires et les matrices disponibles publiquement en ligne, et expérimente avec une ou plusieurs implémentations sélectionnées pour mieux comprendre leurs caractéristiques.

---


### 242. [SpecAHD: Localize to Specialize for Automated Heuristic Design in Large-Scale Routing Problems](https://arxiv.org/abs/2607.23676)

**<font color=#1a73e8>作者：</font>** Kezhao Lai, Yutao Lai, Hai-Lin Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based automated heuristic design (AHD) typically scores executable programs on complete instances or within fixed solver components. In large-scale routing problems, localized reconstruction reduces the size of each optimization task, but repair regions within the same incumbent can exhibit substantially different structures. One construction rule must therefore compromise across them. In this paper, we propose SpecAHD, a coupled bilevel framework for within-instance specialization. An upper-level search learns where to expose bounded repair regions, while a lower-level search evolves a complementary repertoire of executable heuristics for the induced repair tasks. The upper-level program determines the repair tasks seen by the lower level, while checked repair outcomes determine how upper-level programs are evaluated. The lower-level objective favors heuristics that perform well on average or solve tasks that the current repertoire handles poorly. For the repair tasks induced by a fixed upper-level program and a fixed lower-level candidate pool, this objective is monotone submodular, allowing greedy repertoire selection with a (1-1/e) approximation guarantee. Across four routing problems and multiple LLM backbones, SpecAHD reduces held-out objective cost by up to 57.7% against the strongest competing AHD baseline and outperforms the per-instance baseline envelope on most public instances.

---


### 243. [Breaking the Total Variance Barrier: Sharp Sample Complexity for Linear Heteroscedastic Bandits with Fixed Action Set](https://arxiv.org/abs/2607.23679)

**<font color=#1a73e8>作者：</font>** Heyang Zhao, Tianyuan Jin, Weixin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed increasing interests in tackling heteroscedastic noise in bandits and reinforcement learning. In these works, the cumulative variance of the noise $\Lambda = \sum_{t=1}^T \sigma_t^2$, where $\sigma_t^2$ is the variance of the noise at round $t$, is used to characterize the statistical complexity of the problem, yielding \emph{simple regret} bounds of order $\tilde{\cal{O}}(d \sqrt{\Lambda / T^2})$ for $d$-dimensional linear bandits with heteroscedastic noise. However, with a closer look, $\Lambda$ remains the same order even if the noise is close to zero at half of the rounds, which indicates that the $\Lambda$-dependence is not optimal. In this paper, we revisit the stochastic linear bandit problem with heteroscedastic noise, where the action set is prefixed throughout the learning process. We propose a novel variance-adaptive algorithm \texttt{VAEE} (Variance-Aware Exploration with Elimination) for large action set, which actively explores actions that maximizes the information gain among a candidate set of actions that are not eliminated. With the active-exploration strategy, we show that \texttt{VAEE} achieves a \emph{simple regret} with a nearly \emph{harmonic-mean} dependent rate. For finitely many actions, we propose a variance-aware variant of G-optimal design based exploration, which achieves a simple regret with sharper dependence on $d$. We also establish a nearly matching lower bound for the fixed action set setting indicating that \emph{harmonic-mean} dependent rate is unavoidable. To the best of our knowledge, this is the first work that breaks the $\sqrt{\Lambda}$ barrier for stochastic linear bandits with heteroscedastic noise.

---


### 244. [Perturbation-Aware Diffusion-Guided Hybrid Segmentation for Robust and Annotation-Efficient Plant Stress Phenotyping](https://arxiv.org/abs/2607.23680)

**<font color=#1a73e8>作者：</font>** Gurbhit Chaurakoti, Soumyashree Kar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation in agricultural imagery is often evaluated under in-domain protocols, yet practical deployment requires robustness to appearance perturbations, limited annotations, and cross domain shift. This paper presents a diffusion-guided hybrid segmentation framework in which U-Net, DeepLabV3+, and SegFormer backbones generate coarse masks that are refined by Denoising Diffusion Probabilistic Models (DDPM), latent diffusion, or semantic-guided diffusion. The framework is evaluated through a 3x3 architectural screening study on PlantSegV3, followed by boundary-constrained optimization, perturbation-guided retraining, low-data evaluation, constrained hyperparameter screening, and controlled cross-domain adaptation. On PlantSegV3, the best selected hybrid model achieves 71.83% refined mean Intersection-over-Union (mIoU) and 26.10% refined Boundary-F1, and the selected models remain stable under substantially reduced supervision, demonstrating strong annotation efficiency. Perturbation analysis identifies grayscale conversion, fog, coarse dropout, and shadow as the most disruptive appearance shifts, and the resulting augmentation policy substantially improves robustness during retraining. The adapted models further show effective transfer to external agricultural datasets under limited target supervision, indicating that diffusion refinement and boundary-aware optimization provide transferable structural priors. Overall, the results show that carefully matched backbone-refiner pairings, combined with perturbation-aware retraining, can improve structural delineation and robustness under realistic resource and distribution constraints.

---


### 245. [Extreme Volatility Warning under Label Scarcity via Multi-Source Anomaly Fusion](https://arxiv.org/abs/2607.23682)

**<font color=#1a73e8>作者：</font>** Jin Qian, Zhangzhi Xiong, Mingrui Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early warning of extreme market volatility is central to financial risk management, but actionable events are rare, nonstationary, and often triggered by exogenous information shocks. In our CSI~300 setting, only $\sim$80 positive samples are observed across 791 training days, making heavily supervised multi-source models unstable. We first analyze a 100K-parameter hierarchical text-signal fusion model (HTSF) and find that added parameterization hurts in this low-label regime. Motivated by this failure, we propose \textbf{AAMSF} (Anomaly-Augmented Multi-Signal Fusion), a semisupervised framework that combines Isolation Forest anomaly scores over market indicators, GDELT events, Chinese financial news, and English media with lightweight Ridge score fusion. We further introduce \textbf{T-AAMSF}, a temporal extension for multi-day anomaly accumulation. On CSI~300 (2018--2023), AAMSF achieves test AUC-ROC \textbf{0.680}, outperforming the strongest unsupervised baseline (0.630) and neural baseline (0.588), while T-AAMSF improves PR-AUC to 0.291. Ablations reveal strong source asymmetry: GDELT and domestic financial news provide complementary risk signals, whereas English media consistently reduces performance, and learned weighting is unreliable under validation noise. These results suggest an empirical design principle for label-scarce financial risk warning: robust anomaly geometry and source reliability can matter more than supervised representation capacity.

---


### 246. [GNM Head: A Generative aNthropometric Model of the human head](https://arxiv.org/abs/2607.23687)

**<font color=#1a73e8>作者：</font>** Stylianos Ploumpis, Jan Bednarik, Gaspard Zoss 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parametric models of the human head are essential tools traditionally used in computer vision and graphics for animation, rendering, and reconstruction. More recently, they serve as crucial conditioning signals within generative large vision models, allowing for tight spatial control of generated imagery. However, existing publicly available models are typically limited in anatomical scope, modeling only outer geometry while ignoring intra-oral and ocular structures, and frequently suffer from reduced geometric quality stemming from low-fidelity input datasets. In this report we introduce a new parametric model dubbed Generative aNthropometric Model (GNM), named as a homophone of the human genome. GNM encompasses the head, face, neck, eyeballs, teeth, and tongue, and it is built on an extensive database of high-resolution 3D scans combined with high-quality anatomy specific artist-made samples. This report details the data provenance, the model architecture including the specialized sub-models for the ocular and intra-oral structures, and shows its SotA performance on fitting target 3D face scans. To foster community innovation, the complete GNM framework is made publicly available.

---


### 247. [Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV](https://arxiv.org/abs/2607.23693)

**<font color=#1a73e8>作者：</font>** Zefeng Cai, Zerui Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents increasingly reuse their KV cache as memory: a serving system keeps a subset of cached entries and drops the rest. Eviction and episodic-memory schemes therefore rest on a premise rarely tested directly, that a retained event is still informative once the observations that produced it are gone. We test it by omitting one earlier observation from what is served, across otherwise identical agent histories. Among items sensitive to that observation, the answer overwhelmingly follows the omitted value, though no served span says which value is correct. We call this semantic materialization: a downstream event's cached rows act as an independently servable view of computation whose inputs are gone. It can also be written on purpose. A deliberately phrased, answer-free event raises donor-aligned recovery from 6% to 51% on Qwen3-8B without ever naming the value, whereas passively harvesting natural mentions from long-term dialog yields no detected advantage. What such a row carries is specific and bounded. Compact state survives, larger payloads decay toward chance, and whether a construction writes at all turns on phrasing rather than on meaning alone, so two phrasings the model comprehends equally well can diverge sharply. The result is a memory contract for sparse event-KV serving: what to write, where it lands, and what survives once the source is gone. For anyone who evicts the corollary is that dropping a source event and observing no accuracy loss does not show the source was unnecessary.

---


### 248. [Parameter-Efficient Adaptation of SAM3 for Prompt-Driven Surgical Concept Segmentation](https://arxiv.org/abs/2607.23694)

**<font color=#1a73e8>作者：</font>** Changjing Liu, Yiming Huang, Beilei Cui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient surgical segmentation empowers clinical diagnosis, intraoperative monitoring, and downstream robotic pipelines for reconstruction and simulation. Although prompt-driven foundation models like Segment Anything Model 3 (SAM3) achieve strong segmentation performance on natural images, surgical data exhibits domain gaps against its pre-training data, resulting in degraded segmentation accuracy. Furthermore, existing medical SAM methods require full-parameter fine-tuning, incurring heavy computational consumption and low efficiency. To address these limitations, this work proposes a parameter-efficient Low-Rank Adaptation (LoRA) adaptation of SAM3 for surgical concept segmentation. We inject low-rank adapters into the prompt encoder, detector and tracker while fully freezing the vision backbone, which only optimizes 0.98% of the total model parameters and supports training on a single consumer GPU. Comprehensive experiments demonstrate that our method consistently outperforms zero-shot SAM3 and other mainstream baselines, and the generated segmentation results can be directly deployed to support downstream robotic surgical scene reconstruction and physical simulation pipelines.

---


### 249. [Offline-to-Online Creative Optimization with Generative Models and Adaptive Testing](https://arxiv.org/abs/2607.23696)

**<font color=#1a73e8>作者：</font>** Kevin Lee, Benjamin Letham, Zhiyuan Jerry Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ad creative optimization is increasingly constrained by evaluation rather than generation. Generative models can produce many plausible creatives, but reliable evaluation requires online experiments, in which only a limited slate can be tested. We study how to use data from historical A/B tests to generate and select the candidates in that slate. We developed and deployed a performance-driven offline-to-online workflow that guides creative generation with a predictive model as an inference-time critic. In the offline phase, we use a predictive model trained on historical experiments to rank and refine variants created by a generative model. A final test slate is then deployed in an online adaptive experiment. In a 50-arm field experiment, we found that the best creative generated with this method yielded 45.1% higher engagement than the best human-authored creative. Two additional experiments showed the same upper-tail pattern, with lifts of 46.7% and 36.2%. We found that despite the predictive model being too noisy to directly identify the best creative offline, it effectively guides the generative model toward creating strong candidates that can be efficiently evaluated in an adaptive experiment. The results suggest a design principle for creative optimization with generative models: use predictive models to guide generation of a slate to test, judge the slate by whether it contains high-performing candidates at a feasible test size, and use adaptive experiments to select among candidates while limiting traffic lost to weak arms.

---


### 250. [SMARM+: Analyzing and Enhancing Shuffled Measurements for Remote Attestation in Real-Time IoT Settings](https://arxiv.org/abs/2607.23698)

**<font color=#1a73e8>作者：</font>** Amarin Laohajirapan, Norrathep Rattanavipanon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Remote attestation (RA) is a lightweight security primitive for detecting software compromise on IoT devices. Traditional RA schemes require atomic, non-interruptible memory measurements, making them difficult to deploy alongside real-time workloads. SMARM addresses this limitation by measuring memory in a secret, shuffled block order, reducing the non-interruptibility period to the duration of a single block measurement. However, SMARM was originally designed for microkernel-based systems and has not been studied in RTOS-driven real-time environments.
In this work, we present the first systematic study of SMARM in real-time RTOS-based setups. We implement SMARM on commodity ARM TrustZone-M hardware running FreeRTOS and Zephyr, and introduce the Frequency Accuracy Ratio (FAR) to quantify the extent to which attestation can coexist with real-time execution under varying workloads. Our evaluation shows that SMARM's real-time compatibility is highly sensitive to block size: large blocks significantly degrade real-time availability, while small blocks incur substantial secure-storage overhead, limiting deployability on memory-constrained devices.
To address this limitation, we propose SMARM+, a family of enhanced SMARM variants consisting of SMARM+PRNG and SMARM+FPE. They are designed to reduce secure-storage requirements while preserving SMARM's security guarantees and real-time behavior. Our evaluation highlights the trade-off between secure-storage reduction, attestation runtime, and energy overhead, and provides guidance on selecting among SMARM, SMARM+PRNG, and SMARM+FPE for different deployment settings.

---


> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-442](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
