# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 101. [ControlGS: Conditioning Neural Gaussians for Downstream-Processing-Aware XR Rendering](https://arxiv.org/abs/2609.32038)

**<font color=#1a73e8>作者：</font>** Weikai Lin, Junjie Zhao, Carl Marshall 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extended Reality (XR) users do not directly perceive the output of a rendering engine. Instead, rendered images pass through a post-processing pipeline and the physical display-optics path before reaching the eye. Critically, the exact downstream processing can vary significantly at run time, influenced by, for instance, camera pose and display power budget. Traditional 3DGS methods either implicitly assume that this downstream pipeline preserves image quality or cannot adapt to downstream processing changes. To bridge this gap, we present ControlGS, an XR Gaussian rendering pipeline that optimizes end-to-end visual quality. ControlGS models and integrates the entire downstream processing, between the rendering output and the human eye, into the optimization objective. To adapt to downstream processing at run time, ControlGS dynamically generates Gaussian primitives conditioned upon the downstream processing parameters. Experiments show that ControlGS consistently improves end-to-end post-optics XR quality across different neural Gaussian backbones and datasets, with minimal overhead. Code is available at this https URL.

---


### 102. [Amnesia by Design, Memory By Necessity: Persistent State for Document Intelligence](https://arxiv.org/abs/2609.32041)

**<font color=#1a73e8>作者：</font>** Souhail Bakkali, Ayoub Merimi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Document AI reads contracts, extracts fields, reasons over tables, and grounds answers to page regions, then forgets everything. Processing an amendment the next day begins from scratch: no schema retained, no contradiction detected, no experience carried forward. This is a structural choice, not a scale failure: current systems are stateless functions. We call this the statelessness bottleneck. This bottleneck lies beyond parameter scaling, context extension, and retrieval augmentation: storage provides persistence and retrieval provides access, but neither consolidates observations into knowledge that improves future processing. This survey formalizes persistent evidence-grounded document state as a unifying framework, specifying the operations and invariants required to convert multimodal evidence into durable, provenance-linked state. We introduce a statefulness audit showing that ten representative benchmarks, coded against eight statefulness criteria, leave cross-session state evolution untested, and derive a longitudinal benchmark harness with five counterfactual metrics: Experience Gain, Cost Efficiency, Memory Harm, Forgetting Fidelity, Coverage Retention, to characterize the benefit, cost, risk, and governability of persistent document state. Document AI lacks mechanisms coupling persistent state to document-native structure, provenance, and temporal validity. The next era of Document AI will be defined by what systems retain across documents, sessions, and time.

---


### 103. [Interactive Distributionally Robust Multi-Agent Learning with General Function Approximation](https://arxiv.org/abs/2609.32048)

**<font color=#1a73e8>作者：</font>** Debamita Ghosh, George K. Atia, Yue Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model misspecification poses a fundamental challenge in multi-agent reinforcement learning, where transition uncertainty can be amplified by strategic interactions among agents. Distributionally robust Markov games (DRMGs) provide a principled framework for addressing such uncertainty, yet existing methods often rely on restrictive assumptions or scale poorly to large state and joint action spaces. We study online learning in general-sum DRMGs with general function approximation and $\phi$-divergence uncertainty sets. We propose RoMEX-$\phi$, a model-free framework that integrates equilibrium-based exploration with dual fitted learning. Through a functional dual representation of the robust multi-agent Bellman operator, RoMEX-$\phi$ enables tractable worst-case value estimation from nominal interaction data using a centered empirical robust discrepancy. We introduce the robust Multi-Agent Decoupling Coefficient (robust MADC) to characterize the intrinsic exploration complexity arising from strategic interactions and adversarial transition uncertainty. We establish sublinear robust regret guarantees governed by the robust MADC rather than explicitly by the state and joint action space sizes, replacing tabular dependence with intrinsic function-class complexity. Numerical experiments on a scalable general-sum DRMG under total variation uncertainty show that RoMEX-$\phi$ is substantially more resilient to transition shifts than its non-robust counterpart while remaining competitive with an exact tabular robust baseline. Our results provide a scalable framework for distributionally robust multi-agent reinforcement learning with general function approximation.

---


### 104. [Graph Forward Distribution Matching for Molecular Inverse Design](https://arxiv.org/abs/2609.32056)

**<font color=#1a73e8>作者：</font>** Yihan Zhu, Yuhan Liu, Brett Savoie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Achieving precise control over multiple properties without sacrificing chemical validity remains a central challenge in molecular inverse design. Existing reinforcement learning (RL) methods fine-tune graph diffusion models by treating **reverse** sampling as a sequential policy, using a single terminal reward to optimize hundreds of coupled decisions. They often suffer from instability, validity collapse, and limited property gains. We introduce GraphFDM (Graph Forward Distribution Matching), a new online RL paradigm for graph diffusion that performs optimization through the **forward** process. GraphFDM uses valid generations to define a reward-tilted target distribution jointly optimized over graph size and molecular structure for each property condition, incorporating reinforcement signals into supervised learning without storing reverse trajectories. We derive the unique optimal target, prove a condition-wise improvement guarantee, and show that the fixed graph-size prior of standard graph diffusion leaves an irreducible matching gap. In multi-conditional polymer and small-molecule generation, GraphFDM achieves the lowest MAE on every target property, with reductions of up to 53.0\% relative to the strongest baselines and chemical validity above 0.99. It further generalizes to out-of-distribution property combinations.

---


### 105. [Contract monitoring: governing AI via separation of powers](https://arxiv.org/abs/2609.32061)

**<font color=#1a73e8>作者：</font>** Enric Boix-Adsera  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose an AI safety framework that binds worker agents to contracts specifying their permitted actions. We show how these contracts can be enforced and specified by assigning distinct responsibilities to monitor agents and judges, and asymmetric computational resources to monitors and workers. Our framework allows us to empirically measure statistical safety guarantees. The framework applies to a wide range of settings, including code security and escape-the-box scenarios.

---


### 106. [ReFM: Semantic-Aware Refinement Flow Model for Motion Retargeting](https://arxiv.org/abs/2609.32068)

**<font color=#1a73e8>作者：</font>** Jingxiang Qu, Lucie Taglienti, Evan Atherton  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion retargeting transfers motion across characters with different skeletal structures while preserving semantic intent and physical plausibility. Despite recent progress, two fundamental questions remain: (i) how can reliable source-motion semantics be learned without high-quality paired retargeting data, and (ii) how should retargeting be formulated when no reliable paired motion can serve as a definitive regression objective? Existing methods commonly preserve semantics by constraining predictions toward copied motions. However, such initializations entangle useful articulation cues with artifacts caused by mismatched skeletal proportions and body geometry. Moreover, directly regressing a final motion in one forward pass is restrictive because retargeting is inherently underdetermined, and the desired solution must balance semantic fidelity with target-specific physical and temporal constraints rather than match a unique paired target. Motivated by these limitations, we propose ReFM, a source-mesh-agnostic, energy-guided model that reformulates motion retargeting as progressive refinement. First, an SO(3) canonicalizer removes redundant global-orientation variations. Second, a cross-character semantic encoder, pretrained through contrastive learning, provides a character-invariant representation for both optimization guidance and semantic evaluation. ReFM then progressively refines an initialized target motion through a learned flow guided by semantic consistency, physical plausibility, temporal coherence, and minimal motion modification. The framework is compatible with different initialization strategies, including both direct motion copying and Autodesk HumanIK, an industry-standard full-body inverse-kinematics retargeting system.

---


### 107. [When Should a Human Take Back Control? Optimal Delegation under Turbulent AI Risk](https://arxiv.org/abs/2609.32083)

**<font color=#1a73e8>作者：</font>** Haoze Yan, Julien Roze, Ved Upadhyay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying AI systems requires deciding when to delegate tasks and when humans should intervene to monitor and mitigate risk induced by AI operations. These decisions are challenging when failures cluster: a hallucination or harmful output can trigger further errors, creating periods of elevated risk. We introduce a continuous-time framework for learning adaptive human oversight under such turbulent AI risk. Existing oversight and delegation formulations condition on history but do not model incident clustering, or its suppression by supervision effort, jointly with the delegation decision and this study fixes this gap. The self-exciting dynamics capture how risk events increase the likelihood of subsequent events, making their timing and history central to decision-making. We formulate a stochastic control problem combining human actions, monitoring effort, and switching between human-AI-assisted operation and full AI delegation, balancing operational rewards against oversight costs, and cascading AI-failures and induced uncertainty. Human participation is an endogenous component of risk management: the policy determines both when oversight is needed and how much effort to allocate. We study a relaxed switching formulation and propose Hawkes-PPO, a policy-gradient method that uses a bank of exponential filters of observed incident times. In a synthetic environment it attains a higher risk-adjusted objective than either fixed regime and approaches an approximate full-information oracle. We illustrate our results with numerical simulations by examining how cascade risks influence intervention and delegation, connecting reinforcement learning with adaptive human oversight of AI systems. In particular, we illustrate the benefit of our switching strategy and Hawkes-PPO algorithm to monitor the project efficiently along time, reducing turbulent risks occurrences and costs.

---


### 108. [GameBoyWorlds: A Testbed for Self-Improvement in Embodied Video Games](https://arxiv.org/abs/2609.32093)

**<font color=#1a73e8>作者：</font>** Dhananjay Ashok, Adam Shen, Aslan Huo Feng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Powered by expert guidance, agents can operate in interactive environments; however, it is unclear whether they can learn autonomously from their own experience. To evaluate such self-improvement methods, we introduce GameBoyWorlds, a testbed for agentic self-improvement in video games. GameBoyWorlds-Execution evaluates task execution on a collection of 5 distinct game series. Agents are allowed access to dedicated training games but are provided no demonstrations, documentation, or rewards. Agents must ground themselves in the environment through self-directed exploration and by inferring actionable knowledge from their own experience. At test time, agents must complete short-horizon tasks that evaluate their ability to navigate, interact, and engage with game-specific mechanics in unseen games. Out-of-the-box frontier models complete fewer than 50% of the 500 tasks due to failures in multimodal grounding, establishing that self-improvement methods have room to push performance. We demonstrate that contemporary approaches to self-improvement are lacking, with world modelling and autonomous skill discovery failing, and a novel strategy that uses curiosity-based exploration to write guides achieving only partial success. GameBoyWorlds-Playthrough tests end-to-end game completion in two fan-made Pokémon games. We show that while frontier models have been pre-exposed to official releases such as Pokémon Red, they lack essential information on the games in our testbed. Instead of relying on their parametric knowledge to succeed, agents must learn from their own experience and autonomously improve over the course of the playthrough. We show that a sophisticated agentic pipeline with multimodal memory and hierarchical subgoals fails to reach even the first major milestone in both games, establishing GameBoyWorlds as an ambitious target for self-improving agents.

---


### 109. [Robust Game-theoretic Motion Planning over Extended Time Horizons](https://arxiv.org/abs/2609.32098)

**<font color=#1a73e8>作者：</font>** Bennet Outland, Vishala Arya  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This work presents a solution to nonconvex, game-theoretic motion planning problems subject to disturbances over long time horizons. The problem is posed as a partially-decoupled generalized Nash equilibrium problem, in which each agent's dynamics depend only on its own state and control, admitting fast solution methods for competitive multi-agent motion planning. An algorithm, WOLF, is developed that applies receding-horizon model predictive control to an open-loop differential games solver based on sequential convexification. In contrast to robust formulations that fix the uncertainty description offline, the robustness tube here is itself a dynamic state, co-optimized with the trajectory, and its thickness directly sets the tightening of the shared coupling constraints. A sufficient condition is derived under which a nominal trajectory satisfying constraints tightened against all agents' error bounds remains feasible for every admissible disturbance realization. The method is demonstrated on two adversarial on-orbit games with coupled translational-attitude dynamics: a stealthy co-orbital jamming game under an active detection-probability bound, and a sun-blocking game in which an adversary disables an evader by decreasing solar power

---


### 110. [An Attention-Driven Heterogeneous GNN Model for Credit Card Fraud Detection](https://arxiv.org/abs/2609.32106)

**<font color=#1a73e8>作者：</font>** Kathiresan Jayabalan, Sethuraman Radhakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The global transition to a cashless economy has placed credit cards as the key element of digital transactions, acclaimed for their easy use, speed, and acceptance in most places. However, the growing dependence on this payment method has led to an escalation of the risks associated with credit card (CC) fraud. Detecting this type of fraud is a difficult task because the patterns are constantly changing, there is a data imbalance, and it is necessary to identify the legitimate transactions and the fraud ones at the same time. This study addresses this challenge by proposing a credit card fraud detection (CCFD) framework using a data balancing technique and a deep learning (DL) model. The proposed fraud detection model is trained and evaluated by collecting the dataset called Credit Card Fraud Detection from the Kaggle repository. As the dataset is highly imbalanced, we utilized the Synthetic Minority Oversampling Technique (SMOTE)-Tomek technique to balance the dataset. Further, the balanced dataset is classified using the Heterogeneous Graph Neural Network (HGNN) model. The HGNN model represent various transactions using a heterogeneous graph architecture and by using an attention based message passing technique, it managed to consider the complex relationships, time factors, and user behavior. The integration of SMOTE-Tomek in the model further boosted its capacity to identify fraudulent transactions, while lowering the rate of false positives. The HGNN model attained a 99.97% accuracy, a 99.48% F1-score, a 99.15% precision, and a 98.97% recall. The findings indicates that this model is effective and can be applied to real-world CCFD scenarios.

---


### 111. [Escaping Alignment: A Physical Trap Model of Best-of-N Jailbreaking](https://arxiv.org/abs/2609.32116)

**<font color=#1a73e8>作者：</font>** Marco Biroli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Best-of-$N$ jailbreaking (BoN) bypasses safeguards of aligned models by drawing $N$ independent augmentations of an unsafe prompt and sampling $M$ completions of each. Previous works have shown that the attack success rate (ASR) seems to follow a power-law in $N$, which we challenge. The exponent drifts with $N$, with an exponential crossover which is a finite-size artifact of the adversarial dataset. Little work has been done to explore the entire two-budget ($N, M$) attack surface as well as its dependence on the generation temperature $T$. We introduce a simple barrier model where each prompt has a baseline safety level and each augmentation a random thermally activated barrier. Then four numbers, each backed by an interpretable safety mechanism, determine the entire ($N, M$) attack surface. They extrapolate predictions from $N \leq 100$ to $N = 10^4$, collapse five distinct models on the same scaling function and predict ASR at different temperatures from the one they were fitted at.

---


### 112. [Handwritten Digit Leakage from Smartphone Motion Sensors Across Unseen Users and Phone Models](https://arxiv.org/abs/2609.32117)

**<font color=#1a73e8>作者：</font>** Constantino Álvarez Casado, Erkka Rantahalvari, Matteo Pedone 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smartphone motion sensors support interactive applications, but their readings may also reveal touchscreen input beyond their intended use. Assuming known drawing intervals, we study whether handwritten digits remain predictable across users and devices, as a 10-class problem on 19,628 HuMIdb recordings from 481 participants. We compare handcrafted features with classical machine learning algorithms, MiniRocket kernels, and a compact sensor patch transformer on accelerometer, linear acceleration, gyroscope, and gravity signals. The transformer achieves 57.74\% accuracy and 82.64\% top-3 accuracy on 75 unseen participants, and 58.77$\pm$0.95\% over 3 seeds for unseen participants on 9 unseen phone models. Low motion recordings remain informative, accuracy is not monotonic in motion level, and the tested contrastive pretraining, augmentation, and derived signals give no consistent gains. Digits are thus predictable beyond familiar users and phone models under assumed segmentation, while acquisition-order shortcuts limit conclusions about practical privacy exposure. Code available at: this https URL.

---


### 113. [Gaussian Image Steganography via Parameter-Domain Keyed Embeddings](https://arxiv.org/abs/2609.32131)

**<font color=#1a73e8>作者：</font>** Tong Wu, Runze Cheng, Xiaoyue Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 2D Gaussian-based image representation is becoming increasingly popular, and our work proposes a new approach to steganography by embedding information within Gaussian parameters rather than image pixels. We first fit the parameters of this representation to the target image and employ a secret key to select a subset of these parameters for fine-tuning, allowing us to embed an 8-bit message while maintaining high visual fidelity in the reconstructed image. Thirty fitting experiments on three synthetic images show that the correct key can recover the message without error, while decoding with incorrect keys yields a Bit Error Rate (BER) of $0.543$, close to random guessing. Compared with random selection using the key, selecting the least-disturbing edits recovers the message more reliably (one-sided $p=0.031$), and the average PSNR cost is only $0.091$ dB in visual quality. The embedding method transfers to 112 natural images at $256\times256$ using 4,096 Gaussians. The correct-key BER is $0.000$, and decoding under a wrong key stays close to random guessing at $0.520$. Our method embeds the payload through three Gaussian parameter types: log-anisotropy, opacity, and color luminance. In a separate nine-fit reduced setting, color luminance is removed, so the payload uses two instead of three parameter types, a $33.3\%$ reduction; all 256 Gaussians remain in the fitted representation. The correct key still recovers the message without error. However, wrong-key BER rises from $0.514$ to $0.571$, moving farther from random guessing ($0.5$).

---


### 114. [Latency-Aware Client Assignment for Parallel Split Learning With Global Sampling](https://arxiv.org/abs/2609.32132)

**<font color=#1a73e8>作者：</font>** Mohammad Kohankhaki, Valentin Rentschler, Anke Schmeink  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In cross-silo split learning, Parallel Split Learning with Global Sampling forms representative pooled batches when class distributions differ across clients, but ignores client delay when several clients can supply the same class. We introduce Latency Budgeted Parallel Split Learning with Global Sampling, which separates each pooled batch's integer class target from the choice of clients that supply its examples. The flow variant formulates this assignment as an integral network-flow problem and minimizes modeled client-side completion time for the current target. The fast variant uses a greedy next-completion rule to reduce schedule-construction cost. Both preserve the target stream and use every local example once per epoch. A planning rule selects between the variants while accounting for the cost of constructing both candidate schedules. On CIFAR-10, the flow variant reduces modeled training time by 6.75%, with a 0.30 percentage-point decrease in final accuracy. On Tiny ImageNet with 20 candidate classes per client, the fast variant reduces modeled time by 16.87% and reaches all four validation targets earlier than the latency-unaware baseline. Across 405 schedule comparisons, the planning rule stays within 2% of the lower realized cost in 96.54% of cases. In our evaluation, latency-aware provider assignment reduces modeled training time without changing the prescribed class targets, while the preferred variant depends on whether assignment savings outweigh schedule-construction overhead.

---


### 115. [REALM: Regime-Switching, Explainable, and Activation-Induced Linear Models](https://arxiv.org/abs/2609.32141)

**<font color=#1a73e8>作者：</font>** Xiaoran Cheng, Sen Na, Jia Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep ReLU networks are piecewise-affine mappings that partition the input space into cells, each characterized by a distinct activation pattern. This structure motivates fitting a local linear model within each cell to preserve predictive accuracy while improving interpretability. The challenge is to identify regimes that are stable, data-adaptive, and easy to explain. We propose REALM, a mixture of linear models whose regimes are induced by neural activation patterns. Because the number of activation cells in a deep neural network (DNN) can grow rapidly with depth, we first distill a deep teacher into a wide, shallow student network (WSSN), then binarize and cluster its hidden-layer activations to define the regimes and fit a linear model within each regime. Since the regimes are discovered from internal structure, the router does not carry the predictive burden. To make regime assignment interpretable, we train a multiclass logistic regression, the explanatory gate, to reproduce the regime assignments. The two-level structure is interpretable at both stages in terms of raw tabular or learned convolutional features: the gate identifies features that determine regime assignments, while the linear models identify features that drive predictions within each regime. We analyze an idealized setting that illustrates a trade-off between partition complexity and stability: as the number of regimes grows, finer partitions can improve approximation but may reduce regime-assignment stability. Experiments on tabular and image datasets show that REALM achieves competitive predictive performance relative to other DNN-guided mixture surrogates and inherently interpretable models while producing stable regime-level explanations.

---


### 116. [Spectral Reversal: Counteracting Singular Value Bias for Graph Prompting](https://arxiv.org/abs/2609.32143)

**<font color=#1a73e8>作者：</font>** Hanxu Yang, Yuhuan Zhao, Xiaodong He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-training Graph Neural Networks (GNNs) via self-supervised learning has become a dominant paradigm, yet efficiently adapting frozen encoders remains a challenge. Graph prompting offers a parameter-efficient alternative to fine-tuning, but existing methods largely treat pre-trained models as opaque feature extractors, ignoring their internal spectral structure. In this work, we identify a systematic phenomenon in pre-trained GNNs, which we term spectral bias: optimization during pre-training disproportionately aligns representations with directions associated with large singular values, leaving low-energy directions under-explored. We show that these underutilized directions can encode complementary information that is beneficial for downstream adaptation, especially under distribution shift. To leverage this insight, we propose Spectral Reverse Prompt (SRP), a prompting framework that rebalances the spectral contributions of frozen GNN encoders. SRP applies a learnable soft-thresholding mask in the spectral domain to down-weight dominant directions while amplifying weaker ones. In addition, SRP incorporates a null-space augmentation module that captures variation in directions with minimal activation under the frozen encoder. Extensive experiments across multiple benchmarks demonstrate that SRP achieves state-of-the-art performance with minimal additional parameters, highlighting that reweighting spectral components is a principled and effective strategy for parameter-efficient graph adaptation.

---


### 117. [Playing to Par: Reinforcement Learning for Provably Optimal Quadrilateral Block Decompositions](https://arxiv.org/abs/2609.32146)

**<font color=#1a73e8>作者：</font>** Arjun Narayanan, Per-Olof Persson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A quadrilateral block decomposition of a planar domain is judged by whether it is complete, whether its elements are well shaped, and how many of its vertices are irregular. The last has a provable floor: the discrete Gauss-Bonnet identity enforces a lower bound on the total vertex irregularity of any all-quadrilateral mesh of a given domain purely based on its topology and corner angles. We train a reinforcement learning agent to build decompositions that reach this bound, which we call par. It acts directly on the mesh's half-edge data structure through local edits, with a policy network whose convolutions follow the mesh's own connectivity, so it applies unchanged to domains larger than any seen in training. The reward targets the floor directly, and it is sparse: random play reaches it on no domain with more than eight sides. We overcome this exploration barrier via behaviour cloning on optimal meshes that are trivial to construct, walked backward into demonstrations, before training it with PPO. On 96 held-out domains the agent produces an all-quadrilateral mesh on every one, a usable one on 95.7 on average, and a provably optimal one on 90; Gmsh's strongest configuration at the same element count completes 51, is usable on 38 and optimal on none, and even at three to fourteen times the elements never produces a more regular mesh. On 64 domains twice the training size the agent completes all, is usable on 62, and keeps a median excess over par below one against Gmsh's 39 at the same element count.

---


### 118. [Typed Decision Models: An Early Evidence Audit and Evaluation Checklist](https://arxiv.org/abs/2609.32160)

**<font color=#1a73e8>作者：</font>** Lijuan Tang, Yuemeng Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typed decision models (TDMs) return probability distributions over caller-defined options without generating text. TypeSafe released Jev, a commercial typed decision model, on 15 September 2026, and a small body of evaluation and replication work appeared within days. We review 28 papers posted between 19 and 24 September and relate their findings to earlier work on label-probability classification, constrained decoding, reranking, calibration, and model cascades. In this early literature, the typed readout itself has not shown an independent accuracy advantage over comparable label-probability readouts. Jev's clearest gains are in latency and cost, while accuracy gaps remain on harder tasks. In practical deployments, confidence is often used to decide when to defer to a stronger model or a human. We use recurring weaknesses in these studies to derive a 14-item evaluation checklist for future TDM work. Because the evidence covers only the first nine days after the release of one hosted model, the review should be read as an early evidence map rather than a settled assessment of the model class.

---


### 119. [PruneForget: Joint Unlearning and Pruning of Vision Models](https://arxiv.org/abs/2609.32162)

**<font color=#1a73e8>作者：</font>** Yu-Shan Tai, Amber Yijia Zheng, Raymond A. Yeh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning and model pruning are increasingly coupled in the real world. Models must support unlearning requests, e.g., for safety concerns, while also meeting requirements in latency and memory budget. Until recently, existing works have studied each aspect as an independent problem, e.g., running unlearning and pruning sequentially. In this work, we show that unlearning and pruning are naturally aligned and should be solved jointly to be made aware of each other. Intuitively, parameters that encode information of the unlearned samples are natural pruning targets, as unlearning and pruning both call for the "deletion" of such parameters. We propose PruneForget, a method that uses the unlearn set as a guide for pruning, so that unlearning and pruning mutually benefit each other. Extensive experiments on image classifiers and generative models show that PruneForget removes the influence of the unlearned samples while producing a more compact model with reduced inference cost. It achieves a negligible performance gap relative to an oracle that retrains from scratch for unlearning and then prunes.

---


### 120. [PQR3D: Progressive Query Refinement over Reference-Conditioned Temporal Windows for Multi-View 3D Object Detection](https://arxiv.org/abs/2609.32163)

**<font color=#1a73e8>作者：</font>** Hui Ye, Yudong Liu, Yiran Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal context is essential for camera-only multi-view 3D object detection. Existing streaming detectors maintain and propagate query states from one frame to the next, requiring sequence-aware training and chronological inference. We propose PQR3D, which performs progressive query refinement within referenceconditioned temporal windows. This design enables random frame sampling and independent inference without persistent query memory. Within each window, PQR3D progressively transfers motion-aligned high-confidence queries from earlier timestamps toward the target frame. We further introduce masked selfattention to regulate interactions among regular, propagated, and denoising queries while keeping denoising supervision isolated from detection queries. In addition, a stage-decoupled anchor embedding injects position before self-attention and size, orientation, and velocity afterward, reducing interference from temporally inconsistent attributes. With a ViT-L backbone, PQR3D sets a new state of the art on the nuScenes test set, achieving 71.6 NDS and 64.9 mAP. Source code is available at this https URL

---


### 121. [CAFE: Counterfactual Prediction via Fast Posterior Estimation](https://arxiv.org/abs/2609.32167)

**<font color=#1a73e8>作者：</font>** Xinyan Han, Xiaoyu Lin, Hao Zou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual prediction estimates an individual's outcome under an alternative intervention given their factual observations. Such outcomes are generally not identifiable from observational data without additional assumptions. Even within the class of fully observed additive noise models (ANMs), different causal graphs can generate the same observational distribution yet imply different individual counterfactual outcomes. Predictions based on a single estimated graph ignore this structural uncertainty. We therefore target a Bayesian counterfactual posterior predictive distribution that combines predictions from plausible SCMs. We introduce CAFE (\textbf{C}ounterf\textbf{A}ctual Prediction via \textbf{F}ast Posterior \textbf{E}stimation), an amortized inference framework that directly approximates the Bayesian counterfactual posterior predictive distribution. We pretrain a transformer-based model on synthetic counterfactual tasks generated from a diverse prior over ANMs. Given an observational dataset, an individual's factual observations, and an intervention, CAFE approximates the corresponding posterior predictive distribution in a single forward pass. Experiments show that CAFE accurately predicts individual counterfactual outcomes in identifiable settings and approximates the posterior predictive distribution when structural uncertainty induced by observationally indistinguishable causal graphs exists. Strong performance in realistic manufacturing and viticulture settings further demonstrates its empirical robustness beyond the assumptions of the training prior.

---


### 122. [Uncertainty-Aware Selection of Online Algorithms with Simulator Ensembles](https://arxiv.org/abs/2609.32170)

**<font color=#1a73e8>作者：</font>** Yongyi Guo, Zifan Xu, Ziping Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The performance of online reinforcement learning depends critically on design choices, especially those that affect exploration. These choices are often selected by fitting a simulator to offline data, evaluating candidate algorithms in that simulator, and deploying the best-performing one. The simplest Plug-In selection rule simply selects the best performing algorithm on the fitted simulator, making evaluations unreliable when the offline data used to fit the simulator are limited. We investigate Uncertainty-Aware selection, which forms an ensemble of simulators---for example, obtained by bootstrap resampling---and selects the online algorithm with the best average performance across the ensemble. While ensemble-based approaches have been used to mitigate distribution shift and facilitate sim-to-real transfer, we formally show that this approach can mitigate the effects of limited data when fitting the simulator and theoretically has significant regret gains compared to Plug-In selection in multi-armed bandits. We also empirically investigate the Uncertainty-Aware selection approach in deep RL experiments on robotic control tasks that involve selecting reward-shaping hyperparameters, and show that it leads to more reliable selection and improved online performance.

---


### 123. [OneFixer: High-Quality and Consistent One-Step Autoregressive 3DGS Refinement for Driving Scenes](https://arxiv.org/abs/2609.32175)

**<font color=#1a73e8>作者：</font>** Boseong Jeon, Junhyeop Lee, Juhan Cha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion is a promising render-time fixer for 3D Gaussian Splatting (3DGS) in autonomous-driving simulation, but deployment demands high visual quality and temporal consistency at low latency. This is especially hard for one-step causal generation, where each imperfect prediction immediately becomes context for subsequent frames. Existing approaches stabilize rollouts through staged training with multiple modules and rollout-aware regularization, yet one-step quality still falls short of what deployment requires. We introduce OneFixer, a one-step autoregressive video-diffusion fixer trained in a single task-specific adaptation stage. Our key idea is a deployment-matched shared rollout: the model's own one-step predictions serve as the causal context for flow matching, exposing training to deployment-time errors, while the same rollout receives direct pixel-space perceptual supervision to preserve fine detail. Because the predictions optimized for current-frame quality are exactly those reused as future context, fidelity and autoregressive robustness are learned jointly, without bidirectional-to-causal conversion or teacher-student distillation. OneFixer further exploits cues that driving simulation readily provides, lane geometry and dynamic-agent states, to improve geometric fidelity. On Waymo and proprietary driving scenes with 900-frame rollouts, OneFixer achieves the lowest FVD, LPIPS, and DISTS among all baselines at one step, with temporal consistency matching or exceeding multi-stage DMD pipelines. Under identical backbone and conditioning, it matches a multi-stage DMD-with-Self-Forcing pipeline in under half the GPU-hours and keeps improving beyond its plateau. In closed-loop simulation with a driving policy, OneFixer reduces the collision rate by a third relative to raw 3DGS rendering. Project page: this https URL

---


### 124. [Efficient Support Recovery of Mixtures of Sparse Linear Classifiers with Less Measurements](https://arxiv.org/abs/2609.32176)

**<font color=#1a73e8>作者：</font>** Xiaxin Li, Arya Mazumdar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The support recovery problem in mixture of linear classifiers intends to identify which features actually matter when data is generated by a mixture of several linear decision rules. In particular, the aim is to recover the support (nonzero coordinates) of $l$ unknown $k$-sparse vectors from sign measurements. Each measurement is generated by selecting one of the $l$ vectors uniformly at random, and returning the sign of its inner product with a chosen measurement vector.
In this paper, we propose adaptive and non-adaptive schemes that significantly improve upon prior results by reducing the number of measurements and achieving sublinear decoding time simultaneously. In particular, our adaptive constructions substantially reduce measurements compared to existing approaches, while also lowering decoding complexity from super-quadratic to sublinear in the ambient dimension. We further provide a non-adaptive scheme that improves previous measurement bounds while maintaining efficient decoding.
Overall, our approach yields a more efficient trade-off between sample complexity and decoding time for support recovery in mixture models than previously known methods.

---


### 125. [Federated 3D Gaussian Splatting for Large-Scale Scene Reconstruction at Wireless Edge](https://arxiv.org/abs/2609.32177)

**<font color=#1a73e8>作者：</font>** Guanlin Wu, Chao Hu, Pu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional (3D) Gaussian splatting (3D-GS) has emerged as a promising technique for large-scale scene reconstruction due to its high rendering efficiency and fidelity. However, the training of large-scale 3D-GS models at wireless edge faces various technical challenges including the limited communication, computation, and graphics processing unit (GPU) memory resources at edge devices, the structural inconsistency issue across local models hindering their effective aggregation, as well as privacy leakage risks associated with raw visual content and camera parameters. To address these challenges, this paper proposes a novel resource-efficient federated learning framework for efficiently training 3D-GS models of large scenes under severe resource constraints. First, we propose an on-device model lightweighting mechanism that adaptively selects and prunes Gaussian points to balance the rendering quality and training efficiency. In this mechanism, we quantitatively evaluate the importance of different Gaussian points at each device to facilitate the pruning, and use a novel importance-to-latency ratio criterion to determine the number of pruned Gaussian points under GPU memory and computation/communication latency constraints. Furthermore, we develop a 3D-GS model recovery mechanism that restores structural consistency across local 3D-GS models without accessing private camera parameters, enabling their effective aggregation towards a global model. Finally, extensive experiments show that our approach significantly accelerates convergence, maintains high rendering quality, and reduces training latency compared to state-of-the-art federated 3D-GS baselines.

---


### 126. [Analytic-Walk Rotary Positional Encodings for Graphs](https://arxiv.org/abs/2609.32178)

**<font color=#1a73e8>作者：</font>** Jiaqing Xie, Yuxin Wang, Xipeng Qiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rotary position encodings make attention sensitive to relative position, but extending them to graphs requires choosing how graph structure enters the rotation. Previous works assign each node a rotation from spectral coordinates, so the rotary factor between two nodes depends only on their endpoints and cannot distinguish the routes connecting them. We introduce \textit{Analytic-Walk Rotary Positional Encodings} (AW-RoPE), which place the rotations on edges and sum the transported features over all walks, so contributions along different routes can reinforce or cancel. An exact variant evaluates the complete sum by a differentiable linear solve, and a sparse variant truncates it at a finite depth. We prove forward and parameter-derivative truncation bounds at fixed inputs and parameters. Both variants act on projected queries and keys, and the sparse recurrence also augments message-passing networks. Across five synthetic tasks both variants reduce nRMSE by $15$--$58\%$ relative to the strongest baseline, and on real superpixel, peptide and OGB benchmarks the sparse recurrence attains the best mean on every dataset with Performer kernels and on twelve of thirteen datasets with GIN. Analysis shows that AW-RoPE can distinguish routes whose only cue is how two endpoints are connected, while node-wise rotary encodings cannot.

---


### 127. [Binaural Audio-Visual Instance Segmentation](https://arxiv.org/abs/2609.32180)

**<font color=#1a73e8>作者：</font>** Saijun Wang, Guanfeng Tang, Hongbo Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual segmentation (AVS) aims to segment sounding objects at the pixel level by integrating auditory and visual cues. However, existing methods are predominantly developed under the monaural setting and primarily rely on cross-modal semantic correspondence, which limits their ability to distinguish visually similar instances of the same semantic class. In contrast, humans naturally exploit binaural hearing, where interaural differences and direction-dependent acoustic filtering introduced by the head and pinnae provide physically grounded spatial cues for accurate sound source localization. Motivated by this observation, we introduce binaural audio-visual instance segmentation (BiAVIS), a new task that leverages synchronized binaural audio and video frames to segment sounding instances. To advance research on this task, we establish two benchmarks by manually annotating an existing binaural audio-visual dataset and collecting a new real-world dataset, BiAVIS-Bench, in more challenging and diverse scenarios. We further propose a BiAVIS model, which leverages an audio-only sound source localization network to learn spatial and semantic priors for sounding instances from binaural audio. A query-level audio-visual fusion strategy is subsequently introduced to inject these informative priors into the instance segmentation decoder. Extensive experiments conducted on the two proposed benchmarks demonstrate the superior performance of the BiAVIS model over previous monaural AVS methods, especially in resolving instance-level intra-class ambiguity. On the more challenging BiAVIS-Bench, the proposed BiAVIS model outperforms the best-performing monaural baselines by 17.22\% in mAP and 7.71\% in FSLA, respectively.

---


### 128. [Rethinking Cross-Channel Importance in Time-Series Forecasting](https://arxiv.org/abs/2609.32187)

**<font color=#1a73e8>作者：</font>** Yong-Hoon Choi, Kwang-Hyun Park, Youngjin Cho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-channel modeling is central to multivariate time-series forecasting, yet channels that are statistically related, predictively useful, and actually used by a trained forecaster are often treated as if they defined the same notion of importance. We show that they need not coincide. Cross-channel dependency structures change substantially across future offsets, and horizon-adaptive source selection improves a controlled Ridge predictor in 21 of 32 dataset--prediction-length conditions, with a mean gain of $5.16\%$. This selected-set signal also transfers to a matched nonlinear predictor. Yet imposing the same horizon-specific source logic on iTransformer yields only 11 of 20 wins and a mean gain of $0.208\%$, with little alignment between controlled and neural gains. Functional interventions further show that strong forecasters use cross-channel information, while their source-reliance rankings agree little with controlled utility or with one another across iTransformer, TimesNet, and a cross-channel TimeMixer. As a constructive consequence, bounded post-hoc support improves a frozen channel-independent forecaster in 12 of 16 dataset--horizon conditions, with a positive aggregate bootstrap interval. Cross-channel importance should therefore be interpreted relative to the forecasting mechanism and question that define it: related $\neq$ useful $\neq$ used.

---


### 129. [Presence Is Not Faithfulness: Figurative Vehicle Intrusion in Text-to-Image Generation](https://arxiv.org/abs/2609.32188)

**<font color=#1a73e8>作者：</font>** Xiaoyu Ma, Chen Yang, Hao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (TTI) models increasingly generate high-quality images from natural-language prompts, yet figurative language exposes a failure: a vehicle that should guide the depiction of a tenor may instead be rendered as a visible object. We call this failure Figurative Vehicle Intrusion: the intruding content is textually licensed, but it is assigned the wrong visual role, showing that visual presence is not always faithfulness and that presence-oriented evaluation can miss such errors. To study it systematically, we introduce Vehicle Intrusion and Semantic Tenor Assessment (VISTA), a multilingual benchmark of figurative prompts organized by Figurative Form and Mapping Mechanism. We further propose V-Score, a diagnostic question-answering metric that evaluates role-aware figurative faithfulness in generated images. Evaluations on recent high-performing TTI models show that vehicle intrusion persists across languages and figurative categories. As a lightweight mitigation, we introduce VISTA-Guard, which partially reduces vehicle intrusion and suggests a practical path toward more figuratively faithful TTI generation. All resources will be released publicly.

---


### 130. [Evaluating Single and Multi-Omics Based Explainable Artificial Intelligence (MOXAI) for Molecular Subclass Classification of Adult-Type Diffuse Gliomas](https://arxiv.org/abs/2609.32190)

**<font color=#1a73e8>作者：</font>** Md Zahangir Alom, Quynh T. Tran, Breuer Alexandar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> DNA methylation (DNAM) profiling has emerged as a powerful diagnostic tool for classifying brain and solid tumors. However, existing computational models typically analyze methylation and copy number variation (CNV) data separately, failing to capture the complementary information their integration could provide. Moreover, current classification models lack mechanisms for within-class risk assessment analogous to traditional tumor grading, and no established explainability method can attribute classification decisions to specific genomic loci. In this paper, we present MOXAI (Multi-Omics Based Explainable AI), a deep learning framework that integrates DNA methylation and copy number data from methylation arrays to classify molecular subtypes of adult-type diffuse gliomas, alongside single-modality variants for comparison. Using a cohort from The Cancer Genome Atlas (TCGA), we trained ResNet50, DINOv2, and Graph Attention Network (GAT) models on methylation data alone, copy number data alone, and combined multimodal data. We further developed explainable AI (XAI) methods based on class activation maps (CAMs) and gradient-weighted CAM (Grad-CAM) to identify the specific CpG sites, genes, and chromosomal regions most relevant to each classification decision. The multimodal model achieved up to 92.98% cross-validation accuracy, outperforming models trained on CNV data alone. DINOv2 showed the strongest generalization, reaching 94.25% accuracy (confidence >0.9) on independent validation sets. XAI results aligned with established molecular features of adult-type diffuse glioma subtypes, confirming the biological interpretability of the framework.

---


### 131. [CoMemBench: Benchmarking Collaborative Memory Boundaries across Multi-Agent Workflow Topologies](https://arxiv.org/abs/2609.32192)

**<font color=#1a73e8>作者：</font>** Sen Zhao, Ruiqi Kong, Zuyu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent workflows require task-relevant information to be shared across agents, while irrelevant, stale, unverified, or incompatible information must remain isolated. We call this task-conditioned scope of information a collaborative memory boundary. Workflow topology determines which intermediate artifacts are applicable to which downstream workers and when they cease to be valid, thereby providing a structural stress dimension for sharing and isolation. Existing memory benchmarks primarily evaluate retention and retrieval, whereas multi-agent benchmarks emphasize coordination and end-to-end completion, leaving topology-conditioned memory boundaries largely unmeasured. We introduce CoMemBench, an execution-grounded benchmark for collaborative memory sharing and isolation across multi-agent workflow topologies. It constructs 800 composite workflows across four domains from source-grounded dependency graphs, with node-local specifications, verifiable artifact handoffs, native evaluators, and matched isolation challenges. CoMemBench measures workflow completion, verified node progress, required-handoff reliability, isolation robustness, and token cost. Experiments reveal a sharing-isolation trade-off: broader context improves information availability but can weaken isolation, while system rankings shift across topologies and artifact violations.

---


### 132. [DegreeSpar: Structured Degree Sparsity for Efficient Secure Transformer Inference](https://arxiv.org/abs/2609.32204)

**<font color=#1a73e8>作者：</font>** Yifei Cai, Zhuoran Li, Xiaozuo Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Secure Transformer inference protects sensitive inputs but incurs substantial cryptographic overhead, with nonlinear operations such as Softmax and GeLU becoming major bottlenecks. Existing compression methods reduce nonlinear complexity, sequence-dependent computation, or model structure through separately defined compression variables. Under aggressive compression, however, these independently optimized perturbations can accumulate: at a matched compression level, stacking representative approximation, token-pruning, and model-pruning methods reduces ViT-S accuracy from 80.20% to 76.41%. We introduce DegreeSpar, which formulates secure Transformer compression as structured sparsification over nonlinear polynomial degrees. Polynomial degree directly controls the cost of secure nonlinear evaluation, while computation-aligned zero-degree structures expose token-level and model-dimension computation as removable within the same optimization space. DegreeSpar further incorporates approximation-aware training for low-degree Softmax and GeLU, enabling aggressive degree reduction and creating the optimization headroom required for structured computation removal. Across vision and language Transformers, DegreeSpar consistently improves the accuracy-latency trade-off across model scales, tasks, and sequence lengths, achieving speedups from 2.29x to 6.63x over the corresponding baselines. Under the same network setting, DegreeSpar achieves 92.68% accuracy on BERT/SST-2 in 110.55 s, compared with 92.66% in 167.26 s for CipherPrune, the closest prior hybrid secure-inference approach. These results establish structured polynomial degree as an effective shared optimization space for secure Transformer compression.

---


### 133. [HM-ROUTER: Joint Model and Harness Routing for Agentic Systems](https://arxiv.org/abs/2609.32213)

**<font color=#1a73e8>作者：</font>** Hao Mark Chen, Royson Lee, Yasuyuki Okoshi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agent performance depends on both the underlying model and the harness that manages its tool use and execution. Selecting a suitable pair requires accounting for their compatibility, yet training samples may cover only a subset of the growing combination space. We introduce HM-Router, a routing method that jointly selects a model and harness for each query. It learns separate model and harness representations shared across routes, with an interaction term inspired by canonical polyadic (CP) tensor decomposition to capture how their compatibility varies with the query. This sharing allows training samples from observed pairs to inform predictions for unobserved combinations. We curate a benchmark from 12 public agent benchmarks, covering 293 routes, 73 models, and 25 harnesses. HM-Router exceeds the strongest evaluated learned baseline by 7.3 percentage points in mean routing accuracy and leads at all seven evaluated cost budgets on the six-benchmark subset. When 90% of routes have their training outcomes withheld, allowing unobserved combinations improves normalized accuracy by 15.8 points over restricting the same router to observed routes. HM-Router has also demonstrated training sample efficiency for new routes and components and generalization to unseen benchmarks. Our code and data are open-sourced at this https URL.

---


### 134. [DP-Rec: Towards Dynamic Patching for Efficient Long-Sequence Recommendation](https://arxiv.org/abs/2609.32215)

**<font color=#1a73e8>作者：</font>** Dwipam Katariya, Thomas Caputo, Akshat Shreemali 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have redefined sequential recommendation by effectively modeling dynamic user behaviors and long-range dependencies. However, they remain inherently inefficient: standard architectures operate at a fixed rate, allocating comparable computation to every item in a user's history regardless of its information content. This leads to prohibitive computational overhead on long sequences and increased sensitivity to behavioral noise. To address this, practitioners often resort to lossy sequence compression, staged modeling, or truncation. This limits the model's ability to leverage the full context of long histories during inference. Inspired by the recent success of Byte Latent Transformer, we propose DP-Rec, a dynamic latent patching architecture for recommendation. DP-Rec shifts from item-level modeling to patch-level modeling by segmenting interaction sequences using contrastive entropy surprise to identify informative behavioral boundaries. A lightweight patch encoder compresses these temporally contextualized segments into a reduced set of dynamic latent behavior vectors, which are then processed by a larger latent transformer and decoded for next-item prediction. Extensive experiments show that, under constrained computational budgets, DP-Rec scales effectively to long sequences and achieves a superior efficiency-accuracy trade-off over both non-compressed and fixed-size compression baselines.

---


### 135. [A model of rational interlocutors: Unification of comprehension and production](https://arxiv.org/abs/2609.32216)

**<font color=#1a73e8>作者：</font>** Hanlin Wu, Zhenguang G. Cai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Who we communicate with influences both our interpretation of their utterances and the design of our own. Such adjustment to the conversational partner is studied as speaker modeling in comprehension and as audience design in production, with the two literatures having developed largely separately. We argue that both adjustments express one rational computation and propose the rational interlocutor (RI) model, a computational account unifying comprehension and production. An interlocutor maintains a model of their partner, defined by three parameters: an identity parameter {\Pi} sets the messages and forms expected from the partner; a fidelity parameter {\Phi} sets how reliably messages and utterances map onto each other for them; a knowledge parameter {\Lambda} sets how knowledgeable the partner is believed to be. Comprehension and production are thus mirror-image modes of one computation over the partner model. Comprehension chooses the message the partner most likely intends to convey, weighing how well each candidate fits the utterance against how likely this partner is to mean it. Production chooses the utterance from which the partner will best recover the message, weighed against the effort of saying it. This explains why comprehenders appear to rely less on the forms produced by a linguistically less competent speaker, while producers tend to invest more effort in designing forms for them. We conjecture that perceived linguistic competence decomposes into two of these quantities: fidelity and knowledge. Their contrasting profiles across second-language (L2) adults, children, and artificial partners produce distinct and testable predictions.

---


### 136. [Geometry-Preserving Blind Watermarking for Raw 3D Point Clouds](https://arxiv.org/abs/2609.32222)

**<font color=#1a73e8>作者：</font>** Rungui Zhou, Chuanzhi Zhou, Ruihuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Raw 3D point clouds are a core geometric representation. Establishing their ownership is challenging because point sets are irregular, unstructured, and frequently altered by resampling and geometric preprocessing. We present a blind watermarking framework that operates directly on xyz coordinates and supports both object-level shapes and scene-scale scans. At verification time, the embedded message is recovered from the observed point cloud alone, without access to the original point cloud, color, normals, or mesh connectivity. The method jointly learns watermark embedding and extraction through a feed-forward octree-based architecture, enabling efficient multi-scale geometric reasoning on large point sets. During training, a stochastic transformation layer exposes the decoder to common geometric perturbations, while progressive pose alignment improves robustness to pose changes.
Experiments on object-level and scene-level benchmarks demonstrate reliable message recovery under common geometric processing while maintaining low geometric distortion. Qualitative comparisons further show that the learned perturbations are less visually conspicuous and less spatially structured than those of handcrafted alternatives.

---


### 137. ["Where Can I Trust You?": Boundary-Aware Evaluation of Surrogate Fidelity](https://arxiv.org/abs/2609.32230)

**<font color=#1a73e8>作者：</font>** Jackson Eshbaugh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surrogate models are commonly evaluated by how often they agree with their teacher model over an evaluation set. Local variation in this agreement is well known, but its structure and consequences are less clear. We ask whether disagreement is systematically concentrated near the teacher's decision boundary and whether retaining that structure provides information beyond a single global score. Across several datasets and surrogate model classes, we find substantially lower fidelity near teacher decision boundaries under two different methods of identifying near-boundary examples. Moreover, conditioning agreement on confidence-defined regions improves prediction of teacher--surrogate agreement when evaluation-set composition changes, relative to the global score alone. Yet surrogates that agree equally well with the teacher both globally and near the decision boundary can respond very differently to changes selected using the surrogate itself. Finally, we show that independently trained deep teachers can agree on most predictions while identifying different examples as lying near their decision boundaries, complicating the use of those boundaries as stable reference regions for evaluating surrogates. Together, these results show that surrogate fidelity depends not only on how often a surrogate agrees with its teacher, but also on where that agreement holds and, for deep models, how stable the teacher's decision boundary is across training runs.

---


### 138. [Skeletons in Flow: Graph Structured Flow Matching for Human Motion Prediction](https://arxiv.org/abs/2609.32231)

**<font color=#1a73e8>作者：</font>** Yixuan Wang, Brandon C. Fallin, Warren E. Dixon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion prediction requires diverse future trajectories that remain consistent with observed motion and the articulated physical structure of the body. Skeletal constraints restrict individual poses, while coordinated motion depends on spatial interactions (between connected joints) and temporal interactions (between time instants). To facilitate human motion prediction in light of these constraints and interactions, we introduce Graph Structured Flow Matching (GSFM), which transports the complete future skeletal trajectory through a single conditional velocity field. The trajectory produces a spatiotemporal skeleton graph, and spatial and temporal attention couple its evolution according to skeletal relations and physical time offsets. Bone directions lie on unit spheres relative to a root joint, and tangent evolution preserves input bone lengths throughout generation. We train a learned velocity field through conditional flow matching along geodesic paths connecting random trajectories centered on the last-observed pose to recorded future trajectories. Experiments on the Archive of Motion capture As Surface Shapes (AMASS) dataset evaluate prediction accuracy, diversity calibration, and motion statistics. We demonstrate the contributions of spatial and temporal message passing in the developed architecture through an ablation study. GSFM models trained on AMASS also perform competitively on the Human3.6M skeleton without parameter updates or retraining, demonstrating applicability to an unseen skeletal structure.

---


### 139. [KinyaMed: Seeds, Not Rows -- What a Corpus Requirement Written in the Wrong Unit Fails to Constrain](https://arxiv.org/abs/2609.32234)

**<font color=#1a73e8>作者：</font>** Marius Bayizere  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Triage decides who is seen first. Building an urgency classifier for patient-voice Kinyarwanda, we found our specification could be met without producing anything it was meant to secure. We report that, and the instruments that detect it, instead of a classifier. Designed for the four languages a Rwandan health centre receives, with every instrument per-language: sentences are authored in all four arms and rows generate in one, because the frame slots those three need do not exist. Our requirement asked for one million examples; generation produced them in 130 seconds. It fails four of the nine quality gates in that specification, six when rows are attributed to their source sentence. The binding gate counts distinct authored seed phrases, not rows: at our 165, no corpus passes at any row count. Two shortfalls follow and differ: 2,835 further sentences to pass the seed-count gate, 19,835 to reach the stated million rows, because a separate gate caps a seed at 50 rows. Rows come from a machine at 7,700 per second; seeds from clinicians. A row count constrains the cheap quantity, leaves the expensive one free, and so does not constrain quality at all. Two further negatives follow. An evaluation set of 17,942 rows built from nine distinct sentences supports no verdict: our gate, which counts distinct sentences, refuses 38 of its cells and reports nothing. A model trained on a corpus of uniform surface form changes its predicted urgency for 31.5% of inputs under capitalisation and 21.0% under a single typo, reported as measurement and not attribution. A model directory shipped without its tokenizer loads without error and answers its class prior on input it cannot read, with well-formed probabilities. No figure here is evidence of model quality; the contribution is the apparatus and the negative results it produced, reproducible from a clean clone except where marked NOT REPRODUCIBLE.

---


### 140. [Arithmetic Simplicity in Stochastic Gradient Methods](https://arxiv.org/abs/2609.32240)

**<font color=#1a73e8>作者：</font>** Bin Fu, Pengfei Gu, Jose Nunez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A gradient descent method is arithmetically simple if the operations are limited to $+,-, \times$, and division $x/2^t$ with integer $t$. An arthmetically simple gradient method is easy to implement in chip design. We show how to transform AdaGrad, Adam, and AdamW into arithmetically simple.
AdamW is based on the recursion $x_{t+1}=(1-\lambda\eta)x_t-\frac{\eta }{s}m_t$ and Adam is the special case of AdamW with $\lambda=0$. We transform them into a static case with $s=S(T)$, where $T$ is the number of iterations, and $S(T)$ is a fixed function. The convergence analysis is given for a static Adam, which is also arithmetically simple.

---


### 141. [Residual Transferability in Neural Image Watermarking](https://arxiv.org/abs/2609.32241)

**<font color=#1a73e8>作者：</font>** Ziping Dong, Qi Li, Xinchao Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Neural image watermarks can be forged by extracting watermark-bearing residuals from released images and transferring them to unrelated content. While prior work has demonstrated this vulnerability, what makes these residuals transferable remains poorly understood. We formalize this vulnerability with \textbf{residual transferability (RT)}, a metric that quantifies how well watermark evidence remains decodable after transfer across unrelated images. Through comparative analyses and controlled interventions, we find that common training-side variations do not account for the large RT differences across watermarking systems; instead, architectural design plays a central role. By contrasting high- and low-RT systems and validating their architectural differences through controlled interventions, we identify two mechanisms that strengthen the dependence of watermark evidence on the cover image, thereby suppressing the residual transferability. These findings provide concrete design guidance for developing more forgery-resistant watermarking architectures. Complementarily, for existing watermarking systems where architectural redesign is impractical, we introduce \textbf{CoverLock}, a plug-and-play strategy for existing watermarking systems that strengthens such image dependence without architectural redesign. Across representative watermarking systems exhibiting high residual transferability, CoverLock achieves a more favorable security--robustness trade-off than both traditional handcrafted defenses and learned classifier-based defenses.

---


### 142. [Two-Stage Multi-View Gait Recognition with a Re-Embedding Network](https://arxiv.org/abs/2609.32244)

**<font color=#1a73e8>作者：</font>** Long Hoang Le, Trung Thanh Ngo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait recognition always remains challenging due to severe overfitting and the rigid view constraints common in single-stage approaches. We propose a two-stage framework, termed Translate-First-Then-Reason (TFTR), to address these issues. In the first stage, a shallow Siamese convolutional network with triplet loss maps Gait Energy Images (GEIs) into a 128-dimensional view-specific embedding space. In the second stage, these per-view embeddings are treated as tokens and processed by a 12-layer Transformer encoder, which re-projects them into a new space with improved cosine separability. This design enables flexible fusion of an arbitrary number of views at inference, overcoming the fixed-input limitations of prior methods. Trained on the OU-MVLP dataset (6,000 subjects) and evaluated on unseen CASIA-B across normal, bag-carrying, and coat-wearing conditions, our pipeline achieves 96.91\% single-view and 99.49\% three-view accuracy on OU-MVLP, and attains 100\% accuracy on CASIA-B with three views.

---


### 143. [Certifying Interventional Agreement Among Observationally Equivalent Causal Models](https://arxiv.org/abs/2609.32247)

**<font color=#1a73e8>作者：</font>** Sourena Khanzadeh, Daniel Platnick, Marjan Alirezaie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Observationally equivalent causal models can still disagree about what happens under intervention, because interventions create inputs that never occur in observational data. We introduce Interventional Separation Selection (ISS), which repeatedly queries the true system with an admissible intervention on which the surviving candidate models disagree, discards the candidates the outcome contradicts, and stops once no intervention within a cost bound separates the survivors. If the true system is among the candidates, this stopping condition certifies that every survivor agrees with it on every admissible intervention within the bound, a guarantee that no observational learner can give, however much data it sees. The stopping condition depends only on the survivors, so it can be checked without knowing the truth. For continuous variables the candidates form an infinite version space, and mixed-integer linear programs decide the stopping condition exactly over all of it, with agreement holding up to a tolerance. On a three-digit colored MNIST causal abstraction task in which ink hue tracks digit size, plain convolutional networks trained on examples reach zero held-out error, yet disagree with shape-based labels on 26% of single-digit edits, as often as hue-based labels do. Auditing the causal abstractions of networks observed only on such images, ISS certifies what each network perceives with 13.6 interventions per image on average, and each certificate, checked against every admissible intervention, holds whenever the network's true abstraction is among the candidates. When a network bypasses a unit that every candidate abstraction relies on, certificates covering interventions on that unit can be silently void, and twenty random validation interventions refute 69% of them.

---


### 144. [RoboSTAR: Next-Scale Autoregressive Sign Language Translation for Humanoid Robots](https://arxiv.org/abs/2609.32250)

**<font color=#1a73e8>作者：</font>** Yujia Zeng, Chensheng Peng, Yuxin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign-language interpretation in public communication relies on qualified professional interpreters and can be difficult to scale, motivating robotic signing as a complementary accessibility interface. We present RoBoSTAR, a text-conditioned sign language production (SLP) framework for generating human-centric sign motion that can be retargeted for robotic execution, with speech supported optionally through an external ASR front end. Conventional autoregressive approaches flatten motion into a single full-resolution token sequence, forcing long-range and local dependencies to be modeled at a uniform temporal granularity. RoBoSTAR instead combines part-wise Finite Scalar Quantization with next-scale autoregression, generating motion over progressively finer temporal resolutions while predicting synchronized body and hand tokens in parallel within each step. This coarse-to-fine formulation provides compact long-range context before progressively refining motion details, while self-conditioning and context corruption improve robustness to cross-scale prediction errors. The generated motion is subsequently retargeted for physical humanoid execution. Extensive qualitative and quantitative evaluations are conducted to demonstrate the effectiveness of RoBoSTAR.

---


### 145. [Why Directly Learning Periodic Trajectories Can Fail](https://arxiv.org/abs/2609.32254)

**<font color=#1a73e8>作者：</font>** Kaixin Zheng, Anita Layton  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Operator learning of periodic solutions requires deciding how simulation data should be recorded and represented. A natural choice is to integrate long enough for transients to decay and record a window wide enough to contain at least one full period of all trajectories. We find that these conservative choices can make the resulting trajectories difficult to learn, even when the underlying periodic orbits vary regularly with system parameters. Unaligned trajectories generalize poorly even within the training distribution. Phase alignment substantially improves in-distribution generalization, but models trained on a fixed physical-time window still have large errors on trajectories with periods outside the training range. We explain both failures through a common mechanism: frequency differences accumulate over time, so the target phase varies rapidly with the parameters. Predictors that cannot track this variation incur a population MSE floor in both settings; for fixed window prediction, we also derive a per-sample lower bound. We then study one of the simplest representations that escape these floors: learning an aligned, normalized waveform and its period separately. We establish regularity of the decoupled targets under ODE assumptions and show experimentally that this approach avoids both failures in ODE systems and a PDE case study.

---


### 146. [Representation Editing for Multimodal Test-Time Adaptation](https://arxiv.org/abs/2609.32263)

**<font color=#1a73e8>作者：</font>** Longfei Huang, Xiangyu Wu, Yang Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal test-time adaptation (TTA) aims to adapt a pretrained multimodal model online to distribution shift across modalities using unlabeled test data, showing broad potential in real-world applications. However, existing methods primarily focus on adjusting fused features to bridge the source-target gap, lacking explicit control over intermediate representation misalignment, which is a key driver of performance drop under distribution shift. In this work, we tackle this challenge from the perspective of representation engineering. Unlike previous TTA methods that update fusion weights in place, we propose FourIer Representation Editor (FIRE), a novel multimodal TTA approach that directly edits semantically rich intermediate representations. Specifically, we first adopt representation editors into each intermediate layer of the unimodal encoders, enabling layer-wise calibration of unimodal representations. To further enhance the diversity and stability of the low-rank editing subspaces, each representation editor performs frequency domain mixing via the fast Fourier transform to construct structured bases. Moreover, we introduce multi-level adaptation objectives to optimize these editors, jointly promoting cross-modal semantic alignment, source-target statistical alignment, and asymmetric prediction consistency. In this way, FIRE yields aligned unimodal representations for fusion and further improves prediction reliability. Extensive experiments on two widely used multimodal benchmarks under various corruption types demonstrate the superiority of FIRE over existing multimodal TTA methods.

---


### 147. [Self-Reconstruction Dynamics for Autoencoder Reconstruction Refinement](https://arxiv.org/abs/2609.32268)

**<font color=#1a73e8>作者：</font>** Hitoshi Iyatomi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard autoencoder (AE) inference uses a single encoder-decoder pass, though the latent may not be optimal for each sample under a fixed decoder. We ask whether a trained AE can reveal information for improving its own reconstruction. Repeated application of a frozen AE to its reconstruction produces transient image- and latent-space trajectories, termed Self-Reconstruction Dynamics (SRD). Although this degrades fidelity in the AEs studied here, SRD contains sample-specific information for correcting the reconstruction. We propose SRD-guided Reconstruction Refinement (SRD-RR), which predicts a latent correction from a short SRD with the AE frozen and no per-sample test-time optimization. We also introduce MSE-recov, an MSE recovery ratio relative to an empirical decoder-optimized reference. Across six datasets, SRD-RR recovers 38.6% of the empirically recoverable MSE gap with one transition and 45.3% with two. A two-transition variant trained without direct access to original images, using an SRD-derived pseudo-target, achieves 40.7% recovery and a 1.74 dB average PSNR gain. Removing trajectory information reduces the gain, while cross-sample trajectory assignment causes severe degradation, confirming strong sample specificity. Nonlinear SRD-conditioned refinement consistently outperforms fixed and trained linear latent correction. On a pretrained DINOv2-based representation autoencoder (RAE) with substantially different latent dynamics, SRD conditioning again improves a matched trajectory-free predictor. However, pixel-MSE latent refinement reveals a strong mismatch between pixel fidelity and perceptual quality, while the SRD-derived pseudo-target mitigates this degradation. Overall, SRD is a useful sample-specific refinement signal, while the objective determines how it translates into pixel and perceptual quality.

---


### 148. [Certification Frontiers for Gaussian LoRA: Independent Priors, Posterior Risk, and Prediction-Preserving Balancing](https://arxiv.org/abs/2609.32271)

**<font color=#1a73e8>作者：</font>** Joyanta Jyoti Mondal, Ibne Farabi Shihab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc Bayesian fine-tuning places Gaussians around trained low-rank adapters, yet a calibrated posterior does not by itself yield a useful generalization certificate. Such a posterior admits an informative PAC-Bayes certificate only when both the loss of its sampled predictors and its KL divergence from an admissible prior are small. In this research, we characterize this certification frontier for Gaussian LoRA posteriors and separate three interventions: changing the prior, changing the stochastic predictor, and changing only how its complexity is counted. First, an exact isotropic KL envelope eliminates the prior scale and yields a width threshold that excludes posterior widths before sampling, while a zero-KL floor identifies targets that no complexity reduction can reach at a measured risk bound. Second, we minimize KL in closed form over the full $GL(r)$ symmetry of the low-rank factors, leaving every sampled adapter product unchanged, and derive the noncentral objective required when the prior center is trained on an independent split. On a small-pool RoBERTa audit of 567 configurations, the recorded 64-draw summaries imply a certificate floor of $0.7298$ even with zero KL and Chernoff accounting, so reducing complexity alone cannot certify these posteriors at the recorded budgets. For a stable posterior in a controlled Gaussian-factor task, Chernoff accounting certifies risk below $0.1$ on 20 of 20 datasets with 1024 draws, whereas Hoeffding certifies none. On deliberately deformed synthetic rank-four factors, matrix balancing reduces KL by $29.3\%$ on average beyond scalar balancing without changing any prediction. Numerical split-prior scenarios make the remaining risk and complexity budgets explicit.

---


### 149. [Learning Through Game: Skewed Transfer of Tabular Knowledge to Strengthen Image Model](https://arxiv.org/abs/2609.32272)

**<font color=#1a73e8>作者：</font>** Longfei Huang, Shangdong Yang, Yang Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal tabular-image learning is gaining growing attention, yet it faces challenges due to tabular data unavailable at test time. A practical solution involves transferring tabular knowledge to images during training to enhance the performance of image models at inference. However, the overlooked yet important challenges lie in the modality imbalance between images and tables, as well as their asymmetric modality relationship in cross-modal transfer, which limits the auxiliary role of tabular data. To address these issues, we propose Skewed Knowledge Transfer (SKT), which asymmetrically transfers tabular knowledge to improve the image model by adaptive integration of modality gradients in a shared parameter space. Specifically, we first introduce a multimodal shared head, which allows the model to benefit from cross-modal structure without adding additional parameters. We then design a two-step Nash Bargaining strategy to effectively leverage tabular gradients. In the first step, SKT seeks a point of modality balance and uses preference awareness in the second step to steer combined gradients toward image-beneficial directions. Furthermore, we theoretically analyze the Pareto improvement and convergence of SKT. To this end, tabular knowledge is explicitly transferred to enhance image models. Empirical experiments on widely used tabular-image datasets reveal that SKT consistently improves image unimodal performance by using tabular data as auxiliary information.

---


### 150. [FSS-UBrain: Multi-region Few-Shot Brain Tumor MRI Segmentation](https://arxiv.org/abs/2609.32273)

**<font color=#1a73e8>作者：</font>** Truong Viet Vu, Nguyen Phuc Nguyen, Dang Thi Thu Hang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate delineation of whole tumor (WT), tumor core (TC), and enhancing tumor (ET) from multimodal magnetic resonance imaging remains challenging under limited annotation, cross-cohort variation, and severe target sparsity. We propose FSS-UBrain, a region-wise one-shot segmentation framework that uses a labeled positive support slice to condition binary query segmentation separately for WT, TC, and ET. Support-derived foreground and background descriptors guide query-feature adaptation, bottleneck interaction, decoder-side reconstruction, and boundary refinement. Episodic training additionally incorporates hard-negative and fully negative queries with empty-query regularization to suppress spurious foreground activation when the selected region is absent. Although inference operates on two-dimensional support--query slice pairs, checkpoint selection, threshold calibration, and final evaluation are performed after volumetric reconstruction. FSS-UBrain is evaluated on a held-out BraTS 2020 split and under target-supported cross-cohort protocols on BraTS 2023 and BraTS-Africa. Cases used as target support are excluded from the query cohorts, and no target-domain fine-tuning or test-time parameter updates are performed. On BraTS 2020, FSS-UBrain achieves volumetric Dice scores of 89.82%, 82.14%, and 77.42% for WT, TC, and ET, respectively, with corresponding 95th-percentile Hausdorff distance (HD95) values of 11.12, 9.01, and 4.46 mm. It also achieves the highest mean Dice and lowest finite-pair mean HD95 point estimates on BraTS 2023 and BraTS-Africa among the compared few-shot methods. These findings support target-conditioned few-shot segmentation while highlighting sensitivity to support selection and cohort-specific variation.

---


> [!TIP]
> 当前位于：**101-150**（第 3/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
