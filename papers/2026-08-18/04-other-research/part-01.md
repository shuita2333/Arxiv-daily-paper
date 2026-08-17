# 📦 其他研究 | 2026年08月18日

> 本类共 **165** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-165](./part-04.md)

---

### 1. [L-FNO: Lorentzian Fourier Neural Operator for Stochastic Event Dynamics](https://arxiv.org/abs/2608.13562)

**<font color=#1a73e8>作者：</font>** Songhee Kang, Jihoon Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern operational systems face uncertainty even in routine conditions, where rare, bursty, and self-exciting events emerge from both exogenous covariates and endogenous event dynamics. Standard neural operators are typically trained as regression-style function-to-function models rather than conditional-intensity estimators, limiting their suitability for sparse event regimes. We introduce the Lorentzian Fourier Neural Operator (L-FNO), a stochastic neural operator that combines an FNO-style covariate path, Lorentzian spectral kernels for history-dependent excitation, and a likelihood-based training objective. We evaluate L-FNO on eight synthetic point-process benchmarks and three real-world datasets covering disease outbreak prediction and semiconductor fault or defect detection. L-FNO improves event likelihood, calibration diagnostics, and rare-event detection over regression- and likelihood-based neural operator baselines. These results show that structured spectral memory and likelihood-based learning provide effective inductive biases for neural operator models of stochastic event dynamics.

---


### 2. [A Two-Validator Web Interface for Structured Geometry Figure Annotation](https://arxiv.org/abs/2608.13569)

**<font color=#1a73e8>作者：</font>** Sabin-Codrut Badea, Adrian-Marius Dumitran  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Annotating geometric figures from scanned documents has long been addressed by adapting generic annotation tools, tools not originally designed for such tasks, to use cases where they are suboptimal. An interactive web interface is described that is purpose-built for validating automatically generated geometry figure descriptions, allowing annotators to review and correct conditional declaration language (CDL) descriptions while simultaneously adjusting figure crops and editing source problem text. Submissions pass through two independent annotators in sequence, with each round fully logged. The interface is currently deployed and has been used by 12 annotators to validate 483 problem entries.

---


### 3. [The Architect: Interactive Visualization of Deep Learning Mathematics Directly in Microsoft Excel](https://arxiv.org/abs/2608.13572)

**<font color=#1a73e8>作者：</font>** Mohammad Imrul Jubair, Tom Yeh  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present The Architect, a system that turns Microsoft Excel into an interactive view of deep learning mathematics. A user describes a neural network in a compact table. The system then generates a workbook that shows the full forward pass and, when requested, the backward pass and parameter updates. Computed values appear as live spreadsheet formulas, while user-controlled values such as inputs, weights, labels, and hyperparameters remain editable. Excel reactively updates the dependent computations through its recalculation engine.
Most deep learning tools hide the numerical details behind library calls. Many visualization tools show architecture diagrams or training summaries, but they do not expose the full arithmetic of the model. The Architect focuses on that missing middle layer. It makes matrices, activations, losses, gradients, and updates visible as inspectable spreadsheet regions, with editable controls for values users naturally manipulate. The system also produces aligned PyTorch snippets, which helps users connect formulas to implementation.
This report describes the motivation, design, implementation, and use cases of The Architect. We show how the system supports introductory arithmetic tracing, learning-rate exploration, diagnosis of dying ReLU, and inspection of vanishing gradients. The main idea is simple: spreadsheets already support formulas, direct editing, reactive recomputation, and tabular layout. These properties make them a useful medium for understanding how small educational and diagnostic neural networks compute.

---


### 4. [Interactive Analysis of Global Explanations using Aggregated Class Activation Maps for Network Data](https://arxiv.org/abs/2608.13575)

**<font color=#1a73e8>作者：</font>** Igor Cherepanov, David Sessler, Alex Ulmer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent machine learning (ML) advances have demonstrated that deep learning (DL) achieves impressive results in different application domains, including the classification of computer network traffic to corresponding applications. However, the data frequently contains diverging patterns within a single predicted class. This presents a significant challenge to the ability to provide a clear and comprehensive explanation and emphasizes the necessity for tools capable of detecting and analyzing these patterns. Furthermore, the capacity to extract descriptive rules for classes is a crucial requirement in network traffic analysis and intrusion detection, particularly when leveraging advanced tools like next-generation firewalls. We provide a visual-interactive system that explains predictions of classes for network traffic. Global explanations derived from multiple samples of a given class contribute to understanding model predictions. Visualization of global explanations enables recognition of different patterns that offer experts a more comprehensive overview of its characteristics. We introduce a prototype that facilitates visual exploration and refinement of global explanations, enabling network experts to detect and refine new patterns for specific applications. These explanations support the identification of misleading features and the formulation of new rules for the management of networks. Our approach also aims at enabling ML experts to acquire new insights, including the possibility of separating or merging classes and the development of more accurate and reliable DL models. Our proposed prototype was evaluated by experts in machine learning and network analysis.

---


### 5. [AI Evaluation Should Work With Humans](https://arxiv.org/abs/2608.13577)

**<font color=#1a73e8>作者：</font>** Jan Kulveit, Gavin Leech, Tomáš Gavenčiak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This position paper argues that the dominant paradigm of AI evaluation (which focuses on superhuman autonomous performance and so implicitly targets the goal of replacing humans) is guiding AI development in the wrong direction. Instead, the AI community should pivot to evaluating the performance of human--AI teams. We argue that this collaborative shift will foster AI systems that act as true complements to human capabilities and therefore lead to far better societal outcomes than will the current process.

---


### 6. [BCMT: Blockwise Causal Memory Transformer](https://arxiv.org/abs/2608.13578)

**<font color=#1a73e8>作者：</font>** Rachid Arezki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer architectures rely on dense self-attention to model long-range dependencies, but this mechanism exhibits quadratic complexity with respect to sequence length. We introduce BCMT (Blockwise Causal Memory Transformer), an architecture for long-context language modeling that decouples local token interactions from global context propagation. Dense causal self-attention is applied independently within local blocks, while each block produces an adaptive summary aggregated through an exponential causal memory. This memory is subsequently injected back into the token representations, enabling efficient propagation of long-range contextual information without relying on explicit global attention. Unlike standard Transformers and recurrent memory architectures, BCMT maintains neither dense interactions between distant tokens nor learned memory states. Its memory mechanism is fully parallelizable and remains compatible with standard implementations of dense self-attention. Experiments on language modeling with context lengths of up to 1024 tokens show that BCMT achieves validation performance comparable to that of Dense Transformers while significantly improving training throughput and reducing memory consumption. An ablation study further confirms that these improvements arise from the proposed memory mechanism. These results demonstrate that an exponential causal memory constructed from block summaries provides an effective alternative to dense global attention mechanisms for long-context language modeling.

---


### 7. [Regulation, Power, and the Compliance 1 Paradox: A Longitudinal Study of Smart Homes](https://arxiv.org/abs/2608.13582)

**<font color=#1a73e8>作者：</font>** Wael Albayaydh, Ivan Flechais, Rui Zhao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Smart home technologies are becoming increasingly embedded in domestic environments, yet their implications for power, privacy, and inequality remain insufficiently understood, particularly in non-Western contexts. This paper presents a longitudinal socio-technical study of smart home adoption in Jordan, examining how cultural norms, regulatory frameworks, and everyday technological practices shape domestic power dynamics.
Building on our 2022 study, we employ a two-phase grounded theory approach comprising (1) a secondary analysis of 30 interviews and (2) 28 new interviews conducted in 2025 with returning and new participants, including household members, domestic workers, policymakers, and civil society advocates. This design provides a rare longitudinal perspective on how regulatory and technological change reshapes domestic surveillance practices.
Our findings reveal a compliance paradox: although Jordan's 2023 Data Protection Law has increased privacy awareness, it also enables new forms of exploitation by leaving domestic contexts largely outside its scope. We identify three dynamics: (1) the normalization of passive surveillance through convenience and legal compliance; (2) regulatory ambiguity that shifts responsibility to households, reinforcing existing hierarchies; and (3) constrained resistance among domestic workers facing intensified monitoring.
We contribute a longitudinal account of how privacy regulation is appropriated within socio-cultural systems to reproduce existing inequalities. We conclude by identifying four intervention spaces across design, policy, and advocacy, emphasizing the need for contextually grounded approaches to privacy governance in smart home ecosystems.

---


### 8. [UltraArUco: A Lightweight Multilingual Library And Framework With Low-Latency Real-Time Marker-Based Tracking System For Mobile AR Interaction](https://arxiv.org/abs/2608.13584)

**<font color=#1a73e8>作者：</font>** Mikhail Kiselev, Aleksandr Marukhin, Ivan Snegirev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> UltraArUco - a lightweight multilingual library and framework for low-latency, real-time marker-based tracking in mobile augmented reality. Unlike standard OpenCV-based implementations, UltraArUco introduces an optimized multilingual wrapper that reduces per-frame latency by five times, while maintaining high accuracy. Distributed Wi-Fi architecture provides portability, connects a mobile device (camera input) with a PC-based visual application, enabling responsive interactions. The framework is validated through an interactive piano simulation, where static ArUco markers on keys enable occlusion-based note triggering, and hand-mounted markers provide spatial gesture recognition. UltraArUco's system requirements make it perfect for resource-constrained mobile AR applications, demonstrating a viable AR music application without specialized equipment.

---


### 9. [The Tool-to-Entity Threshold: Parasocial Dynamics of Personalised AI Agents in Shared Social Spaces](https://arxiv.org/abs/2608.13586)

**<font color=#1a73e8>作者：</font>** Leonardo Borges, Asif Q. Gill  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI agents acquire names, avatars, phone numbers, and persistent personalities, they increasingly inhabit the same messaging platforms and group conversations as the humans they serve, crossing from tools their users operate into social entities their users relate to. This reclassification carries under-explored consequences for consent, emotional attachment, and group dynamics, yet no existing framework identifies the specific infrastructural markers that cause it. We propose the identity marker framework: six design variables (naming, visual identity, contact presence, personality derivation, social co-presence, and persistence) that collectively trigger a discrete psychological reclassification, operating independently of model capability. The framework is derived inductively and read through two established lenses: parasocial interaction theory (Horton & Wohl, 1956) and the Computers Are Social Actors paradigm (Nass et al., 1994). We further identify four novel dynamics that arise when such an agent participates in existing group conversations: bidirectional information asymmetry, delegation legibility, social norm negotiation, and parasocial contagion. Our method is autoethnographic: the first author built and deployed a personalised agent into WhatsApp and Signal group chats over two months of live use, supplemented by twelve structured interviews with the group members who encountered it. We treat this as a preliminary qualitative evaluation of the framework, with controlled experimental validation left to future work. The strongest design implication runs through all four dynamics: in shared social spaces, consent to an agent's presence is categorically distinct from consent to its processing of the messages exchanged there, and existing consent frameworks collapse the two.

---


### 10. [Robust XGBoosting for Regression](https://arxiv.org/abs/2608.13590)

**<font color=#1a73e8>作者：</font>** Iris Aragón Mladosich, Christophe Croux  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> XGBoost is a very popular and powerful method for prediction. It iteratively fits simple decision trees to the residuals of the previous step. An efficient and scalable implementation is available. The standard loss function for XGBoost is the quadratic loss, but a Huber loss can also be used. In this paper, we study the robustness of XGBoost and show that its performance can be affected by vertical outliers and leverage points. To address this, we explore alternative loss functions, based on M-, S-, and {\tau} -estimators from robust regression. Our results indicate that a two-step procedure, referred to as MM-XGBoost, provides the best trade-off between robustness and prediction accuracy.

---


### 11. [Hard Cases, Bad Labels: Testing Error Exposure and Error Location in Uncertainty Sampling Under Bounded Label Noise](https://arxiv.org/abs/2608.13601)

**<font color=#1a73e8>作者：</font>** John Myron Uy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active learning can reduce labeling cost by selecting informative examples, but the most uncertain examples may also be the hardest to label correctly. This study tests whether uncertainty sampling fails because it acquires more corrupted labels or because errors concentrated in difficult regions are especially harmful. Margin-based uncertainty sampling is compared with random sampling under clean labels, random classification noise (RCN), and bounded difficulty-dependent noise on three public binary tabular datasets. The design uses 100 paired seeds, nine expected noise rates from 0 to 0.30, annotation budgets from 20 to 120, and logistic regression with regularization re-selected by cross-validation at every budget. An exposure-matched RCN control aligns mean final acquired corruption, while a clean-label extension reaches budget 400. Under clean labels, uncertainty sampling improved normalized balanced-accuracy area under the learning curve by 1.09 to 1.77 percentage points on all datasets. Difficulty-dependent noise reduced this advantage more than RCN at six of eight rates on Breast Cancer Wisconsin, but at no tested rate on Banknote Authentication or MAGIC Gamma Telescope. Exposure-matched analyses found no corrected evidence for a universal additional penalty from structured error location. On clean MAGIC data, uncertainty sampling improved balanced accuracy while reducing average precision and true-positive rate at fixed false-positive rates. Thus, uncertainty sampling was label-efficient, but its apparent robustness depended on dataset, budget, noise structure, and evaluation metric.

---


### 12. [Cross-Disciplinary Taxonomy and Modeling of Misunderstanding Generation, Amplification, and Detection, from Pragmatics to AI Agents](https://arxiv.org/abs/2608.13604)

**<font color=#1a73e8>作者：</font>** Babak Abbaschian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detection of misunderstanding is an urgent problem to solve because communication has moved away from real-time, in-person interaction and is increasingly handled by AI-mediated channels. This shift cuts communicators off from the resources repair depends on faster than new means of detection are being built. In this paper we analyse misunderstanding as a layered process in which a divergence is generated, may then be amplified, and is either detected and repaired or left to persist unnoticed. Consolidating accounts from nine fields of research that do not ordinarily cite one another, we identify eleven exact failure modes and show that each operates at a specific point in a communicative process rather than anywhere within it. Those points give eight analytical layers, derived from the literature rather than adopted from an existing model. Eight of the mechanisms primarily generate a divergence, two primarily amplify one already present, and one governs whether a divergence is detected and repaired. We model the eight layers formally, extending information and communication theory from the transmission of signals to the reconstruction of meaning, and we supply a source-by-source evidence matrix that makes every rating auditable, a coding manual, and nine analysed dialogue cases. No prior classification of misunderstanding both locates mechanisms at points in the process and types them by function.

---


### 13. [MobileMem: Learning from a Year of Mobile Experiences](https://arxiv.org/abs/2608.13606)

**<font color=#1a73e8>作者：</font>** Xinle Deng, Yida Xue, Xiangyuan Ru 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The next generation of AI agents is increasingly moving beyond systems that answer isolated questions toward persistent personal assistants that can understand, remember, and continuously learn from users' experiences. Such assistants require long-term memory to accumulate and leverage user-specific experiences over time, yet existing benchmarks remain inadequate for realistic mobile settings, where experiences are heterogeneous, multimodal, evolving, and deeply personal. We introduce MobileMem, a benchmark and framework for studying on-device long-term memory, grounded in a year-scale collection of mobile experiences. MobileMem employs a knowledge-grounded synthesis pipeline to construct coherent and temporally consistent long-horizon trajectories from user-app sessions. It provides complementary text and multimodal settings covering multi-hop and temporal reasoning, knowledge updating, and implicit preference inference. Specifically, MobileMem enables agents to remember the past, understand the present, and adapt to the future. By modeling experiences rather than isolated facts, MobileMem moves memory beyond information retrieval toward experiential intelligence for continuous personal learning.

---


### 14. [Algorithm Design and Physician Liability](https://arxiv.org/abs/2608.13618)

**<font color=#1a73e8>作者：</font>** Shujie Luan, Shubhranshu Singh, Tinglong Dai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A single clinical algorithm can deliver unequal accuracy across patient groups, and concern about such disparity has grown as artificial intelligence (AI) spreads through clinical decision-making. In response, a liability rule introduced in the United States holds healthcare providers responsible when their reliance on disparate algorithms contributes to erroneous clinical decisions. We examine how such liability considerations reshape (i) an AI firm's algorithm design decisions that drive group-specific accuracy and (ii) a physician's decisions to use AI in healthcare delivery. The AI firm designs an algorithm for two patient groups, and improving accuracy for the disadvantaged group is more costly. The physician (who remains the accountable decision-maker) then decides whether to consult AI, weighing the reduction in clinical uncertainty against expected liability exposure when AI errors disproportionately affect the disadvantaged group. We find the liability rule can induce disparate use of AI: the physician may reduce AI use overall and, over an intermediate range of liability, rely on AI less for disadvantaged patients. The effect is non-monotone. As liability increases, the physician's use of AI for disadvantaged patients first declines, then rises as the firm reallocates investment toward reducing disparity or switches to an equal-accuracy design. Mandating equal algorithmic accuracy across patient groups can then inadvertently harm both groups, because a uniform accuracy requirement distorts the firm's investment incentives and the physician's equilibrium AI-use decisions.

---


### 15. [Your Probabilistic JEPA Is Secretly a Hidden Markov Model: A State-Space Interpretation of Joint-Embedding Predictive Learning](https://arxiv.org/abs/2608.13621)

**<font color=#1a73e8>作者：</font>** Yongchao Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A hidden Markov model (HMM) combines three roles: inference of a hidden-state belief from observations, propagation through a Markov transition, and emission back to observation space. We show that full, time-indexed Predictive Information Bottleneck VJEPA (PIB-VJEPA) exposes the same computational structure: a stochastic context encoder plays the role of an amortized filtering distribution, a probabilistic predictor defines latent-state dynamics, and a decoder, inverse target encoder, or induced implicit conditional supplies the emission direction. We distinguish 4 progressively stronger levels of correspondence and give sufficient conditions for exact sequence-level HMM equivalence. To make the connection concrete, we introduce Markov-Chain JEPA (MCJEPA), which replaces the latent predictor by a learned transition matrix; in the finite time-homogeneous case, matrix powers guarantee exact multi-horizon Chapman--Kolmogorov consistency. Conditioned discrete-state transitions, continuous-state Markov kernels, and continuous-time dynamics extend this construction, while deterministic temporal JEPA appears as a degenerate Dirac-kernel special case. We further interpret predictive information-bottleneck learning as seeking a compact predictive state: compression promotes minimality, while residual predictability tests sufficiency. Controlled experiments support transition composition, the filtering interpretation, predictive Markovization in a known synthetic process, and the distinction between JEPA latent prediction and HMM-style sequence learning. Together, these results give temporal JEPA a principled state-space interpretation.

---


### 16. [ARC: Fair Relative Advantage Comparison in Open-Ended Real-World Interaction](https://arxiv.org/abs/2608.13622)

**<font color=#1a73e8>作者：</font>** Yongqi Tong, Tan Li Hui Faith, Choy Zhen Wen Marcus 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-ended real-world interaction admits multiple valid behaviors: an agent may answer directly, ask for clarification, provide progress updates, or confirm before acting. This flexibility breaks a core assumption behind group-based RL: rollouts compared within a group are no longer guaranteed to be behaviorally comparable. As a result, reward-model preferences over interaction style can distort relative advantages and steer optimization toward reward-preferred behaviors rather than context-appropriate ones. We formalize this as a \textit{reward fairness problem} and propose \textbf{ARC} (Advantage Regularization via Conditioning), a training recipe that restores fairer relative comparison through strategy-conditioned rollout grouping, together with hybrid rewards and entropy regularization. We study ARC in our proposed \inter, a novel paradigm for responsive, steerable, and execution-aware user-agent interaction that decouples user-visible communication from latent reasoning and tool use. \inter\ also provides the annotation and distillation pipeline for constructing \inter-86K, our strategy-annotated training corpus for supervised and RL training. Empirically, ARC substantially strengthens the core $\tau/\tau^2$ tool-use benchmarks, while \inter\ reduces time-to-first-token from 4.91s to 1.27s relative to a think-style baseline. Together, these results suggest that a central bottleneck in open-ended interactive learning is not only how agents are rewarded, but whether their behaviors are compared fairly in the first place. The ARC implementation and \inter-86K training data will be released.

---


### 17. [Reward Machines for Signal Temporal Logic](https://arxiv.org/abs/2608.13625)

**<font color=#1a73e8>作者：</font>** Alper Kamil Bozkurt, Shangtong Zhang, Yuichi Motai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Signal temporal logic (STL) provides a formal language for specifying real-time properties of real-valued observations, along with a quantitative robustness score for monitoring satisfaction. Control synthesis from STL specifications is of interest since manual controller design becomes infeasible as real-world systems grow in complexity. Moreover, many modern autonomous and AI-enabled systems lack accurate and complete system models, which makes optimization-based synthesis approaches unsuitable and motivates learning-based control. Prior work uses STL robustness scores as rewards in reinforcement learning (RL) to obtain control policies satisfying given specifications; however, robustness depends on execution history, leading to intractable state space expansion for general long-horizon specifications with arbitrarily nested temporal operators. This work introduces a novel automata-based approach that provides an efficient memory mechanism and associated Markovian rewards suitable for RL frameworks. Our approach constructs a timed alternating automaton from the given STL specifications, augments the state space with automaton locations and clock valuations, and derives rewards from the automaton acceptance condition. We empirically demonstrate that our approach learns policies that achieve higher robustness scores and satisfaction rates than those learned by existing approaches using robustness-based rewards.

---


### 18. [Robust Dual-Model Collaborative Random Vector Functional Link Network](https://arxiv.org/abs/2608.13628)

**<font color=#1a73e8>作者：</font>** A. Quadir, A. Rahaman, Mushir Akhtar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random vector functional link (RVFL) networks are lightweight and fast neural models that offer efficient training and strong generalization through randomized hidden-layer weights and direct input-output connections. However, conventional RVFL models are sensitive to noisy labels, outliers, and imbalanced data, which limits their performance in real-world applications. To address these challenges, we propose the kernel risk-sensitive mean p-power based RVFL (KRPRVFL) model, which integrates the computational efficiency of RVFL with the robustness of the kernel risk-sensitive mean p-power (KRP) criterion. By replacing the standard least-squares objective with a KRP-based loss, KRPRVFL adaptively reduces the influence of corrupted or unreliable samples during training, resulting in improved stability and generalization. Additionally, a collaborative learning mechanism is introduced to enable adaptive interaction among model components, further enhancing robustness in complex and noisy environments. The proposed framework also leverages kernel-induced feature mapping to capture nonlinear relationships without requiring explicit hidden-layer selection, maintaining both efficiency and scalability. Extensive experiments on UCI and KEEL benchmark datasets demonstrate that KRPRVFL consistently outperforms baseline models in terms of accuracy, robustness, and statistical significance, highlighting its effectiveness as a fast, scalable, and reliable solution for challenging classification tasks.

---


### 19. [Exploring ESC Winners with Nested Diagrams](https://arxiv.org/abs/2608.13630)

**<font color=#1a73e8>作者：</font>** Anurag Sharma, Marcel Nöhre, Gerd Stumme  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present ConceptFlow, a scikit-learn-compatible Python library for Formal Concept Analysis that constructs and renders nested line diagrams from many-valued formal contexts. Given a many-valued context and a partition of its attributes into conceptual scales, ConceptFlow performs conceptual scaling, computes the factor lattices, identifies filled nodes of the corresponding subdirect product, and produces an interactive visualization.
We apply ConceptFlow to the winners of the Eurovision Song Contest from 1975 to 2025, exploring relationships between voting patterns and musical characteristics. Voting support is captured by an outer scale spanning regional, cultural, historical, and political dimensions, while an inner scale captures musical characteristics via tempo and key. The resulting nested line diagram reveals implications across both scales, exposing dependencies between how winning entries were voted for and the musical properties they share.

---


### 20. [Contrastive Learning for Interpretable Anomaly Detection at Collider Experiments](https://arxiv.org/abs/2608.13652)

**<font color=#1a73e8>作者：</font>** Haoyi Jia, Sagar Addepalli, Julia Gonski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generic event-level anomaly detection for collider physics has two recurring problems: anomaly scores are hard to interpret, and they correlate strongly with energy scale and object multiplicity. We present Organized Representation via Contrastive learning for Anomaly detection (ORCA), a two-stage framework that first learns an embedding space via supervised contrastive learning across a diverse set of physics processes, then runs a standard autoencoder in that space to generate event-level anomaly scores. On a simulated dataset consistent with conditions at the High-Luminosity Large Hadron Collider, ORCA delivers significant gains in both breadth and depth of sensitivity to new physics signals with respect to a baseline autoencoder architecture. Beyond improved sensitivity, the contrastive embedding makes the anomalous sample interpretable: because known processes occupy distinct regions of the space, a maximum-likelihood template fit to the embedding distributions can attribute events in an anomalous sample to template physics processes with quantified uncertainties. We demonstrate that the fit accurately recovers injected signal yields, including for signals excluded from the training of the embedding, and characterizes signals absent from the template library through the known processes they most resemble. These results establish ORCA as a route to interpretable anomaly detection-based searches at colliders, where the embedding geometry carries higher dimensional physics information compared to standard one-dimensional output fits, enhancing downstream statistical analysis.

---


### 21. ["I Thought You Were The Uncensored Place": Norms, Rules, and Moderation in AI-Generated Sexual Content Communities](https://arxiv.org/abs/2608.13659)

**<font color=#1a73e8>作者：</font>** Lucy Qin, Jaron Mink, Elissa M. Redmiles  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As AI-generated sexual content (AIG-SC) is increasingly produced, online communities have emerged to support creators' needs. To understand whether and how community governance attempts work to prevent abuse while supporting free expression, we interviewed 24 members and moderators of large AIG-SC online communities (10,000+ members) with stated rules against creating and sharing abusive content (e.g., AI-generated CSAM). Through in-depth interviews, we offer insight into: (1) how and why these communities form; (2) implicit community norms; (3) explicitly stated rules---and their operationalization via content moderation; and (4) tensions between community values and moderation that leave space for abusive behavior.
Our findings reveal a complex picture: while many creators and communities have personal boundaries against abuse, advice and resources for creating any form of AI-generated sexual content are accessible to users regardless of their intentions. Further complicating community moderation are norms that center anti-censorship and non-judgment, which leave moderators to justify their actions using the limits of the law and terms of service. We end by reflecting on the ways in which technical, community, and legal governance may most effectively mitigate the production of abusive content.

---


### 22. [What to Preserve, Where to Adapt: A Depth-Wise Analysis of Forgetting in Continual Gynecological Image Segmentation](https://arxiv.org/abs/2608.13660)

**<font color=#1a73e8>作者：</font>** Amal Saqib, Tausifa Jan Saleem, Numan Saeed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation models are typically trained under the assumption that all data are available simultaneously. However, in clinical practice, datasets often arrive sequentially, requiring models to adapt continuously to evolving data distributions. We study this problem in gynecological image segmentation, where substantial heterogeneity across imaging modalities, anatomical structures, and annotation protocols creates a particularly challenging continual learning setting. Under these large distribution shifts, existing continual learning methods struggle to preserve previously learned knowledge, leading to catastrophic forgetting. To better understand forgetting in this setting, we investigate how different encoder--decoder regions influence segmentation performance and forgetting during continual gynecological segmentation. Through block-wise ablation analysis, we observe that ablating early encoder and late decoder regions results in the largest performance degradation, indicating that segmentation performance depends unevenly across the network hierarchy. Using controlled adaptation experiments, we further show that forgetting remains limited when updates are restricted to bottleneck-adjacent regions, but increases sharply once shallower encoders and decoders become trainable, even when only a small subset of parameters is updated. These findings suggest that forgetting in the encoder-decoder architecture is strongly influenced by where updates occur across network depth during continual learning. Full code and analysis pipelines will be made publicly available upon acceptance.

---


### 23. [Multiphase-Diff: Diffusion-Based Generative Modeling for High-Contrast Multiphase Physical Systems with Sharp Interfaces](https://arxiv.org/abs/2608.13669)

**<font color=#1a73e8>作者：</font>** Yining Huang, Zhenyu Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physics-constrained diffusion for high-contrast, sharp-interface multiphase fields faces three coupled difficulties. At coefficient jumps, expanded pointwise strong-form PDE residuals contain singular gradient terms that can penalize physical interfaces. Under extreme contrast, low-magnitude phases may fall below the diffusion noise floor and be erased, misscaled, or generated with negative coefficients, while a global likelihood scale allows high-magnitude phases to dominate supervision. We therefore propose Multiphase-Diff, which makes three corresponding contributions: (i) a conservative flux residual that avoids differentiating discontinuous coefficients and enforces discrete conservation; (ii) an analytic bijective representation that maps low-amplitude signals to order-one latent scales and guarantees coefficient positivity through exponential decoding; and (iii) a Jacobi-preconditioned likelihood that normalizes local residual scales for balanced supervision. Experiments on three complementary multiphase benchmarks demonstrate the superiority of Multiphase-Diff over seven baselines in both physical and distributional fidelity and its robustness across phase contrasts and compositions, establishing its effectiveness for scientific sample generation in this challenging regime.

---


### 24. [PROVE: Training-Free Prompt Recovery using Verifiable Evidence](https://arxiv.org/abs/2608.13671)

**<font color=#1a73e8>作者：</font>** Rupayan Mallick, Mahsa Khoshnoodi, Sarah Adel Bargal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image models can generate highly realistic images from natural-language prompts, while recent advances in prompt inversion have made it increasingly feasible to recover those prompts from generated outputs, raising new concerns for copyright protection and content ownership. As prompt marketplaces emerge, recovered prompts can enable both the unauthorized reproduction and redistribution of copyrighted creative works, and the exposure of the prompts that encode an artist's creative recipe in AI-generated content. Existing prompt inversion methods rely on gradient-based optimization, autoregressive captioning, or reinforcement learning. However, optimization-based methods often produce unreadable prompts, captioning methods hallucinate unverified details, and RL-based approaches frequently overfit to specific generators while introducing evaluation circularity. We introduce PROVE (Prompt Recovery with Verified Evidence), a training-free, black-box prompt inversion attack that reconstructs prompts by composing verifiable scene descriptions rather than optimizing token sequences, targeting both original copyrighted works and AI-generated content. The resulting prompts are fully auditable, with every recovered claim grounded in explicit image evidence, and are formalized through a precision-constrained recall maximization objective. Across MS-COCO, Flickr30K, and Lexica, using state-of-the-art text-to-image generators, PROVE consistently outperforms optimization, captioning, and RL-based baselines on image similarity (DINO, LPIPS) and text-image alignment (CLIP), without any training, generator access, or fine-tuning, demonstrating a stronger and more practical prompt inversion attack.

---


### 25. [Learning to Assemble Novel Structures with Unfamiliar Parts under Semantic Constraints](https://arxiv.org/abs/2608.13684)

**<font color=#1a73e8>作者：</font>** Jonghyuk Park, Alex Lascarides, Subramanian Ramamoorthy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper describes a neurosymbolic architecture for learning to assemble novel structures using evidence from embodied conversations and task demonstrations. We focus on scenarios where an agent encounters, after deployment, semantic constraints on structures--in other words, constraints as to which part types and features make valid structures--that were not available during training, and where it is initially unaware of the relevant structure and component part concepts. The agent must acquire and exploit such knowledge through user interactions while attempting assembly. We study this setting in a simulated toy truck assembly domain, learning from symbolic evidence encoded in natural language and from dense visual observations. Our experiments show that communicating semantic constraints through natural language (e.g., "dump trucks have a dumper") yields more data-efficient online adaptation than relying only on task demonstrations and/or only naming the parts through natural language.

---


### 26. [Weird Machines in Transport Layer Security](https://arxiv.org/abs/2608.13685)

**<font color=#1a73e8>作者：</font>** Michael Collins, Jada Cumberland, Brianne Dunn 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Weird machines are latent computational capabilities that emerge from the composition of architectural components. Prior work has studied this phenomenon extensively in software systems, including x86 instructions, ELF metadata, and page tables, and more recently in cyber-physical systems such as industrial control networks. This paper extends weird machine theory to a new domain: the Transport Layer Security (TLS) handshake and its two dominant implementations, OpenSSL and BoringSSL.
We show that legitimate TLS primitives, including session cache entries, renegotiation logic, extension parsing, and certificate verification steps, compose into Turing-complete systems whose computation is coupled to authentication and trust decisions rather than physical actuation. We formalize this coupling, which we call trust actuation, and argue that any TLS implementation providing session storage, arithmetic on sequence counters, conditional branching on handshake state, and iteration through resumption or retry loops satisfies the conditions for arbitrary computation.
We validate this theory with two working demonstrations built on real OpenSSL code paths. The first, a sentinel system, composes standard TLS primitives into a defensive mechanism that detects anomalous handshake behavior. The second, an authentication bypass, composes the same class of primitives into an attack that defeats a cipher-strength policy check through mid-connection renegotiation, without any memory corruption or external malware. Both demonstrations run against real server and client binaries in Docker.

---


### 27. [SAGE: Surrogate-gradient Adaptation via Attention-Guided Entropy for Spiking Transformers](https://arxiv.org/abs/2608.13702)

**<font color=#1a73e8>作者：</font>** Kiran Nair, Rodrigue Rizk, KC Santosh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs) offer an energy-efficient alternative to conventional deep neural networks by exploiting sparse event-driven computation, but their training remains challenging because the non-differentiable spike function requires surrogate gradients whose fixed shape may be suboptimal across layers and training stages. In this work, we introduce SAGE, an uncertainty-modulated surrogate-gradient mechanism for Transformer-based SNNs. SAGE estimates block-level uncertainty from normalized self-attention entropy and uses this signal to adapt the surrogate-gradient slope during training while leaving the inference model unchanged. By modulating only the training-time surrogate parameter, the proposed method preserves the original architecture and deployment cost while improving optimization flexibility. Experiments on CIFAR-10/100 demonstrate that SAGE achieves improved accuracy over fixed-surrogate baselines, with results up to 1-2\% consistent gains across multiple simulation time steps. These results highlight the potential of attention-derived uncertainty as a lightweight training signal for adaptive surrogate-gradient learning in transformer-based SNNs.

---


### 28. [The Capturing and Logging Ecological Virtual Experiences and Reality (CLEVER) - Job Simulator Dataset](https://arxiv.org/abs/2608.13715)

**<font color=#1a73e8>作者：</font>** Qidi J. Wang, Xiaozheng Wang, Akhilesh M. Anand 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual reality (VR) motion tracking and interaction data has become increasingly recognized as valuable for machine learning experiments for a variety of purposes, including predicting user identities, predicting user attributes like gender and age, predicting retention and learning, and more. However, there exist a limited number of publicly accessible VR motion datasets. In this paper, we present a new open-source dataset of 95 participants playing the SteamVR game Job Simulator. Additionally, we review existing datasets, detail our study procedure, describe our data collection process, list attributes of our dataset, and suggest future work, impact, and applications.

---


### 29. [StreamHear: Domain-Adapted Pseudo-Labeling for Semi-Supervised Streaming Speech Recognition](https://arxiv.org/abs/2608.13717)

**<font color=#1a73e8>作者：</font>** Zefang Liu, Chenyang Zhu, Sangwoo Cho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Streaming automatic speech recognition (ASR) underperforms on domain-shifted target audio, where labeled in-domain data is costly to prepare while unlabeled audio is abundant. We present StreamHear, a semi-supervised pipeline that adapts a pretrained streaming student by fine-tuning an offline transducer teacher on the labeled training set, generating pseudo-labels on the unlabeled portion, and fine-tuning the student on the mixture. We further introduce a prior-regularized dynamic-programming realignment step that fixes chunk-level word placement using an ASR-hypothesis anchor. Across four datasets spanning financial calls, prepared read speech, and phone-quality dialogue, StreamHear consistently outperforms supervised student fine-tuning and narrows the gap to the offline teacher.

---


### 30. [Coverage Aware Active Evaluation for Failure Discovery with Paired Systems](https://arxiv.org/abs/2608.13719)

**<font color=#1a73e8>作者：</font>** Anjali Parashar, Rachel Luo, Apoorva Sharma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous systems can fail in rare and heterogeneous ways, making real-world failure discovery difficult under limited testing budgets. Although cheaper proxies such as simulators, lower-fidelity systems, or related policies can be sampled extensively to find failures, proxy failures often do not transfer to the real world due to sim-to-real and system-to-system gaps. The key challenge is therefore to effectively leverage proxy system information for accurate prediction of severe target system failures. We propose an adaptive failure discovery method that combines proxy evaluations with limited target system results to guide scenario selection for target system testing. Our method learns a local predictor of target risk by correcting proxy failure signals using control-variate-inspired residual modeling. To find failures that are both likely and diverse, we combine this predictor with a support-aware mutual-information objective that favors realistic, well-supported regions while expanding coverage across failure modes. Across autonomous driving, manipulation, and quadruped velocity-tracking tasks, our method discovers up to 2$\times$ as many failures as random sampling and active-learning baselines, including severe and diverse failures missed by competing methods.

---


### 31. [Capacity-Dependent Effects of Data Selection for Reasoning](https://arxiv.org/abs/2608.13721)

**<font color=#1a73e8>作者：</font>** Cuong Dang, Hoang Anh Just, Ruoxi Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reasoning supervised fine-tuning, candidate responses for the same instruction can differ substantially in how well they match the student's current distribution. Recent likelihood-based response selection methods suggest that responses closer to the student distribution provide more effective supervision, motivating the hypothesis that high-likelihood responses may generally be preferable for fine-tuning. In this paper, we revisit this intuition and show that the value of likelihood-based data selection depends critically on model capacity and training duration. Through controlled experiments on mathematical reasoning, using students ranging from 1.5B to 8B parameters and supervision generated by stronger teacher models, we observe a clear \emph{capacity-dependent} ``{\color{SMALLCOLOR}\textbf{Fast-Fit}} / {\color{LARGECOLOR}\textbf{Slow-Gain}}'' pattern. High-likelihood data provides faster and more stable early improvements, especially for smaller models, but low-likelihood data becomes increasingly beneficial for larger models when training is allowed to continue longer. To explain this phenomenon, we analyze learning dynamics, showing that small models often fail to absorb low-likelihood supervision and instead fall into shallow or repetitive behaviors, while larger models are better able to move toward the teacher distribution under such data. We further provide a capacity-constrained theoretical view of distillation that clarifies how data difficulty, data span, and student capacity jointly govern transfer. Overall, our findings show that effective data selection for reasoning should be aware of model capacity and computing budget rather than based on a single universal preference for high-likelihood supervision.

---


### 32. [Limitations of Synthetic Data Generation in Specialized Data-Scarce Domains](https://arxiv.org/abs/2608.13729)

**<font color=#1a73e8>作者：</font>** Edward Zhang, Marcel Hussing, Tanay Tandon 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in diffusion-based generative models have motivated the use of synthetic image generation to alleviate data scarcity in vision tasks. While this strategy has shown promise in natural image benchmarks such as ImageNet, its effectiveness in sparse, high-variance real-world domains remains unclear. In this work, we focus on domains where images differ substantially from common image datasets and additional data are expensive to obtain. Against non-generative data augmentation baselines, we evaluate the downstream classifier performance improvements yielded by two schools of generative sparse data extension: distribution modeling and sample perturbation. Across five trauma classification tasks using subject-wise train--validation splits, no generative approach consistently outperforms a strong non-generative baseline. Feature-space analysis reveals recurring failure modes: memorization or collapse, distributional drift, and generation of visually plausible but simplified canonical instances that are easier to classify than real data.

---


### 33. [GALA: Generation-Aware Cross-Modal Alignment for Text-to-Time-Series Synthesis](https://arxiv.org/abs/2608.13741)

**<font color=#1a73e8>作者：</font>** Haochen Zhang, Gengwei Zhang, Laura Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthesizing time series from natural language is emerging as the most expressive form of controllable time series generation. However, existing text-conditioned generators either take caption embeddings frozen from off-the-shelf text encoders, or adapt the encoder end-to-end, letting the denoising loss shape the embeddings only as a by-product. In either case, the conditioning representation is never deliberately matched to the signal modality, leaving it ill-suited to guide generation. We address this by introducing GALA: Generation-Aware cross-modaL Alignment for text conditional time series generation. GALA is a two-stage approach that first contrastively couples a pretrained text encoder with a time-series foundation model into a shared embedding space with both encoders adapted to generation by an auxiliary generative loss, and then freezes the resulting caption embedding to drive a flow-matching generator. On TSFragment-600K, spanning four domains and three fragment lengths, GALA sets a new state of the art, ranking first in 30 of 36 metric columns and reaching an average rank of 1.08/1.08/1.42 at lengths 24/48/96 against 1.92/2.00/1.75 for the strongest baseline. We further find that generator-internal text encoders force a trade-off between fidelity and caption adherence, whereas conditioning on the aligned embedding breaks it: FID, CTTP, and JFTSD all improve at once. Ablating the auxiliary loss degrades FID, CTTP and JFTSD together, it indicates the generative term is a necessary component of the alignment rather than an add-on.

---


### 34. [CAST: Closed-form Analytic Semantic Transfer for Zero-Shot Classifier Extension](https://arxiv.org/abs/2608.13751)

**<font color=#1a73e8>作者：</font>** William Heyden, Habib Ullah, Muhammad Salman Siddiqui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large pre-trained models have become foundational components of modern machine learning systems. Yet adapting these models to novel categories typically requires examples from the target distribution. In many domains, however, such data are unavailable. Zero-shot learning (ZSL) permits recognition under these limitations through relying on auxiliary semantic information such as textual descriptions. We introduce CAST (Closed-form Analytic Semantic Transfer), a training-free, image-free framework for extending a pre-trained classifier to previously unseen classes through weight injection. We provide a theoretical foundation for CAST and derive a finite-sample error decomposition that identifies the \emph{semantic extrapolation residual} $\rho_u$. The residual is a computable, model-agnostic measure and provides a principled criterion for dataset curation and benchmark design. Experiments on standard zero-shot learning benchmarks demonstrate that CAST matches or exceeds existing image-free approaches and approaches the performance of few-shot adaptation methods, while requiring neither iterative optimization nor examples from the target distribution.

---


### 35. [Kolmogorov-Arnold Networks for Spatially Independent Multispectral Land Classification](https://arxiv.org/abs/2608.13769)

**<font color=#1a73e8>作者：</font>** Katherine L. Bauer, Teemu Harkonen, Simo Sarkka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Land classification from satellite imagery is important for land management, environmental monitoring, and urban planning. Machine learning methods such as random forests and multilayer perceptrons have shown strong performance on multispectral data, while the Kolmogorov-Arnold network has emerged as an alternative architecture with compact model structures. This study evaluates the Kolmogorov-Arnold network for land classification using Landsat 8 imagery and compares it with random forest and multilayer perceptron models. The models were trained and tested on data from Edmonton, Alberta and evaluated on an independent dataset from Calgary, Alberta across five land classes: agriculture, urban, water, forest, and bare ground. For the Calgary dataset, the Kolmogorov-Arnold network matched the accuracy of the random forest and outperformed the multilayer perceptron, while requiring substantially fewer trainable parameters and providing greater interpretability.

---


### 36. [CutClean: Neural Network Pruning for Privacy-Preserving Inference](https://arxiv.org/abs/2608.13773)

**<font color=#1a73e8>作者：</font>** Leonardo Magliolo, Vito Paolo Pastore, Giuseppe Valenzise 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks are increasingly deployed in high-stakes applications with growing privacy leakage concerns. We show that this privacy leakage can occur even in the absence of representation imbalances that lead to traditional dataset biases. This poses significant privacy risks when deploying models that process sensitive attributes. In this context, we propose CutClean, a privacy-aware pruning method that allows to reduce privacy information flow through the network, while increasing its sparsity. Our approach employs auxiliary linear privacy heads placed at each network's block to quantify information leakage, and further applies increasing levels of sparsity to remove the private attribute leakage, measured in terms of the accuracy of the privacy head attached to the last block. Experiments on synthetic and real-world datasets demonstrate that our approach effectively minimizes private information flow while achieving high sparsity rates and preserving classification target accuracy.

---


### 37. [FLARE MCMC: Fidelity-based Layer-Adaptive REcursive proposals for MCMC](https://arxiv.org/abs/2608.13774)

**<font color=#1a73e8>作者：</font>** Harini Venkatesan, Christian Shelton, Ming-Feng Ho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Markov chain Monte Carlo (MCMC) requires only the ability to evaluate the likelihood, making it a common technique for inference in complex models. However, it can have a slow mixing rate, requiring the generation of many samples to obtain good estimates and an overall high computational cost. FLARE MCMC is a multi-fidelity layered MCMC method that exploits lower-fidelity approximations of the true likelihood calculation to improve mixing and leads to overall faster performance. Such lower-fidelity likelihoods are commonly available in scientific and engineering applications where the model involves a simulation whose resolution or accuracy can be tuned. Our technique uses recursive, layered chains with simple layer tuning; it does not require the likelihood to take any form or have any particular internal mathematical structure. We demonstrate experimentally that FLARE MCMC achieves larger effective sample sizes for the same computational time across different scientific domains including hydrology and cosmology.

---


### 38. [A Reproducibility Protocol for Cross-Implementation Evaluation of Post-Quantum ACVP Test Vectors](https://arxiv.org/abs/2608.13784)

**<font color=#1a73e8>作者：</font>** Christopher M. Frost  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Independent implementations of a cryptographic standard should reproduce the same known-answer results, yet agreement is meaningful only when the corpus, revisions, public interfaces, exclusions, and evidence are precisely stated. This study defines a product-neutral reproducibility protocol for three public implementations of NIST ML-KEM against a pinned public Automated Cryptographic Validation Protocol corpus. Protocol v2 freezes provider-specific capabilities, applies one validation-error taxonomy symmetrically, preserves every selected case, and separates bytes, validation verdicts, unsupported operations, and adapter errors. The source-built experiment evaluated @noble/post-quantum 0.7.0, liboqs 0.16.0, and Go 1.26.4. Across three repetitions, the required Cartesian product comprised 2,160 base records: all 1,650 declared executable evaluations matched the NIST oracle, and all 510 unsupported records matched Go's predeclared capability boundary. Pairwise agreement was complete on every executable overlap: 720 of 720 noble-liboqs records and 210 of 210 records for each Go pairing. A separate keyGen-ek-projection diagnostic matched all 150 Go encapsulation-key projections without counting them as full key generation. Three frozen controls independently exercised byte comparison, verdict comparison, and malformed-response error separation; each produced its exact predeclared outcome. No base failure, adapter error, or status instability occurred. The evidence establishes bounded author-run repeatability and exposes a practical standards gap: public ML-KEM packages provide materially different deterministic and validation-test surfaces. Independent external reproduction remains unobserved. The results do not establish certification, exhaustive correctness, side-channel resistance, secure integration, or production assurance.

---


### 39. [PPAPlace: Differentiable Cross-Stage Objectives for Chip Placement Optimization](https://arxiv.org/abs/2608.13790)

**<font color=#1a73e8>作者：</font>** Ruogu Chen, Jie Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Macro placement significantly affects a chip's post-route performance, power, and area (PPA). Most placement methods optimize half-perimeter wirelength (HPWL) as the primary objective. However, recent benchmarking shows a near-zero correlation between HPWL and post-route timing metrics such as the worst negative slack (WNS) and total negative slack (TNS). As a result, all six evaluated artificial intelligence (AI) placers degraded PPA relative to the hierarchical baseline. Recent efforts have tried to train cross-stage predictors to close this gap. However, existing methods focus on macro-only representations and use pre-route metrics as training labels. A label fidelity study of ten circuits at four design flow stages reveals that HPWL and pre-route timing poorly reflect final post-route timing rankings. In contrast, post-global-routing achieves the best balance between final timing fidelity and label generation cost-effectiveness. Based on this finding, PPAPlace is a timing-driven differentiable surrogate predicting post-route PPA from macro and standard-cell placements. The surrogate is a dual-stream predictor that combines graph attention over the chip netlist with spatial convolution over the placement grid. It is trained on post-global-routing labels. The predicted WNS and TNS gradients flow end-to-end back to cell coordinates. PPAPlace exploits these gradients in two ways: as a co-objective injected into an analytical placer's optimization loop (PPAPlace-CoOpt), and as a post-placement refinement step that adjusts macro positions via projected gradient descent (PPAPlace-Refine). On five ChiPBench test circuits excluded from training, PPAPlace improves average WNS and TNS by 22\% and 51\% over the hierarchical baseline while preserving power and routability, using the same predictor without test-circuit retraining. Code is available at this https URL.

---


### 40. [The ack3 H1 2026 DeFi Incident Dataset: Audit Scope Across 135 Security Incidents](https://arxiv.org/abs/2608.13792)

**<font color=#1a73e8>作者：</font>** Josef Gattermayer, Jan Kalivoda, Arman Bašović  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart-contract audits cover defined artifacts at a specific time, but the label audited is often treated as project-wide assurance. We analyze audit history and incident-path scope across 135 DeFi security incidents using the H1 2026 DeFi Incident Dataset published by cybersecurity company ack3 (this https URL), covering 1 January to 29 June 2026. The corpus reports USD 939.86 million in attributed loss. Audit history was identified for 68 incidents. Of these, 46 attack paths were outside all identified public pre-incident audit scopes, 20 were inside at least one scope, and 2 were unresolved. Within this 68-incident subset, outside-scope paths represented 67.6% by count and 94.4% of reported loss. The loss-weighted result was concentrated in two large incidents; excluding both reduced the share to 72.1%, while preserving the direction of the result. We also describe audit age, temporal loss distribution, and affected project types. The results show that project-level audit history and incident-path scope are distinct variables.

---


### 41. [Recent Advances in Deep Learning-Based Drug-Target Binding Affinity Prediction](https://arxiv.org/abs/2608.13797)

**<font color=#1a73e8>作者：</font>** Jafin Khan, Md Hossain Shuvo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computational approaches to drug discovery involve multiple sub-problems, and among them, drug-target binding affinity prediction plays an important role. Despite recent advances, accurately predicting binding affinity remains an open research area. The major objective of our paper is to perform a comprehensive review and comparative analysis of recent machine learning methods for drug-target binding affinity prediction, with a focus on identifying strengths, limitations, and research gaps. We review representative recent deep learning approaches that use common benchmark datasets and evaluation metrics, covering a range of neural network architectures and representation strategies. In addition, we analyze seven widely used benchmark datasets and commonly adopted evaluation metrics for drug-target binding affinity prediction. Our analysis indicates that although many methods report strong performance on standard benchmarks, their effectiveness is often influenced by dataset bias and limited evaluation settings. Furthermore, most methods exhibit reduced performance in cold-start scenarios, highlighting challenges in generalization. We identify several limitations of current approaches, including dataset imbalance, the lack of standardized evaluation, limited real-world applicability, and challenges in cold-start scenarios. We also discuss future research directions, including better dataset design, more robust evaluation methods, improved handling of cold-start problems, and the integration of multimodal representations.

---


### 42. [Dynamic Multi-Depot Vehicle Routing with Online Requests: Event-Driven Transformer--DRL and Rolling-Horizon Benchmarking](https://arxiv.org/abs/2608.13799)

**<font color=#1a73e8>作者：</font>** Faezeh Ardali, Gerald M. Knapp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents an event-driven learning and benchmarking framework for the Dynamic Multi-Depot Vehicle Routing Problem with progressively revealed requests and evolving vehicle states. Masked MLP and Transformer policies are trained through behavior cloning and proximal policy optimization. Deterministic feasibility masking prevents invalid vehicle--request assignments, while fixed-prefix/flexible-suffix route commitments protect completed, active, and near-term decisions and separately measure vehicle reassignment and resequencing. The learned policies are compared with dynamic insertion heuristics and time-limited rolling-horizon optimization. In a 20-scenario policy benchmark, all methods completed every request without invalid actions, but nearest feasible achieved the lowest mean objective and outperformed the learned policies in routing quality, waiting time, stability, makespan, and runtime. Across five independent training runs, PPO had little average effect on the MLP and improved the Transformer on average, although with greater seed variability. Under the common protocol, nearest feasible achieved the lowest combined objective and route disruption, whereas rolling horizon achieved the lowest waiting times and makespan at substantially higher computational cost. The learned policies retained millisecond-level decisions and transferred to instances with up to 80 requests without retraining, but did not outperform the strongest heuristic. No single method was best across routing efficiency, service responsiveness, stability, and online computation.

---


### 43. [Stochastic Control Policies for Robust Molecular Transition Path Sampling](https://arxiv.org/abs/2608.13800)

**<font color=#1a73e8>作者：</font>** Jingqian Liu, Yu-Hsiang Wang, Yanru Qu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transition path sampling (TPS) aims to efficiently generate rare molecular transition trajectories between metastable states and is essential for understanding biomolecular mechanisms. Beyond traditional molecular dynamics (MD)-based sampling, machine learning has become central to state-of-the-art TPS. One major class of methods learns control forces during explicit MD rollouts. By preserving the underlying molecular dynamics, these methods tend to produce more physically plausible trajectories than endpoint-conditioned generators that construct paths directly. However, rollout-based control methods have been reported to exhibit unstable and strongly seed-dependent performance. We recast rollout-based control as learning a path-space proposal distribution and investigate stochasticity placement as a design choice for improving exploration and optimization robustness. We develop two stochastic policies: FS-TPS, which directly parameterizes a state-dependent Gaussian distribution over the control policy output, and LaS-TPS, which samples a compact latent control variable and decodes it into structured, cross-atom-correlated force variation. We conduct extensive multi-seed experiments on three biomolecular systems of increasing size: alanine dipeptide, chignolin, and BBL, a fast-folding protein. Stochastic policies consistently improve transition success and path quality over deterministic-policy baselines while substantially reducing sensitivity to random initialization.

---


### 44. [Mobile Apps vs. Web Browsers: A User Perception Study with Android Apps and Google Chrome](https://arxiv.org/abs/2608.13803)

**<font color=#1a73e8>作者：</font>** Harel Berger  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This study examines user perceptions of mobile applications (apps) versus web browsers for accessing online services, with an emphasis on security, privacy, and usability aspects. Through a combination of an experiment and a survey with Android smartphone users, the research seeks to identify the key concerns and preferences that influence their choice between mobile apps and web browsers. The findings will offer valuable insights for developers to improve the security, privacy, and usability of both platforms by addressing user concerns and misconceptions.

---


### 45. [Vaulted Passkeys: A Device-Bound Proposal for Authenticated Credential Export and Import](https://arxiv.org/abs/2608.13806)

**<font color=#1a73e8>作者：</font>** Pol Henarejos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware authenticators deliberately resist private-key extraction, yet replacement, disaster recovery, and controlled migration create a legitimate need for portability. Existing guidance for device-bound credentials commonly reduces recovery risk by registering an additional authenticator before failure. That creates an independent credential registration and requires replacement hardware to exist in advance; it is redundancy, not a backup of the original credential. This paper addresses the resulting recovery gap by exporting protected credential state while the source is available and restoring it to hardware acquired later, without cloning a complete authenticator or exposing plaintext private keys to routine desktop software. We propose Vaulted Passkeys, a device-bound architecture in which a random 256-bit Kvault protects authenticated PKV1 credential envelopes through HKDF-separated keys and four explicit AEAD profiles. The design separates enrollment from export/import and the required vault from optional identity. We contribute a role-separated system model, wire format, threat analysis, implementation mapping, and falsifiable evaluation plan. The prototype demonstrates feasibility but is neither a formal security proof nor a proposed final standard.

---


### 46. [TLF: Rapid Characterization of RF Transceiver Parameters in Embedded Systems via Bus-Level Interception](https://arxiv.org/abs/2608.13815)

**<font color=#1a73e8>作者：</font>** Larry Hernandez, Sergey Bratus  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present TLF (Transceiver Lifter Framework), a tool for recovering RF transceiver configuration and runtime behavior from bus-level traces captured between a microcontroller and its transceiver IC. A stateful protocol decoder, built against the transceiver's register and data interface, reconstructs operating RF parameters and behavior from intercepted register writes and FIFO transfers. For bus-attached transceivers whose hardware-cryptography keys are loaded through the intercepted host interface, key material is also recoverable. Where the firmware drives frequency hopping -- either through a hardware-assisted engine or a custom schedule -- the decoder extracts the channel table, hop sequence, and timing. We evaluate the approach on two targets from different Semtech families: an SX1233-based UAV C2 modem employing firmware-level FHSS with per-packet sync word rotation, and an SX1276-based Meshtastic node exercising the LoRa register overlay. From a single bus capture, processed in seconds, TLF recovers the complete register-exposed RF configuration (modulation, band plan, phase behavior) without prior knowledge of the target firmware -- sufficient to configure a matched receiver or develop targeted countermeasures. Above the chip layer, a pluggable protocol decoder interprets recovered FIFO payloads as application PDUs, demonstrated end-to-end on Meshtastic. Firmware-level cryptographic state remains, as expected, opaque. The approach requires physical access or emulation of the target hardware, and its recovery depth is bounded by the transceiver's register interface: parameters implemented entirely in firmware (custom FEC, whitening, encryption) are observable only as opaque FIFO payloads.

---


### 47. [SDO: Subspace Deconflicting Operator for Multi-Adapter Composition](https://arxiv.org/abs/2608.13820)

**<font color=#1a73e8>作者：</font>** Zhongsheng Wang, Zhedong Lin, Qian Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Composing independently trained adapters within a shared diffusion backbone provides a modular approach to multi-character generation, but naive joint deployment often causes identity mixing, cross-character attribute leakage, and unstable scene composition. We study this interference from a parameter-space perspective and hypothesize that it arises partly from conflicts between overlapping dominant subspaces in shared layers. To address this issue, we propose \textbf{SDO}, a \textbf{S}ubspace \textbf{D}econflicting \textbf{O}perator for multi-adapter composition. SDO reconstructs layer-wise low-rank updates from the selected adapters, extracts compact subspace signatures, measures pairwise conflict through output-subspace overlap, and applies a permutation-equivariant transformation that suppresses harmful shared directions while retaining identity-specific characteristics. The resulting representations are mapped back to standard adapter updates and can be directly incorporated into existing diffusion inference pipelines. Experiments demonstrate that SDO consistently improves identity fidelity and compositional stability, with particularly clear gains as the number of jointly composed adapters increases.

---


### 48. [HI-MeshGraphNets: Efficient and Accurate Mesh-based Physics Learning with Hierarchical Multi-scale Graph Neural Networks](https://arxiv.org/abs/2608.13827)

**<font color=#1a73e8>作者：</font>** SiHun Lee, Dong-Hyuk Park, Taesoo Bang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learned physical surrogate models have become promising alternatives to mesh-based numerical solvers. Among them, graph neural networks (GNNs) are well suited for representing simulation meshes and learning nodal state evolution through message passing. However, conventional flat message passing becomes inefficient on large, high-fidelity meshes because information propagates only one hop per layer, requiring deep processors for long-range interactions and increasing computational cost, memory usage, and the risk of over-smoothing.
To address this limitation, we propose Hierarchical Interpolating MeshGraphNets (HI-MGN), a multiscale extension of MeshGraphNets for efficient long-range communication on unstructured meshes. HI-MGN replaces the flat processor with a hierarchical multiscale processor that coarsens graphs using farthest-point sampling and Voronoi partitioning while preserving the original mesh topology. Message passing on coarse graphs enables information to travel over larger geometric distances with fewer layers, and a learned graph interpolation network reconstructs fine-resolution features.
Across three structural and fluid benchmarks, HI-MGN achieves improved accuracy compared with MeshGraphNets and the Bi-Stride Multi-Scale GNN while reducing training time and peak memory usage. The results show that topology-aware hierarchical message passing and learned coarse-to-fine interpolation provide an effective and practical framework for scalable mesh-based physics surrogate modeling.

---


### 49. [Verified Pythagorean Composition for Adaptive Cryptographic Games: Noise Flooding in Homomorphic Encryption](https://arxiv.org/abs/2608.13846)

**<font color=#1a73e8>作者：</font>** Yi Lee, Alexandru Cojocaru, Junyi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Noise flooding is a standard defense against decryption attacks on approximate homomorphic encryption, but its security proof is unusually sensitive to composition. Replacing each of $q$ adaptive decryption answers with a statistically close simulation and applying an ordinary hybrid argument loses linearly in $q$. The cryptographic proof instead accumulates conditional Kullback-Leibler (KL) costs and converts to statistical distance once, giving the parameter-critical square-root loss.
We machine-check this argument using Rocq and SSProve. Given any fully homomorphic encryption scheme that is approximately correct and IND-CPA secure, we formalize a reduction for every $q$-query IND-CPAD adversary and prove \[
\Pr[\mathsf{IND\text{-}CPAD}_{\mathsf{NF}}^{\mathcal A}=1]
\leq \beta_{\mathsf{CPA}}(\mathcal B_{\mathcal A,q})
+ \frac{\sqrt{qn}}{2\gamma}. \] where $n$ is the plaintext dimension and $\gamma$ is the flooding-width multiplier. Our proof constructs a new relational program logic over SSProve semantics. Its Pythagorean judgment composes conditional KL budgets without converting them to statistical distance, and a verified trace compiler lifts a local oracle rule to arbitrary adaptive programs with a single final conversion.

---


### 50. [Face Re-morphing: Differential Morphing Attack Detection via Feature-Space Similarity Changes](https://arxiv.org/abs/2608.13858)

**<font color=#1a73e8>作者：</font>** Jie Jin, Masakatsu Nishigaki, Tetsushi Ohki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face morphing attacks pose a serious threat to face recognition systems because a single morphed document image can be matched to multiple contributors. Differential morphing attack detection (D-MAD) addresses this threat by comparing a document image with a trusted live image, but existing methods often rely on static feature differences, constituent-face reconstruction, or multi-cue fusion. This paper proposes Face Re-morphing, a D-MAD method that uses the feature-space response to an additional morphing operation as a detection cue. Given a document image and a trusted live image, the proposed method generates a re-morphed image and uses the change between the document--live and live--re-morphed cosine similarities as the detection score. Experiments on FRLL-Morphs and FEI Morph show that the proposed cue is effective across different morphing conditions, re-morphing methods, and face recognition models. Comparisons with existing methods show favorable results on AMSL and indicate that the proposed method performs well under the Criminal condition on FEI Morph Version~1, particularly when using MorDIFF. These results indicate that re-morphing-induced similarity change provides a complementary cue for D-MAD.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-165](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
