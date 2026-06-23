# 📦 其他研究 | 2026年06月24日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**601-650**（第 13/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-654](./part-14.md)

---

### 601. [Differential Spectral Damping Gap Adaptive Regularization for Ill-Conditioned Kernel Methods](https://arxiv.org/abs/2606.23407)

**<font color=#1a73e8>作者：</font>** Praveg Vashishtha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernel methods requiring matrix inversion -- particularly Least-Squares Twin Support Vector Machines (LSTSVM) -- suffer from exponential eigenvalue decay in their system matrices, producing severely ill-conditioned problems where standard Tikhonov regularization applies uniform damping regardless of eigenvector reliability. We propose Differential Spectral Damping (DSD), a regularization formula that adapts its penalty to localized eigengap structure: preserving eigenvectors with large spectral gaps (reliable per Davis-Kahan perturbation theory) while aggressively suppressing those with small gaps (directionally corrupted beyond recovery). We motivate DSD through a principled design procedure grounded in the Davis-Kahan $\sin(\Theta)$ theorem, systematically deriving the requirements for a reliability-aware damping function and selecting the exponential form for its smoothness, differentiability, and natural saturation properties. Through rigorous paired testing with fairly optimized baselines (including gradient-optimized Tikhonov receiving equal optimization opportunity), we demonstrate that DSD improves LSTSVM classification accuracy by +4.8 percentage points on real-world GINA ($d=970$, Cohen's $d = 4.49$, $p < 0.0001$), +10.4 percentage points at $d=200$, and +2.6 percentage points on Madelon ($d=500$) -- all using only principled spectral initialization while Tikhonov receives grid search. For pre-image reconstruction on manifold data, DSD ties Tikhonov at high perturbation noise ($p=0.99$) but slightly underperforms at lower noise levels; both reduce naive inversion error by $66\times$. We characterize the precise operating regime ($d \geq 100$, condition number $> 10^3$) and document where simpler methods suffice, providing practitioners with clear deployment guidance.

---


### 602. [UnBias-Plus: Detect, Explain, and Rewrite Bias](https://arxiv.org/abs/2606.23412)

**<font color=#1a73e8>作者：</font>** Ahmed Y. Radwan, Ahmed ElKady, Sindhuja Chaduvula 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bias in natural language remains a persistent challenge in both human-written and AI-generated content, affecting domains such as journalism, education, and AI research. Most existing detection methods identify only the presence of bias, with limited support for granular detection, interpretable explanations, neutral rewriting, and openly available trained models. We present UnBias-Plus, an open-source toolkit unifying (1) segment-level multi-class bias classification, (2) biased span localization, (3) neutral text rewriting, and (4) reasoning for each decision. Available via Python, CLI, REST API, and web interfaces, UnBias-Plus supports accessible bias analysis. The toolkit, source code, models, datasets, and documentation are publicly available.

---


### 603. [Detecting Malicious Agent Skills in the Wild using Attention](https://arxiv.org/abs/2606.23416)

**<font color=#1a73e8>作者：</font>** Bacem Etteib, Daniele Lunghi, Tégawendé F. Bissyandé  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly load skills, file-based packages of natural-language instructions written by third parties and distributed through marketplaces, that execute with the user's privileges. A single malicious skill can exfiltrate data, hijack the agent, or persist as a supply-chain foothold, which turns the skill marketplace into a new attack surface for agentic systems. Prompt-injection defenses do not carry over to this setting. They rely on a boundary between trusted instructions and untrusted data, whereas a skill is itself a body of instructions, so an injected command sits among many legitimate ones and inherits their authority. We present Locate-and-Judge, a two-stage detector designed for this regime. A lightweight locator scores the structural spans of a skill by the instruction-following attention each span draws and retains only the top-K. A judge then examines the retained spans in detail. Concentrating the costly judgment on a few high-attention spans lets the detector audit an entire marketplace instead of a sample. Compared to direct LLM-based scanning, this approach offers an order-of-magnitude cost reduction, dramatically increasing its scalability at a small cost to recall, and it dominates keyword and regex baselines at comparable expense. Deployed at marketplace scale and at negligible cost, Locate-and-Judge flags skills with high precision, the majority of which we manually confirmed as malicious, surfacing dozens of live malicious skills, including several disguised as benign functionality and many that SkillSpector and Cisco Skill Scanner fail to detect. We release the resulting labeled dataset.

---


### 604. [Digital Humanism and Evolutionary Design](https://arxiv.org/abs/2606.23417)

**<font color=#1a73e8>作者：</font>** Wolfgang Höhl  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper examines the two concepts of digital humanism and evolutionary design. The aim is to identify and highlight potential common structures, synergies, and challenges. How should and can technical systems be designed, and what implications does this have for the design of our environment? In light of the current debate surrounding artificial intelligence, this paper aims to serve as a preliminary study to help better understand the two concepts of digital humanism and evolutionary design within the context of human-centered technological development. Following a brief introduction, the two concepts of Digital Humanism and Evolutionary Design are presented and graphically visualized. The terms of freedom and responsibility in human decision-making, conviviality, and subjectivity are discussed, along with examples illustrating the distinction between human and artificial intelligence (Turing Test and Chinese Room). The various concepts of evolutionary design (e.g., co-evolutionary or sustainable software development, clean code, or green IT) and Gilbert Simondon's concept of the "open machine" are introduced. The interdependencies between functional specialization and open technology development are highlighted. Both concepts share similar structures. In joint cooperation, they can lead to positive effects and mutual synergies. Significant differences lie in the areas of autonomy and determination in decision-making, as well as in genuine and simulated subjectivity. Open technology development is also currently suffering from the functional specialization of software and AI applications due to a purely market- and consumer-oriented approach. Even optimizations for energy efficiency in sustainable software development lead to greater specialization and thus also have a detrimental effect on open and quality-oriented technology development.

---


### 605. [Interpretable Kolmogorov-Arnold Network with Feature-Isolated Temporal Attention Mechanism for Electricity Load Forecasting](https://arxiv.org/abs/2606.23425)

**<font color=#1a73e8>作者：</font>** Jinhao Li, Hao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate electricity load forecasting is a crucial prerequisite for stable power system operations. While prevalent deep learning models present competitive performance, they often operate as black boxes and lack interpretability. While the Kolmogorov-Arnold network (KAN) has emerged as a promising alternative because of its learnable activation function design, its direct application to time-series forecasting faces challenges in modeling complex temporal data patterns. Also, simple integration into existing architectures, such as serving as replacement of neural modules, cannot fully leverage KAN's interpretability strengths. To address these gaps, this study develops LoadKAN, a novel hybrid and interpretable framework for load forecasting that synergistically combines a specifically-designed feature-isolated temporal attention mechanism with a KAN module. The attention stage aims to extract temporal dynamics from each input feature independently, such as historical load and human mobility, providing distilled feature representations to the KAN module for interpretable predictions. When evaluated on datasets from three representative U.S. electricity markets, our LoadKAN remains highly competitive when compared to extensively-tuned, state-of-the-art, black-box deep learning benchmarks. More importantly, LoadKAN's interpretability enables a granular analysis of the learned non-linear relationships between six distinct mobility patterns and electricity load. Through KAN-learned activation functions, our quantitative sensitivity analyses on mobility features reveal complex and market-specific dependencies. These findings further demonstrate the ability of our LoadKAN to generate insights often obscured by opaque black-box neural forecasting models.

---


### 606. [Rethinking Object-Centric Representations for Video Dynamics Modeling](https://arxiv.org/abs/2606.23436)

**<font color=#1a73e8>作者：</font>** Amaury Wei, Ismail Nejjar, Olga Fink  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised video object tracking aims to decompose dynamic scenes into persistent, object-centric entities without manual annotations. Many recent approaches rely on slot-based representations, where a fixed set of latent variables ("slots") represent individual objects across frames. To preserve object identity, these models enforce temporal consistency on slot embeddings. However, when appearance and pose are entangled, this consistency objective conflicts with object motion and viewpoint changes. As a result, slots tend to lock onto static regions (e.g., background) to satisfy the consistency objective, while foreground objects become fragmented across multiple slots or frequently swap identities. To address these limitations, we propose STAITUS, a unified framework that explicitly disentangles each slot into appearance and geometric pose (position/scale). Leveraging this disentanglement, STAITUS enforces within-frame spatial separation and applies temporal alignment only in appearance space, yielding sharper masks and more persistent identities under motion, occlusion, and object entry/exit. Furthermore, to mitigate over-segmentation, we introduce an adaptive gating mechanism that dynamically adjusts the number of active slots to match scene complexity. Extensive experiments on synthetic and real-world benchmarks demonstrate that STAITUS substantially outperforms state-of-the-art baselines in segmentation quality and tracking stability.

---


### 607. [Cross-Architectural Mixture-of-Experts with Adaptive Soft Routing for Plant Leaf Disease Classification](https://arxiv.org/abs/2606.23441)

**<font color=#1a73e8>作者：</font>** Phi-Hung Hoang, Thi-Thu-Hong Phan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Plant leaf disease classification is crucial for crop protection and precision agriculture but remains challenging under complex backgrounds, illumination variations, and severe class imbalance. Moreover, single-architecture models often fail to effectively capture both local and global representations. To address these challenges, this study proposes an adaptive soft Mixture-of-Experts (MoE) framework with cross-architectural routing that integrates EfficientNet-B0, DenseNet-121, and Swin-Tiny to exploit complementary multi-scale, local, and global features. A soft gating mechanism dynamically assigns input-dependent expert weights, while a two-stage refinement training strategy improves optimization stability and generalization. Experiments on a highly imbalanced potato leaf disease dataset achieve 91.68% recall and 92.62% F1-score, surpassing the strongest individual expert by 5.91% and 5.03%, respectively. Additional evaluations on durian and sesame leaf disease datasets yield F1-scores of 94.03% and 97.04%, demonstrating robust cross-dataset generalization and the potential of the proposed framework for reliable real-world crop health monitoring

---


### 608. [Selective Time Series Forecasting via Metalearning](https://arxiv.org/abs/2606.23448)

**<font color=#1a73e8>作者：</font>** Ricardo Inácio, Vitor Cerqueira, Marília Barandas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning methods have achieved state-of-the-art in time series forecasting, yet their accuracy varies considerably across samples, as some instances remain inherently difficult to predict. Reject option mechanisms, which allow models to abstain from high-risk predictions, are well established in classification and regression but underexplored in forecasting. Existing abstention strategies typically rely on proxies, such as the width of the prediction interval or learned confidence scores derived from forecasts. However, these approaches are inherently tied to the training domain, limiting their ability to generalize. We propose a selective forecasting framework that addresses this limitation by modeling the empirical percentile of forecasting errors, that is, a scale-invariant statistic, based on structural characteristics extracted from recent lags via metalearning. By decoupling the rejection decision from the forecast itself and grounding it in domain-agnostic features, the framework enables effective abstention transfer across heterogeneous time series. Experiments in both in-domain and transfer learning settings show that rejecting samples predicted as challenging consistently improves forecasting accuracy across coverage levels.

---


### 609. [AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction](https://arxiv.org/abs/2606.23449)

**<font color=#1a73e8>作者：</font>** Shanhui Zhao, Jiacheng Liu, Guohong Liu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are driving a new software paradigm, with the ability to autonomously call tools, extract information, manage memory, and complete tasks that span applications and data sources. Most existing end-user operating systems, however, are designed for application-centric workflows and offer little native support for AI agents. This mismatch limits the wider adoption of agents and leads to execution overhead and safety risks when running agents on conventional systems. While the concept of agent-native operating systems is emerging, the research community lacks an open testbed to explore the architectural primitives desired for agent-mediated interaction. We present AOHP (Android Open Harness Project), an OS-level agent harness built on the Android Open Source Project (AOSP). The core design principle of AOHP is to treat agents as first-class OS actors, enabling adaptive user interfaces and agent-friendly runtime environments. AOHP preserves the mature Android software and hardware ecosystem while introducing three agent-oriented system mechanisms: personalized service composition, efficient agent interfaces, and secure information flow. Based on preliminary experiments on challenging tasks covering key capabilities of OS agents, AOHP shows clear advantages in task completion (+21.12% completion rate), execution cost (-51.55% token cost), and security-policy compliance.

---


### 610. [Do Location Encoders Capture Spatial Effects? A GeoShapley Benchmark Across Scales](https://arxiv.org/abs/2606.23453)

**<font color=#1a73e8>作者：</font>** Daniel Kiv, Shaowen Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Location encoders transform geographic coordinates into high dimensional embeddings for downstream machine learning, but it is unclear how well these representations capture interpretable spatial effects. We benchmark whether GeoShapley, a game-theoretic explainer that treats all location features as a single joint player, can recover spatially varying coefficients from models built on location-encoder embeddings. Eleven encoders from the TorchSpatial framework are evaluated against a synthetic process with known coefficients, across three scales (grid, county, global), with and without raw coordinates alongside the embedding, and under untrained and contrastively trained conditions. Measuring recovery as the correlation between estimated and true coefficients, we report how it varies with scale and encoder architecture and compare the embeddings against a raw-coordinate baseline. Recovery of the primary coefficient is consistently high across encoders, whereas recovery of a secondary coefficient is more scale-dependent, differing most at the global scale; the raw-coordinate baseline remains competitive throughout.

---


### 611. [MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing](https://arxiv.org/abs/2606.23455)

**<font color=#1a73e8>作者：</font>** Zesong Yang, Yuanhang Lei, Liyuan Cui 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances integrate physically grounded Newtonian dynamics with neural rendering frameworks, narrowing the gap between photorealistic scene reconstruction and physics-based animation. However, existing approaches focus on mechanically driven dynamics while neglecting temperature, a fundamental yet invisible physical factor underlying phenomena such as melting, solidification, and other thermomechanical processes. In this paper, we propose MeGAS, a novel framework that incorporates thermomechanical phase-change dynamics into 3D Gaussian Splatting (3DGS). Specifically, we propose a new thermomechanical dynamic Gaussian Splatting representation that augments 3DGS with temperature attributes and employs a heat advection-diffusion solver with MPM dynamics incorporating phase transitions, enabling physically plausible and visually realistic synthesis of thermophysical phenomena. Furthermore, a new topology-adaptive Gaussian rendering strategy is proposed to mitigate cracking and floaters under extreme deformation. Extensive experiments demonstrate that MeGAS produces physically consistent thermomechanical behavior while maintaining high-fidelity photorealistic rendering, advancing toward physics-integrated world models.

---


### 612. [War in the Abstract: The Rise and Consequences of Militarized Language in Scientific Communication](https://arxiv.org/abs/2606.23462)

**<font color=#1a73e8>作者：</font>** Sovesh Mohapatra, David Lydon-Staley, Dani S. Bassett  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientists do not, by profession, wage war. Yet warfare's vocabulary consistently appears in their abstracts. To quantify the extent to which warfare's vocabulary pervades scientific abstracts, we analyze 21.4 million papers (2010-2025; OpenAlex, PubMed). We additionally run a within-subject war-framing experiment (N = 801; 32,040 trials) designed to provide causal insight into the effects of militaristic language on persuasion. Between 2010 and 2025, the presence of militaristic terms in scientific abstracts rose 48% in OpenAlex and 32% in PubMed, with the rise accelerating sharply after 2019 (cross-database r = 0.96, p < 10^-8). The prevalence of militaristic language is conflict-aligned at both country and annual scales (Uppsala Conflict Data Program; r = 0.77-0.84), with the abstracts from the Global South displaying the fastest rise in militaristic language. Among disciplines, social sciences leads in level of such language while engineering and computer science lead in growth. The COVID and post-2022 large-language-model eras also saw the rise and narrowed the language gap between native-English and non-English authors. In our follow-up experiment, we found that war framing reduced credibility (mean shift -0.18 Likert units, 95% CI [-0.21, -0.14]; d_z = -0.28, p < 10^-20), funding willingness (d_z = -0.12) and policy support (d_z = -0.08), with a trend-level increase in sense of urgency (d_z = +0.07). Collectively, findings reveal that while scientific abstracts drift toward warfare, the use of militaristic language may erode credibility, funding willingness, and policy support.

---


### 613. [C^2GR: Coupled Comprehensive Generative Replay for a Continually Learnable Universal Segmentation Model](https://arxiv.org/abs/2606.23473)

**<font color=#1a73e8>作者：</font>** Wei Li, Jingyang Zhang, Guoan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Universal segmentation models exhibit significant potential for diverse tasks involving different imaging modalities and segmentation objectives. Task-Incremental Learning provides a privacy-preserving approach to continually evolve a universal model on tasks from sequentially-arriving medical departments. However, training the model solely on the incoming task induces forgetting on past tasks, since consecutive tasks exhibit concurrent shifts in image appearance and segmentation objective. To address this problem, we propose a novel Coupled Comprehensive Generative Replay (C^2GR) framework that simultaneously synthesizes image-mask pairs of previous tasks to mitigate forgetting under concurrent appearance and objective shifts. This requires preserving image-mask correspondence for structure-realistic generation and bridging asynchronous optimization of the generator and segmentor for segmentation-oriented generation. Specifically, we propose a Bayesian Joint Diffusion (BJD) method that formulates the correspondence as conditional distributions optimized via conditional denoising. Furthermore, we develop a Relation-aware Unified Prompt Synchronization (RUPS) scheme to simultaneously modulate the generator and segmentor via a shared task-relation-aware prompt for synchronizing their optimization. Experiments on 20 tasks spanning diverse modalities and objectives demonstrate that C^2GR exhibits only a 2.44% drop in overall performance compared to joint training with all task data, effectively alleviating forgetting from the concurrent shifts. Our code will be made publicly available at this https URL.

---


### 614. [From Reconstruction to Decision: A Post-Encoder Plug-in Adapter for Curvilinear Segmentation](https://arxiv.org/abs/2606.23486)

**<font color=#1a73e8>作者：</font>** Qin Lei, Jiang Zhong, Xin Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Curvilinear object segmentation, including vessels and cracks, is challenging due to extreme spatial sparsity and topological fragility, where small local errors can cause severe structural disconnections. Meanwhile, modern segmentation pipelines increasingly rely on strong but hard-to-modify foundation encoders whose heavy downsampling limits fine structural recovery. Motivated by this, we focus on the post-encoder stage and study two recurring and actionable failure modes: a reconstruction bottleneck in high-resolution feature restoration and a decision bottleneck in binarization. We present PEPA, a lightweight Post-Encoder Plug-in Adapter for 2D curvilinear segmentation pipelines with accessible decoder/head features and target, query, or class descriptors. PEPA couples (i) Target-Conditioned Snake Upsampling (TCSU), which uses target-conditioned continuous snake-like sampling to better recover thin and tortuous structures during upsampling, and (ii) Target-Adaptive Differentiable Thresholding (TADT), which predicts target-specific thresholds and optimizes a soft-threshold surrogate with explicit safeguards against trivial bias shifting. Under this post-encoder interface, PEPA can be attached to both prompt-based decoders and conventional dense predictors. Experiments on five medical and industrial benchmarks show that adding PEPA to frozen-encoder baselines yields consistent improvements, with gains in topological connectivity (clDice) typically exceeding those in region overlap (IoU), indicating improved structural continuity. With only $\sim$0.26M additional parameters, PEPA offers a practical post-encoder enhancement for structure-centric segmentation.

---


### 615. [Hallucinations in Organization-backed AI advisors: Evidence about Skepticism, Verification, and Reliance in Goal-Directed Use](https://arxiv.org/abs/2606.23491)

**<font color=#1a73e8>作者：</font>** Simon J. Blanchard, Aaron M. Garvey, Laura O'Laughlin  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI systems are increasingly used by organizations to deliver information to consumers, patients, students, employees, and citizens. These systems can hallucinate, producing plausible but inaccurate responses. A central question for AI-advised decisions is therefore not only whether users rely on inaccurate information, but whether they recognize that a response may require verification. To answer this question, we review emerging empirical evidence relevant to hallucination detection in goal-directed interactions, with a focus on organization-backed AI advisors. We distinguish three constructs that existing studies often conflate: whether users are skeptical of information presented, whether they check it, whether checking succeeds, and whether the result of user verification affects reliance on the information. Across studies examining product search, medical decision-making, content generation, and chatbot-assisted tasks, several patterns emerge. Nearly all studies measure reliance, while variables such as user skepticism and verification of the information are more often targeted by an intervention than measured directly. The cues used to prompt scrutiny of the AI response are predominantly related to the AI output, such as source citations, and the most deployable of these AI output interventions for organizations (general and specific warnings about the risk of hallucinations) show the weakest and most mixed effects in the studies reviewed. Although the existing literature posits that users may be more likely to scrutinize responses related to particular areas of content, no studies varied the content category, leaving this question open for further research. In future research, measuring skepticism and verification separately from reliance may clarify what current evidence shows, what it only implies, and which questions require further exploration.

---


### 616. [TROPT: An Open Framework for Unifying and Advancing Discrete Text Optimization](https://arxiv.org/abs/2606.23496)

**<font color=#1a73e8>作者：</font>** Matan Ben-Tov, Mahmood Sharif  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete text-trigger optimization -- searching for text sequences that, when ingested by a model, steer it toward a specified objective -- underpins model red-teaming (e.g., LLM jailbreaks), as well as auditing and interpretability. However, the current state of discrete optimizers hinders their adoption and progress. First, existing optimizers, when open-sourced at all, are scattered across research codebases tied to specific models, objectives, and problem domains. Second, optimizer variants proliferate, each requiring engineering overhead to use or extend, and remaining hard to compare head-to-head. Together, these raise the bar for adopting optimizers in existing or new domains, and for advancing them via new strategies. We address these gaps with TROPT, the first open-source framework that unifies discrete optimizers' execution and standardizes their development under a single interface. TROPT makes it easy to customize end-to-end optimization recipes by swapping any component -- models, objectives, and optimizers -- extending its reach across domains and new applications. TROPT currently ships with 30+ optimization recipes -- covering applications such as jailbreaking and probing model internals -- built from 15+ optimizers (spanning white-box to black-box access) and 15+ losses, from foundational to state-of-the-art methods. Demonstrating its utility, we leverage TROPT in several studies: (i) controlled, large-scale experiments comparing and enhancing optimization strategies for LLM jailbreaks, revealing potent-yet-underadopted techniques; and (ii) porting optimizers from one domain (e.g., LLM jailbreak) to new domains (e.g., corpus-poisoning embedding model). In all, TROPT significantly lowers the barrier to adopting and advancing discrete text optimization.

---


### 617. [UniverSat: Resolution- and Modality-Agnostic Transformers for Earth Observation](https://arxiv.org/abs/2606.23503)

**<font color=#1a73e8>作者：</font>** Yohann Perron, Guillaume Astruc, Nicolas Gonthier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViT) dominate computer vision. However, their reliance on rigid patch projectors hinders transfer to Earth Observation (EO), where input modalities, scales, and resolutions vary widely. We introduce UniverSat, a ViT-style backbone built around a Universal Patch Encoder that maps patches from arbitrary spatial, spectral, and temporal resolutions, and from both optical and non-optical sensors, into a shared embedding space with a shared set of weights. This enables training a single model on heterogeneous multimodal corpora via self-supervision, yielding robust, sensor-agnostic spatial features. We validate this approach with strong results across classification and segmentation on standard EO benchmarks from GeoBench, PANGEABench, and SpectralEarth. Our code and models are available at this https URL.

---


### 618. [Arbor: Explicit Geometric Conditioning for Controllable 3D Asset Generation](https://arxiv.org/abs/2606.23514)

**<font color=#1a73e8>作者：</font>** Jan-Niklas Dihlmann, Andreas Engelhardt, Simon Donne 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text and image conditioned 3D models now generate convincing assets, but they still offer little direct control over the space an object should occupy or avoid. In authoring, this spatial intent is often known before generation starts. A chair should fit a seating envelope, a prop should leave clearance for motion, or a part should expose a contact surface. Prompts and image views are poor carriers for such constraints, requiring the need for an explicit control interface.
We present Arbor, a trainable attachment for text conditioned latent 3D generation. Arbor introduces constraint meshes as a native 3D control interface. The interface uses hull regions where geometry should exist, avoidance regions that should remain empty, and touch regions the object should contact. Unlike completion or whole object scaffold control, these meshes are not target evidence. They are local typed requirements and can include regions where no surface should appear. Arbor keeps this signal as geometry by converting constraint meshes into tokens and learning a routed attachment inside a frozen denoiser. Each latent region can therefore receive the part of the constraint that matters for its spatial location.
We evaluate Arbor on automatic and artist curated control benchmarks with hull, avoidance, and touch constraints, and compare the metric trends to a user preference study. Even without dedicated compliance losses, Arbor improves constraint obedience while preserving object quality and variation under fixed constraints.

---


### 619. [Collapsed Effective Operators for Higher-order Structures](https://arxiv.org/abs/2606.23517)

**<font color=#1a73e8>作者：</font>** Maximilian Krahn, Lennart Bastian, Vikas Garg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Higher-order structures are powerful relational modeling tools, yet existing spectral operators decompose the topology into separate ranks, leaving practitioners to fuse the information back to vertices through ad hoc choices. We introduce Collapsed Effective Operators, which condense higher-order degrees of freedom into a single vertex-level operator via Schur complementation of a graded Laplacian. This yields a (generally dense) operator that encodes long-range interactions mediated by topology and is applicable to arbitrary higher-order constructs. We show it preserves positive semi-definiteness with a spectral upper bound relative to the rank-0 Hodge Laplacian, effectively lowering system energy under higher-order connectivity. Empirically, our operator improves spectral clustering, signal smoothing, and enables the inclusion of topological features in neural network architectures via positional encoding. The project page can be found this http URL

---


### 620. [Simulation-Free Estimation of Traffic Flows from Sparse Count Data](https://arxiv.org/abs/2606.23536)

**<font color=#1a73e8>作者：</font>** Davide Guastella, Gianluca Bontempi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a method for estimating time-varying traffic flow patterns from sparse aggregated vehicle counts. The method partitions the study area into spatial regions, constructs a set of feasible region-to-region routes, and solves a weighted least-squares optimization problem to determine the number of vehicles to allocate on each route. A weighted contribution matrix encodes sensor coverage, steering the optimizer toward flow configurations that are directly observable by sensors. Edge-level trajectories are then derived by scoring candidate routes against the temporal and volumetric profiles of aggregated regional sensor counts.
The method is evaluated on the Brussels road network using real and synthetic traffic data. Results show that the proposed approach reproduces the daily traffic profile in the input data and outperforms the baseline methods at a fraction of the computational cost.

---


### 621. [AwakeForest: An Interactive Geospatial Platform for Large-Scale Forest Imagery](https://arxiv.org/abs/2606.23542)

**<font color=#1a73e8>作者：</font>** Suraj Prasai, Kangning Cui, Rongkun Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forest imagery analysis often involves multiple tightly coupled vision tasks, which must be performed under substantial variation in geographic regions, sensors, and acquisition conditions. However, practitioners often lack a unified tool that is geospatial-native, cloud-optimized, and ML-integrated for end-to-end workflows spanning annotation, prediction, visualization, and downstream analysis at scale. We present AwakeForest, an interactive end-to-end platform designed for large-scale forest imagery that integrates model-assisted inference, automatic annotation, and human-in-the-loop refinement within a single workflow. Our platform supports plug-and-play integration of pretrained models and enables scalable interaction with forest imagery ranging from standard aerial scenes to large orthomosaics that can span several gigabytes to hundreds of gigabytes. AwakeForest produces analysis-ready outputs that can be directly used for downstream analysis and to support iterative model and annotation updates on new scenes. We demonstrate the system on the PALMS dataset and illustrate how AwakeForest supports an end-to-end workflow for practical forest management and analysis.

---


### 622. [Dense Reward for Multi-View 3D Reasoning with Global Maps and Local Views](https://arxiv.org/abs/2606.23557)

**<font color=#1a73e8>作者：</font>** Jiho Choi, Seonho Lee, Seojeong Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view 3D Visual Question Answering (MV3D-VQA) requires integrating partial observations into a coherent 3D scene representation and selecting informative viewpoints for multi-step spatial reasoning. However, current multimodal LLMs are typically trained with sparse, answer-level supervision, which often yields inconsistent cross-view reasoning and brittle view selection. We present DR-MV3D (Dense Reward for MV3D-VQA), a map-grounded learning framework that provides dense, verifiable rewards to supervise the reasoning process. Our approach decomposes MV3D-VQA into (i) allocentric global map construction, (ii) question-conditioned view-trajectory planning, and (iii) egocentric grounding for answer prediction. To make intermediate steps learnable without manual annotations, we introduce two rewards: a global consistency reward that aligns the predicted map with geometry-consistent pseudo targets from frozen 3D vision foundation models (e.g., VGGT + SAM3), and a local trajectory reward that supervises ordered viewpoint selection. We optimize the full pipeline with trajectory-level policy optimization (GRPO). Experiments on MindCube, VSI-Bench, and BLINK (MV) show that DR-MV3D consistently improves over strong multi-image baselines, supporting the effectiveness of process-level dense supervision for multi-view 3D reasoning.

---


### 623. [LangMAP: A Language-Adaptive Approach to Tokenization](https://arxiv.org/abs/2606.23566)

**<font color=#1a73e8>作者：</font>** Clara Meister, Suchir Salhan, Andrzej Szablewski 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-specific tokenizers improve tokenization quality and the downstream performance of models on those languages. However, using such a tokenizer comes at a cost: either a new model must be trained from scratch, or the vocabulary of an existing pretrained model must be adapted. We propose Language-adaptive Maximum a Posteriori (LangMAP) Tokenization, a tokenization scheme that extends the UnigramLM algorithm to the multilingual setting, producing language-specific tokenization from a single shared vocabulary. Notably, LangMAP can be used when training a multilingual language model from scratch or to adapt a pretrained model's tokenizer to individual languages without changing its vocabulary. While language labels are required at training time, a key feature of the algorithm is that it then performs language-specific tokenization at inference without knowledge of the input's language. Across 14 open-source tokenizers, 9 natural languages, and 9 programming languages, LangMAP improves morphological boundary alignment and, for all coding languages tested, alignment with abstract syntax tree (AST) leaf boundaries. In fine-tuning experiments, results are mixed: LangMAP improves target-language grammatical acceptability (MultiBLiMP) on the languages tested; its benefits are less consistent on knowledge-related tasks (Global-PIQA, Belebele).

---


### 624. [Patient-Aware Contrastive Learning Preserves Per-Patient Structure in RR-Interval Representations](https://arxiv.org/abs/2606.23570)

**<font color=#1a73e8>作者：</font>** Yasantha Niroshana, Weijith Wimalasiri, Chathuranga Hettiarachchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive representation learning struggles on physiological signals when each subject contributes a distinct baseline pattern. If class differences overlap with subject differences,class-level objectives such as supervised contrastive learning tend to merge per-subject structure into a single per-class cluster,removing the individual variation that a model needs to generalize to unseen patients. We study this problem in the setting of Paroxysmal Atrial Fibrillation(PAF) detection from RR-interval(RRI) sequences and propose a patient-aware contrastive objective that forms positive pairs only from same-patient, same-class segments, preserving each patient's own sinus rhythm(SR) baseline while still pushing the two classes apart. Examining the learned embeddings directly, our objective achieves the most consistent per-patient SR structure (cohesion $0.850$ vs. $0.800$ for supervised contrastive loss (SupCon) and $0.772$ for binary cross-entropy (BCE)). We also identify that BCE produces the cleanest global class separation yet the most disordered per-patient structure. This is precisely why a linear probe trained on its features breaks down on unseen patients. On the IRIDIA-AF dataset, the resulting representation reaches a patient-independent Area Under the Receiver Operating Characteristic Curve (AUROC) of $0.989 \pm 0.003$ with $2.6\times$ lower seed variance than supervised contrastive this http URL results highlight that per-subject geometric consistency, rather than global class separability, is key to robust cross-patient generalization.

---


### 625. [A Spectral Theory of Normalized Corrected GNN Propagation](https://arxiv.org/abs/2606.23572)

**<font color=#1a73e8>作者：</font>** Qihan Chen, Wei Li, Meng Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a spectral theory for \emph{normalized corrected GNN propagation}. The object of study is the symmetric normalized adjacency with its degree-stationary component removed, matching the normalization used by standard GCN-style models while isolating the stationary direction most directly tied to oversmoothing. The central theoretical question is whether this corrected normalized operator preserves class-discriminative signal after many propagation layers. Our main result is a high-probability exact-recovery theorem for the binary Contextual Stochastic Block Model after \(k=O(\log n)\) propagation steps in the dense polylogarithmic regime \(p\ge C\log^B n/n\), for any fixed \(B>4\), under explicit graph-signal and feature-SNR conditions. We also establish a multi-class partial recovery theorem showing contraction toward class centers for most nodes. Synthetic and real node-classification experiments are included as empirical checks of the theory's predicted dependence on depth, graph signal, and feature noise.

---


### 626. [A Watermark for Vision-Language-Action and World Action Models](https://arxiv.org/abs/2606.23574)

**<font color=#1a73e8>作者：</font>** Yule Liu, Shuai Liu, Jiaheng Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models and world-action models (WAM) are the generative models now driving general-purpose robot control, turning raw camera input directly into motor commands. They are increasingly deployed as black-box services, where a partner runs the policy through an interface while the owner keeps the weights private. Training such a model takes proprietary data and heavy computational power, making the deployed model itself a valuable intellectual property.
To address this, we propose the \emph{keyed latent-provenance verification} method, which fingerprints the policy through the seed of the Gaussian noise vector that the models draw before generation. At the injection stage, the owner swaps this seed for a keyed one with the same distribution as ordinary noise, so the fingerprinted actions are statistically identical to those of an ordinary run and an adversary watching the output finds no signal to detect or remove. At the verification stage, the owner runs the suspect model under authorized access and records the action channels the robot executes, a partial and possibly post-processed view of the policy's output. From this view, the verifier recovers the seed by gradient-based maximum a posteriori (MAP) optimization, tests it for the secret key to score each rollout, and aggregates these scores into a single decision on whether the suspect model belongs to the owner.
We evaluate the method on two representative models across two robot suites. The experiments cover detection of the fingerprint, identification of which of several keys a suspect carries, robustness to a range of attacks, and an analysis of why the design works. Across both models, the fingerprint can be detected reliably with little change to task performance, and it remains detectable under output-side removal attacks and weight-level edits.

---


### 627. [Solve for the Hyperparameter, Skip the Search: Kolmogorov-Optimal Scaling Laws for Spline Regression](https://arxiv.org/abs/2606.23575)

**<font color=#1a73e8>作者：</font>** Yong Yi Bay, Kathleen A. Yearick  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperparameter tuning almost always means search: fit the model at every value on a grid, score each by cross-validation, and keep the winner. For spline regression that search is unnecessary. The optimal resolution can be solved for in closed form, to the accuracy an exhaustive search reaches, at a fraction of the compute. Three ingredients make this possible: classical approximation theory pins the squared bias to a known power of the resolution G, exactly the Kolmogorov n-width of the smoothness class; the basis dimension is an explicit polynomial in G; and leave-one-out error follows from a single fit via the PRESS identity. Balancing the two known curves gives the minimizer analytically. We extend this calculus to many coordinates by replacing ambient input dimension with interaction order, the number of active low-order components in an ANOVA decomposition, yielding a scaling law in which the optimal resolution and error are power functions of the effective density (sample size per active component), with input dimension absent from the exponent. The law becomes an algorithm. KORE (Kolmogorov-optimal Order-aware Resolution Estimation) fits two pilot resolutions, solves a leverage-calibrated 2x2 system for the bias and noise scales, and evaluates the closed-form plug-in resolution with a tiny leave-one-out certificate: about a dozen fits instead of a full grid sweep, with a consistency guarantee as the sample grows. Across additive and sparse pairwise targets up to 80 input dimensions, KORE matches exhaustive 3-fold cross-validation and the full classical ladder (GCV, Mallows' Cp, AIC, BIC) while fitting roughly 8x fewer models; on 36 real tabular datasets it ranks first among 21 methods in accuracy per unit of compute, ahead of tuned boosters and kernel machines. When complexity lives in low interaction order, solving for the resolution beats searching for it.

---


### 628. [Decentralized Autonomous Traffic Management through Corridor Networks](https://arxiv.org/abs/2606.23585)

**<font color=#1a73e8>作者：</font>** Jasmine Jerry Aloor, Aadarsh Govada, Hamsa Balakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As autonomous aircraft are introduced at scale and traffic density increases, centralized management becomes insufficient to coordinate the large numbers of crewed and uncrewed aircraft. Dedicated Advanced Air Mobility (AAM) corridors have therefore been proposed for organizing high-density autonomous traffic flows. The desire to scalably provide autonomous aircraft flexibility in trajectory planning motivates the development of decentralized approaches to traffic management in AAM corridors.
In this work, we extend a multi-agent reinforcement learning (MARL) approach to address the challenge of decentralized traffic flow management in air corridor networks. We test policies trained in a single-corridor setting on increasingly complex multi-corridor networks with combinations of merges and splits in a zero-shot manner. Experimental results demonstrate that learned behaviors transfer well to scenarios with varying traffic density, network geometry, and heterogeneous vehicle performance, without needing centralized coordination or model retraining. We evaluate system-level performance in terms of conformance to corridor boundaries, completion rates, average speeds, distance traveled, and maintenance of inter-aircraft separation. We find that although our policies require only locally coordinated entry, traversal, and exit behaviors, they collectively produce desirable traffic flows through the corridor network.

---


### 629. [It's Much Easier for Neural Networks to learn Game of Life Dynamics with the Right Activation Function: Polynomial Kolmogorov-Arnold Networks](https://arxiv.org/abs/2606.23587)

**<font color=#1a73e8>作者：</font>** Tashin Ahmed, Q. Tyrell Davis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Previous work has found a gap between the scale of neural networks that reliably learn Conway's Game of Life, and minimal networks capable of representing the classic cellular automaton with hard-coded parameter values. Viewing neural network learning as a search process suggests a dependence on networks large enough to contain sub-networks with lucky initializations (sometimes known as 'winning tickets') that actually learn the task. In this work, we reorient our perspective from discovering Life rules as a search problem back to a learning problem, and reason that with fitting inductive biases, the problem should be much more amenable to minimal networks. We find that network variants with several alternative activation functions meaningfully outperform the default choice of Rectified Linear Units, and in particular, that a 2nd degree polynomial activation function consistently learns Life dynamics with or without the benefit of learning neural weights. Our results provide an informative demonstration of the benefits of matching learning to the task at hand and challenge the easy default choice of scale for all problems. In particular, we advocate for the use of cellular automata as simple test domains for developing strategies that can benefit machine learning for science, physics-based deep learning, and interpretable machine learning.

---


### 630. [SPIRAL: Learning to Search and Aggregate](https://arxiv.org/abs/2606.23595)

**<font color=#1a73e8>作者：</font>** Jubayer Ibn Hamid, Ifdita Hasan Orney, Michael Y. Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model reasoning can be substantially improved at test time via scaffolds that scale inference compute across different primitives -- sequential reasoning within a trace, independently sampled parallel traces, and aggregation of multiple reasoning traces into a final response. During post-training, however, language models are optimized only for sequential reasoning within a single trace. We introduce Sequential-Parallel-Aggregative Reinforcement Learning (SPIRAL), a framework in which a language model is trained to use all three primitives, as part of a unified inference compute pipeline. Concretely, the language model first samples a set of independent traces in parallel, each produced through sequential chain-of-thought reasoning, and then generates a final aggregation trace conditioned on those traces; all components are optimized end-to-end against the reward of the final aggregated response. To train this system, SPIRAL uses set reinforcement learning to teach models to produce a set of traces that are collectively useful for an aggregator and standard reinforcement learning to teach models to aggregate the set into improved final responses. Our experiments on reasoning tasks show that SPIRAL effectively scales with inference compute, outperforming GRPO by up to 11$\times$ scaling efficiency and 15% higher performance when all three compute primitives are scaled.

---


### 631. [Against Proxy Optimization](https://arxiv.org/abs/2606.23597)

**<font color=#1a73e8>作者：</font>** Sven Neth  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> I discuss conditions under which maximizing a proxy utility function is harmful and suggest this poses problems for applying decision theory.

---


### 632. [MORL-A2C: Multi-Objective Reinforcement Learning Reranker for Optimizing Healthiness in MOPI-HFRS](https://arxiv.org/abs/2606.23603)

**<font color=#1a73e8>作者：</font>** Aarya Vasantlal, Joshua Zolla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unhealthy dietary behavior continues to be a persistent public health issue in the United States, exacerbated by recommendation systems that prioritize user preference without considering nutritional health. The Multi-Objective Personalized Interpretable Health-aware Food Recommendation System (MOPI-HFRS), from which this work extends, addresses this by jointly optimizing preference, health, and diversity through Pareto-based optimization. However, this approach relies on static, per-step tradeoff solutions that fail to capture the sequential nature of dietary decision-making. We introduce MORL-A2C, a sequential decision-making extension to MOPI-HFRS targeting the health-preference axis. Leveraging frozen GNN embeddings, MORL-A2C formulates recommendation as a K-step reranking problem using an Advantage Actor-Critic algorithm with a scalarized relevance/health reward. The policy is warm-started via behavior cloning against a dot-product ranker derived from frozen embeddings. We also identify and correct a non-trivial bug in the MOPI-HFRS evaluation pipeline that understated baseline performance; all results are reported against the corrected baseline. On the macro-nutrient benchmark, MORL-A2C achieves a modest reduction in ranking quality (Recall@20: 25.64% to 23.61%, NDCG@20: 23.52% to 20.64%) in exchange for a substantial improvement in health alignment (H-Score@20: 46.05% to 69.57%), with consistent trends on the full-nutrient benchmark. These findings validate that policy-driven sequential optimization can effectively navigate the health-preference trade-off in multi-objective food recommendation.

---


### 633. [Polycepta: Object-Centric Appearance Estimation for Multi-Object Tracking](https://arxiv.org/abs/2606.23604)

**<font color=#1a73e8>作者：</font>** Mohamed Nagy, Naoufel Werghi, Jorge Dias 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The tracking-by-detection paradigm in multi-object tracking (MOT) typically relies on static appearance descriptors to complement motion estimation. However, these descriptors are frame-independent, limiting their robustness as visual cues. Since such descriptors are often obtained from computationally intensive pretrained backbones, real-time MOT systems frequently abandon appearance cues altogether and rely solely on motion prediction and geometric association. In this work, we introduce Polycepta, an object-centric appearance state estimation framework that reformulates appearance modeling as a recursive estimation problem rather than a frame-wise matching task. Polycepta constructs and continuously updates an independent appearance state for each tracked object, enabling future appearance representations to be estimated from accumulated observations. Polycepta is encouraged to learn the appearance-state construction of object-specific representations rather than memorize them through a proposed learning strategy, enabling appearance estimation for unseen classes. A key property of Polycepta is that the quality of appearance estimation improves as object states evolve during inference. While conventional appearance descriptors remain static or degrade over time, Polycepta progressively refines appearance estimates as additional observations are accumulated. Extensive experiments on KITTI, the Waymo Open Dataset, and MOT17 demonstrate consistent reductions in identity switches and improvements in tracking performance when integrated into the tracking-by-detection pipelines. Polycepta operates at 90.57 Hz and delivers state-of-the-art performance on the KITTI benchmark when integrated into the RobMOT framework, achieving a MOTA of 92.27\%.

---


### 634. [Scaling Linear Mode Connectivity and Merging to Billion Parameter Pretrained Transformers](https://arxiv.org/abs/2606.23607)

**<font color=#1a73e8>作者：</font>** Tianyi Li, Zhiqiang Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear mode connectivity (LMC) provides a promising foundation for understanding and merging independently trained neural networks, but existing methods typically optimize the interpolation path from only one model endpoint, limiting their scalability and effectiveness for large pretrained transformers. We propose a novel and scalable framework for enabling LMC-based model merging to {\em billion-parameter pretrained transformers}. Our method applies properly parameterized functionality-preserving weight transformations to align functionally equivalent solutions, and introduces a dual learning procedure in which both models jointly learn their corresponding transformations toward a shared linear interpolation path. This bidirectional optimization substantially reduces interpolation barriers and enables more reliable merging across large-scale architectures. Empirically, we show that our approach achieves near-zero loss barriers on WikiText for language models with medium-sized parameters, representing, to our knowledge, the first demonstration of near-barrier-free linear connectivity at this scale. In the vision domain, ViT-L maintains above 69\% ImageNet top-1 accuracy throughout the interpolation path, while modern billion-parameter LLMs exhibit only small loss barriers. These results suggest that properly resolving parameter symmetries enables large pretrained Transformers to be connected and merged through simple linear paths with substantially improved interpolation performance. Code: this https URL .

---


### 635. [Causal Discovery in the Era of Agents](https://arxiv.org/abs/2606.23608)

**<font color=#1a73e8>作者：</font>** Yujia Zheng, Vishal Verma, Mantej Gill 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent attempts to combine large language models (LLMs) with causal discovery ask models to infer pairwise directions, propose graph structures, or inject language-model outputs as priors and constraints. These approaches promise faster analysis, but they also obscure whether a causal evidence is supported by data and assumptions or by textual associations, prompt artifacts and hallucinated mechanisms. We argue for a different role for agents in causal discovery. Agents should inspect data, retrieve context, explain method assumptions and clarify graph outputs, but they should not supply edges, orientations, priors, constraints or causal conclusions. We propose the principle that agents assist the workflow, while causal claims remain grounded in data, explicit assumptions, formal algorithms, diagnostics and user or domain-expert decisions. We instantiate this principle in causal-learn+, an online platform that coordinates data analysis, preprocessing, method recommendation, expert-knowledge incorporation, formal discovery and interpretation around the algorithmic ecosystem of causal-learn. A case study on Big Five personality data illustrates agent-assisted pipeline of causal discovery without turning language-model unreliability into causal evidence. The platform is available at this http URL.

---


### 636. [Discovering Latent Groups for Robust Classification](https://arxiv.org/abs/2606.23609)

**<font color=#1a73e8>作者：</font>** Ankur Garg, Ulrich Aïvodji, Samira Ebrahimi Kahou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models exploit spurious correlations, achieving high average accuracy but failing disproportionately on underrepresented subgroups. Existing methods address this by adjusting network parameters, guided either by subgroup annotations or inferred pseudo-group labels. Yet at inference, these methods produce only a class prediction, with no insight into a sample's latent subgroup. We propose neural classification trees (NCT), a framework that achieves robustness by encoding subgroup structure in its tree-shaped architecture. By routing each sample to an "easy" or "hard" node of this tree -- based on prediction correctness -- and reusing these routes as pseudo-labels for the next iteration, NCT disentangles conflicting subgroups, without requiring subgroup supervision. We evaluate NCT on five benchmarks spanning binary and multi-class spurious correlations. Our experiments show that the learned tree topology provides strong interpretability by consistently isolating minority subgroups, which provides a transparent mapping between the model architecture and the data's latent group structure, while yielding competitive robustness with state-of-the-art methods.

---


### 637. [Vera: A Layered Diffusion Model for Content-Preserving Video Editing](https://arxiv.org/abs/2606.23610)

**<font color=#1a73e8>作者：</font>** Hongkai Zheng, Ta-Ying Cheng, Benjamin Klein 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models have enabled remarkable progress in video generation and editing. However, content preservation remains a core challenge: existing methods regenerate every pixel and often alter elements that should remain unchanged, such as characters or background scenes. We introduce Vera, a layered diffusion framework for content-preserving video editing. Instead of regenerating the entire video, Vera generates an edit layer along with an alpha matte for compositing with the source video, separating creative editing from content preservation by design. To encourage coherent composition with the source video, we extend the text-to-video DiT into a Mixture-of-Transformers (MoT) architecture, with separate DiTs for each layer that interact through joint self-attention. To support the training of Vera, we further construct a high-quality layered dataset with accurate alpha mattes, diverse scenes and dynamics, and visual effects. Across our quantitative benchmark and human preference study, Vera outperforms leading open-source video editing models in content preservation while remaining competitive in edit quality, using 486K frames of layered training data.

---


### 638. [Data Selection Through Iterative Self-Filtering for Vision-Language Settings](https://arxiv.org/abs/2606.23611)

**<font color=#1a73e8>作者：</font>** Andrei Liviu Nicolicioiu, Sarvjeet Singh Ghotra, Morgane M. Moss 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The availability of large amounts of clean data is paramount to training neural networks. However, at large scales, manual oversight is impractical, resulting in sizeable datasets that can be very noisy. Attempts to mitigate this obstacle to producing performant vision-language models have so far involved heuristics, curated reference datasets, and using pre-trained models. Here we propose a novel, bootstrapped method in which a CLIP model is trained on an evolving, self-selected dataset. This evolving dataset constitutes a balance of filtered, highly probable clean samples as well as diverse samples from the entire distribution. Our proposed Self-Filtering method iterates between training the model and selecting a subsequently improved data mixture. Training on vision-language datasets filtered by the proposed approach improves downstream performance without the need for additional data or pre-trained models.

---


### 639. [Hedgementation = Hedgerow Segmentation: A Remote Sensing Benchmark](https://arxiv.org/abs/2606.23615)

**<font color=#1a73e8>作者：</font>** Nathan Senyard, Salem Hamdani, Astrid Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Hedgementation: a new benchmark to evaluate machine learning models for hedgerow mapping from remote sensing data at country scale and 10m$^2$ spatial resolution. We combine and harmonize multiple remote sensing data products and ground truth labels sourced from a hedgerow inventory in France. We measure the ability of three baseline models to generalize across spatial distance, and across climatic zones, a more explicitly challenging task. Our benchmark tests both supervised and self-supervised learning approaches for remote sensing, applied to tracking fine-scale features of high agricultural importance. The code to reproduce the benchmark and baselines results is available at this https URL.

---


### 640. [DiT-Reward: Generative Representations for Text-to-Image Reward Modeling](https://arxiv.org/abs/2606.23626)

**<font color=#1a73e8>作者：</font>** Yuanming Yang, Guoqing Ma, Bo Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can representations learned for image generation also support the evaluation of generated images? We study text-to-image reward prediction as a downstream task of generative representation learning. To this end, we introduce DiT-Reward, which converts a pretrained text-to-image Diffusion Transformer into a reward model by processing near-clean image latents and aggregating text-conditioned image representations across transformer layers. Under the same training data mixture as HPSv3, DiT-Reward outperforms HPSv3 on all four evaluated preference benchmarks, reaching 85.6% on HPDv2 and 77.6% on HPDv3. When the generative backbone is frozen, a lightweight learned head can still extract meaningful preference predictions from its representations. Probing across depth further reveals that downstream reward performance is strongest in the middle-to-late layers and benefits from combining representations across different stages. We also observe consistent positive scaling with generative backbone capacity. Finally, when used to optimize Stable Diffusion 3.5 Large with Flow-GRPO, DiT-Reward outperforms HPSv3 along the matched training trajectory, with particularly clear gains in realism. Direct latent scoring also achieves a 1.65x inference speedup over HPSv3 with comparable peak memory. These results show that pretrained generative DiTs provide transferable representations for reward modeling and policy optimization.

---


### 641. [AI-driven Optimisation of Quality of Recovery (QoR) in Remote Patient Monitoring](https://arxiv.org/abs/2606.23631)

**<font color=#1a73e8>作者：</font>** Yansong Liu, Li-Hsi, Pramit Khetrapal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Remote patient monitoring depends on patient-reported data to capture the subjective dimension of recovery that devices cannot measure. The Quality of Recovery (QoR-15) survey is the gold-standard instrument for this purpose. It was designed and validated for occasional in-hospital assessment, yet remote monitoring now administers it to patients daily. In our own post-surgical deployment, only 55% of patients submitted the survey more than 14 days of 30 monitoring days. We developed QoR-compact, a five-item daily input for the RPM prediction pathway. Setting a deployment-driven target of one-third of the daily items, we exhaustively evaluated all 3,003 five-question subsets of the QoR-15 and tested whether the best of them matches the full instrument in predicting near-term postoperative recovery severity. QoR-compact achieves a mean AUC-ROC of 0.968 (95% CI 0.915-0.988), statistically comparable to the 0.964 baseline obtained with one-third of the items. Patient-level backtesting indicates that it tracks readmission events as faithfully as the full form. Its five items span the physical and psychological axes of recovery: Q3 (feeling rested), Q9 (feeling comfortable and in control), Q10 (general well-being), Q12 (severe pain), and Q14 (feeling worried or anxious). The QoR-15 remains the gold-standard measure of recovery; QoR-compact complements it as a shorter daily input designed for prediction. This parity provides the basis for a prospective study of whether a lighter daily input is, in turn, completed more consistently. External validation on larger cohorts is required before clinical use.

---


### 642. [AI Exposure Scores: what they measure, what they miss, and what comes next](https://arxiv.org/abs/2606.23633)

**<font color=#1a73e8>作者：</font>** Campbell Lund, Thomas Euyang, Zanele Munyikwa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A set of exposure scores calculated in 2023 has become a central empirical input to the future of work debate. Produced by Eloundou et al. (2023) and referred to here as the GPTs are GPTs scores, they define exposure as the share of occupational tasks a large language model can assist with. This work is a genuine methodological contribution, but as the scores travel from the time and place they were produced, the limitations the authors named do not always travel with them. Two gaps have widened as a result. The first is structural, between what static exposure scores measure and what policy questions actually require. Taking the diffusion of these scores as a case study, we show how their temporal, geographic, and ontological limitations compound in policy-facing analyses, and we survey five families of research responding to these limits: dynamic and benchmark-based measures, ensemble methods, task-framework extensions, worker-centered metrics, and adoption and usage data. The second gap is the one we argue needs more attention: the coordination between researchers and policymakers. The policy-relevant work which ask who is harmed, who benefits, how, and when, continues to reference the static GPTs are GPTs scores without engagement with the methodological updates that would let these questions be answered more reliably. We then ask what additional steps towards navigating uncertainty remain: ex-post frameworks and the deliberate, political work of reimagining what futures are worthy of building towards are. Closing the research-policy gap is a shared task: policymakers must widen their evidence base, engage workers as epistemic partners, and shift from prediction to preparedness; researchers must build data infrastructure, adopt participatory methods, and write with policymakers in mind. Better measurement matters, but it will not close the second gap alone.

---


### 643. [Pose Anything Anywhere:Model-free Object Poses from Arbitrary References](https://arxiv.org/abs/2606.23634)

**<font color=#1a73e8>作者：</font>** Hongli Xu, Jiaqi Hu, Junwen Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating the 6D pose of unseen objects is a fundamental yet challenging problem for open-world robotics and embodied perception. Model-based methods are accurate but depend on CAD assets or heavy onboarding, while most model-free approaches are still limited to pairwise single-anchor matching and thus fail under occlusion and large viewpoint changes with low query-reference overlap. Therefore, we present PANY, a unified model-free framework that seamlessly supports both RGB and RGB-D inputs, operates on one or sparse pose-free reference views, and generalizes effectively to novel objects. Built on a multi-view transformer geometry backbone, PANY moves beyond pairwise matching by learning view-consistent geometry and cross-view alignment cues that remain stable under wide baselines and limited overlap. When additional unposed assist views are available, PANY aggregates them via pose-graph canonical registration to increase geometric coverage and reinforce the final pose. Extensive experiments show that PANY achieves state-of-the-art performance across multiple benchmarks, substantially outperforming existing model-free methods, improving pose accuracy by +12% on YCB-V and over +20% on LM-O. Furthermore, PANY consistently performs well under both single-reference and sparse-reference settings, demonstrating strong robustness in real-world environments.

---


### 644. [Muown Implicitly Performs Angular Step-size Decay](https://arxiv.org/abs/2606.23637)

**<font color=#1a73e8>作者：</font>** Florian Hübler, Kai Lion, Antonio Orvieto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix-aware optimizers such as Muon and Muown have recently shown strong empirical performance for pre-training Transformers. In particular, Muown separates each weight matrix into row magnitudes and an un-normalized direction variable, updating the former with Adam and the latter with Muon. We show that the directional update of Muown is equivalent to a Riemannian step on the normalized directions, while the magnitude of the un-normalized parameterization only modulates the angular step size. This explains the step-size stability of Muown and suggests making the angular step size explicit. The resulting method, AngularMuown, optimizes directly over the normalized directions and uses a schedulable angular multiplier decoupled from the radial magnitude update. AngularMuown improves over Muown and, at the time of writing, a preliminary version is leading the per-optimizer category of the modded nanoGPT speedrunning competition. Further experiments on Qwen2-0.5B, and 1.1B parameter mixture-of-experts models confirm the algorithm scales beyond small models. An implementation of the algorithm is available at this https URL

---


### 645. [Learning Process Rewards via Success Visitation Matching for Efficient RL](https://arxiv.org/abs/2606.23640)

**<font color=#1a73e8>作者：</font>** Raymond Tsao, Andrew Wagenmaker, Sergey Levine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many modern applications of reinforcement learning (RL), the natural reward for a task of interest is inherently sparse: a reward of 0 is given everywhere except when the task is completed, when a reward of +1 is given. Training a policy to maximize such a sparse reward requires solving a challenging credit assignment problem, leading to slow or ineffective RL improvement. We propose a simple approach to transform a sparse outcome reward into a dense process reward. Our approach relies on training a discriminator to distinguish between previous successful and unsuccessful episodes, and using this discriminator to incentivize the RL-learned policy to match the state-action visitations of successful episodes, while avoiding those of unsuccessful episodes. By incentivizing the policy to match the visitations over all states, not just those that correspond to task success, this reward provides dense feedback on whether progress is being made towards task completion, and, we show, provably achieves this without changing the optimal policy. Focusing on finetuning of robotic control policies, we demonstrate that our approach leads to significantly faster RL finetuning performance on both simulated and real-world manipulation tasks, as compared to simply maximizing the sparse outcome reward.

---


### 646. [Lightweight Neural Framework for Robust 3D Volume and Surface Estimation from Multi-View Images](https://arxiv.org/abs/2606.23653)

**<font color=#1a73e8>作者：</font>** Diego E. Farchione, Ramzi Idoughi, Peter Wonka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate volume and surface area estimation is critical for diverse applications, from marine ecology to medical diagnostics. However, existing methods often suffer from high computational costs and poor performance with sparse and noisy data. We propose a fully feed-forward framework that regresses scale-normalized volume and surface area and their associated uncertainties directly from multi-view images. By fusing 3D point cloud reconstructions with view-aligned 2D features through a graph-based decoder, our model bypasses iterative optimization, ensuring exceptional scalability and rapid inference. Experimental results demonstrate that our approach outperforms state-of-the-art methods, particularly when operating with a low number of input images. Validated across coral monitoring, dietary analysis, and anthropometry, our proposed framework provides a robust, adaptable solution for quantitative shape analysis. This architecture provides a high-speed, scalable alternative for precise geometric estimation from visual data, maintaining high performance even in resource-constrained or sparse-view scenarios.

---


### 647. [EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions](https://arxiv.org/abs/2606.23654)

**<font color=#1a73e8>作者：</font>** Jincheng Zhong, Weizhi Wang, Che Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise agents increasingly operate inside workspaces: they read heterogeneous files, invoke tools, and deliver business artifacts. We introduce EnterpriseClawBench, an enterprise agent benchmark constructed from proprietary, real-world agent sessions. Starting from a large archive of workplace sessions, the EnterpriseClawBench produces 852 reproducible tasks, each paired with recovered fixtures, rewritten prompts, role classes, skill subclasses, hard rules, and semantic rubrics. Because the sessions contain internal enterprise content, we do not release the benchmark data; instead, our reusable contribution is the construction and evaluation protocol. On EnterpriseClawBench, the best configuration reaches only 0.663 (Codex with GPT-5.5). These results show that enterprise agent evaluation must report harness--model combinations, artifact delivery, visual quality, cost, runtime, and skill-transfer behavior, rather than collapsing performance into a single score. Code: this https URL

---


### 648. [Dynamic estimation of slowly varying sequences](https://arxiv.org/abs/2606.23655)

**<font color=#1a73e8>作者：</font>** Prashant Gokhale, Mikhail Khodak, Sandeep Silwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of sequentially approximating functions of each element in a slowly-varying sequence, i.e. one where the magnitude $\alpha_i$ of the difference between the elements at positions $i$ and $i-1$ is small. Recent work on implicit trace estimation shows that when $\alpha_t$ is small, reusing queries to past sequence elements can reduce the overall cost [Dharangutte \& Musco, NeurIPS~2021; Woodruff et al., NeurIPS~2022]. We introduce a framework generalizing this to a variety of linear and nonlinear functions on diverse vector spaces, obtaining novel sequential estimation results for matrix powers, spectral densities, Monte Carlo integration, and a boundary value problem from partial differential equations~(PDEs). Furthermore, we develop a novel algorithm for use with this framework that locally scales the estimation budget with $\alpha_t$, obtaining sharper path-length-style variation bounds of form $\mathcal O(\sum_{i=1}^m\alpha_i)$ on the cost of estimating a sequence of length $m$. This improves upon the previous implicit trace estimation bound of $\mathcal O(m\cdot\max_i\alpha_i)$ [Dharangutte \& Musco, NeurIPS~2021], which is achieved by fixing the query budget using the worst-case $\alpha_i$ and is thus inefficient for stable sequences with rare bursts. Lastly, while all past work assumes a known bound on $\alpha_i$, we show in certain cases how the changes can be estimated on-the-fly with (nearly) no added cost. In summary, our framework makes the sequential approximation toolkit general-purpose and adaptive while improving upon state-of-the-art-guarantees for dynamic trace estimation.

---


### 649. [GeoFidelity-Bench: Evaluating Segment-Level Geographic Fidelity in Text-to-Image Street-View Generation](https://arxiv.org/abs/2606.23669)

**<font color=#1a73e8>作者：</font>** Kaizhen Tan, Hanzhe Hong, Siru Tao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models can generate visually plausible city streets, but whether their outputs correspond to a requested road segment rather than a generic city prior remains unclear. We introduce GeoFidelity-Bench, a reference-panel benchmark for segment-conditioned geographic fidelity in street-view generation. It contains 7,117 curated Mapillary images covering 109 named OpenStreetMap road segments in 25 cities across six continents. For each generated panel, the benchmark ranks the target reference panel against panels from the nearest segment in the same city, other segments in the same city, and segments from other cities, making local discrimination rather than absolute target similarity the primary test. We evaluate six open-weight text-to-image generators under city-only, street-and-neighborhood, and GPS-augmented prompts. Adding street and neighborhood names is associated with an increase of 5.5 percentage points in top-1 retrieval accuracy over city-only prompts, with a 95% confidence interval from 3.4 to 7.7 percentage points. However, the similarity margin between the target and the nearest segment in the same city remains near zero, indicating that local names improve broad local plausibility more than exact segment identity. Prompts that keep the city fixed but use incorrect street or neighborhood names further show that only part of the gain depends on the correct local names, while appending raw GPS coordinates as ordinary text yields no statistically clear additional benefit. Held-out real-image queries successfully recover segment identity, showing that the curated references contain usable segment-level signal. GeoFidelity-Bench thus reveals a persistent gap between city- or neighborhood-plausible street-view generation and faithful generation for a specific road segment.

---


### 650. [PsyBridge: A Hybrid Intelligent Framework for Multi-Dimensional Mental Health Assessment and Decision Support](https://arxiv.org/abs/2606.23673)

**<font color=#1a73e8>作者：</font>** Sunil Wanjari, Manish Thakre, Aayushi Asole 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mental health assessment commonly relies on isolated screening instruments or data-driven models that often lack interpretability and multi-dimensional integration. Existing approaches frequently focus on individual indicators such as depression or anxiety while providing limited support for comprehensive and explainable decision-making. To address this limitation, this study proposes PsyBridge, a hybrid intelligent decision-support framework designed for multi-dimensional mental health assessment through the integration of clinically validated screening tools, cognitive evaluation, and personality profiling within a unified architecture. The proposed framework incorporates PHQ-9 and GAD-7 assessments alongside cognitive and behavioural indicators using a modular design and a weighted aggregation mechanism to generate interpretable mental health risk classifications and recommendations. To evaluate the framework, a semi-synthetic dataset consisting of 500 patient profiles representing varying severity levels was constructed based on clinically grounded score distributions. Experimental results demonstrate that PsyBridge achieves an overall accuracy of 0.84, outperforming standalone PHQ-9 and GAD-7 assessments while improving precision, recall, and F1-score. Sensitivity analysis and ablation studies further indicate that integrating cognitive and personality components contributes to more stable classification performance and reduces inconsistencies in moderate-risk prediction. The findings suggest that PsyBridge provides a scalable and interpretable approach for AI-assisted mental health decision support, particularly within digital healthcare and telehealth environments.

---


> [!TIP]
> 当前位于：**601-650**（第 13/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
