# 📦 其他研究 | 2026年05月06日

> 本类共 **511** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

---

### 51. [Robust volatility updates for Hierarchical Gaussian Filtering](https://arxiv.org/abs/2605.00966)

**<font color=#1a73e8>作者：</font>** Christoph Mathys, Nicolas Legrand, Peter Thestrup Waade 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical Gaussian Filtering (HGF) networks allow for efficient updating of posterior distributions (beliefs) about hidden states of an agent's environment. HGF parent nodes can target the mean or variance of their children. New information entering at input nodes leads to a cascade of belief updates across the network according to one-step update equations for each node's mean and precision (inverse variance). However, the original form of the update equations for variance-targeting parents(volatility coupling) can in some regions of parameter space lead to negative posterior precision, a logical impossibility which causes the updating algorithm to terminate with an error. In this report, we introduce a modified quadratic approximation to the variational energy of volatility-coupled nodes that avoids negative posterior precision. The key idea is to interpolate between two quadratic expansions of the variational energy: one at the prior prediction and one at a second mode whose location is obtained in closed form via the Lambert W function. The resulting update equations are robust across the entire parameter space and faithfully track the variational posterior even for large prediction errors.

---


### 52. [Physiology-Aware Masked Cross-Modal Reconstruction for Biosignal Representation Learning](https://arxiv.org/abs/2605.00973)

**<font color=#1a73e8>作者：</font>** Hao Zhou, Simon A. Lee, Cyrus Tanade 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biosignals acquired from different locations on the body often provide temporally ordered views of the same underlying physiological process. However, most existing self supervised learning methods treat these signals as interchangeable views, overlooking the directional temporal dynamics that link them. A canonical example is the relationship between electrocardiography (ECG), which captures the electrical activation initiating each heartbeat, and photoplethysmography (PPG), which records the resulting peripheral pulse delayed by vascular dynamics. To capture this structured relationship, we introduce xMAE, a biosignal pretraining framework that leverages masked cross modal reconstruction across temporally ordered biosignals as a training time constraint to encourage physiologically meaningful timing structure in the learned representations. We show that pretraining with xMAE yields representations that outperform both unimodal and multimodal baselines on 15 of 19 downstream tasks, including cardiovascular outcome prediction, abnormal laboratory test detection, sleep staging, and demographic inference, while generalizing across devices, body locations, and acquisition settings. Further analysis suggests that the ECG PPG timing structure is reflected in the learned PPG representations. More broadly, xMAE demonstrates the effectiveness of incorporating temporal structure into multimodal pretraining when signals observe different stages of a shared underlying process. Code is available at this https URL.

---


### 53. [Democratizing the medieval English legal tradition](https://arxiv.org/abs/2605.00977)

**<font color=#1a73e8>作者：</font>** Michael Zhang, Elise Wang, Charlotte Whatley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The record of the beginning of the most widespread legal system in the world is contained in millions of pages of handwritten text. Most of the records of the first centuries of the Anglo-American legal system are hand-written in a highly abbreviated form of medieval Latin which only a few dozen scholars in the world are trained to read. In this interdisciplinary project, we construct a dataset of 4029 lines of text across 193 medieval criminal and civil cases. We then use the dataset to train an open-source end-to-end pipeline for transcribing these manuscripts. We first train standard neural network architectures for line segmentation and handwriting recognition (R-Blla and CNN+LSTM with CTC decoding, respectively) and show that they can already achieve 79% word accuracy, despite the relatively small training set and the challenge of expanding abbreviations. We then demonstrate that simple post-processing significantly boosts accuracy: adding an n-gram language model to the CTC decoder improves word accuracy to 82%, while asking Gemini Pro 3 to correct mistakes boosts accuracy to 88%. Finally, we compare the CNN+LSTM architecture with TrOCR, a transformer-based OCR architecture, demonstrating that TrOCR shows comparable word accuracy but worse character accuracy due to its over-willingness to guess, making it harder for humans to infer the correct reading. We incorporated our pipeline into a web portal (this http URL), opening up the English legal tradition to legal scholars, medievalists, and students.

---


### 54. [AnimationDiff: A Visual Comparison Tool for Generated 3D Character Animations](https://arxiv.org/abs/2605.01001)

**<font color=#1a73e8>作者：</font>** Ludwig Sidenmark, Qian Zhou, George Fitzmaurice 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Creating 3D character animations traditionally requires significant time and effort from the animator. Advancements in generative methods now enable easy creation of multiple character animation variations for use or further editing. However, this capability introduces a new challenge in comparing character animations to select the best animation, which is challenging due to temporal misalignment and the large amount of spatial data. We present AnimationDiff, a visual comparison tool for generated character animations. AnimationDiff enables contextual comparisons in the intended scene and camera angle, and embedding of spatial information by combining established animation visualization techniques and easy switching between overlaid and side-by-side comparisons. AnimationDiff also supports filtering to handle information overload, and Temporal Lenses that visualize entire animations over time for overview, alignment, and comparison. We evaluated AnimationDiff in a user study, showcasing its efficacy in animation comparison and providing design insights for comparing motion.

---


### 55. [Temporal Out-of-Distribution Detection for Asynchronous Motor Imagery Brain-Computer Interfaces](https://arxiv.org/abs/2605.01014)

**<font color=#1a73e8>作者：</font>** Chenhao Liu, Siyang Li, Luofei Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Real online brain--computer interfaces operate on continuous electroencephalography (EEG) streams, where users are usually at rest and enter motor-imagery task states only intermittently. EEG windows may also arise from OOD MI activity outside the predefined control set. Conventional closed-set motor-imagery classifiers tend to assign such inputs to ID classes, which can cause erroneous control. To address this issue, this paper proposes a two-stage EEG detection framework for asynchronous motor-imagery brain--computer interfaces. A sliding-window mechanism continuously monitors EEG signals. The first stage uses an EEGNet-based rest/task gate to determine whether the current window should enter the control-decision process. The second stage performs ID MI classification and out-of-distribution detection only for task-state samples. To improve OOD rejection, we further propose TempDens, which combines classification-output energy, deep-feature density, and temporal-consistency scores to characterize distributional deviation from output, feature, and temporal-dynamic perspectives. Experimental results show that the proposed method effectively supports task-state detection and OOD MI recognition in continuous EEG streams, outperforming multiple conventional OOD baselines. This study reframes online motor-imagery control as a hierarchical decision problem involving continuous monitoring, state discrimination, ID classification, and OOD rejection.

---


### 56. [Continual Learning of Feedback-based Molecular Communication](https://arxiv.org/abs/2605.01020)

**<font color=#1a73e8>作者：</font>** Siddhant Setia, Junichi Suzuki, Tadashi Nakano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes and evaluates a new performance estimation method that leverages continual learning (CL) algorithms to carry out sequential simulation experiments for a feedback-based molecular communication protocol. As the protocol is sequentially examined in various experimental settings, the proposed CL-based performance estimators incrementally learn a series of unexperienced estimation tasks without compromising those that have been learned in the past. They are designed to work on a standard neural network architecture by customizing regularization and replay strategies in the loss function. Experimental results demonstrate that the proposed estimators can effectively learn on a continuous stream of simulation results and enhance the baseline neural network by improving estimation accuracy at a variety of computational costs. This paper's contribution is to establish the implications of CL in the field of molecular communication.

---


### 57. [Effect-Transparent Governance for AI Workflow Architectures: Semantic Preservation, Expressive Minimality, and Decidability Boundaries](https://arxiv.org/abs/2605.01030)

**<font color=#1a73e8>作者：</font>** Alan L. McCann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a machine-checked formalization of structurally governed AI workflow architectures and prove that effect-level governance can be imposed without reducing internal computational expressivity. Using Interaction Trees in Rocq 8.19, we define a governance operator G that mediates all effectful directives, including memory access, external calls, and oracle (LLM) queries. Our development compiles with 0 admitted lemmas and consists of 36 modules, ~12,000 lines of Rocq, and 454 theorems. We establishseven properties: (P1) governed Turing completeness, (P2) governed oracle expressivity, (P3) a decidability boundary in which governance predicates are total and closed under Boolean composition while semantic program properties remain non-trivial and undecidable by governance, (P4) goal preservation for permitted executions, (P5) expressive minimality of primitive capabilities (compute, memory, reasoning, external call, observability), (P6) subsumption asymmetry showing structural governance strictly subsumes content-level filtering, and (P7) semantic transparency: on all executions where governance permits, the governed interpretation is observationally equivalent (modulo governance-only events) to the ungoverned interpretation. Together, these results show that governance and computational expressivity are orthogonal dimensions: governance constrains the effect boundary of programs while remaining semantically transparent to internal computation.

---


### 58. [Algebraic Semantics of Governed Execution: Monoidal Categories, Effect Algebras, and Coterminous Boundaries](https://arxiv.org/abs/2605.01032)

**<font color=#1a73e8>作者：</font>** Alan L. McCann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an algebraic semantics for governed execution in which governance is axiomatized, compositional, and coterminous with expressibility. The framework, mechanized in 32 Rocq modules (~12,000 lines, 454 theorems, 0 admitted), is built on interaction trees and parameterized coinduction. A three-axiom GovernanceAlgebra record (safety, transparency, properness) induces a symmetric monoidal category with verified pentagon, triangle, and hexagon coherence, where every tensor composition preserves governance. An algebraic effect system constrains the handler algebra so that only governance-preserving handlers can be constructed in the safe fragment; programs in the empty capability set provably emit only observability directives. Capability-indexed composition bundles programs with machine-checked capability bounds, and a dual guarantee theorem establishes that within_caps and gov_safe hold simultaneously under all composition operators. The capstone result is the coterminous boundary: within our formal model, every program expressible via the four primitive morphism constructors is governed under interpretation, and every governed program is the image of such a program. Turing completeness is preserved inside governance; unmediated I/O is excluded from the governed fragment. Governance denial is modeled as safe coinductive divergence. The governance algebra is parametric: any system instantiating the three axioms inherits all derived properties, including convergence, compositional closure, and goal preservation. Extracted OCaml runs as a NIF in the BEAM runtime, with property-based testing (70,000+ random inputs, zero disagreements) confirming behavioral equivalence between the specification and the runtime interpreter.

---


### 59. [InterPhys: Physics-aware Human Motion Synthesis in a Dynamic Scene](https://arxiv.org/abs/2605.01036)

**<font color=#1a73e8>作者：</font>** Chaoyue Xing, Wei Mao, Miaomiao Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper tackles the problem of physics-aware human motion synthesis in a dynamic scene. Unlike existing works which mainly tend to generate physically unrealistic motions due to limited contact modeling, typically restricted to hands, in this paper, we introduce a physics-aware human motion generation framework that explicitly models the full spectrum of human-related forces, including human-object, human-scene, and internal body dynamics.~Our method imposes soft physical constraints to maintain force and torque balance, ensuring physically grounded motion synthesis. We further propose a novel continuous distance-based force model that generalizes contact modeling to arbitrary surfaces, capturing interactions not only with static environments but also with dynamic, moving objects. Extensive experiments show that our approach significantly improves physical plausibility and generalizes well to complex scenes, setting a new benchmark for physically consistent human motion generation.

---


### 60. [Certified Purity for Cognitive Workflow Executors: From Static Analysis to Cryptographic Attestation](https://arxiv.org/abs/2605.01037)

**<font color=#1a73e8>作者：</font>** Alan L. McCann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a certified purity architecture that converts governance enforcement in cognitive workflow systems from a runtime convention into a structural capability boundary. A prior three-layer governance architecture proves governance completeness, provenance completeness, and the impossibility of ungoverned effects, conditional on the pure module constraint: that step executors cannot perform effects. That constraint was enforced by module import graph analysis, which is insufficient against adversarial bypass on the BEAM virtual machine. This paper closes the gap through four mechanisms: (1) a restricted WebAssembly compilation target where effect-producing instructions are structurally absent; (2) purity certificates, cryptographically signed proofs binding executor binaries to their import classifications; (3) a runtime verification gate that rejects uncertified executors before they enter the governance pipeline; and (4) portable governance credentials via remote attestation for cross-organizational verification. We prove four theorems: structural purity by construction, bypass elimination for all five BEAM bypass classes, certificate integrity, and gate completeness. The guarantee holds relative to an explicit Trusted Computing Base. Evaluation on four implemented executors shows verification latency of 39--42 us, full plan cycle under 400 us, runtime overhead under 0.4% of a 100 ms HTTP request, and zero determinism divergences across repeated invocations.

---


### 61. [Finite-Sample Analysis of Elimination in Active Hypothesis Testing](https://arxiv.org/abs/2605.01039)

**<font color=#1a73e8>作者：</font>** Ziyuan Lin, Hoang Ngoc Nguyen, Jie Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fixed-confidence, finite-sample problem of active hypothesis testing arises in many safety-critical applications. Situated in the context of sequential hypothesis testing, this paper studies the effect of hypothesis elimination on the stopping time. We introduce an elimination-augmented Track-and-Stop algorithm, in which champion-specific active-opponent sets are progressively pruned, and sensing effort is reallocated toward the surviving alternatives. Our analysis derives a non-asymptotic upper bound on the expected stopping time. The gain in finite-sample from elimination appears on the scale of the non-leading term, resulting from tighter tracking and concentration constants on the reduced hypothesis set. Furthermore, we introduce an aggressiveness parameter to modulate the trade-off between faster elimination and weaker confidence guarantee. An experimental study on synthetic Gaussian instances confirms the theoretical predictions.

---


### 62. [Separation Assurance between Heterogeneous Fleets of Small Unmanned Aerial Systems via Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.01041)

**<font color=#1a73e8>作者：</font>** Iman Sharifi, Hyeong Tae Kim, Maheed Hatem Ahmed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In the envisioned future dense urban airspace, multiple companies will operate heterogeneous fleets of small unmanned aerial systems (sUASs), where each fleet includes several homogeneous aircraft with identical policies and configurations, e.g., equipage, sensing, and communication ranges, making tactical deconfliction highly complex for the aircraft. This paper aims to address two core questions: (1) Can tactical deconfliction policies converge or reach an equilibrium to ensure a conflict-free airspace when companies operate heterogeneous fleets of homogeneous aircraft? (2) If so, will the converged policies discriminate against companies operating sUASs with weaker configurations? We investigate a multi-agent reinforcement learning paradigm in which homogeneous aircraft within heterogeneous fleets operate concurrently to perform package delivery missions over Dallas, Texas, USA. An attention-enhanced Proximal Policy Optimization-based Advantage Actor-Critic (PPOA2C) framework is employed to resolve intra- and inter-fleet conflicts, with each fleet independently training its own policy while preserving privacy. Experimental results show that two fleets with distinct, shared PPOA2C policies can reach an equilibrium to maintain safe separation. While two PPOA2C policies outperform two strong rule-based baselines in terms of conflict resolution, a PPOA2C policy exhibits safer interaction with a rule-based policy, indicating adaptive capabilities of PPOA2C policies. Furthermore, we conducted extensive policy-configuration evaluations, which reveal that equilibria between similar policy types tend to favor fleets with stronger configurations. Even under similar configurations but different policy types, the equilibrium favors one of the heterogeneous policies, underscoring the need for fairness-aware conflict management in heterogeneous sUAS operations.

---


### 63. [Non-Markovian Dynamical Systems Modeling of Electroencephalogram-based Brain Activity for Anticipating the Cognitive Fatigue Level](https://arxiv.org/abs/2605.01043)

**<font color=#1a73e8>作者：</font>** Zeinabsadat Saghi, Daria Riabukhina, Olubukola Akinbami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cognitive fatigue, which transitions from focused attention to inexact responses, can cause catastrophic failures in high-stakes environments, yet current black-box assessment techniques ignore the brain's non-Markovian and time-varying interdependent properties, limiting real-time phase transition detection. We develop a fractional dynamical networks-based machine learning (FDNML) framework using coupled fractional-order differential equations to capture brain signal interdependencies and detect cognitive fatigue transitions in real-time. Multifractal properties of brain activity exhibit distinct generalized fractal dimension signatures across fatigue levels, with Wasserstein distances of 0.10, 0.13, and 0.08 between states 0-1, 1-2, and 0-2, respectively. The framework achieves 93.33% classification accuracy and 95% AUROC, enabling the prevention of performance degradation through early detection of neural state transitions.

---


### 64. [Compared to What? Baselines and Metrics for Counterfactual Prompting](https://arxiv.org/abs/2605.01048)

**<font color=#1a73e8>作者：</font>** Zihao Yang, Mosh Levy, Yoav Goldberg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Counterfactual prompting (i.e., perturbing a single factor and measuring output change) is widely used to evaluate things like LLM bias and CoT faithfulness. But in this work we argue that observed effects cannot be attributed to the targeted factor without accounting for baseline ``meaning-preserving'' modifications to text that establish general model sensitivity. This is because every counterfactual edit is a compound treatment that bundles the variable of interest with incidental surface-form variation; this violates treatment variation irrelevance. We observe prediction flip rates on MedQA of 14.9% when we surgically change patient gender. However, this is statistically indistinguishable from the flip rates induced by simply paraphrasing inputs (14.1%). In this case, it would therefore be unwarranted to conclude that the LLM is especially sensitive to patient gender. To account for this and robustly measure the effects of targeted interventions, we propose a framework in which we compare (via statistical testing) differences observed under target interventions to those induced by paraphrasing inputs. We then use this framework to revisit a analysis done on the MedPerturb dataset, which reported evidence of model sensitivity to patient demographics and stylistic cues. We find that these effects largely dissipate when we account for general model sensitivity, with only 5 of 120 tests reaching statistical significance. Applying the same framework to occupational biography classification, we detect clearly significant directional gender bias, showing that the framework identifies real directional effects even when they are small. We evaluate a range of metrics -- aggregate, per-sample distributional, and regression -- and find that per-sample metrics are dramatically more powerful than aggregate metrics and regression powerfully and uniquely characterizes effect direction and magnitude.

---


### 65. [LEAP: Layer-wise Exit-Aware Pretraining for Efficient Transformer Inference](https://arxiv.org/abs/2605.01058)

**<font color=#1a73e8>作者：</font>** Shashank Kapadia, Deep Naryan Mishra, Sujal Reddy Alugubelli 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Layer-aligned distillation and convergence-based early exit represent two predominant computational efficiency paradigms for transformer inference; yet we establish that they exhibit systematic incompatibility under standard deployment conditions for convergence-based early exit. Distillation objectives that align intermediate student layers to teacher representations suppress the representational convergence that early-exit mechanisms exploit, rendering such mechanisms ineffective on distilled models. We introduce LEAP (Layer-wise Exit-Aware Pretraining), an auxiliary training objective that reconciles this incompatibility. LEAP requires no architectural modifications; it augments standard distillation with a single constraint ensuring intermediate layers approximate final-layer representations. LEAP-MiniLM achieves 1.61$\times$ measured wall-clock speedup (batch=1, NVIDIA L4) at $\theta$=0.95, with 91.9% of samples exiting by layer 7 and 1.80$\times$ theoretical layer reduction, where standard distilled models achieve zero effective speedup. We validate across sentence similarity (STS-B: 0.760 $\pm$ 0.006) and retrieval benchmarks (BEIR), providing operational guidance including latency measurements, decision thresholds, and deployment criteria.

---


### 66. [GEODE: Angle-Adaptive OOD Detection with Universal Scorer Compatibility](https://arxiv.org/abs/2605.01063)

**<font color=#1a73e8>作者：</font>** Bruno Abrahao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outlier Exposure (OE) is among the strongest training-based OOD detectors on standard benchmarks but exhibits scorer-dependent tradeoffs (e.g., strong on MSP, weak on KNN) and requires curated auxiliary data. We show why OE works: its features sit at the same geometric locus as real near-OOD data, with the boundary-adjacent quartile driving nearly all of OE's gain. OE is boundary calibration, not OOD coverage. GEODE (GEOmetry-preserving DEtection) replicates this calibration synthetically through an angle-adaptive norm loss in which targets scale per-sample with cosine similarity to the nearest class mean, preserving feature geometry where boundary structure matters. Four theorems grounded in neural collapse justify the design. GEODE works across all seven standard scorers on CIFAR-10 (near-OOD AUROC 89.0-92.3, far-OOD reaching 93.05; no catastrophic failure on any scorer). Since the OOD regime is unknown at deployment, this is the test that matters. GEODE outperforms vanilla CE at matched epoch counts. Combined with OE, GEODE reaches 95.0 MSP / 94.8 KNN on CIFAR-10 and beats OE on every scorer on CIFAR-100. The gains hold on WRN-28-10 (+4.5 Energy, 3 seeds). Unlike methods that push OOD into the classifier null space (e.g., PFS, 14.38 KNN AUROC, worse than random), GEODE's adaptive target preserves the geometry that distance-based scorers depend on.

---


### 67. [A Systematic Exploration of Text Decomposition and Budget Distribution in Differentially Private Text Obfuscation](https://arxiv.org/abs/2605.01065)

**<font color=#1a73e8>作者：</font>** Stephen Meisenbacher, Angelo Kleinert, Florian Matthes  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The goal of differentially private text obfuscation is to obfuscate, or "perturb", input texts with Differential Privacy (DP) guarantees, such that the private output texts are quantifiably indistinguishable from the originals. While perturbation at the word level is intuitive, meaningful text privatization happens on complete documents. Recent research has laid the groundwork for reasoning about privacy budget distribution, namely, how an overall $\varepsilon$ budget can be sensibly distributed among the component pieces of a text. We perform a systematic evaluation of multiple text decomposition and budget distribution techniques in the context of DP text obfuscation, testing how different methods for chunking texts can be combined with techniques for allocating $\varepsilon$ to these chunks. Our experiments reveal that such design choices are very important, as even with comparable privacy budgets, significantly different results can occur based on which methods are chosen. In this, we provide credible evidence of the feasibility of maximizing empirical trade-offs by optimizing DP obfuscation procedures.

---


### 68. [A dimensional R2 regression metric](https://arxiv.org/abs/2605.01066)

**<font color=#1a73e8>作者：</font>** Jaesung Yoo, Stefan Lemke, Jian Zhong Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> R2 score is the standard metric for evaluating regression tasks, offering a normalized magnitude-agnostic measure of accuracy that captures variance. However, R2 has three key limitations: it is limited to at most two dimensional inputs, it reduces the score to a single scalar that hides rich patterns of prediction accuracy, and it is sensitive to low-variance noise channels which can yield large, uninterpretable negative values. We introduce the Dimensional R2 score (Dim-R2), a simple extension of R2 that accepts data of arbitrary dimensionality, provides a multidimensional view of accuracy, and reduces sensitivity to noise. We demonstrate its advantages on both synthetic sinusoidal data and three multidimensional regression datasets. Dim-R2 offers an interpretable and flexible metric that highlights patterns in regression accuracy, guiding regression modeling.

---


### 69. [Deep Variational Inference Symbolic Regression](https://arxiv.org/abs/2605.01067)

**<font color=#1a73e8>作者：</font>** James Butterworth, Gevik Grigorian, Alejandro DiazDelaO  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression discovers explicit, interpretable equations without assuming a functional form in advance. A Bayesian approach strengthens this through probability distributions over candidate expressions, thus quantifying uncertainty in the presence of noisy and limited data. Deep Symbolic Regression (DSR) uses a neural network to generate symbolic expressions, but it is designed to identify a single best-fitting expression rather than infer a posterior distribution over models. We introduce Deep Variational Inference Symbolic Regression (DVISR), a variational Bayesian extension of DSR. DVISR replaces the original reward with the integrand of the evidence lower bound. It also extends the network architecture to output distributions over constants within expressions, enabling posterior inference over both expression trees and their associated constants. We show that DVISR can recover the true posterior in simple settings, both with and without constant tokens, and we examine how its performance changes as the size of the expression space increases. These results position DVISR as a step toward scalable Bayesian symbolic regression with uncertainty over full symbolic models.

---


### 70. [Controlled Paraphrase Geometry in Sentence Embedding Space: Local Manifold Modeling and Latent Probing](https://arxiv.org/abs/2605.01073)

**<font color=#1a73e8>作者：</font>** Leonid Bedratyuk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The paper studies the local geometry of embedding clouds induced by \emph{controlled local classes of semantically close sentences}. The central question is how controlled paraphrase-like semantic variation is organized in sentence embedding space and whether this local structure can be explicitly modeled by low-degree fitted carriers.
We introduce a local geometric modeling scheme based on affine, quadratic, and cubic fitted models. We also use a surface-based latent probing procedure that constructs synthetic latent points in a reduced local PCA space with respect to the fitted carrier. The procedure is intended as an offline method for representation-space analysis, local manifold modeling, and geometry-aware latent probing.
Generated latent points are evaluated using criteria that measure consistency with the fitted surface, preservation of neighborhood structure, agreement with the empirical distribution, stability of Hessian-based second-order shape descriptors, and stability of fitted-model coefficients. Experiments on controlled sets of semantically close sentences show that nonlinear local models describe embedding clouds more accurately than affine models. Surface-based generation provides strong fitted-geometry fidelity, including surface consistency, Hessian-based shape consistency, and coefficient consistency.
Downstream experiments show that geometric validity of synthetic latent points does not automatically translate into improved classification performance. The results support explicit local geometric modeling of sentence embedding space and highlight the need to distinguish geometric validity from discriminative utility. As a resource contribution, we introduce \textbf{CoPaGE-300K}, a controlled template-based dataset of semantically close sentence variants with slot-level annotations and precomputed sentence embeddings.

---


### 71. [Neighbor2Inverse: Self-Supervised Denoising for Low-Dose Region-of-Interest Phase Contrast CT](https://arxiv.org/abs/2605.01075)

**<font color=#1a73e8>作者：</font>** Johannes B. Thalhammer, Lorenzo D'Amico, Lucy Costello 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Propagation-based X-ray phase-contrast imaging (PBI) enables high-contrast visualization of lung structures and holds strong medical potential. However, safe translation to the clinic will require a substantial radiation dose reduction, which inevitably increases image noise. Supervised convolutional-neural-network-based denoising can restore image quality but depends on paired low- and high-dose datasets, which are rarely available in practice. Self-supervised methods avoid this limitation, yet most are not well adapted to the inverse problem of PBI computed tomography (CT). We introduce Neighbor2Inverse, a self-supervised denoising framework designed for low-dose PBI-CT that generalizes to clinical CT. Building on the Neighbor2Neighbor principle, each noisy projection is subsampled into two variants that preserve structural information but contain independent noise realizations. These are reconstructed separately, and the resulting pairs are used to train a denoising network directly in the image domain. We benchmark the proposed method against established analytical and self-supervised denoising approaches. In region-of-interest PBI CT experiments, Neighbor2Inverse achieves superior noise suppression while preserving fine structural details, as demonstrated by improved contrast-to-noise ratio, spatial resolution, and composite image quality metrics. Competitive performance is also observed on clinical CT data under simulated low-dose conditions.
This work has been submitted to the IEEE for possible publication. Copyright may be transferred without notice, after which this version may no longer be accessible.
Code, data, and interactive figures are available at this https URL.

---


### 72. [A Sentence Relation-Based Approach to Sanitizing Malicious Instructions](https://arxiv.org/abs/2605.01078)

**<font color=#1a73e8>作者：</font>** Soumil Datta, Melissa Umble, Daniel S. Brown 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation and tool-integrated LLM agents increasingly depend on external textual sources. This reliance broadens the available attack surface, allowing adversaries to insert malicious instructions that trigger unintended model behaviors. Current defensive measures often utilize LLM-based detectors to filter such content, but these approaches remain vulnerable to optimization-based attacks. Additionally, training-based methods frequently fail to generalize to novel data distributions. To resolve these issues, we introduce SONAR, a prompt sanitization framework that identifies and removes injected content using metrics from natural language inference. Specifically, SONAR constructs a sentence-level relational graph across the user query and external data. By using entailment and contradiction scores as edge weights, the system identifies sentences that deviate from the core task. It then employs connectivity-driven pruning to eliminate flagged injection seeds and their related neighbors while maintaining benign context. Rigorous evaluations across several models and datasets show that SONAR reduces the attack success rate to nearly zero, significantly outperforming nine established baseline defenses.

---


### 73. [WILD SAM: A Simulated-and-Real Data Augmentation for Autonomous Driving Perception under Challenging Weather](https://arxiv.org/abs/2605.01081)

**<font color=#1a73e8>作者：</font>** Hamed Khatounabadi, Xiaohu Lu, Hayder Radha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The performance of state-of-the-art object detectors degrades significantly under adverse weather, causing a safety-critical domain shift problem for autonomous vehicles. Recent efforts address this problem by relying on synthetic data to train the object detectors, which limits their real-world applicability. Meanwhile, pseudo-labeling is widely used for cross-dataset domain adaptation problems. However, these methods have not been exploited by weather-based domain adaptation approaches due to the noisy nature of such labels generated under harsh weather conditions. In this paper, we propose two new approaches to mitigate this weather-induced domain shift. First, we propose a Weather-Induced pseudo Label Denoising (WILD) framework that filters noisy pseudo labels generated by real data captured under adverse weather conditions. Second, we develop a novel hybrid training methodology, WILD SAM, that exploits both pseudo-label denoising and simulation-based training solutions while using real-data from the target harsh-weather domain. We validate both proposed approaches, WILD and WILD SAM, on the recently released Four Seasons dataset across rainy and snowy scenarios. Experiments show that the proposed frameworks improve Average Precision (AP) up to 13\% and significantly reduce the weather-induced performance gap relative to the baseline. The code is available at: this https URL

---


### 74. [Networked Information Aggregation for Binary Classification](https://arxiv.org/abs/2605.01082)

**<font color=#1a73e8>作者：</font>** MohammadHossein Bateni, Zahra Hadizadeh, MohammadTaghi Hajiaghayi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study networked binary classification on a directed acyclic graph (DAG) where each agent observes only a subset of the feature columns of a shared dataset. Agents act sequentially along the DAG: each receives prediction columns from its parents (if any), augments its local features with these columns, fits a logistic predictor by minimizing binary cross-entropy (BCE), and forwards its prediction column to its outgoing neighbors. We ask whether this sequential distributed training procedure achieves information aggregation, meaning that some agent attains small excess loss compared to the best logistic predictor trained with access to all feature columns.
This question was studied for linear regression under squared loss by Kearns, Roth, and Ryu (SODA 2026). Extending their guarantees to classification is nontrivial because their analysis relies on quadratic structure that does not directly transfer to BCE with a logistic link. We analyze the resulting sequential logit-passing protocol and prove: (i) an excess loss upper bound of $O(M/\sqrt{D})$ on depth-$D$ paths under the condition that every $M$ contiguous subsequence of $M$ agents collectively observe all features, and (ii) a close lower bound showing instances with excess loss of at least $\Omega(k/D)$ where $k$ is the dimension of the feature space. Together, these results identify network depth as a fundamental bottleneck for information aggregation in networked logistic regression.

---


### 75. [Patient-Specific Optimization for Mandibular Reconstruction Planning with Enhanced Bone Union](https://arxiv.org/abs/2605.01084)

**<font color=#1a73e8>作者：</font>** Hamidreza Aftabi, John E. Lloyd, Amanda Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mandibular reconstruction with vascularized bone grafts is complicated by donor-host nonunion, and current virtual surgical planning produces a geometric plan rather than a configuration that explicitly promotes bone union. We present OsteoOpt++, an image-to-decision planning loop for patient-specific mandibular reconstruction. A pre-operative computed tomography (CT) is converted into a personalized digital twin through template-to-patient registration and CT-derived updates of the muscle and temporomandibular-joint parameters. Bayesian optimization with an expected-improvement-plus acquisition rule then searches six clinically controllable cut-plane and donor-positioning variables under an apposition-driven objective and a safety-factor-regularized variant. The workflow was evaluated on three generic defects (body, symphysis, and ramus-body) and a total of 3+1 patient-specific cases, with 3 used for optimization and 1 for validation. In the generic cases, against a common surgical approach, cycle-averaged donor-mandible apposition increased by up to 29 percentage points (329% relative); in the patient-specific cases, against the surgeon-implemented day-5 post-operative configuration, by up to 26 percentage points. A 10% sensitivity analysis over eleven modeling parameters capped the change in the apposition-driven objective at 3% for generic cases and 4% for patient-specific cases, and the longitudinal case showed Dice overlap of 0.70 and 0.76 between predicted apposition and year-1 bone formation. Clinically, this provides surgeons with a pre-operative, image-driven recommendation for cut-plane orientation and donor placement that is predicted to improve union conditions over the configurations currently delivered in the operating room. The optimization and patient-specific modeling code is open source at this https URL.

---


### 76. [Learning Discriminators for Resampling in the Ensemble Gaussian Mixture Filter through a Normalizing Flow Approach](https://arxiv.org/abs/2605.01089)

**<font color=#1a73e8>作者：</font>** Zain Jabbar, Andrey A. Popov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ensemble Gaussian mixture filter (EnGMF) is a powerful, convergent particle filter capable of medium-to-high dimensional non-linear filtering. The EnGMF relies on a resampling step that can generate physically unrealistic posterior samples, that would subsequently produce physically meaningless forecasts. This work introduces the discriminator-informed resampling procedure, that augments the posterior resampling step with a discriminator that accepts or rejects candidate particles based on their physical plausibility. In this work these discriminators are learned through a normalizing flow approach. Numerical experiments on both the Ikeda map and the Lorenz '63 system show that discriminator informed resampling procedure consistently reduces error relative to the standard EnGMF in low-ensemble regimes.

---


### 77. [Learning to Race in Minutes: Infoprop Dyna on the Mini Wheelbot](https://arxiv.org/abs/2605.01096)

**<font color=#1a73e8>作者：</font>** Devdutt Subhasish, Henrik Hose, Sebastian Trimpe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has the potential to enable robots with fast, nonlinear, and unstable dynamics to reach the limits of their performance. However, most recent advances rely on carefully designed physics-based simulators and domain randomization to achieve successful sim-to-real transfer within reasonable wall-clock time. In this work, we bypass the need for such simulators and demonstrate that Infoprop Dyna, a state-of-the-art uncertainty-aware model-based reinforcement learning (MBRL) framework, can enable robots to learn directly from real-world interactions. Using Infoprop Dyna, the Mini Wheelbot, an underactuated unicycle robot, learns to race around a track within 11 minutes of real-world experience.

---


### 78. [Interpretable Difficulty-Aware Knowledge Tracing in Tutor-Student Dialogues](https://arxiv.org/abs/2605.01097)

**<font color=#1a73e8>作者：</font>** Shuyan Huang, Alexander Scarlatos, Jaewook Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have led to the development of AI-powered tutoring systems that provide interactive support via dialogue. To enable these tutoring systems to provide personalized support, it is essential to assess student performance at each turn, motivating knowledge tracing (KT) in dialogue settings. However, existing dialogue-based KT approaches often ignore question difficulty modeling and rely on opaque latent representations from LLMs, hindering accurate and interpretable prediction. In this work, we propose an interpretable difficulty-aware conversational KT framework built upon LLMs, which explicitly models students' abilities and the difficulty of tutor-posed tasks at each turn. The framework incorporates the original textual question and the next tutor-posed task to estimate the student's knowledge state and the difficulty of the upcoming turn. Furthermore, it integrates Item Response Theory to map LLM's outputs into student ability and question difficulty parameters, enabling interpretable prediction of student performance grounded in cognitive theories of learning. We evaluate the framework on two tutor-student dialogue datasets. Both quantitative and qualitative results show that our framework outperforms existing KT baselines, meanwhile generating interpretable outputs consistent with cognitive theory.

---


### 79. [Almost for Free: Crafting Adversarial Examples with Convolutional Image Filters](https://arxiv.org/abs/2605.01098)

**<font color=#1a73e8>作者：</font>** Alexander Warnecke, Konrad Rieck  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial examples in machine learning are typically generated using gradients, obtained either directly through access to the model or approximated via queries to it. In this paper, we propose a much simpler approach to craft adversarial examples, drawing inspiration from insights of explainable machine learning. In particular, we design \emph{adversarial image filters} that are based on classic edge detection algorithms but optimized to deceive learning models. The resulting untargeted attacks are transferable and require only a single pass over the input. Empirically, we find that 3x3 filters already enable success rates between 30% and 80% on different neural networks. Compared to related approaches using generative models for crafting adversarial examples, we reduce the number of parameters by five orders of magnitude, resulting in a very efficient attack. When investigating the parameters of the learned filters, we observe interesting properties such as a high transferability between models and structures common to classic image filters. Our results provide further insights into the vulnerability of neural networks and their fragility to malicious noise.

---


### 80. [Towards Multi-Agent Autonomous Reasoning in Hydrodynamics](https://arxiv.org/abs/2605.01102)

**<font color=#1a73e8>作者：</font>** Jinpai Zhao, Albert Cerrone, Joannes Westerink 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Single-agent systems (SAS) have become the default pattern for LLM-driven scientific workflows, but routing planning, tool use, and synthesis through a single context window comes with a well-known cost: as tool specifications and observational traces accumulate, the effective context available for each decision shrinks, and end-to-end reliability suffers. We present a multi-agent system (MAS) prototype for hydrodynamics in which specialized agents are coordinated through a Layer Execution Graph (LEG). A planner agent constructs query-specific execution topologies from natural-language routing heuristics that capture domain knowledge without hard-coding it as rigid control logic; specialist agents operate under strict tool allowlists and occupy complementary data-class roles. Between layers, consolidator agents fuse parallel outputs into concise briefs, and a reporter agent synthesizes the final response, while the runtime logs provenance for every tool invocation to support auditability. All benchmarks, ablations, and stress tests use Claude Sonnet~4.6 as the backbone model for both specialist and general-purpose agents. Evaluated on 37 queries spanning six complexity categories, the prototype achieves 93.6% factual precision with a 100% pass rate. Accuracy remains above 90% across runs from single-threaded to five independent parallel tracks, and under simulated loss of individual data sources the system degrades gracefully, still returning substantive partial answers. Together, these results suggest that planner-guided, graph-structured multi-agent orchestration can meaningfully alleviate the context-saturation bottlenecks that constrain monolithic single-agent architectures.

---


### 81. [Diffusion Operator Geometry of Feedforward Representations](https://arxiv.org/abs/2605.01107)

**<font color=#1a73e8>作者：</font>** Kanishka Reddy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks transform data through learned representations whose geometry affects separation, contraction, and generalization. Recent work studies this geometry using discrete curvature on neighborhood graphs, suggesting Ricci-flow-like behavior across layers. We develop a smooth operator-theoretic alternative for feedforward representation snapshots. Each feature cloud induces a Gaussian-kernel diffusion Markov operator, and transport, spectral, label-boundary, and local-scale observables are derived from this single object via Bakry-Emery $\Gamma$-calculus. In a balanced Gaussian class-conditional snapshot model with shared covariance, the population operator has closed-form class affinities, leakage, and coarse spectra, all controlled by pairwise regularized Mahalanobis separations $c_\varepsilon^{(a,b)}$. We also prove that the resulting operator observables vary smoothly under feature perturbations, while hard neighborhood-graph diagnostics can change discontinuously. Synthetic experiments validate the closed-form Gaussian bridge, while learned MNIST experiments show that the same operator observables track training, width, and perturbation stability. Together, these results give a stable operator-geometric framework for analyzing feedforward representation geometry.

---


### 82. [What Makes an AI Writing Companion a Good Fit? A Personality-Informed Co-Design Study](https://arxiv.org/abs/2605.01108)

**<font color=#1a73e8>作者：</font>** Mengke Wu, Kexin Quan, Weizi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The growing popularity of AI writing assistants creates exciting opportunities to support diverse writers. This study examines how personality shapes expectations for AI writing companions and how personality-informed design can enhance human-AI teaming in writing. Through exploratory co-design workshops with 24 writers representing different personality profiles, we elicited values and design ideas for AI writing companions spanning functionality, interaction dynamics, and visual representation. These insights informed two contrasting prototypes reflecting distinct writing orientations, used as design provocations in review-and-refinement workshops with eight participants to prompt reflection on fit, priorities, and writing practices. Our findings reveal both shared foundational needs across writers and meaningful personality-driven preferences that influence how writers engage with AI. This work underscores the importance of team matching in human-AI collaboration and demonstrates how aligning AI companions with individual cognitive and interpersonal needs can improve engagement and perceived collaboration effectiveness.

---


### 83. [Topological Neural Tangent Kernel](https://arxiv.org/abs/2605.01110)

**<font color=#1a73e8>作者：</font>** Sanjukta Krishnagopal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural tangent kernels give a principled infinite-width theory for graph neural networks, but inherit a basic limitation of graph models: they see only pairwise structure. Many relational systems contain higher-order interactions that are more naturally represented by simplicial complexes. We introduce the Topological Neural Tangent Kernel (TopoNTK), an infinite-width kernel for simplicial message passing on edge features. TopoNTK combines lower Hodge interactions, capturing graph-like coupling through shared vertices, with upper Hodge interactions, capturing coupling through filled simplices. This makes the kernel sensitive to topology invisible to graph kernels, allowing complexes with the same graph but different filled simplices to induce different kernels. Beyond expressivity, the Hodge structure gives the kernel an interpretable learning geometry. Edge signals decompose into gradient-like, harmonic, and local circulation components, and the spectrum of the TopoNTK determines how quickly each component is learned. This yields a topological form of spectral bias: components aligned with large-eigenvalue modes are learned quickly, while global harmonic modes, retained through the residual channel, often lie at smaller eigenvalues and are learned more slowly. We prove expressivity, Hodge-alignment, spectral learning, and stability properties, and validate them on synthetic simplicial tasks and DBLP higher-order link prediction. The results show that topology is not merely extra structure; it can provide coordinates that make relational learning more faithful, interpretable, and effective.

---


### 84. [When Less is Enough: Efficient Inference via Collaborative Reasoning](https://arxiv.org/abs/2605.01111)

**<font color=#1a73e8>作者：</font>** Yilei Chen, Sharut Gupta, Yannis Paschalidis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce DUET (Dual-model Efficient Two-stage inference), a collaborative inference framework in which a capable model and a lightweight model work together to solve a task. Relying on a single large model to perform end-to-end reasoning and prediction often incurs substantial inference cost. In contrast, DUET decomposes inference into two stages: the capable model produces a reasoning signal, and the lightweight model interprets this signal to generate the final answer, allowing reasoning-intensive computation to be handled by the capable model while non-reasoning-intensive components are delegated to the lightweight model without sacrificing task performance. To achieve this objective, we propose a length-penalized joint training objective that encourages the capable model to transmit only the information that is sufficient for the lightweight model to solve the task. As a result, DUET maintains strong reasoning performance with substantially lower inference cost than end-to-end inference using a large model alone, saving up to 60% of the large model's output tokens on challenging reasoning benchmarks, including AIME and GPQA.

---


### 85. [Disciplined Diffusion: Text-to-Image Diffusion Model against NSFW Generation](https://arxiv.org/abs/2605.01113)

**<font color=#1a73e8>作者：</font>** Chi Zhang, Changjia Zhu, Xiaowen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) diffusion models have the ability to build high-quality pictures from text prompts, but they pose safety concerns because they can generate offensive or disturbing imagery when provided with harmful inputs. Existing safety filters typically rely on text-based classifiers or image-based checkers that completely block the output upon detecting a threat, issuing an explicit allow/block feedback signal to the user. This binary strategy leaves models vulnerable to adversarial attacks that alter keywords to bypass detection, and it causes high false-alarm rates that degrade the experience for benign users. To address such vulnerabilities, we propose Disciplined Diffusion (DDiffusion), a novel robust text-to-image diffusion that counters Not Safe For Work (NSFW) generation by uncovering implicit malicious semantics in prompt embeddings. DDiffusion leverages a semantic retrieval mechanism to evaluate prompts against concept distributions rather than relying on brittle pairwise similarity. Furthermore, it employs a localization method during the diffusion process to selectively edit only the harmful regions of the generated image. By returning locally sanitized images instead of applying uniform blocking, DDiffusion suppresses malicious content while preserving generation fidelity for benign prompts and avoiding the binary allow-deny signal on which existing probing attacks rely.

---


### 86. [Machine Learning-Augmented Acceleration of Iterative Ptychographic Reconstruction](https://arxiv.org/abs/2605.01122)

**<font color=#1a73e8>作者：</font>** Bowen Zheng, Katayun Kamdin, David Shapiro 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative ptychographic reconstruction algorithms are widely used for coherent diffractive imaging but can exhibit slow convergence under realistic experimental conditions. We propose a machine learning-augmented approach that accelerates iterative ptychographic reconstruction by introducing a learned fast-forward operator applied during reconstruction. Following an initial warm-up using standard iterations, the fast-forward operator advances the reconstruction toward a more converged state, after which conventional iterative updates are resumed. This strategy preserves the physical consistency and flexibility of established ptychographic solvers while reducing the number of iterations required for convergence. The model is trained on diverse ptychographic datasets and evaluated on experimental data acquired in a different year, demonstrating robustness and temporal generalization. Compared with conventional iterative solvers, the machine learning-augmented method achieves comparable reconstruction quality while converging faster in terms of Poisson negative log-likelihood, yielding over a two-fold reduction in wall-clock time. The approach has been integrated into an existing reconstruction pipeline and deployed in production at a synchrotron beamline, demonstrating practicality for real-time experimental operation.

---


### 87. [Extreme Weather Bench: A framework and benchmark for evaluation of high-impact weather](https://arxiv.org/abs/2605.01126)

**<font color=#1a73e8>作者：</font>** Amy McGovern, Taylor Mandelbaum, Daniel Rothenberg 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting the wide variety of high-impact weather events experienced globally is a challenge for both Artificial Intelligence (AI) and Numerical Weather Prediction (NWP) models and it is critical that such models be properly verified before deployment. Although AI weather models are rapidly evolving, much of their evaluation is currently done either with a global-scale evaluation or by hand-picking a small number of case studies or a region. A widely-used open-source benchmark suite focusing on high-impact weather will help to drive the science forward for all scales of weather models, as it has for other AI fields. Here we introduce Extreme Weather Bench (EWB), a new community-driven benchmark suite that facilitates model validation and verification on a variety of high-impact hazards that matter to people around the globe. EWB provides a standard set of case studies (spanning across multiple spatial and temporal scales and different parts of the weather spectrum), observational data, impact-based metrics, and open-source code for users to evaluate their models. Verifying that a model works against a standard set of case studies, especially events that are high-impact for the general public, is a key piece of improving the trustworthiness of AI models. EWB will help to drive the science forward for all weather models, enabling true comparisons across models and evaluating models on specific high-impact phenomena through the use of case studies. EWB is a free open-source community-driven system and will continue to evolve to include additional phenomena, test cases and metrics in collaboration with the worldwide weather and forecast verification community.

---


### 88. [Revisiting Privacy Leakage in Machine Unlearning: Membership Inference Beyond the Forgotten Set](https://arxiv.org/abs/2605.01129)

**<font color=#1a73e8>作者：</font>** Jie Fu, Nima Naderloui, Da Zhong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine unlearning (MU) has emerged as a key mechanism for ensuring data privacy and regulatory compliance by enabling models to forget specific training samples. However, recent studies have shown that the removal of data can inadvertently introduce privacy leakages to the retain set,i.e., data that remain in the model after unlearning. In this paper, we extend the scope of privacy analysis in unlearning to the often-overlooked retained data. We introduce TC-UMIA, the first tri-class unlearning membership inference attack. TC-UMIA is a population-level inference framework that leverages model predictions before and after unlearning to distinguish among the forget, retain, and unseen set. Extensive experiments on five state-of-the-art unlearning algorithms and six real-world datasets demonstrate that: (i) unlearning can introduce additional privacy risks to the retain set, making it more susceptible to membership inference attacks; (ii) TC-UMIA is effective across a wide range of model architectures, datasets, and MU approaches. Beyond launching the attack, we rigorously evaluate three defense mechanisms, namely label-only outputs, dropout, and differential privacy, to mitigate the privacy risks posed by TC- UMIA. Our results reveal a fundamental trade-off between privacy protection and model accuracy, with the dropout approach offering the most favorable balance.

---


### 89. [Iterative Finetuning is Mostly Idempotent](https://arxiv.org/abs/2605.01130)

**<font color=#1a73e8>作者：</font>** Zephaniah Roe, Jack Sanderson, Dang Nguyen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> If a model has some behavioral tendency, such as sycophancy or misalignment, and it is trained on its own outputs, will the tendency be amplified in the next generation of models? We study this question by training a series of models where each model is finetuned on data generated by its predecessor, and the initial model is seeded with some persona or belief. We test three settings: supervised finetuning (SFT) on instruct models, synthetic document finetuning (SDF) on base models, and direct preference optimization (DPO). In the SFT and SDF settings, traits mostly decay or remain constant so that further finetuning cycles do nothing. In rare cases when amplification occurs, it generally comes at the cost of coherence. In the DPO setting, trait amplification can reliably occur when a model is continually trained with a preference for its own outputs, but vanishes when models are reinitialized at each cycle. Overall, our results suggest that amplification most likely comes from continual post-training, and limiting this stage may be an effective defense. For non-RL finetuning, trait amplification is rare and very sensitive to data quantity, making it significantly less likely to occur accidentally. Finally, the amplification-coherence tradeoff serves as a natural deterrent against trait amplification.

---


### 90. [To Use AI as Dice of Possibilities with Timing Computation](https://arxiv.org/abs/2605.01134)

**<font color=#1a73e8>作者：</font>** Jia Li, Vipin Kumar, Rui Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The dominant noun-based modeling paradigm has fundamentally constrained AI development, precluding any adequate representation of the future as an open temporal dimension. This paper introduces a verb-based paradigm, together with precise definitions of \emph{timing computation} and \emph{possibility}, that enables AI to function as an effective instrument for realizing the grammar of our thought.
Applied to longitudinal EHR data from 3,276 breast cancer patients, the framework empirically demonstrates: (1) automatic discovery of clinically significant patient trajectories, and (2) counterfactual timing deduction. Both results are purely data-driven, require no prior domain knowledge, and, to our knowledge, represent the first such demonstrations in the machine learning literature.

---


### 91. [ScribbleEdit: Synthetic Data for Image Editing with Scribbles and Text](https://arxiv.org/abs/2605.01135)

**<font color=#1a73e8>作者：</font>** Anya Ji, George Ma, Téa Wright 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in generative models has significantly advanced image editing capabilities, yet precise and intuitive user control remains difficult. Specifically, users often struggle to communicate both exact spatial layouts and specific semantic details simultaneously. While natural language instructions effectively convey high-level semantics like texture and color, they lack spatial specificity. Conversely, freehand scribbles provide rough spatial boundaries but cannot express detailed visual attributes. Consequently, achieving precise control requires combining both modalities. However, existing models struggle to jointly interpret abstract scribbles alongside text due to a lack of specialized training data.
In this work, we introduce ScribbleEdit, a large-scale synthetic dataset designed to bridge this gap by combining natural language instructions with freehand scribble inputs for more accurate, controllable edits. We construct this dataset through a synthetic pipeline that automatically generates source-target image pairs via inpainting, which are then paired with human-drawn scribbles and VLM-generated text instructions. Using ScribbleEdit, we evaluate and finetune both diffusion-based and autoregressive unified multimodal image editing models. Our experiments reveal that while off-the-shelf models struggle with abstract scribble inputs, finetuning on our synthetic dataset significantly improves their ability to generate spatially aligned and semantically consistent edits.

---


### 92. [Spectral Graph Sparsification Preserves Representation Geometry in Graph Neural Networks](https://arxiv.org/abs/2605.01136)

**<font color=#1a73e8>作者：</font>** Sanjukta Krishnagopal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectral graph sparsification is a classical tool for reducing graph complexity while preserving Laplacian quadratic forms. In graph neural networks (GNNs), sparsification is often used to accelerate computation while maintaining predictive performance. In this work, we study a complementary representation-level question: does sparsification preserve the geometry of learned embeddings?
For polynomial-filter GNNs, we prove that any $\epsilon$-spectral sparsifier induces $O(\epsilon)$ perturbations in polynomial graph filters, multilayer hidden representations, and their Gram matrices. These guarantees imply stability of squared pairwise distances, class means, and covariance structure in embedding space. We further establish finite-time training stability: under smoothness and boundedness assumptions, gradient descent on dense and sparsified graphs produces weight trajectories whose separation grows at most proportionally to the sparsification distortion.
Empirically, effective-resistance sparsification validates the predicted perturbation chain on synthetic graphs and preserves hidden representation geometry on real datasets. In our experiments, the gram matrix and training dynamics show low divergence even under substantial sparsification, consistent with the predicted stability under spectral sparsification. Hidden Gram preservation strongly predicts neighborhood preservation and class-centroid stability across FashionMNIST, Cora, and Paul15. Together, these results show that spectral sparsification preserves not only graph operators, but also the representation geometry that supports downstream use of GNN embeddings for interpretability.

---


### 93. [Metric-Normalized Posterior Leakage (mPL): Attacker-Aligned Privacy for Joint Consumption](https://arxiv.org/abs/2605.01137)

**<font color=#1a73e8>作者：</font>** Gaoyi Chen, Minghao Li, Weishi Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Metric differential privacy (mDP) strengthens local differential privacy (LDP) by scaling noise to semantic distance, but many machine learning (ML) systems are consumed under joint observation, where model-agnostic, per-record guarantees can miss leakage from evidence aggregation. We introduce metric-normalized posterior leakage (mPL), an attacker-aligned, distance-calibrated measure of posterior-odds shift induced by releases, and show that for single or independent releases, uniformly bounding mPL is equivalent to mDP. Under joint observation, however, satisfying mDP may still leave mPL high because learned aggregators compound evidence across correlated items. To make control practical, we formalize probabilistically bounded mPL (PBmPL), which limits how often mPL may exceed a target budget, and we operationalize it via Adaptive mPL (AmPL), a trust-and-verify framework that perturbs, audits with a learned attacker, and adapts parameters (with optional Bayesian remapping) to balance privacy and utility. In a word-embedding case study, neural adversaries violate mPL under joint consumption despite per-record mDP perturbations, whereas AmPL substantially lowers the frequency of such violations with low utility loss, indicating PBmPL as a practical, certifiable protection for joint-consumption settings.

---


### 94. [Toward a Unified Framework for Collaborative Design of Human-AI Interaction](https://arxiv.org/abs/2605.01153)

**<font color=#1a73e8>作者：</font>** Ankur Bhatt, Sven Mayer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human computer interaction is shifting from screen-based systems to multimodal interfaces where artificial intelligence powered systems increasingly interpret user intent through speech, gesture, and gaze. Yet users rarely understand how these interpretations are made, compromising trust and control. Existing approaches treat multimodal alignment, explainability, and human agency as separate concerns, leaving critical gaps in transparency and user oversight. We propose a Human Artificial Intelligence collaboration framework integrating these three principles as interdependent design requirements: 1) multimodal alignment for accurate intent interpretation, 2) interaction centric explainability delivering real time visual, textual, and audio feedback, and 3) agency preserving mechanisms enabling users to accept, reject, or modify artificial intelligence suggestions at any time. We presented the framework through two scenarios, collaborative design and extended reality warehouse robot collaboration, chosen to span differences in time pressure and error reversibility, with the latter situated in a domain where misinterpretation carries documented safety consequences. This approach reframes collaboration as a continuous interaction property, benefiting designers, researchers, and end users by ensuring that as artificial intelligence systems grow more proactive, user understanding and control remain first class design properties.

---


### 95. [Multi-Perspective Transformers in ARC-AGI-2 Challenge](https://arxiv.org/abs/2605.01154)

**<font color=#1a73e8>作者：</font>** Caleb Talley, Vedant Tibrewal, Seun Adekunle 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ARC-AGI-2 is a benchmark of human-intuitive visual puzzles that measures a machine's ability to generalize from limited examples, interpret symbolic meaning, and flexibly apply rules in varying contexts. In this paper, we discuss our approach to solving the ARC-AGI-2 puzzles with TinyLM, with additional fine-tuning at test time, including Test-Time-Training (TTT) and Products of Experts (POE). Our model achieves 96.1% accuracy on the training set and 21.7% accuracy on the evaluation set.

---


### 96. [CEZSAR: A Contrastive Embedding Method for Zero-Shot Action Recognition](https://arxiv.org/abs/2605.01165)

**<font color=#1a73e8>作者：</font>** Valter Estevam, Rayson Laroca, Helio Pedrini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a novel Zero-Shot Action Recognition~(ZSAR) method based on contrastive learning. In ZSAR, we aim to classify examples from classes that were missing during training. Two well-known problems remain in ZSAR: the semantic gap and the domain shift. A semantic gap occurs because label representations come from the textual domain (i.e., language models) and must be associated with visual representations (i.e., CNNs, RNNs, transformer-based). This multimodal nature implies that the semantic properties of the two spaces are not identical. On the other hand, the domain shift arises from differences between the training and test sets and is inherent to ZSAR once the test set is unknown. One of the most promising methods to address both issues is learning joint embedding spaces. Therefore, we propose a new model that encodes videos and sentences in a joint embedding space, trained by aligning videos with their natural-language descriptions. We design an automatic negative sampling procedure to augment the training dataset and generate unpaired data, i.e., visual appearance and unrelated descriptions. Our results are state-of-the-art on the UCF-101 and Kinetics-400 datasets under several split configurations. Our code is available at this https URL.

---


### 97. [Quantifying and Predicting Disagreement in Graded Human Ratings](https://arxiv.org/abs/2605.01168)

**<font color=#1a73e8>作者：</font>** Leixin Zhang, Çağrı Çöltekin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> It is increasingly recognized that human annotators do not always agree, and such disagreement is inherent in many annotation tasks. However, not all instances in a given task elicit the same degree of opinion divergence. In this paper, we investigate annotation variation patterns in graded human ratings for inappropriate languages, including offensive language, hate speech, and toxic language perception. We examine whether the degree of annotation disagreement can be predicted from textual features. We further propose the Opposition Index, a metric that quantifies perspective opposition among annotators on a given item, and investigate the predictability of instances with potentially opposing human opinions. Our results show a moderate positive correlation between estimated and observed annotation variance. We find that two approaches achieve comparable performance in variance prediction: directly predicting the variance value and estimating it from predicted annotation distributions. Our results on opposition perspective prediction show that items with high opposition index values are more difficult to predict and are often underestimated by models.

---


### 98. [CADFit: Precise Mesh-to-CAD Program Generation with Hybrid Optimization](https://arxiv.org/abs/2605.01171)

**<font color=#1a73e8>作者：</font>** Ghadi Nehme, Eamon Whalen, Faez Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent progress, recovering parametric CAD construction sequences from geometric input, such as meshes or point clouds, is a key challenge for design and manufacturing, as existing CAD reconstruction and generation methods are largely restricted to difficult-to-edit formats like meshes or Breps or editable simple sketch-and-extrude pipelines and low-complexity datasets. We introduce CADFit, a hybrid optimization-based CAD reconstruction framework that recovers complex, editable CAD construction sequences from meshes by incrementally fitting and validating parametric operations using geometric feedback. Our approach is distinguished by formulating reconstruction as an IoU-driven optimization over structured CAD programs and supporting a rich set of operations, including extrusions, revolutions, fillets, and chamfers. Experiments on multiple CAD benchmarks show that CADFit outperforms state-of-the-art mesh-to-CAD methods in volumetric Intersection-over-Union and Chamfer Distance, while substantially reducing the Invalid Ratio of reconstructed CAD programs, particularly for complex designs. We further present a multimodal pipeline that enables end-to-end reconstruction of CAD construction sequences from images by combining image-based geometry reconstruction with CADFit. By enabling accurate reconstruction of higher-complexity CAD models, CADFit provides a practical foundation for generating richer datasets and advancing future learning-based approaches to CAD reverse engineering.

---


### 99. [A Theory of Generalization in Deep Learning](https://arxiv.org/abs/2605.01172)

**<font color=#1a73e8>作者：</font>** Elon Litman, Gabe Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a non-asymptotic theory of generalization in deep learning where the empirical neural tangent kernel partitions the output space. In directions corresponding to signal, error dissipates rapidly; in the vast orthogonal dimensions corresponding to noise, the kernel's near-zero eigenvalues trap residual error in a test-invisible reservoir. Within the signal channel, minibatch SGD ensures that coherent population signal accumulates via fast linear drift, while idiosyncratic memorization is suppressed into a slow, diffusive random walk. We prove generalization survives even when the kernel evolves $\mathcal{O}(1)$ in operator norm, the full feature-learning regime. This theory naturally explains disparate phenomena in deep learning theory, such as benign overfitting, double descent, implicit bias, and grokking. Lastly, we derive an exact population-risk objective from a single training run with no validation data, for any architecture, loss, or optimizer, and prove that it measures precisely the noise in the signal channel. This objective reduces in practice to an SNR preconditioner on top of Adam, adding one state vector at no extra cost; it accelerates grokking by $5 \times$, suppresses memorization in PINNs and implicit neural representations, and improves DPO fine-tuning under noisy preferences while staying $3 \times$ closer to the reference policy.

---


### 100. [Phase-map synthesis from magnitude-only MR images using conditional score-based diffusion models with application in training of accelerated MRI reconstruction models](https://arxiv.org/abs/2605.01185)

**<font color=#1a73e8>作者：</font>** M. Berk Sahin, Dilek Yalcinkaya, Abolfazl Hashemi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accelerated magnetic resonance imaging (MRI) enabled by the training of deep learning (DL)-based image recon. models requires large and diverse raw k-space datasets. In most clinical MRI applications, due to storage and patient privacy concerns, raw k-space data is discarded and magnitude-only images are the only component saved. Consequently, a large portion of the DL-based MRI recon. literature has either relied on small training datasets or has used one of the few available open-source k-space datasets. At the same time, the growing number of anonymized magnitude-only image registries/databases motivates the development of techniques that can use them as training datasets for generalizable DL-based recon. models. Here we propose to address this challenge by employing a generative approach based on conditional score-based diffusion models (SBDMs): given a magnitude-only MR image, it synthesizes a phase map (in the image domain) that realistically corresponds to the magnitude-only image. We evaluate its generative capabilities in a downstream DL-based recon. task whereby a large k-space dataset is generated by combining the SBDM-synthesized phase-maps and the corresponding magnitude-only images, and this k-space dataset is then used to train a DL model for accelerated MRI recon. We compare the performance of the resulting DL model versus those trained according to (a) a naive approach that uses smooth phase, (b) a k-space training dataset generated using synthesized phase maps derived from a generative adversarial network, and (c) the ground truth k-space data. Our results suggest that the DL model trained from SBDM-synthesized k-space data outperforms the other approaches in terms of quantitative metrics as well as qualitatively observed recon. fidelity, i.e., whether the reconstructed images include erroneous or hallucinated features that could adversely impact diagnostic accuracy.

---


> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
