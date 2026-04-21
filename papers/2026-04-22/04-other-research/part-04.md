# 📦 其他研究 | 2026年04月22日

> 本类共 **535** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

---

### 151. [Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI](https://arxiv.org/abs/2604.16875)

**<font color=#1a73e8>作者：</font>** Nils Leutenegger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central question in computational neuroscience is whether the learning rule used to train a neural network determines how well its internal representations align with those of the human visual cortex. We present a systematic comparison of four learning rules -- backpropagation (BP), feedback alignment (FA), predictive coding (PC), and spike-timing-dependent plasticity (STDP) -- applied to identical convolutional architectures and evaluated against human fMRI data from the THINGS-fMRI dataset (720 stimuli, 3 subjects) using Representational Similarity Analysis (RSA). Crucially, we include an untrained random-weights baseline that reveals the dominant role of architecture. We find that early visual alignment (V1/V2) is primarily architecture-driven: an untrained CNN achieves rho = 0.071, statistically indistinguishable from BP (rho = 0.072, p = 0.43). Learning rules only differentiate at higher visual areas: BP dominates at LOC/IT, and PC with local Hebbian updates achieves IT alignment statistically indistinguishable from BP (p = 0.18). FA consistently impairs representations below the random baseline at V1. Partial RSA confirms all effects survive pixel-similarity control. These results demonstrate that the relationship between learning rules and cortical alignment is region-specific: architecture determines early alignment, while supervised objectives drive late alignment.

---


### 152. [OC-Distill: Ontology-aware Contrastive Learning with Cross-Modal Distillation for ICU Risk Prediction](https://arxiv.org/abs/2604.16878)

**<font color=#1a73e8>作者：</font>** Zhongyuan Liang, Junhyung Jo, Hyang-Jung Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early prediction of severe clinical deterioration and remaining length of stay can enable timely intervention and better resource allocation in high-acuity settings such as the ICU. This has driven the development of machine learning models that leverage continuous streams of vital signs and other physiological signals for real-time risk prediction. Despite their promise, existing methods have important limitations. Contrastive pretraining treats all patients as equally strong negatives, failing to capture clinically meaningful similarity between patients with related diagnoses. Meanwhile, downstream fine-tuning typically ignores complementary modalities such as clinical notes, which provide rich contextual information unavailable in physiological signals alone. To address these challenges, we propose OC-Distill, a two-stage framework that leverages multimodal supervision during training while requiring only vital signs at inference. In the first stage, we introduce an ontology-aware contrastive objective that exploits the ICD hierarchy to quantify patient similarity and learn clinically grounded representations. In the second stage, we fine-tune the pretrained encoder via cross-modal knowledge distillation, transferring complementary information from clinical notes into the model. Across multiple ICU prediction tasks on MIMIC, OC-Distill demonstrates improved label efficiency and achieves state-of-the-art performance among methods that use only vital signs at inference.

---


### 153. [Towards Fully Parameter-Free Stochastic Optimization: Grid Search with Self-Bounding Analysis](https://arxiv.org/abs/2604.16888)

**<font color=#1a73e8>作者：</font>** Yuheng Zhao, Yu-Hu Yan, Amit Attia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-free stochastic optimization aims to design algorithms that are agnostic to the underlying problem parameters while still achieving convergence rates competitive with optimally tuned methods. While some parameter-free methods do not require the specific values of the problem parameters, they still rely on prior knowledge, such as the lower or upper bounds of them. We refer to such methods as ``partially parameter-free''. In this work, we target achieving ``fully parameter-free'' methods, i.e., the algorithmic inputs do not need to satisfy any unverifiable condition related to the true problem parameters. We propose a powerful and general grid search framework, named \textsc{Grasp}, with a novel self-bounding analysis technique that effectively determines the search ranges of parameters, in contrast to previous work. Our method demonstrates generality in: (i) the non-convex case, where we propose a fully parameter-free method that achieves near-optimal convergence rate, up to logarithmic factors; (ii) the convex case, where our parameter-free methods are competitive with strong performance in terms of acceleration and universality. Finally, we contribute a sharper guarantee for the model ensemble, a final step of the grid search framework, under interpolated variance characterization.

---


### 154. [Prune, Interpret, Evaluate: A Cross-Layer Transcoder-Native Framework for Efficient Circuit Discovery via Feature Attribution](https://arxiv.org/abs/2604.16889)

**<font color=#1a73e8>作者：</font>** Qinhao Chen, Linyang He, Nima Mesgarani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing feature-interpretation pipelines typically operate on uniformly sampled units, but only a small fraction of cross-layer transcoder (CLT) features matter for a target behavior, with the rest resulting in expensive feature explaining and evaluating costs. We introduce the first CLT-native end-to-end framework, PIE, connecting Pruning, automatic Interpretation, and interpretation Evaluation, enabling systematic measurement of behavioral fidelity and downstream interpretability under pruning. To achieve this, we propose Feature Attribution Patching (FAP), a patch-grounded attribution method that scores CLT features by aggregating gradient-weighted write contributions, and FAP-Synergy, a synergy-aware reranking procedure. We evaluate pruning using KL-divergence behavior retention and assess interpretation quality with FADE-style metrics. Across IOI and Doc-String, across budgets $K \in \{50, 100, 200, 400, 800\}$, and across FAP, FAP-Synergy, Activation-Magnitude, and ACDC-style pruning, the FAP family consistently achieves the best or near-best fidelity, with FAP-Synergy providing its clearest gains in strict-budget regimes. On IOI with CLTs for Llama-3.2-1B and Gemma-2-2B, pruning to $K=100$ features matches the KL fidelity that random selection from the active feature set requires $\approx 4$k features to achieve ($\approx 40\times$ compression), enabling $\approx 40\times$ fewer interpretation/evaluation calls while substantially reducing low-quality features.

---


### 155. [Step-GRPO: Internalizing Dynamic Early Exit for Efficient Reasoning](https://arxiv.org/abs/2604.16890)

**<font color=#1a73e8>作者：</font>** Benteng Chen, Weida Wang, Shufei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models that use long chain-of-thought excel at problem-solving yet waste compute on redundant checks. Curbing this overthinking is hard: training-time length penalties can cripple ability, while inference-time early-exit adds system overhead. To bridge this gap, we propose Step-GRPO, a novel post-training framework that internalizes dynamic early-exit capabilities directly into the model. Step-GRPO shifts the optimization objective from raw tokens to semantic steps by utilizing linguistic markers to structure reasoning. We introduce a Dynamic Truncated Rollout mechanism that exposes the model to concise high-confidence trajectories during exploration, synergized with a Step-Aware Relative Reward that dynamically penalizes redundancy based on group-level baselines. Extensive experiments across three model sizes on diverse benchmarks demonstrate that Step-GRPO achieves a superior accuracy-efficiency trade-off. On Qwen3-8B, our method reduces token consumption by 32.0\% compared to the vanilla model while avoiding the accuracy degradation observed in traditional length-penalty methods.

---


### 156. [CrossFlowDG: Bridging the Modality Gap with Cross-modal Flow Matching for Domain Generalization](https://arxiv.org/abs/2604.16892)

**<font color=#1a73e8>作者：</font>** Antonios Kritikos, Nikolaos Spanos, Athanasios Voulodimos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain generalization (DG) aims to maintain performance under domain shift, which in computer vision appears primarily as stylistic variations that cause models to overfit to domain-specific appearance cues rather than class semantics. To overcome this, recent methods use textual representations as stable, domain-invariant anchors. However, multimodal approaches that rely on cosine similarity-based contrastive alignment leave a modality gap where image and text embeddings remain geometrically separated despite semantic correspondence. We propose CrossFlowDG, a novel DG framework that addresses this residual gap using noise-free, cross-modal flow matching. By learning a continuous transformation in the joint Euclidean latent space, our framework explicitly transports domain-biased image embeddings toward domain-invariant text embeddings of the correct class. Using the efficient VMamba image encoder and CLIP's text encoder, CrossFlowDG is tested against four common DG benchmarks, and achieves competitive performance on several benchmarks and state-of-the-art on TerraIncognita. Code is available at: this https URL

---


### 157. [Covariance-Based Structural Equation Modeling in Small-Sample Settings with $p>n$](https://arxiv.org/abs/2604.16894)

**<font color=#1a73e8>作者：</font>** Hiroki Hasegawa, Aoba Tamura, Yukihiko Okada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Factor-based Structural Equation Modeling (SEM) relies on likelihood-based estimation assuming a nonsingular sample covariance matrix, which breaks down in small-sample settings with $p>n$. To address this, we propose a novel estimation principle that reformulates the covariance structure into self-covariance and cross-covariance components. The resulting framework defines a likelihood-based feasible set combined with a relative error constraint, enabling stable estimation in small-sample settings where $p>n$ for sign and direction. Experiments on synthetic and real-world data show improved stability, particularly in recovering the sign and direction of structural parameters. These results extend covariance-based SEM to small-sample settings and provide practically useful directional information for decision-making.

---


### 158. [Physics-Informed Tracking (PIT)](https://arxiv.org/abs/2604.16895)

**<font color=#1a73e8>作者：</font>** Emil Hovad, Allan Peter Engsig-Karup  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Physics-Informed Tracking (PIT), a video-based framework for tracking a single particle from video, where a neural network autoencoder localizes a particle as a heatmap peak (landmark) and a differentiable physics module embedded in the autoencoder constrains several landmarks over time (a trajectory) to satisfy known dynamics. The novel Physics-Informed Landmark Loss (PILL) compares this predicted trajectory back against the landmarks, enforcing physical consistency without labels. Its supervised variant (PILLS) instead compares the prediction against ground-truth position, velocity, and bounce from simulation, enabling end-to-end backpropagation. To support supervised and unsupervised learning, we use an autoencoder with a split bottleneck that separates A) tracking-related structure via landmark heatmaps from B) background noise and subsequent image reconstruction. We evaluate a replicated 26 factorial design (n = 4 replicates, 64 configurations), showing that PILLS consistently achieves sub-pixel tracking accuracy for the bilinear and physics-refined decoder outputs under both clean and noisy conditions.

---


### 159. [LAGS: Low-Altitude Gaussian Splatting with Groupwise Heterogeneous Graph Learning](https://arxiv.org/abs/2604.16910)

**<font color=#1a73e8>作者：</font>** Yikun Wang, Yujie Wan, Wei Zuo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-altitude Gaussian splatting (LAGS) facilitates 3D scene reconstruction by aggregating aerial images from distributed drones. However, as LAGS prioritizes maximizing reconstruction quality over communication throughput, existing low-altitude resource allocation schemes become inefficient. This inefficiency stems from their failure to account for image diversity introduced by varying viewpoints. To fill this gap, we propose a groupwise heterogeneous graph neural network (GW-HGNN) for LAGS resource allocation. GW-HGNN explicitly models the non-uniform contribution of different image groups to the reconstruction process, thus automatically balancing data fidelity and transmission cost. The key insight of GW-HGNN is to transform LAGS losses and communication constraints into graph learning costs for dual-level message passing. Experiments on real-world LAGS datasets demonstrate that GW-HGNN significantly outperforms state-of-the-art benchmarks across key rendering metrics, including PSNR, SSIM, and LPIPS. Furthermore, GW-HGNN reduces computational latency by approximately 100x compared to the widely-used MOSEK solver, achieving millisecond-level inference suitable for real-time deployment.

---


### 160. [Skilldex: A Package Manager and Registry for Agent Skill Packages with Hierarchical Scope-Based Distribution](https://arxiv.org/abs/2604.16911)

**<font color=#1a73e8>作者：</font>** Sampriti Saha, Pranav Hemanth  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly extended at runtime via skill packages, structured natural-language instruction bundles loaded from a well-known directory. Community install tooling and registries exist, but two gaps persist: no public tool scores skill packages against Anthropic's published format specification, and no mechanism bundles related skills with the shared context they need to remain mutually coherent. We present Skilldex, a package manager and registry for agent skill packages addressing both gaps. The two novel contributions are: (1) compiler-style format conformance scoring against Anthropic's skill specification, producing line-level diagnostics on description specificity, frontmatter validity, and structural adherence; and (2) the skillset abstraction, a bundled collection of related skills with shared assets (vocabulary files, templates, reference documents) that enforce cross-skill behavioral coherence. Skilldex also provides supporting infrastructure: a three-tier hierarchical scope system, a human-in-the-loop agent suggestion loop, a metadata-only community registry, and a Model Context Protocol (MCP) server. The system is implemented as a TypeScript CLI (skillpm / spm) with a Hono/Supabase registry backend, and is open-source.

---


### 161. [The Cognitive Penalty: Ablating System 1 and System 2 Reasoning in Edge-Native SLMs for Decentralized Consensus](https://arxiv.org/abs/2604.16913)

**<font color=#1a73e8>作者：</font>** Syed Muhammad Aqdas Rizvi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decentralized Autonomous Organizations (DAOs) are inclined explore Small Language Models (SLMs) as edge-native constitutional firewalls to vet proposals and mitigate semantic social engineering. While scaling inference-time compute (System 2) enhances formal logic, its efficacy in highly adversarial, cryptoeconomic governance environments remains underexplored. To address this, we introduce Sentinel-Bench, an 840-inference empirical framework executing a strict intra-model ablation on Qwen-3.5-9B. By toggling latent reasoning across frozen weights, we isolate the impact of inference-time compute against an adversarial Optimism DAO dataset. Our findings reveal a severe compute-accuracy inversion. The autoregressive baseline (System 1) achieved 100% adversarial robustness, 100% juridical consistency, and state finality in under 13 seconds. Conversely, System 2 reasoning introduced catastrophic instability, fundamentally driven by a 26.7% Reasoning Non-Convergence (cognitive collapse) rate. This collapse degraded trial-to-trial consensus stability to 72.6% and imposed a 17x latency overhead, introducing critical vulnerabilities to Governance Extractable Value (GEV) and hardware centralization. While rare (1.5% of adversarial trials), we empirically captured "Reasoning-Induced Sycophancy," where the model generated significantly longer internal monologues (averaging 25,750 characters) to rationalize failing the adversarial trap. We conclude that for edge-native SLMs operating under Byzantine Fault Tolerance (BFT) constraints, System 1 parameterized intuition is structurally and economically superior to System 2 iterative deliberation for decentralized consensus.
Code and Dataset: this https URL

---


### 162. [KIRA: Knowledge-Intensive Image Retrieval and Reasoning Architecture for Specialized Visual Domains](https://arxiv.org/abs/2604.16915)

**<font color=#1a73e8>作者：</font>** Parthaw Goswami, Jaynto Goswami Deep  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval augmented generation (RAG) has transformed text based question answering, yet its extension to visual domains remains hindered by fundamental challenges: bridging the modality gap between image queries and text heavy knowledge bases, constructing semantically meaningful visual knowledge bases, performing multihop reasoning over retrieved images, and verifying that generated answers are faithfully grounded in visual evidence. We present KIRA (Knowledge Intensive Image Retrieval and Reasoning Architecture), a unified five stage framework that addresses ten core problems in visual RAG for specialized domains. KIRA introduces: (1) hierarchical semantic chunking with DINO based region detection for multi granularity knowledge base construction, (2) domain adaptive contrastive encoders with fewshot adaptation for rare visual concepts, (3) dualpath crossmodal retrieval with chainOfThought query expansion, (4) chainOfRetrieval for multihop visual reasoning with temporal and multiview support, and (5) evidence conditioned grounded generation with posthoc hallucination verification. We also propose DOMAINVQAR, a benchmark suite that evaluates visual RAG along three axes (retrieval precision, reasoning faithfulness, and domain correctness) going beyond standard recall metrics. Experiments across four specialized domains (medical Xray, circuit diagrams, satellite imagery, and histopathology) with a progressive six variant ablation demonstrate that KIRA achieves 0.97 retrieval precision, 1.0 grounding scores, and 0.707 domain correctness averaged across domains, while the ablation reveals actionable insights about when each component helps and when components introduce precision diversity tradeoffs that must be managed. Code will be released upon acceptance.

---


### 163. [Noise-Adaptive Diffusion Sampling for Inverse Problems Without Task-Specific Tuning](https://arxiv.org/abs/2604.16919)

**<font color=#1a73e8>作者：</font>** Yingzhi Xia, Setthakorn Tanomkiattikun, Liangli Zhen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models (DMs) have recently shown remarkable performance on inverse problems (IPs). Optimization-based methods can fast solve IPs using DMs as powerful regularizers, but they are susceptible to local minima and noise overfitting. Although DMs can provide strong priors for Bayesian approaches, enforcing measurement consistency during the denoising process leads to manifold infeasibility issues. We propose Noise-space Hamiltonian Monte Carlo (N-HMC), a posterior sampling method that treats reverse diffusion as a deterministic mapping from initial noise to clean images. N-HMC enables comprehensive exploration of the solution space, avoiding local optima. By moving inference entirely into the initial-noise space, N-HMC keeps proposals on the learned data manifold. We provide a comprehensive theoretical analysis of our approach and extend the framework to a noise-adaptive variant (NA-NHMC) that effectively handles IPs with unknown noise type and level. Extensive experiments across four linear and three nonlinear inverse problems demonstrate that NA-NHMC achieves superior reconstruction quality with robust performance across different hyperparameters and initializations, significantly outperforming recent state-of-the-art methods. The code is available at this https URL.

---


### 164. [Adaptive receptive field-based spatial-frequency feature reconstruction network for few-shot fine-grained image classification](https://arxiv.org/abs/2604.16936)

**<font color=#1a73e8>作者：</font>** Linyue Zhang, Wenyi Zeng, Zicheng Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature reconstruction techniques are widely applied for few-shot fine-grained image classification (FSFGIC). Our research indicates that one of the main challenges facing existing feature-based FSFGIC methods is how to choose the size of the receptive field to extract feature descriptors (including spatial and frequency feature descriptors) from different category input images, thereby better performing the FSFGIC tasks. To address this, an adaptive receptive field-based spatial-frequency feature reconstruction network (ARF-SFR-Net) is proposed. The designed ARF-SFR-Net has the capability to adaptively determine receptive field sizes for obtaining spatial and frequency features, and effectively fuse them for reconstruction and FSFGIC tasks. The designed ARF-SFR-Net can be easily embedded into a given episodic training mechanism for end-to-end training from scratch. Extensive experiments on multiple FSFGIC benchmarks demonstrate the effectiveness and superiority of the proposed ARF-SFR-Net over state-of-the-art approaches. The code is available at: this https URL.

---


### 165. [L1 Regularization Paths in Linear Models by Parametric Gaussian Message Passing](https://arxiv.org/abs/2604.16949)

**<font color=#1a73e8>作者：</font>** Yun-Peng Li, Hans-Andrea Loeliger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The paper considers the computation of L1 regularization paths in a state space setting, which includes L1 regularized Kalman smoothing, linear SVM, LASSO, and more. The paper proposes two new algorithms, which are duals of each other; the first algorithm applies to L1 regularization of independent variables while the second applies to L1 regularization of dependent variables. The heart of the proposed algorithms is parametric Gaussian message passing (i.e., Kalman-type forward-backward recursions) in the pertinent factor graphs. The proposed methods are broadly applicable, they (usually) require only matrix multiplications, and their complexity can be competitive with prior methods in some cases.

---


### 166. [Better with Less: Tackling Heterogeneous Multi-Modal Image Joint Pretraining via Conditioned and Degraded Masked Autoencoder](https://arxiv.org/abs/2604.16952)

**<font color=#1a73e8>作者：</font>** Bowen Peng, Yongxiang Liu, Jie Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning robust representations across extremely heterogeneous modalities remains a fundamental challenge in multi-modal vision. As a critical and profound instantiation of this challenge, high-resolution (HR) joint optical and synthetic aperture radar (SAR) pretraining seeks modality synergy to mutually enhance single-source representations; its potential is severely hindered by the Heterogeneity-Resolution Paradox: finer spatial scales drastically amplify the physical divergence between complex radar geometries and non-homologous optical textures. Consequently, migrating medium-resolution-oriented rigid alignment paradigms to HR scenarios triggers either severe feature suppression to force equivalence, or feature contamination driven by extreme epistemic uncertainty. Both extremes inevitably culminate in profound representation degradation and negative transfer. To overcome this bottleneck, we propose CoDe-MAE, pioneering a \textit{better synergy with less alignment} philosophy. First, Optical-anchored Knowledge Distillation (OKD) implicitly regularizes SAR's speckle noise by mapping it into a pure semantic manifold. Building on this, Conditioned Contrastive Learning (CCL) utilizes a gradient buffering mechanism to align shared consensus while safely preserving divergent physical signatures. Concurrently, Cross-Modal Degraded Reconstruction (CDR) deliberately strips non-homologous spectral pseudo-features, truncating the inherently ill-posed mapping to capture true structural invariants. Extensive analyses validate our theoretical claims. Pretrained on 1M samples, CoDe-MAE demonstrates remarkable data efficiency, successfully preventing representation degradation and establishing new state-of-the-art performance across diverse single- and bi-modal downstream tasks, substantially outperforming foundation models scaled on vastly larger datasets.

---


### 167. [TSM-Pose: Topology-Aware Learning with Semantic Mamba for Category-Level Object Pose Estimation](https://arxiv.org/abs/2604.16954)

**<font color=#1a73e8>作者：</font>** Jinshuo Liu, Bingtao Ma, Junlin Su 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Category-level object pose estimation is fundamental for embodied intelligence, yet achieving robust generalization to unseen instances remains challenging. However, existing methods mainly rely on simple feature extraction and aggregation, which struggle to capture category-shared topological structures and conduct semantic keypoint modeling, limiting their generalization. To address these, we propose a \textbf{T}opology-Aware Learning with \textbf{S}emantic \textbf{M}amba for Category-Level \textbf{P}ose Estimation framework (TSM-Pose). Specifically, we introduce a Topology Extractor to capture the global topological representation of the point cloud, which is integrated into local geometry features and enables robust category-level structural representation. Simultaneously, we propose a Mamba-based Global Semantic Aggregator that injects semantics priors into keypoints to enhance their expressiveness and leverages multiple TwinMamba blocks to model long-range dependencies for more effective global feature aggregation. Extensive experiments on three benchmark datasets (REAL275, CAMERA25, and HouseCat6D) demonstrate that TSM-Pose outperforms existing state-of-the-art methods.

---


### 168. [Training-inference input alignment outweighs framework choice in longitudinal retinal image prediction](https://arxiv.org/abs/2604.16955)

**<font color=#1a73e8>作者：</font>** Liyin Chen, Nazlee Zebardast, Mengyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative prediction of future retinal appearance from longitudinal imaging would support clinical decisions in progressive macular disease that currently rely on qualitative comparison or scalar progression scores. Recent methods have moved toward increasing generative complexity, but whether this complexity is necessary for slowly progressing retinal disease is unclear. We tested this through a controlled comparison of five conditioning configurations sharing one architecture and training dataset, spanning standard conditional diffusion, inference-aligned stochastic training, and deterministic regression. In our evaluation, aligning the training and inference input distributions produced large gains (delta-SSIM +0.082, SSIM +0.086, both p < 0.001), while the choice among aligned frameworks did not significantly affect any primary metric. Task-entropy and posterior-concentration analyses, replicated on two fundus autofluorescence (FAF) platforms, provided a mechanistic account: the predictable component of inter-visit change is small relative to time-invariant acquisition variability, leaving stochastic sampling with little width to exploit. Guided by these findings, we developed TRU (Temporal Retinal U-Net), a deterministic direct-regression model with continuous time-delta conditioning and multi-scale history aggregation. We evaluated TRU on 28,902 eyes across three imaging platforms: a mixed-disease Optos FAF cohort (9,942 eyes), zero-shot transfer to Stargardt macular dystrophy on Optos (288 eyes) and Heidelberg Spectralis (125 eyes), and a boundary evaluation on Cirrus en-face fundus images from a glaucoma cohort (18,547 eyes). TRU matched or exceeded delta-SSIM, SSIM, and PSNR in every FAF cohort against three state-of-the-art benchmarks, and its advantage grew monotonically with available history length.

---


### 169. [Hyperbolic Enhanced Representation Learning for Incomplete Multi-view Clustering](https://arxiv.org/abs/2604.16959)

**<font color=#1a73e8>作者：</font>** Tianyi Chen, Haobo Wang, Kai Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Incomplete Multi-View Clustering (IMVC) faces the challenge of learning discriminative representations from fragmentary observations while maintaining robustness against missing views. However, prevalent Euclidean-based methods suffer from a geometric mismatch when modeling real-world data with intrinsic hierarchies, leading to semantic blurring where representations drift towards spatially proximal but semantically distinct neighbors. To bridge this gap, we propose HERL, a Hyperbolic Enhanced Representation Learning framework for IMVC. Operating within the Poincaré ball, HERL constructs a structure-aware latent space to enhance representation learning. Specifically, we design a dual-constraint hyperbolic contrastive mechanism optimizing: an angular-based loss to preserve semantic identity via directional alignment, and a distance-based loss to enforce hierarchical compactness. Furthermore, a hyperbolic prototype head is introduced to rectify global structural drift by aligning cross-view hierarchy-aware prototype distributions. Consequently, HERL disentangles fine-grained semantic correlations to sharpen cluster boundaries and imposes geometric constraints to rectify the data recovery process. Extensive experimental results demonstrate that HERL consistently outperforms state-of-the-art approaches.

---


### 170. [Correcting Low-Signal Sensitivity in the Deliberative Reason Index](https://arxiv.org/abs/2604.16963)

**<font color=#1a73e8>作者：</font>** Francesco Veri  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Deliberative Reason Index (DRI) is increasingly used to assess the coherence between considerations and preferences in deliberative settings, including applications to LLM-generated data. Under low-signal conditions, however, the standard DRI can produce inflated scores by treating near-zero correlations as evidence of consistency. Monte Carlo simulations across common study designs show that this bias increases with group size and yields positive values even under random response. A modified DRI is introduced that applies a continuous penalty to low-signal correlation pairs. The modification preserves the original scale and reduces exactly to the standard DRI when substantive signal is present. A threshold sensitivity analysis identifies {\tau}=0.2as the optimal parameter. An empirical check with archival deliberative data shows that substantive inferences remain unchanged. The modification improves the reliability and comparability of the DRI in low-signal settings.

---


### 171. [On Safety Risks in Experience-Driven Self-Evolving Agents](https://arxiv.org/abs/2604.16968)

**<font color=#1a73e8>作者：</font>** Weixiang Zhao, Yichen Zhang, Yingshuo Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Experience-driven self-evolution has emerged as a promising paradigm for improving the autonomy of large language model agents, yet its reliance on self-curated experience introduces underexplored safety risks. In this study, we investigate how experience accumulation and utilization in self-evolving agents affect safety performance across web-based and embodied environments. Notably, experience gathered solely from benign tasks can still compromise safety in high-risk scenarios. Further analysis attributes this degradation to the execution-oriented nature of accumulated experience, which reinforces agents' tendency to act rather than refuse. In more realistic settings where agents encounter both benign and harmful tasks, refusal-related experience mitigates safety decline but induces over-refusal, revealing a fundamental safety-utility trade-off. Overall, our findings expose inherent limitations of current self-evolving agents and call for more principled strategies to ensure safe and reliable adaptation.

---


### 172. [Hyperspectral Unmixing Hierarchies](https://arxiv.org/abs/2604.16969)

**<font color=#1a73e8>作者：</font>** Joseph L. Garrett, P. S. Vishnu, Pauliina Salmi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmixing reveals the spatial distribution and spectral details of different constituents, called endmembers, in a hyperspectral image. Because unmixing has limited ground truth requirements, can accommodate mixed pixels, and is closely tied to light propagation, it is a uniquely powerful tool for analyzing hyperspectral images. However, spectral variability inhibits unmixing performance, the proper way to determine the number of endmembers is ambiguous, and the clarity of the endmembers degrades as more are included. Hierarchical structure is a possible solution to all three problems.
Here, hierarchical unmixing is defined by imposing a hierarchical abundance sum constraint on Deep Nonnegative Matrix Factorization. Binary Linear Unmixing Tactile Hierarchies (BLUTHs) solve the hierarchical unmixing problem with a simple network architecture. Sparsity modulation unmixing growth tailors the topology of a BLUTH to each scene. The structure imposed by BLUTHs allows endmembers with varying levels of spectral contrast to be revealed, mitigating the challenge of spectral variability.
The performance of BLUTHs exceeds state-of-the-art unmixing algorithms on laboratory scenes, particularly with regard to abundance estimation, while their performance remains competitive on remote sensing scenes. In addition, ocean color unmixing by BLUTHs is demonstrated on hyperspectral scenes from the HYPSO and PACE satellites.

---


### 173. [UGD: An Unsupervised Geometric Distance for Evaluating Real-world Noisy Point Cloud Denoising](https://arxiv.org/abs/2604.16976)

**<font color=#1a73e8>作者：</font>** Zhiyong Su, Jincan Wu, Yonghui Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud denoising is a fundamental and crucial challenge in real-world point cloud applications. Existing quantitative evaluation metrics for point cloud denoising methods are implemented in a supervised manner, which requires both the denoised point cloud and the corresponding ground-truth clean point cloud to compute a representative geometric distance. This requirement is highly problematic in real-world scenarios, where ground-truth clean point clouds are often unavailable. In this paper, we propose a simple yet effective unsupervised geometric distance (UGD) for real-world noisy point cloud denoising, calculated solely from noisy point clouds. The core idea of UGD is to learn a patch-wise prior model from a set of clean point clouds and then employ this prior model as the ground-truth to quantify the degradation by measuring the geometric variations of the denoised point cloud. To this end, we first learn a pristine Gaussian Mixture Model (GMM) with extracted patch-wise quality-aware features from a set of pristine clean point clouds by a patch-wise feature extraction network, which serves as the ground-truth for the quantitative evaluation. Then, the UGD is defined as the weighted sum of distances between each patch of the denoised point cloud and the learned pristine GMM model in the patch space. To train the employed patch-wise feature extraction network, we propose a self-supervised training framework through multi-task learning, which includes pair-wise quality ranking, distortion classification, and distortion distribution prediction. Quantitative experiments with synthetic noise confirm that the proposed UGD achieves comparable performance to supervised full-reference metrics. Moreover, experimental results on real-world data demonstrate that the proposed UGD enables unsupervised evaluation of point cloud denoising methods based exclusively on noisy point clouds.

---


### 174. [A phenotype-driven and evidence-governed framework for knowledge graph enrichment and hypotheses discovery in population data](https://arxiv.org/abs/2604.16982)

**<font color=#1a73e8>作者：</font>** Adela Bâra, Simona-Vasilica Oprea  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current knowledge graph (KG) construction methods are confirmatory, focusing on recovering known relationships rather than identifying novel or context-dependent nodes. This paper proposes a phenotype-driven and evidence-governed framework that shifts the paradigm toward structured hypothesis discovery and controlled KG expansion. The approach integrates graph neural networks (GNNs) for phenotype discovery, causal inference, probabilistic reasoning and large language models (LLMs) for hypothesis generation and claim extraction within a unified pipeline. The framework prioritizes relationships that are both structurally supported by data and underexplored in the literature. KG expansion is formulated as a multi-objective optimization problem, where candidate claims are jointly evaluated in terms of relevance, structural validation and novelty. Pareto-optimal selection enables the identification of non-dominated claims that balance confirmation and discovery, avoiding trivial or redundant knowledge inclusion. Experiments on heterogeneous population datasets demonstrate that the proposed framework produces more interpretable phenotypes, reveals context-dependent causal structures and generates high-quality claims that align with both data and scientific evidence. Compared to rule-based and LLM-only baselines, the method achieves the best trade-off across plausibility, novelty, validation and relevance. In retrieval-augmented settings, it significantly improves performance (Recall@5=0.98) while reducing hallucination rates (0.05), highlighting its effectiveness in grounding LLM outputs.

---


### 175. [Adverse-to-the-eXtreme Panoptic Segmentation: URVIS 2026 Study and Benchmark](https://arxiv.org/abs/2604.16984)

**<font color=#1a73e8>作者：</font>** Yiting Wang, Nolwenn Peyratout, Tim Brodermann 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents the report of the URVIS 2026 challenge on adverse-to-extreme panoptic segmentation. As the first challenge of its kind, it attracted 17 registered participants and 47 submissions, with 4 teams reaching the final phase. The challenge is based on the MUSES dataset, a multi-sensor benchmark for panoptic segmentation in adverse-to-extreme weather, including RGB frame camera, LiDAR, radar, and event camera data. Weighted Panoptic Quality (wPQ) is designed and adopted as the official ranking metric for fair evaluation across weather conditions. In this report, we summarise the challenge setting and benchmark results, analyse the performance of the submitted methods, and discuss current progress and remaining challenges for robust multimodal panoptic segmentation. Link: this https URL

---


### 176. [DVAR: Adversarial Multi-Agent Debate for Video Authenticity Detection](https://arxiv.org/abs/2604.16987)

**<font color=#1a73e8>作者：</font>** Hongyuan Qi, Feifei Shao, Ming Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of video generation technologies poses a significant challenge to media forensics, as conventional detection methods often fail to generalize beyond their training distributions. To address this, we propose DVAR (Debate-based Video Authenticity Reasoning), a training-free framework that reformulates video detection as a structured multi-agent forensic reasoning process. Moving beyond the paradigm of pattern matching, DVAR orchestrates a competition between a Generative Hypothesis Agent and a Natural Mechanism Agent. Through iterative rounds of cross-examination, these agents defend their respective explanations against abnormal evidence, driving a logical convergence where the truth emerges from rigorous stress-testing. To adjudicate these conflicting claims, we apply Occam's Razor through the Minimum Description Length (MDL) framework, defining an Explanatory Cost to quantify the "logical burden" of each reasoning path. Furthermore, we integrate GenVideoKB, a dynamic knowledge repository that provides high-level reasoning heuristics on generative boundaries and failure modes. Extensive experiments demonstrate that DVAR achieves competitive performance against supervised state-of-the-art methods while exhibiting superior generalization to unseen generative architectures. By transforming detection into a transparent debate, DVAR provides explicit, interpretable reasoning traces for robust video authenticity assessment.

---


### 177. [Rule-VLN: Bridging Perception and Compliance via Semantic Reasoning and Geometric Rectification](https://arxiv.org/abs/2604.16993)

**<font color=#1a73e8>作者：</font>** Jiawen Wen, Penglei Sun, Wenjie Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As embodied AI transitions to real-world deployment, the success of the Vision-and-Language Navigation (VLN) task tends to evolve from mere reachability to social compliance. However, current agents suffer from a "goal-driven trap", prioritizing physical geometry ("can I go?") over semantic rules ("may I go?"), frequently overlooking subtle regulatory constraints. To bridge this gap, we establish Rule-VLN, the first large-scale urban benchmark for rule-compliant navigation. Spanning a massive 29k-node environment, it injects 177 diverse regulatory categories into 8k constrained nodes across four curriculum levels, challenging agents with fine-grained visual and behavioral constraints. We further propose the Semantic Navigation Rectification Module (SNRM), a universal, zero-shot module designed to equip pre-trained agents with safety awareness. SNRM integrates a coarse-to-fine visual perception VLM framework with an epistemic mental map for dynamic detour planning. Experiments demonstrate that while Rule-VLN challenges state-of-the-art models, SNRM significantly restores navigation capabilities, reducing CVR by 19.26% and boosting TC by 5.97%.

---


### 178. [Inductive Convolution Nuclear Norm Minimization for Tensor Completion with Arbitrary Sampling](https://arxiv.org/abs/2604.17001)

**<font color=#1a73e8>作者：</font>** Wei Li, Yuyang Li, Kaile Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The recently established Convolution Nuclear Norm Minimization (CNNM) addresses the problem of \textit{tensor completion with arbitrary sampling} (TCAS), which involves restoring a tensor from a subset of its entries sampled in an arbitrary manner. Despite its promising performance, the optimization procedure of CNNM needs performing Singular Value Decomposition (SVD) multiple times, which is computationally expensive and hard to parallelize. To address the issue, we reformulate the optimization objective of CNNM from the perspective of convolution eigenvectors. By introducing pre-learned convolution eigenvectors which are shared among different tensors, we propose a novel method called Inductive Convolution Nuclear Norm Minimization (ICNNM), which bypasses the SVD step so as to decrease significantly the computational time. In addition, due to the extra prior knowledge encoded in the pre-learned convolution eigenvectors, ICNNM also outperforms CNNM in terms of recovery performance. Extensive experiments on video completion, prediction and frame interpolation verify the superiority of ICNNM over CNNM and several other competing methods.

---


### 179. [From Public-Key Linting to Operational Post-Quantum X.509 Assurance for ML-KEM and ML-DSA: Registry-Driven Policy, Mutation-Based Evaluation, and Import Validation](https://arxiv.org/abs/2604.17003)

**<font color=#1a73e8>作者：</font>** José Luis Delgado Jiménez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Final FIPS and PKIX standards for ML-KEM and ML-DSA fix the normative floor, but operational assurance in post-quantum X.509 still depends on accountable checks across certificate-profile semantics, SubjectPublicKeyInfo representation, and private-key-container import. We present a workflow-centric assurance framework for ML-KEM and ML-DSA in the narrow executable profile pkix-core. The framework reifies 17 final-standards requirements into an assurance registry indexed by owner, stage, detector kind, normative strength, and mode-specific action; groups them into three operator gate packs; spans certificate/profile, SPKI/public-key, and private-key-container/import surfaces; and evaluates them through a frozen mutation-based corpus with bounded public-appendix and cross-tool supporting evidence.
Across a controlled corpus of 48 artifacts (21 valid, 27 invalid), the artifact detects all expected invalid cases in both strict and deployable modes with zero false positives. Strict blocks all 17 active requirements; deployable preserves the same detection coverage while downgrading exactly one exercised ML-KEM canonicality condition from block to warning. On the importer-owned private-key surface, all 7 active requirements are covered, with 7/7 expected invalid detections and no open detector gaps. On a comparable certificate subset, a frozen JZLint baseline meets 5/10 expected invalid detections and fatally rejects 3 valid ML-KEM certificates, whereas the local artifact meets 10/10 with no fatal valid rejections. A bounded public appendix and a cross-tool matrix further show that parse acceptance and policy conformance diverge materially. Overall, the results support an operational X.509 assurance workflow for CA pre-issuance and private-key import that extends prior PQ public-key linting work.

---


### 180. [MobileAgeNet: Lightweight Facial Age Estimation for Mobile Deployment](https://arxiv.org/abs/2604.17007)

**<font color=#1a73e8>作者：</font>** Arun Kumar, Aswathy Baiju, Radu Timofte 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mobile deployment of facial age estimation requires models that balance predictive accuracy with low latency and compact size. In this work, we present MobileAgeNet, a lightweight age-regression framework that achieves an MAE of 4.65 years on the UTKFace held-out test set while maintaining efficient on-device inference with an average latency of 14.4 ms measured using the AI Benchmark application. The model is built on a pretrained MobileNetV3-Large backbone combined with a compact regression head, enabling real-time prediction on mobile devices. The training and evaluation pipeline is integrated into the NN LEMUR Dataset framework, supporting reproducible experimentation, structured hyperparameter optimization, and consistent evaluation. We employ bounded age regression together with a two-stage fine-tuning strategy to improve training stability and generalization. Experimental results show that MobileAgeNet achieves competitive accuracy with 3.23M parameters, and that the deployment pipeline from PyTorch training through ONNX export to TensorFlow Lite conversion - preserves predictive behavior without measurable degradation under practical on-device conditions. Overall, this work provides a practical, deployment-ready baseline for mobile-oriented facial age estimation.

---


### 181. [Small Model as Master Orchestrator: Learning Unified Agent-Tool Orchestration with Parallel Subtask Decomposition](https://arxiv.org/abs/2604.17009)

**<font color=#1a73e8>作者：</font>** Wenzhen Yuan, Wutao Xiong, Fanchen Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) demonstrate clear advantages in tackling complex problems by coordinating diverse agents and external tools. However, most existing orchestration methods rely on static workflows or serial agent scheduling, and are further constrained by heterogeneous interface protocols between tools and agents. This leads to high system complexity and poor extensibility. To mitigate these issues, we propose Agent-as-Tool, a unified parallel orchestration paradigm that abstracts both agents and tools into a standardized, learnable action space with protocol normalization and explicit state feedback. Building on this paradigm, we train a lightweight orchestrator, ParaManager, which decouples planning decisions from subtask solving, enabling state-aware parallel subtask decomposition, delegation, and asynchronous execution. For training, we adopt a two-stage ParaManager training pipeline. It improves robustness by incorporating supervised fine-tuning (SFT) trajectories equipped with recovery mechanisms, and further applies reinforcement learning (RL) to achieve an optimal balance among task success, protocol compliance, diversity, and reasoning efficiency. Experiments show that ParaManager achieves strong performance across multiple benchmarks and exhibits robust generalization under unseen model pools.

---


### 182. [Towards Universal Skeleton-Based Action Recognition](https://arxiv.org/abs/2604.17013)

**<font color=#1a73e8>作者：</font>** Jidong Kuang, Hongsong Wang, Jie Gui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the development of robotics, skeleton-based action recognition has become increasingly important, as human-robot interaction requires understanding the actions of humans and humanoid robots. Due to different sources of human skeletons and structures of humanoid robots, skeleton data naturally exhibit heterogeneity. However, previous works overlook the data heterogeneity of skeletons and solely construct models using homogeneous skeletons. Moreover, open-vocabulary action recognition is also essential for real-world applications. To this end, this work studies the challenging problem of heterogeneous skeleton-based action recognition with open vocabularies. We construct a large-scale Heterogeneous Open-Vocabulary (HOV) Skeleton dataset by integrating and refining multiple representative large-scale skeleton-based action datasets. To address universal skeleton-based action recognition, we propose a Transformer-based model that comprises three key components: unified skeleton representation, motion encoder for skeletons, and multi-grained motion-text alignment. The motion encoder feeds multi-modal skeleton embeddings into a two-stream Transformer-based encoder to learn spatio-temporal action representations, which are then mapped to a semantic space to align with text embeddings. Multi-grained motion-text alignment incorporates contrastive learning at three levels: global instance alignment, stream-specific alignment, and fine-grained alignment. Extensive experiments on popular benchmarks with heterogeneous skeleton data demonstrate both the effectiveness and the generalization ability of the proposed method. Code is available at this https URL.

---


### 183. [Mini-BEHAVIOR-Gran: Revealing U-Shaped Effects of Instruction Granularity on Language-Guided Embodied Agents](https://arxiv.org/abs/2604.17019)

**<font color=#1a73e8>作者：</font>** Sukai Huang, Chenyuan Zhang, Fucai Ke 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Instruction granularity is an important yet poorly controlled variable in language-guided embodied AI. Existing benchmarks typically pair each task with a single static instruction, making it difficult to study how agent behavior changes when the same task is described at different levels of detail. We introduce Mini-BEHAVIOR-Gran, a new benchmark for controlled studies of instruction granularity that extends Mini-BEHAVIOR with multiple instruction variants per task, ranging from high-level goal descriptions to step-by-step guidance. Using this benchmark, we compare four candidate metrics for cross-task granularity quantification: token count, entity count, action-verb count, and planning-width, and find that width correlates most consistently with agent performance. Using width to organize training and evaluation further reveals a non-monotonic U-shaped relationship between instruction granularity and performance, with peaks at both fine and coarse extremes. Further analysis suggests that the coarse-granularity performance rebound is associated with shallow grounding, where agents learn vision-dominant policies.

---


### 184. [Beyond Black-Box Labels: Interpretable Criteria for Diagnosing SubjectiveNLP Tasks](https://arxiv.org/abs/2604.17022)

**<font color=#1a73e8>作者：</font>** Nisrine Rair, Alban Goupil, Valeriu Vrabie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Subjective NLP datasets typically aggregate annotator judgments into a single gold label, making it difficult to diagnose whether disagreement reflects unclear criteria, collapsed distinctions, or legitimate plurality. We propose a \emph{schema-level diagnostic} for auditing expert-designed annotation schemas \emph{prior to} gold-label commitment, using only multi-annotator criterion judgments. The diagnostic separates two failure modes: unstable criteria with hard-to-operationalize boundaries, and systematic overlap that blurs the boundaries between mutually exclusive categories. Applied to persuasive value extraction in commercial documents, we find that disagreement is not diffuse: instability concentrates in a few criteria, while nearly half of covered sentences activate multiple categories. These signals align with where domain experts disagree, yielding an evidence-based audit for tightening guidelines, revising category structure, or reconsidering the annotation paradigm.

---


### 185. [The Instrumental Dissolution of Typing: Why AI Challenges the Keyboard Era in Knowledge Work](https://arxiv.org/abs/2604.17023)

**<font color=#1a73e8>作者：</font>** Wei Roy Hua  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> For four decades, the QWERTY keyboard organized white-collar knowledge work. Typing's dominance was instrumental, not cognitively necessary. As multimodal AI achieves human-parity understanding of speech and gesture, this necessity dissolves. We introduce instrumental dissolution -- loss of institutional-default status while persisting in specialist niches. The keyboard era ends not through hardware replacement but through migration of its function into AI systems. The central contribution identifies the verification bottleneck: as AI collapses production friction, the primary constraint shifts from generation to evaluation. Knowledge workers become adversarial auditors rather than keystroke-producers. This restructures professional expertise, organizational communication, and how productive labor is recognized. Converging evidence from history, philosophy, neuroscience, technology, organizational studies, and cultural analysis supports this thesis. We map synthetic literacy -- oral input generating literate output -- as the defining feature of this transition. Under three scenarios (optimistic: 2028-2035; base: 2035-2045; pessimistic: 2045-2060), we specify disconfirmation criteria that would weaken the thesis if observed. We propose seven interface primitives operationalizing verification-centered HCI.

---


### 186. [CAM3DNet: Comprehensively mining the multi-scale features for 3D Object Detection with Multi-View Cameras](https://arxiv.org/abs/2604.17024)

**<font color=#1a73e8>作者：</font>** Mingxi Pang, Dingheng Wang, Zekun Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Query-based 3D object detection methods using multi-view images often struggle to efficiently leverage dynamic multi-scale information, e.g., the relationship between the object features and the geometric of the queries are not sufficiently learned, directly exploring the multi-scale spatiotemporal features will pay too many costs. To address these challenges, we propose CAM3DNet, a novel sparse query-based framework which combines three new modules, composite query (CQ), adaptive self-attention (ASA), and multi-scale hybrid sampling (MSHS). First, the core idea in the CQ module is a multi-scale projection strategy to transform 2D queries into 3D space. Second, the ASA module learns the interactions between the spatiotemporal multi-scale queries. Third, the MSHS module uses the deformable attention mechanism to sample multi-scale object information by considering multi-scales queries, pyramid feature maps, and 2D-camera prior knowledge. The entire model employs a backbone network and a feature pyramid network (FPN) as the encoder, then introduces a YOLOX and a DepthNet as a ROI\_Head to produce CQ, and repeatedly utilizes ASA and MSHS as the decoder to gain detection features. Extensive experiments on the nuScenes, Waymo, and Argoverse benchmark datasets demonstrate the effectiveness of our CAM3DNet, and most existing camera-based 3D object detection methods are outperformed. Besides, we make comprehensive ablation studies to check the individual effect of CQ, ASA, and MSHS, as well as their cost of space and computation complexity.

---


### 187. [When Spike Sparsity Does Not Translate to Deployed Cost: VS-WNO on Jetson Orin Nano](https://arxiv.org/abs/2604.17040)

**<font color=#1a73e8>作者：</font>** Jason Yoo, Shailesh Garg, Souvik Chakraborty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking neural operators are appealing for neuromorphic edge computing because event-driven substrates can, in principle, translate sparse activity into lower latency and energy. Whether that advantage survives deployment on commodity edge-GPU software stacks, however, remains unclear. We study this question on a Jetson Orin Nano 8 GB using five pretrained variable-spiking wavelet neural operator (VS-WNO) checkpoints and five matched dense wavelet neural operator (WNO) checkpoints on the Darcy rectangular benchmark. On a reference-aligned path, VS-WNO exhibits substantial algorithmic sparsity, with mean spike rates decreasing from 54.26% at the first spiking layer to 18.15% at the fourth. On a deployment-style request path, however, this sparsity does not reduce deployed cost: VS-WNO reaches 59.6 ms latency and 228.0 mJ dynamic energy per inference, whereas dense WNO reaches 53.2 ms and 180.7 mJ, while also achieving slightly lower reference-path error (1.77% versus 1.81%). Nsight Systems indicates that the request path remains launch-dominated and dense rather than sparsity-aware: for VS-WNO, cudaLaunchKernel accounts for 81.6% of CUDA API time within the latency window, and dense convolution kernels account for 53.8% of GPU kernel time; dense WNO shows the same pattern. On this Jetson-class GPU stack, spike sparsity is measurable but does not reduce deployed cost because the runtime does not suppress dense work as spike activity decreases.

---


### 188. [A Real-Time Bike-Pedestrian Safety System with Wide-Angle Perception and Evaluation Testbed for Urban Intersections](https://arxiv.org/abs/2604.17046)

**<font color=#1a73e8>作者：</font>** Mehmet Kerem Turkcan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collisions between cyclists and pedestrians at urban intersections remain a persistent source of injuries, yet few systems attempt real-time warnings to unequipped road users using commodity hardware. We present a prototype collision warning system that runs on a single edge device with a wide-angle fisheye camera, producing audible and visual alerts at 30\,fps. The system makes four contributions. First, we develop a calibration pipeline for ultra-wide fisheye lenses that overcomes corner-detection failure and optimizer divergence through perspective remapping and direct bundle adjustment. Second, we combine fisheye-aware object detection with a closed-form ground-plane projection via a precomputed lookup table. Third, we introduce a design-time conformance simulation with 24 scripted hazard scenarios, stochastic size-aware detection failures, and a latency sweep showing that a first-order kinematic predictor maintains the mean warning budget above the distracted-pedestrian reaction time across realistic camera latencies. Fourth, we formalize the decision layer as a separable, auditable testbench with explicit deployment gates, contestability mechanisms, and a residual risk register. Under conformance testing with fisheye localization error, the selected pipeline configuration achieves 93.3\% sensitivity and 92.3\% specificity, with a mean warning budget of 3.3\,s. The system design was informed by community-aided design workshops. Code and replication scripts are available at this https URL.

---


### 189. [OASIS: On-Demand Hierarchical Event Memory for Streaming Video Reasoning](https://arxiv.org/abs/2604.17052)

**<font color=#1a73e8>作者：</font>** Zhijia Liang, Jiaming Li, Weikai Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video reasoning requires models to operate in a setting where history grows without bound while meaningful evidence remains scarce. In such a landscape, relevant signal is like an oasis-small, critical, and easily lost in a desert of redundancy. Enlarging memory only widens the desert; aggressive compression dries up the oasis. The real difficulty lies in discovering where to look, not how much to remember. We therefore introduce OASIS, a novel framework for streaming video reasoning that tackles this challenge through structured, on-demand retrieval. It organizes streaming history into hierarchical events and performs reasoning as controlled refinement-short-context inference first, followed by semantically grounded retrieval only when uncertainty arises. As the retrieval is driven by high-level intent rather than embedding similarity, the retrieved memory is substantially more accurate and less noisy. Additionally, the mechanism is plug-and-play, training-free, and readily attaches to different streaming MLLM backbones. Experiments across multiple benchmarks and backbones show that OASIS achieves strong gains in long-horizon accuracy and compositional reasoning with bounded token cost and low request delay. Code is available at this https URL.

---


### 190. [Reference-state System Reliability method for scalable uncertainty quantification of coherent systems](https://arxiv.org/abs/2604.17066)

**<font color=#1a73e8>作者：</font>** Ji-Eun Byun, Hyeuk Ryu, Junho Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coherent systems are representative of many practical applications, ranging from infrastructure networks to supply chains. Probabilistic evaluation of such systems remains challenging, however, because existing decomposition-based methods scale poorly as the number of components grows. To address this limitation, this study proposes the Reference-state System Reliability (RSR) method. Like existing approaches, RSR characterises the boundary between different system states using reference states in the component-state space. Where it departs from these methods is in how the state space is explored: rather than using reference states to decompose the space into disjoint hypercubes, RSR uses them to classify Monte Carlo samples, making computational cost significantly less sensitive to the number of reference states. To make this classification efficient, samples and reference states are stored as matrices and compared using batched matrix operations, allowing RSR to exploit the advances in high-throughput matrix computing driven by modern machine learning. We demonstrate that RSR evaluates the system-state probability of a graph with 119 nodes and 295 edges within 10~seconds, highlighting its potential for real-time risk assessment of large-scale systems. We further show that RSR scales to problems involving hundreds of thousands of reference states -- well beyond the reach of existing methods -- and extends naturally to multi-state systems. Nevertheless, when the number of boundary reference states grows exceedingly large, RSR's convergence slows down, a limitation shared with existing reference-state-based approaches that motivates future research into learning-based representations of system-state boundaries.

---


### 191. [NTIRE 2026 Rip Current Detection and Segmentation (RipDetSeg) Challenge Report](https://arxiv.org/abs/2604.17070)

**<font color=#1a73e8>作者：</font>** Andrei Dumitriu, Aakash Ralhan, Florin Miron 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report presents the NTIRE 2026 Rip Current Detection and Segmentation (RipDetSeg) Challenge, which targets automatic rip current understanding in images. Rip currents are hazardous nearshore flows that cause many beach-related fatalities worldwide, yet remain difficult to identify because their visual appearance varies substantially across beaches, viewpoints, and sea states. To advance research on this safety-critical problem, the challenge builds on the RipVIS benchmark, evaluating both detection and segmentation. The dataset is diverse, sourced from more than $10$ countries, with $4$ camera orientations and diverse beach and sea conditions. This report describes the dataset, challenge protocol, evaluation methodology, final results, and summarizes the main insights from the submitted methods. The challenge attracted $159$ registered participants and produced $9$ valid test submissions across the two tasks. Final rankings are based on a composite score that combines $F_1[50]$, $F_2[50]$, $F_1[40\!:\!95]$, and $F_2[40\!:\!95]$. Most participant solutions relied on pretrained models, combined with strong augmentation and post-processing design. These results suggest that rip current understanding benefits strongly from the robust general-purpose vision models' progress, while leaving ample room for future methods tailored to their unique visual structure.

---


### 192. [Comparison Drives Preference: Reference-Aware Modeling for AI-Generated Video Quality Assessment](https://arxiv.org/abs/2604.17074)

**<font color=#1a73e8>作者：</font>** Minghao Zou, Gen Liu, Guanghui Yue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative models has led to a growing volume of AI-generated videos, making the automatic quality assessment of such videos increasingly important. Existing AI-generated content video quality assessment (AIGC-VQA) methods typically estimate visual quality by analyzing each video independently, ignoring potential relationships among videos. In this work, we revisit AIGC-VQA from an inter-video perspective and formulate it as a reference-aware evaluation problem. Through this formulation, quality assessment is guided not only by intrinsic video characteristics but also by comparisons with related videos, which is more consistent with human perception. To validate its effectiveness, we propose Reference-aware Video Quality Assessment (RefVQA), which utilizes a query-centered reference graph to organize semantically related samples and performs graph-guided difference aggregation from the reference nodes to the query node. Experiments on existing datasets demonstrate that our proposed RefVQA outperforms state-of-the-art methods across multiple quality dimensions, with strong generalization ability validated by cross-dataset evaluation. These results highlight the effectiveness of the proposed reference-based formulation and suggest its potential to advance AIGC-VQA.

---


### 193. [Understanding and Enforcing Weight Disentanglement in Task Arithmetic](https://arxiv.org/abs/2604.17078)

**<font color=#1a73e8>作者：</font>** Shangge Liu, Yuehan Yin, Lei Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Task arithmetic provides an efficient, training-free way to edit pre-trained models, yet lacks a fundamental theoretical explanation for its success. The existing concept of ``weight disentanglement" describes the ideal outcome of non-interfering task composition but does not reveal its underlying cause. Crucially, what intrinsic properties of the pre-trained model ($\theta_0$) or the task vectors ($\tau_t$) enable this disentanglement remains underexplored. In this paper, we introduce Task-Feature Specialization (TFS), a model's ability to allocate distinct internal features to different tasks, as the fundamental principle. We first prove that TFS is a sufficient condition for weight disentanglement. More importantly, we find that TFS also gives rise to an observable geometric consequence: weight vector orthogonality. This positions TFS as the common cause for both the desired functional outcome (disentanglement) and a measurable geometric property (orthogonality). This relationship provides the key insight for our method: since the abstract TFS property is intractable to enforce directly, we can instead promote weight disentanglement by shaping its concrete geometric consequence, orthogonality. Therefore, we propose OrthoReg, a simple and effective regularization method that actively enforces an internal orthogonal structure on weight updates ($\Delta W$) that constitute $\tau_t$ during fine-tuning. And we theoretically prove that OrthoReg promotes disentanglement. Extensive experiments demonstrate that OrthoReg consistently and significantly enhances the performance of various task arithmetic methods. Code is available at \href{this https URL}{this https URL}.

---


### 194. [D-Prism: Differentiable Primitives for Structured Dynamic Modeling](https://arxiv.org/abs/2604.17082)

**<font color=#1a73e8>作者：</font>** Xingyuan Yu, Yijin Li, Chong Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Capturing both geometry and rigid motion for structured dynamic objects, like multi-part assemblies or jointed mechanisms, remains a key challenge. Existing dynamic methods, such as deformable meshes or 3DGS, rely on unstructured representations and fail to jointly model suitable geometry and articulated motion. Primitive-based methods excel at structured static scenes, but their dynamic potential is still unexplored. We propose D-Prism, the first framework to achieve high-fidelity structured dynamic modeling by extending differentiable primitives to the dynamic domain. Specifically, we bind 3DGS to primitive surfaces, leveraging their respective strengths in appearance and geometry. We introduce a deformation network to control primitive motion, ensuring it accurately matches the object's movement. Furthermore, we design a novel adaptive control strategy to dynamically adjust primitive counts, better matching objects' true spatial footprint. Experiments confirm that our method excels at structured dynamic modeling, providing both structured geometry and precise motion tracking.

---


### 195. [Tree of Concepts: Interpretable Continual Learners in Non-Stationary Clinical Domains](https://arxiv.org/abs/2604.17089)

**<font color=#1a73e8>作者：</font>** Dongkyu Cho, Xiyue Li, Samrachana Adhikari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning aims to update models under distribution shift without forgetting, yet many high-stakes deployments, such as healthcare, also require interpretability. In practice, models that adapt well (e.g., deep networks) are often opaque, while models that are interpretable (e.g., decision trees) are brittle under shift, making it difficult to achieve both properties simultaneously. In response, we propose Tree of Concepts, an interpretable continual learning framework that uses a shallow decision tree to define a fixed, rule-based concept interface and trains a concept bottleneck model to predict these concepts from raw features. Continual updates act on the concept extractor and label head while keeping concept semantics stable over time, yielding explanations that do not drift across sequential updates. On multiple tabular healthcare benchmarks under continual learning protocols, our method achieves a stronger stability-plasticity trade-off than existing baselines, including replay-enhanced variants. Our results suggest that structured concept interfaces can support continual adaptation while preserving a consistent audit interface in non-stationary, high-stakes domains.

---


### 196. [Marrying Text-to-Motion Generation with Skeleton-Based Action Recognition](https://arxiv.org/abs/2604.17090)

**<font color=#1a73e8>作者：</font>** Jidong Kuang, Hongsong Wang, Jie Gui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human action recognition and motion generation are two active research problems in human-centric computer vision, both aiming to align motion with textual semantics. However, most existing works study these two problems separately, without uncovering the links between them, namely that motion generation requires semantic comprehension. This work investigates unified action recognition and motion generation by leveraging skeleton coordinates for both motion understanding and generation. We propose Coordinates-based Autoregressive Motion Diffusion (CoAMD), which synthesizes motion in a coarse-to-fine manner. As a core component of CoAMD, we design a Multi-modal Action Recognizer (MAR) that provides gradient-based semantic guidance for motion generation. Furthermore, we establish a rigorous benchmark by evaluating baselines on absolute coordinates. Our model can be applied to four important tasks, including skeleton-based action recognition, text-to-motion generation, text-motion retrieval, and motion editing. Extensive experiments on 13 benchmarks across these tasks demonstrate that our approach achieves state-of-the-art performance, highlighting its effectiveness and versatility for human motion modeling. Code is available at this https URL.

---


### 197. [Live LTL Progress Tracking: Towards Task-Based Exploration](https://arxiv.org/abs/2604.17106)

**<font color=#1a73e8>作者：</font>** Noel Brindise, Cedric Langbort, Melkior Ornik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by the challenge presented by non-Markovian objectives in reinforcement learning (RL), we present a novel framework to track and represent the progress of autonomous agents through complex, multi-stage tasks. Given a specification in finite linear temporal logic (LTL), the framework establishes a 'tracking vector' which updates at each time step in a trajectory rollout. The values of the vector represent the status of the specification as the trajectory develops, assigning true, false, or 'open' labels (where 'open' is used for indeterminate cases). Applied to an LTL formula tree, the tracking vector can be used to encode detailed information about how a task is executed over a trajectory, providing a potential tool for new performance metrics, diverse exploration, and reward shaping. In this paper, we formally present the framework and algorithm, collectively named Live LTL Progress Tracking, give a simple working example, and demonstrate avenues for its integration into RL models. Future work will apply the framework to problems such as task-space exploration and diverse solution-finding in RL.

---


### 198. [Hybrid Multi-Dimensional MRI Prostate Cancer Detection via Hadamard Network-Based Bias Correction and Residual Networks](https://arxiv.org/abs/2604.17107)

**<font color=#1a73e8>作者：</font>** Emadeldeen Hamdan, Gorkem Durak, Muhammed Enes Tasci 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic Resonance Imaging (MRI) is vital for prostate cancer (PCa) diagnosis. While advanced techniques such as Hybrid Multi-dimensional MRI (HM-MRI) have enhanced diagnostic capabilities, the significant need remains for robust, automated Artificial Intelligence (AI)-based detection methods. In this study, we combine quantitative HM-MRI of tissue composition with an AI-based neural network. We propose the Hadamard-Bias Network plus ResNet18 (HBR-Net-18), a two-stage AI framework for PCa detection. In the first stage, a Hadamard U-Net-based algorithm suppresses intensity inhomogeneities (bias fields) across six parametric HM-MRI maps generated via a Physics-Informed Autoencoder (PIA). In the second stage, a Residual Network (ResNet-18) performs patch-level classification. The framework utilizes overlapping 11-by-11 patches, incorporating both 2D intra-slice and 3D inter-slice (adjacent-slice) information to improve spatial consistency. Our experimental results demonstrate that HB-Net achieves balanced sensitivity and specificity, significantly outperforming conventional radiomics-based approaches and baseline CNN models, highlighting its potential for clinical deployment.

---


### 199. [Beyond Word Boundaries: A Hebrew Coreference Benchmark and an Evaluation Protocol for Morphologically Complex Text](https://arxiv.org/abs/2604.17108)

**<font color=#1a73e8>作者：</font>** Refael Shaked Greenfeld, Reut Tsarfaty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coreference Resolution (CR) is a fundamental NLP task critical for long-form tasks as information extraction, summarization, and many business applications. However, CR methods originally designed for English struggle with Morphologically Rich Languages (MRLs), where mention boundaries do not necessarily align with word boundaries, and a single token may consist of multiple anaphors. CR modeling and evaluation protocols standardly assume that, as in English, words and mentions mostly align. However, this assumption breaks down in MRLs, particularly in the context of LLMs' raw-text processing and end-to-end tasks. To assess and address this challenge, we introduce {\em KibutzR}, the first comprehensive CR dataset for Modern Hebrew, an MRL rich with complex words and pronominal clitics. We deliver an annotated dataset that identifies mentions at word, sub-word and multi-word levels, and propose an evaluation protocol that directly addresses word/morpheme boundary discrepancies. Our experiments show that contemporary LLMs perform significantly worse on Hebrew than on English, and that performance degrades on raw unsegmented text. Crucially, we show an inverse performance-trend in Hebrew relative to English, where smaller encoders perform far better than contemporary decoder models, leaving ample space for investigation and improvement. We deliver a new benchmark for Hebrew coreference resolution and a segmentation-aware evaluation protocol to inform future work on other MRLs.

---


### 200. [From Clinical Intent to Clinical Model: An Autonomous Coding-Agent Framework for Clinician-driven AI Development](https://arxiv.org/abs/2604.17110)

**<font color=#1a73e8>作者：</font>** Zihao Zhao, Frederik Hauke, Juliana De Castilhos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical AI development has traditionally followed a collaborative paradigm that depends on close interaction between clinicians and specialized AI teams. This paradigm imposes a practical challenge: clinicians must repeatedly communicate and refine their requirements with AI developers before those requirements can be translated into executable model development. This iterative process is time-consuming, and even after repeated discussion, misalignment may still exist because the two sides do not fully share each other's expertise. However, autonomous coding agents may change this paradigm, raising the possibility that clinicians could develop clinical AI models independently through natural-language interaction alone. In this study, we present such an autonomous prototype for clinician-driven clinical AI development. We evaluated the system on five clinical tasks spanning dermoscopic lesion classification, melanoma-versus-nevus triage, wrist-fracture detection (including a weakly supervised variant with only 5% bounding-box annotations), and debiased pneumothorax classification on chest radiographs. Across these settings, the system consistently developed models from clinician requests and achieved promising performance. Notably, in a debiased pneumothorax classification task on chest radiographs, where chest drains can act as a major confounder, the system successfully mitigated shortcut learning and nearly halved the model's reliance on chest drains. These findings provide proof of concept that autonomous coding agents may help shift clinical AI development toward a more clinician-driven paradigm, reducing the communication overhead and dependence on specialized AI developers. Although further validation and robustness assessment are needed, this study suggests a promising path toward making clinical AI development more accessible.

---


> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
