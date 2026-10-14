# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-550**（第 11/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 501. [Barycentric Guidance: Turning Foundation Image Editors into Continuous Affective Controllers](https://arxiv.org/abs/2610.16892)

**<font color=#1a73e8>作者：</font>** Harvey Mannering, Zhiwu Huang, Adam Prügel-Bennett  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotions are expressed on a continuum and are naturally described in the valence-arousal (VA) space. Existing VA-based image editors are typically training-based and domain-specific, limiting them to VA regions seen during training and making them brittle across datasets and domains. Meanwhile, despite producing high-quality edits, state-of-the-art foundation image editors are not continuous affective controllers: non-linear emotion representations in text encoders makes prompt interpolation poorly calibrated, so accurate and continuous VA control remains unreliable. To fill this gap, we introduce Barycentric Guidance, a training-free framework that turns pretrained foundation image editors into continuous affective controllers over VA, requiring no finetuning, extra data, or model changes. Our method maps any target VA point to simplex-based guidance weights, enabling VA controllability in three aspects: (i) accurate targeting of VA states, (ii) broad coverage across the VA plane, and (iii) continuous control. Across three face datasets, we improve VA target accuracy by 25-29%, expand VA-plane coverage by 28-50%, and increase expression diversity by 29-49%, over the strongest baseline. Unlike prior domain-specific methods, our training-free approach exploits the foundation model's inherent versatility, enabling generalization beyond human faces to animals, artworks, and complex scenes within a single framework. Code is available at this https URL.

---


### 502. [Neural Bayesian Networks for Modular and Scalable Decision-Making Under Uncertainty](https://arxiv.org/abs/2610.16902)

**<font color=#1a73e8>作者：</font>** Giovanni Briglia, Marco Lippi, Stefano Mariani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bayesian Networks (BNs) are established tools for letting agents reason under uncertainty in sequential decision-making. They split a joint distribution into local conditional mechanisms arranged on a directed acyclic graph, which makes them modular, interpretable, and ready to perform probabilistic inference. Their classical formulation, however, has limitations in both expressiveness and scale: each conditional is usually stored as a table or a linear-Gaussian form, and inference evaluates the graph one node and one query at a time.
In this paper we introduce Neural Bayesian Networks (NBNs), in which each conditional is a differentiable, tensor-valued mechanism, while the graph and its factorization are unchanged. NBNs retain the modularity and local mechanisms of BNs, can represent any learnable conditional distribution, and run natively on GPUs. We also release NBN, a PyTorch-based library for learning and inference in NBNs, together with a public benchmark. Our evaluation shows gains in both expressiveness and scale: NBNs fit distributions that classical BN libraries struggle to represent, and on large networks and large batches of queries they run two orders of magnitude faster thanks to GPU parallelization. NBN is available at this https URL.

---


### 503. [Mining Cross-Modal Perception Gaps in Autonomous Driving: When Camera and LiDAR Disagree](https://arxiv.org/abs/2610.16906)

**<font color=#1a73e8>作者：</font>** Hongsen Cao, Mona Jaber, Shanxin Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal fusion for 3D object detection assumes that cameras and LiDAR are broadly complementary. In practice, how much each modality is trusted at a given location is decided by learned weights that are neither characterized nor auditable. We label every ground-truth object by which modalities detected it, then mine the resulting 0.4M-object database across nuScenes, KITTI, and Waymo. Because the patterns shift with distance from the ego vehicle, we read the mined model through Spatially Stratified Feature Attribution (SSFA), which conditions Shapley attribution on distance zones and exposes structure that global attribution averages away. Three assumptions built into the current fusion design do not hold. The modality-preference boundary tracks the object itself: a traffic cone is nearly six times as likely as a truck to be seen by the camera alone (16.8% vs. 2.9%), regardless of range. Camera-only detections peak at 10-30 m, inside the band usually ceded to LiDAR, and fall away on either side. The drivers of failure are not additive either: the distance - density interaction alone outweighs the entire main effect of viewing direction. We further find that modality dominance is directionally non-stationary, with objects behind the vehicle being markedly more LiDAR-dominant than those in front. We compile the mined structure into a Modality Reliability Map and inject it into four pretrained fusion detectors through a lightweight attention layer. This improves performance by up to 1.3 mean Average Precision (mAP) while fine-tuning under 4% of their parameters in 2-3 GPU-hours. Our work lifts reliability out of the weights and treats it as a quantity that can be examined before deployment. That is what a safety measure for multi-modal perception must rest on.

---


### 504. [ConDenseDrive: Knowledge-Dense, Token-Sparse Visual Encoder for End-to-End Autonomous Driving](https://arxiv.org/abs/2610.16908)

**<font color=#1a73e8>作者：</font>** Shengzhen Li, Yongkang Li, Hao Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end driving requires rich spatiotemporal representations to support scene understanding and trajectory planning under strict latency constraints. However, most systems initialize their visual encoders from generic image pretraining and densely process all patch tokens for each camera view and input frame, limiting both representation quality and inference efficiency. To address these challenges, we present ConDenseDrive, a knowledge-dense and token-sparse visual encoder for end-to-end autonomous driving. Our three-stage framework first makes the encoder knowledge-dense by distilling complementary visual, semantic, and geometric knowledge from three vision foundation models. It then adapts the distilled encoder to multi-frame end-to-end driving and integrates spatiotemporal context into register tokens for planning. Finally, it makes the encoder token-sparse by applying register-guided token compression, reducing redundant patch computation and yielding a 2.0$\times$ speedup while improving planning performance. ConDenseDrive achieves 94.5 PDMS on NAVSIM v1 and 90.8 EPDMS on NAVSIM v2, and reaches 37.4 HD-Score in zero-shot evaluation on HUGSIM. Extensive experiments and qualitative analyses demonstrate that visual encoder design provides an effective route to reliable and efficient end-to-end driving.

---


### 505. [Transparent Information Flow Modeling for Role-Aware AI Act Assessment](https://arxiv.org/abs/2610.16916)

**<font color=#1a73e8>作者：</font>** Mattias Brännström, Themis Dimitra Xanthopoulou, Lili Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The European Union's Artificial Intelligence Act introduces a structured framework for governing high-risk AI systems, emphasizing transparency, risk management, and role-specific accountability. However, current assessment practices often rely on monolithic system views or disconnected checklists, limiting their ability to capture the socio-technical complexity of real-world deployments. We explore the use of the Information Flow Methodology (IFM), a modeling-based approach to AI Act compliance assessment. IFM represents decision systems -- whether algorithmic, human, or hybrid -- as networks of information sites and transformation channels, enabling structured analysis of how information, decisions, and responsibilities flow across organizational and technical boundaries. We apply IFM in a real-world case involving a recruitment support tool used by a public-sector organization, evaluating both the Provider's system and the Deployer's recruitment process. Our results demonstrate that IFM can serve as a scaffold to bridge both component-based and holistic perspectives, and how technical systems are situated within socio-technical contexts. In doing so, IFM supports transparency, identifies risk pathways, and enables alignment analysis between intended and actual use. We argue that such modeling provides a foundational tool for effective, context-sensitive AI governance and accountability -- offering capabilities beyond conventional checklist-based assessments.

---


### 506. [Security and robustness analysis of encrypted communications for local home automation: ESPHome Native API and MQTT over TLS 1.3](https://arxiv.org/abs/2610.16928)

**<font color=#1a73e8>作者：</font>** Carlos Roberto Gonzalez-Escarpeta, Juan Eduardo Garcia Sanchez, José Antonio Hernandez Reyes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The expansion of the Internet of Things (IoT) in residential and local automation environments has highlighted the limitations of considering the internal network as an inherently trusted domain. Man-in-the-middle (MitM) attacks, such as ARP spoofing, can allow traffic interception or manipulation when communications lack appropriate confidentiality, integrity, and authentication mechanisms. This paper presents a systematized review of the security mechanisms used by two communication alternatives between ESP-family microcontrollers and the Home Assistant platform: MQTT protected through TLS 1.3 and the ESPHome Native API, whose encryption is based on the Noise Protocol Framework using the Noise_NNpsk0_25519_ChaChaPoly_SHA256 pattern. The analysis considers four dimensions: cryptographic robustness, attack surface, implementation complexity, and resource consumption. The review identifies significant differences resulting from the architecture and cryptographic model of each alternative. TLS 1.3 provides a standardized framework compatible with public-key infrastructure and formal identity management, though it introduces greater configuration complexity and computational overhead during session establishment. The ESPHome Native API employs a more specialized scheme with lower operational complexity, eliminates dynamic algorithm negotiation, and uses ChaCha20-Poly1305. The resource-consumption analysis relies on measurements published by the projects and manufacturers themselves, not on an experimental test bench, and this limitation is explicitly acknowledged. The results identify the conditions under which each mechanism is appropriate for local home-automation architectures and provide a basis for designing IoT systems that balance security, interoperability, and resource constraints.

---


### 507. [Making Tensor Decoupling More Robust and Less Parametric](https://arxiv.org/abs/2610.16937)

**<font color=#1a73e8>作者：</font>** Maxime Rochkoulets, Joppe De Jonghe, Mariya Ishteva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensor decoupling algorithms recover compact representations of multivariate functions by combining linear factor matrices with univariate internal nonlinearities. We identify two limitations of recent methods. First, their performance is not invariant to mismatched output or gradient magnitudes, and second, their spline internals require manual tuning of their degrees of freedom. We propose two lightweight fixes. The first is a preprocessing step that rescales the input Jacobian tensor, removing both the bias towards larger magnitude outputs and the ill-conditioning of certain factor updates caused by such a mismatch. The second replaces B-spline internals by penalized splines coupled with generalized cross-validation, making the method less dependent on the user selecting the right number of control points. Finally, we release an efficient open-source JAX implementation of our algorithm.

---


### 508. [KNN Implementation Details Can Dramatically Change Performance: An Example from Cover Trees](https://arxiv.org/abs/2610.16940)

**<font color=#1a73e8>作者：</font>** Amol Khanna, Edward Raff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nearest neighbor search algorithms are widely used and have a long history, but we find that key implementation details are seldom reviewed in articles about them. These details can materially impact performance, and thus change the conclusions one makes about a given algorithm's superiority. In this article, we highlight these impacts by reviewing the Cover Tree as an example, producing RustKNN, a unified Rust implementation of three construction variants of the Cover Tree with three query modes. Our analysis reveals: (1) the optimal query strategy depends on $k$ and on the dataset (single-tree search is fastest at $k{=}1$ on three of our four largest datasets, while dual-tree search is fastest at $k{\ge}5$ on the three largest), and choosing the wrong query mode can cost up to a $7.5\times$ factor in runtime; (2) the cover tree base parameter, set to 2 in theory and 1.3 in practice, is not a safe default for dual-tree search: 1.3 is optimal on only one of seven datasets, and on covtype it is $1.6\times$ slower than the optimum; (3) among five micro-optimizations, only early-exit distance computation has a consistent effect, and that effect grows with dimension (none at $d{=}32$, $1.31\times$ at $d{=}54$, and $1.49\times$ at $d{=}784$); and (4) all-nearest-neighbor and held-out benchmarks yield different implementation rankings. All main timing tables report medians over 20 independent allocations with bootstrap 95% confidence intervals. RustKNN is open source at this https URL.

---


### 509. [Learning to Design Convex Relaxations for Nonconvex Optimization](https://arxiv.org/abs/2610.16948)

**<font color=#1a73e8>作者：</font>** Jinrun Liu, Bai Yan, Tengfei Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Convex relaxations make nonconvex optimization tractable by replacing hard nonconvex problems with convex surrogates that give valid bounds. Yet their design is still largely manual: a human expert must decide where to relax, which relaxation to use, and how much formulation growth is worth paying. We show that this design process can be learned. The method proposed in this paper, AutoConvexRelax, represents the symbolic formulation of a nonconvex problem as a tripartite graph linking variables, symbolic terms, and their objective or constraint positions. It then learns a policy that composes symbolic rewrites into problem-specific relaxation trajectories as the formulation evolves. We prove that finite action sequences generated by the learned policy preserve relaxation validity under explicit domain, occurrence-context, and representation-consistency conditions. We further establish computable error bounds for mixed relaxations and sufficient conditions for feasible recovery and global-optimality certification. As a first instantiation, we apply the method to nonconvex quadratic problems and fractional problems. On 241 benchmark quadratic instances, the learned policy strengthens McCormick lower bounds by 13.52%. Its mean lower bound is 3.70% below strengthened semidefinite relaxations on the normalized comparison metric, while it uses substantially smaller formulations. The learned policy retains this trade-off on fractional instances and reaches near-semidefinite bounds on beamforming and sensor-network localization instances. These results suggest that convex relaxation design can move from a fixed handcrafted choice to an automated learning process that adapts to problem structures. Code is available at this https URL.

---


### 510. [DiTSG: Context-Aware Air Traffic Scene Generation with Multi-Agent Diffusion Transformers](https://arxiv.org/abs/2610.16959)

**<font color=#1a73e8>作者：</font>** Seokbin Yoon, Kyungmin Kim, Taejung Kwon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Understanding how many aircraft, and which traffic configurations, can be safely and efficiently managed by air traffic controllers within a given airspace is fundamental to air traffic management. Air traffic controllers continuously modify aircraft trajectories through interventions such as speed advisories and radar vectoring, and the patterns of these interventions are difficult to capture effectively using existing air traffic simulators. To address this limitation, we propose Diffusion Transformers for Traffic Scene Generation (DiTSG), which learns to generate air traffic scenes from recorded multi-aircraft trajectories. DiTSG employs stacked multi-agent inverted Transformer layers as the denoising backbone of a diffusion transformer, jointly generates the trajectories of multiple aircraft within a traffic scene, and conditions the generation on agent-specific required times of arrival. The resulting trajectories generated by DiTSG preserve realistic inter-aircraft interactions observed in actual air traffic operations. Experiments show that the DiTSG generates diverse traffic scenes that reproduce the statistical properties of recorded traffic while preserving realistic inter-aircraft interactions.

---


### 511. [Proactive Physical AI through Continuous Observation and Timely Intervention](https://arxiv.org/abs/2610.16967)

**<font color=#1a73e8>作者：</font>** Zhenhua Yang, Jiafeng Liang, Xingyu Zhou 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical AI is commonly formulated around an explicitly specified task: given a goal or instruction, a system perceives, reasons, and acts. In many real-world settings, however, important tasks emerge from continuously changing world states before a person explicitly formulates them. We study this complementary problem as Proactive Physical AI, where an AI system continuously observes the physical world, identifies situations that warrant intervention, and initiates appropriate actions at the right time. We develop ProAgent, an end-to-end system built around two components: a Jev-style proactive timing model (dubbed StreamingJev) that determines whether and when intervention is needed, and a Response Model that generates responses for people or invokes available device capabilities for physical execution. To support learning at scale, we develop an automated data pipeline that converts videos into supervision for proactive timing. Experiments demonstrate strong proactive performance under both explicit objectives and standing roles, combining more accurate intervention timing with fewer false triggers than the source-backbone baseline. Real-robot evaluations further demonstrate ProAgent's ability to identify emerging needs and translate them into appropriate physical actions.

---


### 512. [PRAISE: A Reproducible Workflow for Non-Programmer Scientists to Implement Published AI Models](https://arxiv.org/abs/2610.16980)

**<font color=#1a73e8>作者：</font>** Max Achterweust, Stefan Groot Nibbelink, Vincent J. de Beer 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) models are increasingly developed, published and used across scientific fields. Researchers, students and industry professionals who want to apply these models to their own research questions often lack the programming and data science expertise to do so. Existing guidelines cover single steps, but not the route from a published model to working predictions on one's own data. Here we present the hands-on workflow PRAISE, a Practical, Reproducible AI-model Implementation for Science and Education, that helps non-programmers implement published AI models step by step. Because implementations rarely work the first time, PRAISE anticipates common failures and provides a fallback route for each. As a proof of principle, three BSc chemistry students and their tutor applied PRAISE without prior programming or data science knowledge. They reproduced, validated and extended a state-of-the-art model that predicts enzyme-substrate interactions. This shows that with PRAISE, implementing an AI model from the literature becomes a learnable skill, one that turns non-programmer scientists from users into evaluators and improvers of AI models.

---


### 513. [Predicting Mental Health Help-Seeking Behaviour on Reddit: A Survival Analysis of Linguistic and Behavioural Signals](https://arxiv.org/abs/2610.16983)

**<font color=#1a73e8>作者：</font>** Nisar Ahmed, Ammara Kazmi, Irtaza Bashir Raja 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most prior work on predicting mental health help-seeking treats it as post-hoc classification of users already active in clinical communities, which cannot tell whether someone approaching a transition can be identified in advance. We instead frame help-seeking as a time-to-event problem and ask which Reddit users will eventually seek mental health support, and how imminent that transition is. We build a two-arm cohort: a control frame of 6,337 ordinary users with genuine right-censoring (12.1% transition rate) to answer who will transition, and a clinical frame of 5,023 eventual transitioners to answer how soon. Features come only from posts written before any clinical activity, and user-grouped five-fold cross-validation plus a four-year temporal holdout guard against leakage. We compare TF-IDF, MentalBERT embeddings and behavioural activity features using Cox proportional hazards models, Random Survival Forests and an LSTM sequential model. Behavioural features alone outperform text for predicting who will seek help (C-index 0.797 vs. 0.763), and combining both is best (0.823 under cross-validation, 0.856 on the holdout). The pattern reverses for predicting how soon a known transition will happen: text remains a stable predictor (C-index 0.698) while behavioural features become unstable. Structural engagement patterns therefore carry information about future help-seeking beyond linguistic content, and separating who from when yields a cleaner analysis.

---


### 514. [From Suboptimal to Optimal: One-Step Latent Flow Policies for Offline Reinforcement Learning](https://arxiv.org/abs/2610.16984)

**<font color=#1a73e8>作者：</font>** Shenghua Lu, Zixuan Yang, Rongxu Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning aims to learn effective policies from fixed datasets without environment interaction. Although generative models such as diffusion and flow matching enhance policy expressiveness, they typically start from uninformative Gaussian noise and generate actions through multi-step iteration, leading to high computational costs and failing to effectively leverage suboptimal trajectories in datasets. We propose MeanFlow2Better (MF2B), which reformulates offline RL as generative decision chunk optimization from current performance status to better performance status in a high-level latent decision space. MF2B maps trajectory chunks to high-level latent decision representations through an encoder, placing generation starting points within a structured decision space sculpted by behavioral data. The model learns a shared conditional mean velocity field in this space, constructing two flow mappings: from Gaussian-Induced Decision Sources toward positive behavioral decision regions, and from suboptimal decisions toward high-value decision regions. Both flow mappings complete decision refinement through one-step ODE integration over the unit time interval $\Delta t=1$, requiring neither multi-step iterative sampling nor backpropagation through time. Furthermore, we propose hierarchical chunk-level advantage to guide the flow direction toward high-return regions, where the high-level decisions cover multiple low-level actions, leading to sequence length compression from $T$ to $K \approx T/H$ and significantly lower computational overhead. On the D4RL Gym-MuJoCo benchmark, MF2B achieves an average score of 90.91, matching or surpassing strong baselines.

---


### 515. [Self-Supervised Learning of Semantically Consistent Visual Features via a Simple 3D Prior](https://arxiv.org/abs/2610.16988)

**<font color=#1a73e8>作者：</font>** Sebastian Day, Oisin Mac Aodha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual features extracted from vision models like DINOv2 or Stable Diffusion enable high quality semantic correspondence between images. However, such features exhibit documented limitations that hinder accurate correspondence estimation such as the inability to disambiguate the left from right for categories exhibiting symmetries or repeated parts. Previous attempts to improve these features rely on using supervised data such as annotated keypoint pairs or camera pose information, or make restrictive topological assumptions, such as modelling the object of interest as a 3D sphere. We introduce a new self-supervised approach that allows us to learn features for topologically complex object categories using a simple prior. Instead of relying on an expensive instance-level analysis by synthesis pipeline, our approach makes use of contrastive learning and distribution matching at the global dataset-level to learn the coarse shape and appearance of a category. Combined with additional geometric losses, this enables us to replicate the global and local statistics of visual features which match those that are extracted from real images. Quantitative results are presented across several challenging object categories, demonstrating the effectiveness of our approach.

---


### 516. [Generative Models as Adaptive Trust Regions for Discrete Bayesian Optimisation](https://arxiv.org/abs/2610.16992)

**<font color=#1a73e8>作者：</font>** Michael Dodds, Erik Bodin, Sebastian W. Ober 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimisation (BO) is a powerful framework for sample-efficient optimisation of expensive black-box functions, but its application to high-dimensional discrete scientific design remains challenging. Local trust-region BO methods such as TuRBO address high dimensionality by restricting search to adaptively sized neighbourhoods. However, a direct discrete analogue based on edit distance can be poorly suited to structured discrete objects: neighbourhoods grow combinatorially, and metric proximity does not capture the dependencies that determine whether a design is plausible or useful. Motivated by the growing availability of pretrained generative models, we introduce GenTuRBO, which replaces the geometric trust region with an adaptively scaled proposal distribution defined by a pretrained generator. The generator provides a learned prior over discrete transformations, encoding coordinated changes without explicitly enumerating edit-distance neighbourhoods. GenTuRBO performs strongly across all three domains and achieves the highest mean final scores on Ehrlich sequence optimisation and Sokoban coordination.

---


### 517. [Constant-Depth Rational-Weight GNNs and their Connection to Schanuel's Conjecture](https://arxiv.org/abs/2610.16993)

**<font color=#1a73e8>作者：</font>** Daumantas Kojelis, Carsten Lutz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A landmark result states that the expressive power of graph neural networks (GNNs) is bounded from above by the 1-dimensional Weisfeiler-Leman (1-WL) test. We ask whether a constant-depth GNN can match the expressive power of 1-WL while using only rational weights. We prove that this is the case when Schanuel's conjecture, a famous open problem from transcendental number theory, is taken to be true. Our GNN construction works even with integer weights, and more generally with a broad range of rational weights. As the activation function, it may use logistic sigmoid, hyperbolic tangent, or related functions. It is uniform across all graph sizes. We also prove a partial converse: if a GNN with exponentiation, hyperbolic sine or hyperbolic cosine as activation matches the expressive power of the 1-WL test in a slightly more expressive setting where graphs may contain certain auxiliary vertices, then this implies Schanuel's conjecture restricted to the numbers that arise in computations of the GNN. We also conduct experiments showing that the constructed GNNs indeed match the 1-WL test.

---


### 518. [Intrinsic Geometry Matching: learning observation-equivariant process geometry](https://arxiv.org/abs/2610.16995)

**<font color=#1a73e8>作者：</font>** Manuel Lecha, Michael Bronstein, Iolo Jones  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real data are often arbitrary, indirect observations of an unknown underlying process, and those observations can distort its geometry. Existing geometric methods equip data with the induced geometry of the ambient space, but this entangles the true geometry of the process with the distortion of the observation. To address this, we introduce Intrinsic Geometry Matching (IGM): a scalable approach to learn the intrinsic geometry of the underlying process. Specifically, we learn the carré du champ operator of the process, allowing us to recover its diffusion geometry. Our method uses the fact that data often come with natural perturbations, like steps in a time series, to recover the intrinsic carré du champ while transforming naturally with changes in observation: it is observation-equivariant. Furthermore, since this equivariance relates the geometry of different spaces, we can train a model using additional sources of data, even when that data lies in another space. We evaluate IGM on molecular dynamics, image, and video data and find better performance and scaling than existing neural and graph-based geometric tools.

---


### 519. [A physics-coupled graph neural operator for mid-plane six-component stress tensor field prediction in concrete penetration](https://arxiv.org/abs/2610.16996)

**<font color=#1a73e8>作者：</font>** Wenpu Du, Peng Zhou, Yunlong Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The penetration-resistant design of concrete structures requires the spatiotemporal evolution of the stress field within the target, whereas in design only the strength grade, the geometry and the projectile parameters are known, and the aggregate arrangement is not. Empirical formulae and scalar-output surrogates serve design screening, and mesoscale finite element models resolve the aggregate-scale response, but one solution cannot cover random aggregate samples at scale, and no framework links mesoscale heterogeneity to field-level prediction. A physics-coupled graph neural operator (PC-GNO) is proposed, which learns in function space the evolution of the mid-plane six-component stress tensor field. The training data are generated by full-scale, aggregate-resolved finite element models and comprise 359 cases at the impact velocities of 100, 135 and 165 m/s, corresponding to compressive strengths of 14, 23 and 48 MPa; the data source is verified by laboratory measurements. The coupling strength of message passing is constructed from the impedance contrast across the material interface, and the update is constrained by spectral normalization. Under the single-step primary setting, the mean accuracy of the three levels is 80.16% (91.45%, 77.80% and 71.22%), i.e. 27.81, 42.46 and 34.16 percentage points above the preceding-frame field of the same window; with 20 664 parameters it exceeds the 87.9% of the best Fourier neural operator configuration (about 812 times as many parameters) and the 71.0% of the closed-form linear regression. The output is the complete six-component tensor field rather than a fixed engineering quantity, so that strength criteria and energy indicators follow from one set of weights. For field-level response prediction in concrete penetration, this result provides a data-driven route, with conditions of applicability defined by the training and the evaluation.

---


### 520. [Mixture of GFlowNets](https://arxiv.org/abs/2610.17007)

**<font color=#1a73e8>作者：</font>** Omar G. Younis, Joseph D. Viviano, Chirayu Anant Haryan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative Flow Networks (GFlowNets) learn a policy that samples compositional objects in proportion to an unnormalized reward $R(x)$. This makes them useful wherever many diverse, high-reward candidates are needed and oracle queries are expensive. In practice, a single GFlowNet often fails to cover all modes of a complex distribution, and the obvious ways to scale compute saturate: larger batches and data-parallel gradient averaging draw every trajectory from one, possibly biased, policy, so extra rollouts rediscover known modes instead of finding new ones. We explore whether this mode-bias problem (mode collapse in the extreme) can be addressed with a population of asynchronously trained policies which divide the state space between them. Mixture of GFlowNets (MoG) replaces the single forward policy with a community of $K$ independent GFlowNets coupled through one jointly trained soft classifier, which assigns each member its own region of the state space through reward shaping. Mixing the members under their learned partition functions provably recovers the target $p(x)\propto R(x)$. MoG exchange (MoGX) also lets the classifier route sampled trajectories: a trajectory the classifier assigns to another member is sent to that member and trained on there, with no importance sampling. We evaluate both methods by keeping the environment-interaction budget fixed while scaling the community size, turning parallel compute into mode coverage without extra oracle calls. On HyperGrid, across six reward landscapes and communities of up to $K{=}64$, MoG and MoGX keep finding new modes as $K$ grows, while data-parallel training saturates. On a genomic ideotype-design task, MoGX covers $39%$ of the $1024$ optima at $K{=}64$, against $31\%$ for independent agents and $20\%$ for data-parallel training. MoG also has a lower per-iteration synchronization cost than data-parallel training.

---


### 521. [MAGNET: Manifold-Aware Graph Diffusion Network for Connectome Generation](https://arxiv.org/abs/2610.17014)

**<font color=#1a73e8>作者：</font>** Protyay Dey, Ayush Roy, Hyuna Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Functional brain connectome represents neural connectivity as a matrix of pairwise interactions between brain regions. Generation of functional connectomes is not only a question of validity; rather, having satisfied the constraints on the correlation matrix, the next step is to recover the class-conditional geometry buried under coarse labels. We propose MAGNET, a Manifold-Aware Graph Diffusion Network which uses a normalized-Cholesky representation of the manifold of correlation matrices that guarantees validity. MAGNET lifts noisy latent states into ROI-level region tokens and performs denoising with a relational inductive bias over brain atlas regions. To deal with structural problems induced by coarse labels, MAGNET employs class-anchored conditioning, amortized structural bridge, and relevance-preserving corruption. Across ABIDE, ADNI, and OASIS-3, MAGNET consistently achieves favorable results compared to previous manifold-aware approaches, demonstrating improvements of 7-21% in class-conditional fidelity ($\alpha,\beta$-F1) across three cohorts and better sampling efficiency. Moreover, while training only with strict binary labels, MAGNET is capable of maintaining clinical heterogeneity through fine substructure of the connectomes in a zero-shot setting, improving subclass covariance alignment ($\lambda$-MSE) by over 30%. These results suggest that geometric validity is a necessary but insufficient condition for clinical utility in connectome synthesis. Moreover, efforts in making the diffusion denoising class-conditional manifold aware finds utility beyond the highly curved brain connectome generation as this is a critical problem in various general settings. The code repository can be found at this https URL.

---


### 522. [DIME: Scaling Facial Representation Learning via Differential Masked Autoencoding](https://arxiv.org/abs/2610.17015)

**<font color=#1a73e8>作者：</font>** Hao Yu, Haoyu Chen, Hui Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling up data and model capacity has driven substantial progress in visual representation learning. However, conventional pretext tasks exhibit diminishing returns on fine-grained facial analysis. We attribute this to a scaling bottleneck: these tasks model each image's appearance and are dominated by identity, pose, and illumination, so subtle within-identity facial differences contribute little to the training signal. We introduce DIME, a differential masked autoencoder for large-scale facial representation learning. DIME builds on a simple observation: two images of the same person share identity-specific appearance, so their difference exposes facial changes. DIME reconstructs both masked images in an identity-matched pair and, through an Explicit Differential Direction Supervision (EDDS) objective, aligns the direction of their reconstructed difference with the true difference, while source isolation makes each reconstruction depend only on its own image. Shared appearance cancels in this difference, and because EDDS ignores magnitude, subtle facial changes count as much as large pose or illumination changes. DIME uses identity labels only to form pretraining pairs, requires no dense annotations, and learns dense facial representations with emergent part-level semantics. We pretrain DIME on 20 million high-resolution facial images consolidated from existing face datasets. DIME's AU detection performance continues to improve as pretraining data scales from 6M to 20M images, with its BP4D F1 increasing by 5.9 points, while MAE gains only 0.5 points on the same subsets. DIME also outperforms specialized facial methods on AU detection, AU intensity estimation, cross-domain anti-spoofing, landmark localization, head pose estimation, face parsing, and face generation.

---


### 523. [ProbabilityBench: Model Evaluation and Calibration with Exact Ground-Truth Uncertainty](https://arxiv.org/abs/2610.17016)

**<font color=#1a73e8>作者：</font>** Yuyang Dai, Yuting Tang, Futoshi Futami 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating model uncertainty on real-world data is challenging because each instance provides only a single observed label, leaving true conditional class probabilities unknown. To address this, we introduce ProbabilityBench, a benchmark that provides exact, instance-level class probabilities across three simulated text-based domains: peer review, covert information transfer, and credit risk. By explicitly defining the full data-generating process for each environment, we analytically compute both exact class probabilities and Bayes error. Furthermore, we provide a theoretical guarantee that rendering these cases into natural-language memos strictly preserves their underlying generative probabilities. This exactness enables direct measurement of reported probability quality via KL divergence. Across 16 evaluated models, most models on the observed cost-quality Pareto frontiers are decision models, including Jev and Perplexity Decider. Finally, ProbabilityBench serves as a meta-evaluation framework, leveraging known ground-truth values to benchmark the accuracy of standard calibration metrics and Bayes-error estimators themselves.

---


### 524. [Understanding Personalization Gains in Whisper](https://arxiv.org/abs/2610.17019)

**<font color=#1a73e8>作者：</font>** Sergei Katkov, Antonio Liotta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whisper-style ASR models provide strong zero-shot transcription, but their residual errors are not evenly distributed across datasets, recording conditions, and metadata-based groups. We study when lightweight low-rank adaptation (LoRA) improves Whisper and whether observed gains require group-specific adapters. Across Common Voice, LibriSpeech, and VoxPopuli, we compare zero-shot Whisper, pooled LoRA, and group-specific LoRA under matched within-group splits. We find that adaptation is not uniformly beneficial: gains are concentrated in difficult Common Voice groups, are consistent on VoxPopuli, and largely disappear on low-error LibriSpeech. Crucially, pooled LoRA often matches, and sometimes clearly outperforms, group-specific LoRA. Gains over zero-shot should therefore be tested against matched pooled adaptation before being interpreted as evidence of personalization.

---


### 525. [CWE-bench: Refocusing Agentic Security from Exploitation to Defense](https://arxiv.org/abs/2610.17020)

**<font color=#1a73e8>作者：</font>** Gonzalo Gonzalez-Pumariega, Ajay Jagannath, Adit Jain 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity evaluations of AI agents have focused largely on offense, yet a working exploit does not show that an agent can make software safe. An attacker needs to exploit only one vulnerability; a defender must find and fix all of them. We introduce CWE-bench, a private benchmark of 120 held-out repository audit-and-repair tasks spanning 73 CWE types, eight languages, and all OWASP Top 10 2025 categories. Agents are given a repository to audit and a description of its threat model, but are not told the weakness, where it occurs, or how many vulnerable sites there are. Each patch must block the exploit while preserving original functionality, as checked by a programmatic verifier. We validated the verifier against a panel of agentic judges, manually reviewing disagreements during development and refining the checks. The best agents reach 68% pass@1 and 81% pass@4. We further conduct analyses showing that (i) agents with the same pass@1 differ widely in retry gains and cost, and (ii) no single agent is best across languages or vulnerability categories, and difficulty varies far more by vulnerability category than by language. As the offensive capabilities of agents improve, CWE-bench provides a broad and rigorous measure of whether their defensive capabilities keep pace.

---


### 526. [Benchmarking Quantum Kernel SVMs for Credit Card Fraud Detection: Performance Realities Under NISQ Constraints](https://arxiv.org/abs/2610.17027)

**<font color=#1a73e8>作者：</font>** Hitanshi Arora, Mohit Swarnkar, Aswani Kumar Cherukuri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detecting credit card fraud is notoriously difficult because fraudulent charges make up less than 0.2% of total transactions. Quantum Machine Learning (QML), particularly Quantum Kernel Support Vector Machines (QSVM), promises richer feature representations by embedding classical data into high-dimensional Hilbert spaces. However, whether this theoretical advantage holds up when managing real-world financial data bottlenecks remains unclear. We designed a controlled benchmark comparing three quantum encodings, Angle, ZZFeatureMap, and IQP against classical models while keeping sample sizes, feature counts, and scaling strictly matched. To handle class skew without corrupting quantum state overlaps, we embedded synthetic minority oversampling (SMOTE) directly into the quantum Gram matrix workflow, raising PR-AUC scores by roughly +0.04 across feature maps. When trained on the full European credit card dataset with 30 features, classical baselines reached a top PR-AUC of 0.983. However, restricting classical models to match QSVM hardware constraints (500 samples, 4 PCA features) dropped their PR-AUC to 0.750. This puts our best quantum result 0.730 PR-AUC using IQP encoding on 150 samples into realistic context. Testing on physical quantum hardware reduced performance further to 0.62 due to CNOT gate errors and thermal noise. Overall, our findings pinpoint two main operational bottlenecks for near-term quantum kernels: the scaling of Gram matrix evaluation and heavy information loss from squeezing features onto small qubit registers.

---


### 527. [SPLICE: Sparse Physics Library Identification and Compositional Expansion](https://arxiv.org/abs/2610.17029)

**<font color=#1a73e8>作者：</font>** Lucas Thil, Jesse Read, Guillaume Doquet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operator splitting composes a library of neural operators, one per physical mechanism, into zero-shot simulators of new equations. Existing approaches, however, require these mechanisms and their labels to be specified in advance. We ask whether a pretrained library can instead be adapted and grown from unlabeled trajectories in which multiple mechanisms act simultaneously. We introduce SPLICE, a framework that discovers operators without mechanism labels on mixture data. The contributions of the candidate operators to each trajectory are inferred by solving a convex optimization problem. A calibrated test then assigns each discovered operator the mechanism it implements. Failure cases are also detectable, when the library lacks the required physics or when mechanisms are insufficiently separable. Across one and two dimensional systems, the discovered operators recover mechanisms from unlabeled mixtures and compose into zero-shot simulators of unseen equations; a frozen library can also grow an operator for physics absent from pretraining, without labels and without forgetting. On Navier-Stokes, the discovered operators compose about as accurately as their supervised counterparts.

---


### 528. [AD4EDU: Benchmarking University Lecture Audio Description across Accessibility Standards, Metrics, and Learner Preferences](https://arxiv.org/abs/2610.17042)

**<font color=#1a73e8>作者：</font>** Psychias Stylianos, Gao Yingqiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio description (AD) aims to enhance the accessibility of visual media for blind and low-vision (BLV) persons. However, in higher education, where slide-based lectures are a default mode of teaching, lecture AD remains largely underexplored. The main reason is that existing production guidelines, evaluation metrics, and benchmark datasets are oriented toward entertainment content and do not transfer to lectures, where ADs must complement the lecturer's speech, resolve deictic references, and fit within narrow pauses. In this work, we propose AD4Edu, consisting of an AD benchmark, AD4Edu-Bench, and a rule-diagnosable evaluation metric, AD4Edu-Eval, for generating and evaluating ADs in higher education. Specifically, we consolidated established accessibility guidance, including WCAG 2.2, the DCMP Description Key, and NCAM's STEM description practices. We further collected silver reference ADs, judge-ordered preference pairs, and pairwise preferences from four BLV raters, and post-trained models with direct preference optimization (DPO) for detailed analysis. Our findings indicate that while the metric reliably detects violations of the standard, ADs that comply with it do not necessarily fulfill the subjective preferences of BLV persons, most notably on description length, underscoring the necessity of active participation of BLV persons in co-designing inclusive AI solutions.

---


### 529. [Neos: Learning to Interleave Search and Visual Reasoning](https://arxiv.org/abs/2610.17043)

**<font color=#1a73e8>作者：</font>** Ekko He, Jack Hong, Shilin Yan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent multimodal deep search agents have advanced tool use and visual content retrieval, yet they still struggle to convert intermediate visual evidence into actionable guidance for subsequent search, limiting their effectiveness in long-horizon settings. To address this gap, we present Neos, a multimodal deep search framework that learns both how to acquire evidence and how to use it to guide subsequent decisions. To make this coupling learnable, Neos constructs training tasks with intermediate visual dependencies while filtering out textual shortcuts, and introduces a lightweight, trainable Multimodal Evidence Interface (MEI) that transforms retrieved content into goal-conditioned observations. At its core, an agent-environment co-evolution procedure treats MEI as a co-adaptive component of this loop. Specifically, reference-guided credit assignment uses verified successful trajectories to localize critical policy errors while preserving credit for useful decisions in failed searches, whereas rollout feedback selects informative local evidence-processing interactions for MEI supervised fine-tuning (SFT). By alternating policy reinforcement learning (RL) with MEI SFT, Neos allows the policy's evolving evidence requests to shape MEI training and the adapted MEI to reshape subsequent observations, closing the loop between evidence acquisition and evidence-conditioned action. Across ten benchmarks, Neos-9B and Neos-35B demonstrate leading performance among specialized multimodal deep-search agents.

---


### 530. [VL-DocIR: A Benchmark for Vision-Based Long Document Information Retrieval](https://arxiv.org/abs/2610.17057)

**<font color=#1a73e8>作者：</font>** Simon Ott, Yufan Chen, Ruiping Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-based document retrieval has improved rapidly, but current evaluation settings still emphasize short documents and single relevant pages. This leaves an important gap between leaderboard performance and realistic long-document retrieval, where the evidence needed to answer a query may span multiple pages or even multiple documents. We present VL-DocIR, a page-level benchmark for evidence-complete visual long-document retrieval. VL-DocIR is built from 29,641 HTML-born documents rendered into 388,548 page images from Wikipedia, arXiv, PubMed, and SEC proxy statements. It contains 271,760 queries across 23 domains and six evidence structures, covering single-page, within-document multi-page, and cross-document evidence configurations. Evidence annotations are grounded to rendered pages and HTML element identifiers, and queries are filtered with a cleaning pipeline targeting clarity, correctness, closedness, and the absence of explicit layout references. We evaluate leading single-vector and multi-vector visual retrievers together with diagnostic retrieval settings such as document-context scoring, query splitting, reranking, and round-robin ensembles. The strongest evaluated configuration reaches 69.3 nDCGAll@10 and 80.6 RecallAll@10 under structure-balanced Macro evaluation, but source- and evidence-structure breakdowns show that cross-document retrieval remains substantially harder than single-page retrieval, and that document-context scoring is especially helpful for within-document multi-page queries. VL-DocIR exposes these failure modes and provides a more demanding target for visual long-document retrieval. The new dataset and code will be made publicly available at this https URL.

---


### 531. [PatientWM: Towards Generalizable Clinical World Models via Unified Patient States](https://arxiv.org/abs/2610.17059)

**<font color=#1a73e8>作者：</font>** Ziwen Kan, Jie Peng, Bo Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical decisions depend on anticipating how a patient's condition will evolve as treatment is adjusted and new evidence becomes available. Existing medical world models capture patient-state evolution, but often define the evolving state around a particular modality or task, limiting reuse as inputs or prediction targets change. These models also retain history through observation sequences or recurrent or latent summaries rather than exposing preceding patient states and clinical actions as an ordered transition context. This distinction matters because similar current measurements may follow different recent changes, treatment exposures, and observed responses. To tackle these limitations, we propose PatientWM, a clinical world-model framework built around a unified patient state and sequential latent history. Availability-aware encoders integrate observations available at each decision time into the patient state, while typed decoders produce task-specific clinical readouts without defining the state around any single target. PatientWM further conditions each next-state prediction on the current state and supplied action together with a bounded, ordered history of preceding latent patient states and clinical actions, preserving recent treatment and response context. Experiments across MIMIC-III, MIMIC-IV, and three external clinical datasets show superior performance in clinical prediction, multi-step forecasting, and action-planning evaluation. Transfer experiments further demonstrate the generalizability of PatientWM's patient state. Together, these results establish its ability to forecast clinical evolution and support planning.

---


### 532. [PerturbBridge: Direct Phenotypic Supervision for Cellular Perturbation Generation](https://arxiv.org/abs/2610.17066)

**<font color=#1a73e8>作者：</font>** Yucheng Yang, Xiaoxiao Sun, Huangqingbo Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual cell models should capture phenotypes induced by specific perturbations. However, image-based models are typically trained and evaluated to match real-image distributions, which alone does not explicitly prioritize perturbation-specific biological responses. Recent approaches add biological signals through reinforcement-learning post-training or inference-time steering, raising a central question: where should biological response information enter the generative pipeline? We introduce PerturbBridge, a stochastic data-to-data bridge model that directly supervises perturbation-specific phenotypes in predicted perturbed images during training. PerturbBridge jointly optimizes bridge regression and differentiable biological response losses, with biological gradients passing through a frozen image encoder. We further introduce perturbation-response evaluations based on downstream classification and retrieval. Across three microscopy benchmarks for perturbation profiling and subcellular imaging, PerturbBridge surpasses CellFlux in biological fidelity, image quality, and sampling efficiency. On BBBC021, mechanism-of-action classification improves by 5.66 and 7.5 percentage points with morphological and learned visual features, respectively. On JUMP and AllenCell, retrieval Hit@10 and Hit@1 improve by 1.77 and 7.15 percentage points, respectively. On BBBC021 and JUMP, PerturbBridge achieves lower FID with 80% fewer model evaluations than CellFlux. Overall, these results show that directly supervising perturbation responses during training improves phenotypic fidelity while enabling efficient cellular image generation. Code is available at this https URL.

---


### 533. [A unified three-branch deep learning framework for automated detection and counting of wildlife in aerial imagery](https://arxiv.org/abs/2610.17067)

**<font color=#1a73e8>作者：</font>** Zeyu Xu, Tiejun Wang, Andrew Skidmore 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automating aerial wildlife surveys requires reliable animal detection, consistent delineation of observation strips, and correction for repeated coverage between successive images. We present a unified three-branch deep learning framework that integrates these tasks through WildSeg, WildMatch and WildDet. WildSeg combines rod segmentation with geometric refinement to delineate counting strips from aircraft-mounted markers. WildMatch uses teacher-student distillation to learn dense image correspondences and identify overlapping survey areas without relying on geolocation metadata. WildDet combines dual-scale detection with feature fusion, density supervision and empty-image gating to support animal detection and counting. We evaluated the framework using oblique aerial imagery of four antelope species from the Great Nile Migration Landscape in South Sudan. WildSeg achieved reliable rod extraction, while WildMatch approached teacher-level accuracy with a substantially lighter and faster model. Both modules maintained high accuracy on resized images, improving processing efficiency. WildDet improved detection performance across all four species and reduced detection-based count MAE, RMSE and mean bias by 21.0%, 4.6% and 27.8%, respectively, relative to YOLO11. By connecting spatial survey constraints with animal detection, the framework provides a practical and computationally efficient approach to processing large aerial image collections for wildlife monitoring and population surveys.

---


### 534. [Think Locally Before Computing Jointly: Efficient Secure Multi-Party Computation via Maximizing Local Processing](https://arxiv.org/abs/2610.17072)

**<font color=#1a73e8>作者：</font>** Mingfei Yu, Chenglu Jin, Giovanni De Micheli  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Secure multi-party computation (MPC) lets parties evaluate a function over private inputs without revealing them. In garbled-circuit (GC) protocols, prior optimization has largely treated the number of non-linear gates, especially AND gates, as a proxy for cryptographic cost, and has focused on minimizing multiplicative complexity. We identify an orthogonal source of savings: a gate need not be garbled when one party knows or can locally compute its inputs; that party can evaluate it outside the secure protocol, even when the gate is non-linear. We introduce ownership-aware optimization for GC-based MPC, which minimizes non-linear gates requiring joint evaluation rather than total non-linear gates. We formalize this objective in a cost model and implement a compiler-integrated, gate-level framework that restructures Boolean circuits to increase party-local computation while preserving secure-computation semantics. The method is automated and general-purpose, and composes with existing multiplicative-complexity optimization. Experiments show that it reduces jointly evaluated computation and improves end-to-end GC performance on circuits with party-local structure, revealing protocol-cost savings missed by conventional GC cost models.

---


### 535. [Nearest Neighbor Functional Curve Completion for Intraday Probabilistic Revisions of Renewable Generation Forecasts](https://arxiv.org/abs/2610.17075)

**<font color=#1a73e8>作者：</font>** Guillermo Terrén-Serrano, Michael Ludkovski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a nonparametric approach that fuses deterministic initial forecasts and a partial realization into a probabilistic forecast using the framework of functional curve completion. Our motivation is to construct intra-day forecasts for renewable energy generation, which is a key operational task in modern power grids. The aim is to combine the day-ahead (DA) forecast and the morning realized generation profile to create trajectories for the rest of the day, quantifying operational uncertainty. Starting with a large database of complete forecast-actual pairs across many assets, we adopt a functional point of view and construct a weighted neighborhood based on similarity metrics for the observed partial curve, the DA forecast, the day, and the geographical location. The selected complete nearest-neighbor curves provide a full predictive distribution, including functional focal envelopes and predictive bands based on functional depth. The hyperparameters governing neighborhood size, distances, and fusion rates are tuned across forecast update times and directly target probabilistic calibration in terms of the predictive probability integral transform. Three case studies using synthetic wind and solar assets, as well as real-life regional wind generation, showcase that our algorithm is able to achieve excellent calibration.

---


### 536. [Scaling Unified Multimodal Models to Long-Horizon Interleaved Generation](https://arxiv.org/abs/2610.17080)

**<font color=#1a73e8>作者：</font>** Ziqiao Peng, Yutao Cui, Wang Lin 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) provide an interface for interleaved text-image generation, where generated visual states can directly inform subsequent reasoning and synthesis. However, existing systems are still primarily demonstrated on short trajectories or simplified visual content. We develop a large UMM natively trained on interleaved multimodal data, with strong capabilities in image synthesis, text rendering, complex composition, and multimodal planning, and study how to extend these native capabilities to substantially longer autoregressive trajectories. The main challenge is that generated images continuously accumulate in context: irrelevant or imperfect visual states interfere with future synthesis, while previously established characters and scenes must still be recovered after long intervals. We introduce a visual-memory framework that maintains persistent visual references, selectively retrieves scene-relevant historical states while preserving the complete semantic history, and uses few-step self-rollout to adapt the model to imperfect generated histories. We further introduce LongMIG-Bench for evaluating long-horizon text-to-multi-image and image-to-multi-image generation. Our model achieves high-fidelity long-horizon interleaved generation with strong character and scene consistency, demonstrating how visual memory can scale native interleaved generation to substantially longer trajectories.

---


### 537. [Particle Selection in Virtual Reality](https://arxiv.org/abs/2610.17094)

**<font color=#1a73e8>作者：</font>** Boaz Keren-Gil, James Gain, Lucia Marchetti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Point-cloud representations of 3D data are used in many fields, from astronomical surveys of galaxies to medical imaging and laser scans of buildings. A task common to all of these is interactive selection: picking out a meaningful subset of points for closer analysis. The data is inherently 3D, yet the traditional workflow uses a 2D mouse on a 2D projection and inherits the limitations of a flat screen. This paper compares Virtual Reality (VR) and desktop environments for 3D particle selection, asking whether VR's six-degree-of-freedom hand interaction yields measurable gains in accuracy, speed, usability, workload and flow. In a counterbalanced within-subjects experiment (N = 34), participants selected 90 target galaxies from a catalogue of 16,816 galaxies, using mouse-driven selection with keyboard camera control on the desktop and a hand-held spherical brush that adds or removes particles in VR. We measured task accuracy, completion time, and three standard questionnaires: the System Usability Scale (SUS), the NASA Task Load Index (NASA-TLX) and the Flow State Scale (FSS). Accuracy was comparable (91.6% VR vs. 93.1% desktop; p = 0.858), but every other measure favoured VR. Tasks were 23% faster (p = 0.001, d = 0.93), usability was higher (SUS 84.6 vs. 54.0; d = -1.78), workload was lower (NASA-TLX 20.4 vs. 34.7; d = 0.90), and flow was higher (FSS 83.2 vs. 70.2; d = -1.23). Because the underlying problem, making a 3D selection through a 2D interface, is not specific to astronomy, we expect the pattern to carry over to point-cloud selection in other fields.

---


### 538. [SEAL-DT: An End-to-End Security Engineering and Assurance Framework for Cross-Domain Digital Twins](https://arxiv.org/abs/2610.17097)

**<font color=#1a73e8>作者：</font>** Iraklis Varlamis, Stelios Zindros, Christos Sardianos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber-physical systems connect physical processes, software, networks and organizations. Securing them requires a clear account of what happened, what was observed, which actions were authorized and what evidence supports each decision. Digital Twin (DT) descriptions often fail to explain how these elements stay consistent, blur the distinction between physical events and uncertain observations, or detach simulation results from their requirements and assumptions. This paper presents SEAL-DT (Security Engineering and Assurance Lifecycle for Digital Twins), a structured approach to building and evaluating secure DTs. It brings entity definitions, process models, deterministic simulations, data contracts, evidence records, automated tests and reproducible results into one connected model. The main contribution is an end-to-end DT security framework, spanning scenario definition, entity/process modelling, simulation, security decision logic, evidence handling, validation and reproducible reporting. Security decisions and simulation results thus trace back to their data, assumptions and requirements. A DT is more than a copy of system state: it states what it can observe, how accurate and current its information is, where it came from and which decisions it may support. We demonstrate SEAL-DT in five scenarios: Car2X protection, passive IoT-device detection, an industrial control surrogate, lawful acquisition in a smart home, and medical-IoT monitoring that preserves continuity of care. Each includes formal models, deterministic and negative experiments, uncertainty analyses, schema-valid fixtures, technical reports and verified manifests, testing multiple configurations under normal and adverse conditions. Results show that the framework supports consistent model construction, traceable execution and comparable internal validation, and that security findings link to observable evidence.

---


### 539. [Contrastive learning for video reuse detection](https://arxiv.org/abs/2610.17098)

**<font color=#1a73e8>作者：</font>** Tristan J.B. Cann, Arjun Biswas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The incorporation of footage from other sources has long been a concern from a copyright perspective, as such usage can harm the interests of rights holders. Recent trends in the ``remixing'' of social media content and the development of bespoke stock libraries for specialist causes mean that methods to identify content reuse will have a range of applications. In this paper, we develop a framework based on a Siamese network fine tuned using contrastive learning to identify potential sources for key frames in a given video. This framework makes two contributions to analysis of large video datasets. Firstly, we demonstrate its utility at reducing complex video data to a set of key visuals typically less than 10\% of the size of the full set. Secondly, we show that these reduced sets allow for efficient and effective identification of component footage. We test this method over a set of videos compiled from a stock footage library and demonstrate its effectiveness for constituent video identification with average accuracy greater than 0.95.

---


### 540. [Masked Diffusion for Travel Diaries Synthesis](https://arxiv.org/abs/2610.17109)

**<font color=#1a73e8>作者：</font>** Pascal Jutras-Dubé, Raziq Zaman, Fabian Bastin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Because household travel surveys combine household characteristics, variable-length person rosters, vehicle rosters, and trip chains, existing synthesis pipelines split them across separate models or flatten them into cropped fixed-length vectors. Representation, rather than modeling, becomes the bottleneck: splitting severs cross-segment dependence, and cropping truncates the household-structure distribution. We instead tokenize the diary and keep the object whole: each household-day becomes one token sequence with count tokens for vehicles, persons, and trips, and distinct symbols for padded, hidden, unobserved, and inapplicable positions. We introduce DiaryBridge, a masked diffusion model that bridges the fully hidden sequence to the distribution of complete diaries by unmasking positions in any order. One trained model, conditioned on any observed subset, performs synthesis and partial-diary completion alike. Experiments on real data extracted from the 2017/2018 Regional Travel Survey of the Baltimore region show that DiaryBridge generates travel reflecting vehicle availability and employment status, recovers shared trips using other household members' observed diaries, and better reproduces aggregate demand across modes, purposes, and departure periods than the learned baselines.

---


### 541. [Calibrated Typed Decisions for Entity, Relation, and Event Extraction](https://arxiv.org/abs/2610.17113)

**<font color=#1a73e8>作者：</font>** Yang Wang, Hanlin Xiao, Yanan Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Information extraction models often perform well on the datasets they are trained on, but transferring to new domains and annotation guidelines remains challenging. Supporting user-specified types alone does not resolve this problem. We present CalOn, a unified 0.6B-parameter encoder for entity, relation, and event extraction across datasets and schemas. The model jointly encodes text and type definitions, then directly identifies entity spans, relations between spans, and event triggers and arguments. Its extraction decisions consider the requested types together, using their combined evidence to identify relevant candidates before assigning a type. This gives all three tasks a common probabilistic formulation while keeping every extracted mention anchored to the input text. We train on diverse sources, and supplement supervised learning with a reward that encourages correct extractions and penalises incorrect ones. Across 40 benchmarks, CalOn outperforms the evaluated baselines on most benchmarks. It leads all reported relation extraction benchmarks and achieves the highest average F1 for event triggers and arguments with gold triggers. The same model also performs strongly on aspect sentiment triplet extraction and pronoun resolution through its span-pair formulation. A correction for the probability bias introduced during training improves confidence estimates for entities, relations, and event arguments after calibration, with little change in F1.

---


### 542. [Gluing Local Contexts into Global Meaning: A Sheaf-Theoretic Decomposition of Transformer Representations](https://arxiv.org/abs/2610.17117)

**<font color=#1a73e8>作者：</font>** Bryce Grant, Peng Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing interpretability tools do not test whether a representation keeps the same content when only the phrasing changes. We treat each paraphrase pair as a local witness that two activations should agree and build a cellular sheaf over the paraphrase graph; its Laplacian $L_\mathcal{F}$ answers the question on a frozen model with no training. The kernel $H^0$ is a content subspace: at 20 dimensions it beats the preserved subspace of the concept eraser LEACE on held-out CounterFact fact retrieval across eight architectures by a mean $+17.1$\,pp, and constraining all paraphrases of a fact jointly adds a further $+6.5$\,pp. The spectral complement concentrates causal influence: ablating the most paraphrase-variable coordinates, a coordinate-wise proxy for it, changes model outputs $5.6$ to $26.5\times$ more than ablating coordinates of matched per-coordinate variability, across nine models from 124M to 13B parameters. Stacking layers into a grid creates $b_1 = N(L-1)$ algebraic 1-cycles, and the resulting model-derived harmonic mass varies by nearly three orders of magnitude across six architectures and ranks them as their steering fragility does (Spearman $\rho = 0.90$, exact one-sided permutation $p = 0.014$). The same paraphrase graph yields the content subspace, the influence directions, and the fragility measure. Project page: this https URL

---


### 543. [Can Rényi Accountants Beat Lossless Accountants for DP-SGD?](https://arxiv.org/abs/2610.17120)

**<font color=#1a73e8>作者：</font>** Jinho Bok  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent frameworks in differential privacy (DP), such as privacy loss distributions and $f$-DP, provide lossless representations of the privacy leakage of mechanisms. These approaches are often considered to yield tighter $(\varepsilon, \delta)$-DP guarantees than those obtained from relaxed notions such as Rényi DP. But is that always the case? We study this question for differentially private stochastic gradient descent (DP-SGD) with fixed-size batches under replace adjacency. Our key observation is that in this setting, privacy accounting based on Rényi DP can use a pair of worst-case distributions (i.e., a dominating pair) that differs from the one used in the lossless frameworks. In particular, we characterize the worst-case distributions as two-dimensional Gaussian mixtures and derive an improved Rényi DP bound for DP-SGD. Numerical and asymptotic comparisons show that across various hyperparameter settings, a Rényi DP accountant based on the new bound can yield better privacy guarantees than those obtained from the lossless frameworks.

---


### 544. [Who is the 'I' in AI? Establishing Decentralized Identity and Accountability for Autonomous Agents](https://arxiv.org/abs/2610.17126)

**<font color=#1a73e8>作者：</font>** Ahammod Munim Ramil, Khalid Al Kafi, M. A. Abdullahis Sany 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of autonomous AI agents in decentralized ecosystems challenges existing identity paradigms. While human identity is traditionally anchored in biological and/or self-asserted attributes and government credentials, AI agents lack a standardized definition of selfhood, creating critical gaps in trust and accountability. This paper introduces a novel framework for establishing Decentralized AI Identity rooted in Self-sovereign identity (SSI) principles. We propose a formal model that clearly distinguishes human users and AI agents, enabling distinct verification logic for each class while maintaining a unified identity calculus. The central to our contribution is the ABCD Framework, a multi-layered approach to agent identification and verification: (A) Algorithmic Fingerprint, which binds the identity to static model architectures and provenance; (B) Behavioural Fingerprint, which verifies dynamic performance metrics over time; (C) Cryptographic Identity, which anchors the agent via Decentralized Identifiers (DIDs) and (D) Delegation, which cryptographically binds agent actions to respective human accountability. By orthogonalizing these dimensions, we model how systems can enforce granular trust policies ranging from simple authentication to complex liability assignment, thereby solving the black box identity problem in the autonomous economic activities of AI agents.

---


### 545. [EgoProbe: Benchmarking Long-Range and Exact Memory in Streaming Egocentric Videos](https://arxiv.org/abs/2610.17128)

**<font color=#1a73e8>作者：</font>** Haokai Pang, Yuqian Fu, Yifei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video provides a continuous first-person record of everyday activities, making it a natural foundation for wearable AI assistants. Unlike offline video understanding, streaming systems must process observations as they arrive, while queries may refer to experiences from the distant past. Recent work has begun to explore whether information can be recalled across long temporal gaps. Yet remembering how far is only part of the challenge: recurring objects, actions, and locations also require models to remember exactly which detail belongs to which event. We introduce EgoProbe, a benchmark that evaluates streaming egocentric memory along these two complementary dimensions: long-range retention, i.e., how far, and event-specific recall under interference, i.e., how exact. Built on long-form egocentric videos, EgoProbe uses an event-grounded data engine to extend recall intervals, identify related events, and construct event-grounded distractors, followed by human verification. It contains two subsets: EgoProbe-Base, which evaluates long-range recall without intervening related events, and EgoProbe-Echo, which challenges models with similar intervening events and event-grounded distractors. EgoProbe-Echo adopts coarse-to-fine multi-turn probing: the first turn evaluates coarse-grained event recall, while the second tests whether the model can retrieve the target-specific detail associated with the designated event. Extensive evaluation across diverse models reveals substantial limitations in long-range recall, with further challenges in recovering target-event details among related experiences. Even when models correctly answer coarse-grained questions, they often fail to recall the specific details of the designated event. EgoProbe exposes this underexplored failure mode and provides a testbed for advancing long-range and exact memory in streaming egocentric video understanding.

---


### 546. [Masked Attention Pooling Is Invariant to Padding and Permutation: A Formal Proof in Lean](https://arxiv.org/abs/2610.17132)

**<font color=#1a73e8>作者：</font>** Yusuf Khaled Sadek, Enes Yilmaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention-based multiple instance learning (MIL) pools a variable-size bag of instance embeddings into one vector. In batched training, bags are padded to a common length, and the pooled output is expected not to depend on how much padding was added or on the order in which instances are stored. This expectation holds only if padded rows are removed from both the numerator and the softmax normalizer. Common implementation idioms meet it only under side conditions. Zeroing padded features alone does not work. Masking logits with $-\infty$ fails on empty bags and on nonfinite padding. Masking with a large negative constant is exact only after floating-point underflow. We define masked attention pooling with a guarded normalizer and prove in Lean 4 with mathlib that it is invariant under any bijective reindexing of rows and under appending any finite number of masked rows with arbitrary real features and logits. We also prove that values at masked positions are irrelevant and that an all-masked bag maps to zero. The theorems hold for arbitrary finite index types and feature dimensions. Using the jax-lean certificate pipeline, we connect these theorems to the Jaxpr traced from the JAX kernel itself. Lean checks translation certificates for two concrete shapes, identifies the generated functions with the generic specification, and transfers both invariances to the imported Jaxpr's real-arithmetic semantics. All audited theorems depend only on Lean's three standard axioms. The results concern ideal real arithmetic. Floating-point execution, XLA, and the JAX tracer and importer remain outside the proof.

---


### 547. [MARS: Systematic Multi-Level Acceleration for World Action Models](https://arxiv.org/abs/2610.17141)

**<font color=#1a73e8>作者：</font>** Zengyuan Zuo, Yongchang Zhang, Guangyu Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) have emerged as a promising alternative for embodied intelligence by jointly predicting future world states and robot actions. However, their heavy visual encoding and iterative generative inference incur substantial latency, limiting their applicability to high-frequency closed-loop control. Existing training-free acceleration methods typically optimize a single stage, yielding limited speedups or degraded control under aggressive reuse. In this work, we systematically profile the inference overhead of WAMs and observe abundant redundancy across Transformer computation, diffusion denoising, and consecutive policy queries. However, the safe removal of such redundancy depends strongly on its impact on action prediction and control sensitivity. Based on these observations, we introduce \textbf{MARS}, a training-free and plug-and-play framework for multi-level WAM acceleration. MARS selectively removes low-impact attention computation, adaptively accelerates diffusion inference according to motion granularity, and speculatively reuses predicted future visual representations across consecutive queries with online verification. Together, these complementary mechanisms provide remarkable acceleration while limiting approximation error. Extensive experiments across LIBERO, LIBERO-PRO, and RoboCasa show that MARS achieves up to $4.00\times$, $3.94\times$, and $2.10\times$ end-to-end speedups, respectively, while maintaining task success rate close to the original policy. Moreover, MARS generalizes across different model backbones and across simulation and real-robot experiments, substantially improving the efficiency--performance trade-off of WAM inference. Our code is available at this https URL.

---


### 548. [ModRes: A modification of the ResPlan dataset ready for floor plan analysis and graph machine learning](https://arxiv.org/abs/2610.17178)

**<font color=#1a73e8>作者：</font>** Emma Shelley, Wassim Jabi, Thomas Woolley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Floor plan datasets underpin computational analysis of building layouts, spatial connectivity and graph machine learning. However, publicly available datasets often require substantial preprocessing before they can be used reliably. We present ModRes, a cleaned and enriched version of the ResPlan dataset, containing 8,431 valid and unique residential floor plans. Invalid and duplicate floor plans are removed through a dedicated cleaning workflow, producing a ready-to-use dataset. For each floor plan, ModRes provides two-dimensional geometry, images, three-dimensional building representations and three complementary dual graphs in CSV and JSON formats with graph-, node- and edge-level features. Continuous and categorical graph attributes support machine learning workflows. We characterise the dataset using graph-based statistics and demonstrate its utility through a range of case studies. ModRes provides structured geometric, topological and semantic representations needed to automate spatial analysis and support machine learning-based workflows for building design and performance evaluation.

---


### 549. [CartoVec: General-Purpose Location Embeddings from Open Map Data](https://arxiv.org/abs/2610.17190)

**<font color=#1a73e8>作者：</font>** Furkan Gursoy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geographic coordinates are common inputs in applied machine learning, but latitude and longitude describe position rather than the surrounding environment. Image-grounded location encoders learn this context from satellite or ground-level imagery; structured open map data offers another source of supervision whose utility for continuous coordinate encoders remains less explored. We introduce CartoVec, a coordinate encoder trained to predict Overture-derived land cover, land use, transportation, place and connectivity targets at multiple spatial scales, without image inputs or downstream-task labels. We evaluate frozen embeddings on Census outcomes, Airbnb prices and Philadelphia crime in the US Northeast using spatial block cross-validation. CartoVec has the highest mean performance on most Census outcomes and the highest average across the full suite, with several comparisons close across folds. The findings support open map data as a practical source of reusable location representations with a coordinate-to-vector interface that requires no map lookup at inference. The open-weight model is available at this https URL.

---


### 550. [FreeSolo: Linear-time Sparse Attention with Zero-Shot Length Extrapolation](https://arxiv.org/abs/2610.17191)

**<font color=#1a73e8>作者：</font>** Zekun Shi, Alastair James Arthur Price  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear-time sequence models typically store long-context information in a recurrent state. A fixed-size state limits how much information can be stored, while hybrid architectures that add full attention for better recall incur quadratic sequence cost. Alternatively, sparse attention with continued pretraining (CPT) can extend the effective context length. Generalization beyond the trained length remains challenging, however, and CPT can be costly. We introduce FreeSolo, a native sparse attention mechanism with a short-range sliding window branch and a long-range branch that selects keypoint cells for direct token attention. Its linear-time variant, FS-L, learns to prune the prefix before query-dependent selection through short CPT. FS-B searches balanced trees with $O(N\log^2 N)$ algorithmic cost including radix-sort construction. FreeSolo demonstrates better zero-shot length extrapolation than the baselines without long-context fine-tuning.

---


> [!TIP]
> 当前位于：**501-550**（第 11/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
