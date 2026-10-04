# 📦 其他研究 | 2026年10月05日

> 本类共 **385** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-385**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-385**

---

### 351. [Relative Transitions, Not Absolute Destinations: A Transfer-and-Ground Framework for Target-Trajectory-Free Human Mobility Generation](https://arxiv.org/abs/2610.02033)

**<font color=#1a73e8>作者：</font>** Yidi Wang, Yunhe Zhang, Bangchao Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Individual mobility trajectories support urban analysis and location-based services, yet most trajectory generators require observations from their deployment city. This assumption excludes precisely the cities where trajectories are unavailable even though points of interest (POIs) and their attributes can be obtained from public maps. We study target-trajectory-free generation: learning from POIs and trajectories in source cities while utilizing only POI coordinates and categories in a target city, with no target trajectory or trajectory-derived statistic available for training, model selection, or generation. Existing trajectory generators typically predict absolute destinations, entangling reusable movement behavior with city-specific POI identities and spatial layouts. Our core insight is to replace this city-bound output with context-conditioned relative transitions. We propose Nomad, a transfer-and-ground framework that separates learning how people move from determining where those movements are realized. Specifically, a history-conditioned flow-matching model learns from source trajectories a transition prior over semantic displacement between POI contexts, geographic displacement, and elapsed time; at inference, a behavior graph and an exploration--return walk ground sampled transitions onto the target POI map. This factorization enables a direct test of representation level transferability without assuming invariance of the full mobility distribution. Extensive experiments across ten cities and 14 transfers show that Nomad outperforms adaptation baselines in trajectory fidelity and downstream utility, lowering the average error over the best baseline of each metric by about 15% in distributional fidelity and about 3% in downstream utility.

---


### 352. [Global Coherence: When Every Agent Is Right and the Team Is Still Wrong - A Local-to-Global Semantic Foundation for Multi-Agent Collaboration](https://arxiv.org/abs/2610.02036)

**<font color=#1a73e8>作者：</font>** Xin Heng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can each make locally valid decisions yet jointly produce an invalid result. We call this the global coherence problem: a failure of shared state, not merely of model intelligence.
Our Observation-Aliasing Impossibility Theorem gives the exact boundary. A policy can guarantee a valid action exactly when all worlds producing the same observation share an admissible action. If k indistinguishable worlds require pairwise-disjoint actions, the best randomized worst-case success is 1/k; more reasoning, roles, messages, or samples cannot recover the missing distinction. A stronger model can reason better within its context, but it cannot see beyond it.
We then give local-to-global runtime semantics X = (H, C, G, F; D): topology H records overlapping scopes; category C governs state-changing actions; groupoid G retains reversible translations; sheaf F tests whether local views glue into one world; and minimal history D keeps only distinctions that alter legal futures. Models propose; the harness owns shared state and governs commit.
Nine studies test both the failure and its boundary. On a controlled revision benchmark, the same frontier model scores 40/40 when the deciding event is visible; when it is hidden, tested arms score 12--17/40, consistent with chance (1/3); restoring one authoritative fact returns 40/40. On TeamBench, ordinary teams exceed a shared budget in 5/5 runs, a visible live count leaves 4/5 violations, and commit enforcement leaves 0/5. In tau2-bench Telecom, current-state checks score 0.07 after silent reverts, while the harness scores 1.00. Where a conventional solver already owns the complete relevant state, it ties the harness as predicted. The counterintuitive conclusion is that local intelligence cannot substitute for missing global state.

---


### 353. [Distributionally Robust Schrödinger Bridge](https://arxiv.org/abs/2610.02043)

**<font color=#1a73e8>作者：</font>** Jinhwan Sul, Panagiotis Theodoropoulos, Vincent Pacelli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Schrödinger bridge (SB) learns stochastic transport between prescribed initial and target distributions. When the initial distribution shifts at test time, the learned dynamics can fail to recover the target distribution. We introduce the Distributionally Robust Schrödinger Bridge (DRSB), which learns a single controller that accounts for uncertainty in the initial distribution. The DRSB objective consists of control energy and a KL penalty between the resulting terminal distribution and the target distribution. DRSB seeks a single controller that minimizes the worst-case value of this objective as the initial distribution varies within an ambiguity set around the nominal distribution. We derive an exact variational formulation of this objective and connect its fixed-terminal-cost subproblem to stochastic optimal control and distributionally robust optimization. This formulation motivates an alternating algorithm that updates the adversarial initial distribution, estimates the terminal log-density ratio, and trains the controller. We develop Wasserstein and Sinkhorn variants using stochastic control optimality conditions to approximate the gradients required for adversarial updates. Experiments on two-dimensional transport tasks and image-to-image translation show improved robustness to input perturbations relative to standard SB, with a tradeoff in nominal performance. On Gaussian mixture transport, Sinkhorn DRSB also achieves lower mean sliced Wasserstein distance than fixed-level noise augmentation at both tested unseen noise levels.

---


### 354. [DiDE:Direct Injection with Color-Texture DEcoupling for 3D Stylization](https://arxiv.org/abs/2610.02044)

**<font color=#1a73e8>作者：</font>** Tao Wu, Alexandra Gomez-Villa, Senmao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in rectified flow-based image-to-3D generative models have enabled high-fidelity 3D asset generation. Building on this, a growing line of work has exploited these strong 3D priors for training-free stylization, transferring visual attributes from a reference image onto a generated 3D asset. However, existing methods enforce an all-or-nothing paradigm: color and texture are transferred jointly, with no mechanism to control them independently -- a limitation we formalize as Disentangled 3D Stylization(Disen3D). To address this, we propose DiDE, the first training-free framework for Disen3D. Key to our approach is the observation that the structured latent space of image-to-3D models is overcomplete with respect to texture: texture information occupies only a small subset of the style-significant channels, leaving a free subspace available for independent color encoding. DiDE exploits this via a channel partition mechanism that processes a content image, a texture reference, and a color reference through dedicated branches and composes both style signals interference-free at every self-attention layer, preserving content geometry throughout. Experiments on Disen3D-Bench, our newly collected multi-reference benchmark, show that DiDE consistently outperforms 2D and 3D stylization baselines in color fidelity, texture transfer, and content preservation.

---


### 355. [Learning from Failure: Leveraging Unreliable Predictions in Semi-Supervised Real-World Adverse Weather Removal](https://arxiv.org/abs/2610.02051)

**<font color=#1a73e8>作者：</font>** Cap Dang Xuan Kiet, Tat-Jen Cham  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adverse weather image restoration aims to recover images degraded by rain, haze, snow, and other weather-induced artifacts, thereby improving the robustness of outdoor vision systems. Existing unified restoration models exhibit limited generalization to real-world scenes due to their reliance on synthetic supervision and insufficient semantic constraints. In this paper, we propose a novel student--teacher semi-supervised framework that addresses both challenges. Specifically, we introduce an unreliable database that preserves failed teacher predictions as informative negative samples for contrastive learning, while a reliable database stores high-quality teacher predictions as positive samples. By jointly exploiting reliable pseudo-ground truths and unreliable teacher outputs, the proposed framework learns to enhance desirable restoration characteristics while avoiding common failures. We further propose a phase spectrum-based semantic constraint that replaces computationally expensive text-based supervision with an efficient and naturally aligned semantic prior. An adaptive phase consistency loss is also designed to dynamically balance supervision between the degraded input and teacher pseudo-ground truths according to degradation severity. Extensive experiments on real-world benchmarks demonstrate that the proposed method consistently outperforms existing state-of-the-art approaches in restoration quality and perceptual fidelity while exhibiting stronger generalization to real-world adverse weather conditions.

---


### 356. [Foundations without Fundamentals: Zero-Shot Blind Spots in Time Series FMs](https://arxiv.org/abs/2610.02058)

**<font color=#1a73e8>作者：</font>** Nafiseh Ghoroghchian, Haipeng Zhang, Shuyi Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the success of Time Series Foundation Models (TSFMs) on broad benchmarks, their ability to internalize basic temporal logic, especially in settings supported by exogenous covariates, remains under-examined. We introduce SimpleTimeBench, a diagnostic univariate and multivariate "unit test" suite for primitives such as monotonic trends, periodic signals and leading indicator covariates, scenarios where near-perfect forecasts should be trivial. Surprisingly, prominent multivariate TSFMs (Chronos-2, Moirai and Toto) frequently produce suboptimal zero-shot forecasts for these inputs. While fine-tuning Chronos-2 improves its behaviour on specific tasks, we show that this adaptation degrades performance on other fundamental patterns rather than enhancing its generalizable foundational capabilities. This reveals a gap between pre-training scale and basic temporal reasoning, suggesting that current TSFMs could potentially lack the inductive biases needed to capture simple predictable functions. We further demonstrate that these failures are not merely synthetic curiosities: they persist in real-world sensor forecasting, where TSFMs consistently underutilize leading indicators available in observed covariates. This inability to capture simple relationships limits the practical utility and reliability of current multivariate models.

---


### 357. [Learn the Directions, Normalize the Gains: Post-Training Normalization for LoRA](https://arxiv.org/abs/2610.02067)

**<font color=#1a73e8>作者：</font>** Zailong Tian, Yanzhe Chen, Zhuoheng Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Low-Rank Adaptation (LoRA) enables efficient task specialization, its learned updates can compromise capabilities beyond the target task. We identify \textbf{adaptation imbalance}: a few singular directions dominate the trained update, leaving its performance sensitive to how gains are allocated. We argue that \textbf{learning where to adapt does not ensure that adaptation gains are well balanced}. This motivates \textbf{LoRA-Norm}, a post-training normalization method that retains learned directions while rebalancing their gains. LoRA-Norm combines spectral rebalancing, a fixed nonlinear transformation of singular values, with nuclear-norm restoration, which preserves the original total spectral mass. It requires no calibration data or additional training and introduces no inference overhead. Across two backbones and three adaptation tasks, LoRA-Norm improves average specialization and capability retention, outperforming the evaluated post-hoc spectral pruning and gradient-guided editing configurations on both measures. Stronger functional equalization brings no consistent additional gains, revealing that balancing adapter gains and equalizing their responses are distinct objectives.

---


### 358. [PyPottery: an AI-powered end-to-end suite for pottery processing and publication](https://arxiv.org/abs/2610.02072)

**<font color=#1a73e8>作者：</font>** Lorenzo Cardarelli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The study of ceramic materials constitutes a cornerstone of archaeological research, yet the post-production workflow for pottery documentation remains labor-intensive and creates significant publication bottlenecks. This paper presents PyPottery, an open-source, AI-powered suite designed to semi-automate the complete ceramic documentation pipeline. The suite comprises four integrated modules: PyPotteryScan for automated image extraction and handwriting recognition; PyPotteryInk for automatic inking of pencil drawings; PyPotteryTrace for semantically-aware vectorization; and PyPotteryLayout for automated layout generation. Evaluated on 50 hand-drawn sheets containing 240 pottery drawings from the Terramara di Montale (Italy), the framework achieved substantial time savings confirmed by usability study participants, who reported a median perceived speedup of 40$\times$ over traditional workflows (range: 17.5$\times$--120$\times$). These results highlight the potential of AI-assisted tools in archaeological documentation, while the paper addresses the strategic redistribution of cognitive labor toward augmentation rather than automation.

---


### 359. [Homomorphic Advantage Operator: Stabilizing Reinforcement Learning Under Fully Homomorphic Encryption Constraints](https://arxiv.org/abs/2610.02074)

**<font color=#1a73e8>作者：</font>** Abid Mohamed Nadhir, Ahmad Al Hanbali, Beggas Mounir  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving machine learning presents significant deployment challenges on the cloud for intelligent systems with confidential data. Fully Homomorphic Encryption (FHE) offers a compelling solution for secure computation, preserving data confidentiality of cloud computations. However, applying FHE to reinforcement learning (RL) requires replacing non-linear operations with polynomial approximations, which diverge catastrophically due to a unique recursive error phenomenon known as the Bellman drift. This article introduces the Homomorphic Advantage Operator (HAO), a stabilization framework designed to prevent polynomial approximation divergence in FHE-based deep RL. HAO adapts the zero-mean centering projection from advantage-based value estimation directly to temporal-difference (TD) targets. This linear projection annihilates the uniform state-value baseline that drives the Bellman drift, maintaining per-state action rankings while requiring zero additional non-linear multiplicative depth and avoiding expensive ciphertext bootstrapping. The proposed HAO framework was evaluated using a three-tier experimental methodology, including a tabular Markov Decision Process (MDP), an encrypted CartPole environment using real CKKS cryptographic operations, and a 20-node logistics routing benchmark with dense continuous features. The results demonstrate that the proposed HAO strictly bounds network pre-activations within the safe polynomial approximation domain. The proposed HAO RL agents achieved 0% boundary breaches across all random seeds used, whereas regularization alone (L2 weight decay and gradient clipping) breached the bound on 3 of 5 seeds and the unstabilized baseline did so in 83.8% of episodes. Finally, HAO agents improve optimal policy accuracy by 18.0 percentage points in tabular domains and remain stable when DP-SGD-style Gaussian noise is added to the clipped gradients.

---


### 360. [Are We Recovering Mechanisms? Objective-Level Recovery Gaps in Mechanistic Interpretability](https://arxiv.org/abs/2610.02098)

**<font color=#1a73e8>作者：</font>** Chuqin Geng, Li Zhang, Haolin Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability aims to recover the internal computations responsible for model behavior. Progress in automated circuit discovery is often framed as a search problem: better attribution or optimization should identify better mechanisms. This assumes that the evaluation objective can recognize a better circuit once it is found. We show that intervention-defined faithfulness can instead prefer an equally sized circuit that reproduces the model's behavior less well, creating an objective-level recovery gap. Across four human-reference tasks and InterpBench, we compare validation faithfulness with behavior on held-out prompts under fixed ordinary resampling. The behavioral criterion is agreement with the intact model, including its mistakes, except on Greater-Than, where we use semantic accuracy. Controlled reference edits reveal misranking without any discovery algorithm, and outputs of EAP, EAP-IG, ACDC, and Edge-SP exhibit the same failure. Under resampling, KL misranks 9.4%-41.2% of candidate pairs across these methods on the human-reference tasks. We investigate context distortion as an explanation: replacing excluded signals changes the inputs on which retained components operate. Restoring selected signals from the recipient's intact-model execution repairs 96 of 100 persistent KL misrankings from the discovery pool on both validation and held-out prompts. The circuits and their original behavioral scores remain unchanged. These findings show why better discovery alone is insufficient when its objective rewards the wrong candidate.

---


### 361. [Surface-volume self-supervised representation learning of brain MRI for genetic discovery](https://arxiv.org/abs/2610.02114)

**<font color=#1a73e8>作者：</font>** Tian Xia, Nuo Chen, Zihao Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing genome-wide association studies (GWAS) of brain imaging provide predefined or deep-learning-derived imaging phenotypes, yet these phenotypes come from either volumetric scans or cortical surface meshes, so each captures only part of the heritable variation in brain anatomy. Here we introduce MEVA (Mesh-Enhanced Volumetric Autoencoder), a self-supervised framework that encodes voxel-level image intensity together with cortical mesh geometry, including curvature and cortical thickness at each surface vertex, into one shared set of imaging features. Combining the mesh and volumetric inputs in MEVA yields modest performance gains in age and sex prediction over models that use either input alone. When these features serve as phenotypes for GWAS in the UK Biobank, they reveal more genome-wide significant loci than features learned from volumes alone or from meshes alone. These results suggest that adding cortical surface geometry to volumetric self-supervised learning captures additional heritable variation and so increases the number of loci detected.

---


### 362. [A Comparative Explainability Framework for DeBERTa-v3 in Zero-Shot Medical Abstract Classification](https://arxiv.org/abs/2610.02116)

**<font color=#1a73e8>作者：</font>** Javier Diaz Esteban-Herreros, David Muñoz-Valero, Raquel Martínez-España 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A comparative explainability framework is presented to audit DeBERTa-v3 under zero-shot classification of medical abstracts. The work addresses the disagreement problem in Explainable Artificial Intelligence, where different attribution methods produce divergent explanations for the same input and prediction. A natural language inference engine is implemented over the Medical Abstracts corpus with five enriched hypotheses per diagnostic category and a balanced sample of one thousand texts per class. Five explanation methods are compared: SHAP and LIME as model-agnostic approaches, occlusion and Input x Gradient as deep-learning-specific approaches, and Attention x Gradient as a transformer-specific approach. Explanations are standardized through top-token attribution, and pairwise agreement is quantified using the Jaccard index. High predictive accuracy is achieved across well-defined clinical domains, whereas performance degrades under high semantic ambiguity. Explanatory stability directly mirrors predictive certainty, exhibiting strong convergence in univalent categories and a marked drop under diagnostic uncertainty. Furthermore, qualitative error auditing uncovers three systemic failure mechanisms: lexical hypersensitivity, semantic overlap, and loss of attribution coherence. The results support the combined use of several explanation methods and quantitative agreement metrics when auditing transformer-based models in medical text classification, and suggest prioritizing specific clinical ontologies over broad diagnostic labels.

---


### 363. [Argo-Bench: Evaluating Data Agents on Enterprise-Scale Workflows](https://arxiv.org/abs/2610.02122)

**<font color=#1a73e8>作者：</font>** Gabriel Tomitsuka, Arman Raayatsanati, Emma Xing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world enterprise data science and analytics workflows require reasoning across dozens of tables, performing statistical analyses, and acting on the results. Established text-to-SQL benchmarks evaluate query generation alone, and audits have found their answer keys frequently wrong. Because real enterprise warehouses are too sensitive to release, these benchmarks are built on public datasets where a business event fits in a single table. We introduce Argo-Bench, an evaluation framework comprising 210 data science and analytics tasks. Drawing on public data, peer-reviewed industry literature, and regulatory filings, we simulate a food delivery platform in New York City at true scale, with 81 million orders in 2024, grounded economics, fraud patterns, and marketplace incentives. We export this world to an ERP warehouse of 235 tables and 7.5 billion rows, modeled on the Oracle E-Business Suite schema. The simulator's ground-truth state is withheld from the warehouse the agent sees, so tasks require reconstructing facts by navigating the warehouse before acting on them. Argo-Bench goes beyond text-to-SQL: the agent files actions such as banning fraudulent accounts, allocating courier incentive budgets, or issuing back pay, and the grader scores each by its consequences in the simulator. Every task has an executable reference solution that demonstrates solvability using only the warehouse. The strongest of 14 frontier and open-weight models scores 95 or higher on only 34.8% of tasks and averages 59.5 points. We hope Argo-Bench drives progress toward agents that understand, navigate, and act within real data environments.

---


### 364. [Linear Programming Representations and Strongly Polynomial Algorithms for Robust Markov Decision Processes](https://arxiv.org/abs/2610.02131)

**<font color=#1a73e8>作者：</font>** Han Zhong, Yinyu Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study linear programming (LP) representations and strongly polynomial algorithms for robust Markov decision processes (RMDPs) with rational polyhedral state-action rectangular uncertainty in rewards and transitions. By encoding a finite sequence of robust policy-iteration steps, we construct a single LP whose optimal solutions recover the robust optimal value and all optimal stationary randomized policies. At fixed discount, the LP has polynomial dimension and encoding length and can be constructed in strongly polynomial time. We also develop a general complexity analysis of robust policy iteration that combines the cost of minimizing over uncertainty sets with the number of iterations needed to evaluate a policy. For a fixed discount factor, we use this analysis to improve the known complexity bounds for $\ell_1$ and $\ell_\infty$ RMDPs and establish new strongly polynomial bounds for general interval, weighted $\ell_1$, and Wasserstein RMDPs, as well as turn-based stochastic games with these uncertainty sets.

---


### 365. [MIRTO: a registration-gated, multiverse-tested evaluation protocol for unsupervised anomaly segmentation in brain MRI](https://arxiv.org/abs/2610.02136)

**<font color=#1a73e8>作者：</font>** Negin Kafee Hernashki, Soumick Chatterjee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised anomaly detection (UAD) methods for brain MRI are ranked by a single score, yet that score rests on choices that are rarely reported: how each anomaly map is aligned with the reference, how and on which data the threshold is set, and which false-positive budget, metric, aggregation and lesion definition are used. We present MIRTO, an evaluation protocol that makes these choices explicit and measures their effect. It gates the geometry of every comparison with a registration check and label-free diagnostics of known power, sets thresholds on validation data alone and reports the false-positive volume actually realised on test, repeats each comparison over 15,552 defensible evaluation pipelines, and attaches paired subject-bootstrap intervals with multiplicity control. Applied to four UAD methods trained on the same healthy data and tested on 312 BraTS 2020 subjects, MIRTO showed that an axis-order mismatch between stored maps and the reference lowered a diffusion model's voxel AUROC from 0.873 to 0.583 whilst barely moving its slice-level AUROC. Within each metric, the method explained at least 0.95 of the variance in voxel AUROC and AUPRC and 0.77 in Dice, but only 0.14 in lesion sensitivity, where the lesion definition and hit criterion dominated. A Dice advantage that was significant at validation thresholds vanished at equal realised false-positive burden, and an exact identity attributes it to threshold transfer. A training-free change to REFLECT's latent aggregation raised Dice at equal burden by 0.052. Nine hypotheses were tested against explicit criteria; because the same cohort served to develop the protocol, all inference is exploratory.

---


### 366. [Finetuning with Sampling: SFT Learns Better Than You Think](https://arxiv.org/abs/2610.02140)

**<font color=#1a73e8>作者：</font>** Aayush Karan, Sitan Chen, Yilun Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Introducing new capabilities to frontier models has long been the goal of posttraining, which predominantly employs supervised finetuning (SFT) and reinforcement learning (RL) to this end. Conventional wisdom dictates that RL enables strong generalization on new tasks without losing existing capabilities, while SFT is prone to weak generalization and catastrophic forgetting. At the same time, SFT can learn from off-policy expert data, whereas RL must rely on a model's ability to find successful trajectories with repeated sampling. In our work, we seek to leverage the strength of on-policy learning while utilizing the privileged information contained in off-policy data. However, rather than modifying the learning objective to accommodate this data, we instead tailor the data distribution to better suit the learner. We introduce a Markov chain Monte Carlo (MCMC) sampling algorithm that progressively transforms off-policy traces to be more on-policy given a reference model for finetuning. Across tasks like scientific skill acquisition, mathematical reasoning, and open-ended expertise, our sampling algorithm enables SFT to rival prevailing posttraining techniques, often generalizing better and forgetting less than strong on-policy baselines. In addition, the resulting finetuned models exhibit strong distributional performance and are capable of learning beyond sharpening the base model distribution. At a higher level, our approach presents sampling as a model-native operator that shapes data for learnability, offering broader utility as a general-purpose primitive throughout the posttraining stack.

---


### 367. [Faynt: Scaling and Optimizing Policies for Competitive Melee](https://arxiv.org/abs/2610.02144)

**<font color=#1a73e8>作者：</font>** Ali Janati, Nikita Kuzmin, Rohit Swamy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Faynt, a family of 10M- and 75M-parameter Transformer policies for Super Smash Bros. Melee, each controlling all 26 characters with a single checkpoint. After reinforcement learning (RL), the 10M wins 240 of 244 same-character games (98.4%) against fourteen specialist and multi-character releases on their supported rosters, with a winning record against every release. These opponents retain 21- or 24-frame action delays; Faynt uses no added delay, and we have not isolated the effect of this difference. In a separate evaluation against a privately supplied zero-delay Slippi-AI model, the 10M wins all 68 games across two conditioning settings. We study architecture, optimization, scaling, and hyperparameter transfer to guide pretraining on approximately 840,000 human replays. Post-training combines rank- and outcome-based curricula, 75M-to-10M distillation, and RL restricted to Fox mirror matches. On the initial 152-game benchmark, the supervised 10M wins 69.7% of games, compared with 45.4% for the pretrained 75M, despite higher overall held-out controller-prediction loss. The weighted validation loss used for supervised checkpoint selection agrees with the win-rate ordering of all four pretrained and supervised policies. After supervised post-training, both models take less damage per minute, build larger early leads, and win more often after losing the first life. Optimized inference on recorded game states averages 5.2 ms per decision for the 10M and 8.7 ms for the 75M on an NVIDIA T4, excluding emulator execution and communication. We open-source the weights, both benchmark suites, and a platform for automated model tournaments.

---


### 368. [MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation](https://arxiv.org/abs/2610.02153)

**<font color=#1a73e8>作者：</font>** Yiwen Zhang, Haocheng Xi, Michael Tian-Yue Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon autoregressive video generation is limited by a finite context window. When an object or scene falls out of context, its fine-grained visual details may be lost and difficult to recover upon reappearance. To retain access to such visual details, we introduce MosaiChunk, a spatio-temporal memory mechanism that composes a mosaic of selected historical key-value (KV) entries across space and time. Our approach is motivated by the observation that a frozen video generator can directly consume such non-contiguous historical KV and recover the corresponding visual content. We therefore keep the generator fixed and learn only a lightweight router that determines which historical sections to include in the mosaic under a fixed active-memory budget. We further introduce RememBench, a benchmark of long-horizon revisits with prompt-driven text-to-video (T2V) and camera-driven image-to-video (I2V) splits. Our experiments show that MosaiChunk consistently improves revisit consistency over both sliding-window inference and whole-chunk retrieval under matched memory budgets, across both T2V and I2V settings.

---


### 369. [Muon meets Tamed Langevin: Momentum Preconditioning beyond Convex and gradient-Lipschitz Potentials](https://arxiv.org/abs/2610.02158)

**<font color=#1a73e8>作者：</font>** Nikolaos Makras, Sotirios Sabanis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of sampling from Gibbs distributions on matrix spaces whose potential energies are neither convex nor globally gradient-Lipschitz. We introduce a family of non-quadratic kinetic energies that lead to a new underdamped Langevin system with momentum preconditioning, in which the gradient of the kinetic energy acts as a smooth spectral taming of the momentum. We prove that, under these relaxed assumptions on the potential, the resulting dynamics leaves the target Gibbs measure invariant, and we establish exponential convergence to equilibrium in a weighted total variation distance. Finally, we show that the corresponding Euler-Maruyama discretization admits moment bounds that are uniform in time, without any modification of the potential gradient, which ensures the stability of the resulting sampling algorithm.

---


### 370. [When Do Intrinsic Rewards Lead to Exploration?](https://arxiv.org/abs/2610.02159)

**<font color=#1a73e8>作者：</font>** Scott W. Viteri, Laura Gomezjurado Gonzalez, Clark Barrett  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intrinsic rewards are designed to guide exploration in reinforcement learning by assigning value to an agent's experience, for example through prediction error or learning progress. However, maximizing these rewards need not produce the most informative experience available. We propose a formal criterion for exploration that compares policies by the counterfactual information they acquire: how well their histories can substitute for experience under alternative policies. We construct a single, simple environment in which specified count-based, prediction-error, empowerment, and information-gain objectives have maximizing policies that are Pareto-suboptimal at acquiring counterfactual information. We explain these failures and establish conditions under which existing intrinsic rewards successfully encourage optimal exploration. We also construct an objective that assigns a higher value whenever exploration strictly improves under our criterion.

---


### 371. [4Director: Controlling Video World Models with Rigid 3D Geometry](https://arxiv.org/abs/2610.02160)

**<font color=#1a73e8>作者：</font>** Wei Cao, Hao Zhang, Vikram Voleti 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise control over camera and object motion is essential for professional video production. Existing methods control objects only coarsely, through image-plane cues that are ambiguous in depth and rotation or through 3D tracks and blobs that lack complete geometry and lose consistency across viewpoint changes. We introduce 4Director, a video world model conditioned on an explicit 4D scene representation: each object is reconstructed once from the input image as a canonical mesh and moved by one prescribed rigid transformation per frame. This representation provides an intuitive 3D control interface and prevents unobserved geometry from being regenerated independently in every frame. We render the controlled scene as a depth video and introduce a Motion Adapter that transforms this geometric scaffold into video while synthesizing view-consistent appearance, illumination, and non-rigid dynamics. For training, we construct RealCOD-Rigid, a new dataset of 20,774 clips annotated with rigid 3D scenes by our automatic pipeline. We further introduce Identity-Gated IoU (IG-IoU), which jointly evaluates adherence to prescribed object motion and preservation of object identity. Experiments demonstrate that 4Director consistently outperforms prior methods in visual quality and in camera and object control.

---


### 372. [World Observer: Joint Actor-Observer Generation for Persistent World Modeling](https://arxiv.org/abs/2610.02162)

**<font color=#1a73e8>作者：</font>** Hyunwook Choi, Dahyun Chung, Hyunsung Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How can a world model continuously observe regions beyond the actor's current view? Video world models simulate how an environment evolves from an agent's actions, yet remain actor-centric. Once an object leaves the actor's view, they lose direct evidence of its evolution, often failing to preserve its state and dynamics upon re-entry. To address this, we introduce World Observer, which decouples observing from acting by jointly generating a perspective actor for the agent-centric view with one or more panoramic observers that watch selected world regions. This allows objects that leave the actor's view to remain visually evolving in an observer, so their updated states are reflected when they re-enter. We ground the actor and observers by warping from a shared panoramic source for explicit geometric correspondence, and introduce an Observer Sink of high-resolution perspective references to restore fine appearance upon re-entry. Since the observers are decoupled from the actor, they can be placed freely across the scene, extended to multiple locations for broader coverage, and driven by control signals to steer out-of-view evolution. To evaluate out-of-view evolution, we further introduce world-space metrics and a benchmark spanning real and synthetic scenes. World Observer substantially improves out-of-view dynamics while remaining competitive in visual fidelity, camera control, and 3D adherence.

---


### 373. [Effective Resistance and Graph Neural Network Reliability in Tissue-Specific Interactomes](https://arxiv.org/abs/2610.02175)

**<font color=#1a73e8>作者：</font>** Jianru Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein function annotation needs to know which predictions to distrust, not only what a model predicts. We ask whether tissue-specific interaction structure carries that information. Our candidate signal is effective resistance, used previously to relieve over-squashing by rewiring. Across 24 tissue-specific interactomes it is dominated by inverse degree, and the degeneration deepens as the co-expression filtered network grows, with a Spearman correlation of -0.955. The residual departure from that limit exceeds degree-preserving null graphs in all 24 networks. Controlling for predictive entropy, degree, annotation cardinality, local structure and feature-only difficulty, the residual explains additional per-node loss in 19 of 24 held-out networks once a permutation floor is subtracted, at every depth, and the effect strengthens monotonically with depth. The increment reaches 0.37% of the variance the controls leave unexplained, 5.6 times a permutation floor, against 1.5 times when the model is retrained in a degree-preserving null world. Selective prediction improves negligibly. The signal is reproducible; degree degeneration bounds it.

---


### 374. [Generative Cinematographer: Composing Camera and Object Motion in 3D](https://arxiv.org/abs/2610.02180)

**<font color=#1a73e8>作者：</font>** Jiahan Zhang, Chaohao Yang, Namitha Guruprasad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current controllable video generation systems often rely on 2D motion trajectories or sparse drag signals for object motion. These controls are ambiguous because the same 2D trajectory can correspond to different 3D motions, especially when the camera and objects move simultaneously. We present Generative Cinematographer (GenCine), a system that lifts a single image into an editable 3D scene scaffold where artists jointly author camera and foreground motion. Artists specify a camera path and move selected foreground regions using local 3D motion handles. Several handles can move different parts of a subject independently, providing a piecewise-rigid approximation to non-rigid motion without a physics simulator or category-specific prior. To communicate these controls to a pretrained video model, we project them into guidance maps. These maps record where the controlled regions appear in each frame, assign each handle a fixed color across frames and encode the current 3D positions of its controlled points in the same world coordinate system as the background. This lets us describe object motion relative to the scene even as the camera moves. For training, we recover controls from the motion observed in real videos and use ground-truth geometry and trajectories from synthetic videos. We train a lightweight guidance branch and LoRA adapters on a pretrained Wan model to follow these controls. Our experiments show consistent camera-relative motion, improved geometric consistency under viewpoint changes, and strong controllability across diverse real-world scenes.

---


### 375. [SoftServe: A Scalable Quasi-Newton Method for Deep Learning](https://arxiv.org/abs/2610.02182)

**<font color=#1a73e8>作者：</font>** Joohwan Ko, Tetiana Parshakova, Diana Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quasi-Newton (QN) methods have long been among the most effective methods for large-scale unconstrained convex optimization. Two obstacles have limited their use in deep learning: non-convexity and enormous parameter sizes. We introduce SoftServe, a family of QN methods designed to overcome these obstacles without line searches or ad hoc curvature corrections. SoftServe derives positivedefinite curvature estimates from the variational objective of Berglund et al. (2025), even in the presence of negative curvature. We develop diagonal and Kroneckerfactored variants that preserve positive definiteness by construction and scale to massive neural networks. Finally, SoftServe relies on the stable coupled Newton-Schulz iteration for the required matrix operations, replacing costly matrix decompositions with GPU-friendly matrix multiplications. SoftServe excels on problems that are severely ill-conditioned, including tasks such as recurrent networks, deep autoencoders, physics-informed neural networks, and a 136M-parameter physics-informed diffusion model, often achieving lower losses than established baselines including Adam, Muon, and SOAP.

---


### 376. [Decoding Looped Transformers Better for (Almost) Free](https://arxiv.org/abs/2610.02185)

**<font color=#1a73e8>作者：</font>** Weihao Liu, Huangjie Zheng, Tianrong Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers achieve parameter efficiency by repeatedly executing a shared block across recurrent loops. Each loop yields an intermediate representation decodable for the same next token, yet standard decoding discards earlier states. Because earlier loops embody less computation, recurrence inherently supplies aligned weak-and-strong prediction pairs without auxiliary models or external training. We introduce LoopCD, a training-free contrastive decoding framework that guides token selection by contrasting the final prediction with an earlier recurrent pass, operating either in logit space with one extra output pass (LoopCD-Logits) or in hidden-state space with zero output overhead (LoopCD-Hidden). Across four looped Transformer families, LoopCD delivers substantial, consistent gains at full recurrent depth: LoopCD-Logits raises Ouro-2.6B-Thinking's AIME 2024 pass@1 from 61.88% to 73.33%, while LoopCD-Hidden lifts Huginn's HumanEval pass@1 from 22.56% to 31.71%. Crucially, these performance gains enable halving the number of recurrent loops while still matching or exceeding full-depth unguided baselines, reducing forward FLOPs by 22.5% to 48.2%. By transforming intermediate recurrent states into effective guidance signals, LoopCD achieves superior decoding quality while substantially reducing inference compute.

---


### 377. [DMAD: Distribution Matching as Adversarial Distillation for Fast Visual Generation](https://arxiv.org/abs/2610.02188)

**<font color=#1a73e8>作者：</font>** Zhengming Yu, Junkun Yuan, Haotian Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution Matching Distillation (DMD) trains a few-step student from the difference between separately estimated target and student scores, so it must keep an auxiliary diffusion model fitted to the student's evolving distribution at extra memory and computation cost. We introduce DMAD, Distribution Matching as Adversarial Distillation, which recasts distribution matching as classification and learns the required log-density ratios directly. Two discriminator heads on a shared backbone distinguish real data and teacher samples from the student's, and linear losses on their logits train the student without auxiliary score fitting. We prove that at the discriminator optimum these losses recover the distribution-matching gradient underlying DMD, through the classical identity linking discriminator logits to log-density ratios. We further introduce gap-based reweighting, which adapts teacher supervision across noise levels from the real-data head's empirical logit gap between real and teacher samples. DMAD reaches a Fréchet Inception Distance (FID) of 1.04 with one-step generation on ImageNet-64x64, 14.47 with four-step SDXL on COCO-10K, and a VBench total score of 85.15 with four-step Wan2.1-T2V-14B, the best values among the compared few-step methods and the multi-step teachers. On MiniMax-H3-33B, our four-step student achieves overall human preference rates of 79.1% over DMD2 and 84.6% over rCM for joint audio-video generation, excluding ties. Our code, models and demos are available at this https URL.

---


### 378. [Cost-augmented Schrödinger bridges on graphs are exactly solvable: a Feynman-Kac tilt replaces learned control](https://arxiv.org/abs/2610.02195)

**<font color=#1a73e8>作者：</font>** Akshay Balsubramani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The generalized Schrödinger bridge on a graph moves mass between two distributions while charging a cost for the states visited. It has been approached by learning the rates of a controlled continuous-time Markov chain, with a temporal-difference penalty that restores the cost. A state cost folds into the reference process as a Feynman-Kac tilt. The cost-augmented bridge is then a plain bridge against the tilted reference, and the penalty is unnecessary. The bridge is computed exactly by alternating two endpoint rescalings, each one sparse matrix-exponential application; nothing is discretized in time or learned. The alternation converges at a rate set by the endpoint coupling alone. For a quadratic congestion cost on time-averaged occupancies, damped best response around the exact bridge is gradient descent on a strongly convex function, and its residual bounds its error. On a protein-folding model, a free-energy cost lowers the expected barrier of the folding paths. On the learned approach's road network, roll-outs of the exact bridge match the target within sampling error, and on networks with millions of intersections its memory grows linearly.

---


### 379. [HiPhy: Hierarchical Alignment for Physically-Plausible Multi-Principle Video Generation](https://arxiv.org/abs/2610.02197)

**<font color=#1a73e8>作者：</font>** Tahira Kazimi, Shubhankar Borse, Munawar Hayat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models have achieved remarkable visual fidelity and have strong potential to become general-purpose world simulators. Despite this progress, they still fail to generate videos which adhere to laws of physics. The problem becomes even more apparent in realistic settings where multiple physical principles must work together within the same video; for example, "a balloon floating upward while steam rises from a pot" requires buoyancy and fluid dynamics to unfold coherently and simultaneously. Yet existing methods largely ignore multi-principle interactions, focusing on a single principle per video. We propose HiPhy (Hierarchical Physical Alignment), a reinforcement learning framework that grounds video generation in physical laws through a dual-level objective: locally enforcing the temporal dynamics of individual physical principles, and globally ensuring the physical and semantic coherence of the entire scene. To support multi-principle generation, we construct a 50K-prompt dataset and introduce a prompt benchmark MultiPhyBench, spanning a diverse range of co-occurring physical events. Our experiments show that HiPhy significantly outperforms prior methods and baselines, improving physical commonsense and semantic alignment significantly across various benchmarks, with the largest gains on scenes involving multiple concurrent physical principles where competing methods degrade most sharply.

---


### 380. [FERPO: Forward Entropy-Regularized Policy Optimization](https://arxiv.org/abs/2610.02198)

**<font color=#1a73e8>作者：</font>** Sebastian Sanokowski, Alireza Sarmadi, Majid Khadiv  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Several state-of-the-art methods for online reinforcement learning in continuous control improve policies using action gradients of a learned critic. However, critics are typically trained to predict returns, and accurate value predictions do not necessarily yield accurate action derivatives, potentially leading to unreliable policy updates. We propose Forward Entropy-Regularized Policy Optimization (FERPO), an on-policy maximum entropy reinforcement learning algorithm that performs policy improvement using critic values without differentiating the critic with respect to actions. FERPO derives an optimal target action distribution from a policy-improvement objective regularized by entropy and Kullback-Leibler (KL) divergence. We then fit the actor to this target by minimizing a forward-KL objective, estimated using self-normalized importance sampling (SNIS) with actions drawn from the rollout policy. By limiting the target distribution's deviation from the rollout policy, the KL regularization helps keep these importance weights well behaved. In contrast to reverse-KL objectives, which can favor a subset of the target distribution's modes, the forward-KL objective encourages coverage of multiple high-value modes and thereby promotes exploration. Experiments and ablations on MuJoCo Playground and ManiSkill show competitive performance and sample-efficiency gains. Computational benchmarks also demonstrate faster actor updates than Relative Entropy Pathwise Policy Optimization (REPPO).

---


### 381. [SILSA: Sliding-Window Slice Latents for Topology-Preserving High-Resolution 3D Generation](https://arxiv.org/abs/2610.02201)

**<font color=#1a73e8>作者：</font>** Tianjiao Yu, Xinzhuo Li, Yifan Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution 3D generation increasingly relies on voxel latents and multi-stage pipelines that first predict active structure and then synthesize local geometry. While effective, this design fragments continuous surfaces into many local tokens, inflates generation cost, and often weakens topological consistency for thin or highly connected shapes. We introduce SILSA, a topology-aware 3D generation framework that represents shapes with compact sliding-window slice latents. Instead of generating expensive voxel tokens, SILSA uses a fixed set of overlapping slices along the three canonical axes, where each token summarizes a local depth window to preserve cross-sectional continuity and support single-stage rectified-flow generation. A Slice VAE encodes oriented surface samples into multi-axis slice latents and reconstructs them with a sparse volumetric decoder, while a Volumetric Anchor Lattice coordinates directional slice streams through a shared 3D workspace. To preserve structural correctness, we introduce slice-level topology supervision that matches persistence diagrams and aligns Betti transitions across neighboring slices. Experiments show that SILSA improves structural fidelity while substantially reducing generation cost. SILSA improves PSNR by $8.7\%$, coverage by $5.96$ absolute points, and Betti error by $9.2\%$ over the strongest baseline, while using $70.0\%$ fewer tokens than the next-most compact baseline and over $98\%$ fewer tokens than sparse or hierarchical tokenizers, effectively reducing training memory by $40.4\%$ and inference time by $58.5\%$. Qualitative results further show improved preservation of thin structures, repeated components, and long-range connectivity.

---


### 382. [Embedding Prediction Helps Image Generation](https://arxiv.org/abs/2610.02203)

**<font color=#1a73e8>作者：</font>** Sihan Xu, Ji Xie, Zilin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In diffusion transformers, a class label or a text prompt is embedded once, and the same condition is reused at every denoising step. We ask whether predicted embeddings can serve as this condition instead. Next-Embedding Predictive Autoregression (NEPA) trains a Transformer to predict the next continuous embedding in a sequence. In generation, the clean image follows the noisy image, so its embeddings are the next embeddings after the condition and the noisy image. We train a NEPA model to predict them all at once with Multi-Embedding Prediction, and in Embedding Conditioned Generation, a DiT generator is conditioned on these predictions, recomputed at every denoising step, so the conditioning signal adapts to the current noisy state. Experiments on class-conditional ImageNet $256\times256$ study the condition of the generator, the design of Multi-Embedding Prediction, and the scaling of both models. The NEPA model adds a second network to every sampling step; with it, and combined with REPA, our final model, NEPA-DiT-XL, reaches an FID of 1.32 using about a third of the training compute of REPA.

---


### 383. [One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars](https://arxiv.org/abs/2610.02207)

**<font color=#1a73e8>作者：</font>** Ramazan Fazylov, Stamatis Lefkimmiatis, Ivan Laptev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian avatars support fast rendering, however, their real-time animation is often challenged by the costly neural inference. We address this bottleneck and show that the animation of pretrained avatar models can be closely approximated by a linear combination of identity-independent blendshapes. Building on this finding, we introduce GALA (Gaussian Animation via Linear Approximation), a distillation method that replaces per-frame heavy neural decoding with a shallow coefficient predictor and a linear blend. To improve fidelity and reduce memory requirements, we propose to construct the basis using block-local PCA under a rendering-aware metric and a memory budget. Our method learns a shallow MLP network to predict blendshape coefficients and applies to various animation architectures without retraining original models. We validate GALA by accelerating the inference of three distinct avatar models for 3D animation of facial expressions and full-bodies with clothing dynamics. Across these models, our distillation generalizes to held-out identities and reduces CPU animation cost by up to three orders of magnitude while preserving most of the rendering quality. Excellent results of our method confirm the shared linear structure of learned avatar representations and enable highly efficient and accurate animation at frame rates reaching up to 60fps on mobile devices. Project page: this https URL

---


### 384. [Sphere Encoder 2](https://arxiv.org/abs/2610.02208)

**<font color=#1a73e8>作者：</font>** Kaiyu Yue, Sean McLeish, Ruchit Rawal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sphere Encoder is an autoencoder that generates images by decoding random points from a high-dimensional latent sphere. We identify two limitations of the original formulation that reduce its generation quality. First, random points concentrate near the equator relative to the pole on an encoded latent, but the training rotation never reaches this region, leaving a gap that limits one-step generation. Second, training for generation with pixel-wise reconstruction loss encourages the decoder to average over plausible images, producing blurry images that lack high-frequency details. We present Sphere Encoder 2 to address both limitations, substantially improving image generation quality while maintaining the speed and simplicity of a autoencoder. Models are released at \href{this https URL}{this http URL}.

---


### 385. [Moore, Escher, Penrose: A Conformal Golden Braid](https://arxiv.org/abs/2610.02210)

**<font color=#1a73e8>作者：</font>** Sophia Feldman, Assaf Shocher  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> I don't think I have ever done anything as peculiar in my life. Among other things, it shows a young man looking with interest at a print on the wall of an exhibition that features himself. How can this be? Perhaps I am not far removed from Einstein's curved universe.'' So wrote M.C. Escher about his 1956 lithograph Print Gallery. Nearly half a century later, a mathematical analysis related its geometry to an untwisted source image through a conformal power map $z \mapsto z^\alpha$, $\alpha \in \mathbb{C}$. Building on this construction, we use a frozen text-to-image diffusion model to generate new self-referential scenes. Prompting alone does not enforce the recursion, while a post-hoc transformation can leave structures poorly connected. Applying the transformation during sampling is also insufficient: the denoiser may "repair" the intended distortion or drift out of the prescribed geometry. We construct a generalized inverse $T^\dagger$ of the non-invertible image transformation $T$, adapted to its recursive constraint. In the idealized formulation, the Penrose identity $TT^\dagger T = T$ makes $TT^\dagger$ an idempotent projection onto geometrically admissible images. Yet denoising only the transformed image remains an out-of-distribution task, even with projection. We therefore braid denoising steps with $T$ and $T^\dagger$: source-space steps develop the untwisted scene, while transformed-space steps refine its appearance and connections in the final geometry. We generate Print Gallery-like compositions and explore further transformations. Rather than distorting a finished image, we let the scene and its distortion develop together.

---


> [!TIP]
> 当前位于：**351-385**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-385**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
