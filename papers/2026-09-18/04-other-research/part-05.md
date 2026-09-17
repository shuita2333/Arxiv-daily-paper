# 📦 其他研究 | 2026年09月18日

> 本类共 **223** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-223**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-223**

---

### 201. [KDTwin: Task-Aware Knowledge Distillation for Lightweight Multi-Task Driving Scene Segmentation](https://arxiv.org/abs/2609.18955)

**<font color=#1a73e8>作者：</font>** Huy Che, Minh-Khoi Do, Dinh-Duy Phan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient perception models are essential for real-time autonomous driving, where accuracy and computational cost must be carefully balanced. However, applying knowledge distillation to multi-task driving scene segmentation is challenging because drivable-area and lane segmentation exhibit different spatial characteristics and class imbalance. We propose KDTwin, a task-aware distillation framework for lightweight multi-task segmentation networks. The proposed method performs distillation at both the shared encoder and task-specific decoders. Encoder-level pairwise distillation transfers spatial relational knowledge to enhance the student's shared representation. For the decoders, we use a weighted loss for drivable-area segmentation and a boundary-aware loss for lane segmentation, enabling task-adaptive knowledge transfer without increasing inference complexity. Experiments on BDD100K show consistent improvements across the evaluated CNN-based and Transformer-based student models without increasing inference-time parameters or FLOPs. The results show that designing distillation objectives according to task-specific characteristics can effectively enhance multi-task segmentation performance for autonomous driving. The source code is available at this https URL.

---


### 202. [MechSparse: Mechanism-Guided Sparse PEFT Selection Is Task-Shaped](https://arxiv.org/abs/2609.18961)

**<font color=#1a73e8>作者：</font>** Son Ha Xuan, Phat T. Tran-Truong, Xuan-Bach Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability identifies sparse subsets of heads and MLP blocks that carry specific behaviors. We ask whether such causal signals can guide where to place a small PEFT budget more effectively than the cheap heuristics practitioners already use. \method{} scores attention heads and MLP blocks by normalized activation-patching recovery on clean/corrupted probes and trains LoRA/QLoRA only on the selected sites; \methodc{} adds bounded credit for small within-layer joint subsets.
We compare against random, magnitude, activation-norm, and gradient/Fisher on Ministral-8B/NF4 in three cells: Swahili span-JSON information extraction (IE) at $b{=}0.25\%$ and $1.0\%$, and English$\to$Swahili machine translation (MT) at $b{=}1.0\%$. The causal selectors never win the primary metric. On the headline IE cell (3 seeds, paired-bootstrap CIs over $600$ predictions), \methodc{} beats random by $+0.079$ span+type F1 and gradient/Fisher by $+0.174$, but trails activation-norm by $0.028$, with the smallest cross-seed std ($\pm 0.003$). On MT all four selectors lie within $0.30$ BLEU and every paired CI includes zero. A schema-versus-span decomposition explains the IE gap: activation-norm captures the rigid JSON routine, while causal scores track content-sensitive sites. We distill a preliminary diagnostic -- prefer activation-norm when output structure dominates, treat causal selectors as a hypothesis for content-dominated tasks -- and release masks, scores, predictions, and evaluation files for direct replay.

---


### 203. [The Automaton Underneath: The Additive Input Pathway Is a Parasitic Attractor for State Tracking in Householder Linear RNN](https://arxiv.org/abs/2609.18966)

**<font color=#1a73e8>作者：</font>** Gunner Levi Howe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear RNNs with input-dependent Householder-product transitions (DeltaNet/DeltaProduct-class) can provably represent hard state-tracking automata, yet trained models fail to length-generalize -- a gap recent work attributes to optimization, without a causal account. We give one, in a pre-registered, within-architecture causal ablation: the same model with one term deleted -- the additive input injection $b_t = W_b e_t$. With $b_t$, models fit length 32 and collapse out-of-distribution on parity, $S_4$, $A_5$, and non-solvable $S_5$ word problems (0.20 at position 512 on $S_5$). Without it -- input acting only through the orthogonal transitions -- the same architecture learns the exact automaton: median accuracy 1.00 at 16x the training length, at every width admitted by a representation law we state and test: the minimal number of Householder factors per token equals the maximal reflection length of the task's generators in the format-pinned representation (parity 1, $S_4$ 3, $A_5$ and $S_5$ 4); below it, nothing fits. The contrast with DeltaProduct's $S_4$/$A_5$ at $n_h{=}2$ (group-element classification, $SO(3)$ realization) shows the law is representation-relative: task format is a hidden variable in state-tracking benchmarks. Two pre-registered arms locate the mechanism. (i) Initialized at a verified-exact solution with $W_b{=}0$, Adam grows the additive path and pulls the model off the exact solution; $-b$ controls stay at 1.00. (ii) Our registered prediction that the fit routes through $b_t$ fired its kill criterion: all 49 fitting seeds retain in-domain fit under $W_b{:=}0$ -- and at law-minimal width, zeroing $W_b$ at inference restores exact generalization (parity 5/5, $S_5$ 5/5, $S_4$ 4/5, $A_5$ 4/5). The additive pathway is parasitic: it destabilizes, then conceals, a correctly learned automaton. All 202 runs pre-registered; all numbers regenerate from artifacts.

---


### 204. [A Benchmark Suite and Ground-Truth Methodology for Formal Verification of IEC 61131-3 Ladder Diagram Programs](https://arxiv.org/abs/2609.18994)

**<font color=#1a73e8>作者：</font>** Pierre Dantas, Lucas Cordeiro, Waldir Junior  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the first benchmark suite for formal verification of Programmable Logic Controller (PLC) programs that combines controlled ground truth with coverage of both textual (Structured Text, ST) and graphical (Ladder Diagram, LD) IEC 61131-3 encodings. Despite growing support for tools, the field lacks standard evaluation benchmarks: existing corpora omit formal properties or graphical dialects, and private program sets preclude reproducible measurement of progress. Our suite comprises 50 programs in 83 variants across ten industrial domains, provided in PLCopen Extensible Markup Language (XML) and ST, each paired with a formal property, machine-checkable expected verdict, and violation witness in the Software Verification Competition (SV-COMP) format. The central methodological contribution is a tripartite ground-truth discipline - verdicts are established by construction, fault injection, or audited cross-tool consensus - motivated by a concrete failure mode where the obvious safety property misclassifies all attacks from two public logic-bomb corpora as safe due to invisible non-termination. Reference verdicts are obtained with the Efficient SMT-Based Context-Bounded Model Checker (ESBMC) v8.4 from source: all 25 graphical benchmarks execute, and 43 of 45 accepted variants match recorded verdicts. On the finite-state fragment (21 benchmarks), nuXmv - a model checker with unrelated decision procedures - agrees on all 24 interlock variants and resolves two benchmarks ESBMC-PLC leaves unknown, confirming tool-neutral ground truth and discriminative power. Porting exposes format and semantics fragmentation: front-ends accept different serializations, and timer semantics vary across tools - phenomena the suite is designed to reveal. The corpus, schema, validator, and recheck harness are released as open artifacts.

---


### 205. [Tabular Deep Learning vs Classical Machine Learning for Urban Land Cover Classification](https://arxiv.org/abs/2609.19010)

**<font color=#1a73e8>作者：</font>** Muntasir Tabasum, Tanpia Tasnim, Md. Ekramul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban Land Cover (ULC) classification plays a crucial role in urban planning, environmental monitoring, and sustainable development. We study this task using the ULC dataset from the UCI Machine Learning Repository, which includes tabular features derived from high-resolution aerial imagery across nine classes (e.g., roads, trees, grass, water). The dataset presents typical remote sensing challenges, including high dimensionality, heterogeneous features, and class imbalance. In a unified, reproducible pipeline, we benchmark classical machine learning models (e.g., Logistic Regression, SVM, Random Forest, XGBoost, CatBoost) against Tabular Deep Learning (TDL) models (TabNet, FT-Transformer, TabTransformer, TabSeq, and 1D CNNs). To address class imbalance, we employ weighted cross-entropy loss for TDL models and evaluate performance using accuracy, macro-precision, macro-recall, macro-F1, AUC-ROC, and confusion matrices. Our results show that while tree ensembles remain strong general baselines, TDL models can match or exceed their performance when non-linear interactions are significant and imbalance handling is effective, providing complementary advantages for urban land cover mapping. See code: this https URL

---


### 206. [TwinMark: A Unified Watermark for Provable Survival Under Feature and Logit Distillation](https://arxiv.org/abs/2609.19011)

**<font color=#1a73e8>作者：</font>** Redwanul Karim, Tobias Feigl, Christopher Mutschler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose TwinMark, a watermarking scheme that reads a single SHAKE128 secret through two complementary linear functionals of model-output summaries: a covariance projector against the carrier-set covariance (cov-Feat) and a class-conditional Fisher-aligned linear carrier decoded from class-mean logits (cc-FALC). The two readouts share one bit vector and cover the two extraction surfaces of a deployed vision model: a classifier API attacked by KL knowledge distillation (KD) (Std. KL-KD), and a representation-only host attacked by feature-matching KD (FM-KD). Each readout admits a teacher-measurable a posteriori certificate that lower-bounds post-distillation detection power, and the two channels combine under a regime-restricted OR rule whose test statistic (calibrated null or bit vote) is selected by the exposed surface. cov-Feat admits a rank-blind operator-norm certificate, cc-FALC admits a centered-logit-gap certificate that decouples bit capacity from class count: at K=1024 in m=100 classes (a 10.24x over-encoding), the bit-vote attains z=23.0 sigma at a teacher-accuracy cost of +0.9+-0.2%p. Across 13 attacks on CIFAR-10, CIFAR-100, and Mini-ImageNet, TwinMark verifies on every cell whose post-attack model retains task utility, survives cross-architecture distillation onto ResNet-18/50, VGG-16, and MobileNet-V3, and ports to GNSS few-shot, VOC detection, ISIC segmentation, and STL-10 SimCLR.

---


### 207. [Context-Aware Operational Security for Autonomous Drones](https://arxiv.org/abs/2609.19021)

**<font color=#1a73e8>作者：</font>** Burak Tufekci, Cihan Tunc  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous drone-based services have been gaining significant interest across various application domains due to their mobility, flexibility, cost-effectiveness, and capability to integrate various sensors and actuators. However, operational failures or cyberattacks targeting drone systems can lead to severe economic impacts and safety concerns. Hence, ensuring secure and reliable autonomous drone operations is essential for the safe deployment of drone-enabled services. Nevertheless, the traditional security measures fall short due to drones' limited computational resources and power budget (battery), as well as the temporal and sequential behavior of drone operations due to drones' mobile nature. In this paper, we address this gap by utilizing Recurrent Neural Networks (RNNs), specifically focusing on Long Short-Term Memory (LSTM) networks, for autonomous drone operation security and reliability due to their temporal and sequential analysis capabilities. We leverage these capabilities for anomaly detection in autonomous drone sensor data and operation commands, which we refer to as Denial of Usage Detection Engine IDS (DUDE-IDS). We integrated the proposed DUDE-IDS into the drone mission computer (i.e., operating directly on drones rather than an edge node or ground control stations) to monitor data flows and to detect potential threats in real-time. Extensive experimental results demonstrate the effectiveness of this approach in identifying anomalies associated with GPS spoofing, Man-in-the-Middle (MITM), replay, and Denial-of-Service (DoS) attacks with 98% accuracy. We also evaluate our resource utilization and power consumption under different configurations, demonstrating the applicability of our approach in active drone operations in real-time.

---


### 208. [Structural Decomposability of Encrypted Traffic Side-Channel Leakage](https://arxiv.org/abs/2609.19036)

**<font color=#1a73e8>作者：</font>** Guangjie Liu, Guang Cheng, Weiwei Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing side-channel theories treat leakage as a holistic quantity $I(X;Y)$, without characterizing its internal structure. This paper studies the \emph{structural decomposability} of encrypted-traffic side-channel leakage. Via the structural causal model $X\!\to\!Y_{\mathrm{size}}\!\to\!Y_{\mathrm{dir}}\!\to\!Y_{\mathrm{time}}$ and the mutual-information chain rule, total leakage is decomposed into three sequential increments for packet size, direction, and timing. Defenses are formalized as mechanism replacement by a strategy variable~$D$; coupling information $C_{\mathrm{size,dir}}=I(Y_{\mathrm{size}};Y_{\mathrm{dir}}\!\mid\!X)$ measures inter-dimensional dependence, and the Markov residual gives a testable condition for a single-dimension defense to sever downstream leakage. Causal efficacy~$\eta_d$ quantifies per-unit-cost suppression, and a Fisher-geometric approximation $I(X;Y)\approx\frac{1}{2\ln 2}\mathrm{Tr}(G\Sigma_\theta)$ holds under small perturbations. On the Wang dataset (95 websites), $Y_{\mathrm{dir}}$ dominates undefended leakage (0.637\,bits), while Tor's fixed 512-byte cells make $Y_{\mathrm{size}}$ degenerate; FRONT suppresses the direction term by 63\%, yet its Markov residual of 0.021\,bits (95\% CI $[0.016,0.027]$) shows it cannot sever timing leakage; $\eta_{\mathrm{dir}}=0.97$ vs. $\eta_{\mathrm{time}}\approx 0$ confirms FRONT's design intent. This yields a computable, structured leakage-accounting method for multi-dimensional joint defense design.

---


### 209. [Integrated Optimization of Automated Warehouse Operations and Last-Mile Transport for Differentiated On-Demand Delivery](https://arxiv.org/abs/2609.19048)

**<font color=#1a73e8>作者：</font>** Xiaozhu Sun, Bilal Farooq  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the context of differentiated on-demand goods delivery services, this study proposes an integrated optimization method for automated guided vehicles (AGVs) based smart warehouse operations and the last-mile multi-modal transport. A deep reinforcement learning algorithm for multi-objective joint scheduling is designed to establish a dynamic connection between two systems, solving key challenges such as achieving high-throughput continuous order scheduling, meeting competing requirements, and improving the overall system sensitivity and adaptability. For warehouse optimization within this framework, we propose an improved algorithm based on multi-objective, Multi-Reward Machines-A* Guided Deep Q-Network (MORM-AGDQN), which combines service level, system cost, and external transportation demand. For external optimization, we propose an improved algorithm based on a Multi-Reward, Multi Head attention-Heterogeneous Capacity Vehicle Routing Problem (MRMH-HCVRP) framework, which incorporates the optimized scheduling order sequence and grouping, combined with customer location, demand, and priority, vehicle capacity, speed, and service range. The results show that the proposed framework significantly outperforms traditional methods, achieving 100% on-time delivery rate for warehousing operations. After joint optimization, the average delivery time for the last mile was reduced by 29.3% to 53.2%, the total transportation distance was reduced by 46.4%, the high-priority service rate was increased to over 92%, and a balance was maintained between operating costs and customer satisfaction.

---


### 210. [LightSleepX: A Lightweight, Inception-Based Dual-Modal Network for Sleep Staging](https://arxiv.org/abs/2609.19062)

**<font color=#1a73e8>作者：</font>** Yi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic sleep staging is fundamental to personal health monitoring, yet many existing approaches are ill-suited for real-world applications. Traditional pipelines often rely on hand-crafted features or shallow machine learning models that struggle to generalize, while state-of-the-art deep learning methods, though accurate, are computationally heavy and impractical for resource-constrained environments. This paper introduces LightSleepX, a lightweight framework designed to deliver robust sleep analysis in resource-constrained environments. LightSleepX combines an Inception-style architecture with depthwise separable convolutions and Multi-scale Enhanced Attention for efficient multi-modal EEG/EOG feature extraction, and a Mamba encoder for rule-free long-range temporal modeling. On public benchmark datasets, LightSleepX achieves 85.9% accuracy and a 0.803 macro-F1 score on Sleep-EDF-20, and 81.8% accuracy and a 0.796 macro-F1 score on the cross-subject ISRUC-S3 dataset. With 0.049M parameters and 195.9 MFLOPs, the framework targets practical local deployment where computational cost and privacy are central constraints.

---


### 211. [RLLBC-Lib: An Educational Code Library for Reinforcement Learning and Learning-Based Control](https://arxiv.org/abs/2609.19074)

**<font color=#1a73e8>作者：</font>** Bernd Frauenknecht, Emma Cramer, Artur Eisele 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is an exciting concept as well as a remarkable success story worth sharing. However, RL builds on rather complex interactions between different objects that play out over several cycles. Such dynamics are often best explained with an easily accessible implementation. We present RLLBC-Lib, a carefully crafted code library with the goal of lowering the entry barrier for students and other learners of RL in the context of learning-based control. At its heart, RLLBC-Lib comprises a comprehensive library of tabular RL approaches to enforce a clear understanding of the theoretical foundations. A deep RL library follows the same design principles, underscoring the parallels between simple tabular and state-of-the-art deep RL approaches. Additionally, RLLBC-Lib provides a collection of implementations illustrating core RL principles and contrasting RL to other learning-based control approaches. Finally, RLLBC-Lib provides an ideal basis for creating programming assignments with automated grading.

---


### 212. [Double descent is the principle of least action](https://arxiv.org/abs/2609.19076)

**<font color=#1a73e8>作者：</font>** Congzhou M Sha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The test error of a model plotted against its number of parameters $d$ falls, peaks when the model can just fit the training data, and falls again, exhibiting the double descent phenomenon. We explain the phenomenon with statistical mechanics. The training trajectory of a stochastic gradient-based method is a particle wandering over the energy landscape of the training loss at an induced temperature $T$, and a run that has equilibrated visits every parameter vector of a given training loss equally often, the fundamental postulate of statistical mechanics, with probability given by the Boltzmann distribution. Because training starts at an initial point and has only finite time to diffuse, it carries an effective weight decay, which makes every parameter a quadratic degree of freedom. The equipartition theorem then distributes the energy among the $d$ degrees of freedom in shares of $T/2$, so at a fixed training loss adding parameters lowers the temperature and drives the Boltzmann distribution toward the stationary path. Finally, adding parameters can only lower the $L^2$ norm of the stationary path, so a solution sampled at fixed loss is less likely to be large with increasing $d$, effectively increasing weight regularization.

---


### 213. [Probabilistic Linear Explanations](https://arxiv.org/abs/2609.19077)

**<font color=#1a73e8>作者：</font>** Frederic Koriche, Jean-Marie Lagniez, Chi Tran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Formal explainability provides mathematically grounded justifications for individual predictions. However, abductive explanations often exceed human cognitive limits by involving too many features, while probabilistic relaxations have remained largely limited to categorical classification. We present a unified framework for probabilistic explainability based on sparse, anchored linear models, applicable to both binary classification and continuous regression. By mapping instances to the Boolean hypercube, our linear explanations strictly generalize subset-based approaches: they capture both the magnitude and direction of feature contributions while enforcing a prescribed sparsity budget $k$. We show that minimizing the relevance error for such explanations is \ClassNPPP-hard when the underlying model is a neural network, and we relate this intractable objective to a tractable surrogate---the fidelity error. For a parameterized family of local distributions, the relevance error of any $k$-sparse explanation is bounded by its fidelity error up to a multiplicative factor that remains small locally. We address the resulting empirical problem using two complementary approaches: a Mixed Integer Programming (MIP) formulation that yields provably optimal empirical solutions while maintaining polynomial sample complexity, and a polynomial-time Iterative Hard Thresholding (IHT) algorithm with provable approximation guarantees. Empirical evaluations show that, unlike state-of-the-art baselines such as LIME and MAPLE, our explanations satisfy both the anchoring and sparsity constraints by construction, while consistently achieving lower relevance error.

---


### 214. [Reporting Practice Matters: The Impact of Reference Choice on Chest X-ray Report Evaluation](https://arxiv.org/abs/2609.19093)

**<font color=#1a73e8>作者：</font>** Daniel P. Jeong, Charles Q. Li, Hossein Hosseiny 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Radiologists follow heterogeneous reporting practices. Two radiologists examining the same image and identifying the same clinical findings might nevertheless compose superficially distinct reports, varying in terminology, shorthand, formatting, and level of detail. These variations in reporting norms represent an under-appreciated obstacle in efforts to evaluate AI-based radiology report generation (RRG) models, where machine-generated reports are typically assessed based on their concordance with human-generated references. In this paper, we quantify the sensitivity of established evaluation metrics to variations in reporting practices, revealing impacts large enough to alter the rankings of models. We introduce a radiologist-informed taxonomy of variations in radiology reporting practice and a method (ReRef) that rewrites reference reports along the axes of our taxonomy while preserving clinical interpretation. For instance, when comparing the performance of nine RRG models on MIMIC-CXR using RadCliQ-v1, condensing the discussion of normal findings in the reference reports causes Libra to drop from first to second place while CheXOne rises from third to first. Our results suggest that many current metrics fail to decouple clinical interpretation from conformity to reporting practices and that choosing the ``right'' references that accurately reflect the desired reporting practices can be important in practice. To support future research, we release MIMIC-CXR-Ext-ReRef, a radiologist-validated dataset of 120 (original, alternative) reference report pairs derived from MIMIC-CXR.

---


### 215. [Evidence-Grounded Agentic Formulation Development in an Autonomous Laboratory](https://arxiv.org/abs/2609.19099)

**<font color=#1a73e8>作者：</font>** Michael M. Craig, Riley J. Hickman, Yingshan Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-emulsifying drug delivery systems (SEDDS) can improve the oral bioavailability of poorly soluble drugs, but identifying high-performing formulations remains experimentally intensive. We present Andromeda 2, an agentic system that reasons over structured in-house experimental evidence and invokes computational and experimental tools to design and execute successive formulation batches. Using a miniaturized automated laboratory at a matched budget, we benchmark it against Andromeda 1, a probabilistic optimization model deployed across dozens of live development projects, and a wet-lab design-of-experiments (DoE) campaign. For paclitaxel, Andromeda 2 achieved a 50% high-performance hit rate versus 17% for Andromeda 1 and 2% for DoE, and identified 12 formulations meeting all four target product profile (TPP) objectives versus 6 and 0, respectively. Median $AUC_{10-240}$ was 70.1, 12.0, and 3.5 mg$\cdot$min/mL, while maximum AUC was comparable between Andromeda 2 and Andromeda 1. A selected full-TPP formulation achieved an apparent effective paclitaxel loading of $19 \pm 5\%$ w/w at the first FaSSIF measurement, approximately 3.3-fold higher than the 5.7% w/w loading reported for a published paclitaxel S-SEDDS. A controlled ablation showed that access to structured in-house experimental evidence increased mean AUC by 34%.

---


### 216. [Characterizing Network Centralization and Observability in the Remote MCP Ecosystem](https://arxiv.org/abs/2609.19100)

**<font color=#1a73e8>作者：</font>** Muhammad Abdullah Sohail  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) has emerged as the dominant interface for connecting autonomous agents to external data sources and execution environments. The ecosystem's transition from local process execution to remote Streamable HTTP deployments introduces unmeasured architectural and security constraints at scale. This paper presents a three-tier observability framework comprising catalog metadata (O_0), passive compliance signals (O_1), and live vulnerability analysis (O_2), applied to empirically characterize the public MCP server ecosystem. Evaluation of a stratified sample of 179 remote endpoints across two primary public registries reveals significant infrastructural consolidation. The Herfindahl-Hirschman Index (HHI) computed over the Autonomous System Number (ASN) distribution yields a value of 0.736, well above the 0.25 threshold for a highly concentrated market. Analysis further indicates that server authentication is strongly correlated with hosting platform choice rather than individual operator configuration, with 95\% of commercial PaaS-hosted servers enforcing gateway-level OAuth 2.1 with PKCE. The empirical results identify a Security-Observability Tradeoff observed in the current ecosystem: the platform-level authentication mechanisms that secure the majority of servers simultaneously limit automated vulnerability scanning capabilities, constraining the ability of AI gateway operators to assess tool-poisoning vectors without prior credential provisioning.

---


### 217. [Analog Pin Directionality as an Exfiltration Attack Surface in Mixed-Signal ICs](https://arxiv.org/abs/2609.19111)

**<font color=#1a73e8>作者：</font>** Ramana Ranganatham, Chirag Adiga, Michael Zuzak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mixed-signal SoCs rely on nominally input-only analog pins to acquire off-chip signals, but the directionality of these interfaces is generally treated as a functional property rather than explicitly verified as a security property. This work identifies and experimentally demonstrates a directionality-based class of analog and mixed-signal (AMS) exfiltration attacks in which data-dependent circuit-offset modulation converts a nominally input-only pin into an outbound information channel. We analytically model the attack mechanism and identify three enabling host conditions: a closed-loop amplifier, an exposed amplifier input, and sufficiently high impedance at that pin. This attack class is validated through a representative silicon case study using a photoplethysmography (PPG) analog front-end (AFE) fabricated in a commercial 55-nm CMOS process. The payload incurs $<$0.001\% area overhead relative to typical biosensing AFEs. Under the evaluated conditions, payload activation reduces the filtered PPG-output SNR by only 0.03~dB, while the maximum HT-induced perturbation of 5.9\% of the PPG amplitude remains within the 34.3\% benign variation at the exposed sensor-input pin across process and temperature. The raw exfiltration SINR remains below -20~dB, while targeted filtering increases it above 14~dB and enables signal recovery. Silicon measurements demonstrate data exfiltration through the input pin at bit rates up to 10~kbps and error-free recovery of a PRBS message. These results expose a conventional test-observability gap and establish analog pin directionality as an AMS security property requiring explicit verification, test coverage, and defense rather than being inferred from nominal signal flow.

---


### 218. [Track, Articulate, Act: Generating Articulation from Casual Human Videos](https://arxiv.org/abs/2609.19119)

**<font color=#1a73e8>作者：</font>** Jiaming Zhang, Homanga Bharadhwaj  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human videos contain rich causal evidence for robot manipulation: they reveal how hand motion induces object motion and produces task-relevant changes in object state. In this work, we study articulated objects such as doors, drawers, cabinets, laptops, ovens, and hinged containers that are ubiquitous in daily life and present unique challenges for embodied interaction. These objects cannot be represented by a single pose; their motion depends on the underlying parts and joints. We introduce a real-to-sim framework that reconstructs a simulation-ready articulated object and hand-object interaction from a casual monocular RGB video, without RGB-D or multi-view input, prior scans, manually specified joints, or robot demonstrations. Our key insight is that dense 3D point tracks provide an embodiment-agnostic articulation cue: points on the fixed link remain approximately stationary, while points on the moving link follow coherent revolute or prismatic motion. Our method segments the links, estimates the joint and its state trajectory, reconstructs an articulated asset, and aligns the recovered 3D hand motion with the object. Central to our approach is a modular recipe that repurposes powerful pretrained models for single-image 3D reconstruction, mesh segmentation, and 3D scene flow, connecting their predictions through explicit geometric reasoning to infer articulation. We use the reconstructed articulated object and the human hand trajectory to replay interactions through contact in MuJoCo. The framework shows how pretrained vision models and explicit motion reasoning can turn casual human videos into articulated object models suitable for downstream embodied interactions. this https URL

---


### 219. [Adaptive Convolutional Sparse Coding via Information Bottleneck for Robust Visual Signal Representation](https://arxiv.org/abs/2609.19122)

**<font color=#1a73e8>作者：</font>** Meng'en Qin, Yinchen Liu, Mingxuan Cui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual signals require compact yet sufficient representations for robust downstream prediction. Convolutional sparse coding (CSC) provides an explicit mechanism for suppressing redundant components while preserving signal content, but its sparsity coefficient is typically fixed and manually selected. We propose an adaptive convolutional sparse coding framework for robust visual signal representation. Specifically, we unfold the CSC optimization with the Fast Iterative Shrinkage-Thresholding Algorithm (FISTA) and treat the sparsity coefficient as a differentiable variable jointly learned with the network parameters. From the information bottleneck perspective, this coefficient controls the trade-off between information retention and compression: the sparsity term promotes compact representations, while the reconstruction term together with task loss preserves task-relevant signal content. We further introduce a label-free post-training strategy that adjusts the compression strength for corrupted inputs with the main network parameters fixed. Experiments on CIFAR and ImageNet demonstrate competitive clean-data recognition and greatly improved robustness under different input perturbations.

---


### 220. [Flag Game: A Toy Model for Mechanistic Swarm Interpretability](https://arxiv.org/abs/2609.19124)

**<font color=#1a73e8>作者：</font>** Elizabeth Pavlova, Hidenori Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emergent coordinated behaviors of AI agents are starting to present critical safety risks. A key phenomenon driving these behaviors is the rapid formation and spread of beliefs about the world, and mechanistic understanding is crucial for collective alignment. To this end, we introduce the Flag Game, a toy model for studying the mechanisms of collective belief formation. Concretely, a hidden country flag defines the ground truth, and each bounded agent directly observes only a private crop but can exchange beliefs and weigh social evidence from peers. Despite its simplicity, the Flag Game reproduces rich collective phenomenology: non-monotonic scaling of performance with population size, accuracy gains from social-awareness prompting and team diversity, and strong effects of organizational structure. In particular, we identify that collective belief collapse at small population sizes turns into collective belief polarization as the population grows. This polarization causes the performance decline at large population sizes, but creates diversity in collective beliefs. Finally, we dissect the mechanisms underlying collective belief collapse and polarization with two complementary approaches. We first introduce social circuit attribution, a technique to predict which agent, and what view, matters most to collective dynamics, and verify its predictions by causal interventions on agents, tracing how agent patching changes collective outcomes. However, the efficacy of causal interventions on agents decreases as the population grows. We therefore develop a statistical mechanical theory for larger populations and verify that it matches the empirical phase diagram. Together, these results take a first step toward mechanistic swarm interpretability, a science of how the properties of individual agents and their communication give rise to emergent collective behavior.

---


### 221. [ScienceIDE: Turning World's Scientific Codebase into Agent Learnable Environments](https://arxiv.org/abs/2609.19134)

**<font color=#1a73e8>作者：</font>** Hejia Geng, Zesen Huang, Haoyang Li 等 45 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific code repositories encode decades of human knowledge in executable models, methods, and tools. Yet fragmented toolchains, implicit domain conventions, and specialized correctness criteria make this knowledge difficult to convert into reliable learning experience-a challenge we call the scientific experience bottleneck. We introduce ScienceIDE, infrastructure for turning the world's scientific code into programmable environments for scientific agents. Guided by expert-defined scientific cases and acceptance criteria, agents transform repositories into executable environments that support task generation, execution, and scientific verification. These environments provide a shared foundation for supervised fine-tuning, reinforcement learning, and evaluation. Using verified interaction trajectories, we train PhAI-IDE-72B, PhAI-IDE-9B, and PhAI-IDE-4B. The model family shows gains in held-out scientific-code repair and across selected general-purpose benchmarks in code, reasoning, and knowledge, providing evidence of positive transfer from scientific experience to broader capabilities. ScienceIDE lays the foundation for an integrated workspace for agent learning and scientific practice, making humanity's scientific software a shared substrate for developing scientific intelligence. Code: this https URL

---


### 222. [Exponential Hardness of Off-Policy Evaluation under History-Dependent Logging](https://arxiv.org/abs/2609.19135)

**<font color=#1a73e8>作者：</font>** Pranaya Jajoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a logged dataset visit every hidden state frequently and still be exponentially uninformative about a target policy's value? We show that it can when the logger depends on history. For every horizon $H \ge 3$, we construct two POMDPs with at most two latent states per stage, three actions, and a common logger with three memory states. Action coverage, belief coverage, and two behavior-marginal outcome-revealing conditions all have constants independent of $H$. Nevertheless, evaluating a known deterministic target policy to accuracy $1/8$ requires $\Theta((3/2)^H \log(1/\delta))$ logged episodes at confidence $1-\delta$, for $0 < \delta \le 1/4$, even when both candidate models are known. The mechanism is simple: a reset erases the unknown transition that determines the target value. We characterize the resulting statistical experiment exactly and obtain a matching optimal estimator. A directed two-lane gridworld realizes the construction, and trajectory simulations agree with its finite-sample prediction. The result establishes intractability for the history-dependent-logging, model-based case posed by Zhang and Jiang (2025, arXiv:2503.01134), under their behavior-marginal definition of revealing.

---


### 223. [PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics](https://arxiv.org/abs/2609.19142)

**<font color=#1a73e8>作者：</font>** Bardienus P. Duisterhof, Kaifeng Zhang, Adam Hung 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models endow perceptual systems with the ability to predict how scenes evolve under interaction. They are most beneficial when trained on diverse volumes of data, to instill a rich prior into downstream applications. Existing methods typically require robot action labels to learn action-conditioned 3D dynamics, which excludes web video data from the training pool. We study 3D point track completion as a pre-training objective for learning transferable 3D dynamics without robot data. Given a single RGB-D observation and sparse partial 3D trajectories (tracks), we predict future 3D tracks of all observed points. We show this objective produces a rich 3D dynamics prior, without requiring robot action labels. We contribute a diverse dataset of 2.9 million synthetic frames spanning deformable, articulated, and rigid objects, and use it to train PointZero. We show that a flexible and expressive transformer, PointZero, outperforms prior methods on the same data. We demonstrate the utility of our pre-training objective by post-training PointZero for two downstream applications: (1) action-conditioned 3D dynamics prediction and (2) imitation learning. When fine-tuned to condition on end-effector pose, PointZero outperforms the baselines on the recent PGND 3D dynamics benchmark. When fine-tuned to predict robot actions and 3D tracks, PointZero outperforms or matches the baselines on 6/7 simulated and real-world robot manipulation tasks. We furthermore evaluate training PointZero from scratch to isolate the benefits of our proposed architecture from those of our proposed pre-training objective and dataset. We release the dataset, checkpoints, and full training recipe.

---


> [!TIP]
> 当前位于：**201-223**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-223**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
