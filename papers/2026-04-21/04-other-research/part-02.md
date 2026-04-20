# 📦 其他研究 | 2026年04月21日

> 本类共 **203** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-203](./part-05.md)

---

### 51. [Predicting Where Steering Vectors Succeed](https://arxiv.org/abs/2604.15557)

**<font color=#1a73e8>作者：</font>** Jayadev Billa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Steering vectors work for some concepts and layers but fail for others, and practitioners have no way to predict which setting applies before running an intervention. We introduce the Linear Accessibility Profile (LAP), a per-layer diagnostic that repurposes the logit lens as a predictor of steering vector effectiveness. The key measure, $A_{\mathrm{lin}}$, applies the model's unembedding matrix to intermediate hidden states, requiring no training. Across 24 controlled binary concept families on five models (Pythia-2.8B to Llama-8B), peak $A_{\mathrm{lin}}$ predicts steering effectiveness at $\rho = +0.86$ to $+0.91$ and layer selection at $\rho = +0.63$ to $+0.92$. A three-regime framework explains when difference-of-means steering works, when nonlinear methods are needed, and when no method can work. An entity-steering demo confirms the prediction end-to-end: steering at the LAP-recommended layer redirects completions on Gemma-2-2B and OLMo-2-1B-Instruct, while the middle layer (the standard heuristic) has no effect on either model.

---


### 52. [Preregistered Belief Revision Contracts](https://arxiv.org/abs/2604.15558)

**<font color=#1a73e8>作者：</font>** Saad Alqithami  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deliberative multi-agent systems allow agents to exchange messages and revise beliefs over time. While this interaction is meant to improve performance, it can also create dangerous conformity effects: agreement, confidence, prestige, or majority size may be treated as if they were evidence, producing high-confidence convergence to false conclusions. To address this, we introduce PBRC (Preregistered Belief Revision Contracts), a protocol-level mechanism that strictly separates open communication from admissible epistemic change. A PBRC contract publicly fixes first-order evidence triggers, admissible revision operators, a priority rule, and a fallback policy. A non-fallback step is accepted only when it cites a preregistered trigger and provides a nonempty witness set of externally validated evidence tokens. This ensures that every substantive belief change is both enforceable by a router and auditable after the fact. In this paper, (a) we prove that under evidential contracts with conservative fallback, social-only rounds cannot increase confidence and cannot generate purely conformity-driven wrong-but-sure cascades. (b) We show that auditable trigger protocols admit evidential PBRC normal forms that preserve belief trajectories and canonicalized audit traces. (c) We demonstrate that sound enforcement yields epistemic accountability: any change of top hypothesis is attributable to a concrete validated witness set. For token-invariant contracts, (d) we prove that enforced trajectories depend only on token-exposure traces; under flooding dissemination, these traces are characterized exactly by truncated reachability, giving tight diameter bounds for universal evidence closure. Finally, we introduce a companion contractual dynamic doxastic logic to specify trace invariants, and provide simulations illustrating cascade suppression, auditability, and robustness-liveness trade-offs.

---


### 53. [Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation](https://arxiv.org/abs/2604.15559)

**<font color=#1a73e8>作者：</font>** Jacob Dang, Brian Y. Xie, Omar G. Younis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work on subliminal learning demonstrates that language models can transmit semantic traits through data that is semantically unrelated to those traits. However, it remains unclear whether behavioral traits can transfer in agentic systems, where policies are learned from trajectories rather than static text. In this work, we provide the first empirical evidence that unsafe agent behaviors can transfer subliminally through model distillation across two complementary experimental settings. In our primary setting, we construct a teacher agent exhibiting a strong deletion bias, a tendency to perform destructive file-system actions via an API-style tool interface, and distill it into a student using only trajectories from ostensibly safe tasks, with all explicit deletion keywords rigorously filtered. In our secondary setting, we replicate the threat model in a native Bash environment, replacing API tool calls with shell commands and operationalizing the bias as a preference for issuing chmod as the first permission-related command over semantically equivalent alternatives such as chown or setfacl. Despite full keyword sanitation in both settings, students inherit measurable behavioral biases. In the API setting the student's deletion rate reaches 100% (versus a 5% baseline) under homogeneous distillation; in the Bash setting the student's chmod-first rate reaches 30%-55% (versus a 0%-10% baseline), with the strongest transfer observed in large-to-small distillation. Our results demonstrate that explicit data sanitation is an insufficient defense, and behavioral biases are encoded implicitly in trajectory dynamics regardless of the tool interface.

---


### 54. [Reward Weighted Classifier-Free Guidance as Policy Improvement in Autoregressive Models](https://arxiv.org/abs/2604.15577)

**<font color=#1a73e8>作者：</font>** Alexander Peysakhovich, William Berman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Consider an auto-regressive model that produces outputs x (e.g., answers to questions, molecules) each of which can be summarized by an attribute vector y (e.g., helpfulness vs. harmlessness, or bio-availability vs. lipophilicity). An arbitrary reward function r(y) encodes tradeoffs between these properties. Typically, tilting the model's sampling distribution to increase this reward is done at training time via reinforcement learning. However, if the reward function changes, re-alignment requires re-training. In this paper, we show that a reward weighted classifier-free guidance (RCFG) can act as a policy improvement operator in this setting, approximating tilting the sampling distribution by the Q function. We apply RCFG to molecular generation, demonstrating that it can optimize novel reward functions at test time. Finally, we show that using RCFG as a teacher and distilling into the base policy to serve as a warm start significantly speeds up convergence for standard RL.

---


### 55. [A Framework for Post Quantum Migration in IoT-Based Healthcare Systems](https://arxiv.org/abs/2604.15584)

**<font color=#1a73e8>作者：</font>** Asif Alif, Khondokar Fida Hasan, Basker Palaniswamy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart healthcare industry is increasingly relying on Internet of Things (IoT) devices to improve patient care and operational efficiency. However, the cryptographic algorithms that enable fundamental security and are widely used in these cyber systems are vulnerable to attacks by emerging quantum computers - known as Quantum Threat. This paper examines the quantum threat to healthcare IoT across the four layers of the IoT architecture: physical, network, perception, and application. It proposes a comprehensive migration framework integrating a phased hybrid approach with crypto-agility to transition healthcare IoT systems to quantum-safe cryptography. This framework prioritises resource-constrained devices, emphasises interoperability, and considers the challenges of vendor readiness and infrastructure upgrades. This paper contributes a detailed, phased migration plan specifically tailored to the unique security needs and resource limitations of IoT-based healthcare systems.

---


### 56. [PAWN: Piece Value Analysis with Neural Networks](https://arxiv.org/abs/2604.15585)

**<font color=#1a73e8>作者：</font>** Ethan Tang, Hasan Davulcu, Jia Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the relative value of any given chess piece in a position remains an open challenge, as a piece's contribution depends on its spatial relationships with every other piece on the board. We demonstrate that incorporating the state of the full chess board via latent position representations derived using a CNN-based autoencoder significantly improves accuracy for MLP-based piece value prediction architectures. Using a dataset of over 12 million piece-value pairs gathered from Grandmaster-level games, with ground-truth labels generated by Stockfish 17, our enhanced piece value predictor significantly outperforms context-independent MLP-based systems, reducing validation mean absolute error by 16% and predicting relative piece value within approximately 0.65 pawns. More generally, our findings suggest that encoding the full problem state as context provides useful inductive bias for predicting the contribution of any individual component.

---


### 57. [CSLE: A Reinforcement Learning Platform for Autonomous Security Management](https://arxiv.org/abs/2604.15590)

**<font color=#1a73e8>作者：</font>** Kim Hammar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is a promising approach to autonomous and adaptive security management in networked systems. However, current reinforcement learning solutions for security management are mostly limited to simulation environments and it is unclear how they generalize to operational systems. In this paper, we address this limitation by presenting CSLE: a reinforcement learning platform for autonomous security management that enables experimentation under realistic conditions. Conceptually, CSLE encompasses two systems. First, it includes an emulation system that replicates key components of the target system in a virtualized environment. We use this system to gather measurements and logs, based on which we identify a system model, such as a Markov decision process. Second, it includes a simulation system where security strategies are efficiently learned through simulations of the system model. The learned strategies are then evaluated and refined in the emulation system to close the gap between theoretical and operational performance. We demonstrate CSLE through four use cases: flow control, replication control, segmentation control, and recovery control. Through these use cases, we show that CSLE enables near-optimal security management in an environment that approximates an operational system.

---


### 58. [Privacy, Prediction, and Allocation](https://arxiv.org/abs/2604.15596)

**<font color=#1a73e8>作者：</font>** Ben Jacobsen, Nitin Kohli  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Algorithmic predictions are increasingly used to inform the allocation of scarce resources. The promise of these methods is that, through machine learning, they can better identify the people who would benefit most from interventions. Recently, however, several works have called this assumption into question by demonstrating the existence of settings where simple, unit-level allocation strategies can meet or even exceed the performance of those based on individual-level targeting. Separately, other works have objected to individual-level targeting on privacy grounds, leading to an unusual situation where a single solution, unit-level targeting, is recommended for reasons of both privacy and utility. Motivated by the desire to fully understand the interplay of privacy and targeting levels, we initiate the study of aid allocation systems that satisfy differential privacy, synthesizing existing works on private optimization with the economic models of aid allocation used in the non-private literature. To this end, we investigate private variants of both individual and unit-level allocation strategies in both stochastic and distribution-free settings under a range of constraints on data availability. Through this analysis, we provide clean, interpretable bounds characterizing the tradeoffs between privacy, efficiency, and targeting precision in allocation.

---


### 59. [Imperfectly Cooperative Human-AI Interactions: Comparing the Impacts of Human and AI Attributes in Simulated and User Studies](https://arxiv.org/abs/2604.15607)

**<font color=#1a73e8>作者：</font>** Myke C. Cohen, Mingqian Zheng, Neel Bhandari 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI design characteristics and human personality traits each impact the quality and outcomes of human-AI interactions. However, their relative and joint impacts are underexplored in imperfectly cooperative scenarios, where people and AI only have partially aligned goals and objectives. This study compares a purely simulated dataset comprising 2,000 simulations and a parallel human subjects experiment involving 290 human participants to investigate these effects across two scenario categories: (1) hiring negotiations between human job candidates and AI hiring agents; and (2) human-AI transactions wherein AI agents may conceal information to maximize internal goals. We examine user Extraversion and Agreeableness alongside AI design characteristics, including Adaptability, Expertise, and chain-of-thought Transparency. Our causal discovery analysis extends performance-focused evaluations by integrating scenario-based outcomes, communication analysis, and questionnaire measures. Results reveal divergences between purely simulated and human study datasets, and between scenario types. In simulation experiments, personality traits and AI attributes were comparatively influential. Yet, with actual human subjects, AI attributes -- particularly transparency -- were much more impactful. We discuss how these divergences vary across different interaction contexts, offering crucial insights for the future of human-centered AI agents.

---


### 60. [Adapting in the Dark: Efficient and Stable Test-Time Adaptation for Black-Box Models](https://arxiv.org/abs/2604.15609)

**<font color=#1a73e8>作者：</font>** Yunbei Zhang, Shuaicheng Niu, Chengyi Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-Time Adaptation (TTA) for black-box models accessible only via APIs remains a largely unexplored challenge. Existing approaches such as post-hoc output refinement offer limited adaptive capacity, while Zeroth-Order Optimization (ZOO) enables input-space adaptation but faces high query costs and optimization challenges in the unsupervised TTA setting. We introduce BETA (Black-box Efficient Test-time Adaptation), a framework that addresses these limitations by employing a lightweight, local white-box steering model to create a tractable gradient pathway. Through a prediction harmonization technique combined with consistency regularization and prompt learning-oriented filtering, BETA enables stable adaptation with no additional API calls and negligible latency beyond standard inference. On ImageNet-C, BETA achieves a +7.1% accuracy gain on ViT-B/16 and +3.4% on CLIP, surpassing strong white-box and gray-box methods including TENT and TPT. On a commercial API, BETA achieves comparable performance to ZOO at 250x lower cost while maintaining real-time inference speed, establishing it as a practical and efficient solution for real-world black-box TTA.

---


### 61. [Scalable Algorithms with Provable Optimality Bounds for the Multiple Watchman Route Problem](https://arxiv.org/abs/2604.15610)

**<font color=#1a73e8>作者：</font>** Srikar Gouru, Ariel Felner, Jiaoyang Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In this paper, we tackle the Multiple Watchman Route Problem (MWRP), which aims to find a set of paths that M watchmen can follow such that every location on the map can be seen by at least one watchman. First, we propose multiple methods to reduce the state space over which a search needs to be conducted by pruning map areas that are guaranteed to be seen en route to other areas. Next, we introduce MWRP-CP3, an efficient optimal planner that combines these methods with techniques that improve the quality and calculation time of existing heuristics. We present several suboptimal algorithms with bounds on solution quality, including MxWA*, a general variant of weighted A* for makespan problems. We also present anytime variations of our suboptimal algorithms, as well as techniques to improve an existing suboptimal solution by solving multiple decomposed sub-problems. We show that MWRP-CP3 can reduce the search space by more than 95% and runs more than 200x faster than existing optimal algorithms on 2D grid maps. We also show that our suboptimal algorithms solve maps 3x larger than those solvable by MWRP-CP3. See this http URL for the open source codebase and video demonstrations.

---


### 62. [CLIMB: Controllable Longitudinal Brain Image Generation using Mamba-based Latent Diffusion Model and Gaussian-aligned Autoencoder](https://arxiv.org/abs/2604.15611)

**<font color=#1a73e8>作者：</font>** Duy-Phuong Dao, Muhammad Taqiyuddin, Jahae Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models have emerged as powerful generative models in medical imaging, enabling the synthesis of high quality brain magnetic resonance imaging scans. In particular, predicting the evolution of a patients brain can aid in early intervention, prognosis, and treatment planning. In this study, we introduce CLIMB, Controllable Longitudinal brain Image generation via state space based latent diffusion model, an advanced framework for modeling temporal changes in brain structure. CLIMB is designed to model the structural evolution of the brain structure over time, utilizing a baseline MRI scan and its acquisition age as foundational inputs. Additionally, multiple conditional variables, including projected age, gender, disease status, genetic information, and brain structure volumes, are incorporated to enhance the temporal modeling of anatomical changes. Unlike existing LDM methods that rely on self attention modules, which effectively capture contextual information from input images but are computationally expensive, our approach leverages state space, a state space model architecture that substantially reduces computational overhead while preserving high-quality image synthesis. Furthermore, we introduce a Gaussian-aligned autoencoder that extracts latent representations conforming to prior distributions without the sampling noise inherent in conventional variational autoencoders. We train and evaluate our proposed model on the Alzheimers Disease Neuroimaging Initiative dataset, consisting of 6,306 MRI scans from 1,390 participants. By comparing generated images with real MRI scans, CLIMB achieves a structural similarity index of 0.9433, demonstrating notable improvements over existing methods.

---


### 63. [VoodooNet: Achieving Analytic Ground States via High-Dimensional Random Projections](https://arxiv.org/abs/2604.15613)

**<font color=#1a73e8>作者：</font>** Wladimir Silva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present VoodooNet, a non-iterative neural architecture that replaces the stochastic gradient descent (SGD) paradigm with a closed-form analytic solution via Galactic Expansion. By projecting input manifolds into a high-dimensional, high-entropy "Galactic" space ($d \gg 784$), we demonstrate that complex features can be untangled without the thermodynamic cost of backpropagation. Utilizing the Moore-Penrose pseudoinverse to solve for the output layer in a single step, VoodooNet achieves a classification accuracy of \textbf{98.10\% on MNIST} and \textbf{86.63\% on Fashion-MNIST}. Notably, our results on Fashion-MNIST surpass a 10-epoch SGD baseline (84.41\%) while reducing the training time by orders of magnitude. We observe a near-logarithmic scaling law between dimensionality and accuracy, suggesting that performance is a function of "Galactic" volume rather than iterative refinement. This "Magic Hat" approach offers a new frontier for real-time Edge AI, where the traditional training phase is bypassed in favor of instantaneous manifold discovery.

---


### 64. [Flexible Empowerment at Reasoning with Extended Best-of-N Sampling](https://arxiv.org/abs/2604.15614)

**<font color=#1a73e8>作者：</font>** Taisuke Kobayashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a novel method that incorporates empowerment when reasoning actions in reinforcement learning (RL), thereby achieving the flexibility of exploration-exploitation dilemma (EED). In previous methods, empowerment for promoting exploration has been provided as a bonus term to the task-specific reward function as an intrinsically-motivated RL. However, this approach introduces a delay until the policy that accounts for empowerment is learned, making it difficult to adjust the emphasis on exploration as needed. On the other hand, a trick devised for fine-tuning recent foundation models at reasoning, so-called best-of-N (BoN) sampling, allows for the implicit acquisition of modified policies without explicitly learning them. It is expected that applying this trick to exploration-promoting terms, such as empowerment, will enable more flexible adjustment of EED. Therefore, this paper investigates BoN sampling for empowerment. Furthermore, to adjust the degree of policy modification in a generalizable manner while maintaining computational cost, this paper proposes a novel BoN sampling method extended by Tsalis statistics. Through toy problems, the proposed method's cability to balance EED is verified. In addition, it is demonstrated that the proposed method improves RL performance to solve complex locomotion tasks.

---


### 65. [Majority Voting for Code Generation](https://arxiv.org/abs/2604.15618)

**<font color=#1a73e8>作者：</font>** Tim Launer, Jonas Hübotter, Marco Bagatella 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate Functional Majority Voting (FMV), a method based on functional consensus for code generation with Large Language Models, which identifies a representative solution from multiple generations using their runtime execution signatures on test inputs. We find that FMV is an effective test-time inference strategy, substantially boosting performance on LiveCodeBench without a large compute overhead. Furthermore, we extend the utility of functional consensus and apply it as an aggregation strategy for label-free Test-Time Reinforcement Learning. We demonstrate that this increases pass@1 on holdout tasks, but find no evidence of self-improvement beyond the base model's performance ceiling.

---


### 66. [ZORO: Active Rules for Reliable Vibe Coding](https://arxiv.org/abs/2604.15625)

**<font color=#1a73e8>作者：</font>** Jenny Ma, Sitong Wang, Joshua H. Kung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Rules files (e.g., this http URL, this http URL) are the primary mechanism for human-agent alignment when developers vibe code. However, they remain passive: it is not immediately apparent when rules are being used or followed, or how to improve them. To transform rules from passive text into active controls, we introduce ZORO, an interactive interface that integrates directly with a coding agent and anchors rules to every step of the coding process. After an agent generates an initial plan, ZORO enriches the plan with rules, enforces the rules during implementation by requiring the agent prove that each rule was followed, and allows users to provide in-situ feedback when they are unsatisfied with a rule application to evolve the ruleset. A technical evaluation shows that coding agents follow rules more with ZORO than without. A user study demonstrates a change in people's behavior and cognitive strategies when rules are at the forefront of vibe coding. We discuss how making rules active in agentic systems unlocks broader opportunities for human-agent alignment in coding settings and beyond.

---


### 67. [Too Private to Tell: Practical Token Theft Attacks on Apple Intelligence](https://arxiv.org/abs/2604.15637)

**<font color=#1a73e8>作者：</font>** Haoling Zhou, Shixuan Zhao, Chao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Apple Intelligence is a generative AI (GenAI) service provided by Apple on its devices. While offering a similar set of features as other similar GenAI services, Apple Intelligence is claimed to be designed with an extra focus on user security and privacy through a two-stage authentication and authorization design using anonymous access tokens. In this paper, we present our investigation into this token issuance mechanism with a goal to reveal possible vulnerabilities using traffic analysis, reverse engineering, and cross comparison with Apple's public documentation. Specifically, we present the Serpent attack, the first practical cross-device token replay attack against Apple Intelligence that allows the attacker to steal the access tokens from the victim's device and utilise them on a different device, with all usage rate-limited against the victim. We have achieved successful attacks on the latest macOS 26 Tahoe and demonstrated that an attacker, who even has used up its own allowance, can immediately regain access to Apple Intelligence service. We have responsibly disclosed the vulnerabilities to the vendors and received confirmation from Apple with CVE assigned and bounty given. Our results highlight a general lesson for built-in AI services: Anonymising identity does not by itself make the AI service secure; Enforcing non-transferability requires cryptographic binding to the rightful user.

---


### 68. [Half-Moon Cookie: Private, Similarity-Based Blocklisting with TOCTOU-Attack Resilience](https://arxiv.org/abs/2604.15641)

**<font color=#1a73e8>作者：</font>** Xinyuan Zhang, Anrin Chakraborti, Michael K. Reiter  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blocklisting is a common technique for preventing the use of known malicious content. However, conventional blocklisting infrastructures require either the blocklist to be public or clients to reveal their queries to the blocklist server. In this work, we introduce a private blocklisting framework, Half-Moon Cookie, by which a client can check an item against a proprietary blocklist held by a server, to determine whether the item is close to any blocklist element in a metric space. Critically, our design separates the embedding step from the blocklist check, so that performance degrades with their sum and not their product. Still, this check might be too costly to perform on the critical path of using the item, and so our design also supports a very efficient check that an item previously passed the blocklist check. In doing so, we support applications where one client can perform the blocklist check on the item before sending it, and recipients can more efficiently confirm the previous result before using the item, thereby avoiding TOCTOU attacks. We demonstrate how Half-Moon Cookie can be instantiated for similarity-based malware detection, enabling effective identification of malicious executables without revealing client inputs or disclosing the underlying blocklist.

---


### 69. [PINNACLE: An Open-Source Computational Framework for Classical and Quantum PINNs](https://arxiv.org/abs/2604.15645)

**<font color=#1a73e8>作者：</font>** Shimon Pisnoy, Hemanth Chandravamsi, Ziv Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present PINNACLE, an open-source computational framework for physics-informed neural networks (PINNs) that integrates modern training strategies, multi-GPU acceleration, and hybrid quantum-classical architectures within a unified modular workflow. The framework enables systematic evaluation of PINN performance across benchmark problems including 1D hyperbolic conservation laws, incompressible flows, and electromagnetic wave propagation. It supports a range of architectural and training enhancements, including Fourier feature embeddings, random weight factorization, strict boundary condition enforcement, adaptive loss balancing, curriculum training, and second-order optimization strategies, with extensibility to additional methods. We provide a comprehensive benchmark study quantifying the impact of these methods on convergence, accuracy, and computational cost, and analyze distributed data parallel scaling in terms of runtime and memory efficiency. In addition, we extend the framework to hybrid quantum-classical PINNs and derive a formal estimate for circuit-evaluation complexity under parameter-shift differentiation. Results highlight the sensitivity of PINNs to architectural and training choices, confirm their high computational cost relative to classical solvers, and identify regimes where hybrid quantum models offer improved parameter efficiency. PINNACLE provides a foundation for benchmarking physics-informed learning methods and guiding future developments through quantitative assessment of their trade-offs.

---


### 70. [FD-NL2SQL: Feedback-Driven Clinical NL2SQL that Improves with Use](https://arxiv.org/abs/2604.15646)

**<font color=#1a73e8>作者：</font>** Suparno Roy Chowdhury, Tejas Anvekar, Manan Roy Choudhury 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinicians exploring oncology trial repositories often need ad-hoc, multi-constraint queries over biomarkers, endpoints, interventions, and time, yet writing SQL requires schema expertise. We demo FD-NL2SQL, a feedback-driven clinical NL2SQL assistant for SQLite-based oncology databases. Given a natural-language question, a schema-aware LLM decomposes it into predicate-level sub-questions, retrieves semantically similar expert-verified NL2SQL exemplars via sentence embeddings, and synthesizes executable SQL conditioned on the decomposition, retrieved exemplars, and schema, with post-processing validity checks. To improve with use, FD-NL2SQL incorporates two update signals: (i) clinician edits of generated SQL are approved and added to the exemplar bank; and (ii) lightweight logic-based SQL augmentation applies a single atomic mutation (e.g., operator or column change), retaining variants only if they return non-empty results. A second LLM generates the corresponding natural-language question and predicate decomposition for accepted variants, automatically expanding the exemplar bank without additional annotation. The demo interface exposes decomposition, retrieval, synthesis, and execution results to support interactive refinement and continuous improvement.

---


### 71. [CIG: Measuring Conversational Information Gain in Deliberative Dialogues with Semantic Memory Dynamics](https://arxiv.org/abs/2604.15647)

**<font color=#1a73e8>作者：</font>** Ming-Bin Chen, Jey Han Lau, Lea Frermann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Measuring the quality of public deliberation requires evaluating not only civility or argument structure, but also the informational progress of a conversation. We introduce a framework for Conversational Information Gain (CIG) that evaluates each utterance in terms of how it advances collective understanding of the target topic. To operationalize CIG, we model an evolving semantic memory of the discussion: the system extracts atomic claims from utterances and incrementally consolidates them into a structured memory state. Using this memory, we score each utterance along three interpretable dimensions: Novelty, Relevance, and Implication Scope. We annotate 80 segments from two moderated deliberative settings (TV debates and community discussions) with these dimensions and show that memory-derived dynamics (e.g., the number of claim updates) correlate more strongly with human-perceived CIG than traditional heuristics such as utterance length or TF--IDF. We develop effective LLM-based CIG predictors paving the way for information-focused conversation quality analysis in dialogues and deliberative success.

---


### 72. [SPLIT: Self-supervised Partitioning for Learned Inversion in Nonlinear Tomography](https://arxiv.org/abs/2604.15651)

**<font color=#1a73e8>作者：</font>** Markus Haltmeier, Lukas Neumann, Nadja Gruber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine learning has achieved impressive performance in tomographic reconstruction, but supervised training requires paired measurements and ground-truth images that are often unavailable. This has motivated self-supervised approaches, which have primarily addressed denoising and, more recently, linear inverse problems. We address nonlinear inverse problems and introduce SPLIT (Self-supervised Partitioning for Learned Inversion in Nonlinear Tomography), a self-supervised machine-learning framework for reconstructing images from nonlinear, incomplete, and noisy projection data without any samples of ground-truth images. SPLIT enforces cross-partition consistency and measurement-domain fidelity while exploiting complementary information across multiple partitions. Our main theoretical result shows that, under mild conditions, the proposed self-supervised objective is equivalent to its supervised counterpart in expectation. We regularize training with an automatic stopping rule that halts optimization when a no-reference image-quality surrogate saturates. As a concrete application, we derive SPLIT variants for multispectral computed tomography. Experiments on sparse-view acquisitions demonstrate high reconstruction quality and robustness to noise, surpassing classical iterative reconstruction and recent self-supervised baselines.

---


### 73. [Towards Realistic Open-Vocabulary Remote Sensing Segmentation: Benchmark and Baseline](https://arxiv.org/abs/2604.15652)

**<font color=#1a73e8>作者：</font>** Bingyu Li, Tao Huo, Haocheng Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary remote sensing image segmentation (OVRSIS) remains underexplored due to fragmented datasets, limited training diversity, and the lack of evaluation benchmarks that reflect realistic geospatial application demands. Our previous \textit{OVRSISBenchV1} established an initial cross-dataset evaluation protocol, but its limited scope is insufficient for assessing realistic open-world generalization. To address this issue, we propose \textit{OVRSISBenchV2}, a large-scale and application-oriented benchmark for OVRSIS. We first construct \textbf{OVRSIS95K}, a balanced dataset of about 95K image--mask pairs covering 35 common semantic categories across diverse remote sensing scenes. Built upon OVRSIS95K and 10 downstream datasets, OVRSISBenchV2 contains 170K images and 128 categories, substantially expanding scene diversity, semantic coverage, and evaluation difficulty. Beyond standard open-vocabulary segmentation, it further includes downstream protocols for building extraction, road extraction, and flood detection, thereby better reflecting realistic geospatial application demands and complex deployment scenarios. We also propose \textbf{Pi-Seg}, a baseline for OVRSIS. Pi-Seg improves transferability through a \textbf{positive-incentive noise} mechanism, where learnable and semantically guided perturbations broaden the visual-text feature space during training. Extensive experiments on OVRSISBenchV1, OVRSISBenchV2, and downstream tasks show that Pi-Seg delivers strong and consistent results, particularly on the more challenging OVRSISBenchV2 benchmark. Our results highlight both the importance of realistic benchmark design and the effectiveness of perturbation-based transfer for OVRSIS. The code and datasets are available at \href{this https URL}{LiBingyu01/RSKT-Seg/tree/Pi-Seg}.

---


### 74. [From Zero to Detail: A Progressive Spectral Decoupling Paradigm for UHD Image Restoration with New Benchmark](https://arxiv.org/abs/2604.15654)

**<font color=#1a73e8>作者：</font>** Chen Zhao, Yunzhe Xu, Zhizhou Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-high-definition (UHD) image restoration poses unique challenges due to the high spatial resolution, diverse content, and fine-grained structures present in UHD images. To address these issues, we introduce a progressive spectral decomposition for the restoration process, decomposing it into three stages: zero-frequency \textbf{enhancement}, low-frequency \textbf{restoration}, and high-frequency \textbf{refinement}. Based on this formulation, we propose a novel framework, \textbf{ERR}, which integrates three cooperative sub-networks: the zero-frequency enhancer (ZFE), the low-frequency restorer (LFR), and the high-frequency refiner (HFR). The ZFE incorporates global priors to learn holistic mappings, the LFR reconstructs the main content by focusing on coarse-scale information, and the HFR adopts our proposed frequency-windowed Kolmogorov-Arnold Network (FW-KAN) to recover fine textures and intricate details for high-fidelity restoration. To further advance research in UHD image restoration, we also construct a large-scale, high-quality benchmark dataset, \textbf{LSUHDIR}, comprising 82{,}126 UHD images with diverse scenes and rich content. Our proposed methods demonstrate superior performance across a range of UHD image restoration tasks, and extensive ablation studies confirm the contribution and necessity of each module. Project page: this https URL.

---


### 75. [DPDSyn: Improving Differentially Private Dataset Synthesis for Model Training by Downstream Task Guidance](https://arxiv.org/abs/2604.15660)

**<font color=#1a73e8>作者：</font>** Mingxuan Jia, Wen Huang, Weixin Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> How to synthesize a dataset while achieving differential privacy for AI model training is a meaningful but challenging problem. To address this problem, state-of-the-art methods first select original private dataset's multiple low-dimensional distributions that have the potential to approximate the distribution of original private dataset with high precision, and then synthesize a dataset obeying all selected low-dimensional distributions as the synthetic dataset. However, it is difficult to select suitable low-dimensional distributions, which in turn degrades the data utility of resulting synthetic dataset. To improve differentially private dataset synthesis, we propose to train a differentially private AI model for downstream tasks on the original private dataset and utilize the trained model to synthesize datasets. In particular, on the one hand, the AI model satisfies differential privacy so no matter how to use the model does not disclose private information of original private dataset. On the other hand, the AI model is trained to complete the downstream task so the AI model preserves critical information for completing downstream tasks. We utilize the AI model to synthesize datasets to achieve the goal of improving data utility while preserving privacy. Empirical evaluations on four benchmark datasets demonstrate that our proposed DPDSyn consistently outperforms eight state-of-the-art baselines with a maximum improvement of 2.40x in accuracy and 333.73x in synthesis efficiency. Further experiments also validate that DPDSyn has strong scalability across varying data scales.

---


### 76. [Designing More Engaging Serious Games to Support Students' Mental Health: A Pilot Study Based on A CBT-Informed Design Framework](https://arxiv.org/abs/2604.15662)

**<font color=#1a73e8>作者：</font>** Ting-Chen Hsu, Zheyuan Zhang, Ziyi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Addressing the issues of dullness, low compliance, and lack of appeal in current digital mental health education and serious games for students and adolescents, this study proposes a novel, experience-centered framework for serious game design: the Therapeutic Procedural Rhetoric and Mechanism Mapping Framework (TPR-MMF). Based on this framework, a side-scrolling serious game prototype, "World + You - World," was developed. This study compared the effectiveness of TPR-MMF-based games with traditional explicit educational serious games through a small-sample randomized controlled trial (N=28). The results of the Intrinsic Motivation Inventory (IMI) showed that the experimental group (playing "World + You - World") significantly outperformed the control group in four aspects. Furthermore, qualitative survey results indicated that players could perceive the psychological metaphors within the game mechanics and spontaneously resonated with real-life experiences. This study provides a highly engaging new development paradigm for gamified mental health education for students and adolescents.

---


### 77. [Stargazer: A Scalable Model-Fitting Benchmark Environment for AI Agents under Astrophysical Constraints](https://arxiv.org/abs/2604.15664)

**<font color=#1a73e8>作者：</font>** Xinge Liu, Terry Jingchen Zhang, Bernhard Schölkopf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rise of autonomous AI agents suggests that dynamic benchmark environments with built-in feedback on scientifically grounded tasks are needed to evaluate the capabilities of these agents in research work. We introduce Stargazer, a scalable environment for evaluating AI agents on dynamic, iterative physics-grounded model-fitting tasks using inference on radial-velocity (RV) time series data. Stargazer comprises 120 tasks across three difficulty tiers, including 20 real archival cases, covering diverse scenarios ranging from high-SNR single-planet systems to complex multi-planetary configurations requiring involved low-SNR analysis. Our evaluation of eight frontier agents reveals a gap between numerical optimization and adherence to physical constraints: although agents often achieve a good statistical fit, they frequently fail to recover correct physical system parameters, a limitation that persists even when agents are equipped with vanilla skills. Furthermore, increasing test-time compute yields only marginal gains, with excessive token usage often reflecting recursive failure loops rather than meaningful exploration. Stargazer presents an opportunity to train, evaluate, scaffold, and scale strategies on a model-fitting problem of practical research relevance today. Our methodology to design a simulation-driven environment for AI agents presumably generalizes to many other model-fitting problems across scientific domains. Source code and the project website are available at this https URL and this https URL, respectively.

---


### 78. [CPU Optimization of a Monocular 3D Biomechanics Pipeline for Low-Resource Deployment](https://arxiv.org/abs/2604.15665)

**<font color=#1a73e8>作者：</font>** Yan Zhang, Xiong Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Markerless 3D movement analysis from monocular video enables accessible biomechanical assessment in clinical and sports settings. However, most research-grade pipelines rely on GPU acceleration, limiting deployment on consumer-grade hardware and in low-resource environments. In this work, we optimize a monocular 3D biomechanics pipeline derived from the MonocularBiomechanics framework for efficient CPU-only execution. Through profiling-driven system optimization, including model initialization restructuring, elimination of disk I/O serialization, and improved CPU parallelization. Experiments on a consumer workstation (AMD Ryzen 7 9700X CPU) show a 2.47x increase in processing throughput and a 59.6\% reduction in total runtime, with initialization latency reduced by 4.6x. Despite these changes, biomechanical outputs remain highly consistent with the baseline implementation (mean joint-angle deviation 0.35$^\circ$, $r=0.998$). These results demonstrate that research-grade vision-based biomechanics pipelines can be deployed on commodity CPU hardware for scalable movement assessment.

---


### 79. [NK-GAD: Neighbor Knowledge-Enhanced Unsupervised Graph Anomaly Detection](https://arxiv.org/abs/2604.15668)

**<font color=#1a73e8>作者：</font>** Zehao Wang, Lanjun Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph anomaly detection aims to identify irregular patterns in graph-structured data. Most unsupervised GNN-based methods rely on the homophily assumption that connected nodes share similar attributes. However, real-world graphs often exhibit attribute-level heterophily, where connected nodes have dissimilar attributes. Our analysis of attribute-level heterophily graphs reveals two phenomena indicating that current approaches are not practical for unsupervised graph anomaly detection: 1) attribute similarities between connected nodes show nearly identical distributions across different connected node pair types, and 2) anomalies cause consistent variation trends between the graph with and without anomalous edges in the low- and high-frequency components of the spectral energy distributions, while the mid-part exhibits more erratic variations. Based on these observations, we propose NK-GAD, a neighbor knowledge-enhanced unsupervised graph anomaly detection framework. NK-GAD integrates a joint encoder capturing both similar and dissimilar neighbor features, a neighbor reconstruction module modeling normal distributions, a center aggregation module refining node features, and dual decoders for reconstructing attributes and structures. Experiments on seven datasets show NK-GAD achieves an average 3.29\% AUC improvement.

---


### 80. [DEMUX: Boundary-Aware Multi-Scale Traffic Demixing for Multi-Tab Website Fingerprinting](https://arxiv.org/abs/2604.15677)

**<font color=#1a73e8>作者：</font>** Yali Yuan, Yaosheng Liu, Qianqi Niu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Website fingerprinting (WF) attacks infer the websites visited by users from encrypted traffic in anonymous networks such as Tor. Existing deep learning methods achieve high accuracy under the single-tab assumption but degrade substantially when users open multiple tabs concurrently, producing interleaved traffic that transforms WF into an implicit demixing problem. We identify three structural requirements for effective multi-tab demixing, namely signal integrity at segment boundaries, multi-scale local modeling, and relative temporal association of dispersed fragments, and show that no prior method satisfies all three simultaneously. We propose DEMUX, a designed framework that addresses these requirements through three tightly coupled components. A Boundary Preserving Aggregation Module employs overlapping window partitioning with joint packet-level and burst-level feature extraction. A Multi-Scale Parallel CNN captures heterogeneous temporal patterns via parallel branches. A two-stage Transformer encoder with Rotary Positional Embedding enables robust cross-window fragment association. The Boundary Preserving Aggregation Module additionally serves as a plug-and-play preprocessor that consistently improves existing baselines without architectural modification. Extensive experiments across closed-world, open-world, defense-augmented, dynamic-tab, and cross-configuration settings demonstrate that DEMUX achieves state-of-the-art performance. In the challenging closed-world 5-tab setting, DEMUX attains a P@5 of 0.943 and MAP@5 of 0.961, outperforming the strongest baseline by 9.2 and 6.2 percentage points respectively, confirming its strong robustness in complex multi-tab demixing scenarios.

---


### 81. [HyCal: A Training-Free Prototype Calibration Method for Cross-Discipline Few-Shot Class-Incremental Learning](https://arxiv.org/abs/2604.15678)

**<font color=#1a73e8>作者：</font>** Eunju Lee, MiHyeon Kim, JuneHyoung Kwon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained Vision-Language Models (VLMs) like CLIP show promise in continual learning, but existing Few-Shot Class-Incremental Learning (FSCIL) methods assume homogeneous domains and balanced data distributions, limiting real-world applicability where data arises from heterogeneous disciplines with imbalanced sample availability and varying visual complexity. We identify Domain Gravity, a representational asymmetry where data imbalance across heterogeneous domains causes overrepresented or low-entropy domains to disproportionately influence the embedding space, leading to prototype drift and degraded performance on underrepresented or high-entropy domains. To address this, we introduce Cross-Discipline Variable Few-Shot Class-Incremental Learning (XD-VSCIL), a benchmark capturing real-world heterogeneity and imbalance where Domain Gravity naturally intensifies. We propose Hybrid Prototype Calibration (HyCal), a training-free method combining cosine similarity and Mahalanobis distance to capture complementary geometric properties-directional alignment and covariance-aware magnitude-yielding stable prototypes under imbalanced heterogeneous conditions. Operating on frozen CLIP embeddings, HyCal achieves consistent retention-adaptation improvements while maintaining efficiency. Experiments show HyCal effectively mitigates Domain Gravity and outperforms existing methods in imbalanced cross-domain incremental learning.

---


### 82. [Hierarchical Active Inference using Successor Representations](https://arxiv.org/abs/2604.15679)

**<font color=#1a73e8>作者：</font>** Prashant Rangarajan, Rajesh P. N. Rao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active inference, a neurally-inspired model for inferring actions based on the free energy principle (FEP), has been proposed as a unifying framework for understanding perception, action, and learning in the brain. Active inference has previously been used to model ecologically important tasks such as navigation and planning, but scaling it to solve complex large-scale problems in real-world environments has remained a challenge. Inspired by the existence of multi-scale hierarchical representations in the brain, we propose a model for planning of actions based on hierarchical active inference. Our approach combines a hierarchical model of the environment with successor representations for efficient planning. We present results demonstrating (1) how lower-level successor representations can be used to learn higher-level abstract states, (2) how planning based on active inference at the lower-level can be used to bootstrap and learn higher-level abstract actions, and (3) how these learned higher-level abstract states and actions can facilitate efficient planning. We illustrate the performance of the approach on several planning and reinforcement learning (RL) problems including a variant of the well-known four rooms task, a key-based navigation task, a partially observable planning problem, the Mountain Car problem, and PointMaze, a family of navigation tasks with continuous state and action spaces. Our results represent, to our knowledge, the first application of learned hierarchical state and action abstractions to active inference in FEP-based theories of brain function.

---


### 83. [Self-Supervised Angular Deblurring in Photoacoustic Reconstruction via Noisier2Inverse](https://arxiv.org/abs/2604.15681)

**<font color=#1a73e8>作者：</font>** Markus Haltmeier, Nadja Gruber, Gyeongha Hwang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photoacoustic tomography (PAT) is an emerging imaging modality that combines the complementary strengths of optical contrast and ultrasonic resolution. A central task is image reconstruction, where measured acoustic signals are used to recover the initial pressure distribution. For ideal point-like or line-like detectors, several efficient and fast reconstruction algorithms exist, including Fourier methods, filtered backprojection, and time reversal. However, when applied to data acquired with finite-size detectors, these methods yield systematically blurred images. Although sharper images can be obtained by compensating for finite-detector effects, supervised learning approaches typically require ground-truth images that may not be available in practice. We propose a self-supervised reconstruction method based on Noisier2Inverse that addresses finite-size detector effects without requiring ground-truth data. Our approach operates directly on noisy measurements and learns to recover high-quality PAT images in a ground-truth-free manner. Its key components are: (i) PAT-specific modeling that recasts the problem as angular deblurring; (ii) a Noisier2Inverse formulation in the polar domain that leverages the known angular point-spread function; and (iii) a novel, statistically grounded early-stopping rule. In experiments, the proposed method consistently outperforms alternative approaches that do not use supervised data and achieves performance close to supervised benchmarks, while remaining practical for real acquisitions with finite-size detectors.

---


### 84. [Neural Continuous-Time Markov Chain: Discrete Diffusion via Decoupled Jump Timing and Direction](https://arxiv.org/abs/2604.15694)

**<font color=#1a73e8>作者：</font>** Jingyuan Li, Xiaoyi Jiang, Fukang Wen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models based on continuous-time Markov chains (CTMCs) have shown strong performance on language and discrete data generation, yet existing approaches typically parameterize the reverse rate matrix as a single object -- via concrete scores, clean-data predictions ($x_0$-parameterization), or denoising distributions -- rather than aligning the parameterization with the intrinsic CTMC decomposition into jump timing and jump direction. Since a CTMC is fundamentally a Poisson process fully determined by these two quantities, decomposing along this structure is closer to first principles and naturally leads to our formulation. We propose \textbf{Neural CTMC}, which separately parameterizes the reverse process through an \emph{exit rate} (when to jump) and a \emph{jump distribution} (where to jump) using two dedicated network heads. We show that the evidence lower bound (ELBO) differs from a path-space KL divergence between the true and learned reverse processes by a $\theta$-independent constant, so that the training objective is fully governed by the exit rate and jump distribution we parameterize. Moreover, this KL factorizes into a Poisson KL for timing and a categorical KL for direction. We further show that the tractable conditional surrogate preserves the gradients and minimizers of the corresponding marginal reverse-process objective under standard regularity assumptions. Our theoretical framework also covers masked and GIDD-style noise schedules. Empirically, while the uniform forward process has been explored in prior work, our model, to our best of the knowledge, is the first pure-uniform method to outperform mask-based methods on the OpenWebText this http URL facilitate reproducibility, we release our pretrained weights at this https URL.

---


### 85. [Graph self-supervised learning based on frequency corruption](https://arxiv.org/abs/2604.15699)

**<font color=#1a73e8>作者：</font>** Haojie Li, Mengjiao Zhang, Guanfeng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph self-supervised learning can reduce the need for labeled graph data and has been widely used in recommendation, social networks, and other web applications. However, existing methods often underuse high-frequency signals and may overfit to specific local patterns, which limits representation quality and generalization. We propose Frequency-Corrupt Based Graph Self-Supervised Learning (FC-GSSL), a method that builds corrupted graphs biased toward high-frequency information by corrupting nodes and edges according to their low-frequency contributions. These corrupted graphs are used as inputs to an autoencoder, while low-frequency and general features are reconstructed as supervision targets, forcing the model to fuse information from multiple frequency bands. We further design multiple sampling strategies and generate diverse corrupted graphs from the intersections and unions of the sampling results. By aligning node representations from these views, the model can discover useful frequency combinations, reduce reliance on specific high-frequency components, and improve robustness. Experiments on 14 datasets across node classification, graph prediction, and transfer learning show that FC-GSSL consistently improves performance and generalization.

---


### 86. [Target-Oriented Pretraining Data Selection via Neuron-Activated Graph](https://arxiv.org/abs/2604.15706)

**<font color=#1a73e8>作者：</font>** Zijun Wang, Haoqin Tu, Weidong Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Everyday tasks come with a target, and pretraining models around this target is what turns them into experts. In this paper, we study target-oriented language model (LM) pretraining by introducing Neuron-Activated Graph Ranking (NAG-based Ranking), a training-free and interpretable framework for target pretraining data selection. Rather than using black-box representations, our approach directly characterizes each target input by a sparse set of high-impact neurons in any off-the-shelf LLMs. Concretely, we quantify neuron impact and select the most influential neurons across layers into a compact Neuron-Activated Graph (NAG), and rank candidate data by NAG similarity to target examples. We conduct experiments across six benchmarks, where our NAG-based Ranking improves target-oriented pretraining by 4.9% on average over random sampling, and also outperforms state-of-the-art baselines by 5.3% accuracy on HellaSwag. It also remains effective under a more applicable multi-target setting, where our best setup surpasses two baselines by 1.1% and 4.1%, respectively. Furthermore, we provide a comprehensive analysis on why and how our NAG works, e.g., deactivating NAG-selected neurons (only 0.12% of all) causes a 23.5% performance collapse, and restricting NAG to the final layer incurs a 4.1% average drop, indicating that NAG captures a sparse "functional backbone" for learning target features. We release the code at this https URL.

---


### 87. [LP$^{2}$DH: A Locality-Preserving Pixel-Difference Hashing Framework for Dynamic Texture Recognition](https://arxiv.org/abs/2604.15707)

**<font color=#1a73e8>作者：</font>** Ruxin Ding, Jianfeng Ren, Heng Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal Local Binary Pattern (STLBP) is a widely used dynamic texture descriptor, but it suffers from extremely high dimensionality. To tackle this, STLBP features are often extracted on three orthogonal planes, which sacrifice inter-plane correlation. In this work, we propose a Locality-Preserving Pixel-Difference Hashing (LP$^{2}$DH) framework that jointly encodes pixel differences in the full spatiotemporal neighbourhood. LP$^{2}$DH transforms Pixel-Difference Vectors (PDVs) into compact binary codes with maximal discriminative power. Furthermore, we incorporate a locality-preserving embedding to maintain the PDVs' local structure before and after hashing. Then, a curvilinear search strategy is utilized to jointly optimize the hashing matrix and binary codes via gradient descent on the Stiefel manifold. After hashing, dictionary learning is applied to encode the binary vectors into codewords, and the resulting histogram is utilized as the final feature representation. The proposed LP$^{2}$DH achieves state-of-the-art performance on three major dynamic texture recognition benchmarks: 99.80% against DT-GoogleNet's 98.93% on UCLA, 98.52% against HoGF$^{3D}$'s 97.63% on DynTex++, and 96.19% compared to STS's 95.00% on YUPENN. The source code is available at: this https URL.

---


### 88. [APC: Transferable and Efficient Adversarial Point Counterattack for Robust 3D Point Cloud Recognition](https://arxiv.org/abs/2604.15708)

**<font color=#1a73e8>作者：</font>** Geunyoung Jung, Soohong Kim, Inseok Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advent of deep neural networks has led to remarkable progress in 3D point cloud recognition, but they remain vulnerable to adversarial attacks. Although various defense methods have been studied, they suffer from a trade-off between robustness and transferability. We propose Adversarial Point Counterattack (APC) to achieve both simultaneously. APC is a lightweight input-level purification module that generates instance-specific counter-perturbations for each point, effectively neutralizing attacks. Leveraging clean-adversarial pairs, APC enforces geometric consistency in data space and semantic consistency in feature space. To improve generalizability across diverse attacks, we adopt a hybrid training strategy using adversarial point clouds from multiple attack types. Since APC operates purely on input point clouds, it directly transfers to unseen models and defends against attacks targeting them without retraining. At inference, a single APC forward pass provides purified point clouds with negligible time and parameter overhead. Extensive experiments on two 3D recognition benchmarks demonstrate that the APC achieves state-of-the-art defense performance. Furthermore, cross-model evaluations validate its superior transferability. The code is available at this https URL.

---


### 89. [Bilevel Optimization of Agent Skills via Monte Carlo Tree Search](https://arxiv.org/abs/2604.15709)

**<font color=#1a73e8>作者：</font>** Chenyi Huang, Haoting Zhang, Jingxu Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent \texttt{skills} are structured collections of instructions, tools, and supporting resources that help large language model (LLM) agents perform particular classes of tasks. Empirical evidence shows that the design of \texttt{skills} can materially affect agent task performance, yet systematically optimizing \texttt{skills} remains challenging. Since a \texttt{skill} comprises instructions, tools, and supporting resources in a structured way, optimizing it requires jointly determining both the structure of these components and the content each component contains. This gives rise to a complex decision space with strong interdependence across structure and components. We therefore represent these two coupled decisions as \texttt{skill} structure and component content, and formulate \texttt{skill} optimization as a bilevel optimization problem. We propose a bilevel optimization framework in which an outer loop employs Monte Carlo Tree Search to determine the \texttt{skill} structure, while an inner loop refines the component content within the structure selected by the outer loop. In both loops, we employ LLMs to assist the optimization procedure. We evaluate the proposed framework on an open-source Operations Research Question Answering dataset, and the experimental results suggest that the bilevel optimization framework improves the performance of the agents with the optimized \texttt{skill}.

---


### 90. [SSMamba: A Self-Supervised Hybrid State Space Model for Pathological Image Classification](https://arxiv.org/abs/2604.15711)

**<font color=#1a73e8>作者：</font>** Enhui Chai, Sicheng Chen, Tianyi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathological diagnosis is highly reliant on image analysis, where Regions of Interest (ROIs) serve as the primary basis for diagnostic evidence, while whole-slide image (WSI)-level tasks primarily capture aggregated patterns. To extract these critical morphological features, ROI-level Foundation Models (FMs) based on Vision Transformers (ViTs) and large-scale self-supervised learning (SSL) have been widely adopted. However, three core limitations remain in their application to ROI analysis: (1) cross-magnification domain shift, as fixed-scale pretraining hinders adaptation to diverse clinical settings; (2) inadequate local-global relationship modeling, wherein the ViT backbone of FMs suffers from high computational overhead and imprecise local characterization; (3) insufficient fine-grained sensitivity, as traditional self-attention mechanisms tend to overlook subtle diagnostic cues. To address these challenges, we propose SSMamba, a hybrid SSL framework that enables effective fine-grained feature learning without relying on large external datasets. This framework incorporates three domain-adaptive components: Mamba Masked Image Modeling (MAMIM) for mitigating domain shift, a Directional Multi-scale (DMS) module for balanced local-global modeling, and a Local Perception Residual (LPR) module for enhanced fine-grained sensitivity. Employing a two-stage pipeline, SSL pretraining on target ROI datasets followed by supervised fine-tuning (SFT), SSMamba outperforms 11 state-of-the-art (SOTA) pathological FMs on 10 public ROI datasets and surpasses 8 SOTA methods on 6 public WSI datasets. These results validate the superiority of task-specific architectural designs for pathological image analysis.

---


### 91. [GTA-2: Benchmarking General Tool Agents from Atomic Tool-Use to Open-Ended Workflows](https://arxiv.org/abs/2604.15715)

**<font color=#1a73e8>作者：</font>** Jize Wang, Xuanxuan Liu, Yining Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The development of general-purpose agents requires a shift from executing simple instructions to completing complex, real-world productivity workflows. However, current tool-use benchmarks remain misaligned with real-world requirements, relying on AI-generated queries, dummy tools, and limited system-level coordination. To address this, we propose GTA-2, a hierarchical benchmark for General Tool Agents (GTA) spanning atomic tool use and open-ended workflows. Built on real-world authenticity, it leverages real user queries, deployed tools, and multimodal contexts. (i) GTA-Atomic, inherited from our prior GTA benchmark, evaluates short-horizon, closed-ended tool-use precision. (ii) GTA-Workflow introduces long-horizon, open-ended tasks for realistic end-to-end completion. To evaluate open-ended deliverables, we propose a recursive checkpoint-based evaluation mechanism that decomposes objectives into verifiable sub-goals, enabling unified evaluation of both model capabilities and agent execution frameworks (i.e., execution harnesses). Experiments reveal a pronounced capability cliff: while frontier models already struggle on atomic tasks (below 50%), they largely fail on workflows, with top models achieving only 14.39% success. Further analysis shows that checkpoint-guided feedback improves performance, while advanced frameworks such as Manus and OpenClaw substantially enhance workflow completion, highlighting the importance of execution harness design beyond the underlying model capacity. These findings provide guidance for developing reliable personal and professional assistants. Dataset and code will be available at this https URL.

---


### 92. [NeuroLip: An Event-driven Spatiotemporal Learning Framework for Cross-Scene Lip-Motion-based Visual Speaker Recognition](https://arxiv.org/abs/2604.15718)

**<font color=#1a73e8>作者：</font>** Junguang Yao, Wenye Liu, Stjepan Picek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual speaker recognition based on lip motion offers a silent, hands-free, and behavior-driven biometric solution that remains effective even when acoustic cues are unavailable. Compared to traditional methods that rely heavily on appearance-dependent representations, lip motion encodes subject-specific behavioral dynamics driven by consistent articulation patterns and muscle coordination, offering inherent stability across environmental changes. However, capturing these robust, fine-grained dynamics is challenging for conventional frame-based cameras due to motion blur and low dynamic range. To exploit the intrinsic stability of lip motion and address these sensing limitations, we propose NeuroLip, an event-based framework that captures fine-grained lip dynamics under a strict yet practical cross-scene protocol: training is performed under a single controlled condition, while recognition must generalize to unseen viewing and lighting conditions. NeuroLip features a 1) Temporal-aware Voxel Encoding module with adaptive event weighting, 2) Structure-aware Spatial Enhancer that amplifies discriminative behavioral patterns by suppressing noise while preserving vertically structured motion information, and 3) Polarity Consistency Regularization mechanism to retain motion-direction cues encoded in event polarities. To facilitate systematic evaluation, we introduce DVSpeaker, a comprehensive event-based lip-motion dataset comprising 50 subjects recorded under four distinct viewpoint and illumination scenarios. Extensive experiments demonstrate that NeuroLip achieves near-perfect matched-scene accuracy and robust cross-scene generalization, attaining over 71% accuracy on unseen viewpoints and nearly 76% under low-light conditions, outperforming representative existing methods by at least 8.54%. The dataset and code are publicly available at this https URL.

---


### 93. [The World Leaks the Future: Harness Evolution for Future Prediction Agents](https://arxiv.org/abs/2604.15719)

**<font color=#1a73e8>作者：</font>** Chuyang Wei, Maohang Gao, Zhixin Han 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many consequential decisions must be made before the relevant outcome is known. Such problems are commonly framed as \emph{future prediction}, where an LLM agent must form a prediction for an unresolved question using only the public information available at the prediction time. The setting is difficult because public evidence evolves while useful supervision arrives only after the question is resolved, so most existing approaches still improve mainly from final outcomes. Yet final outcomes are too coarse to guide earlier factor tracking, evidence gathering and interpretation, or uncertainty handling. When the same unresolved question is revisited over time, temporal contrasts between earlier and later predictions can expose omissions in the earlier prediction process; we call this signal \emph{internal feedback}. We introduce \emph{Milkyway}, a self-evolving agent system that keeps the base model fixed and instead updates a persistent \emph{future prediction harness} for factor tracking, evidence gathering and interpretation, and uncertainty handling. Across repeated predictions on the same unresolved question, \emph{Milkyway} extracts internal feedback and writes reusable guidance back into the harness, so later predictions on that question can improve before the outcome is known. After the question is resolved, the final outcome provides a \emph{retrospective check} before the updated harness is carried forward to subsequent questions. On FutureX and FutureWorld, Milkyway achieves the best overall score among the compared methods, improving FutureX from 44.07 to 60.90 and FutureWorld from 62.22 to 77.96.

---


### 94. [Diffusion Autoencoder for Unsupervised Artifact Restoration in Handheld Fundus Images](https://arxiv.org/abs/2604.15723)

**<font color=#1a73e8>作者：</font>** Mathumetha Palani, Kavya Puthumana, Ayantika Das 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advent of handheld fundus imaging devices has made ophthalmologic diagnosis and disease screening more accessible, efficient, and cost-effective. However, images captured from these setups often suffer from artifacts such as flash reflections, exposure variations, and motion-induced blur, which degrade image quality and hinder downstream analysis. While generative models have been effective in image restoration, most depend on paired supervision or predefined artifact structures, making them less adaptable to unstructured degradations commonly observed in handheld fundus images. To address this, we propose an unsupervised diffusion autoencoder that integrates a context encoder with the denoising process to learn semantically meaningful representations for artifact restoration. The model is trained only on high-quality table-top fundus images and infers to restore artifact-affected handheld acquisitions. We validate the restorations through quantitative and qualitative evaluations, and have shown that diagnostic accuracy increases to 81.17% on an unseen dataset and multiple artifact conditions

---


### 95. [MambaBack: Bridging Local Features and Global Contexts in Whole Slide Image Analysis](https://arxiv.org/abs/2604.15729)

**<font color=#1a73e8>作者：</font>** Sicheng Chen, Chad Wong, Tianyi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole Slide Image (WSI) analysis is pivotal in computational pathology, enabling cancer diagnosis by integrating morphological and architectural cues across magnifications. Multiple Instance Learning (MIL) serves as the standard framework for WSI analysis. Recently, Mamba has become a promising backbone for MIL, overtaking Transformers due to its efficiency and global context modeling capabilities originating from Natural Language Processing (NLP). However, existing Mamba-based MIL approaches face three critical challenges: (1) disruption of 2D spatial locality during 1D sequence flattening; (2) sub-optimal modeling of fine-grained local cellular structures; and (3) high memory peaks during inference on resource-constrained edge devices. Studies like MambaOut reveal that Mamba's SSM component is redundant for local feature extraction, where Gated CNNs suffice. Recognizing that WSI analysis demands both fine-grained local feature extraction akin to natural images, and global context modeling akin to NLP, we propose MambaBack, a novel hybrid architecture that harmonizes the strengths of Mamba and MambaOut. First, we propose the Hilbert sampling strategy to preserve the 2D spatial locality of tiles within 1D sequences, enhancing the model's spatial perception. Second, we design a hierarchical structure comprising a 1D Gated CNN block based on MambaOut to capture local cellular features, and a BiMamba2 block to aggregate global context, jointly enhancing multi-scale representation. Finally, we implement an asymmetric chunking design, allowing parallel processing during training and chunking-streaming accumulation during inference, minimizing peak memory usage for deployment. Experimental results on five datasets demonstrate that MambaBack outperforms seven state-of-the-art methods. Source code and datasets are publicly available.

---


### 96. [Sketch and Text Synergy: Fusing Structural Contours and Descriptive Attributes for Fine-Grained Image Retrieval](https://arxiv.org/abs/2604.15735)

**<font color=#1a73e8>作者：</font>** Siyuan Wang, Hanchen Gao, Guangming Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained image retrieval via hand-drawn sketches or textual descriptions remains a critical challenge due to inherent modality gaps. While hand-drawn sketches capture complex structural contours, they lack color and texture, which text effectively provides despite omitting spatial contours. Motivated by the complementary nature of these modalities, we propose the Sketch and Text Based Image Retrieval (STBIR) framework. By synergizing the rich color and texture cues from text with the structural outlines provided by sketches, STBIR achieves superior fine-grained retrieval performance. First, a curriculum learning driven robustness enhancement module is proposed to enhance the model's robustness when handling queries of varying quality. Second, we introduce a category-knowledge-based feature space optimization module, thereby significantly boosting the model's representational power. Finally, we design a multi-stage cross-modal feature alignment mechanism to effectively mitigate the challenges of cross modal feature alignment. Furthermore, we curate the fine-grained STBIR benchmark dataset to rigorously validate the efficacy of our proposed framework and to provide data support as a reference for subsequent related research. Extensive experiments demonstrate that the proposed STBIR framework significantly outperforms state of the art methods.

---


### 97. [Why Colors Make Clustering Harder:Global Integrality Gaps, the Price of Fairness, and Color-Coupled Algorithms in Chromatic Correlation Clustering](https://arxiv.org/abs/2604.15738)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chromatic Correlation Clustering (CCC) extends Correlation Clustering by assigning semantic colors to edges and requiring each cluster to receive a single color label. Unlike standard CC, whose LP relaxation has integrality gap 2 on complete graphs and admits a 2.06-approximation, the analogous LP for CCC has a strict lower bound of 2.11, and the best known LP-rounding algorithm achieves 2.15. We explain this gap by isolating the source of difficulty: cross-edge chromatic interference. Neutral edges, whose color does not match the candidate cluster color, create an irreducible cost absent from standard CC and force any color-independent rounding scheme to pay an additional mismatch penalty.
We make four contributions. First, we prove a Global Integrality Gap Decomposition Theorem showing that the gap of any color-independent CCC rounding algorithm equals the standard CC gap plus an irreducible chromatic penalty Delta(L) > 0. Second, we solve the associated min-max problem and derive the staircase formula Delta(L) = ((L-1)/L) Delta_infinity, where Delta_infinity is approximately 0.0734. In particular, the two-color gap is 2.0967, separating CCC from standard CC already at L = 2. Third, we introduce Color-Coupled Correlation Clustering (C4). Adding the valid global constraint sum_c x_uv^c >= L-1 and a correlated interval-packing rounding scheme makes neutral edges behave like classical negative edges, recovering the optimal 2.06 approximation and bypassing the 2.11 lower bound for the uncoupled LP. Fourth, experiments on extremal instances, real multi-relational networks, and fairness benchmarks validate the theory: empirical LP gaps follow the predicted staircase, and C4 matches the unconstrained approximation ratio under fairness constraints.

---


### 98. [Collective Kernel EFT for Pre-activation ResNets](https://arxiv.org/abs/2604.15742)

**<font color=#1a73e8>作者：</font>** Hidetoshi Kawase, Toshihiro Ota  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In finite-width deep neural networks, the empirical kernel $G$ evolves stochastically across layers. We develop a collective kernel effective field theory (EFT) for pre-activation ResNets based on a $G$-only closure hierarchy and diagnose its finite validity window. Exploiting the exact conditional Gaussianity of residual increments, we derive an exact stochastic recursion for $G$. Applying Gaussian approximations systematically yields a continuous-depth ODE system for the mean kernel $K_0$, the kernel covariance $V_4$, and the $1/n$ mean correction $K_{1,\mathrm{EFT}}$, which emerges diagrammatically as a one-loop tadpole correction. Numerically, $K_0$ remains accurate at all depths. However, the $V_4$ equation residual accumulates to an $O(1)$ error at finite time, primarily driven by approximation errors in the $G$-only transport term. Furthermore, $K_{1,\mathrm{EFT}}$ fails due to the breakdown of the source closure, which exhibits a systematic mismatch even at initialization. These findings highlight the limitations of $G$-only state-space reduction and suggest extending the state space to incorporate the sigma-kernel.

---


### 99. [DepCap: Adaptive Block-Wise Parallel Decoding for Efficient Diffusion LM Inference](https://arxiv.org/abs/2604.15750)

**<font color=#1a73e8>作者：</font>** Xiang Xia, Wuyang Zhang, Jiazheng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive language generation due to their potential for parallel decoding and global refinement of the entire sequence. To unlock this potential, DLM inference must carefully balance generation quality and decoding speed. Recent block-wise DLM decoding methods improve this trade-off by performing diffusion-based decoding sequentially in blocks. However, existing methods typically rely on fixed block schedules or current-step local signals to determine block boundaries, and use conservative confidence-based parallel decoding to avoid conflicts, limiting the quality-speed trade-off. In this paper, we argue that block-wise DLM inference requires more suitable signals for its two core decisions: cross-step signals for determining block boundaries, and token-level conflict signals for parallel decoding. Based on this view, we propose DepCap, a training-free framework for efficient block-wise DLM inference. Specifically, DepCap instantiates the cross-step signal as the influence of the last decoded block and uses it to adaptively determine how far the next block should extend, while identifying a conflict-free subset of tokens for safe parallel decoding within each block, enabling substantial inference acceleration with negligible quality degradation. DepCap is a plug-and-play method applicable to various DLMs, and compatible with existing KV-cache strategies for block-wise DLM. An information-theoretic analysis further suggests that the cumulative last-block influence on a candidate block is approximately additive across tokens, supporting the proposed block-partitioning criterion. Experimental results show that DepCap achieves favorable speed-quality trade-offs across multiple DLM backbones and reasoning and coding benchmarks, with up to 5.63$\times$ speedup without significant performance degradation.

---


### 100. [PoSME: Proof of Sequential Memory Execution via Latency-Bound Pointer Chasing with Causal Hash Binding](https://arxiv.org/abs/2604.15751)

**<font color=#1a73e8>作者：</font>** David L. Condrey  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce PoSME (Proof of Sequential Memory Execution), a cryptographic primitive that enforces sustained sequential computation via latency-bound pointer chasing over a mutable arena. Each step reads data-dependent addresses, writes a block whose value and causal hash are mutually dependent (symbiotic binding), and chains the result into a global transcript. This yields three properties: (1) strict linear sequential memory-step enforcement, (2) high time-memory trade-off resistance (a tenfold penalty at a write density of 4, with a formal space-time lower bound that scales quadratically with the number of steps), and (3) a tight ASIC advantage bound by DRAM random-access latency rather than bandwidth. Benchmarks across 17 CPU platforms and 4 GPU architectures demonstrate that hash computation is under 3.5 percent of step cost and GPU hardware is 14 to 19 times slower than a consumer CPU. POSME requires no trusted setup and provides a foundation for verifiable delay, authorship attestation, and Sybil resistance.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-203](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
