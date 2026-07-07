# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 51. [Track the Noise, Move the World:3D-Grounded Motion-Consistent Noise for Controllable Video Generation](https://arxiv.org/abs/2607.02798)

**<font color=#1a73e8>作者：</font>** Long Vu, Tan Ngo, Animesh Karnewar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image-and-text-to-video diffusion models can synthesize highly realistic videos by iteratively denoising an initial Gaussian noise tensor conditioned on reference image and text inputs. However, existing approaches still lack precise and unified controllability over both object motion and camera motion within a single generation process. We present UniCaMo, a unified framework that enables simultaneous control of object trajectories and camera viewpoints by directly constructing the input noise of the diffusion model. Specifically, UniCaMo builds a shared 3D-grounded motion-consistent noise space across latent video frames. Sparse 3D point tracks are used to warp the Gaussian noise of the reference frame along desired object trajectories, while a virtual spherical noise representation provides globally consistent noise values for newly revealed scene regions under camera motion. By combining local track-guided noise warping with global sphere-based noise sampling, UniCaMo maintains geometric and temporal consistency under both object movement and viewpoint changes. Because UniCaMo modifies only the input noise, it requires no auxiliary adapters, control branches, or architectural changes to the underlying video diffusion model. With lightweight LoRA fine-tuning on large pretrained video diffusion models, including Wan 2.1 (14B), UniCaMo achieves state-of-the-art results in both video quality and motion controllability on standard controllable video generation benchmarks.

---


### 52. [Conversational Human Audio-visual Talking Dialogue Generation](https://arxiv.org/abs/2607.02799)

**<font color=#1a73e8>作者：</font>** Junhao Song, Lluis Guasch, Xilin He 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale dyadic interactive audio-visual dialogue (DIAD) datasets provide fundamental data resources for developing humanoid interactive virtual agents and digital humans. However, collecting such data is time-consuming, expensive, and ethically sensitive. To address this, we propose CHAT, a new dyadic interactive audio-visual dialogue generation (DIADG) framework that generates diverse, paired, and mutually responsive speech-face dialogue clips from a single textual prompt. CHAT unifies large language models and talking face models with interactive audio and facial behaviour refinement modules, enabling the generation of aligned dyadic dialogue clips with diverse contents and facial identities. Experiments show that CHAT outperforms existing related methods designed for similar tasks under both objective and subjective evaluations. Moreover, our synthesised CHAT-AVD-50k dataset serves as effective pre-training data for downstream interactive head generation, consistently improving PerFRDiff and ReactDiff on REACT 2024. CHAT offers a scalable alternative to the costly and ethically sensitive collection of real dyadic interaction data.

---


### 53. [Induction Heads Interpolate N-Grams](https://arxiv.org/abs/2607.02800)

**<font color=#1a73e8>作者：</font>** Francesco D'Angelo, Oguz Kaan Yuksel, Swathi Shree Narashiman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Induction heads are attention circuits believed to underlie in-context learning in transformers, yet a precise characterization of the estimators they implement remains elusive. We study transformers trained on order-$k$ Markov chains and identify two complementary smoothing mechanisms. First, at finite attention-weight scale, the circuit implements a soft context-matching estimator: it aggregates contributions from exact and partial context matches, weighted exponentially by their overlap, and induces a data-dependent interpolation across context orders analogous to Jelinek-Mercer smoothing. Second, a beginning-of-sequence (BOS) token induces additive pseudo-counts, recovering Dirichlet-style smoothing. We construct a disentangled transformer implementing both mechanisms and show that trained transformers recover the predicted attention patterns. Across settings where pseudo-count smoothing is optimal or lower-order contexts provide structured evidence, trained transformers match or outperform classical count-based baselines. Our results bridge mechanistic interpretability of induction heads with classical statistical smoothing, revealing that transformers learn to regularize in-context estimation rather than simply count.

---


### 54. [SwarmResearch: Orchestrating Coding Agents for Open-Ended Discovery](https://arxiv.org/abs/2607.02807)

**<font color=#1a73e8>作者：</font>** Yuvraj Virk, Zack Edds, Chunqiu Steven Xia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running coding agents such as autoresearch can persistently discover optimizations for open-ended problems. However, they tend to converge onto a single high-level approach, then proceed with low-level edits while missing other superior approaches to the problem. We hypothesize two harness-level design choices contribute to this behavior: accumulating context in a single long-running agent and only exposing a single program state to edit. We introduce SwarmResearch, an orchestrator-subagent harness in which a Shepherd Agent uses global context to steer a population of Search Agents, each operating with local context in their respective git branch. On open-ended optimization tasks, SwarmResearch discovers better or comparable solutions to state-of-the-art LLM-guided evolution and multi-agent techniques on 13/15 tasks, driven by higher-level exploration. Compared with fixed scaling of serial and parallel agents, SwarmResearch's orchestrator-guided scaling discovers better-performing solutions by adapting parallelism at different search depths.

---


### 55. [SovereignNegotiation-Bench: Evaluating User-Owned Personal Agents In Delegated Bargaining Under Privacy, Consent, Evidence, And Institutional Pressure](https://arxiv.org/abs/2607.02814)

**<font color=#1a73e8>作者：</font>** Dylan Zongmin Liu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Personal agents will increasingly negotiate on behalf of users: splitting costs with other personal agents, appealing platform decisions, escalating support disputes, requesting refunds, changing subscriptions, and negotiating deadlines or reimbursements. Existing negotiation benchmarks emphasize agreement, surplus, or strategic competence, but a user-owned agent can reach an agreement while harming the user through privacy leakage, consent violation, unsupported advocacy, over-concession, failed escalation, or poor auditability. We introduce SovereignNegotiation-Bench, a trace-level multi-turn benchmark for delegated personal-agent negotiation under private utilities, disclosure constraints, evidence requirements, and institutional asymmetry. The benchmark separates agent-visible observable state from evaluator-only labels and evaluates agreement success jointly with user utility, privacy, consent, evidence grounding, concession discipline, escalation, and auditability. We report an artifact-backed validation over 240 scenarios, 4 model families, 14 baselines, 13,440 frozen-prompt live trajectories, 61,135 parsed action rows, and a blinded 3-annotator audit over 300 items. The strongest agreement-maximizing baseline achieves the highest agreement rate but low user utility and high privacy/consent risk; FullSovereign does not maximize agreement, but obtains the best sovereign negotiation score by preserving utility, minimizing leakage, grounding claims, and reducing unauthorized commitments. The results show that agreement success is insufficient for user-owned negotiation agents.

---


### 56. [Git Hash Chain Malleability](https://arxiv.org/abs/2607.02820)

**<font color=#1a73e8>作者：</font>** Jacob Ginesin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Git commit signing is widely entrusted to serve as evidence that a commit hash uniquely and immutably identifies a specific piece of signed content. We show this invariant does not hold. Given any signed commit, an attacker without access to the signing key, and without breaking SHA2 can produce a second, distinct commit with an identical tree, identical metadata, a valid signature, and a ``Verified'' badge from a Git Forge such as Github, differing only in its commit hash. The modified commit cascades to modify the values of all the subsequent, dependent commit hashes, hence we introduce the terminology ``hash chain malleability'' to describe this phenomenon. The malleability in signed Git hashes is feasible due to the inherent malleability present in many of the data representations that make up a commit. In this paper we show three such malleation routes: (i) algebraic inversion s -> n-s for ECDSA; (ii) structural insertion of an unhashed OpenPGP subpacket (RFC4880 5.2.3) for RSA and EdDSA; and (iii) non-canonical DER length re-encoding (X.690 10.1) inside the CMS envelope for S/MIME. Algebraic inversion for ECDSA signatures and subpacket insertion were found to pass local verification (git verify-commit), and all three methods yield a persistent, independent ``Verified'' record on Github. We discuss the consequences of Git hash chain malleation for hash-based commit blocking, dependency pinning (Nixpkgs, Go modules, Github Actions), and reproducible-build systems that treat the commit hash as a content-addressable primary key, and we provide proof-of-concept tooling that automates all three routes.

---


### 57. [Less Tokens, Better Forecasts: Sparse Residual Routing for Efficient Weather Prediction](https://arxiv.org/abs/2607.02829)

**<font color=#1a73e8>作者：</font>** Janet Wang, Yunbei Zhang, Lin Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing ViT-based weather forecasting models apply uniform computation across all spatial tokens, even though nearby atmospheric grid points often contain similar values and large regions evolve smoothly over time. This makes much of the intermediate per-token computation redundant. Standard token-efficiency methods, such as pruning or merging, reduce cost by removing or fusing tokens. However, weather forecasting is a spatiotemporal dense prediction problem in which a history of atmospheric states must be mapped to future values on the original latitude-longitude grid. Thus, every grid cell must retain a physically meaningful representation, especially under autoregressive rollout. We introduce Sparse-Reslim, a parameter-free plug-in routing module that makes sparse token processing compatible with this fixed-grid requirement. Sparse-Reslim routes only 25% of spatial tokens through the expensive middle transformer blocks and treats those blocks as residual updates: it computes the change produced for the routed tokens and scatters only this delta back to the full sequence. Unselected tokens keep their pre-routing representations exactly, so no grid cell is dropped or replaced by a mask token, and no fusion layer or additional parameters are introduced. Across ERA5 resolutions up to the operational 0.25\textdegree{} standard and two model families, a deterministic Transformer and a diffusion model, Sparse-Reslim improves forecast accuracy on every evaluated variable while substantially reducing cost: training is about 2.5x faster in the main settings and reaches 3.18x speedup at 0.25\textdegree{}, with over 2.2x lower peak memory. A controlled decomposition shows that the accuracy gain comes primarily from sparse routing itself, while random token selection provides an additional regularization benefit without selector overhead.

---


### 58. [On the Design Space of Discrete Diffusion Online Adaptation for Molecular Optimization](https://arxiv.org/abs/2607.02834)

**<font color=#1a73e8>作者：</font>** Trevor Chen, Ariel Dai, Jason Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular optimization often starts from a pretrained generative model that captures a broad prior over valid molecular structures. At test time, however, the goal is not to sample from this prior, but to use a limited oracle budget to shift generation toward task-specific high-reward molecules. We study this adaptation problem for discrete diffusion models. Each online round couples several choices. The loop must decide which candidates to evaluate, how rewards become model updates, which feedback to reuse, and how far to move beyond the pretrained prior. These choices have mostly been studied in isolation, leaving open whether they complement one another, become redundant, or interfere inside a full online adaptation loop. We conduct controlled studies across six small-molecule binding-affinity tasks and three protein-fitness tasks. We find that acquisition, reward shaping, and model debiasing provide complementary routes to higher reward, especially for small molecules. Replay further stabilizes learning, while validity penalties keep small-molecule exploration on the valid molecular manifold. Together, these findings point to a practical recipe for feedback-efficient molecular optimization: online fine-tuning with acquisition, reward shaping, debiasing, replay, and validity control. This recipe outperforms offline fine-tuning and inference-time search baselines under matched oracle-call budgets and GPU-hour accounting. The gains are largest when high-reward candidates require larger shifts from the pretrained prior.

---


### 59. [ShannonProver: Towards Automating Formal Cryptographic Proofs](https://arxiv.org/abs/2607.02847)

**<font color=#1a73e8>作者：</font>** Yiping Ma, Yu-Lin Tsai, Mayank Rathee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographic proofs are produced at a scale that increasingly exceeds the community's ability to verify them manually. Machine-checked proofs offer a path toward scalable proof verification, but writing proof scripts for expressive proof assistants such as EasyCrypt remains a major bottleneck: even when the high-level proof plan is known, converting it into proof tactics requires substantial reasoning effort. This paper presents ShannonProver, an agentic framework for automating cryptographic proofs. ShannonProver targets the setting in which a cryptographer provides the security model and a decomposition of the target theorem into lemma-level proof obligations, while the system automatically constructs EasyCrypt proof scripts for those obligations.
We evaluate ShannonProver on a dataset of formal cryptographic proofs in EasyCrypt. The dataset spans textbook primitives, deployed protocols, and standardization efforts such as NIST proposals, and includes expert case studies drawn from a corpus that has not previously been available online. We show that ShannonProver can automate substantial portions of cryptographic proof engineering for case studies such as ChaChaPoly1305 and MEE-CBC. More broadly, this work suggests a path toward accelerating cryptographic research: as agents automate the proof-engineering burden, cryptographers can iterate more quickly on new constructions, obtain machine-checked assurance earlier, and bring trustworthy protocols from design to deployment faster.

---


### 60. [Labeled-Data-Free Meta-Learning: Efficient Task Generation Using Pre-trained Models and Unlabeled Data](https://arxiv.org/abs/2607.02850)

**<font color=#1a73e8>作者：</font>** Lei Sun, Yusuke Tanaka, Tomoharu Iwata  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Meta-learning without labeled data is crucial for real-world applications, where obtaining labeled datasets can be expensive or restricted due to privacy concerns. Data-Free Meta-Learning (DFML) addresses this challenge by leveraging pre-trained models without access to training data. However, existing DFML methods rely on model inversion to generate training data, a process that is generally difficult and computationally expensive due to the need to generate high-dimensional data matching the original distribution. To address this limitation, we propose a novel meta-learning setting that avoids model inversion by jointly leveraging pre-trained models and unlabeled data. Our method generates meta-training tasks by assigning soft labels from pre-trained models to unlabeled data. Since the quality of these tasks can vary, we introduce a task-weighting mechanism based on task confidence and class distribution balance to ensure effective meta-learning. Extensive experiments demonstrate that our approach substantially reduces computational cost and improves generalization, achieving up to 104-fold speedup and 8.4 percent to 36.4 percent improvements in few-shot classification accuracy compared to state-of-the-art DFML methods.

---


### 61. [Cancelable Biometric Template Protection Based on Multi-Instance Fusion: A Contralateral Iris Approach](https://arxiv.org/abs/2607.02860)

**<font color=#1a73e8>作者：</font>** Jittarin Chaivong, Nicha Vikromrotjananan, Teekatat Piriyapittaya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biometric templates are vulnerable to theft if stored without protection. Unlike passwords, a compromised iris cannot be reissued. Although existing cancelable biometric schemes address this problem, most still require an external key or token, introducing an additional attack surface. This paper proposes a cancelable contralateral iris template protection scheme that eliminates the need for a separate token or stored secret, satisfying the three requirements of ISO/IEC 24745: irreversibility, unlinkability, and confidentiality. The method fuses three enrollment samples per eye using Majority Vote Fusion to produce a stable template, and applies a salt-based bit permutation derived from the subject's enrollment ID. Combining the left- and right-permuted templates via a bitwise XOR produces a single Protected Fused Template. Since left and right iris patterns are statistically independent, fusing contralateral irises improves the accuracy of the system. An attacker must possess both iris codes and both salts to recover any useful information, yielding a larger effective key space than single-iris schemes. Experiments on three datasets, CASIA-IrisV4-Interval, CASIA-IrisV2 (two devices), and CASIA-Iris-Thousand, yield EERs of $0.36$\%, $4.88$\%, $10.80$\%, and $3.35$\%, respectively; the highest value reflects the more challenging cross-device scenario. These results demonstrate that our contralateral approach outperforms unprotected baselines while remaining competitive with state-of-the-art cancelable methods. %In addition, an ablation study confirms the benefit on both recognition performance and security. To the best of our knowledge, this is the first scheme to combine tokenless multi-instance fusion and contralateral binding under ISO/IEC 24745.

---


### 62. [Trading Confidence: Comprehensive Uncertainty Estimation in Algorithmic Trading](https://arxiv.org/abs/2607.02864)

**<font color=#1a73e8>作者：</font>** Lin Li, Li Rong Wang, Hsuan Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has emerged as a powerful approach in financial trading, enabling agents to learn optimal strategies through direct market interaction. However, financial markets are highly uncertain, with price fluctuations driven by stochastic volatility, model limitations, and regime shifts. Traditional RL models struggle in dynamic environments, often failing to adapt to sudden market disruptions, leading to suboptimal trading decisions. To address this challenge, we propose an uncertainty-aware RL framework that integrates distributional, epistemic, and aleatoric uncertainty estimations. Our approach enhances uncertainty estimation using SHAP-weighted reconstruction uncertainty, MC Dropout, and an LSTM-based technical indicator consensus mechanism. Experimental results on five major U.S. stock indices demonstrate that RL agents equipped with uncertainty estimation significantly outperform traditional models in return and risk management. This study advances uncertainty estimation in RL-based financial trading, with future research extending its application to other asset classes and alternative RL architectures for greater adaptability.

---


### 63. [E-TraMamba: A New Paradigm for Efficient Long-Term 3D Feature Tracking with Event Cameras](https://arxiv.org/abs/2607.02866)

**<font color=#1a73e8>作者：</font>** Juwei Shen, Yujie Wu, Changwen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based 3D tracking enables low-latency and high-speed perception, while existing CNN- and Transformer-based trackers struggle to capture long-range spatiotemporal dependencies in sparse, noisy event streams, especially under real-time and efficiency constraints. To address these challenges, we present E-TraMamba, the first Mamba-based framework for 3D feature tracking on event data. This new framework adopts a linear state-space model for efficient long-range modeling and integrates a lightweight affine-transform predictor to maintain stable tracking under motion blur and occlusion. We also design an effective scheme to fuse multi-scale cues -- local spatiotemporal patches, correlation maps, and positional embeddings -- into a unified representation that enables stable and smooth 3D tracking. We construct a large-scale synthetic dataset, named EvD-PointOdyssey, which is generated with monocular rendering and provides synchronized event streams, depth maps, and accurate 3D trajectories for training and evaluating event-based 3D tracking models. Extensive experiments on event-based benchmarks demonstrate that E-TraMamba achieves state-of-the-art performance, delivering over $2\times$ longer feature lifetimes under strict accuracy thresholds (e.g., 0.1 m), with higher tracked-feature ratios and lower RMSE than all baselines. These results make E-TraMamba a strong candidate for low-latency visual odometry, real-time SLAM, and interactive robotics.

---


### 64. [Poisson-Gamma Modeling of Inter-Relational Dependencies in Dynamic Knowledge Graphs](https://arxiv.org/abs/2607.02872)

**<font color=#1a73e8>作者：</font>** Nan Fang, Yijun Wang, Hao Liao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic knowledge graphs are ubiquitous in today's AI applications, as we represent molecular structures, social relationships, and language information using these graph models. As knowledge graphs evolve over time and are often noisy and incomplete, modeling their temporal and relational dependencies becomes crucial for downstream tasks. To address these challenges, this paper proposes PGRE (Poisson-Gamma Relational Evolution), a probabilistic model for modeling inter-relational dependencies in dynamic knowledge graphs. PGRE represents multi-relational temporal links via a Poisson-Bernoulli formulation. It introduces Gamma-distributed latent variables to capture entity-factor associations and cross-relation dependencies mediated by shared latent communities. A Gamma Markov process further models the temporal evolution of these latent variables, enabling principled characterization of relational dynamics. Experiments on benchmark datasets show that PGRE achieves competitive performance in link prediction, particularly in sparse settings, while revealing meaningful relational evolution patterns in dynamic knowledge graphs.

---


### 65. [Overprivilege Analysis of Security Policies in Serverless Cloud Applications](https://arxiv.org/abs/2607.02875)

**<font color=#1a73e8>作者：</font>** Elvis Yeboah-Duako, Pubali Datta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Serverless computing has seen rapid adoption in cloud deployments, yet the security implications of its service-oriented programming model remain poorly understood. Distributed, modular, and heterogeneous applications complicate the specification of precise security policies. Role-based access control solutions such as Identity and Access Management (IAM) already exhibit pervasive misconfiguration problems, and the multiplicity of functions, services, and resources in serverless applications, together with frequent permission model changes by cloud providers, greatly increases the likelihood of policy misconfigurations. Consequently, policies are often overprivileged, thereby enlarging the attack surface and exposing sensitive cloud resources to compromise.
We present a large-scale measurement study of overprivilege in real-world serverless applications, analyzing a curated dataset of 689 AWS Lambda applications comprised of 1,293 functions. To enable this study, we develop PrivLess, a static policy analysis framework that extracts function-to-resource interactions from application source code, derives an interaction-permission mapping, and reconciles inferred interactions with declared policies to quantify overprivilege. Our measurement reveals that overprivilege is systemic and severe across the serverless ecosystem: 47.7% of applications carry excess permissions with a significant privilege reduction potential of 99.65%. Applications with wildcard-defined permissions exhibited an average overprivilege ratio 274x higher than those without. More critically, the excess permissions enable concrete attack vectors: 18.8% of applications hold unnecessary Privilege Escalation capabilities, and 12 applications had Defense Evasion permissions they did not need.

---


### 66. [PraMem: Practice-derived Experiential Memory for Long-horizon Behavior Prediction](https://arxiv.org/abs/2607.02881)

**<font color=#1a73e8>作者：</font>** Zhuoqun Li, Boxi Cao, Jiawei Chen 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon behavior prediction aims to infer a user's next action based on a lengthy historical sequence, playing a crucial role in artificial intelligence field. The rise of large language models (LLMs) offers a promising direction for sequential behavior prediction, yet LLMs struggle with latent behavioral pattern induction and model-intrinsic cognitive biases when tackling long-horizon behavior prediction. Prior memory management methods follow a context-compression paradigm that attempts to address this task by alleviating the historical sequence burden, yet fail to resolve the core challenges. In this paper, we advocate a paradigm shift that reframes the lengthy historical sequence from a burden into a valuable resource to be exploited, and accordingly propose PraMem, which conducts beforehand practice over the lengthy historical sequence to build an experiential memory, thereby serving as the assisted input for accurate long-horizon behavior prediction. Extensive experiments across diverse tasks demonstrate that PraMem achieves superior performance than prior methods, and more in-depth analyses provide valuable insights into the mechanism and evolution of the experiential memory. Code: this https URL.

---


### 67. [SPLIT: Training-Free AI-Generated and Partially Edited Video Detection via Spatial Patch-Level Incoherence and Temporal Roughness](https://arxiv.org/abs/2607.02886)

**<font color=#1a73e8>作者：</font>** Jongyeop Hyun, Hyounghun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying AI-generated video detectors in real-world services demands an ultra-low false positive rate (FPR) on real videos to avoid falsely rejecting authentic content, a regime where standard metrics such as AUROC fail to reflect actual operating behavior. We introduce Spatial Patch-Level Incoherence and Temporal Roughness (SPLIT), a training-free detector that operates on patch tokens from a frozen vision encoder to detect both fully generated and partially edited videos. SPLIT computes two complementary signals: Two-step Temporal Roughness (TTR), capturing non-smooth patch trajectories via one-step and two-step feature variation contrast, and Local Spatial Motion Incoherence (LSMI), measuring spatially inconsistent temporal changes through gradients of a feature-space motion field. The two are fused multiplicatively with gamma correction to sharpen real-fake separation at strict thresholds. We further propose a service-aligned evaluation protocol based on Fake Recall at fixed FPR with real-only threshold calibration and cross-real threshold transfer. Across three benchmarks (FakeParts, GenVideo, and ViF-Bench), SPLIT achieves the highest Fake Recall at FPR = $0.1\%$, substantially outperforming supervised and training-free baselines while remaining robust to post-processing with negligible overhead. The code is publicly available at this https URL .

---


### 68. [Dynamic Regret for Non-Stationary Linear Bandits via Misspecification Reductions](https://arxiv.org/abs/2607.02891)

**<font color=#1a73e8>作者：</font>** Zihao Hu, Yuan Yao, Jiheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many online decision-making problems involve both round-specific feasible actions and drifting reward models: eligible ad impressions, feasible prices, and available treatments can change over time, while user preferences, demand curves, and patient responses may evolve. Motivated by these applications, we study non-stationary linear bandits with round-specific feasible decision sets. Existing methods that obtain the optimal \(\widetilde O(T^{2/3}P_T^{1/3})\) dependence, where \(P_T\) is the path length of the reward-parameter sequence, impose an orthogonal-structure assumption on round-specific decision sets, which can be restrictive in contextual applications. We address this gap through a unified misspecification-reduction viewpoint: after partitioning the horizon into blocks, we relate each block's dynamic regret to regret against a fixed-parameter linear bandit benchmark, with the within-block parameter drift entering as bounded misspecification. Restarting algorithms with misspecification-dependent regret guarantees then yields the optimal \(T^{2/3}P_T^{1/3}\) dynamic-regret dependence for both linear bandits with general compact decision sets and \(K\)-armed contextual linear bandits.

---


### 69. [TIER: Trajectory-Invariant Explanation Regularization for Membership Privacy](https://arxiv.org/abs/2607.02903)

**<font color=#1a73e8>作者：</font>** Varun Sharma, Kar Wai Fok, Vrizlynn L. L. Thing  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Explainability is central to building trustworthy AI, yet explanation interfaces can inadvertently provide adversaries with an expanded privacy-related attack surfaces. Recent studies show that advanced membership-inference attacks succeed by exploiting confidence-drop trajectories, induced through attribution-guided perturbations, as discriminative features, rather than directly using confidence scores or explanation vectors. Existing defenses against membership inference fail to directly mitigate such explanation-driven attacks. In this work, we investigate whether, during training, a model's own gradients can be leveraged as defense signals against such attacks, thereby aligning explanation profiles between members and non-members. To this end, we propose a Trajectory-Invariant Explanation Regularization (TIER) defense that penalizes erratic fluctuations in confidence drops simulated through gradient-guided perturbations and simultaneously minimizes the distributional shifts via KL-divergence. Unlike conventional adversarial training, which emphasizes label robustness, our approach targets explanation robustness by enforcing self-consistency through KL-divergence and reducing the variance of confidence drops between members and non-members. Extensive experiments confirm that our method effectively mitigates these attacks, delivering privacy protection while maintaining model utility and explanation fidelity.

---


### 70. [Holo-Captioning: Toward the Text Equivalent of 3D Scenes](https://arxiv.org/abs/2607.02908)

**<font color=#1a73e8>作者：</font>** Kun-Yu Lin, Chengke Bu, Zhenguo Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work introduces holo-captioning, a novel task that strives to seek the text equivalent of 3D scenes. As the initial step, we formulate holo-captioning as generating a structured textual description that comprehensively depicts all entities within a 3D scene -- including their semantic tags, spatial locations, attributes, and inter-entity relations. To tackle this challenging task, we first develop an effective captioning engine to produce detailed descriptions of individual entity instances and instance pairs, and contribute a large-scale benchmark comprising over 15K scenes for training and evaluation. Building upon this foundation, we propose HoloScribe, a novel model that features an instance-aware decoupled pipeline for generating structured holo-captions, and further incorporates anchor-aware instance linking to identify relational instance pairs. Additionally, we propose a comprehensive evaluation metric named HoloScore, and provide a human-curated test set to ensure reliable model assessment. Experimental results demonstrate that HoloScribe significantly outperforms state-of-the-art 3D dense captioners and 3D LLM generalists, underscoring the effectiveness of our approach. Project page: this https URL

---


### 71. [See the Emotion: A Facial Emoji Proxy Modeling for EEG Emotion Recognition](https://arxiv.org/abs/2607.02912)

**<font color=#1a73e8>作者：</font>** Jingjing Hu, Guo Dan, Haofan Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the high accuracy of EEG-based emotion recognition, existing models remain opaque "black boxes", lacking semantic grounding between abstract neural features and human-interpretable states. In this paper, we reframe EEG explainability as a cross-modal generation task, shifting the paradigm from feature attribution to behavioral visualization. We introduce Facial Emoji Proxy Modeling, a novel framework that translates high-dimensional EEG signals into identity-anonymized facial emojis. Guided by the neuroscientific inspiration of neural-facial association, this approach grounds neural representations in the manifold of observable facial dynamics. Technically, our framework integrates FMENet, a specialized backbone modeling expression-relevant spatial synergies, and the Facial Emoji Learning Branch (FELB), which treats emoji reconstruction as a structured semantic regularizer. Extensive experiments on EAV and MMER benchmarks demonstrate that our method achieves state-of-the-art accuracy among EEG-only models. Crucially, it generates semantically faithful facial animations that provide a transparent, privacy-preserving window into the brain's emotional evolution, effectively allowing users to "see the emotion" directly from neural signals. Code is available at this https URL

---


### 72. [Bootstrap Flow-Map Tree Sampling Enables Online Feedback Driven Search](https://arxiv.org/abs/2607.02915)

**<font color=#1a73e8>作者：</font>** Binglin Ji, Anindya Sarkar, Hengchang Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many scientific and engineering domains, maximizing discovery within a limited sampling budget demands strategic, observation-guided exploration. While generative models have enabled training-free reward alignment, current methods typically excel in local searches within narrow regions of the underlying distribution. These approaches struggle when preferences are unknown a priori and only revealed through sequential feedback-a scenario demanding broad exploration to uncover high-utility regions. To address this, we introduce Bootstrap Flow-Map-Tree (a.k.a BFMT), a novel computationally efficient sampling framework designed for history-aware global search and alignment under sampling budget constraints. BFMT enables full tree-path construction from any tree depth using a single function evaluation, drastically reducing computational overhead while providing critical foresight for sequential sampling. By enabling dynamic transition time steps scheduling, BFMT efficiently allocates its sampling budget, smoothly transitioning from broad global exploration to fine-grained local refinement of high-utility modes discovered through exploration. Extensive experiments and ablations across diverse search and alignment tasks demonstrate that BFMT substantially outperforms baseline approaches.

---


### 73. [R3D: Quantitative 3D Spatial Reasoning for Egocentric Wearables](https://arxiv.org/abs/2607.02921)

**<font color=#1a73e8>作者：</font>** Maxwell Horton, Wei Lu, Quan Tran 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative 3D spatial reasoning from egocentric RGB-D video is a critical capability for next-generation wearable assistants. Yet existing benchmarks do not reflect the challenges of handling (1) natural egocentric video, (2) posed RGB-D video inputs, and (3) challenging quantitative 3D spatial reasoning Q&A. To fill this gap, we introduce R3D-Bench (Reasoning in 3D), a benchmark of 3,033 quantitative spatial reasoning questions across 15 types -- spanning multiple-choice, distance-based, and volumetric reasoning questions -- built on top of 57 egocentric video sequences from Aria Digital Twin. To set a strong baseline on this dataset, we introduce R3D, a model-agnostic spatial tool-calling framework. In contrast to existing approaches that directly embed 3D information into the model's input representation, R3D constructs a 3D scene from video using segmentation and depth-lifted object representations. It provides this information to an LLM through eight composable spatial tools. On R3D-Bench, R3D with Qwen3-VL 235B achieves 73.5% mean relative accuracy, substantially outperforming the best depth-enabled baseline (CuTR+Tools, 61.9%) and the best RGB-only baseline (Gemini 3 Flash, 46.5%).

---


### 74. [STAC: Selective Spatiotemporal Aggregation and Compression for Video Reasoning Segmentation](https://arxiv.org/abs/2607.02922)

**<font color=#1a73e8>作者：</font>** Syed Ariff Syed Hesham, Yun Liu, Guolei Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video reasoning segmentation demands pixel-accurate object tracking across hundreds of frames under complex natural language queries, producing dense spatiotemporal tokens whose quadratic self-attention cost makes long-video processing prohibitive. Existing methods address this through token compression, yet typically operate on encoder features lacking temporal context, constraining selection before content redundancy can be reliably assessed. Informed compression requires contextual awareness, but acquiring that awareness at full resolution incurs the same quadratic cost compression aims to reduce. State-space models resolve this constraint, as their linear recurrence selectively conditions each token on temporal context at $\mathcal{O}(T)$ cost, producing representations where content redundancy becomes assessable. Building on this, Selective SpatioTemporal Aggregation and Compression (STAC) enriches features via decoupled bidirectional spatial and causal temporal scanning, leveraging recurrence-derived redundancy for hierarchical compression with adaptive thresholds optimised with segmentation objective. STAC achieves 85% token reduction and 1.8$\times$ speedup while surpassing compression-free baselines on reasoning segmentation benchmarks in a zero-shot streaming-compatible setting. Code is available \href{this https URL}{here}.

---


### 75. [CoFEND: A Cross-Modal Fusion End-to-End Network for Cold-Start Drug-Drug Interaction Prediction](https://arxiv.org/abs/2607.02928)

**<font color=#1a73e8>作者：</font>** Di Wu, Hongyi Sun, Haichao Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cold-start drug-drug interaction (DDI) prediction for new drugs is critical for minimizing unexpected adverse drug reactions. The key challenge is to capture similarity between new and known drugs. However, such similarity is closely associated with complex relationships and mechanisms among drugs, enzymes, transporters, molecular structures, and other biomedical entities. Existing methods have three limitations in capturing such similarity: (1) only partial relationships and mechanisms are considered, which overlooks cross-modal information and yields incomplete or biased similarity modeling; (2) similarity computation between new and known drugs is conducted separately across modalities and performed offline for cold-start DDI prediction, leading to misalignment between similarity computation and DDI prediction; and (3) existing interpretability analyses are typically single-modality and focus primarily on key determinants of the perpetrator drug, while the underlying causes of susceptibility for the victim drug are seldom investigated. To address these issues, this paper proposes a novel Cross-Modal-Fused End-to-End Learning Network (CMF-ELN) with three components. First, diverse multimodal information is leveraged to construct four types of drug-centered knowledge graphs, enabling comprehensive similarity modeling under reconstruction-based supervision. Second, a four-channel graph autoencoder is designed to fuse cross-modal similarity within an end-to-end learning framework. Finally, a two-stage interpretability scheme is devised to precisely localize key factors for both perpetrator and victim drugs. Extensive experiments on two real datasets demonstrate that CMF-ELN achieves significantly higher prediction accuracy and more comprehensive interpretability of mechanisms than its peers.

---


### 76. [VERITAS: Towards a General-Purpose Replication Tool for Scientific Research](https://arxiv.org/abs/2607.02931)

**<font color=#1a73e8>作者：</font>** Haokun Liu, Filbert Aurelian Tjiaranata, Chenhao Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI tools are accelerating scientific publication while the systems that review it struggle to keep up, and independent verification of published research has become both harder and more important. As manual replication is slow and expensive, a growing line of work uses coding agents to automate parts of the process. Existing efforts are largely packaged as benchmarks with companion agents that only run inside the benchmark's own pipeline, and no general-purpose replication tool exists. We present VERITAS, a domain-agnostic replication framework built around CLI coding agents. Given a paper, a code repository, or both, VERITAS extracts the paper's claims, runs the methodology while resolving issues as they arise, and judges each claim against the evidence from experiment runs. The pipeline returns an importance-weighted Replication Score, a severity-rated log of every fix applied, and the patched codebase. We evaluate VERITAS on CORE-Bench and ReplicationBench, 65 papers spanning computer science, social science, medicine, and astrophysics. Against two strong Claude Code baselines on the same model and host environment, VERITAS achieves state-of-the-art performance and leads on every metric on both benchmarks.

---


### 77. [PromptPET: Privacy-Utility Optimized Prompt Obfuscation](https://arxiv.org/abs/2607.02932)

**<font color=#1a73e8>作者：</font>** Ke Yang, Olivia Figueira, Umar Iqbal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy is an important challenge when users interact with AI chatbots, since users may share sensitive information, explicitly or implicitly, and AI chatbots can use this information for user profiling. In this paper, we aim to protect user privacy via a user-side mechanism that transforms sensitive information in a user prompt, while preserving enough information to elicit a useful response from the chatbot. This approach faces an inherent tradeoff between protecting privacy (i.e., avoiding profiling) and preserving utility (i.e., getting personalized and task-specific responses). To that end, we consider, evaluate, and compare four different obfuscation actions, namely redaction, abstraction, replacement, and a novel noising/denoising scheme that we introduce. Additional novel insights include: utilizing a data type taxonomy to both identify and obfuscate sensitive information and explicitly taking into account the utility of chat responses in making the obfuscation decision. First, we systematically optimize and evaluate each obfuscation action independently in terms of the privacy-utility tradeoff it achieves. Second, we propose PROMPTPET, an LLM-based agent that selects the best obfuscation action for each sensitive part of the prompt, using a reinforcement-learning inspired rule optimizer, applied for the first time in this context. Using a real-world chat dataset, we show that PROMPTPET matches the best privacy-utility tradeoff attainable by any single obfuscation action and significantly outperforms prior state-of-the-art approaches.

---


### 78. [MatPhaseBench: A Semantics-Guided Benchmark for Materials Phase Diagrams Understanding](https://arxiv.org/abs/2607.02934)

**<font color=#1a73e8>作者：</font>** Hanwen Wang, Sihan Liang, Zhiwei Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Materials phase diagrams are a core knowledge representation in materials science, encoding temperature,composition, phase stability, and phase transformation pathways, with their full understanding requiring thermodynamic mechanism analysis and scientific reasoning. Although VLMs have shown promise in scientific image understanding, their systematic evaluation on such logically complex images demanding deep mechanistic interpretation remains limited, and phase diagrams provide a challenging testbed for this purpose. We introduce MatPhaseBench, a high-quality, high-reliability benchmark for complex scientific image understanding, focused on materials phase diagrams. MatPhaseBench is constructed from 3681 papers in classical materials science journals, from which 200 high-quality diagram-text pairs were selected, covering 189 material systems and 70 elements. The benchmark has three key features: (1)targeting complex scientific image understanding-it moves beyond simple objective tests to open-ended tasks requiring deep comprehension; (2)comprehensive image-text alignment-semantic information associated with images is fully preserved during literature mining and matching; (3) high-quality human-supervised text acquisition-all descriptions undergo strict manual validation. Experimental results show that current VLMs remain substantially behind expert-level understanding: they are largely limited to surface visual perception, lack deep reasoning grounded in thermodynamic mechanisms, have limited domain awareness and expert analytical experience, and perform poorly in distinguishing fine-grained differences in composite or multi-diagram settings. Overall, MatPhaseBench constitutes a challenging research-grade benchmark, providing a foundational platform for complex scientific image understanding, phase diagram analysis, and trustworthy multi-modal AI in science.

---


### 79. [In-span learning: adapting reduced-order models using their own predictions](https://arxiv.org/abs/2607.02937)

**<font color=#1a73e8>作者：</font>** Amirpasha Hedayat, Laura Balzano, Karthik Duraisamy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reduced-order models compress high-dimensional dynamics into low-dimensional representations that can be evaluated rapidly, but they lose accuracy when online dynamics drift beyond the training data. Adaptive methods address this by updating the subspace online with external, out-of-span information, such as full-order corrections or sensor snapshots. We discovered that a complementary and previously unexploited in-span adaptation channel exists within the current reduced subspace. By streaming the model's own predictions through an incremental singular-value decomposition with forgetting, we obtain a trajectory-informed spectral preconditioner, in which the subspace is unchanged but the basis is reweighted and realigned toward the modes visited by the dynamics. This enables the model to absorb future out-of-span corrections more effectively. We expose aspects of this mechanism on a three-dimensional spiral and confirm it on viscous Burgers and Fisher-KPP dynamics. We also discuss how in-span learning can be viewed as a dynamical-systems analogue of in-context learning. More broadly, in-span learning suggests a new principle for computational science, revealing that model-generated trajectories contain more usable information than previously recognized.

---


### 80. [Missingness as Signal: Channel-Independent Spectrogram Learning for Clinical Time Series Prediction](https://arxiv.org/abs/2607.02938)

**<font color=#1a73e8>作者：</font>** Soyeon Park, Charmgil Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical time series prediction in intensive care units remains challenging due to heterogeneous physiological variables and informative missingness. The presence or absence of a measurement can reflect clinical decisions and patient severity, and thus missingness can serve as a predictive signal rather than a simple data artifact. This work presents CISM, a Channel-Independent Spectrogram framework with a Missingness stream for clinical multivariate time series prediction. CISM converts each clinical variable into a variable-wise time-frequency spectrogram, preserves variable identity through variable-aligned encoding, and aligns an explicit missingness stream with the spectrogram representation. Experiments on an in-hospital mortality task derived from MIMIC-IV show that CISM achieves the highest mean AUROC (0.7225), AUPRC (0.3308), and F1 (0.3808) among the compared time series, missingness-aware, vision, and time-frequency baselines. Ablation studies further show that observation patterns provide a meaningful informative signal. Pixel-level mask injection improves performance over plain spectrogram inputs and recovers much of this predictive value. The aligned missingness stream contributes a further, complementary gain in both AUROC and AUPRC. These results highlight the importance of modeling observation patterns as structured signals in clinical time series prediction.

---


### 81. [A Sliding-Window-Based Reinforcement Learning for Dynamic Assembly Flow Shop Scheduling with Multi-Product Delivery](https://arxiv.org/abs/2607.02941)

**<font color=#1a73e8>作者：</font>** Junhao Qiu, Jianjun Liu, Ting Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-product kitting delivery imposes significant challenges for real-time scheduling in hybrid manufacturing systems that integrate processing and assembly, as dynamic order arrivals simultaneously alter supply dependencies and the set of feasible job-machine assignments. This paper proposes a sliding-window-based reinforcement learning (SWRL) framework for end-to-end online scheduling in the flexible assembly flow shop scheduling problem with complex kitting constraints. The problem is formulated as a heterogeneous graph-based Markov decision process that captures the dual-layer kitting structure and the tail-product bottleneck dynamics that produce a sparse reward landscape. To address the resulting challenges, SWRL integrates a sliding-window filtering mechanism that filters inactive nodes and prioritizes kitting-critical operations, a spatiotemporal graph encoding network that tracks bottleneck shifts across consecutive decision states, and a dynamic action mapping module with a constrained waiting strategy that adapts to the changing action space under variable topologies. Experiments on real-world instances from a home appliance manufacturer demonstrate that SWRL achieves consistent tardiness reductions over classical dispatching rules and existing deep reinforcement learning methods, and exhibits robust performance across varying resource configurations, order loads, and arrival concentrations.

---


### 82. [A Precedent-Guided Co-Scientist for Side-Effect-Aware Drug Redesign](https://arxiv.org/abs/2607.02944)

**<font color=#1a73e8>作者：</font>** Yujin Kim, Charmgil Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose PRECEDE, a precedent-guided co-scientist for side-effect-aware drug redesign that revises a parent compound to mitigate a specified side effect while preserving therapeutic function. Rather than isolated molecular generation, PRECEDE frames redesign as evidence-grounded reasoning over drug--side-effect associations, biomedical knowledge graphs, and precedents of safety-driven optimization, coordinated by an LLM orchestrator with explicit policies and human-review checkpoints. We position PRECEDE as a human-supervised AI-for-science workflow in which hypotheses remain auditable, falsifiable, and bounded by prior pharmacology.

---


### 83. [Pooling-Based Context Modeling for Convolution-Free Deep Image Prior](https://arxiv.org/abs/2607.02952)

**<font color=#1a73e8>作者：</font>** Gihyun Kim, Jong-Seok Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional Neural Networks (CNNs) achieve strong denoising performance by exploiting spatial context from neighboring pixels. Deep Image Prior (DIP) leverages this property to restore images from a single noisy input without requiring large datasets. However, the over-parameterized architecture of DIP often leads to noise fitting during optimization. In this paper, we propose Pool-DIP, a convolution-free architecture that incorporates pooling-based contrast modeling to capture spatial context efficiently. Pool-DIP improves denoising performance while significantly reducing the number of parameters and computational complexity compared to convolution-based DIP models. Experimental results show that Pool-DIP achieves competitive performance across multiple datasets, including a real-world benchmark. Spectral analysis further reveals that Pool-DIP stabilizes the evolution of high-frequency components during optimization and suppresses erroneous high-frequency signals. The proposed architecture also generalizes well to other image restoration tasks such as super-resolution and inpainting.

---


### 84. [MORE: A Multilingual Document Parsing Benchmark and Evaluation](https://arxiv.org/abs/2607.02956)

**<font color=#1a73e8>作者：</font>** Long Xu, Binghong Wu, Tinghao Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multilingual documents encapsulate rich regional cultures, scientific discoveries, and historical records. Parsing this content into structured, machine-readable formats is critical for unlocking global knowledge. However, existing benchmarks predominantly focus on high-resource languages like English and Chinese, creating an evaluation blind spot concerning model performance on other languages. While recent Vision-Language Models (VLMs) claim support for hundreds of languages, the lack of ground truth makes it impossible to empirically verify these capabilities. To bridge this gap, we introduce MORE, a large-scale benchmark designed for multilingual document parsing evaluation. MORE distinguishes itself through three key dimensions: (1) Unprecedented Scale: It covers 149 languages, making it the most linguistically diverse benchmark to date; (2) Structural Complexity: Unlike previous works, it extends evaluation beyond plain text to include structural elements such as code blocks, tables, and catalogs; and (3) Data Authenticity: All samples are curated from real-world documents via a model-assisted, human-refined annotation pipeline. We evaluate state-of-the-art models using MORE, establishing new performance baselines for long-tail languages and validating the benchmark's effectiveness in diagnosing model capabilities in realistic, diverse scenarios. The MORE dataset will be available at this https URL.

---


### 85. [ReLo-IRR: Reflection-Guided LoRA Framework for Image Reflection Removal](https://arxiv.org/abs/2607.02957)

**<font color=#1a73e8>作者：</font>** Chaoqun Wang, Yuehuan Wei, Haoxiang Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image reflection removal (SIRR) aims to recover the clean transmission layer from a reflection-contaminated image. Although recent methods achieve promising results with large diffusion models, they rely on image-agnostic adaptation strategies, e.g., fine-tuning or ControlNet, that enforce uniform suppression regardless of reflection severity. As a result, heavy reflections often leave residuals, while weak ones suffer from detail loss. To this end, we propose ReLo-IRR, a reflection-guided LoRA framework built upon the rectified flow model. First, a lightweight estimator is designed to predict the reflection strength descriptor, providing an explicit prior of reflection dominance for each image and enabling image-dependent LoRA modulation. Second, we introduce a time-conditioned mechanism that fuses this reflection descriptor with timestep embeddings, enabling LoRA modulation to evolve consistently with the coarse-to-fine denoising process. By jointly modeling reflection strength and denoising dynamics, our ReLo-IRR achieves robust suppression of diverse reflection conditions. Extensive experiments on challenging benchmarks validate the effectiveness of ReLo-IRR, demonstrating superior dereflection performance and robust generalization. The code is released at this https URL.

---


### 86. [Parallelized Autoregressive Decoding for Omni-Modal Dense Video Captioning](https://arxiv.org/abs/2607.02963)

**<font color=#1a73e8>作者：</font>** Wenzheng Zeng, Siyi Jiao, Chen Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense video captioning aims to generate temporally grounded descriptions of video events, benefiting both event-level video understanding and generation. In this domain, autoregressive video large language models have emerged as a prevalent paradigm due to their strong generative and cross-modal modeling capacity. However, generating dense captions under the token-by-token paradigm severely limits inference efficiency and hinders scalability as video length and event density increase. In this work, we propose a parallelized autoregressive framework that not only improves generation efficiency but also enhances temporally grounded captioning performance. Our key insight is to exploit the weak local dependencies across temporally distinct events to restructure the causal dependency graph, thereby enabling lossless parallel generation. Specifically, tokens with weak cross-event dependencies can be decoded in parallel, while tightly coupled tokens within each event retain sequential decoding to preserve local semantic coherence. To realize this insight, we introduce two key components for lossless parallel decoding: (1) a latent global planning mechanism that automatically learns the event-level structure and produces compact tokens encoding global inter-event causality while adaptively aggregating event-level audio-visual semantics, guiding subsequent dependency restructuring and parallel decoding; and (2) an event-factorized parallel decoding mechanism that effectively balances local focus with global inter-event awareness. Experiments on various benchmarks demonstrate the clear advantage of our approach in both efficiency and performance in omni-modal event grounding and captioning. Project website: this https URL.

---


### 87. [Individual Parameters in Weight-Sparse Transformers Appear Interpretable](https://arxiv.org/abs/2607.02964)

**<font color=#1a73e8>作者：</font>** Arnau Marin-Llobet, Stefan Heimersheim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central goal of mechanistic interpretability is to understand how neural networks work and what each individual component does. Dominant circuit-finding approaches focus on a specific behavior and reverse-engineer the role of components on the associated sub-distribution. However, past work has shown that components can have different functions that are active on different subsets of the input distribution. In this work we ask whether a single weight can be understood globally across the full training distribution by characterizing when it matters (the inputs on which ablating it changes the model's predictions). We introduce an automated LLM pipeline that writes a short, human-readable description of when a weight matters and verifies it on held-out text, crediting a weight only if its description generalizes. Across two sparse and two dense transformers, the fraction of weights that are interpretable (in this sense) is higher in sparse transformers than in dense ones, a gap that widens once unreliable descriptions are discarded. Our results show that a meaningful fraction of a sparse transformer model's weights can be interpreted: 12 to 31% of weights have a single short description that identifies what the weight is used for.

---


### 88. [Rank-Order N-of-M Codes for Sparse Distributed Memory: Disentangling Representation and Learning Effects in Noise Robustness Against Contemporary Neuromorphic Architectures](https://arxiv.org/abs/2607.02967)

**<font color=#1a73e8>作者：</font>** Joy Bose  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models remain limited as continual learning systems, motivating renewed interest in Sparse Distributed Memory (SDM) as an explicit online episodic memory. CALM (Nechesov and Ruponen, 2025) identifies its threshold-binary encoder as an open design question. This paper evaluates rank-order N-of-M encoding (Furber et al., 2007) as an alternative. We make three contributions. First, a faithful reimplementation validates the published architecture by confirming exact equivalence between WheelSDM and RankOrderSDM (cosine similarity 1.0000 across 10 seeds) and reproducing the documented divergence of RDLIF neurons under interference. Second, multi-seed capacity experiments show RankOrderSDM outperforming StandardSDM by 13.4 percentage points at saturation in the scaled configuration and by 0.8 percentage points at the published architecture scale. Third, BER robustness experiments disentangle representation and learning effects, showing that the large robustness gain arises primarily from the interaction of rank-order encoding with MAX-Hebbian learning, while the encoder alone provides only a small advantage under matched learning conditions. Experiments on GloVe-100 embeddings confirm this small but consistent encoding benefit on real structured data, whereas sentence embeddings exhibit a ceiling effect at low memory load. A secondary analysis shows that idealized rank-order encoding requires half the component-level encoding energy of SpikingMamba's SI-LIF neurons at four-bit precision, although decoder costs dominate overall system energy. These results identify which components of the original rank-order SDM architecture provide measurable benefits for contemporary memory-augmented AI systems, offering practical guidance for architectures such as CALM.

---


### 89. [Awakening Diffusion Transformers: Eliciting Stronger Generation and Understanding via Massive Activation Modulation](https://arxiv.org/abs/2607.02968)

**<font color=#1a73e8>作者：</font>** Chaofan Gan, Zicheng Zhao, Yuanpeng Tu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Massive Activations (MAs) have been widely observed in Transformer-based models, yet their structure and functional roles in Diffusion Transformers (DiTs) remain insufficiently understood. In this work, we systematically analyze MAs in representative DiTs and find that they are spatially distributed across image tokens while concentrated in a small set of fixed feature dimensions. We further show that these dimensions are closely aligned with AdaLN residual scaling factors and are primarily modulated by the denoising timestep rather than text conditions. This structure leads to two task-dependent effects: for generation, MAs are critical for fine-grained detail synthesis while having limited influence on global semantics; for understanding, their shared high-magnitude directions make raw DiT features overly similar across spatial tokens and weaken dense feature discrimination. Based on these findings, we introduce Eliciting Massive Activation (EMA), a training-free framework that leverages Massive Activations (MAs) as a unified modulation signal to improve both generative and representational capabilities of DiTs. For generation, EMA proposes MA-driven Detail G}uidance (DG), which suppresses MA dimensions to construct a detail-deficient counterfactual prediction and guides sampling toward finer visual details. DG further supports efficient partial-forward inference, integration with classifier-free guidance, and token-level Local DG for refining selected image regions. For understanding, EMA introduces MA-modulated REPresentation extraction (MREP), which uses pretrained AdaLN channel-wise modulation to reduce MA directional dominance and concatenates spatially normalized MA maps to preserve useful spatial structure. Extensive experiments demonstrate that EMA consistently improves both the generation quality and representation capability of DiTs.

---


### 90. [Evaluating Generative Agents with Actions Grounded in Socially Distributed Task Environments using Incognita](https://arxiv.org/abs/2607.02975)

**<font color=#1a73e8>作者：</font>** Dan C. Hsu, Luke Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective agency in social environments depends on when an agent seeks knowledge, when it acts, and whether its actions are justified by acquired information. Existing grounded benchmarks provide executable actions, persistent state, and verifiable outcomes, while social simulation environments provide rich interaction among language agents. We study an evaluation setting that combines these requirements. We define socially distributed task environments as interactive environments where task-relevant knowledge is partitioned across role-isolated participants and consequential actions are accessible only through them. Communication serves as exploration over role-partitioned knowledge, while grounded action serves as exploitation over environment state. We introduce Incognita, a Concordia-based framework that separates social interaction from grounded execution. The evaluated agent routes messages to a user or specialist entities; specialists mediate admissible operations; a deterministic sub-environment executes accepted operations over a canonical state; and an offline evaluator scores outcomes with inherited rewards. Incognita-Retail transforms tau-bench retail into a multi-entity environment while preserving final-state reward semantics. We evaluate three generative agent models on 18 tasks stratified by social breadth, with 540 trials. Progress appears in reward and behavior: success rises from 0 percent to 8.9 percent and 17.2 percent, while premature finalization falls from 100 percent to 87 percent and 58 percent. Stronger models elicit more hidden knowledge, contact more entities, and attempt more grounded writes, yet reliability remains low. These findings show that socially distributed task environments expose behavior before reliable success, including knowledge elicitation, source selection, grounded action attempts, and premature completion belief.

---


### 91. [Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling](https://arxiv.org/abs/2607.02980)

**<font color=#1a73e8>作者：</font>** Xiang Hu, Xinyu Wei, Hao Gu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scaling modern large language models (LLMs) to long contexts is limited by the quadratic computation cost, and poor length extrapolation of dense attention. Chunk-wise sparse attention offers a promising alternative, but all existing methods fall short of full attention because of their inaccurate chunk selection. We propose Hierarchical Landmark Sparse (HiLS) Attention, a chunk-wise sparse attention mechanism that learns chunk selection end-to-end under the language-modeling (LM) loss. HiLS factorizes attention hierarchically: each query performs attention independently with each retrieved chunk to extract chunk-specific information, and the resulting outputs are fused according to chunk retrieval scores. By incorporating retrieval scores into the forward attention computation, HiLS optimizes them directly with the LM loss, enabling end-to-end retrieval learning and native sparse training. Experimental results show that HiLS-Attention achieves performance comparable to, and in some cases better than, full attention at in-domain context lengths. Meanwhile, HiLS-Attention extrapolates more than $64\times$ the training context length with 90% retrieval accuracy, far beyond full attention. Moreover, existing full-attention models can be converted to HiLS-Attention with lightweight continued pretraining, preserving in-domain performance while acquiring ultra-long-context extrapolation. Together with its sparse KV access and computation, HiLS-Attention breaks the usual efficiency-performance trade-off, enabling long-context LLMs that are both more efficient and more effective on general long-context tasks than their full-attention counterparts.

---


### 92. [Enhanced Feature Extraction for IoT Network Intrusion Detection Using GNNs and KAN](https://arxiv.org/abs/2607.02981)

**<font color=#1a73e8>作者：</font>** Long Zhao, Shixun Ji, Bin Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent advancements in the Internet of Things (IoT) emphasize the urgent need for advanced network security, as IoT networks feature dynamic topologies, imbalanced traffic, and complex attack patterns. Unlike general IT networks, IoT environments exhibit extreme heterogeneity and sparse topologies. Traditional GNN-based intrusion detection methods often struggle to efficiently model node and edge features or capture fine-grained anomalies in such settings. To address this, we propose SKGFusionKAN, a novel IoT-tailored approach enhancing GraphSAGE with a multi-scale selective kernel attention mechanism. This enables adaptive extraction of node and edge features under diverse traffic conditions. Specifically, our edge-oriented message passing strengthens information propagation, while selective kernel attention adaptively weights edge-derived information from different scales to handle heterogeneity. We also introduce a gated fusion process to dynamically integrate multi-scale features, improving robustness against evolving attacks. Finally, we leverage Kolmogorov-Arnold Networks (KAN) for classification, offering superior nonlinear modeling capabilities essential for detecting intricate, low-frequency attacks. To our knowledge, this work presents a comprehensive integration of GNNs and KAN with dedicated architectural innovations for IoT intrusion detection. Extensive experiments on four NIDS benchmarks show that SKGFusionKAN consistently outperforms state-of-the-art approaches in binary and multiclass tasks, demonstrating its potential for IoT security.

---


### 93. [RePos: Relative-to-Absolute Output Factorization for Cross-Environment WiFi-Based 3D Human Pose Estimation](https://arxiv.org/abs/2607.02986)

**<font color=#1a73e8>作者：</font>** Zhangcheng Hou, Tomoaki Ohtsuki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Device-free 3D human pose estimation using commodity WiFi Channel State Information (CSI) enables privacy-preserving and illumination-robust human sensing, but its deployment is limited by poor cross-environment generalization. Unlike images, CSI measurements do not have a spatially localized correspondence to body parts and are heavily affected by multipath propagation, causing models that regress absolute poses to entangle body structure with environment-specific location cues. Within a single environment this coupling is benign: an end-to-end absolute-pose variant, RePos-D, already achieves state-of-the-art accuracy on Person-in-WiFi-3D (86.9 mm MPJPE, a 3.4% gain over the previous best WiFi method, DT-Pose). Across environments, however, the same model overfits position and suffers significant performance degradation. We therefore propose RePos, a factorized framework that separates root-relative pose estimation from root localization. By preventing absolute-pose supervision from affecting the structure branch, RePos learns environment-invariant pose representations. Specifically, it groups CSI features into body-part-aware latent tokens that skeleton-guided modeling refines into the pose, while a separate amplitude-based network estimates the root position through a differentiable spatial-decomposition module. Under the strict MM-Fi cross-environment protocol, RePos achieves MPJPEs of 254.4-296.1 mm, a 10-21% reduction over existing WiFi-based methods. The improvement remains consistent across activity protocols, leave-one-environment-out splits, and leakage-free few-shot transfer. Analysis of the learned features shows that relative-pose representations remain largely position-agnostic, while root localization retains environment dependence, indicating distinct generalization behavior for structure and localization.

---


### 94. [Cross-device Collaborative Test-time Adaptation with Zeroth-order Optimization and Model Merging](https://arxiv.org/abs/2607.02988)

**<font color=#1a73e8>作者：</font>** Yu Mitsuzumi, Akisato Kimura, Yasuhiro Fujiwara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) mitigates domain shifts by using incoming test data to update a model on the fly. The majority of TTA methods require resource-intensive backpropagation (BP) for model updates, particularly demanding large memory sizes, which makes it infeasible to deploy them on resource-limited devices (e.g., edge devices). To address this issue, we integrate two different techniques, zeroth-order optimization (ZOO) and model merging, under the recently established cross-device collaborative TTA (CDC-TTA) framework, where the system is composed of a mixture of resource-abundant and resource-limited devices, and the model information (e.g., model weights obtained on each device) is shared across the devices. Our method is executable on resource-limited devices by introducing ZOO, which requires only forward processing and bypasses the resource-intensive BP optimization. Concurrently, to mitigate the high-dimensional optimization difficulty caused by the side effect of ZOO, we incorporate model merging of the shared multiple models and set the merge coefficients as the optimization objective, which successfully reduces the optimization dimension. In addition, to enhance the synergistic combination of ZOO and model merging, we propose a unique preprocessing strategy that trims intra-model non-influential weights and reduces the inter-model information redundancy. We empirically confirmed the effectiveness of our method using common corruption and style-transferred image benchmarks.

---


### 95. [MABLE: Masked Autoencoding with Bi-Lipschitz Decoding for Embeddings and Graph Metric Learning](https://arxiv.org/abs/2607.02990)

**<font color=#1a73e8>作者：</font>** Yaniv Shulman, Shaghayegh Akbarpour, Jack B. Muir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose MABLE (Masked Autoencoding with Bi-Lipschitz Decoding for Embeddings and Graph Metric Learning), a self-supervised framework for learning node and graph embeddings from large, heterogeneous graphs, demonstrated here on geospatial mineral-exploration data. MABLE combines masked reconstruction with fixed cosine-similarity losses that align matched augmented views while keeping unpaired embeddings well spread. A bi-Lipschitz feature decoder ties a low-dimensional reconstruction component of each node embedding to feature similarity, while matched-node consistency shapes the remaining context used by graph pooling. Lipschitz-controlled pooling helps stabilize graph-level representations under perturbations of retained node embeddings, while augmentation alignment trains robustness to masking, node dropping, and sampling variation. Across local copper and regional Arabian Shield studies, MABLE embeddings provide complementary downstream signal and produce coherent embedding-derived layers for hypothesis generation without learned discriminators or hard-negative selection.

---


### 96. [REAL-OW: Rehearsal-free Open World Object Detection with Low-Rank Adaptation and Dual-Stage Objectness Modeling](https://arxiv.org/abs/2607.03004)

**<font color=#1a73e8>作者：</font>** Huazhong Zhang, Xiaowen Fu, Yang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-World Object Detection (OWOD) requires detectors to identify previously unseen objects as unknown and incrementally incorporate them into the set of known categories, while preserving previously acquired knowledge. Existing frameworks rely heavily on exemplar replay to mitigate catastrophic forgetting, but in some real applications, storing raw data conflicts with data access restrictions and leads to data exposure risks, while incurring significant memory overhead. In this paper, we propose REAL-OW, a novel rehearsal-free framework that decouples incremental knowledge through a collaborative adapter architecture based on Low-Rank Adaptation (LoRA). Specifically, we deploy General Adapters (GAs) in the backbone to enable the significance-aware refinement of cross-task universal representations, while Specific Adapters (SAs) in the decoder provide orthogonal storage for task-specific expertise. To resolve representation drift in objectness modeling under rehearsal-free constraints, we introduce Dual-Stage Objectness Modeling (DSOM), which alternates between feature aggregation and boundary consolidation to stabilize objectness distributions while maintaining the separation between known and unknown categories. Furthermore, DSOM is supported by a Calibrated Gaussian Negative Log-Likelihood (CG-NLL) distance tailored for the dispersed feature distributions inherent in rehearsal-free settings. Extensive evaluations demonstrate that REAL-OW achieves state-of-the-art performance, surpassing existing exemplar replay methods in both detection precision and unknown discovery. Our approach establishes a new baseline for rehearsal-free OWOD.

---


### 97. [Transfer Learning in High-dimensional Ising Models](https://arxiv.org/abs/2607.03005)

**<font color=#1a73e8>作者：</font>** Joonho Kim, Seyoung Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In high-dimensional Ising model estimation, target sample sizes are often limited, and effectively using auxiliary binary datasets of unknown relevance remains challenging. To address this, we propose Trans-Ising, a transfer learning method that combines a loss-based source screening rule with a two-stage estimation procedure. The method first identifies informative auxiliary sources using held-out target pseudolikelihood to prevent negative transfer. It then computes an initial estimator via pooled nodewise $\ell_1$-regularized logistic regression, followed by a target-only correction step using a folded-concave penalty. Theoretically, we establish fixed-node $\ell_2$ and $\ell_1$ error bounds, exact graph selection consistency, and the conditional consistency of the screening rule. Through extensive simulations and real-data analyses, we demonstrate that Trans-Ising achieves lower estimation errors than both target-only estimation and naive data pooling.

---


### 98. [PosterHarness: Turning Scientific Poster Generation into an Auditable Instruction-Following Benchmark](https://arxiv.org/abs/2607.03006)

**<font color=#1a73e8>作者：</font>** Tianyi Yang, Dawei Fu, Youpeng Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-rich image models can now design poster-scale layouts, but we lack ways to measure whether they honor scientific communication contracts: legible labels, prescribed aspect ratios, and -- above all -- abstaining from fabricated scientific figures. We present POSTERHARNESS, an auditable harness reframing poster generation as measurable instruction-following tasks, with a pilot benchmark and failure taxonomy. POSTERHARNESS uses a placeholder-first contract to separate two jobs models otherwise conflate. The model performs visual-summary design: typography, reading path, color, and background -- but never draws data-bearing figures. Every figure region must be an empty labeled placeholder; a deterministic compositor inserts real source-paper figures at detected coordinates. This makes properties measurable: placeholder count and ID accuracy, blankness, aspect-ratio compliance, abstention from synthesized graphics, public-text hygiene, and source-figure provenance -- with failures logged as explicit rejections, not hidden in plausible-looking output. We instantiate the harness on 12 papers (6 HEP, 6 AI/ML-adjacent) and report three findings. (i) A counterfactual probe shows the placeholder contract drives VLM-counted synthesized figures from 34 to 0 across three papers. (ii) A failure taxonomy identifies blocking contracts: placeholder geometry, placeholder QA, template critic, and public text. (iii) Comparison with Paper2Poster shows a trade-off: PosterHarness yields higher-resolution artifacts, lower white-canvas fraction, and stronger VLM visual preference; the deterministic baseline retains slightly more PosterQuiz-style information and runs faster. We report this as regime characterization, not a superiority claim. All artifacts, prompts, manifests, and audit scripts are released as a reusable evaluation component.

---


### 99. [Can Model Merging Improve Aggregation in DiLoCo?](https://arxiv.org/abs/2607.03011)

**<font color=#1a73e8>作者：</font>** Stefan Horoi, Benjamin Thérien, Guy Wolf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging techniques, which aggregate independently finetuned models into one to combine their capabilities, have become a topic of significant interest in recent years, with a broad array of methods having been proposed to tackle this problem. Simultaneously, an emerging trend in distributed learning has been the use of methods such as local SGD and DiLoCo, which greatly reduce communication costs by periodically aggregating the independently trained local models. However, these communication-efficient methods have been shown to degrade in performance relative to the FLOP-matched data-parallel gold standard as the number of independent local models grows and as the number of local training steps before global communication is increased. In this work, we draw an explicit analogy between the pseudo-gradient aggregation step in local SGD/DiLoCo and task arithmetic-based model merging, establishing a straightforward way to utilize merging methods in the context of distributed optimization. We then evaluate multiple state-of-the-art model merging methods in this setting and identify one method in particular, Iso-C, as a promising approach for improving DiLoCo. We find that DiLoCo SGD with Iso-C aggregation outperforms not only simple pseudo-gradient averaging but even the momentum-based DiLoCo, despite lacking a momentum mechanism itself. Building on this finding, we propose IsoLoCo, which adapts Iso-C for distributed training by equipping it with Nesterov momentum. Our empirical evaluations on language model pre-training across varying numbers of local workers show that IsoLoCo significantly outperforms DiLoCo, with the gap between them widening as the number of workers increases. This advantage remains present across model sizes and inner step counts, confirming that merging-inspired aggregation is an effective strategy for low-communication distributed training.

---


### 100. [HyperVAttention: Efficient Sparse Attention with Spatio-Temporal Clustering for Video Diffusion](https://arxiv.org/abs/2607.03012)

**<font color=#1a73e8>作者：</font>** Dongyeun Lee, Amir Zandieh, Vahab Mirrokni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Diffusion Transformers (VDiTs) have demonstrated significant capabilities in high-fidelity video generation. However, their ability to produce long-duration videos is fundamentally constrained by the quadratic complexity of the self-attention mechanism. Recent clustering-based sparse attention methods improve the quality-speed trade-off by grouping semantically similar tokens, but their practical efficiency remains limited by two bottlenecks: substantial clustering overhead and low CTA utilization caused by irregular cluster-induced blocks. We propose HyperVAttention (HVA), a training-free sparse attention framework that addresses both bottlenecks jointly. To reduce clustering overhead, we introduce 3D local-window clustering, which exploits the spatio-temporal locality of video tokens to restrict centroid search to fixed local neighborhoods, and implement it with a custom Triton kernel for efficient execution. We further propose a hybrid clustering strategy that performs full clustering only at anchor steps and updates only subset tokens at intermediate steps, leveraging the temporal stability of cluster assignments across denoising steps. To improve CTA utilization, we present hardware-aware cluster merging that minimizes CTA-aligned execution cost through parallel agglomerative merging, improving block density and approximation fidelity by utilizing idle tile capacity. Together, these components reduce clustering overhead, avoid redundant updates, and better align sparse attention with the fixed tile structure of modern GPU kernels. Experiments on Text-to-Video generation show that HVA establishes a new Pareto frontier for training-free sparse attention in video diffusion, reducing end-to-end latency by up to $2.13\times$ while improving fidelity over existing training-free sparse attention baselines.

---


> [!TIP]
> 当前位于：**51-100**（第 2/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
