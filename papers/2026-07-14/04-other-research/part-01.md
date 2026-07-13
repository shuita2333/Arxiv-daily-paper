# 📦 其他研究 | 2026年07月14日

> 本类共 **147** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-147](./part-03.md)

---

### 1. [Interval Certifications for Multilayered Perceptrons via Lattice Traversal](https://arxiv.org/abs/2607.08773)

**<font color=#1a73e8>作者：</font>** Merkouris Papamichail, Konstantinos Varsos, Giorgos Flouris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work we present a rigorous theoretical framework to a foundational problem of AI safety, namely adversarial robustness. In particular, we show that the adversarial robustness problem can be reduced to a lattice traversal problem. Each element of this lattice corresponds to an interval, i.e., an axis-aligned hyper-rectangle, containing an input point $\mathbf{x}$. Consider a multilayered perceptron classifier (MLP). An interval $I$ constitutes a sound certification if $\mathbf{x} \in I$ and $\mathbf{x}$ can be freely perturbed in $I$ without changing the MLP's prediction. Complementarily, an interval $I$ constitutes a complete certification if $\mathbf{x} \in I$ and when $\mathbf{x}$ moves outside of $I$ the MLP's prediction is guaranteed to change. While the sound certification problem corresponds to the well-studied adversarial robustness, complete certifications have not been examined in the literature. We develop lattice traversal operators, which we apply in a refine & verify iterative scheme. Using formal MLP verifiers, sound maximality and complete minimality are guaranteed. Moreover, we examine objective optimization problems. There we discover some interesting asymmetries. For complete certifications, the minimum solution is obtained in polynomial oracle calls. This does not hold for sound certifications, where we prove strong intractability results. Additionally, we examine optimization problems in symmetric intervals (i.e., $\ell_\infty$-spheres), where we provide logarithmic algorithms. Finally, we present an empirical evaluation, using the novel ParallelepipedoNN system.

---


### 2. [LieBN: Batch Normalization over Lie Groups](https://arxiv.org/abs/2607.08783)

**<font color=#1a73e8>作者：</font>** Ziheng Chen, Yue Song, Rui Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Manifold-valued measurements are prevalent in various machine learning tasks. Recent advances have extended Deep Neural Networks (DNNs) to operate on manifolds, accompanied by normalization techniques tailored to different geometries, collectively referred to as Riemannian normalization. However, most existing Riemannian normalization methods are either designed for specific manifolds or fail to effectively normalize manifold-valued sample distributions. To address these limitations, we propose LieBN, a framework for Riemannian Batch Normalization (RBN) over Lie groups. Our approach leverages the theoretically convenient left- and right-invariant metrics, which naturally exist in every Lie group, and provides theoretical guarantees for controlling the Riemannian mean and variance. We instantiate LieBN across nine distinct geometries: four on the Symmetric Positive Definite (SPD) manifold, one on the group of rotation matrices, and four on the manifold of full-rank correlation matrices. Notably, among the SPD metrics, we introduce a novel right-invariant metric and extend three existing Lie group structures via matrix power deformation. Extensive experiments on different manifolds validate the effectiveness of our framework. The code is available at this https URL.

---


### 3. [HERO: A Heterogeneity-Aware Benchmark Library for Federated Continual Learning](https://arxiv.org/abs/2607.08784)

**<font color=#1a73e8>作者：</font>** Thinh T. H. Nguyen, Le-Tuan Nguyen, Minh-Duong Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated continual learning (FCL) evaluates how distributed clients learn from changing data streams while retaining previously learned knowledge. Existing evaluations are difficult to compare because they often change datasets, task splits, client data splits, task orders, backbones, memory assumptions, and reporting rules simultaneously. We introduce \textbf{HERO}, a heterogeneity-aware benchmark library for FCL. HERO builds benchmark streams by separating three choices that are often coupled, namely the task split, the client data split, and the client task sequence. In HERO-Core, the main comparable benchmark, $\alpha$ controls client data skew and $\rho$ controls task-order mismatch. We evaluate representative FCL methods on CIFAR-100 and TinyImageNet using final average accuracy, average forgetting, and bottom-10\% client accuracy. We also include a graph-based Domain-IL portability case study on OGB-MolPCBA, where scaffold-domain granularity changes the input distribution while the prediction task remains fixed. Our results show that method behavior changes across easy and heterogeneous settings, that average accuracy can hide weak bottom-client performance, that task-order mismatch favors different strategies from synchronized evaluation, and that the same HERO interface can expose domain-shift difficulty beyond image-based FCIL. HERO releases benchmark streams, configurations, method implementations, and reporting scripts to support reproducible and setting-aware FCL evaluation.

---


### 4. [DaDaDa: A Dataset for Data Pricing in Data Marketplaces](https://arxiv.org/abs/2607.08785)

**<font color=#1a73e8>作者：</font>** Qiheng Sun, Hongwei Zhang, Junxu Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-quality data drives machine learning advances across industries. Recognizing the value of data, data transactions are increasingly common, giving rise to many data marketplaces, e.g., AWS Marketplace, Databricks, and Datarade. However, determining the appropriate prices for data products remains a significant challenge due to the unique properties of data products. Traditional pricing methods in economics can be categorized into the cost approach, the income approach, and the sales comparison approach. The cost approach fails in data pricing due to near-zero marginal cost from data replication, and the income approach fails due to inherently unpredictable data revenue. The sales comparison approach remains viable, yet its application is hindered by the absence of standardized pricing benchmarks for data products across marketplaces. To address this challenge, we introduce \texttt{DaDaDa}, the first dataset for data product pricing, containing metadata for 16,147 data products from 9 major data marketplaces worldwide. \texttt{DaDaDa} enables the training of pricing models, thereby establishing price benchmarks for new data products. In addition, \texttt{DaDaDa} can be utilized for other important tasks in data markets, such as data product classification and retrieval. Experiments and a retrieval prototype demonstrate the effectiveness of \texttt{DaDaDa} for pricing, classification, and retrieval of data products. The dataset and code are available at this https URL.

---


### 5. [Adaptive Bayes exactly tracks information over intrinsic time](https://arxiv.org/abs/2607.08789)

**<font color=#1a73e8>作者：</font>** Akshay Balsubramani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian and multiplicative-weights updates reweight experts, models, or actions from sequential feedback. We show that the regret of any such update obeys an exact information-accounting identity. On each round, the learner's excess loss to any chosen comparator is the sum of an immediate payment for the uncertainty exposed by the round and a reduction in the information distance from the learner's current weights to the comparator. The cumulative payment defines a pathwise uncertainty clock, the \emph{intrinsic time} of the realized sequence. Summing one-step balances yields two exact adaptive decompositions of cumulative regret, one for each natural way of composing the update across rounds. Because the decompositions are exact rather than upper bounds, favorable stochastic or low-noise regimes appear as self-bounding properties of the realized intrinsic time, not as slack in worst-case analyses. The same calculus covers Hedge, optimistic and side-information variants, continuous priors, boosting, online convex optimization, contextual bandits, and repeated games: the pathwise account is the same in every case.

---


### 6. [A Seed for Privacy -- semi-automatic privacy-revealing data reminder in databases and data streams](https://arxiv.org/abs/2607.08801)

**<font color=#1a73e8>作者：</font>** He Gu, Thomas Plagemann, Vera Goebel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sharing databases and data streams imposes the danger of revealing private information in the form of complex events which can comprise individual data elements and their combinations. Identifying these privacy-revealing complex events is crucial for preserving privacy while maintaining data utility. However, data producers often lack the expertise to comprehensively identify these events, which undermines many state-of-the-art privacy-preserving mechanisms that rely on accurate event labeling. To address this challenge, we developed pArborist - a tool that can semi-automatically create a set of queries to identify and label privacy-revealing complex events in both static datasets and dynamic data streams, guided by the privacy requirements of the data producer. pArborist uses the schema of the database or data stream combined with initial input from the data producer, i.e., seed queries. From each seed query, pArborist grows a tree containing all possible syntactically correct queries, constrained by an upper limit on computational resources. Following this growing phase, the tree is refined by eliminating queries that lack correlation to the seed or are conditionally independent of the seed. Our evaluation indicates that pArborist achieves overall recall of 90% and precision of 93% in finding privacy-revealing queries, and this significantly surpasses the state-of-the-art approach FQID. In data stream processing experiments, pArborist introduces a delay of approximately 1.3 ms following an average warm-up period of 920 ms. The experiments also show that pArborist can automatically detect privacy-revealing complex events according to GDPR.

---


### 7. [StereoSplat+: Feed-Forward Stereo Gaussian Splatting with Diffusion-Assisted Progressive Inference](https://arxiv.org/abs/2607.08808)

**<font color=#1a73e8>作者：</font>** Zihua Liu, Masatoshi Okutomi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D Gaussian Splatting (3DGS) have enabled high-quality, render-ready scene representations for novel-view synthesis. However, most existing 3DGS pipelines rely on multi-view observations (or non-causal access to future frames) to achieve sufficient coverage, which is often unavailable in on-device robotics and AR settings where sensing is restricted to a single stereo rig. Recovering a high-quality 3DGS scene from one stereo observation, therefore, remains challenging due to occlusions, limited field of view, and missing geometry. We present StereoSplat+, a diffusion-enhanced feed-forward framework that enables causal reconstruction from a single stereo pair. Our method builds on two key components. First, we propose StereoSplat, an input-invariant feed-forward 3D Gaussian estimator that takes a variable number of posed stereo pairs as input and predicts high-quality 3D Gaussians. StereoSplat fuses complementary geometry cues via a cost-volume branch and a triplane-based 3D volume branch and leverages continuous pose encoding to generalize across view counts and camera configurations. Second, since multiple posed stereo pairs are typically unavailable at inference time, we introduce a diffusion-enhanced one-shot progressive inference scheme called StereoSplat+: starting from one stereo pair, we render novel stereo views from the predicted 3DGS, refine them with a one-step diffusion enhancer, and feed them back as additional inputs to update the 3DGS. Experiments on the KITTI-360 dataset show that StereoSplat+ improves novel-view rendering quality and geometry accuracy, especially in occluded regions and under strong view extrapolation, outperforming recent feed-forward 3DGS baselines.

---


### 8. [Privacy-Preserving Intent Fulfilment and Assurance for 6G RAN](https://arxiv.org/abs/2607.08809)

**<font color=#1a73e8>作者：</font>** Joss Armstrong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intent-based network management is the emerging paradigm for 6G service lifecycle automation, with the 3GPP intent management framework (TS~28.312) defining creation, translation, fulfilment, and assurance stages. Existing fulfilment and assurance approaches require deep packet inspection, per-flow state tracking, or access to vendor-internal node telemetry to verify that provisioned resources satisfy expressed intents. These requirements conflict with regulatory constraints (GDPR, ePrivacy Directive) in multi-tenant networks and with vendor opacity in multi-vendor O-RAN deployments.
We present an architecture for privacy-preserving intent fulfilment and assurance in which a coordinator provisions resources from declared intent categories without traffic inspection, and verifies fulfilment using only aggregate standardised PM counters at the O1 interface. A data-processing inequality argument shows that the resource allocation reveals at most $\log_2 K$ bits about traffic content, where $K$ is the number of intent categories. We define two architectural privacy properties, intent-traffic unlinkability and node-opaque verification, and show that both hold by construction. Node-opacity does not sacrifice detection power: the aggregate verifier weakly dominates the per-agent verifier under a homogeneity condition.
We map the architecture to the 3GPP intent lifecycle and the O-RAN Non-RT RIC, identifying the concrete interfaces, data objects, and deployment points at which the mechanism operates. On production PM counter data from four operator networks, increasing intent-category granularity sharpens provisioning but weakens assurance, consistent with the theoretical prediction that the privacy ceiling is a structural side effect of the detection constraint rather than a separate design parameter.

---


### 9. [How are linear representations learned? Exact solutions to the dynamics of abstraction](https://arxiv.org/abs/2607.08843)

**<font color=#1a73e8>作者：</font>** William W. Yang, Andrew M. Saxe, Peter E. Latham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In artificial and biological neural networks, concepts are often encoded as consistent linear directions in representation space. In deep learning, this idea is known as the linear representation hypothesis and underpins many interpretability and control methods based on linear probes, from concept detection to activation steering. Yet while prior work has studied whether such directions should exist $\textit{after}$ training, the dynamics of how they emerge $\textit{during}$ training remain poorly understood. Here, we develop a framework to study the alignment of concept directions during training - a process we call "abstraction". In a minimal linear network setting, we obtain exact solutions for the full trajectory of abstraction. These solutions reveal key analytic principles governing abstraction: (i) data and target geometry jointly determine abstraction at the end-of-learning, (ii) abstraction improves with network depth, and (iii) initialization scale controls the maximum abstraction reached during training. Extending our theory to nonlinear networks, we analyze how the choice of nonlinearity affects abstraction dynamics: erf networks approximate the linear theory, while abstraction in ReLU networks depends less on target geometry and more on input geometry. Across both, we prove a striking attenuation law: both nonlinearities weaken abstraction in activations relative to preactivations. We find evidence for this law in open models (DINOv3, Gemma 4) and apply our theory to improve linear probe generalization in LLMs. Together, our results provide a dynamical theory of abstraction with implications for interpretability and control.

---


### 10. [Entropy Bootstrapping for Wireless Embedded Systems](https://arxiv.org/abs/2607.08865)

**<font color=#1a73e8>作者：</font>** Javier Blanco-Romero, Florina Almenares Mendoza, Daniel Díaz-Sánchez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Weak randomness has broken deployed cryptography through implementation bugs, boot entropy scarcity, and backdoored generators. Inexpensive wireless sensors concentrate the risk because many boot or operate in highly deterministic conditions while relying on basic, rudimentary, or opaque RNGs. On ESP32-class boards, RF-disabled wireless device RNG register (WDEV) output is pseudorandom by specification yet passes the same statistical screens as RF-active states, showing that output tests cannot replace source-state admission. We propose a defense-in-depth boot path for ESP32-class IoT nodes that combines SRAM startup material, radio burst extraction, and asymmetric entropy capsules under explicit source-state admission. In radio burst extraction, a trusted node in the local IoT network, such as a gateway or dedicated entropy node, sends a public packet burst to open a measurement window. The client samples its own WDEV output and packet timing during that window, then credits only the local response. Capsules cover the cold-start case with a pre-provisioned asymmetric key pair. The trusted node encrypts fresh seed material to the client's public key and signs the capsule; the client verifies, decapsulates, and hashes before it has local entropy. We benchmark the ESP32 RNG under several radio operating modes, the fixed-burst extraction window, the deterministic capsule client path, and SRAM startup reads. Together, these measurements support an admission policy in which each root is credited only when its required source state and protocol checks hold.

---


### 11. [Secure-by-Disguise: A Systematic Evaluation of Image Disguising for Confidential Medical Image Modeling](https://arxiv.org/abs/2607.08867)

**<font color=#1a73e8>作者：</font>** Jason Rojas, Jiajie He, Yash Patel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cloud-based deep learning enables large-scale medical image analysis but raises significant privacy concerns when sensitive patient images are outsourced for model development. Image disguising has recently emerged as a promising privacy-enhancing technology (PET) that transforms images into visually unintelligible representations while preserving information for downstream learning. We established a unified framework to evaluate representative methods, DisguisedNets and NeuraCrypt, across four datasets involving classification and semantic segmentation tasks. Our analysis assessed predictive utility, efficiency, and robustness against reconstruction attacks. Results showed that image disguising performance varies significantly between tasks; while methods preserved utility for medical image classification, they caused substantial degradation in dense semantic segmentation. Specifically, Randomized Multidimensional Transformation (RMT) offered the optimal balance of performance and security, whereas AES-based disguising severely impacted utility. Furthermore, regression-based reconstruction attacks effective on natural images proved considerably less successful on realistic medical images. These findings provide a systematic assessment of PET suitability for confidential medical AI applications.

---


### 12. [Decoupled Illumination Priors for Spatially Controllable Multi-View Indoor Scene Relighting](https://arxiv.org/abs/2607.08879)

**<font color=#1a73e8>作者：</font>** Chenjian Gao, Linning Xu, Tianfan Xue  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Indoor scene relighting demands photorealism, precise spatial control, and strict multi-view consistency. While diffusion-based image editing models enable semantic lighting manipulation via text prompts, enforcing exact 3D light placement often disrupts their generative priors. We propose Lume-Palette, a progressive framework that leverages semantic lighting priors for spatially controllable multi-view indoor relighting. The approach decouples relighting into two stages: (1) illumination distillation, which extracts canonical illumination palettes from a pretrained diffusion model to preserve realistic material-light interactions, and (2) illumination casting, which explicitly maps target spatial lighting conditions defined from coarse 3D geometry. To efficiently handle dense multi-view and multi-modal inputs, we introduce an asymmetric multi-view conditioning strategy that selectively injects essential spatial context. Experiments on diverse synthetic scenes and real-world scenes demonstrate that Lume-Palette produces photorealistic, spatially controllable, and multi-view consistent relighting results. Project Page: this https URL

---


### 13. [HAT Super-Resolution and a PARSeq+CLIP4STR Voting Ensemble for Extreme In-the-Wild License Plate Recognition](https://arxiv.org/abs/2607.08896)

**<font color=#1a73e8>作者：</font>** Karthik Sivarama Krishnan, Koushik Sivarama Krishnan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe our entry to the ICIP 2026 Grand Challenge on Extreme In-the-Wild License Plate Super-Resolution (XLPSR), which scored 9.73 wECR on the public validation leaderboard. The system pairs a Hybrid Attention Transformer super-resolution (HAT) front-end with an ensemble of two scene-text recognisers (PARSeq-S and CLIP4STR-B) and a confidence-weighted character-voting scheme that abstains on uncertain positions. We treat XLPSR as a recognition task gated by image legibility: the SR step exists to lift characters out of sub-pixel territory, and the asymmetric scoring rule (+2 / -1 / 0) is exploited explicitly through abstention. Our pipeline runs in 1.7 s per sequence on RTX 3090 (max 2.7 s, p99 2.4 s), well under the 60 s/sequence Docker budget.

---


### 14. [Proof-of-Continuity: A Temporal Model for Authority Propagation in Distributed Systems and AI Agents](https://arxiv.org/abs/2607.08906)

**<font color=#1a73e8>作者：</font>** Nicola Gallo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Proof-of-Possession authorization models derive authority from the possession of artifacts such as tokens, credentials, or capabilities. This paper argues that possession is insufficient for discrete execution chains, whether they span multiple services or occur as separated steps within the same machine, because it does not guarantee preservation of the causal relationship between the origin of a request and the authority exercised at later steps. We introduce Proof-of-Continuity, a minimal authority-propagation discipline for the Provenance Identity Continuity (PIC) model, in which each execution step must be causally linked to the previous step and may only propagate a non-expansive subset of the authority received from the origin. It introduces Proof of Relationship, a single-hop causal primitive whose transitive composition is Proof-of-Continuity; these complement Proof-of-Possession rather than replace it. Under this model, the confused deputy condition cannot be satisfied as valid model behavior: any privilege exercised at a later step must already be present in the origin authority context. This is directly relevant to distributed systems and AI agents, where executors invoke tools and downstream services while holding multiple authority sources, so that the same authority/causality mismatch recurs across service boundaries. Under Proof-of-Continuity these sources may be carried together but are never merged into a combined authority, since each step is authorized only against the authority context of the lineage that caused it.
This paper concerns authorization propagation rather than authentication: identity and authentication mechanisms such as OIDC, verifiable credentials, wallets, and workload identity remain complementary mechanisms for establishing the origin, while Proof-of-Continuity addresses how authority propagates after that origin exists.

---


### 15. [MemeBuddy: Dialog-Style Audio Representations for Engaging Non-Visual Meme Experiences](https://arxiv.org/abs/2607.08912)

**<font color=#1a73e8>作者：</font>** Chirag Bhansali, Vikas Ashok, Hae-Na Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Image memes are a pervasive form of online communication, widely used to convey humor, opinions, and cultural references. Prior work has explored making memes accessible to blind users, primarily through auto-generated descriptive captions. While these approaches improve comprehensibility and sometimes incorporate prosodic or emotional cues, they often fail to capture the humor, narrative structure, and contextual nuances that make memes engaging. We present MemeBuddy, a system that models memes as dialog, generating structured, multi-turn audio representations using role-based speakers. MemeBuddy reinterprets a meme as a conversation between two speakers, integrating extracted meme text with contextual knowledge implicitly inferred by a multimodal LLM (e.g., recognition of common meme templates and cultural references) to convey intent, timing, and implicit meaning through conversational interaction. We evaluate MemeBuddy in a user study with 14 blind participants. Results show that dialog-style meme representations consistently improve engagement and user satisfaction compared to caption-style descriptions, while maintaining comparable comprehension.

---


### 16. [Pattern-Aware Graph Neural Networks for Handling Missing Data](https://arxiv.org/abs/2607.08915)

**<font color=#1a73e8>作者：</font>** Minett Tran, Taehee Jeong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Missing data is ubiquitous in real-world datasets. Traditional methods either discard incomplete samples or apply imputation techniques that ignore potentially informative missingness patterns, implicitly assuming that missingness occurs randomly. However, missingness patterns might provide additional information. We propose pattern-aware graph neural networks that explicitly encode which features are missing alongside observed values. We used four encoding strategies -- learned embeddings, frozen random embeddings, statistical features, and hierarchical representations -- across seven UCI datasets with naturally occurring missingness. Our Pattern-aware methods achieve substantial improvements over baselines, with an average improvement of 17\% in balanced accuracy and 22\% in F1-macro across all datasets. The benefits vary significantly by dataset: annealing shows dramatic improvement (+80\% balanced accuracy), while hepatitis and soybean show minimal gains (+4--5\%). Notably, even simple random pattern embeddings perform comparably to learned embeddings (0.650 vs 0.663 balanced accuracy), suggesting that distinguishing between patterns may be more important than task-specific optimization. Our ablation study reveals that attention mechanisms, while helpful, are not critical when pattern information is available -- simple mean aggregation with pattern awareness achieves 0.640 balanced accuracy compared to 0.645 for attention-based variants.

---


### 17. [A Machine Learning Surrogate for Component Criticality Ranking in Interdependent Power-Communication Networks](https://arxiv.org/abs/2607.08918)

**<font color=#1a73e8>作者：</font>** Sohini Roy, Xheni Hylviu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cyber-physical power systems are vulnerable to cascading failures caused by tight interdependencies between power and communication infrastructures. Evaluating these failures over large N-k contingency sets with a high-fidelity simulator is computationally prohibitive for resilience planning. Using the previously published Modified Implicative Interdependency Model (MIIM) as the ground-truth cascade simulator, this paper develops a machine-learning surrogate that predicts contingency severity from leakage-free structural features and derives a component-criticality ranking for prioritized hardening analysis. On the IEEE 118-bus system, the Gradient Boosting surrogate achieves Spearman correlations of 0.849 for per-contingency severity prediction and 0.853 for per-component criticality ranking, while remaining stable across three independently sampled datasets. MIIM-derived component criticality itself reproduces only to a Spearman of approximately 0.85 under the present sampling pipeline, and the surrogate operates at this empirical ceiling to within sampling variation. Topological centrality measures on the full interdependent network provide meaningful baselines (Spearman 0.60-0.69), and feature ablation shows that the surrogate's advantage is driven primarily by inter-layer dependency information. These results support a two-stage workflow in which the surrogate rapidly ranks candidate components and MIIM is reserved for selective verification.

---


### 18. [SafeExplorer: An Unbiased Policy Gradient for Reinforcement Learning with Recovery Interventions](https://arxiv.org/abs/2607.08925)

**<font color=#1a73e8>作者：</font>** Elham Daneshmand, Majid Khadiv, Glen Berseth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training reinforcement-learning agents directly on physical robots makes every fall costly, since a fall can damage the platform and cannot be undone like a simulator reset; the goal is therefore to minimize falls during training rather than trade them off against return, as constrained Markov decision process (MDP) formulations do. A standard mitigation hands control to a separate recovery policy whenever the agent leaves a designer-specified safe region (a subset of state space it should stay within), but the resulting mixed-policy rollouts silently bias every on-policy update, and the importance-sampling correction that would remove this bias is ill-defined whenever the recovery policy is deterministic. We address this bias with a drop-in modification of proximal policy optimization (PPO). Its core is an unbiased policy-gradient estimator that uses the score function only at safe timesteps and never evaluates the recovery policy's density, so it stays valid even when the recovery policy is deterministic, exactly where importance sampling breaks, and it empirically dominates importance sampling even when the recovery policy is stochastic. Because the recovery policy still makes credit assignment slow near the safe-region boundary, two further components accelerate learning: a closed-form value for recovery-triggering states when dynamics and recovery are deterministic, and an imitation loss that copies recovery actions only when recovery succeeds. On a three-environment, five-seed benchmark, the resulting algorithm reduces training-time falls by factors of 233x, 48x, and 26x on HalfCheetah, Ant, and Unitree Go1 over standard PPO, while matching or exceeding PPO's final reward, and on Ant, where the recovery policy is unreliable, it is the only method that reaches 80% of the best final reward.

---


### 19. [Vision Transformers Learn Gestalt-Like Figure-Ground Cues from Natural Images](https://arxiv.org/abs/2607.08932)

**<font color=#1a73e8>作者：</font>** Matthias Tangemann, Benjamin Lo, Zygmunt Pizlo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Figure-ground organization in the human visual system relies on several shape-based cues, including surroundedness, convexity, and symmetry. While these cues have been extensively studied using abstract stimuli, little is known about how they operate under natural conditions or how they arise from the statistics of natural scenes. Deep neural networks offer a promising path forward: a model that relies on the same figure-ground cues as humans would provide tractable experimental access to the underlying mechanisms. In this study, we evaluate shape-based figure-ground organization in Vision Transformers (ViTs), for which prior work has demonstrated the emergence of object-based grouping. We test 25 ViTs spanning supervised and self-supervised training objectives, by fitting linear probes to predict figure-ground assignment from intermediate patch representations using both natural images and controlled artificial stimuli that isolate individual cues. Our results show that ViTs robustly encode surroundedness and convexity, and that probes trained on natural images generalize zero-shot to artificial stimuli across several models. For symmetry we observe mixed results: the cue is encoded for uniformly colored but not for textured regions. Taken together, our findings demonstrate that Gestalt-like figure-ground cues can be learned from natural scene statistics and position ViTs as a compelling model system for studying the computational mechanisms of perceptual organization.
Code and data is available at this https URL

---


### 20. [Is sub-metre resolution necessary for cocoa mapping? A landscape-stratified evaluation of very high resolution imagery, decametric Earth Observation inputs, and operational products in Cote d'Ivoire](https://arxiv.org/abs/2607.08945)

**<font color=#1a73e8>作者：</font>** Kasimir Orlowski, Filip Sabo, Michele Meroni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate cocoa mapping is increasingly important for deforestation monitoring, supply-chain transparency, and regulatory applications. Spatial aggregation in conventional medium-resolution Earth observation (EO) imagery may limit cocoa detection in heterogeneous smallholder landscapes. In Cote d'Ivoire, we therefore evaluated how mapping performance varies across landscape conditions, whether very high resolution (VHR) imagery provides a meaningful advantage, and whether foundation-model embeddings improve decametric cocoa mapping. We developed models using 0.5 m Pleiades VHR imagery, a 10 m Sentinel-2 annual composite, and embeddings from TESSERA and AlphaEarth Foundations (AEF), and additionally assessed four publicly available cocoa mapping products. Performance was evaluated through a landscape-stratified accuracy assessment using 2,821 independently interpreted reference points distributed across gradients of tree cover density and landscape fragmentation. The VHR model achieved the highest performance (F1 = 0.92) and maintained F1-scores above 0.90 across all strata. Among the decametric inputs, TESSERA performed best (F1 = 0.86), followed by AEF (F1 = 0.82) and Sentinel-2 (F1 = 0.76). Of the existing cocoa products, the Kalischek product performed best (F1 = 0.83), comparable to the internally trained AEF model. Performance differences between VHR and decametric approaches increased with fragmentation and under low and high tree cover density conditions. Targeted VHR acquisition may therefore be particularly beneficial in complex cocoa landscapes, while foundation-model embeddings offer a scalable alternative for large-area mapping.

---


### 21. [Training, Reading, and Editing Legible Transformers](https://arxiv.org/abs/2607.08946)

**<font color=#1a73e8>作者：</font>** Mark Oskin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A transformer can be built from operators that are legible by construction -- bounded, named units that read as fuzzy set operations rather than dense activations -- but legibility must be pressed for during training, and the pressure has a failure mode. A crispness penalty meant to sharpen a bounded operator into a decisive detector instead collapses it into a dead constant. An identity, E[v(1-v)] = mu(1-mu) - var, shows why -- the penalty is a variance-minimizer blind to the difference between a live detector and a constant -- and names the fix: a per-channel variance floor, the target legibility metric written as a loss, which recovers both legibility and quality. A learned per-unit fraction then retires the hand-set reserved-GELU partition of prior work: given the choice the model keeps no unit as pure GELU and routes 87% of its load-bearing computation through crisp operators. The result is the most legible transformer we have built -- 78% of its feed-forward operands and 50% of its attention value channels are crisp-and-contextual detectors, and per-head legibility rises from 18% in shallow layers to 78% in deep ones. Read in the correct rotated per-layer frame, these units separate a clean detection (what a unit responds to) from a harder naming (what its output decodes to); and because the objective makes each unit crisp and sparse, edits to them are far more local -- 50-184x in the deep layers where the edit sites concentrate -- and can target explicit conjunctions a single neuron cannot express. Finally, a between-unit decorrelation pressure exposes a legibility dial: it trades a circuit's reuse for independence at no quality cost, turning concepts into single, surgically editable units and a prediction into a short explanation read off a handful of named operations. Quality holds at parity with a conventional baseline throughout.

---


### 22. [FairSelect: A Systematic Evaluation of Multi-Level and Intersectional Algorithmic Fairness](https://arxiv.org/abs/2607.08953)

**<font color=#1a73e8>作者：</font>** Nick Souligne, Isabella Mixton-Garcia, Vignesh Subbian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Algorithmic fairness methods are increasingly used to identify and mitigate bias in machine learning models, yet most approaches are evaluated in isolation and along single demographic axes. This limits practical guidance for selecting fairness strategies, where disparities may arise across intersectional subgroups and across multiple stages of the modeling lifecycle. This work presents FairSelect, a toolkit for systematically evaluating fairness mitigation strategies applied individually and in combination across preprocessing, inprocessing, and postprocessing stages. FairSelect supports multiple model architectures, intersectional subgroup evaluation, and comparison of fairness utility tradeoffs across baseline, single method, and multi level configurations. The framework was validated using synthetic clinical datasets designed to represent specific bias mechanisms and a real-world replication of two-year stroke risk prediction among patients with atrial fibrillation. Synthetic experiments showed that targeted fairness methods generally reduced intended subgroup disparities, while combined strategies produced larger average fairness improvements with modest utility tradeoffs. In the clinical prediction task, mitigation effects were highly variable, with some combinations improving both fairness and predictive performance while others were ineffective or counterproductive. These findings demonstrate that fairness interventions interact in nonadditive and context dependent ways. FairSelect provides a practical framework for systematically identifying fairness strategies that improve subgroup equity while preserving model performance in clinical machine learning.

---


### 23. [Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading](https://arxiv.org/abs/2607.08964)

**<font color=#1a73e8>作者：</font>** Zongxia Li, Zhongzhi Li, Yucheng Shi 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents have become capable of autonomously completing short, well-specified tasks. However, existing terminal benchmarks largely focus on simple problems that finish within minutes and are evaluated only by their final outcome. This setup overlooks intermediate progress and partial solutions, yielding sparse reward signals and an incomplete picture of agent capability. We introduce Long-Horizon-Terminal-Bench, a terminal benchmark of 46 long-horizon tasks spanning nine categories, including experiment reproduction, software engineering, multimodal analysis, interactive games, and scientific computing. Each task follows a Terminal-Bench-style setup with a reference solution or simulation engine, but is further decomposed into fine-grained graded subtasks. This design enables dense intermediate rewards and partial credit, allowing evaluation to capture not only whether an agent reaches the final goal, but also how far it progresses on open-ended workflows. Tasks in Long-Horizon-Terminal-Bench typically require hundreds of episodes and minutes to hours of execution, stressing long-horizon planning, long-context management, and iterative debugging rather than one-shot problem solving. We evaluate 15 frontier models and find that agents consume on average 9.9M tokens per task, with roughly 231 episodes and 85.3 minutes of execution time per run, making Long-Horizon-Terminal-Bench more demanding than prior terminal-based benchmarks. Even the strongest tested model achieves 15.2% pass@1 at a partial-reward threshold of 0.95 and 10.9% at a perfect-reward threshold of 1.0, while the mean pass rate across models is 4.3% and 1.7% under the two thresholds, respectively. These results reveal headroom for improvement. We further analyze failure modes and error patterns, and release Long-Horizon-Terminal-Bench to support future progress on long-horizon terminal agents.

---


### 24. [MultiView-Bench: A Diagnostic Benchmark for World-Centric Multi-View Integration in VLMs](https://arxiv.org/abs/2607.08970)

**<font color=#1a73e8>作者：</font>** Hantao Zhang, Jinru Sui, Ed Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent benchmarks for VLMs largely assess single- or limited-view perception, leaving untested the core cognitive ability to integrate observations across viewpoints into a coherent, world-centric (allocentric) 3D mental model. We introduce MultiView-Bench, a diagnostic benchmark expressly designed to evaluate multi-view integration for holistic 3D scene comprehension. Unlike existing datasets that focus on pixel-level mapping or camera-relative navigation, MultiView-Bench requires models to decouple object positioning from transient perspectives and ground them in a fixed global coordinate system. This capability serves as a prerequisite for VLMs before being deployed for downstream tasks such as mechanical part assembly. Our systematic evaluation of frontier VLMs reveals consistent failure modes: strong performance on 2D planar relations from a single image, but marked difficulty with 3D spatial relations and with aggregating information across views. We further identify biases in VLMs, such as struggles with unconventional axis directions and sensitivity to object colorways and texture variations. Acknowledging these limitations, we propose ViewNavigator, a multi-agent framework that actively selects informative viewpoints, perceives, and fuses multi-view evidence, improving diverse base models on MultiView-Bench even under a strict budget-matched comparison (and by 3-5x for the full agent).

---


### 25. [Stochastic Linear Bandits with Partially Observed Actions](https://arxiv.org/abs/2607.08971)

**<font color=#1a73e8>作者：</font>** Gautam Dasarathy, Vineet Gattani, Lalit Jain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The stochastic linear bandit, where actions are represented as vectors and rewards are linear, is a central paradigm for sequential decision making. We study a partially observed variant of this problem in which the learning agent only sees a random subset of coordinates for each action. Such partial observability arises naturally in settings like recommendation and healthcare, where full action descriptions can be expensive or even impossible to obtain. In general, this makes sublinear regret information-theoretically impossible. However, we show that this barrier can be overcome when the action vectors have low intrinsic dimension. We propose an algorithm, TOFU-POV, that estimates the latent action subspace using the masked actions, imputes current actions using an epoch-wise frozen representation, and runs OFUL in the resulting low-dimensional coordinates. Our theory shows that TOFU-POV enjoys a $\sqrt{T}$ regret that scales with the intrinsic action subspace dimension as opposed to the ambient dimension and quantifies the interaction between these quantities and the missingness, decision set size, and subspace conditioning. We also devise a rank-adaptive algorithm that does not require the knowledge of the intrinsic dimension. We complement these guarantees with a lower bound based on a novel product construction that separates usual reward-learning uncertainty from a missingness-dependent cost intrinsic to partial observation. Synthetic and real data experiments support our theory and show that TOFU-POV can substantially improve upon natural baselines in this challenging problem.

---


### 26. [Federated Low-Rank Koopman Learning for Multivariate Time-Series Anomaly Detection in IoT Systems](https://arxiv.org/abs/2607.08978)

**<font color=#1a73e8>作者：</font>** Tung-Anh Nguyen, Van-Phuc Bui, Anh Tuyen Le 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed IoT systems generate multivariate time-series streams for monitoring physical assets, servers, and embedded sensing platforms. Detecting abnormal temporal behavior is critical for fault diagnosis, predictive maintenance, and security. However, practical IoT anomaly detection is hindered by decentralized and non-IID data, limited bandwidth, and the constrained computation and memory of edge devices. This paper proposes FedKAD, a resource-efficient federated Koopman anomaly detection framework for distributed IoT multivariate time series. Unlike deep-learning-based anomaly detectors that require training and communicating large neural models, FedKAD learns normal temporal dynamics through lightweight sliding-window Koopman representations. Federated training is formulated as a low-rank consensus problem, where raw sensor streams and local reduced dynamics remain on device while only compact subspace variables are exchanged with the server. To optimize the shared representation under orthonormality constraints, we develop a federated Stiefel-ADMM algorithm and provide convergence and stationarity analysis under partial client participation. During inference, each client detects anomalies locally by measuring the prediction residual between observed future trajectories and the learned Koopman dynamics. Experiments on four widely used multivariate time-series anomaly detection benchmarks show that FedKAD maintains or improves detection performance compared with federated deep-learning baselines. More importantly for IoT deployment, FedKAD provides up to $2.1\times10^3$ faster training, $80\times$ lower communication, and $79\times$ lower inference latency than neural baselines, confirming its suitability for resource-constrained edge devices.

---


### 27. [Optimal Top-$k$ Identification from Pairwise Comparisons](https://arxiv.org/abs/2607.08979)

**<font color=#1a73e8>作者：</font>** Motti Goldberger, Nils Rudi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the active learning problem of fixed-confidence top-$k$ identification from noisy pairwise comparisons. In this problem, an algorithm sequentially chooses pairs of items to compare, observes the outcomes, and stops when it can return the set of top-$k$ items with error probability at most $\delta$. The objective is to design such a $\delta$-correct procedure that minimizes the expected number of comparisons (the sample complexity). This problem falls within the broader literature on fixed-confidence pure exploration in bandit models, where a common target is asymptotic optimality: the algorithm's expected sample complexity matches the information theoretic lower bound as $\delta \to 0$. Asymptotically optimal procedures have been developed for a range of fixed-confidence pure-exploration problems, however to the best of our knowledge, for top-$1$, or more generally top-$k$ identification from pairwise comparisons under latent utility models an asymptotically optimal algorithm has not been established. In this setting, we develop such an algorithm. We characterize the structure of the lower bound and formulate it as a saddle-point problem. This structure enables a computationally efficient primal-dual procedure that learns the asymptotically optimal comparison allocation online. We then construct an adaptive comparison-allocation algorithm that tracks the allocation learned by the primal-dual procedure and prove it is asymptotically optimal.

---


### 28. [AlphaZero in Sparsely Rewarded Games: Limits and Auxiliary Supervision](https://arxiv.org/abs/2607.08984)

**<font color=#1a73e8>作者：</font>** Brent Kong, Tejas Ram, Tony Yue Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AlphaZero has demonstrated that a neural-guided Monte Carlo Tree Search can achieve superhuman performance, but strong play does not necessarily imply perfect play. We study this gap in two oracle-evaluable domains with contrasting structure: Connect Four, a solved partisan game with exact game-theoretic values, and Chomp, an impartial game whose optimal play is governed by Grundy-number structure. Under a unified self-play $+$ MCTS pipeline, we compare vanilla AlphaZero, a multi-frame variant (limited to Chomp), and an AlphaZero Auxiliary Loss (AZAL) that adds oracle-derived policy supervision. We find that vanilla AlphaZero achieves strong play across both domains but cannot preserve the exact trajectories required for optimal play: in Connect Four, it fails to maintain the optimal line of play, while in Chomp, it fails to consistently restore the $g=0$ invariant. On rectangular Chomp boards, multi-frame inputs alone do not remove this gap. Nevertheless, AZAL substantially improves oracle consistency across multi-seeded full-game traces and sampled-state evaluations. On Chomp, AZAL reaches perfect full-game oracle consistency on 10x11 and high but not complete consistency on 9x10; on Connect Four, AZAL improves oracle-match rate and delays the first oracle mistake, but does not reach perfect play.

---


### 29. [A Formalization of the Mean-Field Derivation of the Vlasov Equation: AI-Assisted Lean Formalization as a Strategy Game](https://arxiv.org/abs/2607.08986)

**<font color=#1a73e8>作者：</font>** Joseph K. Miller  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We formalize a research result in the Lean 4 proof assistant by having a mathematician direct an AI system, and frame the activity as a formalization game. The objective is to turn a LaTeX document into Lean. The game is won when the development compiles, contains no sorry, and a machine check shows the target theorems rest on Lean's foundational axioms alone. Reuse is a second check, by a definition we introduce: whether the development yields a self-contained layer of general mathematics the wider library could absorb. The case study is a complete, axiom-clean formalization of well-posedness for the nonlinear Vlasov equation via Dobrushin's mean-field route -- existence, uniqueness, the stability estimate and mean-field limit, and a short-window superposition principle (weak solutions are Lagrangian). The human's role was to direct, not to write proofs: to scope the definitions, steer the decompositions, and triage the library's gaps; the AI agent executed. The formalization certifies the proof of each statement as written; whether the written statement is the intended theorem stays the mathematician's judgment. The optimal-transport machinery that fell out of the build (in particular, properties of the Wasserstein-1 metric and the Kantorovich-Rubinstein duality theorem) separates into a self-contained layer that compiles against Mathlib alone: about a sixth of the development (49 of 299 declarations), behind a 22-declaration interface with no reverse dependency. The headline theorems ran in about a week, the full development in about a month. We report the quantitative claims as observations of one game, not as general laws. The game's rules name no particular system, so the methodological framing is meant to outlast the tools of any one run.

---


### 30. [Group Invariant Spectral Embedding](https://arxiv.org/abs/2607.08987)

**<font color=#1a73e8>作者：</font>** Yeari Vigder, Paulina Hoyos, David Thong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectral embedding methods are widely used for dimensionality reduction and clustering of high-dimensional datasets with intrinsic low-dimensional structures. Although many datasets of practical interest exhibit invariance under symmetries such as rotations, standard spectral embedding methods do not account for this, treating symmetry-related data points as unrelated. Our approach to this problem is to incorporate the symmetries directly into the affinity kernels used for spectral embedding. We analyze the case of a Riemannian data manifold $M$ with symmetries given by a compact Lie group~$G$ and prove that, under suitable conditions, graph Laplacians constructed from three types of invariant kernels converge pointwise to explicit second-order differential operators on the quotient space $M/G$. Our analysis implies improved convergence rates, as the effective dimension drops according to the dimension of the group. We validate our approach on datasets with $\mathrm{SO}(2)$ or $\mathrm{SO}(3)$ symmetry, and show that $G$-invariant spectral embedding recovers the intrinsic geometry of the data, in contrast to standard spectral embedding, which fails to do so even in the limit of infinite data.

---


### 31. [Model Agnostic Graph Prompt Learning for Crystal Property Prediction](https://arxiv.org/abs/2607.08996)

**<font color=#1a73e8>作者：</font>** Shrimon Mukherjee, Kishalay Das, Partha Basuchowdhuri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks have emerged as a powerful tool for the fast and accurate prediction of various crystal properties. These models often encode domain-specific knowledge into their graph encoding modules, which increases their parameter size and makes their performance heavily dependent on domain expertise. Added to this, explicitly incorporating all chemical and structural features, that might influence a specific crystal property into the GNN encoder, is a challenging task. In this work, we propose a soft prompt learning framework that captures latent features essential for property prediction, which are not explicitly provided to the GNN. We introduce a novel multilevel graph prompt learning framework comprising both node-level and graph-level soft prompts. At the node level, we capture the local chemical semantics of different atom types, while at the graph level, we encode the global structural symmetry of the crystal graph. Our proposed prompt learning framework is lightweight and seamlessly integrates with any existing GNN encoder. Extensive experiments on popular benchmark datasets show that incorporating prompt learning significantly improves (3\% - 15\%) the performance of state-of-the-art GNN models in crystal property prediction tasks. Furthermore, the learned soft prompts enable cross-property knowledge transfer, enhancing prediction performance for properties with limited training data. Code is available at this https URL

---


### 32. [RaMark: Radioactive Watermarking for Generated Tabular Data](https://arxiv.org/abs/2607.09000)

**<font color=#1a73e8>作者：</font>** Xin Che, Lingyang Chu, Qiqi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative modeling have made generated tabular data a practical solution for privacy-sensitive data sharing, where watermarking enables ownership verification. However, existing watermarking methods fundamentally fail under retraining attacks, in which an adversary retrains a generative model on a watermarked dataset and regenerates high-utility data that no longer carries the watermark. We address this challenge by introducing radioactivity, the property that a watermark remains detectable after generative model retraining, and propose RaMark, a radioactive watermarking method that embeds a sinusoidal dependency as an intrinsic component of the data distribution. By coupling the watermark with the underlying distribution, RaMark ensures that any generative model preserving data utility also has to preserve the watermark. We theoretically show that with high probability removing watermark degrades utility and alters data distribution. Extensive experiments on two real-world tabular datasets, under a large-scale ownership verification setting with $10^5$ independent data owners, demonstrate that RaMark achieves substantially stronger radioactivity than seven state-of-the-art methods and consistently outperforms them against both retraining and data modification attacks.

---


### 33. [Living Inside the Black Box: Behavioral Probing and Adaptation in Mandatory Wearable Sensing](https://arxiv.org/abs/2607.09009)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Bingyi Liu, Ruiqi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wearable sensing systems in high-stakes institutional contexts translate behavioral data into consequential judgments, yet wearers have little access to how those judgments are made. We present a qualitative study of 24 individuals who experienced mandatory electronic monitoring in China's community corrections system. We show that participants built what we term sensor literacy under constraint, a practical form of risk-oriented knowledge developed through uncertainty, behavioral probing, and adaptation. We identify two orientations across rule domains. Where participants had mapped system behavior, they sometimes regained limited flexibility. Where uncertainty remained costly, they contracted movement and discretionary activity beyond formal rules. Some former wearers described residual habits of calculation after device removal. We discuss design implications for making institutional sensing intelligible to wearers, including sensor uncertainty, usable documentation, and evaluation after device wearing.

---


### 34. [Secret Scanner Agent: Extracting Secrets and Access Context from Unstructured Documents](https://arxiv.org/abs/2607.09011)

**<font color=#1a73e8>作者：</font>** Zixiao Chen, Mariko Wakabayashi, Charlotte Siska  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Exposed documents such as emails, chat threads, tickets, and incident notes routinely leak credentials, but during incident response a leaked secret is only half the story. Responders also need to identify the ``door'' the secret opens: the account, tenant, endpoint, database, cloud resource, or other system that the credential could allow an attacker to access. Traditional secret scanners rely on regular expressions or trained classifiers which work well on well-formatted code, yet they struggle when a credential is fragmented, reformatted, or far from the resource it unlocks, and they report the secret string without naming what it opens. We present Secret Scanner Agent (SSA), a multi-agent large-language-model system that extracts both the secret and its associated door, together with supporting evidence, from unstructured exposed documents. SSA pairs a detection agent that favors recall with a review agent that filters false positives and recovers missing context. Because real credential data is sensitive, we evaluate SSA on synthetic benchmarks we generated that span 23 secret types and multiple document formats, scored with a three-step pipeline of programmatic matching, an LLM judge, and human review. Across six models, multi-agent SSA improves extraction precision over a single-agent variant, with the largest gains on door extraction, by up to 16 percentage points. SSA matches a regular-expression scanner's precision while more than tripling its recall, and against thirteen security analysts it is more precise, recovers nearly twice as many secret--door pairs, and runs five to seventeen times faster. By returning the secret, its door, and supporting evidence in one result, SSA turns credential detection into an actionable finding for triage and remediation.

---


### 35. [Central Tendency Bias in Human Selection of AI-Generated Design Variations](https://arxiv.org/abs/2607.09018)

**<font color=#1a73e8>作者：</font>** Huiyang Chen, Keqing Jiao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Image-generation AI systems increasingly support creative work by producing multiple design variations for users to evaluate and select. In such human-AI co-creation workflows, selection becomes a critical stage where human judgment guides AI-generated possibilities toward final outcomes. While presenting multiple alternatives is intended to encourage exploration, the simultaneous multi-option presentation may introduce systematic biases in human decision making. Drawing on ensemble perception theory, we investigate whether these interfaces induce central tendency bias-the tendency to favor options closer to the center of a design set. We conducted a controlled experiment manipulating the variance of design sets (high vs. low) and measured participants' selections in both aesthetic preference and representativeness tasks. Results show that higher variance increases the selection of center-proximal designs across both tasks. These findings suggest that multi-variation interfaces in image-generation AI systems may constrain selection diversity, revealing a potential tension between diversity in generated outputs and diversity in human selection outcomes.

---


### 36. [Privacy Detective: A Narrative Game that Cultivates Student Developers' Privacy Awareness by Harnessing Legal Documents](https://arxiv.org/abs/2607.09022)

**<font color=#1a73e8>作者：</font>** Shao-Yu Chu, Jennifer Forsyth, Xu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Developers' choices about what data a system collects, how it is used and shared, and what defaults govern user choices directly shape users' privacy experiences. Yet, developers often make problematic privacy-related design decisions without realizing the potential consequences. We introduce Privacy Detective, a narrative investigation game that leverages real-world legal documents to train developers' privacy awareness. In the game, players search for privacy violation evidence derived from legal documents and organize this evidence into privacy violation reports using curated templates. We evaluated Privacy Detective in a between-subjects study with student developers, comparing it against a baseline in which participants read raw FTC legal documents. Participants in the game condition identified more true violations than the baseline group, flagged fewer non-issues, and provided more complete justifications for the violations they reported.

---


### 37. [Variable-Length Generative Protein Design via Generalized Poisson Flow](https://arxiv.org/abs/2607.09039)

**<font color=#1a73e8>作者：</font>** Chaoran Cheng, Zhanghan Ni, Yanru Qu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ability to generate variable-length proteins is crucial in protein design, where the optimal length is often unknown and tightly coupled to designability. Current diffusion- and flow-based generative models typically require the protein length to be specified before sampling, limiting their flexibility in exploring the feasible design space. To address this limitation, we introduce Generalized Poisson Flow (GPFlow), a variable-length generative framework that learns the rate function of an inhomogeneous generalized Poisson process by minimizing its negative log-likelihood. We establish population-level guarantees for recovering the joint multimodal distribution and derive an upper bound on the KL divergence between the data and generated distributions. We comprehensively evaluate GPFlow across structure and sequence design, motif scaffolding, and peptide co-design, spanning Euclidean, categorical, and Riemannian modalities to fully validate its variable-length generation quality. In unconditional design, GPFlow improves structural designability and achieves the best distributional fitness for sequence design compared to their corresponding fixed-length baselines, while perfectly recovering the length distribution. In conditional motif scaffolding, GPFlow ranks first on 10 of 16 structure-based design tasks with significantly more unique successes and also achieves more passed tasks in sequence-based design. In peptide co-design, GPFlow remains competitive even without access to a native-length oracle.

---


### 38. [Learning More from Less: Reinforcement Learning from Hindsight](https://arxiv.org/abs/2607.09042)

**<font color=#1a73e8>作者：</font>** Iris Xu, Sunshine Jiang, John Marangola 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is increasingly used to post-train vision-language-action (VLA) models, but every update consumes robot rollouts that are slow and costly to collect, making sample efficiency a central concern. Manipulation tasks typically provide only sparse rewards, so a weak policy fails almost every rollout early in training and has little to learn from, even when those failures execute coherent behavior. Such a failure, however, is a success at a different task. We present Learning from Hindsight (LfH), which brings hindsight relabeling to RL post-training of VLAs by scoring failed rollouts against the tasks they actually achieved. A single vision-language model relabels both the instruction and the reward, proposing a hindsight instruction for a group of failed rollouts and scoring how well each satisfies it, and the policy trains on the relabeled and original rollouts jointly. Because VLAs generalize across language, relabeling in language lets the policy learn more from the same trajectories. On out-of-distribution LIBERO-PRO tasks, where standard RL improves only slowly, LfH achieves $5\times$ improvement in sample efficiency, and outperforms a dense progress-reward baseline. The gains hold across VLA backbones and on a physical Franka robot.

---


### 39. [STEAM: Stable Self-Training with Elastic Matching and Adaptive Purification](https://arxiv.org/abs/2607.09057)

**<font color=#1a73e8>作者：</font>** Shaoxiang Wang, Kejia Zhang, Haiwei Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view geo-localization (CVGL) aims to achieve GPS-free localization by matching drone-view images with corresponding satellite-view images. Existing supervised methods rely on large-scale manually annotated cross-view image pairs, making them costly and difficult to scale. In contrast, existing unsupervised approaches typically depend on generative models or clustering-based stage-wise optimization, which are prone to distribution bias and the accumulation of noisy pseudo-labels. To address these limitations, we propose STEAM (Stable Self-Training with Elastic Matching and Adaptive Purification), an end-to-end unsupervised cross-view geo-localization framework that performs self-training directly on real drone and satellite images. Specifically, the proposed Stable Spatial-Aware Module enhances the stability of feature representations, Elastic Matching discovers high-quality cross-view pseudo-labels, and Adaptive Purification dynamically maintains a reliable pseudo-label repository throughout the self-training process. Extensive experiments on the University-1652 and SUES-200 benchmarks demonstrate that STEAM achieves state-of-the-art performance among all existing unsupervised methods and delivers performance comparable to supervised approaches, validating the effectiveness and superiority of the proposed framework. The source code is available at this https URL.

---


### 40. [ARCANA: A Reflective Multi-Agent Program Synthesis Framework for ARC-AGI-2 Reasoning](https://arxiv.org/abs/2607.09059)

**<font color=#1a73e8>作者：</font>** Kunbo Zhang, Lei Fu, Zeyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present ARCANA, a collaborative multi agent framework for solving ARC AGI 2 tasks under strict test time and hardware constraints. ARCANA decomposes each task into iterative perception, hypothesis generation, symbolic execution, and reflective refinement. A perceptual grounding agent builds object centric scene graphs from raw grids, a latent program policy proposes diverse DSL programs, a symbolic executor verifies candidates on demonstrations, and a reflective agent synthesizes failure driven feedback for the next turn. These agents communicate through a shared differentiable blackboard and are scheduled by a learned meta controller. The design combines structured program search with adaptive multi turn correction, improving reasoning efficiency and solution quality on challenging abstract transformation tasks.

---


### 41. [On Locality and Length Generalization in Visual Reasoning](https://arxiv.org/abs/2607.09061)

**<font color=#1a73e8>作者：</font>** Pulkit Madan, Sanjay Haresh, Reza Ebrahimi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A striking feature of the human visual system is that it ingests visual information through a series of local foveated glimpses, rather than a single global computation. This makes human vision distinctly different from most popular computer vision models in use today, which input images globally and in a single shot. A natural question therefore is whether local, sequential vision models may provide any fundamental computational benefits in addition to being biologically more plausible than global models. In this work, we investigate this question from the perspective of visual state tracking and length generalization. Inspired by recent studies of length generalization in language models, we study the behavior of vision models trained on simple vision tasks that require the aggregation of local information across an image. Our experiments reveal that, similar to language models, vision models can learn to exploit global shortcuts and thereby fail to generalize over task length or complexity. We also show that recurrent vision policies based on strictly local perception can mitigate these failures, thereby allowing models to generalize on these tasks. Our results show that local attention may be an essential overlooked requirement for robust compositional generalization.

---


### 42. [EvoLP: Self-Evolving Latency Predictor for Model Compression in Real-Time Edge Systems](https://arxiv.org/abs/2607.09063)

**<font color=#1a73e8>作者：</font>** Shuo Huai, Hao Kong, Shiqing Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge devices are increasingly utilized for deploying deep learning applications on embedded systems. The real-time nature of many applications and the limited resources of edge devices necessitate latency-targeted neural network compression. However, measuring latency on real devices is challenging and expensive. Therefore, this letter presents a novel and efficient framework, named EvoLP, to accurately predict the inference latency of models on edge devices. This predictor can evolve to achieve higher latency prediction precision during the network compression process. Experimental results demonstrate that EvoLP outperforms previous state-of-the-art approaches by being evaluated on three edge devices and four model variants. Moreover, when incorporated into a model compression framework, it effectively guides the compression process for higher model accuracy while satisfying strict latency constraints. We open source EvoLP at this https URL.

---


### 43. [Probing Diffusion Denoising Dynamics for Contrastive Representation Learning](https://arxiv.org/abs/2607.09067)

**<font color=#1a73e8>作者：</font>** Yasong Dai, Zeeshan Hayder, David Ahmedt-Aristizabal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models exhibit unprecedented generative capability and contain rich intermediate representations that can be useful for discriminative vision tasks. Motivated by this observation, we study a focused question: how can the denoising dynamics of a pretrained diffusion model be adapted to support discriminative representation learning while preserving its generative behavior under parameter-efficient updates? We present D$^3$CL as an investigation of this question. Our key observation is that noisy latents at different diffusion timesteps can be interpreted as stochastic views of the same underlying image, enabling a contrastive objective to be coupled with the standard denoising reconstruction loss. This formulation provides a simple way to probe the interaction between generative denoising and discriminative representation learning without training from scratch. To keep the adaptation lightweight, we apply LoRA updates to a pretrained Stable Diffusion backbone while freezing the original model parameters. D$^3$CL provides strong empirical evidence that reconstruction and noise-level contrastive objectives can be complementary: on ImageNet-1K, it obtains 80.1% linear-probing accuracy and an FID of 5.56 for $256 \times 256$ unconditional generation. Additional ablations on the design space suggest that the usefulness of diffusion features depends on where and how denoising states are sampled. These results establish D$^3$CL as a parameter-efficient adaptation framework for pretrained diffusion models, showing that noise-level contrastive learning can structure denoising representations for discriminative tasks while maintaining generative performance.

---


### 44. [OmniMapBench: Benchmarking Visual-Centric Reasoning on Diverse Map Documents](https://arxiv.org/abs/2607.09068)

**<font color=#1a73e8>作者：</font>** Yang Chen, Yunwen Li, Yufan Shen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in LVLMs necessitate robust benchmarks for complex, visually grounded reasoning. A critical limitation is identified in many document understanding benchmarks: visual content is often reducible to text, enabling high performance without genuine visual grounding. To address this limitation, OmniMapBench is introduced to foster visual-centric reasoning for map documents. The benchmark comprises 2,096 manually annotated question-answer pairs across 1,603 map documents from nine categories. It is designed to probe a hierarchy of skills, ranging from perception to multi-step visual reasoning. To quantify benchmark properties, a simple yet effective benchmark-level metric is proposed: the Visual Dependency Index (VDI), defined as the accuracy drop when images are replaced with question-agnostic descriptions. OmniMapBench exhibits higher VDI than established benchmarks, which quantitatively validates its focus on irreducible visual reasoning. Comprehensive evaluations of 25 leading LVLMs are conducted on OmniMapBench. A significant performance gap is observed, with the top-performing model achieving only 75.03\% accuracy. This result underscores the challenges posed by OmniMapBench to current LVLMs. This work aims to catalyze progress in visual-centric reasoning for document understanding of LVLMs. The dataset and code are publicly available at this https URL.

---


### 45. [Pitfalls and Remedies for Multi-Task Bayesian Optimization](https://arxiv.org/abs/2607.09073)

**<font color=#1a73e8>作者：</font>** Carl Hvarfner, Sam Daulton, Max Balandat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization routinely warm-starts a target experiment with data from related source tasks, and the multi-task Gaussian process is the textbook surrogate for the job. We revisit this default in a controlled setting and find that it misestimates the cross-task correlation even in the simplest non-trivial case, affinely related source and target tasks, where a working transfer learning method should obviously succeed. We trace the failure to two independent structural mechanisms. Per-task standardization, the textbook fix for the affine slice ambiguity, propagates a finite-sample alignment error into the recovered correlation. The marginal likelihood itself identifies the correlation only at a per-sample rate that a Gaussian process at non-overlapping designs further dilutes. We propose three conservative remedies that follow from the analysis: promoting per-task means and scales to model parameters, restricting the task covariance to non-negative correlations, and co-locating part of the source and target designs. Across synthetic multi-task problems and surrogate-based hyperparameter tuning transfer, these remedies recover the target-only baseline on the simple instances, while the broader failure persists on harder instances and across most rank-based and latent-context variants.

---


### 46. [Toward Active Object Detection for UAVs in the Wild: A Large-Scale Dataset, Benchmark and Method](https://arxiv.org/abs/2607.09078)

**<font color=#1a73e8>作者：</font>** Tianpeng Liu, Xinhua Jiang, Li Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection is a fundamental component in numerous Unmanned Aerial Vehicle (UAV) applications, yet it has long been plagued by hindrances like occlusion or target pixel scarcity. Active Object Detection (AOD) provides a novel paradigm to address these challenges via active vision, while UAV-based AOD research remains scarce due to the lack of high-quality datasets and benchmarks for algorithm development and evaluation. To fill this gap, this paper presents ATRNet-LUDO, the first large-scale real-world dataset for UAV-Ground Active Object Detection (UGAOD). It contains 121,000 multi-view panoramic multi-target aerial images and 1.21 million local single-target slices, covering 10 vehicle targets across 40 scenarios. It enables the construction of diverse training and testing environments for UAV agent interaction and active observation policy learning. Based on this dataset, we establish a comprehensive evaluation benchmark for AOD policy learning methods. Most existing AOD policies rely on Deep Reinforcement Learning (DRL) but suffer from poor generalization. Evaluations on our benchmark reveal a significant generalization gap between training and testing performance, highlighting an urgent need for solutions. To this end, we leverage the Joint Embedding Predictive Architecture (JEPA) to construct a world model that enhances state representation learning, and propose AOD-JEPA by incorporating AOD-specific prior knowledge. Extensive experiments validate its effectiveness and superiority. We hope ATRNet-LUDO and the benchmark will advance research in the UGAOD field. The dataset and code are soon available at this https URL.

---


### 47. [Adaptive Latent Trajectory Anchoring for Action Segmentation Dataset Condensation](https://arxiv.org/abs/2607.09081)

**<font color=#1a73e8>作者：</font>** Artheme Gauthier-Villar, Guodong Ding, Angela Yao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset condensation for action segmentation synthesizes compact, informative representations of long, untrimmed video datasets. The existing approach relies on Variational Autoencoders and an iterative latent optimization; it is computationally expensive and suffers from over-smoothed reconstructions and rigid temporal constraints. This paper proposes to shift the condensation paradigm from optimization-based inversion to deterministic latent mapping. By leveraging Denoising Diffusion Implicit Models, we represent action segments as continuous trajectories anchored by sparse latent points in the noise manifold. To maximize representational efficiency, we introduce an adaptive allocation mechanism that dynamically redistributes the anchoring budget based on segment-wise reconstruction difficulty. Extensive experiments demonstrate that our framework significantly outperforms state-of-the-art methods in segmentation performance across common datasets. Notably, our approach achieves performance parity with real data training while maintaining a condensation ratio of 2.4\% on Breakfast dataset.

---


### 48. [REBASE: Reference-Background Subspace Elimination for Training-Free In-Context Segmentation](https://arxiv.org/abs/2607.09082)

**<font color=#1a73e8>作者：</font>** Mantha Sai Gopal, Jaison Saji Chacko, Harsh Nandwana 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free in-context segmentation enables new object categories to be introduced at inference time from a single annotated reference image, eliminating the retraining and memory overhead of class-incremental learning. Recent approaches achieve this by combining vision foundation models for semantic correspondence with promptable segmentation networks like SAM. However, their performance is fundamentally limited by the quality of the cross-image similarity map; shared contextual backgrounds between the reference and query systematically elevate similarity in non-target regions, degrading prompt localization. We present REBASE, a training-free framework that explicitly suppresses these spurious contextual correspondences. Our method identifies the low-rank background feature subspace from the reference image and project the reference and query features onto its orthogonal complement in closed form, yielding cleaner semantic matching. We then generate positive point prompts using similarity-weighted farthest-point sampling, paired with a refined dense similarity prior. Without any training or parameter updates, our approach establishes a new state of the art among training-free methods on PACO-Part, FSS-1000, and cross-domain datasets such as ISIC2018, demonstrating that explicit background subspace removal is a highly effective principle for one-shot localization.

---


### 49. [A Survey on the Green Development of Large Models: From Resource-Efficient Architectures to Hardware-Software Co-Design](https://arxiv.org/abs/2607.09084)

**<font color=#1a73e8>作者：</font>** Linhui Xiao, Guiping Cao, Mingyue Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of large-scale AI models has led to significant performance breakthroughs across diverse domains, yet it has also raised critical concerns regarding computational costs, energy consumption, and environmental sustainability. This survey provides a comprehensive overview of the green development of large models, emphasizing resource-efficient architectures and full-stack hardware-software co-design. We systematically review recent advances in efficient model construction, including attention operator optimization, linear-complexity architectures, and model sparsification and merging, as well as training and deployment strategies such as data-efficient learning, parameter-efficient fine-tuning, and computational compression. Beyond algorithmic improvements, we explore energy-efficient AI hardware, including mainstream AI chips, memory optimization, cross-platform deployment, and sustainable infrastructure. Furthermore, we examine how large models are being applied to sustainability-critical domains such as DeepSeek, remote sensing interpretation, national-scale infrastructure, and global initiatives. Finally, we discuss key challenges and future directions, highlighting the need for continual learning paradigms, memory-centric hardware, and standardized evaluation protocols. This survey aims to offer a holistic roadmap toward sustainable, scalable, and socially responsible development of large models. Paper homepage: this https URL

---


### 50. [Subtoken Vision Transformer for Fine-grained Recognition](https://arxiv.org/abs/2607.09086)

**<font color=#1a73e8>作者：</font>** Jie Zhu, Ivy Zhang, Minchul Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Subtoken Vision Transformer (SubViT), a selective image tokenization method for fine-grained visual recognition. Standard Vision Transformers compress each fixed-size patch into a single token, although fine-grained distinctions often depend on localized variations within only a few patches. SubViT addresses this mismatch by representing discriminative patches with multiple subtokens while retaining the original token sequence for global context, thereby allocating additional capacity where it is most needed. Since attention heads encode complementary semantics and extracting attention maps at inference requires an extra backbone forward, we adopt a two-stage training strategy. Stage 1 fine-tunes the ViT using subdivision regions sampled from random attention heads, exposing the model to diverse subdivision patterns. Stage 2 identifies informative attention maps through feature-degradation distances and distills them into a lightweight single-map router, which directly predicts deterministic token-importance scores without a separate attention forward. We evaluate SubViT on Generalized Category Discovery (GCD), a challenging task requiring both fine-grained discrimination and generalization to unlabeled novel categories. Across CUB, FGVC-Aircraft, and Stanford Cars, SubViT improves the average novel-category accuracy of DINOv2 from $81.3\%$ to $84.7\%$, with only $0.50$ ms additional latency and $3.4\%$ more FLOPs, while reducing latency by $73.8\%$ relative to Retina Patch. Results on CIFAR-10 and ImageNet-100 demonstrate its broader applicability.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-147](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
