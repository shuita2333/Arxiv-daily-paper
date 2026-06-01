# 📦 其他研究 | 2026年06月02日

> 本类共 **317** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-317](./part-07.md)

---

### 251. [Generalized Intention Modeling in Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.31318)

**<font color=#1a73e8>作者：</font>** Mateusz Odrowaz-Sypniewski, Jasmine Bayrooti, Ajay Shankar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling an opponent's intent is critical for effective decision-making in non-cooperative, competitive, and general-sum multi-agent reinforcement learning. Existing opponent modeling methods encode intent using an embedding derived from episode information chosen a priori, such as the opponent's next action or a future environment state, and use this to guide the ego-agent's behavior. These approaches assume that the chosen information is universally representative of intent; however, we show empirically that this is not the case as intentions are often task- and environment-dependent. To address this, we introduce a task-adaptive opponent modeling framework that learns a performance-driven mixture of multiple intent representations. We further introduce a new intention representation that maximizes mutual information with the ego-agent's future returns, thereby capturing opponent information that is most directly relevant to performance. Our approach consistently matches or exceeds the performance of state-of-the-art baselines across diverse tasks and yields insights into when and why different opponent modeling strategies succeed.

---


### 252. [Inconsistency-Aware Minimization: Improving Generalization with Unlabeled Data](https://arxiv.org/abs/2605.31324)

**<font color=#1a73e8>作者：</font>** Hee-Sung Kim, Hyeonseong Kim, Sungyoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating the generalization gap and developing optimization methods that improve generalization are crucial for deep learning models, for both theoretical understanding and practical applications. Leveraging unlabeled data for these purposes offers significant advantages in real-world scenarios. This paper introduces a novel generalization measure, local inconsistency, derived from an information-geometric perspective on the parameter space of neural networks. A key feature of local inconsistency is that it can be computed without explicit labels. We establish theoretical underpinnings by connecting local inconsistency to the Fisher information matrix and the loss Hessian. Empirically, we demonstrate that local inconsistency correlates with the generalization gap. Based on these findings, we propose Inconsistency-Aware Minimization (IAM), which incorporates local inconsistency into the training objective. We demonstrate that in standard supervised learning settings, IAM enhances generalization, achieving performance comparable to that of existing methods such as Sharpness-Aware Minimization. Furthermore, IAM exhibits efficacy in semi- and self-supervised learning scenarios, where the local inconsistency is computed from unlabeled data.

---


### 253. [MeshGuard: MUD-Based Network Access Control for Large-Scale Thread-Powered IoT Networks](https://arxiv.org/abs/2605.31326)

**<font color=#1a73e8>作者：</font>** Dominik Roy George, Wouter van Hoof, Habib Mostafaei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The IETF standard Manufacturer Usage Description (MUD) enables manufacturers to equip IoT devices with certified URLs that provide traffic profiles for those devices, helping administrators enforce network access control. However, MUD assumes devices operate on full IP stacks and therefore does not account for constrained IoT devices running Thread--the dominant low-power mesh networking standard--which lacks complete TCP/IP functionality. While prior work proposes extensions to support MUD in Thread environments, these approaches are limited to simple topologies with a single border router and do not scale to realistic deployments with multiple, heterogeneous border routers. We introduce MeshGuard, a framework enabling MUD-based access control in complex Thread networks, with any number of border routers. MeshGuard extends the Mesh Link Establishment (MLE) protocol to deliver MUD information from constrained devices to border routers regardless of network topology. Moreover, MeshGuard leverages Software-Defined Networking (SDN) to synchronize access control lists across all routers. Experiments on our proof-of-concept with real devices (nRF5340, nRF52833, Raspberry-Pi 3) demonstrate enhanced security, minimal overhead, and linear scalability compared to state-of-the-art approaches.

---


### 254. [A Focus of Attention-Based Virtual Training Platform for Pre-Prosthetic Myoelectric Skill Acquisition: A Proof-of-Concept Study](https://arxiv.org/abs/2605.31332)

**<font color=#1a73e8>作者：</font>** Xiaochen Zhang, Sigrid Dupan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Advances in myoelectric prosthetic technology have substantially increased the functional potential of modern devices. Accordingly, heightened control demands have led to the acknowledgement of pre-prosthetic training as a key stage in the acquisition of myoelectric skills. Existing training paradigms largely emphasize internal muscle activation while external, goal-directed outcomes required for effective real-world use are often neglected. We address this gap by introducing a virtual pre-prosthetic training platform that integrates EMG-driven cursor with animated hand gestures, enabling the delivery of both muscle-level and functional-level feedback. In this proof-of-concept study, participants were assigned to one of two focus of attention (FoA) protocols, each incorporating both feedback types but differing in whether internal or external FoA was emphasised. Participants successfully acquired and retained myoelectric skill across both protocols, but distinct performance characteristics and learning strategies emerged, indicating that both FoAs contribute meaningfully to learning and that their timing may play an important role. External FoA was positively associated with retention, suggesting that it may strengthen the link between training and skill acquisition. Together, the results demonstrate the feasibility of an FoA-based virtual training platform for pre-prosthetic applications and indicate that it can provide a foundation for designing training protocols that better prepare users for prosthetic use.

---


### 255. [DecMem: Towards Minute-Long Consistent World Generation with Decoupled Memory](https://arxiv.org/abs/2605.31336)

**<font color=#1a73e8>作者：</font>** Zhenhao Yang, Xiaoshi Wu, Zhengyao Lv 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generative models have promoted rapid progress in controllable world models. However, maintaining fine-grained spatio-temporal consistency under long-horizon reasoning remains a key challenge. In this work, we move beyond explicit 3D memory and coarse frame-level implicit modeling, and propose a fine-grained, learnable, and scalable memory for consistent world generation. We first identify two fundamental limitations of naïve learnable memory architectures in long-horizon extrapolation, namely computational inefficiency and attention dispersion. Through a systematic analysis of attention dispersion, we propose DecMem, a decoupled memory architecture that employs Sparse Global Memory for efficient fine-grained access to global history and Anchored Local Memory for stable and high-quality extrapolation. Extensive experiments demonstrate that DecMem significantly outperforms current state-of-the-art methods. By ensuring precise and efficient long-term memory and achieving superior extrapolation capabilities, DecMem enables minute-level controllable long video generation with high fidelity and consistency.

---


### 256. [Bundesrecht: An Open Library and Corpus for German Statutory Reference Processing](https://arxiv.org/abs/2605.31338)

**<font color=#1a73e8>作者：</font>** Harshil Darji, Martin Heckelmann, Christina Kratsch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Statutory references are central to legal language understanding, but are difficult to process automatically, as they appear in compact and variable surface forms, may combine multiple targets, use special abbreviations, and often point to lower-level units. Existing tools for German focus either on parsing references from legal documents or accessing statutory text once citations are explicit. This paper introduces bundesrecht, an open resource for German statutory reference processing, consisting of a software library and a structured corpus of German federal law. The library parses, normalizes, and resolves German statutory references, mapping raw citation strings to structured objects, expanding compact references into canonical forms, and linking them to statutory provisions. The accompanying dataset preserves the internal hierarchy of statutes from laws to fine-granular subclauses. We evaluate the parser and normalizer on 2,944 annotated German legal references using strict exact-match and micro information extraction metrics. We further evaluate canonical reference deduplication and show that normalized references group real citation surface variants far more reliably than string matching. bundesrecht is the first open resource that covers German statutory reference processing as an end-to-end pipeline, from raw citation string to resolved statutory provision, and is available on PyPI.

---


### 257. [Appropriateness of Empathy in AI: A Signal-Cost Perspective](https://arxiv.org/abs/2605.31340)

**<font color=#1a73e8>作者：</font>** Chi-Ching Juan, Tao Wang, Harold Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The appropriateness of empathy in AI has emerged as a critical concern, as excessive empathy risks seeming manipulative while insufficient empathy appears dismissive. While prior research has explored how to quantify empathy in AI, few studies examine whether such empathy is contextually appropriate. This paper introduces an economic perspective by applying signaling theory to human-AI conversations. We propose Signal Cost Proxies (emotional richness, perspective-taking, and contextual tailoring) mapped to affective, cognitive, and associative empathy. This multidimensional framework enables systematic evaluation of empathy not just by presence, but by its appropriateness relative to user demand.

---


### 258. [A Visually Impaired Assistance Benchmark for VLM-as-a-Judge Evaluation](https://arxiv.org/abs/2605.31351)

**<font color=#1a73e8>作者：</font>** Yi Zhao, Siqi Wang, Zhe Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-based Visually Impaired Assistance (VIA) remains challenging, largely due to the high cost of human evaluation. The VLM-as-a-Judge paradigm may offer a promising alternative, although it has mostly been studied in general domains. We therefore ask whether such judges can be trusted for VIA tasks. To investigate this question, we introduce VIABLE (Visually Impaired Assistance Benchmark for VLM-as-a-Judge Evaluation), the first benchmark for VLM-as-a-Judge evaluation in VIA. VIABLE contains over 300K judgment samples across three scenarios and introduces an Effectiveness--Impartiality--Stability framework with a 12-mode failure taxonomy. Based on VIABLE, our systematic study of seven judges across different model scales shows that existing models are largely unreliable across all evaluation axes. The strongest judge, GPT-5.4, achieves only 52.6% single-failure diagnostic accuracy, yet exhibits the highest self-preference rate at 94.2%; while open-source judges are strongly biased and adversarially fragile. To address these issues, we propose VIA-Judge-Agent, a model-agnostic inference-time harness that augments judges with visual evidence extraction and a taxonomy-guided workflow. It enables positive improvements in diagnostic accuracy and downstream VIA responses more preferred by BLV users. Data and code are available at: this https URL

---


### 259. [Diagnosing Failure Modes of Shared-State Collaboration in Resource-Constrained Visual Agents](https://arxiv.org/abs/2605.31354)

**<font color=#1a73e8>作者：</font>** Yunpeng Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modular visual reasoning systems increasingly rely on shared working memory for multi-step collaboration, yet the failure dynamics of intermediate state evolution in low-capacity regimes remain underexplored. We study failure modes of collaborative reasoning with weak learners (4B--8B models) through the lens of noise accumulation. We introduce CoSee, an auditing framework that formalizes the read-write-verify loop to trace information flow in document visual question answering. Across multi-page, chart, and web-based benchmarks, we find a counter-intuitive degradation: naive shared workspaces often amplify hallucinations rather than resolve them. We identify two dominant failure modes: Noise Reinforcement, where ungrounded notes are reused as evidence, and Policy Collapse, where added context shifts the model toward under-specified, short-form answers. Using cost-accuracy Pareto frontiers, we show that increased compute can correlate negatively with performance without explicit verification. Our findings suggest that for resource-constrained agents, the bottleneck lies not in reasoning depth but in communication fidelity, providing trace-level diagnostics and a mechanistic baseline for reliable modular design.

---


### 260. [dashi: A Python library for Dataset Shift Characterization to Support Trustworthy AI Development and Deployment](https://arxiv.org/abs/2605.31360)

**<font color=#1a73e8>作者：</font>** David Fernández-Narro, Pablo Ferri, Ángel Sánchez-García 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Artificial Intelligence (AI) life cycle requires a thorough understanding of the underlying data dynamics for robust, safe and cost-effective AI development and use. Dataset shifts are defined as changes between train and test data distributions. Whether occurring over time (temporal) or across different sites (multi-source), they can severely degrade model performance and compromise data quality. This is particularly important in health AI, where the safety and fundamental rights of patients can be severely affected by uncontrolled shifts both at training and operational stages. While the theoretical foundations of covariate, prior, and concept shifts are well established, there is a lack of accessible and comprehensive software tools to perform their analysis. We introduce dashi, an open-source Python library designed for the exploration, quantification, and characterization of dataset shifts. dashi provides a dual approach: an unsupervised approach that leverages information geometry and non-parametric statistical manifolds to data variability characterization and analysis (e.g., Information Geometric Temporal plots and Multi-Source Variability metrics like Global Probabilistic Deviation and Source Probabilistic Outlyingness), and a supervised approach that quantifies and characterizes model performance degradation. Both unsupervised and supervised approaches work across user-defined temporal and domain/source batches. We demonstrate the utility of dashi on three simulated and real-world health AI case studies on gestational diabetes mellitus, COVID-19 and emergency medical dispatch. By providing interactive visual analytics and variability metrics, dashi supports trustworthiness of AI life cycle stages enabling robust and safe machine learning pipelines through the assessment of data coherence and AI performance.

---


### 261. [Trading Complexity for Expressivity Through Structured Generalized Linear Token Mixing](https://arxiv.org/abs/2605.31367)

**<font color=#1a73e8>作者：</font>** Erwan Fagnou, Paul Caillon, Blaise Delattre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Token mixing layers play a key role in how language models can learn and generate long-range dependencies. Their efficiency relies on the necessary trade-off between decoding speed and the memory requirements, along with the cache size. Considering causal generation, this paper explores new trade-offs thanks to a unified framework which separates two crucial features: (i) the direct influence of inputs on outputs in one generation step; (ii) the recurrent propagation of information through past outputs. This framework encompasses major architectures such as attention and state-space models, but also generalizes the recurrence equations by allowing each state to depend on multiple past states rather than only the immediate predecessor. By introducing structure, we design new recurrence patterns that provably achieve the desired complexity, while providing theoretical insights on their expressivity -- trading runtime for expressivity in a principled way. Empirical validation is performed on synthetic tasks, along with language modeling. Together, these results provide a unified toolkit for the understanding and design of efficient and expressive token mixers across model families.

---


### 262. [A Unifying View of Variational Generative Wasserstein Flows](https://arxiv.org/abs/2605.31369)

**<font color=#1a73e8>作者：</font>** Paul Caucheteux, Clément Bonet, Anna Korba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many modern generative models can be viewed as minimizing divergences between probability distributions, yet they rely on different algorithmic and geometric principles. Wasserstein gradient flows provide a continuous-time formulation for optimizing over distributions, and can be approximated through their implicit discretization via the Jordan-Kinderlehrer-Otto (JKO) scheme. In this work, we present a unified theoretical framework for generative modeling based on Wasserstein gradient flows, which we refer to as Generative Wasserstein Flows (GWF). We show that a broad class of existing methods can be derived as instances of parametric JKO schemes for $f$-divergence objectives, and we establish equivalences between several recently proposed algorithms. We extend this framework beyond f-divergence to Integral Probability Metrics and squared Maximum Mean Discrepancy, deriving new JKO-based generative algorithms, and clarifying their connections with GANs. We study empirically the impact of the JKO regularization for a wide set of objectives. Finally, we analyze parametric Wasserstein flows, where the dynamics are restricted to distributions induced by parametrized maps.

---


### 263. [Softsign: Smooth Sign in Your Optimizer For Better Parameter Heterogeneity Handling](https://arxiv.org/abs/2605.31371)

**<font color=#1a73e8>作者：</font>** Dmitrii Feoktistov, Timofey Belinsky, Andrey Veprikov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sign-based and LMO-inspired optimizers have recently attracted substantial attention in deep learning due to their strong performance and low memory footprint. However, their fixed-magnitude updates can hurt terminal convergence: they decouple update mechanisms from gradient magnitudes and fail to account for parameter heterogeneity, often leading to oscillation rather than convergence. We propose SoftSignum, a smooth relaxation of sign-based optimization that replaces the hard sign map with a temperature-controlled soft-sign transformation, enabling a parameter-wise transition from sign-like updates to magnitude-sensitive SGD-like steps. We complement it with an adaptive quantile-based temperature schedule and extend the same principle to matrix-valued optimizers, obtaining SoftMuon. We also develop a generalized geometry-relaxation framework based on strongly convex regularizers and Fenchel conjugates, proving convergence in stochastic non-convex setting. Experiments on diverse deep learning tasks, including LLM pretraining, show that SoftSignum and SoftMuon consistently improve over their hard sign-based counterparts and standard AdamW.

---


### 264. [Scaling Higher-Order Graph Learning with Maximal Clique Complexes](https://arxiv.org/abs/2605.31373)

**<font color=#1a73e8>作者：</font>** Antoine Vialle, Aref Einizade, Fragkiskos D. Malliaros 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) are limited to modeling pairwise interactions, while higher-order models based on cell complexes achieve greater expressivity but often suffer from poor scalability. We introduce simplified and factored cellular Weisfeiler Leman tests (sCWL and fCWL), which preserve the expressivity of the CWL test while improving computational efficiency. We further introduce the maximal clique complex, enabling scalable CWNs with reduced time and memory complexity while retaining strong empirical performance. To avoid explicit clique enumeration, we propose CliqueWalk, a biased random walk that samples maximal cliques and scales linearly with graph size. These contributions yield a scalable topological learning framework for higher-order graph representation.

---


### 265. [Toward Accessible Mobile Money: A Voice-Driven, Biometrically Secured USSD Automation Framework for Visually Impaired Users](https://arxiv.org/abs/2605.31375)

**<font color=#1a73e8>作者：</font>** Sunday Ajayi, Babatunde Eric Olatunji, Eric Umuhoza  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Financial inclusion has expanded significantly across Africa through mobile money services delivered primarily via USSD technology. However, visually impaired individuals continue to face accessibility and security barriers when conducting financial transactions. Current USSD systems are not designed for non-visual interaction, forcing users to rely on third-party assistance even for PIN entry, thereby increasing fraud exposure and reducing transaction confidence. Although alternative assistive technologies such as screen readers exist, they are not compatible with USSD operations, often causing sessions to time out before the user can complete a transaction. This paper presents an Android-based intelligent middleware that automates USSD transactions, integrates biometric-secured PIN injection, and introduces a privacy-preserving screen-dimming mechanism: Blackout Mode. The system leverages Android Accessibility Services, hardware-backed Keystore security, and on-device natural language parsing to enable independent, secure voice-based mobile money access. We show that the proposed solution improves task success rates from 65-75% to more than 90% and reduces transaction completion time from 40-60 seconds to 12-15 seconds, while also improving perceived security.

---


### 266. [Multi-Turn Multi-Agent Dialogue for Collaborative Reconstruction Improves VLM Performance on Spatial Reasoning, But Only Barely](https://arxiv.org/abs/2605.31387)

**<font color=#1a73e8>作者：</font>** Chalamalasetti Kranti, Sherzod Hakimov, David Schlangen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Robots operating in diverse environments rely on visual input to interpret objects and spatial layouts. In human-collaborative tasks, they are expected to communicate this understanding through language. Vision-language models (VLMs) support robotic tasks involving visual interpretation, question answering, and instruction following, but their capabilities in collaborative dialogue tasks requiring spatial reasoning remain underexplored. We study this gap through a collaborative structure-building task that combines visual interpretation, grounding, language-guided interaction, and action generation. We develop a framework in which VLMs use dialogue to reconstruct a target structure from visual and textual inputs. We evaluate open-weight and closed VLMs across interaction settings, input modalities, and image representations. Results show that spatial reasoning over visual representations remains difficult for the evaluated VLMs. Detailed text representations of the target yield higher reconstruction success across modality conditions, while decomposed image representations improve performance. These findings reveal limits in visual spatial grounding and grounded instruction generation for collaborative VLM agents.

---


### 267. [Constrained Multi-Objective Reinforcement Learning with Max-Min Criterion](https://arxiv.org/abs/2605.31388)

**<font color=#1a73e8>作者：</font>** Giseung Park, Hyunyoung Nam, Woohyeon Byeon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-Objective Reinforcement Learning (MORL) extends standard RL by optimizing policies with respect to multiple, often conflicting, objectives. While max-min MORL has emerged as an effective approach for promoting fairness, its applicability remains limited, particularly when constraints must be incorporated. In this paper, we propose a MORL framework that integrates the max-min criterion with explicit constraint satisfaction. We establish a theoretical foundation for the proposed framework and validate the resulting algorithm through convergence analysis and experiments in tabular settings. We further demonstrate the practical relevance of our approach in simulated building thermal control, multi-objective locomotion control, and greenhouse-gas-emission-aware traffic management. Across these domains, our method effectively balances fairness and constraint satisfaction in multi-objective decision-making.

---


### 268. [FSM-Net: An Efficient Frequency-Spatial Network for Real-World Deblurring](https://arxiv.org/abs/2605.31400)

**<font color=#1a73e8>作者：</font>** Vinh-Thuan Ly  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image deblurring demands both high-fidelity restoration and computational efficiency, a balance existing methods often struggle to achieve. In this paper, we propose FSM-Net (Frequency-Spatial Multi-branch Network), a highly efficient solution that secured 2nd place in the NTIRE 2026 Challenge on Efficient Real-World Deblurring. FSM-Net pioneers a dual-domain approach: a novel Frequency Attention module explicitly recovers high-frequency structural details via FFT, while a Cross-Gated Vision E-Branchformer at the bottleneck captures global dependencies with linear complexity. To ensure robust convergence, we employ a progressive curriculum training strategy guided by a composite loss function (Multi-Scale Charbonnier, Structural Edge, and Frequency). Evaluated on the RSBlur benchmark, FSM-Net achieves an outstanding 33.144 dB PSNR with only 4.94M parameters and 159.35 GMACs (at 1920x1200 resolution). By effectively pushing the Pareto frontier of efficiency and quality, FSM-Net establishes a strong baseline for resource-constrained image restoration.

---


### 269. [Skill Availability and Presentation Granularity in Large-Language-Model Agents: A Controlled SkillsBench Study](https://arxiv.org/abs/2605.31408)

**<font color=#1a73e8>作者：</font>** Xiaonan Xu, Wenjing Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skill documents provide procedural knowledge to large-language-model agents at inference time. This article studies whether the presentation granularity of controlled skill knowledge changes downstream task success. The experiment uses a pinned SkillsBench version, a 30-task domain-balanced subset validated by official oracle runs, two reasoning-enabled model configurations, six skill conditions, and five trials per task-condition-model cell. Skill availability is the clearest empirical signal. Relative to no skill, skill conditions increase task-mean pass rate by 26.7 to 36.0 percentage points for GPT-5.5 and by 18.0 to 26.0 percentage points for DeepSeek V4-Flash. The final data contain 1,800 rows, with 900 rows for each model. The task is the inference unit. Five trials are aggregated within each task-condition-model cell before paired contrasts are estimated over 30 tasks. The primary presentation contrasts are smaller and uncertain. Low-abstraction guidance differs from high-abstraction guidance by +0.7 percentage points for GPT-5.5 and -6.7 percentage points for DeepSeek V4-Flash, with both 95% bootstrap confidence intervals crossing zero. Adding one worked example to medium-abstraction guidance differs from the no-example variant by +0.7 and +1.3 percentage points. Mean-reward robustness checks preserve the same substantive conclusion. In this controlled subset, skill availability is associated with higher success than no skill, while the tested presentation-granularity changes yield small, uncertain, and model-dependent effects.

---


### 270. [Triangle Splatting SLAM](https://arxiv.org/abs/2605.31419)

**<font color=#1a73e8>作者：</font>** Nicholas Fry, Eric Dexheimer, Kirill Mazur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a dense RGB-D SLAM system using differentiable triangles as the 3D map representation. While 3D Gaussian Splatting has emerged as the leading method for novel-view synthesis, triangles remain the standard primitive for traditional rendering hardware, game engines, and downstream tasks requiring explicit geometry such as simulation, collision, and editing. Recent offline methods have demonstrated that an unstructured 'triangle soup' can be optimised into a photorealistic mesh via Delaunay triangulation across a set of posed images. Building upon this insight, we present the first dense SLAM system to employ Triangle Splatting to perform both tracking and mapping through online differentiable rendering of a triangle soup. The map can be converted into a connected mesh on-the-fly via restricted Delaunay triangulation, enabling new online capabilities such as mesh deformation and collision checking. On Replica and TUM-RGBD, our system outperforms baselines on 3D geometry, matches the camera-tracking accuracy, and enables online mesh-based scene editing.

---


### 271. [Neuro-symbolic Syntactic Parsing: Shaping a Neural Network with the CYK Algorithm](https://arxiv.org/abs/2605.31421)

**<font color=#1a73e8>作者：</font>** Fabio Massimo Zanzotto, Federico Ranaldi, Giorgio Satta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we show the possibility of a direct injection of algorithms into neural network architecture. We focus on a complex algorithm, that is, Cocke-Youger-Kasami (CYK) for parsing context-free grammars in Chomsky Normal Form and we propose CYKNN, a simple recurrent neural network architecture for encoding the CYK algorithm in trainable matrix-vector this http URL experimented with a very simple grammar with 4 variations showing that our approach outperforms existing LLMs with more than 20B parameters with an in-context learning setting and smaller LLMs of the Qwen family fine-tuned with LoRA. Our attempt paves the way to a different approach to neuro-symbolic methodologies.

---


### 272. [Fixed Universal Transformers](https://arxiv.org/abs/2605.31423)

**<font color=#1a73e8>作者：</font>** Jingwen Liu, Alexandr Andoni, Daniel Hsu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce \emph{universal transformers}: fixed transformers that can simulate any transformer in a given class via a suitable input embedding. Analogous to a universal Turing machine, the input embedding encodes a description of the target model while all internal parameters remain fixed. We provide explicit sparse constructions achieving universality when the embedding dimension is sufficiently large, and further show that universality is generic: randomly initialized transformers are universal almost surely, which aligns with recent empirical results of Zhong and Andreas (2024). We empirically validate our theory on the algorithmic tasks of parenthesis balancing and multi-hop reasoning. Our results suggest that much of a transformer's expressive power may reside in its input representation rather than its learned weights.

---


### 273. [DG-CoLearn: An Efficient Collaborative Learning Framework for Dynamic Graphs](https://arxiv.org/abs/2605.31427)

**<font color=#1a73e8>作者：</font>** Ashley Hoi-Ting Au, Zikun Zhang, Ligang He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic graph learning (DGL) is essential for modelling evolving graph data, but existing methods suffer from significant computational overhead due to repeated full-snapshot retraining and are not well-suited for collaborative settings with partitioned data. In realistic graph systems, cross-partition edges are unavoidable, but direct sharing of graph structure between clients may violate privacy constraints. We propose DG-CoLearn, a client-oblivious collaborative dynamic graph learning framework built on incremental graph snapshot processing, which focuses computation on graph regions affected by temporal updates while preserving historical information through temporal modelling. This incremental design is consistently applied across the entire graph processing pipeline, including a server-mediated embedding exchange mechanism to enable accurate multi-hop message passing without exposing raw cross-client structural information. Extensive experiments demonstrate that DG-CoLearn achieves up to 33.8$\times$ speedup in training time and 27.4$\times$ reduction in communication overhead, while consistently improving predictive performance on both node classification (up to 13.36% F1 improvement) and link prediction (up to 8.27% MAP improvement) tasks. These results highlight the effectiveness of DG-CoLearn in bridging efficiency, scalability, and client-to-client structural privacy in collaborative dynamic graph learning.

---


### 274. [SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks](https://arxiv.org/abs/2605.31433)

**<font color=#1a73e8>作者：</font>** Wai-Chung Kwan, Aryo Pradipta Gema, Joshua Ong Jun Leang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-play can train language models without external supervision. However, existing methods require rule-checkable answers, leaving open-ended tasks dependent on curated prompts or frontier-model judges. We introduce SCOPE, a data-free self-play framework for open-ended tasks that co-evolves two policies: a Challenger that generates document-grounded tasks, and a Solver that answers them through multi-turn retrieval. A frozen copy of the initial model serves as the self-judge, which writes task-specific rubrics from the source document and grades Solver responses against them. Across three 7-8B instruction-tuned models (Qwen2.5, Qwen3, OLMo-3), SCOPE improves open-ended performance by up to +10.4 points on eight benchmarks and matches or exceeds GRPO_data trained on ~9K curated prompts. Although trained only on open-ended tasks, SCOPE also improves held-out short-form QA by up to +13.8 points on seven held-out benchmarks, surpassing GRPO_data on all three models. Ablations show that co-evolving the Challenger is necessary to keep tasks near the Solver's frontier, that gains arise from improvements in both retrieval and synthesis with the relative contribution varying by task, and that rubric generation quality is the bottleneck for self-judging.

---


### 275. [Flow map learning in nonlinear vector autoregressive models: influence of the feature-library structure on the training error](https://arxiv.org/abs/2605.31438)

**<font color=#1a73e8>作者：</font>** Markus Gross  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting often requires learning nonlinear and time-delayed dependencies. A paradigmatic class of forecasting models are nonlinear vector autoregressive processes (NVAR), also known as next-generation reservoir computers (NG-RCs). These models approximate the Koopman operator on the space spanned by their explicit feature library. We consider the identifiability problem for learning Markovian nonlinear dynamical systems and show that the training error as a function of time resolution follows characteristic (pre-)asymptotic scaling laws. These laws depend on whether the feature library can represent the early Lie-series coefficients of the flow map (propagator) exactly or merely approximately. For dynamical systems governed by polynomial vector fields, we demonstrate the mechanism for NVAR/NG-RC models with monomial and Fourier feature libraries. We determine the dependence of the training error on the temporal resolution, the involved nonlinear degree, and the number of delay terms. While delay terms reduce the optimal one-step training error, they improve long-horizon forecasts only when the library provides sufficient nonlinearity. Thus, small training error coexists with weak generalization as the model class is mismatched to the true data-generating process. Numerical experiments on various chaotic dynamical systems confirm the theoretical predictions.

---


### 276. [Answer-Set-Programming-based Abstractions for Reinforcement Learning](https://arxiv.org/abs/2605.31444)

**<font color=#1a73e8>作者：</font>** Rafael Bankosegger, Thomas Eiter, Johannes Oetsch  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) enables autonomous agents to learn policies from experience, but realistic problems often involve enormous state spaces, making learning and generalisation challenging. Abstraction and approximation are therefore essential. Relational Reinforcement Learning (RRL) offers a way to reason about objects and their relations, and the CARCASS framework by Martijn van Otterlo demonstrates how logical representations can model Markov Decision Processes (MDPs) in first-order domains. Originally implemented in Prolog, CARCASS leverages domain knowledge to create powerful abstractions. We explore Answer-Set Programming (ASP), which is a rich and, contrary to Prolog, fully declarative modelling language, to realise CARCASS abstractions. We evaluate our ASP-based implementation in case studies of two domains, viz. Blocks World and Minigrid. Our results indicate that CARCASS with ASP provides a promising approach to constructing abstractions for RL, especially when domain knowledge is available.

---


### 277. [Fine-grained Verification via Diagnostic Reasoning Supervision for Aspect Sentiment Triplet Extraction](https://arxiv.org/abs/2605.31446)

**<font color=#1a73e8>作者：</font>** Wenna Lai, Haoran Xie, Guandong Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect Sentiment Triplet Extraction (ASTE) aims to identify aspect terms, opinion terms, and sentiment polarities as structured triplets, providing essential inputs for downstream information system applications such as opinion mining, explainable recommendations, and review summarization. Prior work mainly focuses on end-to-end extraction, while post hoc verification of extracted triplets remains comparatively underexplored. This gap limits the reliability of ASTE systems, since predicted triplets may be locally plausible while being globally invalid. Moreover, candidate invalidity is multi-faceted and candidate usability is inherently graded, motivating a fine-grained verification mechanism that can filter or re-rank outputs from diverse extractors. In this paper, we propose FiVeD, a framework for Fine-grained Verification with Diagnostic reasoning supervision. Specifically, the verifier is trained with multiple complementary objectives, including validity classification and quality score estimation as primary tasks, with error type classification and rationale generation as auxiliary tasks. We define hierarchical error categories and construct plausible incorrect triplets under semantic and syntactic constraints, and leverage an off-the-shelf LLM with task-specific rubrics to produce quality scores and diagnostic rationales. During inference, the resulting quality scores are used to filter candidate outputs, supporting adjustable precision-recall tradeoffs. Experiments across multiple ASTE baselines demonstrate that FiVeD consistently improves extraction performance by up to 3.53 F1 points as a plug-and-play verification module.

---


### 278. [VolFill: Single-View Amodal 3D Scene Reconstruction with Volumetric Flow Matching](https://arxiv.org/abs/2605.31466)

**<font color=#1a73e8>作者：</font>** Tuan Duc Ngo, Chuang Gan, Evangelos Kalogerakis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing the complete geometry of a scene from a single RGB image remains challenging - especially when inferring hidden structures where visual evidence is incomplete. We introduce VolFill, a generative framework that predicts the 3D structure of the complete scene rather than relying on traditional pixel-aligned regression. Our method utilizes a hybrid 3D VAE to compress sparse truncated unsigned distance function grids into a compact latent space, paired with a latent Diffusion Transformer that denoises this representation to recover the complete scene. We condition the generation on geometry foundation models, leveraging rich spatial priors for robust reasoning. Unlike existing methods limited by per-ray constraints or unstructured point-cloud queries, VolFill provides a structured representation that supports direct surface extraction and occupancy queries at scale. Extensive experiments on the SCRREAM and NRGB-D datasets demonstrate that our approach significantly outperforms current baselines, providing a robust foundation for holistic spatial understanding.

---


### 279. [Scaling Conversational Hungarian ASR: The BEA-Dialogue+ Corpus](https://arxiv.org/abs/2605.31469)

**<font color=#1a73e8>作者：</font>** Máté Gedeon, Piroska Zsófia Barta, Péter Mihajlik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational automatic speech recognition in Hungarian is constrained by the limited amount of publicly available dialogue-style training data. The BEA-Dialogue corpus addresses this need, but its strictly speaker-disjoint train/dev/eval split reduces the usable material to only 85 hours. In this paper, we introduce BEA-Dialogue+, an expanded version of the corpus that relaxes the split criterion for experimenters and dialogue partners while preserving complete separation of the primary speakers. This results in 200 hours of transcribed natural conversations and enables a controlled study of the trade-off between additional training data and speaker overlap across the splits. We evaluate several Whisper- and FastConformer-based models on both corpus versions, including Serialized Output Training (SOT)-based fine-tuning for dialogue transcription. Our results show that the larger corpus is more challenging for models without fine-tuning, whereas SOT-based adaptation yields consistent improvements in WER, CER, cpWER, and cpCER. Overall, BEA-Dialogue+ provides a substantially larger yet still demanding benchmark for Hungarian dialogue ASR, and a practical resource for training and evaluating dialogue transcription systems.

---


### 280. [Balanced LoRA: Removing Parameter Invariance to Accelerate Convergence](https://arxiv.org/abs/2605.31484)

**<font color=#1a73e8>作者：</font>** Valérie Castin, Kimia Nadjahi, Pierre Ablin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) is the most widely adopted method for fine-tuning large language models. Notably, LoRA is inherently overparameterized: multiple pairs of low-rank factors can yield the same adapted weight matrix. We show--both theoretically and empirically--that these pairs exhibit significantly different condition numbers. As a result, converging to different loss minimizers directly impacts the convergence rate of LoRA. Building on this observation, we introduce Balanced Low-Rank Adaptation (BaLoRA), a variant of LoRA that projects iterates onto a balanced manifold. This manifold improves the conditioning of the loss landscape while preserving the adapted matrix. The projection step is computationally lightweight and integrates seamlessly into existing fine-tuning pipelines. Empirically, BaLoRA converges faster than standard LoRA and achieves superior performance across a range of fine-tuning tasks.

---


### 281. [Graphical einops: bridging tensor networks and computation graphs](https://arxiv.org/abs/2605.31485)

**<font color=#1a73e8>作者：</font>** Vincent Wang-Maścianica, Nikhil Khatri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Architecture diagrams are ubiquitous in deep learning, but they are usually only representational: the tensor-program identities they suggest are still proved by prose and tensor-axis manipulation. We introduce a formal graphical calculus for the structural fragment of tensor programming underlying einops, making such diagrams proof-enabling. Our calculus represents tensor axes as nested graded tubes around a base type. The tube boundary recovers the undirected tensor-network view of axes, while the directed interior retains the operational reading of computation graphs. The key rewrite is grade-naturality: sliding spectacles over tubes. Standard equivariance proofs become short diagrammatic derivations. We additionally demonstrate how our rewrite system may be applied to convert attention masks into pre-processing operations, recovering efficient implementations of sparse attention blocks.

---


### 282. [Enhancing Computer Vision Model Generalization in Warehouse Facilities: A Case Study on Anomaly Detection in Vertical Material Handling Systems](https://arxiv.org/abs/2605.31487)

**<font color=#1a73e8>作者：</font>** Ruiliang Liu, Tina Dongxu Li, Joshua Migdal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying computer vision models in Warehouse Facilities traditionally requires extensive resources for camera mounting, image collection, annotation, training, and deployment - a process often needing repetition in each new environment due to camera mounting constraints and environmental variability. This paper explores an innovative approach to streamline this process by conducting the standard procedure solely in a laboratory setting, focusing on vertical material handling systems and anomaly detection in forks of the systems. Through extensive experimentation, we have found that combining optimal camera placement, strategic image triggering, careful model selection and model ensemble enables effective generalization from laboratory conditions to diverse warehouse facilities environments, potentially transforming warehouse automation implementation by simplifying warehouse facilities deployment to just camera mounting, image collection, and model deployment, thereby saving significant resources and time typically spent on image annotation and model retraining. This is an experimental research study and not a production deployment.

---


### 283. [Are Full Rollouts Necessary for On-Policy Distillation?](https://arxiv.org/abs/2605.31490)

**<font color=#1a73e8>作者：</font>** Yaocheng Zhang, Jiajun Chai, Songjun Tu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) provides dense teacher feedback along rollouts generated by the student and has emerged as a promising post-training paradigm for long-horizon reasoning. However, standard OPD typically generates full rollouts during training, which is computationally expensive and may expose the student to unreliable teacher feedback at late rollout positions, especially during early training. We identify the rollout horizon as a key bottleneck in OPD that substantially impacts training efficiency. Unlike Reinforcement Learning with Verifiable Rewards (RLVR), OPD does not require a complete trajectory or a final answer reward to provide learning signals. This observation suggests that full rollouts may not always be necessary for effective OPD. Motivated by this insight, we propose two simple horizon-control strategies: Progressive OPD (POPD), which gradually expands the rollout horizon during training, and Truncated OPD (TOPD), which permanently performs distillation on reliable truncated rollouts. Experiments on mathematical reasoning show that POPD improves the training efficiency of OPD by up to 3$\times$, while TOPD matches OPD performance using only 10\% of the rollout horizon, leading to substantial wall-clock and memory reductions. These results demonstrate that controlling the rollout horizon offers a simple and practical path to more efficient OPD.

---


### 284. [Assign and Add: A Mechanistic Study of Compositional Arithmetic](https://arxiv.org/abs/2605.31497)

**<font color=#1a73e8>作者：</font>** Brady Exoo, Alberto Bietti, John Sous  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are able to compose skills in order to perform complex tasks, many of which might not have been seen during training. The details of how exactly this composition occurs remain elusive. In this paper, we study a mechanism for compositional generalization in transformers by considering a simple controlled setting involving variable assignment and modular addition. By partitioning our training data into disjoint sets, we observe that small transformers are able to generalize to previously unseen combinations of variables and numbers. Our mechanistic analysis shows that the same ``modular addition'' MLP module is used whether the inputs are given directly or indirectly through a separate variable assignment mechanism. We also analyze the training dynamics from an empirical lens, which reveals three phases of learning: first, modular addition is learned, then the structure required for variable assignment, and finally a refinement phase where the model generalizes to some hard sequences not seen in training. Finally, we provide a theoretical framework to explain how compositionality emerges from training dynamics. These results suggest that compositional generalization can be a natural consequence of the compositionality of internal mechanisms in~transformers.

---


### 285. [Scalable Inference-Time Annealing with Surrogate Likelihood Estimators](https://arxiv.org/abs/2605.31498)

**<font color=#1a73e8>作者：</font>** Daniel Peñaherrera, Rishal Aggarwal, David Ryan Koes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A long standing challenge in computational chemistry and biophysics is efficiently sampling the Boltzmann distribution of molecules. Advances in generative modeling have been proposed to address the limitations of conventional sampling techniques by eliminating the computational cost of simulation. A promising direction is iteratively finetuning diffusion models along a temperature ladder whereby training data is generated via importance sampling during inference-time annealing. Unfortunately, these methods require computing a divergence over the score field to estimate importance weights, rendering them intractable for larger systems. Here we present scalable inference-time annealing (SITA), which retrains flow-based models to generate samples at progressively lower temperatures using an energy-based model to facilitate fast surrogate likelihoods. We demonstrate state-of-the-art performance on both Alanine Dipeptide and Alanine Tripeptide while avoiding costly divergence terms. Our code is available at: this https URL

---


### 286. [On Efficient Scaling of GNNs via IO-Aware Layers Implementations](https://arxiv.org/abs/2605.31500)

**<font color=#1a73e8>作者：</font>** Daria Fomina, Daniil Krasylnikov, Alexey Boykov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) are bottlenecked by sparse, irregular memory access. Popular frameworks such as DGL and PyTorch Geometric support general message passing, but complex layers often materialize edge-wise intermediates, increasing memory traffic and limiting scalability on large graphs. We take an I/O- and arithmetic-intensity--centric view and show that widely used layers fall into three kernel families: SpMM-based convolutions, reduction-based aggregations, and attention-based layers (GATv2/Graph Transformer). For each family, we develop GPU kernels that reduce data movement, improve locality, and remain robust across realistic graphs. We also study graph reordering and find that its impact depends on the kernel mapping: it benefits neighbor-parallel (gather-dominated) kernels more consistently than feature-parallel designs. Empirically, our fused attention kernels reach up to $\textbf{3.9}\times$ speedup for Graph Transformer (median $\textbf{1.6}\times$), with Tensor Core (block-sparse) variants up to $\textbf{7.3}\times$ on locally dense graphs; for GATv2 we reach up to $\textbf{8.5}\times$ speedup (median $\textbf{2.0}\times$) while reducing peak memory by up to $\textbf{76}\times$ (median $\textbf{6}\times$). Our degree-aware reduction kernels achieve up to $\textbf{10}\times$ speedup (median $\textbf{2.6}\times$). For SpMM-based layers, properly cached cuSPARSE achieves up to $\textbf{8}\times$ speedup over DGL and outperforms evaluated custom baselines in the majority of evaluations. We release our implementations as drop-in replacements to support reproducible, hardware-aware GNN acceleration.

---


### 287. [How can embedding models bind concepts?](https://arxiv.org/abs/2605.31503)

**<font color=#1a73e8>作者：</font>** Arnas Uselis, Darina Koishigarina, Seong Joon Oh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans easily determine which color belongs to which shape in multi-object scenes, an ability known as concept binding. Vision-language embedding models such as CLIP struggle with binding: they recognize individual concepts but fail to represent which concepts form which objects. Although CLIP behaves like a bag-of-concepts model in cross-modal retrieval, object information is recoverable from its image and text embeddings separately. We study this tension through the binding function, which maps concepts to scene embeddings. We find that scene embeddings decompose additively into object representations, explaining why uni-modal probes can recover object information. However, CLIP's binding function is high-complexity, which likely prevents the image and text encoders from learning a shared binding mechanism that generalizes to unseen concept combinations. We then ask whether this limitation is fundamental. We show that it is not. In controlled transformer models trained from scratch, binding generalization emerges with sufficient data coverage. These models learn low-complexity binding functions characterized by multiplicative interactions between concepts, enabling systematic generalization. Code is publicly available at this https URL.

---


### 288. [Internalizing Temporal Consistency in Video Object-Centric Learning without Explicit Regularization](https://arxiv.org/abs/2605.31508)

**<font color=#1a73e8>作者：</font>** Rongzhen Zhao, Zhiyuan Li, Juho Kannala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Object-Centric Learning (OCL) aims to represent objects as \textit{slot} vectors and maintain their consistency across frames. Slot-Slot Contrastive (SSC) loss has become the cornerstone for state-of-the-art (SOTA) video OCL methods. While highly effective, SSC relies on one-to-one object correspondence across frames and introduces an extra loss. Following Occam's Razor, we propose a paradigm shift: temporal consistency is better enforced as an implicit model design rather than an explicit loss. To elegantly exclude SSC (\textbf{xSSC}), we introduce two quasi-zero-overhead synergistic mechanisms: (\textit{i}) Chrono-Channel Decomposition (CCD) structurally disentangles slot representations along the channel dimension into \textit{static} and \textit{dynamic} sub-spaces, serving as an empirically unified information bottleneck; (\textit{ii}) Cross-Temporal Reconstruction (CTR) stochastically reconstructs target features of either the current or previous time step by fusing current slots' static channels and target slots' dynamic channels, using a single standard OCL decoder with minor training adaptation. Thereby, the slot sets inherently learn temporal consistency by minimizing the standard reconstruction error alone. Extensive experiments show that integrating xSSC into leading baselines not only improves training efficiency but also establishes new SOTAs on video object discovery and recognition tasks. Furthermore, our PCA and gradient analyses confirm that objects' time-invariant semantics and time-variant kinematics are encoded into the proposed sub-spaces. Our source code, model checkpoints and training logs are provided on this https URL.

---


### 289. [On the Relationship Between Activation Outliers and Feature Death in Sparse Autoencoders](https://arxiv.org/abs/2605.31518)

**<font color=#1a73e8>作者：</font>** Elana Simon, Etowah Adams, James Zou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) decompose neural network activations into interpretable features, but many learned features never activate, a problem called feature death that wastes dictionary capacity and can reintroduce superposition. Death rates vary dramatically between models: near-zero on GPT-2, over 70% on AlphaFold3 with identical configurations. We find that dimension-level activation outliers (dimensions whose mean magnitude is large relative to per-token variation) cause this by shifting pre-activations at initialization based on each feature's alignment with the activation mean. Features anti-aligned with the mean receive permanently negative pre-activations and never fire. We formalize outlier severity as $\gamma = \|\mu\|/\|\sigma\|$; it predicts initial death rates (Spearman $\rho = 0.89$ for dead-by-TopK, $0.82$ for dead-by-ReLU) across 454 model-layer combinations spanning language, vision, protein, and genomic models. Dead features can revive during training, but recovery requires the SAE bias to learn the activation mean, a process that is prohibitively slow at high $\gamma$. Mean-centering (subtracting the activation mean) sidesteps this and eliminates outlier-induced death across all tested models, confirming the mechanism and providing a principled basis for when and why this preprocessing step is necessary.

---


### 290. [UniAudio-Token: Empowering Semantic Speech Tokenizers with General Audio Perception](https://arxiv.org/abs/2605.31521)

**<font color=#1a73e8>作者：</font>** Yuhan Song, Linhao Zhang, Aiwei Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic speech tokenizers have become a widely used interface for Audio-LLMs, owing to their compact single-codebook design and strong linguistic alignment. However, their focus on linguistic abstraction induces acoustic blindness, limiting their applicability beyond speech-centric tasks. We propose UniAudio-Token, a framework that empowers semantic tokenizers with general audio perception without compromising speech ability. Instead of altering the semantic paradigm, UniAudio-Token mitigates its information loss through two key innovations: (1) Semantic-Acoustic Primitives (SAP) provide structured supervision by decomposing audio into linguistic content, vocal attributes, and auditory-scene primitives; and (2) Semantic-Acoustic Equilibrium (SAE) introduces a content-aware gating mechanism that adaptively restores fine-grained acoustic details from shallow layers. Extensive evaluations show that UniAudio-Token learns comprehensive universal representations while preserving high-fidelity speech generation. When integrated with downstream LLMs, it outperforms all single-codebook baseline tokenizers on both understanding and generation tasks, effectively serving as a unified audio interface. We publicly release all our code, including training and inference scripts, together with the model checkpoints at this https URL.

---


### 291. [Chem-PerturBridge: a harmonized compendium of small molecule perturbation transcriptomic effects](https://arxiv.org/abs/2605.31522)

**<font color=#1a73e8>作者：</font>** Artur Szałata, Olga Novitskaia, Maiia Shulman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large perturbation models require training data encompassing chemical, cellular, and assay diversity. Current transcriptomic resources for small-molecule modeling, however, are fragmented across technologies, metadata conventions, controls, doses, and preprocessing pipelines. We introduce Chem-PerturBridge, a harmonized multi-dataset resource comprising over 37k compounds, 136 cellular contexts, and 1.25M transcriptomic samples across eight assay types, with standardized identifiers, metadata, and replicate-aware condition-level effects. We use the resource to evaluate matched-condition agreement across datasets and replicate agreement within datasets. Matched same-compound conditions generally show weak agreement in fine-grained logFC rankings and magnitudes across most dataset pairs, often falling below same-context different-compound baselines. In contrast, logFC direction agreement is substantially more stable and usually exceeds these baselines. We further evaluate Chem-PerturBridge as a pretraining resource for compound representation learning. Under a compound-held-out OP3 evaluation split, embeddings pretrained on Chem-PerturBridge improve over L1000-only embeddings, Morgan fingerprints, and the descriptor-free OP3 baseline across metrics. An extensive molecule-holdout evaluation across 11 datasets further shows that models trained on Chem-PerturBridge outperform or match those that are not. Chem-PerturBridge therefore supports both diagnostic evaluation of cross-dataset signature agreement and model-oriented reuse of heterogeneous perturbation transcriptomic data.

---


### 292. [Value Functions as Supermartingale Certificates](https://arxiv.org/abs/2605.31524)

**<font color=#1a73e8>作者：</font>** Alessandro Abate, Daniel Contro, Mirco Giacobbe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Certification methods for stochastic systems provide sufficient proof rules, based on real-valued supermartingale certificates, to determine the almost-sure satisfaction of $\omega$-regular properties (and therefore of linear temporal logic) over general state spaces, encompassing both countably infinite and continuous state spaces. Conversely, reinforcement learning (RL) methods for $\omega$-regular tasks have received considerable attention, but they typically lack formal guarantees that the learned policy satisfies the specification, except possibly for finite state and action spaces. We bridge these two lines of research by establishing a novel theoretical connection: under an appropriate reward, the value function associated to a policy that almost surely satisfies an $\omega$-regular property encodes a Streett supermartingale certificate for that specification. Our results, validated experimentally on finite Markov decision processes, hold for finite, countably infinite, and continuous state spaces, suggesting a principled route to certificate synthesis via RL.

---


### 293. [SVI-Bench: A Dynamic Microworld for Strategic Video Intelligence](https://arxiv.org/abs/2605.31529)

**<font color=#1a73e8>作者：</font>** Yulu Pan, Han Yi, Seongsu Ha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> True video intelligence demands more than recognizing what is visible: it requires reasoning about why events unfold, predicting what would change under different conditions, and deciding what to do next. We refer to this progression, from perception through causal reasoning and simulation to strategic planning, as Strategic Video Intelligence (SVI). No existing benchmark evaluates this capability stack: in-the-wild videos lack verifiable ground truth for causal and strategic questions, while synthetic environments sacrifice the complexity of real multi-agent systems. To bridge this gap, we introduce SVI-Bench, a large-scale benchmark that leverages team sports as a dynamic microworld, combining the complexity of real-world multi-agent interaction (10-22 agents making coordinated decisions under adversarial pressure) with the verifiability of explicit rules and definitive outcomes. SVI-Bench comprises approximately 35K hours of broadcast video, 15M annotated actions, 15K hours of expert commentary, 23K game reports, and 103K structured statistical records across basketball, soccer, and hockey, all constructed via a data engine that transforms raw game data into a dense, cross-referenced corpus. We organize evaluation into 9 tasks spanning a progressive four-pillar hierarchy: Dynamic Scene Understanding, Causal Reasoning, Strategic Simulation, and Agentic Synthesis. Evaluating strong multimodal and agentic baselines, we find a capability cliff: models perform competently on perceptual tasks, achieving approximately 73% on fine-grained action QA, but degrade sharply at each successive cognitive level. Agentic tasks prove hardest: the strongest model achieves only 5% accuracy when required to autonomously gather and integrate evidence across a corpus of 1.8M clips.

---


### 294. [Feature-Optimized Vision for Adaptive 3D Scene Reconstruction](https://arxiv.org/abs/2605.31534)

**<font color=#1a73e8>作者：</font>** Eric Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional scene reconstruction depends on local image evidence that is both visually discriminative and geometrically useful. Fixed feature thresholds and uniform feature budgets are easy to deploy, but they can waste computation on repeated texture, low-parallax regions, or unstable points. This paper proposes an adaptive feature-optimized vision front end for 3D reconstruction. The method scores candidate features by texture, repeatability, distinctiveness, expected triangulation angle, and spatial coverage, then allocates a per-view feature budget to maximize useful tracks under a fixed reconstruction pipeline. A small synthetic multi-view prototype evaluates four selection policies across corridor, facade, object-table, and cluttered scenes. Compared with random, texture-only, and uniform-grid baselines, the adaptive policy obtains the best quality-aware completeness and the lowest aggregate reconstruction RMSE while preserving broad image coverage. The result is not a replacement for modern learned matching or neural reconstruction systems; it is a modular front-end policy that can make classical and learned 3D pipelines more deliberate about which visual evidence they spend compute on.

---


### 295. [RayDer: Scalable Self-Supervised Novel View Synthesis from Real-World Video](https://arxiv.org/abs/2605.31535)

**<font color=#1a73e8>作者：</font>** Ulrich Prestel, Stefan Andreas Baumann, Nick Stracke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised novel view synthesis (NVS) remains challenging to scale, despite the abundance of video data, largely due to the brittleness of training on realistic videos and the hard-to-predict scaling behavior of multi-network system designs. We introduce RayDer, a unified, feed-forward transformer that consolidates camera estimation, scene reconstruction, and rendering into a single backbone, turning self-supervised NVS into a well-posed single-model scaling problem. A minimal dynamic state, treated as a nuisance factor, absorbs time-varying content and enables stable training on unconstrained real-world video. Importantly, RayDer keeps static-scene NVS as its target task: dynamic content is leveraged purely as scalable supervision, not reconstructed as in dynamic-scene (4D) NVS. Across multiple model sizes and orders of magnitude in data, RayDer exhibits clean power-law scaling with data and compute, and outperforms static-scene data mixtures. On a large number of benchmarks, RayDer achieves strong zero-shot open-set performance competitive with state-of-the-art supervised approaches. Project Page: this https URL

---


### 296. [Automated Prediction of Postoperative Pancreatic Fistula Using Preoperative Computed Tomography](https://arxiv.org/abs/2605.31539)

**<font color=#1a73e8>作者：</font>** Ashok Choudhary, Chris Varghese, Leo Y. Li-Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Postoperative pancreatic fistula (POPF) is a serious complication after pancreatic resection, increasing morbidity, hospital stay, and healthcare costs. We present an automatic, end-to-end deep learning pipeline-from pancreatic segmentation to classification-for preoperative POPF risk estimation and stratification using preoperative CT scans. A data set with auto-segmented pancreas volumes and surgical outcomes was used to evaluate multiple architectures, including a custom lightweight 3D CNN baseline (CNN3D), R(2+1)D ResNet-18, and ResNet-MC3-18 models. Evaluation across multiple 3D architectures demonstrated promising predictive performance. This approach offers a clinically valuable tool and a methodological benchmark for pancreas-specific CT classification, supporting improved preoperative decision-making in pancreatic surgery.

---


### 297. [The Dynamic-Probabilistic Consistency Gap in Chaotic Surrogate Modeling](https://arxiv.org/abs/2605.31547)

**<font color=#1a73e8>作者：</font>** Andre Herz, Matthijs Pals, Daniel Durstewitz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamical systems reconstruction (DSR) aims to learn surrogate models that capture the dynamics underlying time-series data. Reliably deploying these surrogates requires uncertainty estimates consistent with the learned dynamics. We expose a dynamic-probabilistic consistency (DPC) gap: the pursuit of finite-horizon probabilistic objectives can degrade dynamics or decouple predictive uncertainty from the local tangent dynamics it ought to reflect. We isolate three mechanisms behind this gap: core collapse, noise masking, and blind uncertainty. Specifically, we show that open-loop Gaussian rollout objectives can penalize Jacobian-generated covariance growth in chaotic systems, encouraging optimization shortcuts that weaken physical expansion or decouple uncertainty from it. To mitigate this gap, we propose KAFFEE (Kalman-Aware Framework For Ergodic Emulation), a differentiable extended Kalman filter-based training framework that evaluates likelihood on local predictive residuals (innovations) while transporting covariance through learned local Jacobians. On stochastic hyperchaotic Lorenz-96, KAFFEE reduces the identified failure modes, improves reconstruction of dynamical invariants relative to open-loop objectives, and maintains competitive predictive scores. We further show that the DPC gap appears when probabilistically adapting a DSR foundation model across 13 chaotic systems, where KAFFEE enables in-context Bayesian filtering while largely preserving zero-shot dynamics.

---


### 298. [SMART: SMPLest-X Mesh Adaptation and RAFT Tracking for Soccer Pose Estimation](https://arxiv.org/abs/2605.31551)

**<font color=#1a73e8>作者：</font>** Parthsarthi Rawat  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present our approach to the FIFA Skeletal Tracking Challenge 2026, which requires estimating 3D world-space poses of soccer players from broadcast video. Our method finetunes SMPLest-X (ViT-H, 687 M parameters) via a stratified clip split, multi-task depth supervision, and broadcast augmentation, paired with a RAFT dense optical flow camera tracker, foot-plane anchoring, and two-pass temporal smoothing. Against the FIFA baseline score of 1.053 on the validation set, SMART achieves 0.647, a 38.6% improvement; on the held-out test set, SMART scores 0.593 (Global MPJPE: 0.324 m, Local MPJPE: 0.054 m).

---


### 299. [EGOSTREAM: A Diagnostic Benchmark for Streaming Episodic Memory in Egocentric Vision](https://arxiv.org/abs/2605.31557)

**<font color=#1a73e8>作者：</font>** Rosario Forte, Giuseppe Lando, Antonino Furnari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous episodic memory is a core capability for autonomous agents operating in dynamic, real-world environments, yet current streaming video benchmarks provide limited tools for diagnosing what models remember and for how long. We introduce \egostream, a diagnostic benchmark for streaming episodic memory evaluation in egocentric vision. \egostream organizes 2,250 curated questions along seven cognitive dimensions: detail, spatial, temporal, event, social, causal, and prospective memory. We introduce the Answer Validity Window (AVW), which specifies the temporal span an answer remains valid as the observed scene evolves. This allows us to expand the questions into 8,528 recall-conditioned evaluations, enabling controlled testing from instant to ultra-long-term recall while separating genuine model forgetting from natural world-state changes. We rigorously establish baseline performance through a unified streaming MLLM framework that compares several state-of-the-art memory-management mechanisms, covering sliding windows, attention sinks, KV-cache pruning, merging, and offloading. Experiments within a unified Qwen3-VL backbone reveal that comparable aggregate accuracies mask starkly different memory profiles. For instance, token pruning preserves fine-grained details and temporal structure significantly better than token merging, while quantized offloading rescues ultra-long-term recall. Ultimately, all mechanisms operate well below real-time (>1s per frame), and top performing methods ceil at about 45\% accuracy, exposing critical gaps in current architectures. \egostream provides the diagnostic testbed needed to close these gaps.

---


### 300. [Positional versus Symbolic Attention Heads: Learning Dynamics, RoPE Geometry, and Length Generalization](https://arxiv.org/abs/2605.31558)

**<font color=#1a73e8>作者：</font>** Felipe Urrutia, Juan José Alegría, Cinthia Sanchez Macias 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models are widespread in today's society. As such, understanding the mechanisms by which they solve structured tasks and predicting how they may behave in novel scenarios is of great importance for safe deployment. We study the learning dynamics of attention heads in a controlled setting by training a decoder-only Transformer (GPT-J) on two structurally equivalent multi-hop reasoning tasks: a number task requiring positional reasoning and a letter task requiring symbolic reasoning. Using a recently introduced metric that classifies attention-head behavior as positional or symbolic for a given prompt, we show that successful learning is associated with the emergence of pure heads, i.e., heads that express themselves as either positional or symbolic. Despite the tasks' structural equivalence, they impose different mechanistic demands: the number task requires both positional and symbolic heads, whereas the letter task requires only symbolic heads. We then identify the computational roles of these heads, characterize the basic functions they implement, and give theoretical constructions showing how single-layer RoPE-based attention can realize these functions through geometrically interpretable query, key, and value operations. This analysis yields a quantitative separation between positional and symbolic mechanisms in their robustness to longer sequences, formalized through a novel notion of discrepancy. We empirically validate the resulting predictions in both controlled and real-world models, showing that symbolic mechanisms extrapolate more reliably to longer sequences while positional mechanisms face sharper limitations.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-317](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
