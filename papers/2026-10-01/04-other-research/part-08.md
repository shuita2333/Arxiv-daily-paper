# 📦 其他研究 | 2026年10月01日

> 本类共 **447** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-447](./part-09.md)

---

### 351. [Beyond a single latent space: a dual-latent world model for long-horizon planning](https://arxiv.org/abs/2609.37644)

**<font color=#1a73e8>作者：</font>** Delin Zhao, Zhengrong Yue, Shaobin Zhuang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent world models often struggle with long-horizon planning despite accurate short-term predictions. Recursive rollouts accumulate errors, while distance concentration in high-dimensional latent spaces can weaken goal discrimination. We introduce the Dual-Latent World Model (Dual-WM), which separates local execution and long-range planning through distinct state representations and dynamics models. The low-level model predicts action-conditioned transitions, while the high-level model uses learned macro-actions to plan over longer temporal spans. We also propose Long-Horizon Representation Learning with Weighted Rollout (LoRe), which supervises self-generated predictions at both levels. An analysis of recursive error propagation motivates exponential horizon weights with separate decay rates for the two temporal scales. During planning, the high-level model generates latent subgoals that the low-level model refines into actions for precise execution. We evaluate from-scratch Dual-WM on five goal-conditioned visual control tasks against the task-wise strongest baselines without actor-guided proposals. At goal offsets of 50 and 100 environment steps, mean success increases from 75.9% to 84.4% and from 61.4% to 69.5%, respectively. At offset 100, Dual-WM outperforms these baselines on all five tasks and improves mean success over LeWM by 30.8 percentage points. Ablations and supporting analyses provide evidence of more informative representations for goal evaluation and greater consistency under recursive prediction. These results highlight the value of separating temporal roles and training across multiple horizons for reliable latent planning. Our core implementation is available at this https URL.

---


### 352. [RACE: Relation-Level Counterfactual Explanations for Heterogeneous Graph Neural Networks](https://arxiv.org/abs/2609.37650)

**<font color=#1a73e8>作者：</font>** Yuxiang Yao, Zijun Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations of graph neural networks identify edge deletions that flip a prediction. On heterogeneous graphs, however, existing methods first collapse the graph into untyped edges, so they cannot answer the question a domain expert actually asks: which relation type drives this prediction? We present RACE (Relation-Aware Counterfactual Explanations), which gives this question an exact, per-instance answer. For every explained instance, an exhaustive search over relation subsets returns the certified minimum relation-deletion set that flips the prediction -- or an explicit report that no such deletion exists; each relation-level answer is then refined into a typed edge set within the attributed relations, verified on the discrete model by single-edge restoration. The relation-level answer is exact and deterministic given the frozen backbone, whereas soft-mask baselines vary by 6-8 pp in success rate across runs differing only in random ordering. On ACM, a Cora-derived graph, and ogbn-mag, RACE improves counterfactual success rate over the strongest baseline by up to +2.7 pp while deleting fewer edges, and attains the highest success rate among all same-task baselines on every dataset; the advantage reproduces across four backbones on ogbn-arXiv and on DBLP, with cross-seed relation-set agreement up to 0.89. A synthetic study with known generating mechanisms confirms that the search recovers the relation the trained model actually relies on -- and reports infeasibility rather than fabricating an attribution when the model has learned none -- so the explanations stay trustworthy exactly where explanations matter.

---


### 353. [Texture Space Material Diffusion](https://arxiv.org/abs/2609.37654)

**<font color=#1a73e8>作者：</font>** Jacob Munkberg, Peter Kocsis, Jon Hasselgren  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a method for generating high quality materials for 3D objects entirely in texture space. We finetune a video diffusion transformer for text-guided material generation, multi-view material generation, and material upscaling. Our key insight is to use the known projection from image space to texture space, enabling the diffusion process to generalize across arbitrary geometries and texture parameterizations. This approach also avoids the view consistency issues inherent in video and multi-view diffusion models. Because texture space is two dimensional, we can reuse the strong priors of pretrained video diffusion models. We apply our method to high quality material reconstruction from posed photos captured under unknown lighting, as well as to text- and image guided material generation. Our method can scale to high resolutions (8K), 100+ input views, and neural material representations. In quantitative and qualitative evaluations we show state-of-the-art results for material generation and reconstruction.

---


### 354. [Nonpreemptive Scheduling While Learning Context-Dependent Service Rates](https://arxiv.org/abs/2609.37660)

**<font color=#1a73e8>作者：</font>** Wansoo Choi, Seoungbin Bae, Dabeen Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study nonpreemptive contextual queueing bandits in a single-server system. Each job is represented by a $d$-dimensional context vector; in each round, a job may arrive with its context drawn from an unknown distribution $\mathcal{D}$, and its departure probability is determined by a logistic model of that context vector with an unknown parameter $\theta^*$. The server learns from service outcomes while deciding which waiting job to serve and whether to idle, aiming to minimize queue-length regret, the gap between its expected terminal queue length and the minimum achievable by an admissible policy. Once selected, a job must be served until completion, and we refer to this as the nonpreemptive setting. A central challenge is that, even with full model knowledge, the optimal policy cannot in general be characterized by a simple myopic rule, since the optimal action can change with the remaining horizon at the same queue state. Nevertheless, when the model and horizon are known, the optimal action can be obtained through a finite-horizon Bellman recursion. Motivated by this, we propose Learn--Clear--Plan (LCP), which estimates the system and uses the resulting Bellman recursion to make horizon-dependent decisions. LCP achieves $\widetilde{O}(\sqrt{d/T})$ queue-length regret, while a lower-bound construction gives $\Omega(\min\{1/\sqrt{d},\sqrt{d/T}\})$ regret for every learning policy on some instance, establishing optimality up to polylogarithmic factors when $T\ge d^2$. When the horizon is unknown, no horizon-independent policy achieves vanishing regret against the finite-horizon optimum. We therefore use SEPT, the policy that serves a waiting job with the highest probability of departure, as a fixed reference, and suggest an estimated-SEPT algorithm that achieves a tracking error of $\widetilde{O}(\sqrt{d/t})$ without knowing the model.

---


### 355. [Learning Causal Normalizing Flows from Incomplete Data via Observed-Data Likelihood](https://arxiv.org/abs/2609.37664)

**<font color=#1a73e8>作者：</font>** Trung-Dung Hoang, Alceu Bissoto, Tim Flühmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal Normalizing Flows (CNFs) enable causal inference from observational data given the causal structure, but they assume fully observed training data. We introduce MissCNF, which trains CNFs directly on incomplete data by maximizing the marginal likelihood of each partially observed sample, without discarding rows or constructing a completed dataset. Thanks to the causal structure encoded in the autoregressive factorization of CNFs, only missing variables in the ancestral closure of the observed set are integrated out, while the others are dropped without computation. We further establish the conditions under which MissCNF recovers the true joint distribution, and introduce \emph{causal-family positivity}, where identification is possible even when no record in the dataset is ever complete. We compare MissCNF with two common strategies for handling missing data: listwise deletion and impute-then-fit pipelines. Across eight synthetic causal benchmarks, three missingness mechanisms, and missing rates up to $90\%$, MissCNF achieves the lowest KL divergence in 23 of 24 nonlinear MCAR and MAR settings and in all nonlinear MNAR settings, as well as the lowest counterfactual error in 20 of 24 settings. On linear SCMs, where linear imputation performs best, MissCNF ranks in the top two in 22 of 24 settings.

---


### 356. [Where Privacy Belongs: Placement Diagnosis and Certified Selection for Private Counterfactual Explanations on Graphs](https://arxiv.org/abs/2609.37667)

**<font color=#1a73e8>作者：</font>** Yuxiang Yao, Zijun Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations for graph neural networks (GNNs) find the minimal intervention that flips a node's prediction--but computing one requires reading sensitive graph structure, and releasing it discloses that structure. Both existing placements fail. Privatizing the graph before explaining corrupts the target on exactly the borderline nodes needing recourse, manufacturing spurious flips that flip the privatized graph but not the true one. Explaining on the clean graph and perturbing the released explanation resists certification: re-auditing the standard heuristic shows an implied full-release budget of 573--753 on Cora and 256 on CiteSeer--orders of magnitude beyond its advertised budget--with worst-case single-entry leakage at AUC 1.0. We propose PrivCFS, which replaces certification-by-optimization with certification-by-construction: counterfactual selection over a fixed, data-independent candidate universe--edge interventions from a public prior graph, feature interventions from a public schema--whose no-op semantics give neighboring graphs the same output support. A validity-gated, clipped utility of global sensitivity $\Delta u \le 1$ released through the exponential mechanism gives pure $\varepsilon$-DP for the complete released object, composable over queries--to our knowledge the first such guarantee on graphs. Privacy noise is the cheapest stage: at $\varepsilon$=8 the release retains 94--97% of its support-restricted non-private optimum on the recourse population and 83--95% on the general one; the optimal edge-inference audit attains AUC 0.50 on average and 0.59 worst-pair, versus the heuristic's worst entry 1.0; and transfers to a 15K-node graph at 0.96 valid rate. The dominant cost is a measurable, monotone price in public disclosure, readable off one table before any budget is spent--turning explanation privacy from an accounting risk into a purchasable decision.

---


### 357. [MeanFlowAdvantage: Stable Reward Fine-Tuning for Few-Step Average-Velocity Generators](https://arxiv.org/abs/2609.37670)

**<font color=#1a73e8>作者：</font>** Haocheng Tang, Tianchi Xie, Xingqiao Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> MeanFlow enables efficient few-step generation by predicting interval-average velocities, but this representation creates a mismatch for reward fine-tuning: existing advantage-based objectives are typically defined on instantaneous velocities or equivalent $x_0$-space predictions, whereas inference directly uses the learned average-velocity map. We introduce MeanFlowAdvantage, a signed advantage-weighted least-squares objective for average-velocity generators. Our key construction uses a shared, detached MeanFlow derivative correction to express the reward objective in prediction space while making rollout and reference regularization exact penalties on the average-velocity network deployed at inference. The resulting formulation preserves MeanFlow's native few-step sampler and provides a direct mechanism for transferring reward improvements to the deployed flow map. On SD3.5-Medium, MeanFlowAdvantage improves all eight reported metrics over the matched four-step MeanFlowNFT baseline and, with only four NFEs, matches or exceeds the 40-step DiffusionNFT baseline on six of eight metrics. The same objective also transfers to DNA promoter design, where it supports both teacher-free on-policy RL for a generator defined on a manifold and teacher-guided reward-graded distillation, with the latter yielding the lowest one-step Sei profile MSE among the compared configurations.

---


### 358. [She Spoofed Sea Ships by the Sea Shore: Measuring Large-Scale GPS Spoofing in Global Maritime Traffic](https://arxiv.org/abs/2609.37676)

**<font color=#1a73e8>作者：</font>** Anna Raymaker, Ryan Von Brock, Ryan Pickren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> GPS spoofing has emerged as a serious threat to maritime security, yet its global prevalence, persistence, and structure remain largely unmeasured. In this paper, we present the first large-scale measurement study of maritime GPS spoofing, using global Automatic Identification System (AIS) data, which contain the GPS coordinates broadcasted over time by ships across the world. We focus on large-scale regional spoofing, where external interference displaces many vessels across an area at once, leaving a recognizable signature of physically implausible motion correlated across ships; our motion-aware, marine-specific framework identifies this signature and grades the evidence for GPS spoofing in each region it finds. Applying our approach to AIS data from over 367,000 vessels collected between late November 2024 and early February 2025, we identify 31 persistent anomalous hotspots across high-traffic maritime regions, at least 22 of which show strong evidence of GPS spoofing, with spatial and temporal structure aligning with regional conflict and economic sanctions. Notably, our method found that the spoofing activity in the Red Sea responsible for the highly-publicized grounding of the 75,000-ton container ship, MSC Antonia, was ongoing months before the incident, which has not been previously documented. Similarly, we detected persistent spoofing in the Strait of Hormuz over a year before the 2026 Iran war brought commercial shipping through the Strait to near-standstill. Together, this work establishes GPS spoofing as a widespread, recurring, and measurable threat to global maritime navigation.

---


### 359. [Med-RADIO: Reducing All Medical Domains Into One via Multi-Teacher Distillation](https://arxiv.org/abs/2609.37682)

**<font color=#1a73e8>作者：</font>** Chu Zhang, Haoyu Jiang, Hongyuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of large-scale medical datasets and computational resources has driven significant progress in medical foundation models. Given the inherent heterogeneity of medical imaging modalities, current research mainly follows two paths: specialized models optimized for specific modalities, and generalist models designed to handle multiple modalities. However, medical generalist models suffer from both insufficient training data scale relative to natural image generalists and inadequate domain-specific depth relative to medical specialists. Empirically, generalist models establish a cross-modality performance baseline, while specialists define the performance ceiling within their respective domains. To elevate this baseline toward these ceilings, we propose Med-RADIO, a medical multi-teacher distillation framework that Reduces All Domains Into One by compressing complementary expertise from multiple domain-specific teachers into a unified medical vision foundation model. Our method curates both generalist and specialist teachers, allocates modality-aligned distillation streams to reorganize generalist pretraining data so it matches specialist domains, and uses a balanced loss to prevent any single teacher from dominating the distillation process. On internal and external classification benchmarks spanning five modalities, Med-RADIO improves over strong medical generalists under linear probing and remains competitive with representative specialists on most evaluated modalities. Code is available at this https URL.

---


### 360. [Learning from Shared-Control Overrides: Context-Driven Acceleration Profile Prediction for Personalized Overtaking](https://arxiv.org/abs/2609.37684)

**<font color=#1a73e8>作者：</font>** Ruizheng Xu, Lounis Adouane, Javier Ibañez-Guzmán 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adaptive Cruise Control (ACC) systems are typically calibrated for an average driver, often resulting in a mismatch between vehicle behavior and individual expectations during time-critical maneuvers such as highway overtaking. When the ACC is perceived as too conservative and inconsistent, drivers intervene through throttle overrides, providing implicit feedback on the system's behavior. This paper reframes these override actions as human-in-theloop supervisory signals and proposes a data-driven framework for personalized vehicle adaptation, termed Context-driven Personalized ACC (CoP-ACC). Rather than relying solely on end-to-end regression, which tends to over-smooth dynamic responses, we introduce a hybrid pipeline combining: (i) unsupervised hierarchical clustering to extract representative acceleration profiles from override events; (ii) a context classifier that maps pre-maneuver driving conditions to the appropriate profile; and (iii) a residual regressor that refines the selected profile into a smooth, personalized acceleration profile tailored to the immediate context. Evaluated on real-world public-road data against a withheld forced-ACC baseline, the approach demonstrates high reconstruction fidelity and generates acceleration profiles that tend toward the driver's expected behavior in potential override contexts. The results highlight the potential of learning from shared-control overrides to enable anticipatory, personalized ACC behavior, reducing manual interventions and improving ride comfort.

---


### 361. [EngiWorld: What Can Frontier Agents Deliver in Professional Engineering Environments?](https://arxiv.org/abs/2609.37686)

**<font color=#1a73e8>作者：</font>** Hongcheng Gao, Hailong Qu, Yu Lei 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents have made rapid progress in general-purpose computer use, but reliable automation of professional industrial engineering remains out of reach, as engineering workflows demand reasoning over geometric and physical constraints and dependencies preserved across software and design stages. We present EngiWorld, the first benchmark structured around the complete design loop: 1,301 expert-curated tasks spanning 6 engineering domains (CAD, CAE, CAM, BIM, EDA, and 3D visualization) and 26 professional software platforms, with both GUI and CLI interfaces and 6 task types ranging from software-selection to open-ended tasks. We further introduce an artifact-centric evaluation methodology built on a unified domain-verifier suite, which programmatically checks the geometric validity, physical feasibility, and rule compliance of final and intermediate artifacts, and scores quantitative design tasks continuously by specification attainment rather than binary success. Evaluation of seven frontier models reveals a substantial capability gap: the strongest model achieves an EngiScore of only 44.3, and just 3.6% of multi-software attempts succeed. EngiWorld provides the first rigorous foundation for measuring progress toward agents that operate professional engineering software end to end.

---


### 362. [WISE-ATTA: When to Ask for Labels in Budgeted Active Test-Time Adaptation](https://arxiv.org/abs/2609.37687)

**<font color=#1a73e8>作者：</font>** Muhammad Huzaifa, Lea Schönherr, Thorsten Eisenhofer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Active test-time adaptation (ATTA) improves robustness under distribution shift by updating a deployed model during inference while selectively querying supervision. However, most existing ATTA methods implicitly assume that supervision can be requested for every incoming test batch, which can incur substantial annotation cost over long test streams. In this work, we introduce \emph{budgeted ATTA} in which labels are available for only a fraction of test batches. This formulation shifts the central challenge from deciding \emph{what} to label within a batch to deciding \emph{when} supervision should be applied over time. To address this challenge, we propose a budget-aware approach \emph{WISE-ATTA} that allocates supervision over the test stream based on lightweight signals computed online, prioritizing periods where supervision is likely to be most useful. When a batch is selected for supervision, we further employ a drift-based sample selection criterion that targets samples exhibiting ongoing, unconverged adaptation dynamics, enabling effective updates from a single labeled example. We evaluate this approach on synthetic corruptions (ImageNet-C) and natural distribution shifts (ImageNet-R/K/A). Across settings, WISE-ATTA achieves competitive or improved performance compared to recent ATTA methods while requiring substantially fewer labels. Overall, we find that the timing of supervision is a key, yet underexplored, aspect of active test-time adaptation. Code: this https URL

---


### 363. [Honeycomb: Constant-Size Scene Memory Representation for Video World Models](https://arxiv.org/abs/2609.37690)

**<font color=#1a73e8>作者：</font>** Jack Wei Lun Shi, Kaichen Zhou, Haoyu Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models require persistent scene memory to maintain consistency during long-horizon video generation. Existing spatial memory systems accumulate RGB observations or latent features, causing storage requirements to grow as generation proceeds. We introduce **Honeycomb**, a video world model built on **HexMemory**, a compact low-rank representation that stores scene features in a fixed-size memory comprising six spatial and spatiotemporal planes. A feed-forward writer maps each newly generated video chunk to plane features. As the spatial coverage or temporal range expands, HexMemory warps the existing planes while preserving their dimensions, then integrates new features through confidence-weighted pooling and a learned residual correction. A reader retrieves latent features from HexMemory to condition subsequent video generation. Because the writer processes only observations from the latest chunk, Honeycomb avoids per-scene optimization and repeated processing of the full generation history. Experiments on WorldScore and RealEstate10K demonstrate strong video generation quality and robust consistency when revisiting previously observed regions, while maintaining constant feature-storage requirements throughout generation. Code and additional visualizations are available on our this https URL.

---


### 364. [GARDiff: Graph-Aligned Residual Diffusion for Probabilistic Multivariate Time-Series Forecasting](https://arxiv.org/abs/2609.37694)

**<font color=#1a73e8>作者：</font>** Rui Han, Min Yang, Xu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently shown strong potential for probabilistic multivariate time-series forecasting by modeling complex conditional distributions. Recent decoupled diffusion frameworks further separate forecasting into deterministic prediction and stochastic residual generation, making it natural to derive dependency graphs from deterministic representations and use them to guide residual diffusion. However, we show that this direct structural transfer is unreliable. Although deterministic-derived graphs encode useful global dependency priors, they exhibit substantial edge-level misalignment with residual dependency structures, introducing inaccurate or redundant conditions during residual generation. This reveals a previously overlooked deterministic-to-residual structural alignment problem in decoupled diffusion forecasting. To address this problem, we propose GARDiff, a Graph-Aligned Residual Diffusion framework for probabilistic multivariate time-series forecasting. Instead of treating deterministic-derived graphs as fixed diffusion conditions, GARDiff progressively adapts them to residual generation. Specifically, GARDiff estimates residual uncertainty to distinguish high- and low-uncertainty regions, enabling uncertainty-aware structural refinement, and further performs timestep-aware edge sparsification during reverse diffusion to evolve graph conditions from broad dependency aggregation to localized residual refinement. Extensive experiments on six real-world benchmarks demonstrate that GARDiff consistently improves probabilistic forecasting performance and uncertainty calibration over strong baselines.

---


### 365. [Width Expansion as a Method for Class Incremental Learning](https://arxiv.org/abs/2609.37702)

**<font color=#1a73e8>作者：</font>** A. L. S. Conde, Y. Elkhatib, C. M. Ranieri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class Incremental Learning (Class-IL) requires models to learn new classes over time while preserving previously acquired knowledge without access to past data or task identity. This setting intensifies the stability-plasticity dilemma and makes catastrophic forgetting a central challenge. Existing approaches include regularization, knowledge distillation, replay, and architectural expansion. However, many expansion methods rely on explicit task identifiers or predefined growth strategies, limiting their applicability when task boundaries are unavailable at inference time. This work proposes a dynamic width expansion method that increases the number of neurons within existing layers according to a normalized loss criterion, without requiring task-specific information. An attention mechanism with persistent key-value memory is also incorporated to stabilize feature representations and reduce interference between previously learned and newly introduced classes. The approach is evaluated on Split MNIST and Split CIFAR-100 under the standard Class-IL protocol. Experiments compare fixed-capacity and dynamically expanding architectures, both with and without attention, combined with established continual learning methods including EWC, LwF, and A-GEM. Results show that progressive width expansion consistently improves performance over fixed architectures, particularly when combined with functional methods and A-GEM. The combination of width expansion and attention provides the most consistent gains. Overall, dynamic width expansion based on representational demand provides an effective and flexible strategy for Class-IL, although uncontrolled growth may increase overfitting and computational cost.

---


### 366. [Generative Interactions: Weaving Multiparty Human Motion with Bilevel Latent Dynamics](https://arxiv.org/abs/2609.37708)

**<font color=#1a73e8>作者：</font>** Ojas Shirekar, Yash Surange, Agustinas Jučas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human social behaviour is not a collection of independent motions, but a jointly organised process in which group dynamics and individual variation continuously shape one another. Yet existing social motion models often prioritise plausible trajectories while leaving interaction state implicit, limiting their ability to transfer across groups, tasks, and partial-observation regimes. To address this gap, we introduce Bilevel Representations for Agent Interaction Dynamics (BRAID), a hierarchical sequential latent-variable model for generative multi-person interaction. BRAID explicitly formulates social motion generation as a meta-transfer learning problem: shared interaction priors are learned across datasets and adapted through arbitrary context sets of observed people and joints. The model represents each scene through a group-level latent state that captures shared interaction dynamics and person-level latent states that capture individual behaviour conditioned on the evolving group context. This modelling choice enables coherent generation under full, sparse, or partial observations while exposing compact social-state vectors that can serve as an interface for downstream embodied-agent systems. We evaluate BRAID under a unified SMPL-based representation on social forecasting, tracking and in-filling, and response generation, using metrics that assess not only reconstruction accuracy but also realism, diversity, temporal alignment, and interpersonal coordination. We further analyse the hierarchical latent space, showing that it captures separable group- and individual-level structure.

---


### 367. [VIF-Bench: Evaluating Visual Instruction Following in Multi-Reference Image Generation](https://arxiv.org/abs/2609.37709)

**<font color=#1a73e8>作者：</font>** Yuta Oshima, Masakazu Yoshimura, Masahiro Suzuki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal image generation models can take multiple images and textual instructions as input, enabling reference-based generation guided not only by text but also by visual instructions such as layouts, arrows, and pose cues. However, existing benchmarks do not evaluate the joint setting in which multiple references must be composed under multiple and heterogeneous visual-instruction images. To address this gap, we introduce VIF-Bench, a benchmark of 1,241 tasks designed to assess the edge of model capabilities in this joint setting by covering: (i) multi-reference generation (up to 7) under multiple heterogeneous visual instructions (up to 6), (ii) cases where reference images can potentially compete with visual instructions (e.g., a strongly posed subject vs. a target pose), and (iii) controlled comparison of visual instructions with text descriptions at different levels of specificity. Using these capabilities, we uncover three findings: (1) models face an adherence-artifact trade-off: once models reach stronger visual instruction adherence, stronger adherence tends to coincide with more instruction artifacts in generated images, (2) visual instruction adherence tends to be lower on tasks whose reference images carry a salient state of the controlled attribute (e.g., a neon-lit subject under a light-direction instruction), most consistently for light and wind, and (3) for models that can understand visual instructions, it is often better to provide visual constraints directly rather than describe them in text; when using text, a moderate level of detail works better than an exhaustive description. VIF-Bench is released as an open benchmark to establish a basis for fair comparison in controllable multi-reference image generation.

---


### 368. [Spatiotemporal Hyperedges for EEG Seizure Detection and Prediction](https://arxiv.org/abs/2609.37730)

**<font color=#1a73e8>作者：</font>** Hyunju Kim, Sheo Yon Jhin, Noseong Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Seizure detection and prediction from EEG are clinically important but challenging because seizures are rare, temporally localized, and propagate as coordinated events across multiple channels. Recent dynamic graph neural networks model this by running a temporal model over a sequence of per-time-step pairwise channel edges. However, this pairwise construction misses the spatiotemporal coupling that constitutes a seizure, at substantial training cost. We propose HyBrain, which summarizes spatiotemporal EEG evidence through a small set of soft hyperedges rather than pairwise edges. A per-channel Mamba backbone produces one token per (channel, second), and a spatiotemporal hyperedge block pools these tokens into E_h shared group embeddings through soft memberships and broadcasts them back. The same encoder serves three downstream tasks: window-based detection, one-second point-wise detection, and preictal seizure prediction. On TUSZ and CHB-MIT, HyBrain achieves the best AUROC on every reported setting against ten baselines, with the largest gap on long-clip preictal prediction. It also matches the most efficient baselines in training time and peak GPU memory. A qualitative analysis shows that even a single learned hyperedge cleanly captures the preictal -> ictal -> postictal trajectory on a real seizure clip.

---


### 369. [HyDI: A hybrid Deep Learning-Inductive Logic Programming ensemble for multi-label classification](https://arxiv.org/abs/2609.37740)

**<font color=#1a73e8>作者：</font>** Simon Flügel, Till Mossakowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While attaining remarkable results for many applications, Deep Learning models are notoriously difficult to explain. This work introduces HyDI, a hybrid ensemble architecture for hierarchical multi-label classification. It combines a Deep Learning (DL) model with rule-based classifiers generated by Inductive Logic Programming (ILP). For leaf classes of the label hierarchy, the rule-based classifiers replace the DL model, leading to more transparent classification results. HyDI is applied to the Chemical Entities of Biological Interest (ChEBI) ontology, providing ILP-generated rules for 314 classes. For these classes, HyDI can generate global explanations as well as local explanations that combine visual and text-based descriptions.

---


### 370. [Lights, Camera, Attack: Exploiting Temporal HDR Fusion with Pulsed Light](https://arxiv.org/abs/2609.37742)

**<font color=#1a73e8>作者：</font>** Alkim Domeke, Michael Kuhr, Roman Gilliatt 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern cameras widely use temporal High Dynamic Range (HDR) to improve visibility by capturing a sequence of exposures with different integration times and fusing them into a single image. This process implicitly assumes that scene illumination remains sufficiently stable during capture. We introduce FLASH (Fusion-Level Attack by Saturating HDR), an external pulsed-light attack that deliberately attacks this assumption by creating cross-exposure inconsistency before downstream perception. FLASH exploits an algorithmic assumption rather than relying on sensor damage or hardware failure, and requires neither physical camera access, access to raw exposure brackets, knowledge of the fusion algorithm, nor exact phase lock to the camera. Across eight physical camera platforms spanning embedded, surveillance, photography, smartphone, and automotive use cases, and matched optical controls, FLASH causes pipeline-dependent darkening, overexposure, and visibility loss. This includes extreme-darkening rates of 50.0% on an iPhone 16 Pro and 33.7% on a Wyze Battery Cam Pro. On the Wyze camera, FLASH triggers the system-level low-visibility response in 10/10 trials, compared with 0/10 continuous-light and randomized-frequency flashing controls. In a controlled stationary OpenPilot case study, 23.0% of frames exhibit severe darkening in the traffic-cone target region, with target-background CNR decreasing by up to 90.8%. Under FLASH, the OpenPilot interface also fails to display the system-level path state observed in the corresponding control trials. In a controlled night-only HDR reconstruction stress test, a proof-of-concept exposure-rejection defense reduces median output-brightness deviation by 79.16%. These results show that temporal HDR fusion itself requires security-aware validation of exposure evidence.

---


### 371. [Which papyrus HTR is good enough? Character-error-rate tolerance of four papyrological tasks on Greek texts](https://arxiv.org/abs/2609.37755)

**<font color=#1a73e8>作者：</font>** Anton Repushko, Elena Chepel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Purpose: Most Greek papyri remain unpublished and undigitised; a handwritten text recognition (HTR) pipeline that transcribes them automatically would let scholars discover documents and literary works that have so far gone unread. Recognition systems for Ancient Greek papyri are in statu nascendi, and how accurate they must be for a given papyrological task has not been examined. To answer this and set a benchmark for Greek papyrus HTR, we test a range of character error rates (CER) against four papyrological tasks, using published editions as ground truth. Methods: From 63,846 current editions of Greek texts in this http URL, we imitate a letters-only "perfect HTR" output by removing the editorial layer, then degrade it with a seeded algorithm to exact CERs of 1 - 50%, with lost lines and four error-shape variants. On these data we train small models (TF-IDF, fastText, a character CNN, ByT5-small) for document type, dating and documentary-versus-literary classification, and apply eight keyword search methods. We compare models trained on clean text with models retrained at a specific CER level, and evaluate across CERs. Results: Tolerance differs by task. With clean-trained models, documentary-versus-literary classification retains 90% of its metric up to 20% CER; document type up to 7.5%; subtypes and search up to 5%; dating only up to 3%. Retraining on text containing character errors largely eliminates the sharp degradation that otherwise sets in above 15% CER. Models generally tolerate concentrated damage in a long document better than small errors spread across a short text. Conclusion: The study provides a CER target for each of the four tasks and shows that models trained on noisy text make current, imperfect text recognition useful for them.

---


### 372. [HiRAE: Hierarchical Representation Autoencoding with Residual Budgets](https://arxiv.org/abs/2609.37775)

**<font color=#1a73e8>作者：</font>** Xuanyu Zhu, Yan Bai, Yang Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained visual representations support image generation, but may not fully preserve the fine-grained details needed for faithful reconstruction. Meanwhile, intermediate encoder layers contain complementary visual details, but learning to fuse them for reconstruction can produce a latent distribution that is difficult to model. Existing fusion methods require empirical tuning of layer selection or staged optimization of fusion and decoding, increasing configuration effort or training complexity. We introduce HiRAE (Hierarchical Representation Autoencoder), which learns a hierarchical fusion framework over the full encoder hierarchy to improve reconstruction fidelity while maintaining compatibility with generative modeling. HiRAE groups encoder layers by depth and learns residual corrections to the deepest representation. Group-wise norm caps bound these corrections relative to the deep anchor, with tighter budgets for shallower groups. Our HiRAE-24 preserves the latent token count and channel dimension. On ImageNet-256, HiRAE-24 reduces reconstruction FID from 0.299 to 0.209 relative to RAEv2 while maintaining competitive guided generation quality. For text-to-image generation, HiRAE-24 improves alignment over RAEv2 on GenEval, DPG-Bench, and GenAI-Bench both before and after supervised fine-tuning. Under the same generator-training and evaluation protocol, post-fine-tuning GenEval increases from 84.86 to 87.70.

---


### 373. [A Benchmark & Dataset for Detecting AI-Manipulated Visual Evidence in the Court System](https://arxiv.org/abs/2609.37783)

**<font color=#1a73e8>作者：</font>** Kelly McConvey, Sajad Ebrahimi, Nima Jamali 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photographic evidence is becoming increasingly vulnerable to forms of alteration and fabrication that existing legal and technical workflows are not well equipped to evaluate. Surveillance frames, dashcam stills, and phone photographs may be used to establish presence, sequence, causation, damage, or identity, yet contemporary generative systems allow non-experts to alter or fabricate such images through ordinary prompt-based interfaces. Existing image-forensics benchmarks provide important resources for face manipulation, classical tampering, and general synthetic-image detection, but they are not organized around the forms of visual evidence submitted in courts, the localized edits that can change what an exhibit appears to prove, or the consumer-tool threat model now facing the justice system. We introduce the CIFAR Synthetic Evidence Corpus for Detecting AI-Manipulated Images, a benchmark for evidentiary image authentication in court and justice-system contexts. The corpus contains 1,505 photographic items, including 720 authentic controls and 785 manipulated or fabricated images, spanning surveillance, dashcam, and consumer-photo imagery. Manipulations are organized into scene-condition edits, localized element edits, and full fabrications produced with contemporary generative systems. Each item is released with structured metadata covering source provenance, manipulation tier, subtype, generator, prompt template, and scene attributes, enabling controlled evaluation beyond aggregate binary detection. We also establish baselines with publicly available image-manipulation detectors, showing that current systems exhibit error profiles that remain problematic for evidentiary use. The dataset, prompts, metadata, code, and baseline evaluation scripts are released to support research on visual evidence authentication, information integrity, and trustworthy AI for the justice system.

---


### 374. [Planetary Feature Fields are Scalable Earth Representations](https://arxiv.org/abs/2609.37784)

**<font color=#1a73e8>作者：</font>** Arjun Rao, Sebastian Loeschcke, Anthony Fuller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite observations, precomputed embeddings, and map products describe the same evolving Earth, yet are stored as independent, petabyte-scale data products. Their continued growth calls for compact representations of multiple products while preserving spatial and temporal detail. We introduce Planetary Feature Fields (PFFs), which exploit redundancy across data products by modeling them jointly as continuous functions of space and time at planetary scale. PFFs are spatially local explicit-implicit (hybrid) neural fields. Each field shares a factored feature volume---a decomposition of an explicit 3D grid with smaller factors---across products, while lightweight implicit decoders reconstruct individual products across multiple timesteps. PFFs reconstruct EO products over space and time more accurately than single-product fields at matched compression rates. At $1800\times$ compression relative to the uncompressed source data, reconstructed features retain approximately $90\%$ or more of the performance achieved with the original features on pixel-level segmentation, change detection, and patch-level classification tasks. PFFs can add new timesteps by extending their factored feature volumes and add new products by attaching new decoders, while leaving existing outputs unchanged. PFFs reduce end-to-end feature access latency by an order of magnitude relative to evaluated API and cloud-storage pipelines.

---


### 375. [Adam under Generalized Smoothness with Second-Moment-Type Stochastic Gradients](https://arxiv.org/abs/2609.37787)

**<font color=#1a73e8>作者：</font>** Ruinan Jin, Difei Cheng, Ling Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adam is widely observed to remain stable even when the objective deviates significantly from global smoothness. Under the generalized smoothness framework, however, existing analyses rely on strong tail assumptions on the stochastic gradients, such as almost-sure boundedness or sub-Gaussianity. Whether Adam converges on generalized smooth objectives under only second moment information on the stochastic gradients, without such concentration assumptions, was identified as an important open direction by Li et al. (2023). This paper gives an affirmative answer under fairly general conditions: such tail assumptions are not necessary. Building on the Adam self-normalization framework of Jin et al. (2026), developed for classical smoothness and bounded variance, we extend the stopping-time and de-preconditioning strategy to the $L_0$-$L_p$ generalized smoothness condition and a generalized second moment ABC condition. Even when the stochastic-gradient condition provides only second moment information that may grow along the trajectory, the stochastic trajectory of Adam remains in a locally well-behaved smoothness region, with stretched-exponential tail decay under bounded variance and global smoothness. Consequently, we establish high-probability convergence rate guarantees over the full range $p<2$, with confidence dependence of order $\delta^{-1/2}$, while the stepsize prefactor depends on $\delta$ only through a single logarithmic factor. We further construct a hard instance showing that, under only second-moment information, this $\delta^{-1/2}$-type confidence dependence is sharp. Finally, in the regime $p<1$, we combine the trajectory control with polynomial-growth estimates on rare events to obtain convergence rate guarantees in expectation.

---


### 376. [Predictive Self-Supervised Learning Provably Identifies Stochastic Signals under Nuisance](https://arxiv.org/abs/2609.37789)

**<font color=#1a73e8>作者：</font>** Fabian A. Mikulasch, Friedemann Zenke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) by predicting in latent space, without generating the input data itself, learns highly abstract, useful representations. Intuitively, this success is often attributed to its ability to discard nuisance information that is irrelevant to prediction. However, this poses a conundrum: both stochastic variation in a prediction-relevant latent signal and true nuisance make observations partly unpredictable; how could they be distinguished? Surprisingly, we prove that common SSL methods can achieve exactly this, by implicitly instantiating a latent-variable model with stochastic dynamics and observation-private nuisance. We trace their ability to recover the stochastic signal to two complementary principles: Predictive mutual information maximization ensures that representations retain the information needed for prediction, while latent distribution matching constrains how this information is encoded, thereby making the retained signal identifiable. We confirm this identifiability result in simulations for Gaussian predictors, which recover the true signal up to an affine transformation even in dynamic, nuisance-laden environments.

---


### 377. [A neural network that maintains and retrieves memories based on context](https://arxiv.org/abs/2609.37791)

**<font color=#1a73e8>作者：</font>** Hayoung Song, JeongJun Park, Qihong Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every day, people continuously infer situational context and adjust the way they understand and remember the world. Context, signaled by the prefrontal cortex, is known to modulate working memory and episodic memory, but the algorithmic understanding of this modulation remains limited. Here, we train a recurrent neural network (RNN), augmented with an episodic memory buffer, to infer context using Bayesian inference as it continuously makes predictions of upcoming scenes while watching naturalistic movies. When the inferred context modulates the RNN's recurrent connectivity (the basis of working memory) in a low-rank manner, the model's activity patterns best match neural responses in human participants who watched the same movies during fMRI. Context also modulates episodic memory retrieval, such that the model retrieves memories based on not only content similarity but also context similarity. This is implemented as a key-value system with self-attention, designed to additionally encode context and retrieve context-congruent memories. The resulting model not only better resembles human brain representations but also learns to retrieve memories like humans much faster than a model without context modulation. Together, our findings suggest a computational mechanism by which context modulates information maintenance and long-term memory retrieval in naturalistic environments.

---


### 378. [Challenges and Solutions for Bandits in the Wild: Warm-Started Mixture Bandits for Cross-Cohort Slate Recommendation](https://arxiv.org/abs/2609.37800)

**<font color=#1a73e8>作者：</font>** Serafima Lebedeva, Sumantrak Mukherjee, Ali Arshad Sadal 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many recommender services repeatedly encounter cold-start cohorts, where new users arrive with little or no interaction history. This creates two challenges: learning user preferences quickly from limited feedback and sustaining useful recommendations when each user has a finite catalog that can become repetitive or depleted over time. We propose CohortMix-TS, a warm-started mixture bandit that learns latent user groups from earlier cohorts and uses available metadata to construct group-informed priors for new users. Starting from these fixed priors, the model personalizes independently as feedback from each user becomes available. Session slates combine Thompson sampling with diversity and inventory-depletion controls. We evaluate CohortMix-TS through simulation, semi-synthetic experiments, and a 25-day randomized in-the-wild deployment with 713 registered participants in a Campus Games quiz application. Our evaluations show that cross-cohort transfer improves early recommendation quality and user-level regret, while inventory-aware slate construction helps prevent premature exhaustion of preferred items. In the field deployment, treatment users also showed a larger early-to-late change in correctness than users receiving random recommendations. Together, these results show how warm-start transfer and inventory-aware recommendations can support personalization for short-lived, repeatedly cold-starting cohorts.

---


### 379. [ByteTraX: Enhancing the ByteTrack Architecture with Optimised Thresholding](https://arxiv.org/abs/2609.37801)

**<font color=#1a73e8>作者：</font>** Thomas A. O'Shea-Wheller  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The ByteTrack algorithm is a widely used and computationally efficient multi-object tracking architecture. Its core innovation lies in the combination of lenient bounding box associations with tracklet similarity matching to robustly deal with object occlusions. However, this strategy is nevertheless vulnerable to erroneous track reclassification and identity switching, as detection confidence scores dictate association priority. To address this, I present a simple enhancement of the ByteTrack architecture, named ByteTraX, that optimises track continuity via a single unified matching threshold, while penalising identity switches through stringent track initiation criteria. This approach achieves consistently improved performance across a range of diverse benchmarks including GMOT-40, LC-MOT, SportsMOT, TeamTrack, DAMUNT, and DeepSea-MOT, while simultaneously increasing processing speed by >10%. Specifically, results demonstrate a >40% reduction in identity switches, accompanied by mean increases in HOTA of 3.6, IDF1 of 5.6, and FPS of 6.3. As such, adoption of the ByteTraX algorithm has the potential to substantially enhance tracking performance over the ByteTrack baseline, while retaining the efficiency needed for real-time deployment. To facilitate usage, I provide the source code, integration functionality for the YOLO family of object detection models, and deployment instructions via an open source repository.

---


### 380. [Feedback-Calibrated Protein Optimization with Batch-Aligned Tail Arbitration](https://arxiv.org/abs/2609.37808)

**<font color=#1a73e8>作者：</font>** Zefeng Lin, Xianyong Fang, Tianfan Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein optimization aims to discover high-fitness sequences under a limited experimental budget. Existing machine-learning methods use task-specific predictors, biological priors, or ranking-aware objectives to guide which variants are tested in the next experimental round. However, these methods cannot adapt to shifts in the reliability of predictive evidence as measurements accumulate and ensure the correct ranking of key high-fitness candidates. To address these challenges, we propose Batch-Aligned Tail Arbitration (BATA), which uses experimental feedback to adaptively combine prior-informed and task-specific rankings for next-batch selection, with calibration focused on the batch-aligned high-fitness region. Across measured GB1, PABP, and TrpB landscapes, BATA achieves the best mean task rank (1.67) in final best fitness after 480 measurements. Controlled comparisons further show task-dependent gains from high-fitness calibration and batch alignment. Our work introduces feedback-calibrated predictor arbitration, where experimental feedback dynamically determines how predictive evidence guides next-batch selection, opening a new direction for protein optimization.

---


### 381. [Pixel-Level Transformers in Remote Sensing: A Canopy Height Case Study](https://arxiv.org/abs/2609.37809)

**<font color=#1a73e8>作者：</font>** Sven Ligensa, Jan Pauls, Karsten Schrödter 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting canopy height from medium-resolution satellite imagery is a common and scalable approach for assessing the condition of the world's forests, which play a crucial role in climate change mitigation. While Transformer-based architectures have shown strong performance in many domains, their straightforward application to dense (i.e., pixel-level) regression tasks often yields suboptimal results. In particular, the patch size has a crucial impact on the model performance. In this work, we consider pixel-level attention schemes and show that the resulting models generally outperform those relying on larger patch sizes. However, pixel-level attention can be a prohibitively resource-intensive operation. For this reason, we conduct an extensive experimental study using efficient attention variants to identify favorable trade-offs between prediction quality and resource requirements, facilitating the practical deployment of the proposed models. In addition, we perform a comprehensive comparison with several well-established models in the field and show that, with suitable hyperparameter choices, Transformer-based architectures can outperform competing approaches. Our findings provide practical guidance for designing models for pixel-level regression tasks on medium-resolution satellite imagery, including canopy height and biomass estimation, soil moisture mapping, and yield forecasting.

---


### 382. [CommSketch: How Speaking while Sketching Steers Human--AI Design Ideation](https://arxiv.org/abs/2609.37813)

**<font color=#1a73e8>作者：</font>** Weiyan Shi, Darryl Lim, Geraldine Quek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Designers often speak while sketching when explaining ideas, yet AI design tools often rely on sketches or prompts, overlooking context expressed as ideas develop. We developed a sketch-based AI design interface that jointly interprets sketches and concurrent speech. Through a between-subjects study ($N=24$), we examined how speaking while sketching steers human--AI design ideation compared with sketches alone. For creativity support, concurrent speech supported natural expression of design intent and efficient visualisation. For human--AI collaboration, speech helped establish a shared understanding of design intent, supported significantly higher perceived alignment ($p<.05$), and enabled participants to guide AI contributions as ideas co-evolved. We discuss how future human--AI design tools could support dynamic alignment, broader multimodal expression, and human--AI co-creativity.

---


### 383. [WINGS: Reference-Free Gaussian Splatting Inpainting with 3D-Native Generative Priors](https://arxiv.org/abs/2609.37816)

**<font color=#1a73e8>作者：</font>** Noé Lallouet, Michael Fischer, Elie Michel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inpainting 3D Gaussian Splatting scenes, a key challenge in 3D editing, requires generating plausible content within a masked region of 3D space. Prior approaches rely on 2D diffusion models to produce one or several inpainted reference views, making them susceptible to challenges associated with multi-view inconsistency and lengthy optimization times. Departing from these approaches, we introduce a reference-free Gaussian splatting inpainting method operating natively in 3D. Our method leverages the embedding space of a large, pre-trained 3D prior, combined with a structure completion network to feed a generative prior which reconstructs the missing region's geometry and appearance. Performing content generation entirely in 3D, it avoids the need to reconcile inconsistencies of multiple inpainted reference images, and is faster than related 2D-based methods. We demonstrate the effectiveness of our method qualitatively and quantitatively, through extensive experiments and a user study. To the best of our knowledge, this work is the first Gaussian splatting inpainting method to operate in the learned representation space of a 3D-native generative prior without relying on inpainted reference views.

---


### 384. [Minkowski Attractor Networks: Closed-Form Hyperbolic Flows for Visual Representations](https://arxiv.org/abs/2609.37817)

**<font color=#1a73e8>作者：</font>** Zhongping Ji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric representation learning predominantly scaffolds representations onto flat Euclidean subspaces or compact product tori ($\mathbb{T}^K$). However, flat manifolds possess vanishing curvature and polynomial volume growth, inherently suffering from metric distortion when embedding multi-scale, tree-like visual hierarchies. While hyperbolic spaces ($\mathbb{H}^m$) circumvent this via constant negative curvature ($K<0$) and exponential volume expansion, prior hyperbolic deep architectures are hindered by computationally cumbersome Riemannian optimization, non-linear gyrovector calculus, and floating-point instabilities.
In this work, we introduce \textbf{Minkowski Attractor Networks (MAN)}, an operator-splitting-inspired framework that embeds representations within pseudo-Riemannian Minkowski spacetime ($\mathbb{R}^{1,m}$). By framing hyperbolic manifolds as quadric level sets, MAN resolves hyperbolic geometry by combining linear Lorentz group transport with non-linear cone lifting and closed-form radial rescaling, evaluating in a single forward pass without numerical ODE solvers or iterative retractions. We establish \textbf{MAN-2D} ($\mathbb{R}^{1,1} \to \mathbb{H}^1$) as our primary, high-throughput visual backbone, which maximizes channel factorization granularity into $D/2$ independent two-dimensional Minkowski blocks. We further formulate \textbf{MAN-4D} ($\mathbb{R}^{1,3} \to \mathbb{H}^3$) as a spacetime extension, leveraging a commuting Cartan-subalgebra parameterization of $\mathrm{SO}^+(1,3)$ to evaluate 4D Lorentz isometries via two commuting 2D planar maps without matrix-exponential overhead.

---


### 385. [Behavioral Convergence Without Representational Convergence: Persistent Training-History Dependence in Neural Networks](https://arxiv.org/abs/2609.37836)

**<font color=#1a73e8>作者：</font>** Ertuğrul Mutlu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks trained toward the same final objective can reach similar predictive performance while retaining internal representations shaped by earlier training history. We study this effect using controlled sequential-training experiments in which paired convolutional networks start from identical weights, experience reversed task orders, and then receive the same deterministic common-relaxation distribution. Across 20 paired MNIST runs, 16 satisfy a predeclared behavioral-matching criterion, yet their matched representations retain a mean history score of 0.139 (95% bootstrap CI: 0.127-0.153) and approximately 3.1% prediction disagreement. Extending common relaxation to 50,000 optimizer updates does not erase the measured difference: across five paired seeds, the representation-history score remains 0.190 (95% bootstrap CI: 0.161-0.219) at the end of the measured horizon while the mean accuracy gap is only 0.18 percentage points. Fresh linear probes show that, with sufficient labeled data, the two histories retain practically equivalent linearly accessible class information. A same-label rotated-MNIST control reproduces the effect: all five paired seeds reach behavioral matching while retaining a mean representation-history score of 0.162. Finally, a matched-learning-rate ReLU-LeakyReLU control reduces the 50,000-update representation residue by 0.040 on average in all five paired seeds, providing directional evidence that activation-mediated plasticity contributes to the persistence of training-history effects. These results provide protocol-scoped evidence that behavioral convergence need not imply representational convergence and that optimization history can leave measurable internal traces after prolonged common training.

---


### 386. [Counterfactual Probing for Parallel Unmasking with Hidden Forest Structure](https://arxiv.org/abs/2609.37841)

**<font color=#1a73e8>作者：</font>** Ryotaro Kawata, Satoshi Hayakawa, Taiji Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked generative models offer parallel token prediction, but accurate parallel sampling must account for dependencies among tokens. When dependencies are unknown, finding safe batches also costs model evaluations. We study whether total evaluations, including discovery, can be sublinear in sequence length $N$; sublinear sequential depth then follows. We consider discrete distributions with hidden forest structure, accessed through a fixed approximate conditional oracle. Under explicit regularity conditions and uniform Hellinger error bounds, for any fixed target accuracy $\varepsilon\in (0,1/8]$ and sufficiently large $N$, our sampler achieves seed-averaged total-variation error at most $\varepsilon$, with total masked-state submissions and sequential depth both bounded by $O(N^C \varepsilon^a)$ for constants $0 <C <1$ and $a > 0$. These guarantees use polynomial vocabulary size and an edge-response lower bound set by $N$ and $\varepsilon$. The sampler shares evaluations of hypothetical reveals across dependence tests to identify safe parallel batches without requiring full recovery of the hidden forest. A tunable parameter trades probing cost against irreversible commit rounds. In the same class, any admissible irreversible product-commit sampler attaining the same seed-averaged accuracy requires $\Omega(N^c \varepsilon^b)$ counterfactual submissions or commit rounds in the worst case, for constants $c,b>0$.

---


### 387. [Evaluation Choices Shape Biomedical ML Claims: A Pediatric Pneumonia Benchmark Case Study](https://arxiv.org/abs/2609.37848)

**<font color=#1a73e8>作者：</font>** Bhanu Prakash Vangala, Sowmya Guda, Latha Peddi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biomedical machine learning papers often compress model performance into one headline number. That number can look like a property of the model even when it depends strongly on how the benchmark was evaluated. We study this problem on the widely used Kermany pediatric chest radiograph dataset using nine image classifiers and a controlled evaluation protocol. Under the same protocol, the eight pretrained backbones differ by only 0.026 AUROC. In contrast, changing whether the backbone is frozen or fine-tuned changes AUROC by 0.044 on average, and changing the decision threshold changes balanced accuracy by 0.090 on average. The official test split is also measurably different from the training pool: a partition classifier distinguishes them at AUC 0.697, rising to 0.898 for normal radiographs. Most strikingly, a classifier using only file properties, with no image anatomy, reaches 0.992 balanced accuracy within the training pool but falls to 0.496 on the official test split. Validation-fitted thresholds and calibration also transfer imperfectly. These results show that a high benchmark score can support different conclusions when the split, training policy, threshold, metric, calibration, and uncertainty are not communicated with it. We end with a seven-item reporting recommendation in which each item is tied to an effect measured in the study

---


### 388. [RelayVSR: Large-Small Model Collaboration for Efficient Real-World Video Super-Resolution](https://arxiv.org/abs/2609.37850)

**<font color=#1a73e8>作者：</font>** Xijun Wang, Xin Li, Zirui Lang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large generative models can recover realistic detail in real-world video super-resolution (VSR), but processing an entire video with them is computationally expensive. In this work, we present RelayVSR, a streaming VSR framework built on the Sparse Generative Relay mechanism. A large generative model generates reference latents for sparse keyframes, while a lightweight VSR network uses these references and low-resolution video to super-resolve every frame. The lightweight VSR network, implemented as a Dual-Memory Video Transformer, reuses keyframe information across frames and updates recent video context, supporting first-keyframe conditioning and dual-endpoint conditioning with bounded lookahead. However, errors in shared keyframes can propagate and accumulate across output frames, making keyframe quality alone an insufficient optimization target. We address this collaboration gap with Video-Aware Reference Optimization (VARO), which uses reinforcement learning to update the large generative model with two reward levels: a system-level reward evaluates videos produced by the fixed lightweight VSR network, while a reference-level reward evaluates decoded keyframe quality. VARO improves final video quality over direct joint training, and its dual-level rewards outperform a system-level reward alone. At 1080p on a single NVIDIA A100 80GB, dual-endpoint RelayVSR with a 15-frame keyframe interval reaches 29.29 FPS, 13.82 GB peak GPU memory, and 0.327 s first-frame model latency, compared with 7.80 FPS, 24.447 GB, and 2.83 s for FlashVSR-Tiny. The code is available at this https URL.

---


### 389. [HandAnthro: Automated Hand Anthropometry from a Single Image](https://arxiv.org/abs/2609.37855)

**<font color=#1a73e8>作者：</font>** Fan Zhou, Shuairan Chen, Mengying Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand anthropometry supports protective-glove design, but existing measurement methods often require trained operators, specialized hardware, or manual landmarking. We present HandAnthro, which estimates 44 projected hand dimensions from a smartphone photograph of a palm-up hand on US letter-size paper. The pipeline reconstructs wrist-occluded paper boundaries for rectification, whitens non-hand pixels, and refines 41 anthropometry-specific landmarks from a fine-tuned You Only Look Once (YOLO) pose model using image-specific geometry and contours. Controlled evaluation comprised 720 captures from 45 held-out participants, each contributing 16 images across two smartphones, two backgrounds, two angles, and two nominal illumination settings. HandAnthro produced complete outputs for 704 captures (97.8%); among these, mean absolute error (MAE) was 3.80 mm per dimension against two trained operators' caliper measurements. Regional MAEs were 2.48 mm for non-thumb fingers, 6.04 mm for thumbs, and 6.17 mm for palm and wrist. In a researcher-assisted mobile-app pilot, automated batch processing returned all 44 dimensions for 260 of 268 retained, researcher-screened firefighter images (97.0%). A descriptive, unpaired comparison with an independent national firefighter reference yielded a mean absolute difference of 2.40 mm across 28 sex-by-dimension group-mean contrasts. These results characterize controlled measurement performance and researcher-assisted field feasibility for future distributed hand-anthropometry studies.

---


### 390. [One Threshold Does Not Fit All Languages: Language-Conditional Deferral for Reliable and Efficient Low-Resource Text Classification](https://arxiv.org/abs/2609.37861)

**<font color=#1a73e8>作者：</font>** Bhanu Prakash Vangala, Vangala Navya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In the Global South, the lower-income countries of Africa, Asia, and Latin America where most of the world's languages are spoken, a deployed text classifier usually runs on ordinary CPUs, serves many languages with a single model, has few labeled examples in any of them, and relies on people to catch its mistakes. Such a system is only useful if it can promise how often it will be wrong: at most a fixed fraction of the labels it assigns on its own may be incorrect, and everything else must go to a person. Split conformal prediction delivers this promise through a single confidence threshold, normally estimated on validation data pooled across languages. We ask whether the promise reaches every language, and it does not. On MasakhaNEWS (16 African languages) and AfriSenti (12 languages plus two never seen in training), a pooled threshold meets the 90% target on average but covers Somali at 77.5%, Tigrinya at 83.7%, and the two unseen languages at 77.5% and 81.2%. Estimating one threshold per language brings every language to between 89.1% and 91.0% without retraining, and it shows how unequal the cost of the promise is: keeping it means sending 43% of Somali news and over 80% of Amharic and Xitsonga tweets to a person, against under 8% of Nigerian Pidgin news. One or two hundred labels per language are enough and the models train in minutes on one CPU core, so the fix is affordable: calibrate, report, and budget human review one language at a time.

---


### 391. [Strict-Saddle Landscapes and Multi-Rank Geometry in Low-Tubal-Rank Tensor Sensing](https://arxiv.org/abs/2609.37865)

**<font color=#1a73e8>作者：</font>** Eugene Agyei-Kodie, Longxiu Huang, Shuang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the optimization landscape of low-tubal-rank tensor sensing through a balanced factorization. Under a tubal restricted isometry condition, we establish a quantitative strict-saddle landscape with no spurious local minima for arbitrary Fourier multi-rank profiles. We further show that the local geometry depends on the Fourier-slice ranks rather than the tubal rank alone. Uniform ranks yield quadratic growth transverse to the solution orbit, whereas nonuniform ranks produce quartically flat directions through hidden frequency-wise overparameterization, even when the factor width equals the exact tubal rank. Numerical experiments illustrate the global optimization behavior and the contrasting local geometries.

---


### 392. [Learning from synthetic photorealistic raindrop for single image raindrop removal](https://arxiv.org/abs/2609.37870)

**<font color=#1a73e8>作者：</font>** Zhixiang Hao, Shaodi You, Yu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Raindrops adhered to camera lens or windshield are inevitable in rainy scenes and can become an issue for many computer vision systems such as autonomous driving. Because raindrop appearance is affected by too many parameters, therefore it is unlikely to find an effective model based solution. Learning based methods are also problematic, because traditional learning method cannot properly model the complex appearance. Whereas deep learning method lacks sufficiently large and realistic training data. To solve it, in our work, we propose the first photo-realistic dataset of synthetic adherent raindrops for training. The rendering is physics based with consideration of the water dynamic, geometric and photometry. The dataset contains various types of rainy scenes and particularly the rainy driving scenes. Based on the modeling of raindrop imagery, we introduce a detection network which has the awareness of the raindrop refraction as well as its blurring. Based on that, we propose the removal network that can well recover the image structure. Rigorous experiments demonstrate the state-of-the-art performance of our proposed framework.

---


### 393. [EndoPrior-GS: Dynamic Endoscopic Reconstruction with a Joint Texture Prior](https://arxiv.org/abs/2609.37874)

**<font color=#1a73e8>作者：</font>** Jiaqi Huang, Shidong Wang, Tong Xin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic endoscopic reconstruction is fundamental to robotic surgery and computer-assisted interventions. While 3D Gaussian Splatting (3DGS) realises real-time rendering, its application to deformable intraoperative environments remains constrained by spurious geometry and varying illuminations. To address these limitations, we introduce EndoPrior-GS, a novel pipeline that explicitly couples frame-extracted vision heuristics and estimated depth maps. EndoPrior-GS derives a joint texture prior from a tool-filtered valid tissue mask, a non-specular photometric filter, and anatomical structural salience, yielding a probability map that guides primitive initialisation and subsequent density control. The prior is further extended to the temporal domain through a texture-aware term that dynamically weighs pairwise primitive contributions during training. We conduct extensive experiments on benchmark datasets EndoNeRF and SCARED, and the obtained results show that our method EndoPrior-GS reduces Flow Error by 27.7% and 25.8% over the representative approaches while preserving competitive rendering quality and real-time rendering speed. Our project website is available at this https URL.

---


### 394. [Co-PiLOT: Constrained Physics-Informed Latent Optimization for Target-Driven Inverse Design](https://arxiv.org/abs/2609.37875)

**<font color=#1a73e8>作者：</font>** Mahish K. Guru, Mayank Nagar, Ayush vyas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inverse design of physical systems (molecules, devices, microstructures) often reduces to optimizing a high-dimensional structure against an expensive black-box simulator. Direct search is difficult because the space is non-Euclidean, feasibility is hard to encode, and each evaluation is expensive. We present Co-PiLOT, a latent optimization approach that maps candidates through a generative encoder-decoder, uses the decoder as a learned validity prior, and searches the latent space with physics-informed black-box optimization. The framework is applied on the inverse design of magnesium alloy microstructure/texture. We develop a vision transformer based-encoder; paired with latent diffusion, diffusion transformer and rectified-flow transformer-based decoders on $\sim80{,}000$ EBSD-derived microstructure dataset to learn a minimal bottleneck, $z$. The ViT-FMDiT model ($z$=$768$) reconstructs high-fidelity microstructure images (FID $27.86$, MS-SSIM $0.178$), which our self-segmenting orientation codec converts into input grids for crystal plasticity solver. Finally, we introduce MERIDIAN, an active latent optimizer driven by deep-kernel Gaussian-process uncertainty, failure-aware feasibility prediction, manifold-aware trust regions, and target-aware acquisition. Within a budget of $160$ simulations, the ViT-FMDiT and MERIDIAN combination yields the best target-driven objective score, reducing the relative target error by $3$--$22\%$ against seven baselines (DANTE, TuRBO, BAxUS, CMA-ES, DDOM, SEIKO, DDPO) on the same decoder.

---


### 395. [TopoEmbedX: A General Framework for Representation Learning on Topological Domains](https://arxiv.org/abs/2609.37884)

**<font color=#1a73e8>作者：</font>** Florian Frantzen, Ibrahem AlJabea, Ines Henriques-Cadby 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Topological structures such as simplicial complexes, hypergraphs, and cell complexes extend standard graph models by modeling higher-order relationships. These structures appear in many modern datasets and require specialized methods for generating meaningful embeddings. In this paper, we introduce TopoEmbedX, a unified framework for embedding a wide range of topological domains into Euclidean spaces. The package brings together several existing topological embedding algorithms---DeepCell, Cell2Vec, CellDiff2Vec, HOLE, and HOGLEE---and introduces five new algorithms: ComplexNetMF, ComplexRep, ComplexRandNE, ComplexWalklets, and ComplexHeat. These algorithms extend well-known graph embedding techniques to higher-order settings using the augmented Hasse graph of a topological domain. TopoEmbedX provides a clear, consistent, and easy-to-use framework for topological representation learning. Experiments show that the embeddings generated by TopoEmbedX support tasks such as classification and regression across multidimensional data.

---


### 396. [Visual Branch is What You Need for CLIP-based Class-Incremental Learning](https://arxiv.org/abs/2609.37888)

**<font color=#1a73e8>作者：</font>** Tao Hu, Zhen-Hao Xie, Jingcai Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-Incremental Learning (CIL) requires models to recognize new classes over time without forgetting previously learned ones. With the rise of vision-language pre-training, CLIP has become a strong foundation for CIL. A common design in CLIP-based CIL is to construct textual classifier weights by encoding class-name templates with the CLIP text encoder, and then classify visual features by image-text cosine similarity. This design is appealing: since CLIP aligns images and text in a shared embedding space, textual weights appear to provide an off-the-shelf classifier for incremental classes. However, we show that this seemingly natural design is not always beneficial, as a modality gap can still separate the two modalities and make textual classifier weights deviate from visual class distributions. Empirically, under identical task-wise CIL training, initializing the cosine classifier with visual class centers yields lower loss and better incremental accuracy than using CLIP textual this http URL by these observations, we propose VIS, a visual-only method for CLIP-based CIL that removes the deployed textual branch and constructs the incremental classifier entirely in the visual space. To obtain stronger task-adaptive visual representations, VISuses only base-session data to enhance CLIP's final visual representation with informative visual-layer features. Built on the enhanced visual representation, VISemploys a simple kernelized incremental least-squares SVM, whose classifier weights are solved in closed form from additive sufficient statistics. When new classes arrive, VISaccumulates their sufficient statistics and recomputes the classifier weights for all seen classes, enabling efficient incremental updates while preserving historical class knowledge. Extensive experiments show that VISachieves state-of-the-art performance without a textual branch.

---


### 397. [Scaling Zero-Order Pretraining through Model Sharding](https://arxiv.org/abs/2609.37899)

**<font color=#1a73e8>作者：</font>** Francois Chaubard, Mykel J. Kochenderfer, Chris Ré  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-order optimization (ZO) trains without backpropagation, making it relevant to forward-only hardware and non-differentiable loss, but its gradient variance grows with perturbed dimension, inhibiting large-model training. Sharded Optimization Mixture of Assemblies (SOMA) trains LSTM experts independently on $N$ data clusters using simultaneous perturbation stochastic approximation (SPSA), without exchanging gradients, activations or optimizer state. Its separable loss removes cross-expert perturbation noise at the cost of jointly learned representations across domains. Using 80,000 estimated RTX 5090 GPU-hours, we show modest sharding improves training compute efficiency over all tested monolithic ZO controls. At 8.44M parameters and 150 aggregate GPU-hours, SOMA $N=2$ with 64 perturbations reaches 1.76 test nats/byte, versus 2.00--2.11 for monolithic SPSA at 64, 256 or 1,024 perturbations and 2.21 for EGGROLL. On WikiText-103, these frozen checkpoints reach 2.07, 2.25--2.36 and 2.49, respectively. On a fixed separable objective with equal-size blocks, we prove independent losses reduce relative gradient variance to approximately $1/N$ of a shared-loss estimator's. Holding starting weights, data, perturbations and compute fixed, independent rather than summed losses lower SOMA $N=4$ test loss by 0.035 nats/byte after 1,000 updates across three seeds. Larger ensembles offer a separate inference benefit: at similar model size with top-$k$ routing ($k=4$), SOMA $N=256$ achieves 2.36M tokens/s versus 257k for SOMA $N=8$ ($9.19\times$, including routing), at lower test loss (1.68 versus 1.71), albeit using $59.9\times$ as much aggregate training compute. We release all training and evaluation code and checkpoints.

---


### 398. [Beyond Interaction Capacity: Estimator Scaling with Recursive Models for CTR Prediction](https://arxiv.org/abs/2609.37905)

**<font color=#1a73e8>作者：</font>** Shivang Chopra, Fotis Iliopoulos, Zsolt Kira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Click-Through Rate prediction, a core task in recommendation and advertising systems, relies on modeling interactions among sparse categorical features. Explicit cross networks are a central paradigm for CTR prediction, and recent progress has largely come from increasing the interaction capacity of a single predictor through deeper cross networks and more expressive cross operators. We revisit whether continually increasing interaction capacity remains the most effective way to improve predictive performance, and find that its benefits quickly exhibit diminishing returns even as capacity continues to grow. This motivates a complementary scaling direction that we call estimator scaling, where additional resources are used to incorporate multiple related estimators rather than only enlarging a single predictor. Through theoretical analysis, we show that the gains from estimator scaling are governed by the amount of non-shared predictive variation available across estimators. However, exploiting this variation naively can be expensive: independently trained models provide substantial estimator diversity but require deployment cost to grow with ensemble size. This motivates a parameter-efficient realization of estimator scaling that can incorporate diversity from multiple estimator sources without maintaining multiple full models. Building on this view, we introduce RECursive Averaged Predictor (RECAP), a parameter-efficient recursive CTR model that operationalizes estimator scaling at three levels: distillation across independently trained models, exponential moving averaging over training trajectories, and aggregation over inference-time routes within a weight-shared recursive backbone. Experiments across multiple benchmarks establish new state-of-the-art predictive performance on standard benchmarks, while placing the RECAP on a favorable performance-parameter Pareto frontier.

---


### 399. [Pixels to Keys: Exploring Spatial and Motion Cues in Gameplay Inverse Dynamics](https://arxiv.org/abs/2609.37907)

**<font color=#1a73e8>作者：</font>** Abhishek Pillai, Ekta Prashnani, Joohwan Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video games offer scalable environments for studying perception and control in embodied this http URL online gameplay videos could supply demonstrations, but they rarely include player inputs for training. Inverse Dynamics Models (IDMs) have thus been proposed to infer inputs from frames. Large (up to 1B parameters) IDMs trained on $\sim$1K-2K gameplay hours demonstrate feasibility and cross-environment generalization at this scale, but researchers do not clarify what the key components are to recover individual actions and often report only aggregate accuracy that can mask rare-action failures. We study the problem in a data-constrained scenario to evaluate how spatial motion features, model architectures, and training objectives affect an IDM's outcome and we analyse our models on per-key and balanced metrics such as $F_1^{macro}$. Our experiments on Trackmania highlight the importance of factors like the model architecture and motion flow extraction in preprocessing, while also showing the limits of evaluation through unbalanced metrics. The application of the same architecture and training recipe to Cyberpunk 2077 reveals uneven performance across game mechanics. Our per-action evaluation and failure analysis highlight ambiguities from camera motion, delayed effects and imbalanced key-press frequencies that call for explicit modeling of 3D scene structure, long-term state and the adoption of proper losses in future implementations.

---


### 400. [Search Dimension in Unlabeled Projection Pursuit: A Scaling Law for Subspace Restriction](https://arxiv.org/abs/2609.37917)

**<font color=#1a73e8>作者：</font>** Rares Dimitrie Grozavescu, Mark Girolami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Projection pursuit searches for a direction along which the data look least Gaussian. When the observation space contains a large Gaussian complement, the empirical objective can be minimized by a direction that carries no signal, with empirical kurtosis as low as at the truth. Sample splitting exposes rather than repairs this failure. Appending coordinates independent of the latent regime degrades the search while leaving Bayes recoverability unchanged. Restricting the search to the column space of a known forward operator removes the failure exactly on the negative-kurtosis branch. Estimating a principal subspace from the data is the alternative. In a controlled two-component model, the leading sufficient scalings differ in the gain with which the operator transmits the discriminant: $\varsigma^{-4}$ for covariance-spike estimation and $\varsigma^{-8}$ for fourth-moment search. At fixed search dimension, the measured threshold ratio collapses onto $n/p^2$ with exponent $0.156$, close to the predicted $1/8$. This is an empirically supported scaling motivated by sufficient bounds, not a proved asymptotically tight law. When the search dimension is varied, the measured exponent is $0.325$, substantially larger than $1/8$, and the tested range does not identify its functional form. The crossing location also depends on calibration and model configuration. Under a downstream excess-error criterion, the scaling largely disappears.

---


> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-447](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
